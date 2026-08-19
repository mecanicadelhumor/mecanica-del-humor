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
PAD_INICIO = 0.6     # el mismo colchón que mete montaje.py al principio


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


def arranque(mp4, ventana=4.0):
    """Radiografía del primer segundo de audio, para cazar el falso arranque.

    `silencio_inicial` mira dónde acaba el PRIMER silencio y para ahí. Eso no
    basta: si el sintetizador mete delante una sílaba suelta —el fallo que
    Silvestre oyó en MDH-001.en y otra vez en MDH-002.en— la secuencia real es
    «colchón, fragmento, otro silencio, narración de verdad», y el primer
    silencio acaba exactamente donde debe. La métrica daba 0,629 s, o sea
    correcta, mientras el defecto seguía ahí.

    Aquí se listan TODOS los silencios de los primeros segundos, con un umbral
    de duración más corto (0,12 s) para no perder los huecos pequeños. Si
    después del colchón hay un trozo de audio breve y luego otro silencio, eso
    es un fragmento y se marca.
    """
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-t", str(ventana), "-i", str(mp4),
         "-af", "silencedetect=n=-45dB:d=0.12", "-f", "null", "-"],
        capture_output=True, text=True)
    silencios, abierto = [], None
    for linea in r.stderr.splitlines():
        if "silence_start" in linea:
            try:
                abierto = float(linea.split("silence_start:")[1].strip().split()[0])
            except (IndexError, ValueError):
                abierto = None
        elif "silence_end" in linea and abierto is not None:
            try:
                silencios.append([round(abierto, 3),
                                  round(float(linea.split("silence_end:")[1].split("|")[0]), 3)])
            except (IndexError, ValueError):
                pass
            abierto = None
    if abierto is not None:
        silencios.append([round(abierto, 3), None])

    # El primer silencio es el colchón de entrada que pone montaje.py. Si hay
    # un segundo silencio que empieza dentro del primer segundo y medio de
    # narración, lo que suena en medio es un fragmento, no una frase.
    fragmento, dur_frag = False, None
    if len(silencios) >= 2 and silencios[0][1] is not None:
        hueco = silencios[1][0] - silencios[0][1]
        if 0 < hueco < 0.9 and silencios[1][0] < 2.5:
            fragmento, dur_frag = True, round(hueco, 3)

    return {
        "silencios_s": silencios,
        "fragmento_antes_de_la_narracion": fragmento,
        "duracion_fragmento_s": dur_frag,
        "_nota": "Si «fragmento_antes_de_la_narracion» es true, el sintetizador ha metido "
                 "una sílaba suelta delante de la primera frase: se oye un trozo de palabra "
                 "que no pertenece a nada. Comprobado a mano en MDH-001.en y MDH-002.en. "
                 "«silencio_inicial» NO lo detecta, porque el colchón de entrada acaba donde debe.",
    }



def instantes(carpeta, dur_total, n=N_FOTOGRAMAS):
    """Momentos en los que de verdad hay algo que ver.

    Muestrear a intervalos ciegos cae con frecuencia en mitad del fundido entre
    dos escenas: el fotograma sale casi negro y no informa de nada. Pasó con el
    primero de MDH-002.es, que salió al 20 % de opacidad. Con el guion
    cronometrado sí se sabe dónde empieza cada escena, así que se apunta al 60 %
    de su duración: la entrada escalonada ya ha terminado y la salida aún no ha
    empezado.
    """
    ciego = [round(dur_total * (i + 0.5) / n, 2) for i in range(n)]
    timed = carpeta / "guion.timed.json"
    if not timed.exists():
        return ciego
    escenas = json.loads(timed.read_text(encoding="utf-8")).get("escenas", [])
    tramos, reloj = [], PAD_INICIO
    for e in escenas:
        d = float(e.get("duracion_s") or 0)
        if d >= 3.0:                     # las muy cortas no dan un buen fotograma
            tramos.append((reloj, d))
        reloj += d
    if not tramos:
        return ciego
    elegidas = {round(i * (len(tramos) - 1) / max(n - 1, 1)) for i in range(n)}
    return sorted(round(min(tramos[j][0] + max(tramos[j][1] * 0.6, 1.2),
                            dur_total - 0.6), 2) for j in elegidas)


def subtitulos(carpeta):
    """Si el vídeo lleva o no subtítulos quemados, y de quién es la culpa.

    Los subtítulos palabra a palabra no son un adorno: son lo único que se mueve
    durante el tramo central de cada escena, que es estático por diseño. Un
    vídeo sin ellos se percibe como una sucesión de diapositivas.
    """
    ass, srt = carpeta / "subtitulos.ass", carpeta / "subtitulos.srt"
    n = ass.read_text(encoding="utf-8", errors="ignore").count("Dialogue:") if ass.exists() else 0
    return {
        "ass_existe": ass.exists(),
        "lineas_ass": n,
        "srt_existe": srt.exists(),
        "quemados": bool(n),
        "_nota": ("«quemados» en false significa que el vídeo sale sin subtítulos en pantalla. "
                  "Si ass_existe es true y lineas_ass es 0, el fallo está en voz.py: el "
                  "sintetizador no devolvió marcas de tiempo por palabra (WordBoundary). "
                  "Si lineas_ass es alto y aun así no se ven en los fotogramas, el fallo "
                  "está en el quemado de montaje.py."),
    }


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

    marcas = instantes(carpeta, dur)
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
        "arranque": arranque(mp4),
        "subtitulos": subtitulos(carpeta),
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
