#!/usr/bin/env python3
"""Captura la página de animación fotograma a fotograma (mismo método que render.py:
Chromium sin pantalla, pintar(t), captura) y la codifica con ffmpeg.

  python3 capturar.py pagina.html --hoja hoja.jpg        # hoja de contactos (20 instantes por escena)
  python3 capturar.py pagina.html --video mudo.mp4       # el vídeo mudo entero, 30 fps
"""
import argparse, json, subprocess, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("pagina")
ap.add_argument("--hoja")
ap.add_argument("--video")
ap.add_argument("--fps", type=int, default=30)
ap.add_argument("--instantes", default="")
a = ap.parse_args()

with sync_playwright() as pw:
    nav = pw.chromium.launch()
    pag = nav.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    errores = []
    pag.on("pageerror", lambda e: errores.append(str(e)))
    pag.on("console", lambda m: errores.append(m.text) if m.type == "error" else None)
    pag.goto(Path(a.pagina).resolve().as_uri())
    pag.wait_for_timeout(300)
    if errores:
        print("ERRORES EN LA PÁGINA:", *errores, sep="\n  "); sys.exit(1)
    total = pag.evaluate("TOTAL")
    ini = pag.evaluate("ESC.map(e => [e[0], e[1]])")
    lienzo = pag.locator("#lienzo")

    # la barrera: 20 instantes por escena, el peor caso (trampa 15)
    malos = {}
    for n, (i0, d) in enumerate(ini, 1):
        for k in range(20):
            t = i0 + d * k / 19
            for m in pag.evaluate("t => comprobar(t)", t):
                malos.setdefault(m.split(":")[0], (round(t, 2), m))
    print("Barrera (textos fuera de su caja o de la zona segura):", "ninguno" if not malos else "")
    for k, (t, m) in malos.items():
        print(f"  t={t}: {m}")
    if errores:
        print("ERRORES:", errores); sys.exit(1)

    if a.hoja:
        from PIL import Image
        import io
        ts = [float(x) for x in a.instantes.split(",")] if a.instantes else \
             [i0 + d * f for (i0, d) in ini for f in (0.15, 0.5, 0.8, 0.98)]
        imgs = []
        for t in ts:
            pag.evaluate("t => pintar(t)", t)
            imgs.append((t, Image.open(io.BytesIO(lienzo.screenshot(type="jpeg", quality=80)))))
        cols = 6 if len(imgs) > 6 else len(imgs)
        filas = (len(imgs) + cols - 1) // cols
        w, h = 270, 480
        from PIL import ImageDraw
        hoja = Image.new("RGB", (cols * w, filas * (h + 28)), "#05080f")
        dr = ImageDraw.Draw(hoja)
        for k, (t, im) in enumerate(imgs):
            x, y = (k % cols) * w, (k // cols) * (h + 28)
            hoja.paste(im.resize((w, h)), (x, y + 28))
            dr.text((x + 6, y + 6), f"t={t:.2f}s", fill="#F2F4F8")
        hoja.save(a.hoja, quality=85)
        print("hoja:", a.hoja, len(imgs), "instantes")

    if a.video:
        n = int(round(total * a.fps))
        ff = subprocess.Popen(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                               "-f", "image2pipe", "-framerate", str(a.fps), "-c:v", "png", "-i", "-",
                               "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                               "-r", str(a.fps), a.video], stdin=subprocess.PIPE)
        t0 = time.time()
        for f in range(n):
            pag.evaluate("t => pintar(t)", f / a.fps)
            ff.stdin.write(lienzo.screenshot(type="png"))
        ff.stdin.close(); ff.wait()
        print(f"vídeo: {a.video} · {n} fotogramas en {time.time() - t0:.0f} s")
    nav.close()
