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
from datetime import datetime, timezone
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
#   1. --motor {edge,gemini}. [SUSTITUIDO el 15/09 por C33.1] Aquí decía
#      «respaldo automático e inmediato a edge-tts ante CUALQUIER fallo de
#      Gemini en una escena». Eso es lo que publicó MDS-017 con dos voces
#      alternándose. Ahora el respaldo es por vídeo entero y en escalera:
#      ver la cabecera de C33.1, más abajo.
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
    "seccion":
        "Aquí empieza una parte nueva del vídeo, pero el vídeo ya estaba en marcha. "
        "Dilo como quien pasa página en una conversación: con algo más de energía "
        "que la frase anterior y sin anunciarlo como un locutor.",
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
    # C33.1: un «titulo» que no es la escena 1 abre una parte nueva de un
    # episodio largo. Con «apertura» se le decía que era la primera frase del
    # vídeo, y MDH-007 tiene seis escenas así.
    if papel == "apertura":
        papel = "seccion"
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

    Sin reintentos aquí: los reintentos y la escalera de modelos viven en
    `_gemini_escena` y `_voz_gemini_completa` (C33.1). Hasta el 15/09 no había
    reintentos en ningún sitio y cualquier fallo mandaba la escena sola a
    edge-tts: así salió MDS-017 con dos voces.
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


# ----------------------------------------------------------------------------
# C33.1 (15/09/2026) · Un vídeo, una voz. Nunca mezclada.
#
# MDS-017 se publicó el martes 15 con tres escenas en Gemini y tres en
# edge-tts (`ficha.json`: «gemini: 3, edge (respaldo): 3»). Nadie lo decidió:
# el respaldo era POR ESCENA. Cualquier fallo de una llamada, del tipo que
# fuera, mandaba esa escena sola a edge-tts y la producción seguía con la
# siguiente. El codirector ya lo había dicho del episodio largo el 7/09 —dos
# voces en un mismo vídeo es una chapuza— y el criterio vale igual para un
# Short: una voz que cambia cada diez segundos no se puede seguir.
#
# Había tres defectos, y cada uno tiene su arreglo:
#
#   1. **No había reintentos.** La documentación de Google lo dice con estas
#      palabras: los modelos TTS devuelven a veces tokens de texto en vez de
#      audio, el servidor responde con un 500 «de forma aleatoria» y hay que
#      reintentar. Aquí un 500 mandaba la escena a edge-tts al instante. Ahora
#      cada escena tiene INTENTOS_POR_ESCENA intentos, y el último va con una
#      dirección mínima. Eso cubre la otra limitación documentada: un prompt
#      ambiguo puede ser rechazado o, peor, el modelo puede leer en voz alta
#      las instrucciones. Ese segundo caso lo caza `_audio_plausible`, que mira
#      si lo que ha vuelto dura lo que tiene que durar.
#   2. **La cuota diaria no se reconocía.** Google la nombra
#      «..._per_model_per_day» / «PerDay», y aquí se buscaba «per day» o
#      «perday» sin quitar los guiones bajos. Nunca coincidía, así que con la
#      cuota ya agotada se seguía llamando escena tras escena, con 25 s de
#      espera entre una y otra, para nada.
#   3. **El respaldo era por escena.** Ahora es por vídeo, en escalera:
#        a) todas las escenas con MODELO_GEMINI (3.1), mirando antes la caché;
#        b) si no se completan, TODAS otra vez con MODELO_GEMINI_LARGO (2.5),
#           que tiene su propia cuota de 10 al día (lo muestra el panel del
#           codirector, 14/09);
#        c) si tampoco sale y es un cron de antes de las 08:00 UTC, el paso
#           FALLA SIN SUBIR NADA. La cuota de Google se reinicia a medianoche
#           de California (07:00 UTC en verano y 08:00 en invierno), así que el
#           cron de las 08:23 lo vuelve a intentar con la cuota llena. Lo que
#           ya se sintetizó queda en la caché;
#        d) solo en ese último intento, el vídeo ENTERO con edge-tts. Entero,
#           nunca mezclado. En una ejecución manual no se llega a este paso:
#           el paso falla y decide el codirector.
#   El largo sigue la misma escalera, pero con un solo modelo: el de su caché.
# ----------------------------------------------------------------------------

MODELOS_CORTO = (MODELO_GEMINI, MODELO_GEMINI_LARGO)
MODELOS_LARGO = (MODELO_GEMINI_LARGO,)
INTENTOS_POR_ESCENA = 3
ESPERA_LIMITE_MINUTO_S = 65.0      # un 429 por minuto: se deja pasar el minuto entero
HORA_UTC_ULTIMO_INTENTO = 8        # producir.yml: crons a las 01:13, 04:47 y 08:23 UTC
SALIDA_SIN_VOZ_COMPLETA = 3        # código de salida: «no hay voz entera, no subas nada»

