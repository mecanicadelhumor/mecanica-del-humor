#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
miniatura.py — genera la miniatura 1280x720 con la fórmula de marca.

La miniatura de Mecánica del Humor debe parecer la figura de un paper, no un
clickbait: fondo oscuro, retícula, y un solo acento ámbar señalando el punto
clave. Se genera desde el mismo motor de escenas, así que nunca se desvía de
la identidad del canal.

Si el guion tiene alguna escena de tipo "dato" (una cifra que ya pasó por el
Verificador, con su fuente), esa cifra se convierte en el elemento dominante
de la miniatura — grande, en monoespaciada, con un titular corto de apoyo
debajo. Es la palanca con más impacto en CTR por menos esfuerzo: promete un
dato concreto y verificado, no una emoción fabricada. Si no hay ninguna
escena de dato, se usa el formato anterior (titular + pie).

    python3 miniatura.py guion.json -o miniatura.png
    python3 miniatura.py guion.json -o m.png --texto "Nadie nace *gracioso*" --pie "Hay datos"
    python3 miniatura.py guion.json -o m.png --sin-cifra   # fuerza el formato de texto
"""
import argparse
import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent

# Nombre del canal y forma de numerar el episodio, por idioma. En inglés "Nº"
# no se usa: lo natural es "No.".
MARCAS = {"es": "Mecánica del Humor", "en": "Humor Mechanics"}
NUMERO = {"es": "Nº ", "en": "No. "}

HTML_TEXTO = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
:root{--fondo:#0B1220;--reticula:#16213A;--tinta:#F2F4F8;--tenue:#8A97AE;--ambar:#FFB020;--cian:#4CC9F0}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1280px;height:720px;overflow:hidden;background:var(--fondo);
  font-family:"Archivo Black","Inter","DejaVu Sans",sans-serif;color:var(--tinta)}
#r{position:absolute;inset:0;background-image:
  linear-gradient(var(--reticula) 1px,transparent 1px),
  linear-gradient(90deg,var(--reticula) 1px,transparent 1px);background-size:64px 64px;opacity:.6}
#v{position:absolute;inset:0;background:radial-gradient(ellipse at 46% 44%,transparent 30%,rgba(0,0,0,.6) 100%)}
#m{position:absolute;inset:34px;border:1px solid rgba(242,244,248,.12)}
#m::before{content:"";position:absolute;top:-1px;left:-1px;width:26px;height:26px;
  border:3px solid rgba(255,176,32,.6);border-right:0;border-bottom:0}
#c{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:86px 96px}
h1{font-size:__TAM__px;line-height:.98;letter-spacing:-.025em}
.amb{color:var(--ambar)} .cia{color:var(--cian)}
#p{margin-top:34px;font-size:30px;color:var(--tenue);font-family:"Inter","DejaVu Sans",sans-serif;
  font-weight:500;letter-spacing:.02em;max-width:78%}
#f{position:absolute;left:96px;bottom:52px;font-size:19px;letter-spacing:.26em;
  text-transform:uppercase;color:var(--tenue)}
#n{position:absolute;right:88px;top:74px;font-size:22px;color:var(--ambar);
  font-family:"JetBrains Mono","DejaVu Sans Mono",monospace;border:1px solid rgba(255,176,32,.5);padding:8px 14px}
</style></head><body>
<div id="r"></div><div id="c"><h1>__T__</h1><div id="p">__P__</div></div>
<div id="v"></div><div id="m"></div><div id="f">__MARCA__</div><div id="n">__N__</div>
</body></html>"""

HTML_CIFRA = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
:root{--fondo:#0B1220;--reticula:#16213A;--tinta:#F2F4F8;--tenue:#8A97AE;--ambar:#FFB020;--cian:#4CC9F0}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1280px;height:720px;overflow:hidden;background:var(--fondo);
  font-family:"Archivo Black","Inter","DejaVu Sans",sans-serif;color:var(--tinta)}
#r{position:absolute;inset:0;background-image:
  linear-gradient(var(--reticula) 1px,transparent 1px),
  linear-gradient(90deg,var(--reticula) 1px,transparent 1px);background-size:64px 64px;opacity:.6}
#v{position:absolute;inset:0;background:radial-gradient(ellipse at 46% 44%,transparent 30%,rgba(0,0,0,.6) 100%)}
#m{position:absolute;inset:34px;border:1px solid rgba(242,244,248,.12)}
#m::before{content:"";position:absolute;top:-1px;left:-1px;width:26px;height:26px;
  border:3px solid rgba(255,176,32,.6);border-right:0;border-bottom:0}
