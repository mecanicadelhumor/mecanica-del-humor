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
import base64
import hashlib
import json
import os
import re
import subprocess
import time
import wave
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


# ---------------------------------------------------------------------------
# C7 · Gemini TTS en los Shorts (07-09/09/2026, versión 5.1 y 6 del plan).
#
# Se escribió la semana del 7 con --motor edge por defecto para no tocar la
# producción de esa semana ni gastar la ranura de cambio (que era de C19+C16).
# El valor por defecto ha pasado a "gemini" el lunes 14/09 (revisión diaria:
# MDS-016 salió bien el sábado/domingo/hoy y ESTADO.md decía OK), confirmando
# antes las dos cosas que este fichero no podía arreglar por sí solo porque
# viven en .github/workflows/producir.yml (protegido, ver REGLAS.md regla
# 11.7): el paso de voz.py ya expone el secreto GEMINI_API_KEY en su entorno
# (verificado, línea «Sintetizar narración») y `google-genai` ya está en
# requirements.txt, que sí es mío.
#
# Solo se usa en Shorts (formato "corto"): un episodio largo son ~40 escenas
# y el nivel gratuito da 10 peticiones al día POR MODELO — no cabe en un día
# (ver C27 en la versión 6.1 del plan, que sí lo resuelve con una caché por
# adelantado y un workflow nuevo, todavía sin escribir).
#
# Las salvaguardas son las de la versión 5.1, sin las cuales esto no se toca:
#   1. --motor {edge,gemini}, con respaldo automático e inmediato a edge-tts
#      ante CUALQUIER fallo de Gemini en una escena (cuota, red, respuesta
#      vacía). Un vídeo con una voz peor es mejor que un día sin vídeo.
#   2. El motor real usado se escribe escena a escena (e["motor_voz"]) para
#      que se vea en el expediente, no que se descubra escuchando.
#   3. 25 segundos entre llamadas REALES a Gemini (el límite es 3/min); una
#      escena servida desde caché o ya resuelta por respaldo no cuenta.
#   4. Control de ritmo por escena (e["ritmo_pal_s"]): aviso si cae fuera de
#      1,6-3,2 palabras/segundo. No bloquea — el vídeo se sincroniza con la
#      duración real— pero se ve.
#   5. El .srt no cambia: se sigue escribiendo por bloques de escena, no por
#      palabra. Lo que sí muere es el .ass por escena Gemini (la API no da
#      WordBoundary), y con él el canario «lineas_ass» de qa.py — sustituido
#      ahí por uno nuevo que compara la duración calculada con la real de
#      voz.mp3, que es lo que de verdad hay que vigilar.
#   6. Se enciende con un episodio (el lunes 14, hecho), no con la semana:
#      si algún día siguiente ESTADO.md no dice OK por causa de la voz de un
#      Short, se vuelve a "edge" cambiando el valor por defecto de este mismo
#      argparse — es una línea, no hace falta más.
#
# Y la caché, que es la pieza de la que depende además que el episodio largo
# pueda dejar edge-tts más adelante (C27): cada escena sintetizada con Gemini
# se guarda en 03_produccion/cache_voz/<sha256(narración+motor+voz)>.mp3, y
# antes de pedirle nada a la API se mira si ya está — así una producción que
# se rehace a mano no vuelve a gastar cuota (el 07/09 hubo que rehacer
# MDS-011 y se pagó dos veces), y un guion corregido solo resintetiza las
# escenas que cambiaron. La caché es SOLO de Gemini: edge-tts no tiene cuota
# que ahorrar y cachearlo perdería las marcas de palabra que sí necesita.
CACHE_VOZ_DIR = Path(__file__).resolve().parent.parent / "cache_voz"
MODELO_GEMINI = "gemini-3.1-flash-tts-preview"
# El episodio largo usa OTRO modelo, con cuota diaria propia, para no comerse la
# de los cinco Shorts de la semana. Tiene que ser exactamente el mismo literal
# que usa voz_precache.py o el precacheo de toda la semana no se encuentra.
MODELO_GEMINI_LARGO = "gemini-2.5-flash-preview-tts"
VOZ_GEMINI_NARRADOR = "Charon"    # grave, tranquila. El que explica.
VOZ_GEMINI_ESCEPTICO = "Puck"     # más alta y viva. El que interrumpe.
RITMO_GEMINI_HZ = 24000           # Hz que devuelve la API
ESPERA_ENTRE_LLAMADAS_GEMINI = 25.0   # RPM = 3, o sea una cada 20s. 25 con margen.
RITMO_PAL_S_MIN, RITMO_PAL_S_MAX = 1.6, 3.2

# Dirección de actor SIN pausas en segundos (la versión 5.1 midió que pedir
# pausas se toma al pie de la letra y mete silencios de decenas de segundos:
# 83s para un guion de 41s de voz real). Las pausas entre escenas las sigue
# poniendo `pausa_despues_s`, determinista. Lo que se le pide al modelo es lo
# que edge-tts no sabe hacer: contar en vez de leer, y enlazar una escena con
# la siguiente.

