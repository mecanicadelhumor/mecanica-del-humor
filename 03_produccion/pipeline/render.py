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

# ---------------------------------------------------------------------------
# Todas las llamadas a ffmpeg/ffprobe de este fichero van con
# `stdin=subprocess.DEVNULL`, y no es cosmético.
#
# ffmpeg, si no le cierras la entrada estándar, la LEE — espera pulsaciones
# («q» para abortar, «+»/«-» para el nivel de log). En producción estos
# scripts se llaman desde un bucle del workflow:
#
#     while read -r ID; do  python3 voz.py ...  ; done < <(jq ... plan.json)
#
# El cuerpo del bucle hereda como stdin el mismo descriptor del que `read`
# está sacando las líneas. Cada ffmpeg que arranca se traga lo que quede de
# ese descriptor, así que **el segundo trabajo del plan desaparece sin un
# solo error**: el bucle no vuelve a iterar porque ya no hay nada que leer.
#
# Eso, y no otra cosa, es lo que dejó al canal inglés sin vídeo el 19 y el
# 20 de agosto. No se veía porque no hay nada que ver: no falla, se salta.
# El 20 salió a la luz porque `figura.py` —que no toca stdin— sí iteraba
# sobre los dos trabajos y reventó al buscar el `guion.timed.json` del
# inglés, que nunca se había llegado a generar.
#
# Reproducido con dos líneas de shell: con DEVNULL entran los dos IDs; sin
# él, el segundo llega mutilado o no llega.
# ---------------------------------------------------------------------------


AQUI = Path(__file__).resolve().parent
ESCENA_HTML = AQUI / "escena.html"

# Constantes que deben coincidir con las de escena.html
ESCALONADO = 0.16     # desfase entre unidades animadas
ENTRADA = 0.55        # lo que tarda cada unidad en aparecer
SALIDA = 0.45         # lo que tarda la escena en irse

PALABRAS_POR_MINUTO = 150
MINIMO_S = 2.6
COLA_S = 0.5

# La firma de la esquina inferior izquierda es lo único de escena.html que
# cambia con el idioma: cada canal tiene su nombre. Se inyecta por escena en
# lugar de estar escrita a fuego en el HTML, para que el mismo motor sirva
# para los dos canales sin duplicar ficheros.
MARCAS = {"es": "Mecánica del Humor", "en": "Humor Mechanics"}

# La línea del remate de marca con la que termina cada Short. Un guion puede
# poner la suya en la clave "remate"; si no, se usa esta.
REMATES = {"es": "El mecanismo, cada día a las 19:00",
           "en": "The mechanism, every day"}

# Los dos formatos del canal. El vertical es para Shorts: 1080x1920, que es lo
# que YouTube clasifica automáticamente como Short al subirlo por la API — no
# hay casilla que marcar ni hace falta la etiqueta #shorts.
LIENZO = {"largo": (1920, 1080), "corto": (1080, 1920)}


def duracion_estimada(texto):
    return max(MINIMO_S, len((texto or "").split()) / PALABRAS_POR_MINUTO * 60 + COLA_S)


def preparar(guion):
    idioma = guion.get("idioma", "es")
    formato = guion.get("formato", "largo")
    escenas = []
    for i, e in enumerate(guion["escenas"], 1):
        d = dict(e)
        d["duracion_s"] = e.get("duracion_s") or (
            duracion_estimada(e.get("narracion", "")) + e.get("pausa_despues_s", 0.45))
        d["ref"] = e.get("fuente", "") or ""
        d["n"] = i
        d["idioma"] = idioma
        d["marca"] = MARCAS.get(idioma, MARCAS["es"])
        d["formato"] = formato
        escenas.append(d)
    # C15 · la capa viva necesita saber dónde está cada escena dentro del vídeo
    # ENTERO: la barra de avance, la deriva de la retícula y el giro del
    # engranaje son función del tiempo global. Si se reiniciaran en cada corte,
    # el corte se notaría más, no menos.
    reloj = 0.0
    for d in escenas:
        d["t_inicio"] = round(reloj, 4)
        reloj += d["duracion_s"]
    for d in escenas:
        d["total_s"] = round(reloj, 4)
    # El remate de marca del cierre: la cita de mañana. Se pasa desde aquí para
    # que el motor de escenas no tenga que saber nada de la parrilla.
    if escenas:
        escenas[-1]["remate"] = guion.get("remate") or REMATES.get(idioma, REMATES["es"])
    return escenas


def render(guion_path, salida, fps=30, escala=1.0, solo=None, verbose=True):
    guion = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    escenas = preparar(guion)
    ancho, alto = LIENZO.get(guion.get("formato", "largo"), LIENZO["largo"])
    if solo:
        escenas = [e for e in escenas if e["n"] == solo]

    # «vivo»: captura continua. Se enciende en los Shorts, donde el movimiento
    # es la diferencia entre un vídeo y un pase de diapositivas, y se deja
    # apagado en el episodio largo — 5 minutos a 30 fps son 9.000 capturas y
    # ahí el ritmo lo llevan los cortes, no la animación. Un cambio por vez
    # (regla 11.1): el largo se decide con las métricas del Short delante.
    vivo = guion.get("formato", "largo") == "corto"

    tmp = Path(tempfile.mkdtemp(prefix="mdh_"))
    lista = tmp / "lista.txt"
    entradas, capturados, total_s = [], 0, 0.0

    if verbose:
        print(f"Renderizando {len(escenas)} escenas · "
              f"{int(ancho*escala)}x{int(alto*escala)} @ {fps}fps "
              f"[{guion.get('formato', 'largo')}]")

    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none",
                                      "--disable-lcd-text",
                                      "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": ancho, "height": alto},
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

            if vivo:
                # ---- C15 · captura continua (Shorts) --------------------
                # El tramo central YA NO es un fotograma congelado. Se captura
                # la escena entera a fps porque en escena.html hay movimiento
                # todo el rato: revelado por palabra, acercamiento lento,
                # deriva de la retícula, barra de avance y el personaje.
                #
                # Lo que costaba esto era la razón de no hacerlo, y esa razón
                # ya no existe: el repositorio es PÚBLICO y los minutos de
                # Actions en repositorios públicos son ilimitados (verificado
                # el 28/08/26 contra la nota de precios de 2026 de GitHub).
                # El único límite real es el timeout de 150 min del job, y un
                # Short de 60 s a 30 fps son 1.800 capturas ≈ 4 min.
                n_f = max(1, int(round(dur * fps)))
                for f in range(n_f):
                    entradas.append((capturar(f / fps), 1 / fps))
                total_s += dur
                if verbose:
                    print(f"  {e['n']:>2} [{e['tipo']:<11}] {dur:>5.1f}s  "
                          f"{n_f:>4} capturas  ({n_uds} uds) · vivo")
                continue

            # tramo de entrada
            n_ent = max(1, int(round(t_fin_ent * fps)))
            for f in range(n_ent):
                entradas.append((capturar(f / fps), 1 / fps))
            # tramo estático: un único fotograma que dura lo que haga falta.
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
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=tmp,
                       stdin=subprocess.DEVNULL)
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
