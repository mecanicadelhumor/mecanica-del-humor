#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
qa.py — el expediente de calidad de cada vídeo.

Deja en el repositorio lo mínimo imprescindible para que alguien —o algo— pueda
juzgar un vídeo sin descargarse 40 MB de mp4: seis fotogramas repartidos por la
pieza y un puñado de medidas objetivas del audio y del montaje.

    python3 qa.py build/MDH-002.es -o 05_calendario/qa/MDH-002.es

Existe por una razón muy concreta: los tres fallos que ha tenido este pipeline
—el falso arranque de la voz, el salto de posición del subtítulo y el temblor
de un píxel del zoom— eran todos visibles en un fotograma o medibles en una
cifra, y ninguno se detectó hasta que alguien miró el vídeo entero. Esto pone
esos indicios donde la revisión diaria puede leerlos sin credenciales, porque
el repositorio es público y los artefactos de Actions no lo son.
"""
import argparse
import json
import subprocess
from pathlib import Path

N_FOTOGRAMAS = 6
ANCHO = 640          # suficiente para leer titulares y ver desencuadres


def ffprobe(ruta, entradas, stream=None):
    cmd = ["ffprobe", "-v", "error", "-show_entries", entradas,
           "-of", "json"]
    if stream:
        cmd += ["-select_streams", stream]
    cmd.append(str(ruta))
    r = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(r.stdout or "{}")


def medir_audio(mp4):
    """Nivel integrado y pico real, que es donde se ve si el montaje se pasó."""
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp4),
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
         "-f", "null", "-"],
        capture_output=True, text=True)
    salida = r.stderr
    try:
        bloque = salida[salida.rindex("{"):salida.rindex("}") + 1]
        d = json.loads(bloque)
        return {"lufs": float(d["input_i"]), "pico_dbtp": float(d["input_tp"]),
                "rango_lu": float(d["input_lra"])}
    except (ValueError, KeyError):
        return {}


def silencio_inicial(mp4):
    """Segundos de silencio al empezar. El falso arranque de la voz inglesa se
    veía aquí: 0.0 s de colchón donde debería haber ~0.6."""
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp4),
         "-af", "silencedetect=n=-45dB:d=0.2", "-f", "null", "-"],
        capture_output=True, text=True)
    for linea in r.stderr.splitlines():
        if "silence_end" in linea:
            try:
                fin = float(linea.split("silence_end:")[1].split("|")[0])
                dur = float(linea.split("silence_duration:")[1])
                return round(fin - dur, 3), round(fin, 3)
            except (IndexError, ValueError):
                break
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta", help="build/<ID>")
    ap.add_argument("-o", "--salida", required=True)
    a = ap.parse_args()

    carpeta, salida = Path(a.carpeta), Path(a.salida)
    mp4 = carpeta / "final.mp4"
    if not mp4.exists():
        raise SystemExit(f"No hay {mp4}: nada que revisar.")
    salida.mkdir(parents=True, exist_ok=True)

    fmt = ffprobe(mp4, "format=duration,size,bit_rate").get("format", {})
    dur = float(fmt.get("duration", 0))

    # Fotogramas repartidos, evitando el primer y el último medio segundo:
    # ahí solo se ve el fundido a negro y no informan de nada.
    marcas = [round(dur * (i + 0.5) / N_FOTOGRAMAS, 2) for i in range(N_FOTOGRAMAS)]
    for i, t in enumerate(marcas, 1):
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", str(mp4),
             "-frames:v", "1", "-vf", f"scale={ANCHO}:-2", "-q:v", "4",
             str(salida / f"f{i}_{t:g}s.jpg")], check=True)

    guion = {}
    timed = carpeta / "guion.timed.json"
    if timed.exists():
        g = json.loads(timed.read_text(encoding="utf-8"))
        escenas = g.get("escenas", [])
        largas = [(i, round(e.get("duracion_s", 0), 1))
                  for i, e in enumerate(escenas, 1) if e.get("duracion_s", 0) > 14]
        guion = {
            "titulo_trabajo": g.get("titulo_trabajo"),
            "idioma": g.get("idioma"),
            "voz": g.get("voz_usada"),
            "escenas": len(escenas),
            "duracion_narracion_s": g.get("duracion_total_s"),
            "escenas_por_encima_de_14s": largas,
            "escena_mas_larga_s": max((e.get("duracion_s", 0) for e in escenas), default=0),
        }

    ini, fin = silencio_inicial(mp4)
    ficha = {
        "id": carpeta.name,
        "duracion_final_s": round(dur, 2),
        "tamano_mb": round(int(fmt.get("size", 0)) / 1e6, 1),
        "audio": medir_audio(mp4),
        "silencio_inicial": {"empieza_s": ini, "acaba_s": fin,
                             "_nota": "Debe rondar 0.6 s: es el colchón de entrada. "
                                      "Un 0 aquí significa que el vídeo entra en seco."},
        "musica": json.loads((carpeta / "musica.json").read_text(encoding="utf-8"))
                  if (carpeta / "musica.json").exists() else None,
        "guion": guion,
        "fotogramas_s": marcas,
        "_nota": "Lo genera qa.py al final de cada producción. Sirve para que la revisión "
                 "diaria pueda juzgar el vídeo leyendo el repositorio, sin credenciales y "
                 "sin descargar el mp4.",
    }
    (salida / "ficha.json").write_text(
        json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"QA de {carpeta.name}: {N_FOTOGRAMAS} fotogramas y ficha en {salida}")


if __name__ == "__main__":
    main()