# Para el último intento de una escena. Sigue la recomendación de Google:
# un preámbulo que diga claramente que es una petición de voz y una etiqueta
# que marque dónde empieza el texto que hay que decir.
DIRECCION_MINIMA = (
    "Lee en voz alta, en español de España y con voz natural de persona que "
    "cuenta algo, el texto que va después de la palabra TEXTO. No te rías, no "
    "añadas nada y no leas esta instrucción.\n\nTEXTO:\n")


class CuotaDiariaAgotada(Exception):
    """El modelo no da más peticiones hoy. No tiene sentido reintentar."""


def _normalizado(msg):
    return re.sub(r"[\s_\-]", "", str(msg).lower())


def clase_de_error(exc):
    """Clasifica un fallo de Gemini: 'dia', 'minuto', 'rechazo' o 'transitorio'.

    Se compara sin espacios ni guiones bajos porque Google escribe lo mismo
    de tres maneras («per day», «per_day», «PerDay»), y durante una semana
    aquí solo se reconocía la primera (ver C33.1, punto 2).
    """
    msg = str(exc)
    n = _normalizado(msg)
    if "resourceexhausted" in n or re.search(r"\b429\b", msg):
        return "dia" if "perday" in n else "minuto"
    if ("prohibitedcontent" in n or "invalidargument" in n
            or re.search(r"\b400\b", msg)):
        return "rechazo"
    return "transitorio"


def _audio_plausible(texto, dur):
    """¿Puede esta toma ser ESTE texto leído en voz alta?

    No mira el contenido; mira solo la duración. El fallo que tiene que cazar
    es el que describe Google: que el modelo lea en voz alta las instrucciones
    de dirección, que son diez veces más largas que la narración. Los límites
    van de 5 palabras/s (nadie habla más rápido) a 1,1 palabras/s más 1,5 s de
    margen (nadie habla más lento). Una toma buena cae siempre dentro: el
    control de ritmo de verdad (1,6-3,2) sigue siendo solo un aviso.
    """
    n = max(1, len((texto or "").split()))
    if dur <= 0.3:
        return False
    return n / 5.0 <= dur <= max(4.0, n / 1.1 + 1.5)


def _edge_permitido(ahora=None):
    """(permitido, motivo). ¿Puede este vídeo salir entero con edge-tts?

    Solo en un cron que ya corre con la cuota de Google reiniciada. Con
    VOZ_ULTIMO_INTENTO=1 o =0 se fuerza la respuesta; sirve para las pruebas.
    """
    forzado = os.environ.get("VOZ_ULTIMO_INTENTO")
    if forzado in ("0", "1"):
        return forzado == "1", f"VOZ_ULTIMO_INTENTO={forzado}"
    evento = os.environ.get("GITHUB_EVENT_NAME", "")
    if evento != "schedule":
        return False, (f"ejecución «{evento or 'local'}»: en una ejecución manual edge-tts "
                       "nunca entra solo; decide el codirector")
    ahora = ahora or datetime.now(timezone.utc)
    if ahora.hour < HORA_UTC_ULTIMO_INTENTO:
        return False, (f"son las {ahora:%H:%M} UTC y la cuota de Gemini aún no se ha "
                       f"reiniciado: el cron de las 08:23 UTC lo vuelve a intentar")
    return True, f"último intento del día ({ahora:%H:%M} UTC)"


