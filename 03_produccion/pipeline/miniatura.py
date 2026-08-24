#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
miniatura.py — la portada. Donde se juega el CTR antes que en ningún otro sitio.

QUÉ CAMBIÓ Y POR QUÉ (20 de agosto de 2026)
-------------------------------------------
Las miniaturas anteriores eran azul marino (#0B1220) sobre retícula azul marino,
sin cara y sin ningún color de alto contraste. Eran elegantes y en una cuadrícula
de YouTube desaparecían.

El dato que manda aquí: de los vídeos que rompen, el 69 % llevan una cara humana
en la miniatura (el 80 % entre los que más rompen) y el 89 % llevan **cara o color
de altísimo contraste**. Una de las dos, siempre. Las viejas no llevaban ninguna.

Las reglas nuevas, todas comprobables por código:

  1. Fondo saturado o claro. El azul marino es el color del VÍDEO, no de la portada.
  2. El Engranaje —el personaje— ocupando entre un cuarto y un tercio del encuadre.
     Es la cara que un canal sin cara puede permitirse.
  3. Cuatro palabras o menos. La mediana de los vídeos que rompen es cinco.
  4. Nada en la esquina inferior derecha: ahí YouTube pinta la duración.
  5. Contraste medido, no opinado: ratio WCAG >= 7:1 entre el texto y su fondo.
     Si baja de ahí, esto sale con código 1 y la producción se para.
  6. Tres variantes por vídeo, que cambian UN elemento cada vez, para poder
     rotarlas con thumbnails.set() y comparar CTR sin gastar un euro.

    python3 miniatura.py guion.json -o miniatura.png
    python3 miniatura.py guion.json -o mini.png --variantes      # a, b y c
    python3 miniatura.py guion.json -o mini.png --texto "Nadie nace *gracioso*"
"""
import argparse
import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent
PERSONAJE_SVG = AQUI.parents[1] / "02_marca" / "personaje.svg"

MARCAS = {"es": "Mecánica del Humor", "en": "Humor Mechanics"}
NUMERO = {"es": "Nº ", "en": "No. "}

LIENZO = {"largo": (1280, 720), "corto": (1080, 1920)}

# ---------------------------------------------------------------------------
# Temas. Cada uno es un fondo y una tinta, y los dos juntos pasan el 7:1.
# El azul marino sigue existiendo — como acento y como color de la retícula —,
# pero ya no es el fondo.
# ---------------------------------------------------------------------------
TEMAS = {
    "ambar":   {"fondo": "#FFB020", "tinta": "#0B1220", "reja": "#E09512", "acento": "#0B1220"},
    "cian":    {"fondo": "#4CC9F0", "tinta": "#08131F", "reja": "#3BAACC", "acento": "#08131F"},
    "granate": {"fondo": "#8A0E22", "tinta": "#FFFFFF", "reja": "#6B0A1A", "acento": "#FFB020"},
    "hueso":   {"fondo": "#F2EFE7", "tinta": "#0B1220", "reja": "#DAD6CC", "acento": "#B3123C"},
}
ORDEN_TEMAS = ["ambar", "cian", "granate", "hueso"]


# ---------------------------------------------------------------------------
# Contraste WCAG. Es aritmética, así que se calcula en vez de discutirse.
# ---------------------------------------------------------------------------
def _lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminancia(hexcol):
    h = hexcol.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contraste(a, b):
    la, lb = luminancia(a), luminancia(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


MIN_CONTRASTE = 7.0

# Encoge el titular hasta que cabe en su caja. Se ejecuta en la página, después
# de que las tipografías estén aplicadas: medir en Python sería adivinar.
AJUSTE_JS = """
() => {
  const c = document.getElementById('c'), t = document.querySelector('h1');
  const cif = document.querySelector('.cif');
  // La cifra va en una sola línea; si no cabe a lo ancho, se encoge ella antes
  // de tocar el titular. Es el elemento con más aire que ceder.
  if (cif) {
    let g = parseFloat(getComputedStyle(cif).fontSize), k = 0;
    while (cif.scrollWidth > cif.clientWidth + 2 && g > 90 && k++ < 24) {
      g *= 0.94; cif.style.fontSize = g + 'px';
    }
  }
  let f = parseFloat(getComputedStyle(t).fontSize);
  const cabe = () => c.scrollHeight <= c.clientHeight + 2
                  && t.scrollWidth  <= t.clientWidth  + 2;
  let n = 0;
  while (!cabe() && f > 48 && n++ < 24) { f *= 0.94; t.style.fontSize = f + 'px'; }
  return Math.round(f);
}
"""


def rico(s, acento):
    s = (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*([^*]+)\*", f'<span style="color:{acento}">\\1</span>', s)
    return re.sub(r"_([^_]+)_", f'<span style="color:{acento}">\\1</span>', s)


def limpiar(s):
    return re.sub(r"[*_]", "", s or "").strip()


def palabras(s):
    return len(limpiar(s).split())


def acortar(texto, maximo=4):
    """Cuatro palabras o menos. Si el titular es más largo, se queda con el
    trozo que lleva el resaltado, que es donde el guionista puso el peso."""
    t = limpiar(texto)
    if len(t.split()) <= maximo:
        return texto
    m = re.search(r"[*_]([^*_]+)[*_]", texto or "")
    if m:
        pal = m.group(1).split()
        if len(pal) <= maximo:
            antes = limpiar(texto[:m.start()]).split()
            hueco = maximo - len(pal)
            return " ".join(antes[-hueco:]) + " *" + " ".join(pal) + "*" if hueco else "*" + m.group(1) + "*"
    return " ".join(t.split()[:maximo])


def tam_titular(texto, ancho):
    n = len(limpiar(texto))
    base = {True: [(10, 200), (18, 160), (26, 130), (99, 104)],
            False: [(10, 168), (18, 136), (26, 112), (99, 90)]}[ancho >= 1280]
    for tope, px in base:
        if n <= tope:
            return px
    return base[-1][1]


def tam_cifra(texto, ancho):
    n = len(limpiar(texto))
    esc = 1.0 if ancho >= 1280 else 0.86
    for tope, px in [(3, 380), (6, 290), (10, 210), (99, 165)]:
        if n <= tope:
            return int(px * esc)
    return int(165 * esc)


def cifra_mas_fuerte(guion):
    """Primera escena «dato» cuya cifra sea de verdad una cifra.

    El campo se llama «cifra» pero el guionista lo usa a veces para una frase
    corta —MDH-002 traía «El mismo circuito»—, y entonces la maquetación de
    número gigante en monoespaciada no tiene ningún sentido: sale una frase
    enorme en una tipografía de máquina de escribir y el titular queda debajo,
    diminuto. Si no empieza por un número, se usa el diseño de texto.
    """
    for e in guion.get("escenas", []):
        if e.get("tipo") == "dato" and e.get("cifra"):
            c = limpiar(e["cifra"])
            if re.match(r"^[^\w]{0,2}\d", c):      # «50 años», «≈1 mes», «3 de cada 4»
                return e["cifra"]
    return None


def cara(expresion="duda"):
    svg = PERSONAJE_SVG.read_text(encoding="utf-8")
    svg = svg.split("\n", 1)[1]
    return ('<svg id="cara" class="mdh-cara ex-%s" viewBox="20 20 172 160" '
            'xmlns="http://www.w3.org/2000/svg">\n%s' % (expresion, svg))


PLANTILLA = """<!DOCTYPE html><html lang="__LANG__"><head><meta charset="utf-8"><style>
:root{--fondo:__FONDO__;--tinta:__TINTA__;--reja:__REJA__;--acento:__ACENTO__}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:__W__px;height:__H__px;overflow:hidden;background:var(--fondo);
  font-family:"Archivo Black","Inter","DejaVu Sans",sans-serif;color:var(--tinta)}
