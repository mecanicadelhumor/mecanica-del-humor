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
import hashlib
import json
import subprocess
from pathlib import Path

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


# Colchón al principio y al final: sin esto el vídeo entra y sale en seco,
# como si se hubiera cortado (feedback del 18/08). Se clona el primer/último
# fotograma y se funde a negro/silencio en vez de cortar de golpe.
PAD_INICIO = 0.6
PAD_FIN = 1.0
FUNDE_IN = 0.4
FUNDE_OUT = 0.6
# La música se apaga sola antes de que el amix la corte. Ver el comentario
# largo en la cadena de audio.
FUNDE_MUSICA = 1.5


def ejecutar(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        print(r.stderr[-3000:])
        raise SystemExit(f"FFmpeg falló: {' '.join(cmd[:6])}...")
    return r


def duracion_s(ruta):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(ruta)],
        capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0 or not r.stdout.strip():
        raise SystemExit(f"ffprobe falló al medir {ruta}: {r.stderr[-500:]}")
    return float(r.stdout.strip())


def montar(carpeta, musica=None, vol_musica=0.14, quemar_subs=False, salida=None):
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

    # Duración del vídeo mudo ya renderizado: sobre ella calculamos dónde debe
    # empezar el fundido de salida, una vez sumado el colchón de ambos lados.
    dur_mudo = duracion_s(mudo)
    dur_total = dur_mudo + PAD_INICIO + PAD_FIN
    # El amix lleva duration=first y su primera entrada es la voz, así que la
    # mezcla termina exactamente cuando termina voz.mp3. Ese es el instante en
    # el que hay que tener la música ya en silencio.
    dur_voz = duracion_s(voz)

    # --- cadena de audio ---
    # Colchón de audio: silencio al principio (adelay) y al final (apad), más
    # un fundido de entrada/salida sobre ese silencio para que no suene a corte.
    colchon_audio = (
        f"adelay={int(round(PAD_INICIO * 1000))}|{int(round(PAD_INICIO * 1000))},"
        f"apad=pad_dur={PAD_FIN},"
        f"afade=t=in:st=0:d={FUNDE_IN},"
        f"afade=t=out:st={dur_total - FUNDE_OUT:.3f}:d={FUNDE_OUT}"
    )
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
            "[mus][voz1]sidechaincompress=threshold=0.02:ratio=14:attack=8:release=380[musduck0];"
            # La música se apaga ella sola antes del corte del amix.
            #
            # El afade=t=out del colchón NO servía para esto: se calcula sobre
            # dur_total (mudo + los dos colchones) y arranca en
            # dur_total-FUNDE_OUT, que cae 0,4 s DESPUÉS de que amix haya
            # cortado ya la mezcla en dur_voz. Es decir, atenuaba el silencio
            # del apad. Medido sobre una prueba sintética: la música se
            # mantenía plana en -32,8 dBFS y caía a silencio digital en una
            # sola ventana de 0,1 s. Eso es el corte seco que se oía al final.
            f"[musduck0]afade=t=out:st={max(0.0, dur_voz - FUNDE_MUSICA):.3f}:"
            f"d={FUNDE_MUSICA}[musduck];"
            "[voz2][musduck]amix=inputs=2:duration=first:dropout_transition=0,"
            "loudnorm=I=-14:TP=-1.5:LRA=11[apre];"
            f"[apre]{colchon_audio}[aout]"
        )
    else:
        filtro_audio = (
            "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
            "highpass=f=80,acompressor=threshold=0.09:ratio=3:attack=15:release=180,"
            "loudnorm=I=-14:TP=-1.5:LRA=11[apre];"
            f"[apre]{colchon_audio}[aout]"
        )

    # --- cadena de vídeo ---
    # NO usar zoompan aquí. Se probó una "respiración" de zoom lentísima
    # (1.0 -> 1.015 -> 1.0) y el resultado no es un zoom suave: zoompan trunca
    # a entero el origen del recorte (x,y) en cada fotograma, así que la imagen
    # da saltos erráticos de ±1px arriba/abajo/izquierda/derecha. Medido sobre
    # una escena estática: 13 posiciones distintas del texto en 120 fotogramas
    # con zoompan, frente a 1 sola sin él. Es imperceptible como "movimiento"
    # pero hace incómoda la lectura, que es justo lo contrario de lo que busca
    # el canal. El plano vivo lo aportan la entrada escalonada de cada unidad,
    # la cifra que cuenta y los subtítulos quemados palabra a palabra.
    #
    # Colchón de vídeo: clona el primer/último fotograma (tpad) para no cortar
    # en seco. Desplaza el contenido real +PAD_INICIO en la línea de tiempo,
    # igual que adelay hace con el audio, así que vídeo, voz y subtítulos
    # siguen sincronizados.
    PAD = (
        f"tpad=start_duration={PAD_INICIO}:start_mode=clone:"
        f"stop_duration={PAD_FIN}:stop_mode=clone"
    )
    # El fundido a negro va el último, sobre el vídeo ya paginado (y con subs
    # quemados si los hay), con los mismos tiempos que el fundido de audio.
    FUNDE = (
        f"fade=t=in:st=0:d={FUNDE_IN}:c=black,"
        f"fade=t=out:st={dur_total - FUNDE_OUT:.3f}:d={FUNDE_OUT}:c=black"
    )
    # ---------------------------------------------------------------------
    # Subtítulos quemados: APAGADOS por decisión de canal (20/08).
    #
    # Costó tres vídeos hacerlos funcionar, así que conviene dejar escrito por
    # qué se apagan y que no es un fallo: con ellos en pantalla, Silvestre vio
    # el vídeo terminado y distraen. Palabra a palabra, en la banda baja y
    # sobre un diseño que ya es tipográfico, compiten con el propio texto de
    # la escena en vez de acompañarlo.
    #
    # No se pierde accesibilidad: `publicar.py` sube `subtitulos.srt` a YouTube
    # como pista de subtítulos de verdad, así que quien los quiera los activa
    # con el botón y además puede traducirlos, buscarlos y leerlos a su tamaño.
    # Eso es mejor que quemarlos, no peor.
    #
    # Lo que sí se pierde es movimiento: los subtítulos eran lo único que se
    # movía durante el tramo central de cada escena. Está anotado en
    # MEJORA_VISUAL.md, porque ahora los ítems de animación suben de prioridad.
    #
    # El `.ass` se sigue generando y `qa.py` sigue contando sus líneas: es el
    # canario que avisa si edge-tts vuelve a dejar de mandar WordBoundary, y
    # sin él ese fallo volvería a ser invisible. Volver a encenderlos es pasar
    # `--con-subs`, o cambiar el False de arriba por True.
    # ---------------------------------------------------------------------
    n_subs = ass.read_text(encoding="utf-8", errors="ignore").count("Dialogue:") if ass.exists() else 0
    if not quemar_subs:
        print(f"Subtítulos NO quemados (decisión de canal). "
              f"El .ass tiene {n_subs} líneas y el .srt va a YouTube como pista aparte.")
    if quemar_subs and n_subs:
        filtro_video = f"[0:v]{PAD}[pad];[pad]ass='{ass.as_posix()}'[vsub];[vsub]{FUNDE}[vout]"
        print(f"Subtítulos quemados: {n_subs} líneas")
    else:
        if quemar_subs:
            motivo = "no existe subtitulos.ass" if not ass.exists() else "subtitulos.ass no tiene líneas"
            print(f"::warning::Montando SIN subtítulos quemados: {motivo}.")
        filtro_video = f"[0:v]{PAD}[pad];[pad]{FUNDE}[vout]"
    mapa_v = "[vout]"

    filtros = f"{filtro_video};{filtro_audio}"

    cmd = ["ffmpeg", "-y", *entradas,
           "-filter_complex", filtros,
           "-map", mapa_v, "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-shortest", "-movflags", "+faststart", str(salida)]

    ejecutar(cmd)

    # Deja constancia de qué pista se usó. publicar.py la necesita para poner
    # la atribución en la descripción del vídeo, que en las CC BY es obligación
    # legal. Se guarda el sha256 y no solo el nombre porque cama.mp3 es una
    # copia de otra pista: el hash identifica la música de verdad.
    if musica:
        m = Path(musica)
        (carpeta / "musica.json").write_text(json.dumps({
            "archivo": m.name,
            "sha256": hashlib.sha256(m.read_bytes()).hexdigest(),
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    # Deja constancia de si se quemaron subtítulos DE VERDAD, no solo de si se
    # pidieron: qa.py no tiene otra forma de saberlo (propuesta de la revisión
    # diaria del 24/08, aprobada por Silvestre el 28/08). Antes lo adivinaba a
    # partir de si subtitulos.ass tenía líneas, y acertaba solo mientras
    # quemar_subs era true por defecto; desde que es false (20/08) el .ass
    # sigue teniendo líneas y la adivinanza salía mal.
    (carpeta / "montaje.json").write_text(json.dumps({
        "subtitulos_quemados": bool(quemar_subs and n_subs),
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    mb = salida.stat().st_size / 1e6
    print(f"Vídeo final: {salida}  ({mb:.1f} MB)")
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--musica", default=None)
    ap.add_argument("--vol-musica", type=float, default=0.14)
    ap.add_argument("--sin-subs", action="store_true", help="(ya es el comportamiento por defecto)")
    ap.add_argument("--con-subs", action="store_true", help="vuelve a quemar los subtítulos en el vídeo")
    ap.add_argument("-o", "--salida", default=None)
    a = ap.parse_args()
    # Por defecto NO se queman. `--sin-subs` se mantiene por compatibilidad y
    # ya no hace nada; para volver a quemarlos hay que pedirlo con `--con-subs`.
    montar(a.carpeta, a.musica, a.vol_musica, a.con_subs, a.salida)