#c{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:70px 96px}
.cif{font-family:"JetBrains Mono","IBM Plex Mono","DejaVu Sans Mono",monospace;
  font-size:__TAMCIF__px;line-height:.85;letter-spacing:-.02em;color:var(--ambar)}
h1{font-size:__TAM__px;line-height:1.08;letter-spacing:-.02em;margin-top:26px;max-width:94%}
.amb{color:var(--ambar)} .cia{color:var(--cian)}
#f{position:absolute;left:96px;bottom:52px;font-size:19px;letter-spacing:.26em;
  text-transform:uppercase;color:var(--tenue)}
#n{position:absolute;right:88px;top:74px;font-size:22px;color:var(--ambar);
  font-family:"JetBrains Mono","DejaVu Sans Mono",monospace;border:1px solid rgba(255,176,32,.5);padding:8px 14px}
</style></head><body>
<div id="r"></div><div id="c"><div class="cif">__CIF__</div><h1>__T__</h1></div>
<div id="v"></div><div id="m"></div><div id="f">__MARCA__</div><div id="n">__N__</div>
</body></html>"""


def rico(s):
    s = (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*([^*]+)\*", r'<span class="amb">\1</span>', s)
    return re.sub(r"_([^_]+)_", r'<span class="cia">\1</span>', s)


def tamano(texto):
    n = len(re.sub(r"[*_]", "", texto or ""))
    if n <= 16:  return 128
    if n <= 26:  return 104
    if n <= 38:  return 86
    return 72


def tamano_cifra(texto):
    n = len(re.sub(r"[*_]", "", texto or ""))
    if n <= 3:   return 340
    if n <= 6:   return 260
    if n <= 10:  return 190
    return 150


def tamano_apoyo(texto):
    # El titular es de apoyo aquí, no el protagonista, así que va más contenido.
    n = len(re.sub(r"[*_]", "", texto or ""))
    if n <= 30:  return 68
    if n <= 50:  return 56
    return 46


def cifra_mas_fuerte(guion):
    """Primera escena de tipo "dato" del guion — ya pasó por el Verificador,
    así que la cifra viene con fuente detrás. None si el guion no tiene ninguna."""
    for e in guion.get("escenas", []):
        if e.get("tipo") == "dato" and e.get("cifra"):
            return e["cifra"]
    return None


def generar(guion_path, salida, texto=None, pie=None, cifra=None, sin_cifra=False):
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    primera = g["escenas"][0]
    texto = texto or primera.get("titulo") or g["titulo_trabajo"]

    if not sin_cifra and cifra is None:
        cifra = cifra_mas_fuerte(g)

    idioma = g.get("idioma", "es")
    marca = MARCAS.get(idioma, MARCAS["es"])
    numero = g["id"].replace("MDH-", NUMERO.get(idioma, NUMERO["es"]))

    if cifra:
        html = (HTML_CIFRA.replace("__CIF__", rico(cifra))
                           .replace("__T__", rico(texto))
                           .replace("__N__", numero)
                           .replace("__MARCA__", marca)
                           .replace("__TAMCIF__", str(tamano_cifra(cifra)))
                           .replace("__TAM__", str(tamano_apoyo(texto))))
    else:
        pie = pie or primera.get("subtitulo") or g.get("tesis", "")
        if len(pie) > 96:
            pie = pie[:93].rsplit(" ", 1)[0] + "…"
        html = (HTML_TEXTO.replace("__T__", rico(texto))
                          .replace("__P__", rico(pie))
                          .replace("__N__", numero)
                          .replace("__MARCA__", marca)
                          .replace("__TAM__", str(tamano(texto))))

    # Absoluta: Path.as_uri() (usado más abajo para abrir el HTML en el
    # navegador) exige sí o sí una ruta absoluta, si no falla con ValueError.
    salida = Path(salida).resolve()
    tmp = salida.with_suffix(".html")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb", "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": 1280, "height": 720})
        pag.goto(tmp.as_uri())
        pag.screenshot(path=str(salida))
        nav.close()
    tmp.unlink(missing_ok=True)
    print(f"Miniatura: {salida}" + (f"  (cifra: {cifra})" if cifra else ""))
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("-o", "--salida", default="miniatura.png")
    ap.add_argument("--texto", default=None)
    ap.add_argument("--pie", default=None)
    ap.add_argument("--cifra", default=None)
    ap.add_argument("--sin-cifra", action="store_true")
    a = ap.parse_args()
    generar(a.guion, a.salida, a.texto, a.pie, a.cifra, a.sin_cifra)