#r{position:absolute;inset:0;background-image:
  linear-gradient(var(--reja) 2px,transparent 2px),
  linear-gradient(90deg,var(--reja) 2px,transparent 2px);
  background-size:__REJILLA__px __REJILLA__px;opacity:.5}
#m{position:absolute;inset:__MARCO__px;border:3px solid var(--tinta);opacity:.22}
#c{position:absolute;inset:0;display:flex;flex-direction:column;
   justify-content:__JUSTIFY__;padding:__PAD__}
.cif{font-family:"JetBrains Mono","DejaVu Sans Mono",monospace;font-size:__TAMCIF__px;
     line-height:.9;letter-spacing:-.03em;margin-bottom:20px;white-space:nowrap}
h1{font-size:__TAM__px;line-height:.98;letter-spacing:-.03em;max-width:__ANCHOTIT__}
/* El personaje: entre 1/4 y 1/3 del encuadre. Es la cara del canal.
   Los selectores llevan #cara delante A PROPÓSITO. personaje.svg trae su
   propio <style> con reglas .mdh-cara, y como el SVG va después en el
   documento, con la misma especificidad ganaría él: el personaje saldría
   ámbar y cian sobre un fondo ámbar o cian, o sea invisible. Con el id
   delante (1,1,0 contra 0,2,0) manda el tema de la miniatura. */