# ----------------------------------------------------------------------------
# C33 (14/09/2026) · La dirección de actor deja de ser una constante
#
# Hasta hoy había UNA sola frase de dirección, idéntica para las seis escenas
# del Short, y decía «cuéntala con la entonación de quien cuenta algo que le
# hace gracia». Dos consecuencias, las dos señaladas por la dirección el mismo
# día en que se encendió Gemini:
#
#   1. **Se ríe todo el rato.** Ningún guion lleva risas escritas —comprobado
#      sobre MDS-016 a MDS-020: cero—, así que las risas las pone el modelo, y
#      las pone porque se las pedimos en cada escena, incluida la del dato y la
#      del «y aquí falla». Una instrucción de tono aplicada a las seis escenas
#      por igual no es tono: es un tic.
#   2. **Suena inconexo.** Cada escena es una llamada independiente, así que el
#      modelo le pone a cada fragmento su propia entonación de arranque y su
#      propio punto final. Seis fragmentos autónomos seguidos suenan como seis
#      frases sueltas por mucho que el guion tenga hilo — que es exactamente lo
#      que se describió como «resumido sin puntos en común y difícil de
#      seguir». El guion de un Short se cose desde el 12/09 (las tres pruebas
#      de `guionista_corto.md`); lo que faltaba era coser también la voz.
#
# El arreglo es determinista y no toca al guionista: todo lo que hace falta
# para dirigir una escena ya está en el guion.
#
#   - `tipo` dice qué papel hace la escena (dato, comparación, cierre...).
#   - la posición dice si abre o cierra.
#   - `pausa_despues_s` de la escena ANTERIOR dice si esta es el remate:
#     `guionista_corto.md` manda 1,2-1,5 s entre planteamiento y remate y
#     0,2-0,6 s en el resto, así que el umbral separa las dos poblaciones sin
#     ambigüedad (medido sobre los cinco guiones sin producir: 4 remates
#     detectados, los 4 reales, ningún falso positivo).
#   - las comillas dicen dónde va el retintín, que es el único sitio donde la
#     ironía está escrita de verdad.
#
# Y la parte que arregla el corte, que es la menos obvia: **cuando después de
# una frase viene un silencio nuestro, hay que pedir que la frase quede
# suspendida.** Hoy el modelo cierra la entonación y encima le metemos 1,35 s
# de silencio: eso no es una pausa dramática, es un final seguido de otro
# principio. La pausa la seguimos poniendo nosotros —la versión 5.1 midió que
# pedírsela al modelo da silencios de decenas de segundos— pero le decimos qué
# hacer con la frase que la precede.
# ----------------------------------------------------------------------------

# Por encima de este umbral, la pausa de una escena es «la pausa es el chiste»
# de `guionista_corto.md` y la escena siguiente es el remate. Por debajo es
# respiración entre escenas.
PAUSA_DE_REMATE_S = 1.2

# Qué papel hace cada tipo de escena. Los tipos son los de `esquema_guion.json`;
# uno que no esté aquí cae en «explicacion», que es la dirección más neutra.
PAPEL_POR_TIPO = {
    "titulo": "apertura",
    "enunciado": "planteamiento",
    "comparacion": "contraste",
    "dato": "cifra",
    "lista": "enumeracion",
    "cita": "cita",
    "diagrama": "explicacion",
    "figura": "explicacion",
    "cierre": "objecion",
}

# Una frase por papel. Concretas a propósito: «tono irónico» no es una
# instrucción, «lo que va entre comillas se dice con retintín» sí.
DIRECCION_POR_PAPEL = {
    "apertura":
        "Es la primera frase del vídeo y no hay presentación ni preámbulo: "
        "entras en frío, en mitad de una historia que ya ha empezado. Tono de "
        "conversación, como quien se lo cuenta a un amigo. Ni locutor ni anuncio.",
    "planteamiento":
        "Es el planteamiento. Cuéntalo llano y sin subrayar nada: lo que viene "
        "después es la gracia, y anunciarla la estropea.",
    "remate":
        "Es el remate, y llega justo después de un silencio. Dilo del tirón, sin "
        "pausas por dentro, y dilo completamente en serio, como si fuera lo más "
        "normal del mundo. Ahí está la gracia. No lo subrayes, no cambies de tono "
        "al llegar a la última palabra y sobre todo no te rías tú.",
    "contraste":
        "Son dos mitades enfrentadas. Di la primera en un tono y cambia claramente "
        "de color de voz en la segunda. El contraste lo hace el tono, no el volumen.",
    "cifra":
        "Hay una cifra en esta frase. El resto va del tirón y la cifra se dice algo "
        "más despacio y muy clara. Sin énfasis de anuncio: no estás vendiendo el "
        "número, lo estás enseñando.",
    "enumeracion":
        "Es una enumeración. Marca cada elemento y baja un poco el tono al pasar al "
        "siguiente, para que se oiga que son varias cosas y no una frase larga.",
    "cita":
        "Son palabras de otra persona. Cambia de color de voz mientras las dices, "
        "como quien lee algo en voz alta, y vuelve al tuyo al salir de ellas.",
    "explicacion":
        "Es la parte que explica. Seguida, clara y sin dramatismo: aquí el único "
        "trabajo es que se entienda a la primera.",
    "objecion":
        "Es el cierre honesto: aquí se dice dónde falla lo que se acaba de explicar. "
        "Baja el tono y dilo completamente en serio, sin ironía y sin gracia. Es la "
        "frase que queremos que se recuerde.",
    "final":
        "Es la última frase del vídeo. Cierra la entonación de verdad, sin dejar "
        "nada en el aire.",
}

