"""Muestra de la cara del final (29/10/2026): el cierre de MDS-045 con la cola (b), ahora y con la risa."""
import json, subprocess, sys, shutil
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "03_produccion/pipeline"))
import render
from playwright.sync_api import sync_playwright
M = Path(__file__).resolve().parent; S = Path(sys.argv[1])
g = json.load(open(RAIZ / "05_calendario/guiones/MDS-045.es.json"))
VOZ = RAIZ / "07_pruebas/c36-2026-10-22/c36.mp3"
VOZ_INI, VOZ_FIN = 28.4, 36.31          # el cierre en la toma única (lo mismo que la muestra de la cola del 26/10)
FPS, COLA, REMATE_S = 30, 1.8, 1.5
for nombre in ("ahora", "risa"):
    voz = VOZ_FIN - VOZ_INI
    guion = {"idioma": "es", "formato": "corto", "escenas": [dict(g["escenas"][-1], duracion_s=round(voz + COLA, 3))]}
    esc = render.preparar(guion)
    tmp = S / nombre; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(parents=True)
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--force-color-profile=srgb", "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": 1080, "height": 1920})
        pag.goto((M / f"escena_{nombre}.html").as_uri())
        pag.add_style_tag(content="html,body{background:#4f5d57 !important}")
        pag.evaluate("d => cargar(d)", esc[0])
        dur = esc[0]["duracion_s"]; n = int(round(dur * FPS))
        for f in range(n):
            t = f / FPS
            pag.evaluate("t => pintar(t)", t)
            etiqueta = "voz" if t < voz else ("cola · tarjeta" if t >= dur - REMATE_S else "cola")
            pag.evaluate("""([e, t]) => { let d = document.getElementById('_et');
                if (!d) { d = document.createElement('div'); d.id = '_et'; document.body.appendChild(d);
                  d.style.cssText = 'position:fixed;left:30px;top:30px;z-index:99999;font:bold 44px sans-serif;color:#fff;background:#000a;padding:8px 18px;border-radius:10px'; }
                d.textContent = e + ' · ' + t; }""", [etiqueta, f"{max(0.0, dur - t):.1f} s al final"])
            pag.screenshot(path=str(tmp / f"{f:05d}.png"))
        nav.close()
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(tmp / "%05d.png"),
                    "-ss", f"{VOZ_INI}", "-t", f"{voz:.3f}", "-i", str(VOZ),
                    "-filter_complex", f"[1:a]apad=whole_dur={dur:.3f}[a]", "-map", "0:v", "-map", "[a]",
                    "-vf", "scale=540:960", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", str(M / f"final_{nombre}.mp4")])
    print(nombre, "duración", dur, "fotogramas", n)
