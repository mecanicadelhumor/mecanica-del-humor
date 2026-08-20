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


# Recorte del fragmento inicial. Ver fragmento_inicial() más abajo.
MAX_FRAG_S, MIN_HUECO_S, VENTANA_FRAG_S = 0.45, 0.15, 1.0


def _comunicar(texto, voz):
    """Crea el Communicate pidiendo EXPLÍCITAMENTE las marcas por palabra.

    Aquí estuvo el fallo que dejó TRES vídeos seguidos sin subtítulos
    quemados, del 18 al 19 de agosto.

    edge-tts cambió el 22/03/2026 (commit 4bdb8e4, rama 7.2.x) el valor por
    defecto del parámetro `boundary` de "WordBoundary" a "SentenceBoundary".
    Ese valor decide literalmente lo que la librería le pide al servicio de
    Microsoft en el mensaje speech.config:

        boundary="SentenceBoundary"  ->  "wordBoundaryEnabled":"false"
        boundary="WordBoundary"      ->  "wordBoundaryEnabled":"true"

    Con el nuevo valor por defecto, el servicio **no manda ni un solo evento
    WordBoundary**. El audio llega perfecto —por eso el fallo no se notaba
    escuchando— y la lista de marcas se queda vacía, así que escribir_ass()
    genera un .ass con cabecera y sin una sola línea de diálogo, y montaje.py
    lo quema sin error y sin efecto.

    Y entró solo, sin que nadie tocara este repositorio, porque
    requirements.txt no fijaba la versión: cada producción instalaba la última
    publicada. Ahora se hacen las dos cosas —fijar el rango de versión y pedir
    el parámetro— porque cualquiera de las dos bastaría, pero juntas cierran
    también la puerta a que vuelva por el otro lado.

    Las versiones anteriores a la 7 no aceptan `boundary`; si no existe, se
    reintenta sin él, que es justo el caso en el que el defecto por defecto
    era el bueno.
    """
    try:
        return edge_tts.Communicate(texto, voz, rate=RITMO, pitch=TONO,
                                    boundary="WordBoundary")
    except TypeError:
        return edge_tts.Communicate(texto, voz, rate=RITMO, pitch=TONO)


def fragmento_inicial(mp3):
    """Segundos a recortar por delante, o 0 si la escena arranca limpia.

    El sintetizador cuela de vez en cuando un trozo de palabra al principio de
    una escena: se oye una sílaba que no pertenece a ninguna frase. Silvestre
    lo detectó en MDH-001.en, en MDH-002.en y —esta es la que rompió el
    diagnóstico anterior— en el minuto 5:35 de MDH-002.es. No es un «falso
    arranque» del vídeo: como aquí se sintetiza una escena por petición, puede
    caer al principio de cualquiera.

    El patrón es inconfundible y por eso se puede recortar sin miedo: un trozo
    de sonido de menos de MAX_FRAG_S seguido de un silencio de al menos
    MIN_HUECO_S, todo dentro del primer segundo. El habla normal no hace eso.
    Si no encaja exactamente, se devuelve 0 y no se toca nada.
    """
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-t", str(VENTANA_FRAG_S + 1),
                        "-i", str(mp3), "-af", "silencedetect=n=-45dB:d=0.10",
                        "-f", "null", "-"], capture_output=True, text=True,
                       stdin=subprocess.DEVNULL)
    abierto = None
    for linea in r.stderr.splitlines():
        if "silence_start" in linea:
            try:
                abierto = float(linea.split("silence_start:")[1].strip().split()[0])
            except (IndexError, ValueError):
                abierto = None
        elif "silence_end" in linea and abierto is not None:
            try:
                fin = float(linea.split("silence_end:")[1].split("|")[0])
            except (IndexError, ValueError):
                abierto = None
                continue
            if abierto <= MAX_FRAG_S and (fin - abierto) >= MIN_HUECO_S and fin <= VENTANA_FRAG_S:
                return round(fin, 3)
            abierto = None
    return 0.0


