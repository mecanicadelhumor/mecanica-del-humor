#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
voz.py — Agente Locutor.

Sintetiza la narración de cada escena con edge-tts (voces neuronales de
Microsoft, gratis y sin clave), mide la duración real de cada escena y genera
los subtítulos a partir de las marcas de tiempo por palabra que el propio
sintetizador devuelve. Sin Whisper, sin transcripción, sin errores.

Requiere internet -> se ejecuta en GitHub Actions, no en el contenedor de Cowork.

    pip install edge-tts
    python3 voz.py guion.json --salida build/MDH-001

Produce:
    build/MDH-001/voz/escena_001.mp3 ...
    build/MDH-001/voz.mp3            narración completa concatenada
    build/MDH-001/subtitulos.srt     para subir a YouTube
    build/MDH-001/subtitulos.ass     para quemar en el vídeo (palabra a palabra)
    build/MDH-001/guion.timed.json   el guion con duracion_s real por escena
"""
import argparse
import asyncio
import json
import subprocess
from pathlib import Path

try:
    import edge_tts
except ImportError:
    raise SystemExit("Falta edge-tts.  pip install edge-tts")

# Para inglés se usa la voz monolingüe, NO la variante "Multilingual". Es el
# mismo locutor (Andrew), pero el modelo multilingüe existe para leer varios
# idiomas con una sola voz, cosa que aquí no hace falta: cada canal tiene su
# guion en su idioma. En MDH-001.en la variante multilingüe metió un falso
# arranque audible antes de la primera palabra ("think" cortado antes de
# "Think about..."), y en español, con voz monolingüe, no ocurrió.
VOCES = {
    "es": "es-ES-AlvaroNeural",
    "es-f": "es-ES-ElviraNeural",
    "en": "en-US-AndrewNeural",
    "en-multi": "en-US-AndrewMultilingualNeural",   # solo si un guion mezcla idiomas
    "en-gb": "en-GB-RyanNeural",
}

# Ritmo: un poco más lento que el habla natural favorece la comprensión y da
# aire a la animación. -4% es el punto en el que deja de sonar a robot con prisa.
RITMO = "-4%"
TONO = "+0Hz"


def hms(seg, coma=","):
    h = int(seg // 3600); m = int(seg % 3600 // 60); s = seg % 60
    return f"{h:02d}:{m:02d}:{int(s):02d}{coma}{int(round((s%1)*1000)):03d}"


async def sintetizar(texto, voz, destino):
    """Devuelve (duracion_s, [(ini_s, fin_s, palabra), ...])."""
    com = edge_tts.Communicate(texto, voz, rate=RITMO, pitch=TONO)
    audio, palabras = bytearray(), []
    async for trozo in com.stream():
        if trozo["type"] == "audio":
            audio.extend(trozo["data"])
        elif trozo["type"] == "WordBoundary":
            ini = trozo["offset"] / 1e7
            dur = trozo["duration"] / 1e7
            palabras.append((ini, ini + dur, trozo["text"]))
    destino.write_bytes(bytes(audio))
    dur = palabras[-1][1] if palabras else 0.0
    return dur, palabras


def duracion_real(path):
    """Duración exacta del mp3 según ffprobe (más fiable que la última palabra)."""
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def escribir_srt(bloques, destino):
    L = []
    for i, (ini, fin, txt) in enumerate(bloques, 1):
        L += [str(i), f"{hms(ini)} --> {hms(fin)}", txt, ""]
    destino.write_text("\n".join(L), encoding="utf-8")


def escribir_ass(palabras, destino, ancho=1920, alto=1080):
    """Subtítulo quemado: bloques de ~5 palabras, la actual en ámbar.

    Alineación 1 (abajo-IZQUIERDA), no 2 (abajo-centro): con centrado, cada
    bloque de 5 palabras tiene un ancho de línea distinto, así que ASS lo
    recentra cada vez y el texto entero "salta" de sitio en cada bloque
    (~cada 1.5-2s durante todo el vídeo) — eso es lo que mareaba al leer,
    no la retícula. Con el ancla fija a la izquierda (mismo MarginL siempre)
    el borde izquierdo del texto no se mueve nunca; solo crece hacia la
    derecha según el bloque. Comprobado con captura de fotograma: con
    centrado el borde izquierdo saltaba de x=912 a x=435px entre dos
    bloques; con este cambio se queda fijo en x=184px en ambos.
    """
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {ancho}
PlayResY: {alto}
WrapStyle: 2

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: pie,Inter,58,&H00F8F4F2,&H00201408,&H96000000,-1,0,0,0,100,100,0,0,1,0,0,1,180,180,96,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
    lineas = []
    for i in range(0, len(palabras), 5):
        grupo = palabras[i:i + 5]
        ini, fin = grupo[0][0], grupo[-1][1]
        for j, (pi, pf, _) in enumerate(grupo):
            txt = " ".join(
                (f"{{\\c&H0020B0FF&}}{w}{{\\c&H00F8F4F2&}}" if k == j else w)
                for k, (_, _, w) in enumerate(grupo))
            lineas.append(f"Dialogue: 0,{hms(pi,'.')[:-1]},{hms(pf,'.')[:-1]},pie,,0,0,0,,{txt}")
    destino.write_text(cab + "\n".join(lineas), encoding="utf-8")


async def principal(guion_path, salida, voz=None):
    guion = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    idioma = guion.get("idioma", "es")
    voz = voz or VOCES.get(idioma, VOCES["es"])
    salida = Path(salida); (salida / "voz").mkdir(parents=True, exist_ok=True)

    reloj, bloques, palabras_todas, partes = 0.0, [], [], []
    for i, e in enumerate(guion["escenas"], 1):
        texto = (e.get("narracion") or "").strip()
        mp3 = salida / "voz" / f"escena_{i:03d}.mp3"
        if not texto:
            e["duracion_s"] = e.get("duracion_s", 3.0)
            reloj += e["duracion_s"]
            continue
        _, pal = await sintetizar(texto, voz, mp3)
        dur = duracion_real(mp3) or (pal[-1][1] if pal else 3.0)
        cola = e.get("pausa_despues_s", 0.45)      # respiración entre escenas
        e["duracion_s"] = round(dur + cola, 3)
        e["audio"] = str(mp3.relative_to(salida))
        bloques.append((reloj, reloj + dur, texto))
        palabras_todas += [(reloj + a, reloj + b, w) for a, b, w in pal]
        partes.append((mp3, cola))
        reloj += e["duracion_s"]
        print(f"  escena {i:>2}  {e['duracion_s']:>5.1f}s  {texto[:56]}")

    # concatenar con silencios entre escenas
    lista = salida / "concat.txt"
    silencio = salida / "voz" / "_silencio.mp3"
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                    "-t", "0.45", "-q:a", "9", str(silencio)],
                   check=True, capture_output=True)
    with lista.open("w", encoding="utf-8") as fh:
        for mp3, _ in partes:
            fh.write(f"file '{mp3.resolve()}'\nfile '{silencio.resolve()}'\n")
    # Re-codificar, NO "-c copy". Cada MP3 lleva su propio retardo de codificador
    # (~40 ms), y al pegarlos en crudo ese retardo se acumula en cada junta: la
    # narración sale más larga que la suma de sus trozos, mientras que los
    # subtítulos y las duraciones de escena se calcularon sobre los trozos
    # sueltos. El resultado es una deriva creciente entre imagen, voz y
    # subtítulos. Medido con la estructura de MDH-001 (38 escenas + 38
    # silencios): "-c copy" se va +3,82 s al final; re-codificando el resultado
    # es exacto a la muestra.
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
                    "-c:a", "libmp3lame", "-q:a", "2", "-ar", "24000", "-ac", "1",
                    str(salida / "voz.mp3")], check=True, capture_output=True)

    escribir_srt(bloques, salida / "subtitulos.srt")
    # Sin marcas de tiempo por palabra no hay subtítulos quemados, y los
    # subtítulos quemados son lo único que se mueve durante el tramo central de
    # cada escena, que es estático por diseño. Un vídeo sin ellos se percibe
    # como un pase de diapositivas. Hasta el 18/08 esto fallaba en silencio.
    if not palabras_todas:
        print("::warning::El sintetizador no ha devuelto marcas de tiempo por palabra "
              "(WordBoundary). El vídeo saldrá SIN subtítulos quemados.")
    escribir_ass(palabras_todas, salida / "subtitulos.ass")
    print(f"Marcas de palabra: {len(palabras_todas)}")
    guion["duracion_total_s"] = round(reloj, 2)
    guion["voz_usada"] = voz
    (salida / "guion.timed.json").write_text(
        json.dumps(guion, ensure_ascii=False, indent=2), encoding="utf-8")

    m, s = divmod(reloj, 60)
    print(f"\nNarración: {int(m)}m {s:04.1f}s con la voz {voz}")
    print(f"Salida en {salida}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("-o", "--salida", required=True)
    ap.add_argument("--voz", default=None, help=f"por defecto según idioma: {VOCES}")
    a = ap.parse_args()
    asyncio.run(principal(a.guion, a.salida, a.voz))
