#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_produccion/pipeline/muestrario_visual.py — C50, PRUEBA (versión 12 del plan, 23/09/2026).

Con lo que ha dejado `visual.py` en la carpeta de salida, monta para cada guion:

  · tres HOJAS DE CONTACTOS (una por variante), seis escenas en fila, con la
    frase de cada escena y la fuente de su imagen debajo. Van a `hojas/`, que
    sí se sube al repositorio: son JPG pequeños y es lo que se mira primero.
      A · vídeo de archivo detrás y la frase corta de la escena encima (el
          texto de siempre, sin el fondo azul);
      B · lo mismo, pero con subtítulos grandes de la narración en vez de la
          frase corta (los subtítulos quemados se apagaron el 20/08 porque
          competían con el texto de la escena; aquí no hay texto de escena con
          el que competir, y decide el codirector mirándolo);
      C · imágenes generadas en todas las escenas, con movimiento de cámara.
  · y una PREVIA EN VÍDEO de las variantes A y C, sin sonido, con los planos
    en movimiento y el texto encima. Van a `salida/`, que NO se sube al
    repositorio (pesan): se descargan del artefacto del workflow.

El texto lo pinta el motor de verdad, `03_produccion/pipeline/escena.html`,
con el fondo transparente. Lo único que cambia respecto a producción es el
fondo; así lo que se juzga es la imagen y no una maqueta.

Regla 11.2: esto es para MIRARLO antes de decidir. Nada de aquí llega a un
vídeo publicado.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(AQUI))
import render  # noqa: E402  (preparar() y ESCENA_HTML, los de producción)

GUIONES = RAIZ / "05_calendario" / "guiones"
PRUEBA = RAIZ / "07_pruebas" / "visual-23-09"
SALIDA = PRUEBA / "salida"   # lo cambia --salida
HOJAS = PRUEBA / "hojas"     # lo cambia --hojas
W, H = 1080, 1920
FPS = 30
TARJETAS = {"comparacion", "dato", "diagrama", "lista", "cita", "figura"}

# Lo único que se cambia del motor: el fondo desaparece, y lo que va encima de
# una imagen necesita un poco de sombra o una caja opaca para leerse.
CSS_SOBRE_IMAGEN = """
html,body{background:transparent !important}
#reticula,#vineta,#marco{display:none !important}
.enunciado,h1,h2,.sub,.cifra,.cifra-pie,.pie,blockquote,.autor{
  text-shadow:0 6px 28px rgba(0,0,0,.75),0 2px 6px rgba(0,0,0,.6)}
.panel,.pila .paso{background:rgba(11,18,32,.86) !important}
"""


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


# ---------------------------------------------------------------------------
# Capas
# ---------------------------------------------------------------------------
def capas_de_texto(guion, destino):
    """Un PNG transparente por escena con el texto tal como lo pinta
    producción, en el instante en que ya está asentado."""
    from playwright.sync_api import sync_playwright
    escenas = render.preparar(guion)
    destino.mkdir(parents=True, exist_ok=True)
    rutas = {}
    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb", "--font-render-hinting=none",
                                      "--disable-lcd-text", "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": W, "height": H})
        pag.goto(render.ESCENA_HTML.as_uri())
        pag.add_style_tag(content=CSS_SOBRE_IMAGEN)
        for e in escenas:
            pag.evaluate("d => cargar(d)", e)
            # C50: el Engranaje solo firma el cierre; en el resto de escenas, fuera.
            ultimo = e["n"] == len(escenas)
            pag.evaluate("v => { const c = document.getElementById('personaje');"
                         " if (c) c.style.visibility = v ? 'visible' : 'hidden'; }", ultimo)
            pag.evaluate("t => pintar(t)", e["duracion_s"] * 0.7)
            ruta = destino / f"texto_e{e['n']}.png"
            pag.screenshot(path=str(ruta), omit_background=True)
            rutas[e["n"]] = ruta
        nav.close()
    return rutas, escenas


def degradado():
    """Oscurece un poco todo y bastante la mitad de abajo: el texto se lee
    encima de cualquier imagen sin tapar la imagen."""
    capa = Image.new("RGBA", (W, H))
    px = capa.load()
    for y in range(H):
        f = y / H
        a = 0.28 + (0.42 * ((f - 0.45) / 0.55) ** 1.5 if f > 0.45 else 0.0)
        a += 0.18 * max(0.0, 1 - f / 0.12)
        fila = (0, 0, 0, int(255 * min(a, 0.82)))
        for x in range(W):
            px[x, y] = fila
    return capa