async def _gemini_escena(it, modelo, estado):
    """Sintetiza una escena con `modelo`. Devuelve el origen de la toma o None.

    El origen es 'caché', 'llamada' o 'llamada (dirección mínima)'. Devuelve
    None si la escena no ha salido tras INTENTOS_POR_ESCENA intentos, y lanza
    CuotaDiariaAgotada si el modelo ya no da más hoy.
    """
    cache = _cache_voz_ruta(it["texto"], modelo, it["voz_gemini"], it["dirigido"])
    if cache.exists():
        it["mp3"].write_bytes(cache.read_bytes())
        return "caché"
    if estado["agotados"].get(modelo):
        raise CuotaDiariaAgotada(modelo)

    for intento in range(1, INTENTOS_POR_ESCENA + 1):
        ultimo = intento == INTENTOS_POR_ESCENA
        prompt = (DIRECCION_MINIMA + it["texto"]) if ultimo else it["dirigido"]
        espera = ESPERA_ENTRE_LLAMADAS_GEMINI - (time.monotonic() - estado["ultima"])
        if estado["ultima"] and espera > 0:
            await asyncio.sleep(espera)
        estado["llamadas"][modelo] = estado["llamadas"].get(modelo, 0) + 1
        tmp = it["mp3"].with_suffix(".tmp.mp3")
        try:
            cli = estado["cliente"] or _gemini_cliente()
            estado["cliente"] = cli
            pcm = _gemini_pcm(cli, modelo, prompt, it["voz_gemini"])
            estado["ultima"] = time.monotonic()
            if not pcm:
                raise RuntimeError("la respuesta no trae audio")
            _pcm_a_mp3(pcm, RITMO_GEMINI_HZ, tmp)
            dur = duracion_real(tmp)
            if not _audio_plausible(it["texto"], dur):
                raise RuntimeError(
                    f"toma descartada: {dur:.1f} s para {len(it['texto'].split())} palabras "
                    "(¿ha leído las instrucciones en voz alta?)")
            tmp.replace(it["mp3"])
            CACHE_VOZ_DIR.mkdir(parents=True, exist_ok=True)
            tmp_cache = cache.with_suffix(".tmp.mp3")
            tmp_cache.write_bytes(it["mp3"].read_bytes())
            tmp_cache.replace(cache)
            return "llamada (dirección mínima)" if ultimo else "llamada"
        except Exception as exc:
            tmp.unlink(missing_ok=True)
            estado["ultima"] = time.monotonic()
            clase = clase_de_error(exc)
            print(f"::warning::escena {it['i']} · {modelo} · intento {intento}/"
                  f"{INTENTOS_POR_ESCENA} · fallo «{clase}»: {str(exc)[:220]!r}")
            if clase == "dia":
                estado["agotados"][modelo] = True
                raise CuotaDiariaAgotada(modelo) from exc
            if not ultimo and clase == "minuto":
                await asyncio.sleep(ESPERA_LIMITE_MINUTO_S)
    return None