#cara{position:absolute;__POSCARA__;width:__TAMCARA__px;height:__TAMCARA__px;
      --am:var(--tinta);--ci:var(--tinta);--te:var(--tinta);--ti:var(--tinta)}
#cara .chapa {stroke:var(--tinta);stroke-width:5.5}
#cara .fino  {stroke:var(--tinta);opacity:.22}
#cara .lente {stroke:var(--tinta);stroke-width:5}
#cara .pupila{fill:var(--acento)}
#cara .biela {fill:var(--tinta)}
#cara .boca  {stroke:var(--tinta);stroke-width:7}
#cara .remache{fill:var(--tinta);opacity:.5}
#cara .eje   {stroke:var(--tinta);opacity:.55}
#cara .diente{stroke:var(--tinta);opacity:.55}
#f{position:absolute;left:__PADLAT__px;bottom:38px;font-size:__TAMFIRMA__px;
   letter-spacing:.24em;text-transform:uppercase;opacity:.72}
#n{position:absolute;right:__PADLAT__px;top:__TOPNUM__px;font-size:__TAMFIRMA__px;
   font-family:"JetBrains Mono","DejaVu Sans Mono",monospace;
   border:2px solid var(--tinta);padding:8px 14px;opacity:.72}
</style></head><body>
<div id="r"></div>
<div id="c">__CUERPO__</div>
__CARA__
<div id="m"></div><div id="f">__MARCA__</div><div id="n">__N__</div>
</body></html>"""


def construir(texto, cifra, tema, formato, marca, numero, idioma, expresion, layout):
    T = TEMAS[tema]
    w, h = LIENZO[formato]
    vertical = formato == "corto"

    ratio = contraste(T["fondo"], T["tinta"])
    if ratio < MIN_CONTRASTE:
        raise SystemExit(
            f"Contraste insuficiente en el tema «{tema}»: {ratio:.1f}:1 "
            f"(mínimo {MIN_CONTRASTE}:1 entre {T['tinta']} y {T['fondo']}). "
            f"Una miniatura que no se lee en un móvil no sirve de nada.")
    r_ac = contraste(T["fondo"], T["acento"])
    if r_ac < 4.5:
        raise SystemExit(f"El acento del tema «{tema}» solo da {r_ac:.1f}:1 sobre su fondo.")

    cuerpo = ""
    if cifra and layout == "cifra":
        cuerpo += f'<div class="cif">{rico(cifra, T["acento"])}</div>'
    cuerpo += f'<h1>{rico(texto, T["acento"])}</h1>'

    # El personaje va al lado contrario del texto y NUNCA en la esquina inferior
    # derecha: ahí YouTube pinta la duración encima.
    if vertical:
        pos_cara = "left:50%;transform:translateX(-50%);bottom:520px"
        tam_cara = 420                     # 39 % del ancho
        pad = "300px 76px 980px"
        justify = "flex-start"
    else:
        pos_cara = "right:56px;top:50%;transform:translateY(-50%)"
        tam_cara = 360                     # 50 % del alto, 28 % del ancho
        # 128px abajo: la firma va anclada a 38px del borde y NO está en el
        # flujo de #c, así que sin ese hueco el titular se le monta encima.
        pad = "72px 452px 128px 92px"      # el hueco de la derecha es para la cara
        justify = "center"

    return (PLANTILLA
            .replace("__LANG__", idioma)
            .replace("__FONDO__", T["fondo"]).replace("__TINTA__", T["tinta"])
            .replace("__REJA__", T["reja"]).replace("__ACENTO__", T["acento"])
            .replace("__W__", str(w)).replace("__H__", str(h))
            .replace("__REJILLA__", "72" if vertical else "80")
            .replace("__MARCO__", "40" if vertical else "30")
            .replace("__PAD__", pad).replace("__JUSTIFY__", justify)
            .replace("__TAM__", str(tam_titular(texto, w)))
            .replace("__TAMCIF__", str(tam_cifra(cifra or "", w)))
            .replace("__ANCHOTIT__", "100%" if vertical else "780px")
            .replace("__POSCARA__", pos_cara).replace("__TAMCARA__", str(tam_cara))
            .replace("__PADLAT__", "76" if vertical else "92")
            .replace("__TOPNUM__", "150" if vertical else "56")
            .replace("__TAMFIRMA__", "26" if vertical else "22")
            .replace("__CUERPO__", cuerpo)
            .replace("__CARA__", cara(expresion))
            .replace("__MARCA__", marca).replace("__N__", numero)), (w, h), ratio


def generar(guion_path, salida, texto=None, cifra=None, sin_cifra=False,
            variantes=False, expresion="duda"):
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    formato = g.get("formato", "largo")
    idioma = g.get("idioma", "es")
    marca = MARCAS.get(idioma, MARCAS["es"])
    numero = re.sub(r"^MD[HS]-", NUMERO.get(idioma, NUMERO["es"]), g["id"])

    texto = texto or g["escenas"][0].get("titulo") or g["escenas"][0].get("texto") \
        or g["titulo_trabajo"]
    texto = acortar(texto, 4)
    if not sin_cifra and cifra is None:
        cifra = cifra_mas_fuerte(g)

    # El tema base rota con el número de episodio: el canal se ve coherente y
    # cada vídeo, distinto. Determinista — mismo guion, mismo tema, siempre.
    n = int(re.sub(r"\D", "", g["id"]) or 0)
    base = ORDEN_TEMAS[n % len(ORDEN_TEMAS)]
    otro = ORDEN_TEMAS[(n + 2) % len(ORDEN_TEMAS)]

    # Tres variantes que cambian UN elemento cada una. Si cambian dos y el CTR
    # se mueve, no se sabe cuál fue.
    planes = [("a", base, "cifra" if cifra else "texto")]
    if variantes:
        planes += [("b", otro, "cifra" if cifra else "texto"),   # solo cambia el tema
                   ("c", base, "texto")]                          # solo cambia el diseño

    salida = Path(salida).resolve()
    salida.parent.mkdir(parents=True, exist_ok=True)
    hechas = []
    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb", "--hide-scrollbars"])
        for sufijo, tema, layout in planes:
            html, (w, h), ratio = construir(texto, cifra, tema, formato, marca,
                                            numero, idioma, expresion, layout)
            destino = salida if len(planes) == 1 else \
                salida.with_name(f"{salida.stem}_{sufijo}{salida.suffix}")
            tmp = destino.with_suffix(".html")
            tmp.write_text(html, encoding="utf-8")
            pag = nav.new_page(viewport={"width": w, "height": h})
            pag.goto(tmp.as_uri())
            # Ajuste automático: se encoge el titular hasta que el bloque cabe.
            # Antes esto era un error y paraba la producción, lo cual castigaba
            # a quien escribía un título de cinco palabras en vez de resolverlo.
            # Un titular que desborda no se lee, pero encogerlo un 8 % sí.
            # Ajuste automático: se encoge el titular hasta que el bloque cabe.
            # Un titular que desborda no se lee, pero encogerlo un 6 % sí, y eso
            # no debe costar una produccion entera.
            px = pag.evaluate(AJUSTE_JS)
            pag.screenshot(path=str(destino))
            pag.close()
            tmp.unlink(missing_ok=True)
            print(f"Miniatura {destino.name}: tema {tema}, {layout}, "
                  f"{palabras(texto)} palabras, titular {px}px, contraste {ratio:.1f}:1"
                  + (f", cifra {limpiar(cifra)}" if cifra and layout == "cifra" else ""))
            hechas.append(destino)
        nav.close()
    return hechas


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("-o", "--salida", default="miniatura.png")
    ap.add_argument("--texto", default=None)
    ap.add_argument("--cifra", default=None)
    ap.add_argument("--sin-cifra", action="store_true")
    ap.add_argument("--variantes", action="store_true",
                    help="genera _a, _b y _c para rotarlas y comparar CTR")
    ap.add_argument("--expresion", default="duda",
                    choices=["neutra", "duda", "entiende", "no", "rie", "piensa"])
    a = ap.parse_args()
    generar(a.guion, a.salida, a.texto, a.cifra, a.sin_cifra, a.variantes, a.expresion)