def cubrir(im):
    """Escala y recorta al centro para llenar 1080x1920 sin deformar."""
    im = im.convert("RGB")
    k = max(W / im.width, H / im.height)
    im = im.resize((max(W, round(im.width * k)), max(H, round(im.height * k))), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def fotograma(plano, tmp):
    """El fondo de un plano como imagen 1080x1920 (el fotograma de 1 s si es
    vídeo). None si el plano no tiene imagen."""
    if plano.get("fuente") == "sin_imagen" or not plano.get("fichero"):
        return None
    ruta = SALIDA / plano["fichero"]
    if plano.get("tipo") == "video":
        salida = tmp / (ruta.stem + "_f.png")
        ffmpeg("-ss", "1", "-i", str(ruta), "-frames:v", "1", str(salida))
        return cubrir(Image.open(salida))
    return cubrir(Image.open(ruta))


FONDO_MARCA = (11, 18, 32)


def componer(fondo, tipo, capa_texto, grad):
    base = fondo if fondo is not None else Image.new("RGB", (W, H), FONDO_MARCA)
    if fondo is not None and tipo in TARJETAS:
        base = base.filter(ImageFilter.GaussianBlur(18))
    lienzo = base.convert("RGBA")
    if fondo is not None:
        lienzo = Image.alpha_composite(lienzo, grad)
    if capa_texto is not None:
        lienzo = Image.alpha_composite(lienzo, capa_texto)
    return lienzo.convert("RGB")


def fuente(nombre, tam):
    try:
        ruta = subprocess.run(["fc-match", "-f", "%{file}", nombre],
                              capture_output=True, text=True).stdout.strip()
        return ImageFont.truetype(ruta, tam)
    except Exception:
        return ImageFont.load_default()


def capa_subtitulo(frase):
    """Variante B: tres o cuatro palabras grandes, blancas con contorno, a
    media altura. Lo que se ve a mitad de escena."""
    palabras = frase.split()
    medio = len(palabras) // 2
    trozo = " ".join(palabras[max(0, medio - 2):medio + 2]).strip(",.;:")
    capa = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(capa)
    f = fuente("Archivo Black", 96)
    lineas, linea = [], ""
    for w in trozo.upper().split():
        prueba = (linea + " " + w).strip()
        if d.textlength(prueba, font=f) > W - 160 and linea:
            lineas.append(linea)
            linea = w
        else:
            linea = prueba
    lineas.append(linea)
    y = int(H * 0.60) - len(lineas) * 60
    for l in lineas:
        x = (W - d.textlength(l, font=f)) / 2
        d.text((x, y), l, font=f, fill=(255, 255, 255, 255),
               stroke_width=8, stroke_fill=(0, 0, 0, 255))
        y += 120
    return capa


# ---------------------------------------------------------------------------
# Hoja de contactos
# ---------------------------------------------------------------------------
def hoja(ident, variante, titulo, cuadros, pies, destino):
    cw, ch = 360, 640
    alto_pie = 170
    hoja = Image.new("RGB", (cw * len(cuadros), 80 + ch + alto_pie), (245, 246, 248))
    d = ImageDraw.Draw(hoja)
    d.text((20, 22), f"{ident} · variante {variante} · {titulo}", font=fuente("Inter:weight=800", 34),
           fill=(11, 18, 32))
    f = fuente("Inter", 19)
    for i, (c, pie) in enumerate(zip(cuadros, pies)):
        hoja.paste(c.resize((cw, ch), Image.LANCZOS), (i * cw, 80))
        # el pie: la frase (para juzgar si la imagen cuenta lo mismo) y la fuente
        y, linea = 80 + ch + 8, ""
        for w in pie.split():
            prueba = (linea + " " + w).strip()
            if d.textlength(prueba, font=f) > cw - 16:
                d.text((i * cw + 8, y), linea, font=f, fill=(40, 45, 55))
                y += 23
                linea = w
                if y > 80 + ch + alto_pie - 24:
                    break
            else:
                linea = prueba
        if y <= 80 + ch + alto_pie - 24:
            d.text((i * cw + 8, y), linea, font=f, fill=(40, 45, 55))
    destino.parent.mkdir(parents=True, exist_ok=True)
    hoja.save(destino, quality=85)
    print(f"  hoja → {destino}")


def describir(plano):
    f = plano.get("fuente")
    if f == "pexels":
        return f"[Pexels · {plano.get('autor')}]"
    if f == "pixabay":
        return f"[Pixabay · {plano.get('autor')}]"
    if f == "ia":
        return "[imagen generada]"
    return "[sin imagen]"


# ---------------------------------------------------------------------------
# Previa en vídeo
# ---------------------------------------------------------------------------
def segmento(plano, dur, tipo, capa_png, grad_png, salida):
    """Un plano en movimiento con el texto encima, en mp4."""
    ruta = SALIDA / plano["fichero"] if plano.get("fichero") else None
    cubrir_f = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H},setsar=1,fps={FPS}")
    desenfoque = ",boxblur=18:2" if tipo in TARJETAS else ""
    if ruta is None:
        entrada = ["-f", "lavfi", "-t", f"{dur:.2f}", "-i",
                   f"color=c=0x0B1220:s={W}x{H}:r={FPS}"]
        fondo = "[0:v]null[bg]"
    elif plano.get("tipo") == "video":
        entrada = ["-stream_loop", "-1", "-t", f"{dur:.2f}", "-i", str(ruta)]
        fondo = f"[0:v]{cubrir_f}{desenfoque}[bg]"
    else:
        # imagen: acercamiento lento (Ken Burns) del 100 % al 112 %
        n = max(1, int(dur * FPS))
        # -framerate 30: sin él la imagen entra a 25 fps, zoompan (d=1) saca un
        # fotograma por cada uno de entrada y el plano dura 25/30 de lo que debe.
        entrada = ["-framerate", str(FPS), "-loop", "1", "-t", f"{dur:.2f}", "-i", str(ruta)]
        fondo = (f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,"
                 f"crop={W*2}:{H*2},zoompan=z='1+0.12*on/{n}':d=1:"
                 f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}"
                 f"{desenfoque},setsar=1[bg]")
    filtro = (f"{fondo};[bg][1:v]overlay=0:0[g];[g][2:v]overlay=0:0,format=yuv420p[v]")
    ffmpeg(*entrada, "-i", str(grad_png), "-i", str(capa_png),
           "-filter_complex", filtro, "-map", "[v]", "-t", f"{dur:.2f}", "-r", str(FPS),
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", str(salida))


def previa(ident, variante, manifiesto, escenas, capas, grad_png, tmp, destino):
    partes = []
    por_escena = {}
    for p in manifiesto["planos"]:
        por_escena.setdefault(p["escena"], []).append(p)
    for e in escenas:
        planos = por_escena.get(e["n"]) or [{"fuente": "sin_imagen"}]
        dur_p = e["duracion_s"] / len(planos)
        for k, p in enumerate(planos, 1):
            seg = tmp / f"seg_{variante}_{e['n']}_{k}.mp4"
            segmento(p, dur_p, e.get("tipo"), capas[e["n"]], grad_png, seg)
            partes.append(seg)
    lista = tmp / f"lista_{variante}.txt"
    lista.write_text("".join(f"file '{s}'\n" for s in partes), encoding="utf-8")
    destino.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg("-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", str(destino))
    print(f"  previa → {destino}")


# ---------------------------------------------------------------------------
def muestrario(ident, con_previa=True):
    guion = json.loads((GUIONES / f"{ident}.es.json").read_text(encoding="utf-8"))
    tmp = SALIDA / ident / "_tmp"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True, exist_ok=True)
    capas_rutas, escenas = capas_de_texto(guion, tmp)
    capas = {n: Image.open(r).convert("RGBA") for n, r in capas_rutas.items()}
    grad = degradado()
    grad_png = tmp / "degradado.png"
    grad.save(grad_png)
    print(f"\n{ident}")
    for variante, titulo in (("A", "archivo + frase corta encima"),
                             ("B", "archivo + subtítulos grandes"),
                             ("C", "imágenes generadas + frase corta encima")):
        origen = "C" if variante == "C" else "A"
        ruta_man = SALIDA / ident / origen / "manifiesto.json"
        if not ruta_man.exists():
            print(f"  variante {variante}: no hay {ruta_man}; me la salto")
            continue
        manifiesto = json.loads(ruta_man.read_text(encoding="utf-8"))
        primero = {}
        for p in manifiesto["planos"]:
            primero.setdefault(p["escena"], p)
        cuadros, pies = [], []
        for e in escenas:
            p = primero.get(e["n"], {"fuente": "sin_imagen"})
            fondo = fotograma(p, tmp)
            if variante == "B" and e.get("tipo") not in TARJETAS and e["n"] != len(escenas):
                capa = capa_subtitulo(e.get("narracion", ""))
            else:
                capa = capas[e["n"]]
            cuadros.append(componer(fondo, e.get("tipo"), capa, grad))
            pies.append(f"{e['n']}. {e.get('narracion', '')} {describir(p)}")
        hoja(ident, variante, titulo, cuadros, pies, HOJAS / f"{ident}_{variante}.jpg")
        if con_previa and variante in ("A", "C"):
            previa(ident, variante, manifiesto, escenas, capas_rutas, grad_png, tmp,
                   SALIDA / ident / f"previa_{ident}_{variante}.mp4")
    shutil.rmtree(tmp, ignore_errors=True)


def main():
    global SALIDA, HOJAS
    ap = argparse.ArgumentParser(description="C50 · muestrario (prueba)")
    ap.add_argument("guiones", nargs="+")
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--hojas", default=str(HOJAS))
    ap.add_argument("--sin-previa", action="store_true", help="solo las hojas de contactos")
    a = ap.parse_args()
    SALIDA, HOJAS = Path(a.salida).resolve(), Path(a.hojas).resolve()
    for ident in a.guiones:
        muestrario(ident, not a.sin_previa)


if __name__ == "__main__":
    sys.exit(main())