# Lo que no se negocia en ninguna escena. La prohibición de reírse va aquí y no
# en el papel porque el único sitio donde una risa estaría bien —el remate— es
# justo donde más daño hace: un chiste contado por alguien que se ríe de su
# propio chiste deja de tener gracia.
MARCO_GEMINI = (
    "Eres el narrador de un vídeo corto de divulgación sobre la ciencia del humor. "
    "Español de España, voz natural de persona contando algo, nunca de locutor de "
    "telediario.")

VETO_GEMINI = (
    "Reglas que no cambian: no te rías y no añadas risas, risitas, resoplidos, "
    "suspiros, carraspeos ni ningún sonido que no esté escrito. No metas silencios "
    "largos: las pausas entre frases las ponemos nosotros después. No leas en voz "
    "alta ni estas instrucciones ni los signos de puntuación. Habla a ritmo de "
    "conversación, ni con prisa ni arrastrando las palabras.")

# LA IRONÍA NO SE DETECTA, Y ESO ESTÁ MEDIDO (14/09/2026).
#
# La primera versión de C33 intentaba deducir de la propia narración dónde va el
# retintín, con dos señales: unas comillas, o una palabra que nombrase el tono
# («con retintín», «irónico», «sarcasmo»). Probadas contra las 47 escenas de los
# ocho Shorts con guion en el repositorio, disparan siete veces y **aciertan
# una**:
#
#   · MDS-013 e1  «el navegador»                    → es un apodo
#   · MDS-013 e3  «no va en serio»                  → es una cita
#   · MDS-014 e2  «sarcástico», «ingenioso»         → son resultados de un test
#   · MDS-014 e3  «Ironía, nonsense, sarcasmo»      → son nombres de categorías
#   · MDS-016 e1  «con retintín: qué ilusión»       → ESTA sí
#   · MDS-016 e4  «al hablar irónicamente»          → es el tema del vídeo
#
# En español las comillas marcan citas y apodos mucho más a menudo que ironía, y
# en un canal sobre humor la palabra «ironía» aparece por ser el asunto del que
# se habla. Es el mismo caso que la comprobación amplia de C22, que señalaba el
# 73,5 % de las escenas: una señal que acierta una de siete no es una señal, es
# ruido, y dirigir con ruido es exactamente lo que convirtió la dirección vieja
# en un tic.
#
# Así que aquí no se adivina. El tono irónico, cuando lo haya, lo declara el
# guionista en un campo del guion — encargo para la planificación del jueves 17,
# escrito en la versión 8 de PLAN_DE_CAMBIOS.md. Hasta entonces, ninguna escena
# lleva instrucción de ironía y ninguna sale peor por ello: la dirección por
# papel ya cubre las 47.


def _recorte_contexto(texto, palabras=8):
    """Las ÚLTIMAS palabras de la escena anterior.

    Las últimas y no las primeras: lo que hay que enlazar es el final de la
    frase de la que se viene, que es donde quedó la entonación.
    """
    trozos = (texto or "").split()
    return ("…" if len(trozos) > palabras else "") + " ".join(trozos[-palabras:])


def _papel_escena(escenas, i):
    """Qué papel hace la escena `i` (1-based). Determinista, sin heurística.

    El orden de las reglas importa: «remate» gana sobre el tipo (una escena de
    comparación que llega tras un silencio de 1,35 s es un remate antes que una
    comparación), y «apertura» gana sobre todo porque la escena 1 de un Short
    tiene un trabajo que no tiene ninguna otra.
    """
    if i == 1:
        return "apertura"
    previa = escenas[i - 2]
    if float(previa.get("pausa_despues_s") or 0.0) >= PAUSA_DE_REMATE_S:
        return "remate"
    tipo = (escenas[i - 1].get("tipo") or "").strip().lower()
    papel = PAPEL_POR_TIPO.get(tipo, "explicacion")
    if i == len(escenas) and papel not in ("objecion",):
        return "final"
    return papel


