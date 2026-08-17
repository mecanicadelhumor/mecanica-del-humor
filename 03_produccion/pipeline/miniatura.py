#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
miniatura.py — genera la miniatura 1280x720 con la fórmula de marca.

La miniatura de Mecánica del Humor debe parecer la figura de un paper, no un
clickbait: fondo oscuro, retícula, tres o cuatro palabras grandes, y un solo
acento ámbar señalando el punto clave. Se genera desde el mismo motor de
escenas, así que nunca se desvía de la identidad del canal.

    python3 miniatura.py guion.json -o miniatura.png
    python3 miniatura.py guion.json -o m.png --texto "Nadie nace *gracioso*" --pie "Hay datos"
"""
import argparse
import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
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
<div id="v"></div><div id="m"></div><div id="f">Mecánica del Humor</div><div id="n">__N__</div>
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


def generar(guion_path, salida, texto=None, pie=None):
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    primera = g["escenas"][0]
    texto = texto or primera.get("titulo") or g["titulo_trabajo"]
    pie = pie or primera.get("subtitulo") or g.get("tesis", "")
    if len(pie) > 96:
        pie = pie[:93].rsplit(" ", 1)[0] + "…"

    html = (HTML.replace("__T__", rico(texto))
                .replace("__P__", rico(pie))
                .replace("__N__", g["id"].replace("MDH-", "Nº "))
                .replace("__TAM__", str(tamano(texto))))
    tmp = Path(salida).with_suffix(".html")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb", "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": 1280, "height": 720})
        pag.goto(tmp.as_uri())
        pag.screenshot(path=str(salida))
        nav.close()
    tmp.unlink(missing_ok=True)
    print(f"Miniatura: {salida}")
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("-o", "--salida", default="miniatura.png")
    ap.add_argument("--texto", default=None)
    ap.add_argument("--pie", default=None)
    a = ap.parse_args()
    generar(a.guion, a.salida, a.texto, a.pie)
