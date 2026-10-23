"""Muestrario 2D (C61) · paso 2: fotograma a fotograma en Chromium, como render.py.

Uso:
  python render.py hoja                       -> hoja_expresiones.png
  python render.py completo AUDIO INICIO FIN  -> personaje_completo.mp4
  python render.py esquina  AUDIO INICIO FIN  -> personaje_esquina.mp4
"""
import base64
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).parent.resolve()
FOTO = AQUI.parents[2] / "02_marca" / "banco" / "apreton_manos_hombres_reunion.jpg"


def abrir(p, modo, ancho, alto):
    nav = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None,
                            args=["--force-color-profile=srgb", "--font-render-hinting=none"])
    pag = nav.new_page(viewport={"width": ancho, "height": alto})
    init = ""
    pista = AQUI / "pista.json"
    if pista.exists():
        init += f"window.PISTA = {pista.read_text()};"
    if modo == "esquina":
        datos = base64.b64encode(FOTO.read_bytes()).decode()
        init += f"window.FOTO = 'data:image/jpeg;base64,{datos}';"
    pag.add_init_script(init)
    pag.goto((AQUI / "personaje.html").as_uri() + f"?modo={modo}")
    pag.wait_for_load_state("networkidle")
    return nav, pag


def main():
    modo = sys.argv[1]
    with sync_playwright() as p:
        if modo == "hoja":
            nav, pag = abrir(p, "hoja", 1800, 1560)
            pag.screenshot(path=str(AQUI / "hoja_expresiones.png"))
            nav.close()
            return
        audio, a, b = sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
        fps = json.loads((AQUI / "pista.json").read_text())["fps"]
        n = int((b - a) * fps)
        tmp = Path(tempfile.mkdtemp())
        nav, pag = abrir(p, modo, 1080, 1920)
        t0 = time.time()
        for i in range(n):
            pag.evaluate(f"setT({i / fps})")
            pag.screenshot(path=str(tmp / f"{i:05d}.png"))
        nav.close()
        t_cap = time.time() - t0
    salida = AQUI / f"personaje_{modo}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(fps), "-i", str(tmp / "%05d.png"),
                    "-ss", str(a), "-to", str(b), "-i", audio,
                    "-af", f"afade=t=out:st={b - a - 0.4}:d=0.4",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", str(salida)], check=True)
    shutil.rmtree(tmp)
    print(f"{salida.name}: {n} fotogramas, captura {t_cap:.1f} s ({t_cap / n * 1000:.0f} ms/fotograma)")


if __name__ == "__main__":
    main()
