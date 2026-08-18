#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
montaje.py — Agente Montador.

Une vídeo mudo + narración + música, aplica ducking (la música baja
automáticamente cuando habla la voz), quema los subtítulos animados y
normaliza el volumen al estándar de YouTube (-14 LUFS).

    python3 montaje.py build/MDH-001 --musica assets/musica/cama_01.mp3

Espera encontrar en la carpeta:
    mudo.mp4          (de render.py)
    voz.mp3           (de voz.py)
    subtitulos.ass    (de voz.py, opcional)
Produce:
    final.mp4
"""
import argparse
import subprocess
from pathlib import Path


def ejecutar(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:])
        raise SystemExit(f"FFmpeg falló: {' '.join(cmd[:6])}...")
    return r


def montar(carpeta, musica=None, vol_musica=0.14, quemar_subs=True, salida=None):
    carpeta = Path(carpeta)
    mudo = carpeta / "mudo.mp4"
    voz = carpeta / "voz.mp3"
    ass = carpeta / "subtitulos.ass"
    salida = Path(salida or carpeta / "final.mp4")
    for f in (mudo, voz):
        if not f.exists():
            raise SystemExit(f"Falta {f}")

    entradas = ["-i", str(mudo), "-i", str(voz)]
    if musica:
        entradas += ["-stream_loop", "-1", "-i", str(musica)]

    # --- cadena de audio ---
    if musica:
        # sidechaincompress: la voz (cadena lateral) comprime la música.
        # La voz se usa dos veces (como cadena lateral y en la mezcla final),
        # así que hay que duplicarla con asplit — FFmpeg no deja reutilizar
        # una misma etiqueta de salida como entrada de dos filtros distintos.
        filtro_audio = (
            "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
            "highpass=f=80,acompressor=threshold=0.09:ratio=3:attack=15:release=180,"
            "asplit=2[voz1][voz2];"
            f"[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume={vol_musica}[mus];"
            "[mus][voz1]sidechaincompress=threshold=0.02:ratio=14:attack=8:release=380[musduck];"
            "[voz2][musduck]amix=inputs=2:duration=first:dropout_transition=0,"
            "loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
        )
    else:
        filtro_audio = (
            "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
            "highpass=f=80,acompressor=threshold=0.09:ratio=3:attack=15:release=180,"
            "loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
        )

    # --- cadena de vídeo ---
    # Respiración lentísima de zoom (1.0 -> 1.015 -> 1.0 cada 24s): da sensación
    # de plano vivo durante los tramos estáticos de render.py sin recapturar ni
    # un fotograma más con Playwright — es puro postprocesado de FFmpeg sobre
    # el mudo.mp4 ya renderizado. El fps debe coincidir con el de render.py.
    RESPIRACION = (
        "zoompan=z='1.0+0.015*(1+sin(2*PI*on/720))/2':d=1:"
        "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30"
    )
    if quemar_subs and ass.exists():
        filtro_video = f"[0:v]{RESPIRACION}[zoom];[zoom]ass='{ass.as_posix()}'[vout]"
    else:
        filtro_video = f"[0:v]{RESPIRACION}[vout]"
    mapa_v = "[vout]"

    filtros = f"{filtro_video};{filtro_audio}"

    cmd = ["ffmpeg", "-y", *entradas,
           "-filter_complex", filtros,
           "-map", mapa_v, "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-shortest", "-movflags", "+faststart", str(salida)]

    ejecutar(cmd)
    mb = salida.stat().st_size / 1e6
    print(f"Vídeo final: {salida}  ({mb:.1f} MB)")
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--musica", default=None)
    ap.add_argument("--vol-musica", type=float, default=0.14)
    ap.add_argument("--sin-subs", action="store_true")
    ap.add_argument("-o", "--salida", default=None)
    a = ap.parse_args()
    montar(a.carpeta, a.musica, a.vol_musica, not a.sin_subs, a.salida)