def direccion_escena(escenas, i, texto):
    """Construye la dirección de actor de la escena `i` (1-based).

    Devuelve `(prompt_completo, papel)`. `papel` se guarda en `ficha.json` para
    poder revisar en el expediente qué se le pidió a cada escena sin tener que
    escuchar el vídeo entero — es la misma idea que `motor_voz`.
    """
    papel = _papel_escena(escenas, i)
    partes = [MARCO_GEMINI, DIRECCION_POR_PAPEL[papel]]

    # Continuidad hacia atrás: de dónde viene esta frase.
    if i > 1:
        # `hablable()` también aquí: el resaltado está prohibido en «narracion»
        # (C29), pero si alguna vez se cuela no tiene por qué llegar al prompt.
        antes = _recorte_contexto(hablable(escenas[i - 2].get("narracion") or ""), 8)
        if antes:
            # Sin comillas y con el aviso pegado: unas comillas alrededor del
            # contexto lo hacen indistinguible del texto que sí hay que locutar.
            partes.append(
                f"Contexto, que NO se locuta: la frase anterior terminaba hablando de "
                f"esto — {antes} — así que enlaza con ello y no arranques como si "
                "abrieras el vídeo.")

    # Continuidad hacia delante: qué pasa después de esta frase. Es la parte que
    # convierte un silencio nuestro en una pausa dramática en vez de en un corte.
    propia = float((escenas[i - 1]).get("pausa_despues_s") or 0.0)
    if i < len(escenas):
        if propia >= PAUSA_DE_REMATE_S:
            partes.append(
                "Después de esta frase hay un silencio y luego llega el remate. Deja la "
                "frase suspendida, en el aire, sin cerrar la entonación: el silencio lo "
                "ponemos nosotros y tiene que sonar a espera, no a punto final.")
        else:
            partes.append(
                "La frase sigue teniendo continuación después, así que no cierres la "
                "entonación del todo.")
    else:
        partes.append(
            "Con esta frase acaba el vídeo: cierra la entonación de verdad, sin dejar "
            "nada en el aire.")

    partes.append(VETO_GEMINI)
    cuerpo = " ".join(partes)
    return (
        f"[Instrucciones para el actor. No se leen en voz alta.]\n{cuerpo}\n"
        f"[Fin de las instrucciones. Locuta únicamente el texto que va debajo.]\n\n"
        f"{texto}"
    ), papel


def _cache_voz_ruta(texto, motor, voz, direccion=""):
    """Clave de caché por contenido.

    Desde C33 la dirección de actor entra en la clave: dos escenas con el mismo
    texto pero distinto papel —o la misma escena antes y después de que cambie
    la dirección— tienen que sonar distinto, y una caché que solo mire el texto
    devolvería la toma vieja sin decir nada. El efecto secundario de meterla es
    justamente el que se quiere: cambiar la dirección invalida la caché entera y
    la siguiente producción se sintetiza de cero.
    """
    clave = hashlib.sha256(
        f"{texto}|{motor}|{voz}|{direccion}".encode("utf-8")).hexdigest()
    return CACHE_VOZ_DIR / f"{clave}.mp3"


def _gemini_cliente():
    if not os.environ.get("GEMINI_API_KEY"):
        raise RuntimeError("Falta GEMINI_API_KEY en el entorno.")
    from google import genai
    return genai.Client()


def _gemini_pcm(cli, modelo, texto_dirigido, voz_gemini):
    """Una sola llamada, una sola voz (cada escena tiene un único hablante).

    Sin reintentos aquí: en producción, cualquier fallo cae al respaldo
    edge-tts (ver `_sintetizar_con_motor`) en vez de reintentar y arriesgar
    el RPM de 3/min o, peor, el RPD de 10/día con una escena que de todas
    formas va a tener voz de respaldo.
    """
    if hasattr(cli, "interactions"):
        inter = cli.interactions.create(
            model=modelo, input=texto_dirigido,
            response_format={"type": "audio"},
            generation_config={"speech_config": [{"voice": voz_gemini}]})
        return base64.b64decode(inter.output_audio.data)

    from google.genai import types
    cfg = types.SpeechConfig(voice_config=types.VoiceConfig(
        prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voz_gemini)))
    r = cli.models.generate_content(
        model=modelo, contents=texto_dirigido,
        config=types.GenerateContentConfig(response_modalities=["AUDIO"],
                                            speech_config=cfg))
    return r.candidates[0].content.parts[0].inline_data.data


