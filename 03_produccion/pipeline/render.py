#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render.py — Agente Realizador (parte visual).

Convierte un guion.json en un vídeo mudo: abre escena.html en un Chromium sin
interfaz, captura únicamente los fotogramas en los que algo se mueve y deja que
FFmpeg estire los tramos estáticos. Un vídeo de 7 minutos necesita unos 2.000
fotogramas reales en vez de 13.000.

No necesita GPU. No necesita internet.

Uso:
    python3 render.py ../../05_calendario/guiones/MDH-001.es.json -o build/MDH-001/mudo.mp4
    python3 render.py guion.json -o borrador.mp4 --fps 15 --escala 0.5   # previsualización
"""
import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent
ESCENA_HTML = AQUI / "escena.html"

# Constantes que deben coincidir con las de escena.html
ESCALONADO = 0.16     # desfase entre unidades animadas
ENTRADA = 0.55        # lo que tarda cada unidad en aparecer
SALIDA = 0.45         # lo que tarda la escena en irse

PALABRAS_POR_MINUTO = 150
MINIMO_S = 2.6
COLA_S = 0.5


def duracion_estimada(texto):
    return max(MINIMO_S, len((texto or "").split()) / PALABRAS_POR_MINUTO * 60 + COLA_S)


def preparar(guion):
    escenas = []
    for i, e in enumerate(guion["escenas"], 1):
        d = dict(e)
        d["duracion_s"] = e.get("duracion_s") or (
            duracion_estimada(e.get("narracion", "")) + e.get("pausa_despues_s", 0.45))
        d["ref"] = e.get("fuente", "") or ""
        d["n"] = i
        escenas.append(d)
    return escenas


def render(guion_path, salida, fps=30, escala=1.0, solo=None, verbose=True):
    guion = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    escenas = preparar(guion)
    if solo:
        escenas = [e for e in escenas if e["n"] == solo]

    tmp = Path(tempfile.mkdtemp(prefix="mdh_"))
    lista = tmp / "lista.txt"
    entradas, capturados, total_s = [], 0, 0.0

    if verbose:
        print(f"Renderizando {len(escenas)} escenas · {int(1920*escala)}x{int(1080*escala)} @ {fps}fps")

    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none",
                                      "--disable-lcd-text",
                                      "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": 1920, "height": 1080},
                           device_scale_factor=escala)
        pag.goto(ESCENA_HTML.as_uri())

        for e in escenas:
            n_uds = pag.evaluate("d => cargar(d)", e)
            dur = e["duracion_s"]
            t_fin_ent = min((max(n_uds - 1, 0) * ESCALONADO) + ENTRADA, max(dur - SALIDA, 0.1))
            t_ini_sal = max(dur - SALIDA, t_fin_ent)
            estatico = max(0.0, t_ini_sal - t_fin_ent)

            def capturar(t):
                nonlocal capturados
                ruta = tmp / f"{capturados:06d}.png"
                pag.evaluate("t => pintar(t)", t)
                pag.screenshot(path=str(ruta))
                capturados += 1
                return ruta

            # tramo de entrada
            n_ent = max(1, int(round(t_fin_ent * fps)))
            for f in range(n_ent):
                entradas.append((capturar(f / fps), 1 / fps))
            # tramo estático: un único fotograma que dura lo que haga falta.
            # El movimiento durante ese tramo lo ponen los subtítulos quemados.
            if estatico > 1 / fps:
                entradas.append((capturar(t_fin_ent), estatico))
            # tramo de salida
            n_sal = max(1, int(round((dur - t_ini_sal) * fps)))
            for f in range(n_sal):
                entradas.append((capturar(t_ini_sal + f / fps), 1 / fps))

            total_s += dur
            if verbose:
                print(f"  {e['n']:>2} [{e['tipo']:<11}] {dur:>5.1f}s  "
                      f"{n_ent + n_sal + 1:>4} capturas  ({n_uds} uds)")
        nav.close()

    with lista.open("w", encoding="utf-8") as fh:
        for ruta, d in entradas:
            fh.write(f"file '{ruta.name}'\nduration {d:.5f}\n")
        fh.write(f"file '{entradas[-1][0].name}'\n")   # el demuxer ignora el último duration

    # Absoluta: el subproceso de FFmpeg de abajo corre con cwd=tmp, así que una
    # ruta relativa se buscaría dentro de la carpeta temporal y no en el proyecto.
    salida = Path(salida).resolve()
    salida.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
           "-fps_mode", "cfr", "-r", str(fps),
           "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(salida)]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=tmp)
    if r.returncode != 0:
        print(r.stderr[-2500:])
        raise SystemExit("FFmpeg falló al montar el vídeo mudo")

    shutil.rmtree(tmp, ignore_errors=True)
    m, s = divmod(total_s, 60)
    if verbose:
        print(f"\nVídeo mudo: {salida}  ({int(m)}m {s:04.1f}s, {capturados} fotogramas capturados)")
    return salida, total_s


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("-o", "--salida", default="mudo.mp4")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--escala", type=float, default=1.0)
    ap.add_argument("--escena", type=int, default=None)
    a = ap.parse_args()
    render(a.guion, a.salida, a.fps, a.escala, a.escena)