def _recortar(mp3, desde_s):
    """Quita los primeros `desde_s` segundos del mp3, en su sitio."""
    tmp = mp3.with_suffix(".rec.mp3")
    subprocess.run(["ffmpeg", "-y", "-ss", str(desde_s), "-i", str(mp3),
                    "-c:a", "libmp3lame", "-q:a", "2", str(tmp)],
                   check=True, capture_output=True, stdin=subprocess.DEVNULL)
    tmp.replace(mp3)


async def sintetizar(texto, voz, destino):
    """Devuelve (duracion_s, [(ini_s, fin_s, palabra), ...], n_marcas_de_frase).

    La tercera cifra solo sirve para diagnosticar: si llegan marcas de frase y
    ninguna de palabra, el problema es el parámetro `boundary` y no la red.
    """
    com = _comunicar(texto, voz)
    audio, palabras, n_frases = bytearray(), [], 0
    async for trozo in com.stream():
        if trozo["type"] == "audio":
            audio.extend(trozo["data"])
        elif trozo["type"] == "WordBoundary":
            ini = trozo["offset"] / 1e7
            dur = trozo["duration"] / 1e7
            palabras.append((ini, ini + dur, trozo["text"]))
        elif trozo["type"] == "SentenceBoundary":
            n_frases += 1
    destino.write_bytes(bytes(audio))
    dur = palabras[-1][1] if palabras else 0.0
    return dur, palabras, n_frases


def duracion_real(path):
    """Duración exacta del mp3 según ffprobe (más fiable que la última palabra)."""
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True,
                       stdin=subprocess.DEVNULL)
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
    frases_totales, recortadas = 0, []
    for i, e in enumerate(guion["escenas"], 1):
        texto = (e.get("narracion") or "").strip()
        mp3 = salida / "voz" / f"escena_{i:03d}.mp3"
        if not texto:
            e["duracion_s"] = e.get("duracion_s", 3.0)
            reloj += e["duracion_s"]
            continue
        _, pal, n_fr = await sintetizar(texto, voz, mp3)
        frases_totales += n_fr
        # Sílaba suelta al principio de la escena: se recorta si el patrón
        # encaja exactamente. Las marcas de palabra vienen referidas al audio
        # SIN recortar, así que hay que restarles lo mismo o los subtítulos
        # quedarían adelantados esa cantidad durante toda la escena.
        recorte = fragmento_inicial(mp3)
        if recorte:
            _recortar(mp3, recorte)
            pal = [(max(0.0, a - recorte), max(0.0, b - recorte), w) for a, b, w in pal]
            recortadas.append((i, recorte))
            print(f"  escena {i:>2}  recortada sílaba suelta de {recorte:.2f}s al principio")
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
                   check=True, capture_output=True, stdin=subprocess.DEVNULL)
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
                    str(salida / "voz.mp3")], check=True, capture_output=True,
                   stdin=subprocess.DEVNULL)

    escribir_srt(bloques, salida / "subtitulos.srt")
    # Sin marcas de tiempo por palabra no hay subtítulos quemados, y los
    # subtítulos quemados son lo único que se mueve durante el tramo central de
    # cada escena, que es estático por diseño. Un vídeo sin ellos se percibe
    # como un pase de diapositivas. Hasta el 18/08 esto fallaba en silencio.
    if not palabras_todas:
        if frases_totales:
            print(f"::error::El servicio ha devuelto {frases_totales} marcas de FRASE y "
                  "ninguna de PALABRA. Ese es el síntoma exacto de que «boundary» no está "
                  "pidiendo WordBoundary: mira _comunicar() y la versión de edge-tts "
                  "instalada (requirements.txt fija >=7,<8).")
        else:
            print("::warning::El sintetizador no ha devuelto marcas de tiempo por palabra "
                  "(WordBoundary) ni de frase. El vídeo saldrá SIN subtítulos quemados.")
    escribir_ass(palabras_todas, salida / "subtitulos.ass")
    print(f"Marcas de palabra: {len(palabras_todas)}")
    if recortadas:
        detalle = ", ".join(f"escena {n} ({d:.2f}s)" for n, d in recortadas)
        print(f"::warning::Sílabas sueltas recortadas en {len(recortadas)} escena(s): {detalle}")
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