def _pcm_a_mp3(pcm, hz, destino):
    tmp = destino.with_suffix(".pcm.wav")
    with wave.open(str(tmp), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(hz)
        w.writeframes(pcm)
    subprocess.run(["ffmpeg", "-y", "-i", str(tmp), "-c:a", "libmp3lame", "-q:a", "2",
                    str(destino)], check=True, capture_output=True, stdin=subprocess.DEVNULL)
    tmp.unlink(missing_ok=True)


async def _sintetizar_con_motor(texto, papel, voz_edge, mp3, indice, motor, estado,
                                direccion=None, modelo=None, solo_cache=False):
    """Sintetiza una escena con el motor pedido. Siempre escribe `mp3`.

    Devuelve (palabras, n_frases, motor_usado). `palabras` viene vacío para
    cualquier resultado de Gemini (caché o llamada real): la API no da
    WordBoundary, así que esas escenas no aportan marcas al .ass — es lo
    esperado, no un fallo (ver el canario nuevo en qa.py).

    `estado` es un dict compartido entre las escenas de una misma
    producción: {"agotado": bool, "ultima": monotonic|0.0, "cliente": None}.
    Si una escena anterior ya agotó la cuota DIARIA de Gemini, el resto de
    la producción va directa a edge-tts sin más intentos ni esperas.
    """
    if motor != "gemini":
        _, pal, n_fr = await sintetizar(texto, voz_edge, mp3)
        return pal, n_fr, "edge"

    voz_gemini = VOZ_GEMINI_ESCEPTICO if papel == "esceptico" else VOZ_GEMINI_NARRADOR
    # Sin dirección (una llamada suelta, p. ej. desde una prueba) se manda el
    # texto pelado: es peor, pero nunca peor que no tener voz.
    dirigido = direccion or texto
    # La clave de caché lleva el NOMBRE EXACTO del modelo, no la palabra
    # "gemini": son dos modelos con cuota independiente y su audio no es
    # intercambiable. (Hasta el 14/09 los Shorts se cacheaban con el literal
    # "gemini"; esa caché la invalida C33 de todas formas al meter la dirección
    # de actor en la clave, así que este es el momento de dejar de arrastrarlo.)
    clave_modelo = modelo or MODELO_GEMINI
    cache = _cache_voz_ruta(texto, clave_modelo, voz_gemini, dirigido)
    if cache.exists():
        mp3.write_bytes(cache.read_bytes())
        return [], 0, "gemini (caché)"

    # Pieza C de C27: el episodio largo NO llama a la API el día de producción.
    # Sus cuarenta escenas no caben en las diez peticiones diarias, así que las
    # sintetiza `voz_precache.py` de martes a viernes y aquí solo se recogen de
    # la caché. Lo que no esté cacheado el sábado sale con edge-tts, que es la
    # misma política de degradación de siempre: un vídeo con alguna escena de
    # voz peor es mejor que un sábado sin vídeo.
    if solo_cache:
        _, pal, n_fr = await sintetizar(texto, voz_edge, mp3)
        return pal, n_fr, "edge (sin precacheo)"

    if not estado["agotado"]:
        espera = ESPERA_ENTRE_LLAMADAS_GEMINI - (time.monotonic() - estado["ultima"])
        if estado["ultima"] and espera > 0:
            await asyncio.sleep(espera)
        try:
            cli = estado["cliente"] or _gemini_cliente()
            estado["cliente"] = cli
            pcm = _gemini_pcm(cli, MODELO_GEMINI, dirigido, voz_gemini)
            estado["ultima"] = time.monotonic()
            _pcm_a_mp3(pcm, RITMO_GEMINI_HZ, mp3)
            CACHE_VOZ_DIR.mkdir(parents=True, exist_ok=True)
            cache.write_bytes(mp3.read_bytes())
            return [], 0, "gemini"
        except Exception as exc:
            estado["ultima"] = time.monotonic()
            msg = str(exc)
            agotado_por_dia = ("RESOURCE_EXHAUSTED" in msg or "429" in msg) and (
                "per day" in msg.lower() or "perday" in msg.lower().replace(" ", ""))
            if agotado_por_dia:
                estado["agotado"] = True
                print(f"::warning::escena {indice}: cuota DIARIA de Gemini agotada; "
                      f"el resto de esta producción va directa a edge-tts.")
            print(f"::warning::escena {indice}: Gemini ha fallado, respaldo automático "
                  f"a edge-tts. Error: {msg[:200]!r}")

    _, pal, n_fr = await sintetizar(texto, voz_edge, mp3)
    return pal, n_fr, "edge (respaldo)"


# ---------------------------------------------------------------------------
# La narración es lo ÚNICO que recibe el sintetizador, y el sintetizador lee lo
# que le llega, literalmente. El 7 de septiembre de 2026 MDS-011 salió
# publicado diciendo «guion bajo pensamiento divergente guion bajo» porque el
# guionista escribió «_pensamiento divergente_» dentro de `narracion`.
#
# El resaltado existe y es correcto —*ámbar* para el acento de la frase, _cian_
# para el término del oficio— pero es de PANTALLA: lo interpreta `rico()` en
# escena.html sobre `texto`, `cifra`, `titulo`, `pie`... En `narracion` no
# significa nada y sí se oye.
#
# Esto se hace aquí, en el punto exacto en el que la narración deja de ser un
# dato del guion y pasa a ser voz, porque así arregla de una vez las DOS
# salidas que se derivan de ese mismo texto: el audio y el `.srt` (que se
# escribe con esta misma variable, más abajo en `bloques`). Y arregla también
# los guiones que ya están escritos, sin tocarlos.
#
# El validador avisa del defecto para que el guionista deje de cometerlo; esto
# impide que llegue al público mientras tanto. Son las dos capas, no una.
MARCAS_DE_PANTALLA = re.compile(r"[*_`#\[\]|~]")


def hablable(s):
    """La narración tal y como hay que decirla en voz alta.

    Quita el marcado de resaltado —que es de pantalla— sin tocar ni una
    palabra. Determinista y sin red: mismo guion, mismo audio.
    """
    return re.sub(r"\s{2,}", " ", MARCAS_DE_PANTALLA.sub("", str(s or ""))).strip()



def hms(seg, coma=","):
    h = int(seg // 3600); m = int(seg % 3600 // 60); s = seg % 60
    return f"{h:02d}:{m:02d}:{int(s):02d}{coma}{int(round((s%1)*1000)):03d}"


# Recorte del fragmento inicial. Ver fragmento_inicial() más abajo.
# MIN_FRAG_S es el que faltaba y el que costó el arranque de MDH-003.es.
# «abierto» es el instante en que empieza un silencio, así que para que lo de
# delante sea una sílaba suelta tiene que haber sonado ALGO: si el silencio
# empieza en 0 (o antes), lo de delante no es una sílaba, es el colchón de
# entrada del propio mp3. Sin este suelo, el patrón encajaba en el colchón de
# cualquier escena limpia.
MIN_FRAG_S, MAX_FRAG_S, MIN_HUECO_S, VENTANA_FRAG_S = 0.05, 0.45, 0.15, 1.0


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
    una escena: se oye una sílaba que no pertenece a ninguna frase. El codirector
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
            if (MIN_FRAG_S <= abierto <= MAX_FRAG_S
                    and (fin - abierto) >= MIN_HUECO_S and fin <= VENTANA_FRAG_S):
                return round(fin, 3)
            abierto = None
    return 0.0


def _recortar(mp3, desde_s):
    """Quita los primeros `desde_s` segundos del mp3, en su sitio."""
    tmp = mp3.with_suffix(".rec.mp3")
    # `atrim` y no «-ss antes de -i»: sobre un mp3, el salto de entrada va a la
    # trama más cercana y se pasa. Medido, pedirle 0,250 s quitaba 0,261 s — y
    # esos 11 ms se los come el ataque de la primera palabra.
    subprocess.run(["ffmpeg", "-y", "-i", str(mp3),
                    "-af", f"atrim=start={desde_s},asetpts=N/SR/TB",
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


async def principal(guion_path, salida, voz=None, motor="edge"):
    guion = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    idioma = guion.get("idioma", "es")
    voz = voz or VOCES.get(idioma, VOCES["es"])
    salida = Path(salida); (salida / "voz").mkdir(parents=True, exist_ok=True)

    # C7 + C27: Gemini en los dos formatos, pero por caminos distintos.
    #
    #   · Short  → llamada en vivo. Seis escenas caben en las diez peticiones
    #              diarias del nivel gratuito, con margen para el respaldo.
    #   · Largo  → SOLO caché, nunca llamada. Cuarenta escenas no caben en un
    #              día; las sintetiza `voz_precache.py` de martes a viernes con
    #              su propio modelo, y aquí solo se recogen. Lo que falte sale
    #              con edge-tts y queda dicho escena a escena en `ficha.json`.
    es_corto = guion.get("formato") == "corto"
    usar_gemini = motor == "gemini" and es_corto
    largo_desde_cache = motor == "gemini" and guion.get("formato") == "largo"
    modelo_gemini = MODELO_GEMINI if es_corto else MODELO_GEMINI_LARGO
    motor_pedido = "gemini" if (usar_gemini or largo_desde_cache) else "edge"
    estado_gemini = {"agotado": False, "ultima": 0.0, "cliente": None}
    if largo_desde_cache:
        print(f"::notice::episodio largo con --motor gemini: se usa SOLO la caché de "
              f"{MODELO_GEMINI_LARGO} (C27). Las escenas sin precachear salen con "
              f"edge-tts; mira `motor_voz` escena a escena en el expediente.")
    elif motor == "gemini" and not usar_gemini:
        print(f"::notice::--motor gemini pedido pero formato=«{guion.get('formato')}», "
              f"que no es ni «corto» ni «largo». Esta producción va con edge-tts.")

    reloj, bloques, palabras_todas, partes = 0.0, [], [], []
    frases_totales, recortadas = 0, []
    for i, e in enumerate(guion["escenas"], 1):
        crudo = (e.get("narracion") or "").strip()
        texto = hablable(crudo)
        if texto != crudo:
            print(f"::warning::escena {i}: la narración traía marcado de resaltado "
                  f"(* o _) y se ha quitado antes de sintetizar. El resaltado es de "
                  f"pantalla; en «narracion» el sintetizador lo lee en voz alta.")
        mp3 = salida / "voz" / f"escena_{i:03d}.mp3"
        if not texto:
            e["duracion_s"] = e.get("duracion_s", 3.0)
            reloj += e["duracion_s"]
            continue
        papel = "esceptico" if e.get("voz") == "esceptico" else "narrador"
        # C33: la dirección de actor se construye por escena a partir del
        # propio guion (tipo, posición, pausa de la escena anterior, comillas).
        # Solo sirve para Gemini; edge-tts no la lee.
        dirigido, papel_escena = direccion_escena(guion["escenas"], i, texto)
        e["direccion_voz"] = papel_escena
        pal, n_fr, motor_usado = await _sintetizar_con_motor(
            texto, papel, voz, mp3, i, motor_pedido, estado_gemini,
            direccion=dirigido if (usar_gemini or largo_desde_cache) else None,
            modelo=modelo_gemini, solo_cache=largo_desde_cache)
        frases_totales += n_fr
        # Sílaba suelta al principio de la escena: el patrón se midió sobre
        # edge-tts (ver fragmento_inicial) y la red de seguridad de abajo
        # depende de las marcas de palabra, que Gemini no da. Así que este
        # recorte solo se intenta cuando la escena de verdad vino de
        # edge-tts, sea como motor principal o como respaldo.
        recorte = 0.0
        if motor_usado.startswith("edge"):
            recorte = fragmento_inicial(mp3)
            # Red de seguridad: edge-tts nos dice en qué milisegundo empieza
            # la primera palabra. Si el recorte llega hasta ahí, lo que
            # íbamos a tirar no era una sílaba de más: era el principio de la
            # narración. Se avisa y no se toca.
            if recorte and pal and recorte > pal[0][0]:
                print(f"::warning::escena {i}: recorte de {recorte:.2f}s descartado — "
                      f"se metía en la primera palabra, que empieza en {pal[0][0]:.2f}s")
                recorte = 0.0
            if recorte:
                _recortar(mp3, recorte)
                pal = [(max(0.0, a - recorte), max(0.0, b - recorte), w) for a, b, w in pal]
                recortadas.append((i, recorte))
                print(f"  escena {i:>2}  recortada sílaba suelta de {recorte:.2f}s al principio")
        dur = duracion_real(mp3) or (pal[-1][1] if pal else 3.0)
        cola = e.get("pausa_despues_s", 0.45)      # respiración entre escenas
        e["duracion_s"] = round(dur + cola, 3)
        e["audio"] = str(mp3.relative_to(salida))
        e["motor_voz"] = motor_usado
        # Control de ritmo (salvaguarda 4 de C7): fuera de 1,6-3,2 pal/s es la
        # firma de la pista plana de Gemini (corría al doble, 4,74 pal/s en
        # la prueba del 04/09). No bloquea —el vídeo se sincroniza con `dur`
        # real, así que nada se desincroniza— pero queda escrito para verlo
        # en el expediente sin tener que escuchar.
        ritmo = round(len(texto.split()) / dur, 2) if dur else 0.0
        e["ritmo_pal_s"] = ritmo
        if not (RITMO_PAL_S_MIN <= ritmo <= RITMO_PAL_S_MAX):
            print(f"::warning::escena {i}: ritmo {ritmo} palabras/s fuera de "
                  f"{RITMO_PAL_S_MIN}-{RITMO_PAL_S_MAX} (motor {motor_usado}).")
        bloques.append((reloj, reloj + dur, texto))
        palabras_todas += [(reloj + a, reloj + b, w) for a, b, w in pal]
        partes.append((mp3, cola))
        reloj += e["duracion_s"]
        print(f"  escena {i:>2}  {e['duracion_s']:>5.1f}s  [{motor_usado}] "
              f"[{papel_escena}]  {texto[:44]}")

    # Concatenar con silencios entre escenas — cada uno con la pausa REAL de
    # esa escena («cola», ya guardada en `partes` desde el bucle de arriba),
    # no un valor fijo.
    #
    # Bug encontrado el 11/09/2026 revisando `sincronia_voz()` (el canario que
    # se añadió ayer): este bloque generaba un único `_silencio.mp3` de 0,45s
    # fijos y lo insertaba después de CADA escena, mientras que
    # `e["duracion_s"]` (la que usa `render.py` para medir cuánto dura cada
    # escena en el vídeo) se calculaba con `dur + cola`, y `cola` casi nunca
    # es 0,45 — va de 0,2 a 1,35 según la escena. Resultado: el vídeo mudo y
    # `voz.mp3` llevaban duraciones de escena distintas desde la primera
    # escena, y el error se acumulaba durante todo el vídeo. Medido en
    # MDS-015 (cinco escenas, pausas de 0,2 a 1,3s): 0,85s de desfase real
    # (`sincronia_voz` en `qa.py`), que cuadra con `sum(cola_i) - 0,45*N =
    # 0,9s` calculado a mano sobre ese mismo guion.
    #
    # Primer intento, descartado: generar un `_silencio_<dur>.mp3` por cada
    # pausa distinta e insertarlos con el demuxer `concat` de siempre (una
    # lista de ficheros). Funciona en un Short, pero cada mp3 de silencio muy
    # corto sale con su propio redondeo de fotograma al codificarlo suelto
    # (medido: pedir 0,45s da un fichero de 0,504s; pedir 0,9s da 0,96s), y
    # ese redondeo SÍ se acumula una vez por escena. En un Short de 5 escenas
    # no se nota (0,08s), pero en un episodio de 40 se va a 1,6s — peor que
    # el bug que se quería arreglar.
    #
    # Arreglo de verdad: nada de ficheros de silencio de por medio. Cada
    # escena entra como su propio `-i` y se le añade su pausa exacta con el
    # filtro `apad` (silencio generado dentro del propio grafo de filtros,
    # a nivel de muestra, sin pasar por ningún códec suelto); `concat` las
    # une todas y SOLO ENTONCES se codifica una vez, al final. Verificado con
    # guiones sintéticos de 3, 5 (la estructura real de MDS-015) y 40
    # escenas (la de MDH-006): el desfase queda en 0,05-0,08s en los tres
    # casos, plano, no crece con el número de escenas — y muy por debajo del
    # umbral de 0,5s de `sincronia_voz`.
    entradas_audio, filtro_partes = [], []
    for i, (mp3, cola) in enumerate(partes):
        entradas_audio += ["-i", str(mp3)]
        filtro_partes.append(f"[{i}:a]apad=pad_dur={max(0.0, cola):.3f}[a{i}]")
    etiquetas = "".join(f"[a{i}]" for i in range(len(partes)))
    filtro_partes.append(f"{etiquetas}concat=n={len(partes)}:v=0:a=1[aout]")
    subprocess.run(["ffmpeg", "-y", *entradas_audio,
                    "-filter_complex", ";".join(filtro_partes),
                    "-map", "[aout]",
                    "-c:a", "libmp3lame", "-q:a", "2", "-ar", "24000", "-ac", "1",
                    str(salida / "voz.mp3")], check=True, capture_output=True,
                   stdin=subprocess.DEVNULL)

    escribir_srt(bloques, salida / "subtitulos.srt")
    # Sin marcas de tiempo por palabra no hay subtítulos quemados, y los
    # subtítulos quemados son lo único que se mueve durante el tramo central de
    # cada escena, que es estático por diseño. Un vídeo sin ellos se percibe
    # como un pase de diapositivas. Hasta el 18/08 esto fallaba en silencio.
    if not palabras_todas:
        if usar_gemini:
            print("Sin marcas de palabra: es lo esperado con --motor gemini (la API no "
                  "las da). El .ass sale vacío a propósito —no se quema nada, "
                  "quemar_subs=False— y el .srt no lo necesita: se escribe por bloques "
                  "de escena. qa.py comprueba la sincronía por duración, no por "
                  "«lineas_ass», cuando el motor es Gemini.")
        elif frases_totales:
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
    guion["motor_voz"] = motor_pedido
    (salida / "guion.timed.json").write_text(
        json.dumps(guion, ensure_ascii=False, indent=2), encoding="utf-8")

    m, s = divmod(reloj, 60)
    print(f"\nNarración: {int(m)}m {s:04.1f}s con la voz {voz} (motor: {motor_pedido})")
    print(f"Salida en {salida}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("-o", "--salida", required=True)
    ap.add_argument("--voz", default=None, help=f"por defecto según idioma: {VOCES}")
    # C7 (versión 5.1 y 6 del plan): se escribió con "edge" por defecto la
    # semana del 7, y ha pasado a "gemini" el lunes 14/09 (revisión diaria,
    # con producir.yml ya exponiendo GEMINI_API_KEY al paso de voz.py
    # confirmado antes del cambio). Si algún día ESTADO.md deja de decir OK
    # por causa de la voz de un Short, se vuelve a "edge" cambiando SOLO
    # esta línea.
    ap.add_argument("--motor", choices=["edge", "gemini"], default="gemini",
                     help="gemini por defecto desde el 14/09 (revisión diaria: ESTADO.md "
                          "en OK ese día) -- solo Shorts, con caché y respaldo automático "
                          "a edge ante cualquier fallo")
    a = ap.parse_args()
    asyncio.run(principal(a.guion, a.salida, a.voz, a.motor))