async def _voz_gemini_completa(items, modelo, estado):
    """{indice: origen} si TODAS las escenas han salido con `modelo`; si no, None.

    Se para en la primera escena que no sale: seguir gastaría cuota en escenas
    que este vídeo ya no va a usar con este modelo. Lo que sí ha salido queda
    en la caché para el próximo intento.
    """
    origenes = {}
    for it in items:
        try:
            origen = await _gemini_escena(it, modelo, estado)
        except CuotaDiariaAgotada:
            print(f"::warning::cuota DIARIA de {modelo} agotada (escena {it['i']}). "
                  f"Hechas con este modelo: {len(origenes)} de {len(items)}.")
            return None
        if origen is None:
            print(f"::warning::la escena {it['i']} no sale con {modelo} tras "
                  f"{INTENTOS_POR_ESCENA} intentos. Hechas: {len(origenes)} de {len(items)}.")
            return None
        origenes[it["i"]] = origen
        print(f"  escena {it['i']:>2}  {modelo}  [{origen}]")
    return origenes


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

    # C7 + C27 + C33.1: Gemini en los dos formatos, y siempre UNA sola voz por
    # vídeo. La escalera está explicada en la cabecera de C33.1, más arriba.
    #
    #   · Short  → 3.1, y si no se completa, 2.5 entero. Llamadas en vivo con
    #              caché: seis escenas caben en las diez peticiones diarias.
    #   · Largo  → solo 2.5, que es el modelo de su caché. Casi todo llega
    #              precacheado de martes a viernes (`voz_precache.py`), y lo que
    #              falte se pide en vivo. Si no cabe en la cuota del día, el
    #              episodio no se mezcla: espera al cron siguiente.
    formato = guion.get("formato")
    es_corto = formato == "corto"
    motor_pedido = "gemini" if (motor == "gemini" and formato in ("corto", "largo")) else "edge"
    if motor == "gemini" and motor_pedido == "edge":
        print(f"::notice::--motor gemini pedido pero formato=«{formato}», que no es ni "
              f"«corto» ni «largo». Esta producción va con edge-tts.")

    escenas = guion["escenas"]

    # 1. Qué hay que decir en cada escena, y cómo.
    items = []
    for i, e in enumerate(escenas, 1):
        crudo = (e.get("narracion") or "").strip()
        texto = hablable(crudo)
        if texto != crudo:
            print(f"::warning::escena {i}: la narración traía marcado de resaltado "
                  f"(* o _) y se ha quitado antes de sintetizar. El resaltado es de "
                  f"pantalla; en «narracion» el sintetizador lo lee en voz alta.")
        if not texto:
            continue
        papel = "esceptico" if e.get("voz") == "esceptico" else "narrador"
        # C33: la dirección de actor se construye por escena a partir del
        # propio guion (tipo, posición, pausa de la escena anterior).
        dirigido, papel_escena = direccion_escena(escenas, i, texto)
        e["direccion_voz"] = papel_escena
        items.append({
            "i": i, "e": e, "texto": texto, "dirigido": dirigido,
            "voz_gemini": VOZ_GEMINI_ESCEPTICO if papel == "esceptico" else VOZ_GEMINI_NARRADOR,
            "mp3": salida / "voz" / f"escena_{i:03d}.mp3",
        })

    # 2. Qué motor pone la voz. Uno solo para todo el vídeo.
    resultado = {}          # indice -> (palabras, n_frases, motor, origen)
    modelo_final = "edge-tts"
    if motor_pedido == "gemini":
        estado = {"agotados": {}, "llamadas": {}, "ultima": 0.0, "cliente": None}
        for modelo in (MODELOS_CORTO if es_corto else MODELOS_LARGO):
            print(f"Voz: intentando el vídeo entero con {modelo}…")
            origenes = await _voz_gemini_completa(items, modelo, estado)
            if origenes is not None:
                modelo_final = modelo
                for it in items:
                    resultado[it["i"]] = ([], 0, modelo, origenes[it["i"]])
                break
        print(f"Llamadas reales a Gemini en esta producción: {estado['llamadas'] or 0}")
        if not resultado:
            permitido, motivo = _edge_permitido()
            if not permitido:
                print(f"::error::No hay voz de Gemini para el vídeo entero y no se sube nada "
                      f"({motivo}). Nunca se mezclan dos voces en un vídeo (C33.1). Lo ya "
                      f"sintetizado queda en 03_produccion/cache_voz/.")
                raise SystemExit(SALIDA_SIN_VOZ_COMPLETA)
            print(f"::warning::Ningún modelo de Gemini ha dado voz a todas las escenas y es "
                  f"el {motivo}: el vídeo ENTERO sale con edge-tts, nunca mezclado.")
    if not resultado:
        origen = "respaldo, vídeo entero" if motor_pedido == "gemini" else "pedido"
        for it in items:
            _, pal, n_fr = await sintetizar(it["texto"], voz, it["mp3"])
            resultado[it["i"]] = (pal, n_fr, "edge-tts", origen)

    motores = {r[2] for r in resultado.values()}
    if len(motores) > 1:     # no puede pasar; si pasa, que no llegue al público
        raise SystemExit(f"Voz mezclada ({sorted(motores)}): esto no debería ocurrir nunca.")

    # 3. Duraciones reales, recortes y subtítulos, escena a escena.
    reloj, bloques, palabras_todas, partes = 0.0, [], [], []
    frases_totales, recortadas = 0, []
    for i, e in enumerate(escenas, 1):
        if i not in resultado:
            e["duracion_s"] = e.get("duracion_s", 3.0)
            reloj += e["duracion_s"]
            continue
        texto = hablable((e.get("narracion") or "").strip())
        mp3 = salida / "voz" / f"escena_{i:03d}.mp3"
        pal, n_fr, motor_usado, origen = resultado[i]
        papel_escena = e.get("direccion_voz", "")
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
        e["origen_voz"] = origen
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
        if modelo_final != "edge-tts":
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
    # Hasta el 15/09 aquí iba siempre la voz de edge-tts, también cuando hablaba
    # Gemini, y `ficha.json` decía «es-ES-AlvaroNeural» en vídeos sin una sola
    # palabra de Alvaro.
    guion["voz_usada"] = voz if modelo_final == "edge-tts" else VOZ_GEMINI_NARRADOR
    guion["motor_voz"] = motor_pedido
    guion["modelo_voz"] = modelo_final
    (salida / "guion.timed.json").write_text(
        json.dumps(guion, ensure_ascii=False, indent=2), encoding="utf-8")

    m, s = divmod(reloj, 60)
    print(f"\nNarración: {int(m)}m {s:04.1f}s · motor: {modelo_final}"
          f"{'' if modelo_final != 'edge-tts' else f' (voz {voz})'}")
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
                     help="gemini por defecto desde el 14/09. Desde el 15/09 (C33.1), una "
                          "sola voz por vídeo: 3.1 → 2.5 → esperar al cron siguiente → "
                          "edge-tts entero solo en el último intento del día")
    a = ap.parse_args()
    asyncio.run(principal(a.guion, a.salida, a.voz, a.motor))
