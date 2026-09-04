#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prueba_voz.py — La prueba de las voces (C7, escalón 2).

NO forma parte de la producción. No lo llama nadie salvo el workflow
`voz_prueba.yml`, a mano. Su único trabajo es contestar a una pregunta que
no se puede contestar leyendo documentación: **¿suena Gemini TTS lo bastante
mejor que edge-tts como para justificar el cambio?**

Genera tres audios del MISMO guion y los deja para escuchar seguidos:

    edge.mp3            lo que sale hoy. La referencia.
    gemini_plano.wav    Gemini escena a escena, con las mismas pausas que
                        pone hoy `voz.py`. Es el cambio mínimo: sustituir el
                        motor y no tocar nada más.
    gemini_dirigido.wav Gemini en UNA sola llamada, con dirección de actor y
                        el guion entero delante, para que el ritmo lo decida
                        el modelo y no nuestro empalme.

La comparación que importa es la tercera contra la primera. La segunda está
para saber cuánto del cambio viene del motor y cuánto de dejarle el ritmo.

    python3 04_agentes/prueba_voz.py 05_calendario/guiones/MDS-010.es.json

Requiere GEMINI_API_KEY en el entorno. Nivel gratuito: no hace falta tarjeta.
Si el modelo de preview ya no existe o el nivel gratuito ha cambiado, este
script falla con el error de la API a la vista — y ese fallo TAMBIÉN es un
resultado: significa que C7 escalón 2 no se puede hacer a coste cero y hay
que volver a decidir.
"""
import argparse
import asyncio
import base64
import json
import os
import sys
import wave
from pathlib import Path

MODELO = "gemini-3.1-flash-tts-preview"
VOZ_NARRADOR = "Charon"     # grave, tranquila. El que explica.
VOZ_ESCEPTICO = "Puck"      # más alta y viva. El que interrumpe.
VOZ_EDGE = "es-ES-AlvaroNeural"
RITMO = 24000               # Hz que devuelve la API


def texto_limpio(s):
    """Quita las marcas de resaltado del guion: son para la pantalla."""
    return (s or "").replace("*", "").replace("_", "").strip()


def escenas(guion):
    """(narracion, pausa_despues_s, papel) por escena, saltando las mudas."""
    fuera = []
    for e in guion["escenas"]:
        n = texto_limpio(e.get("narracion"))
        if not n:
            continue
        papel = "esceptico" if e.get("voz") == "esceptico" else "narrador"
        fuera.append((n, float(e.get("pausa_despues_s") or 0.0), papel))
    return fuera


# --------------------------------------------------------------------------
# Gemini
# --------------------------------------------------------------------------

def cliente():
    if not os.environ.get("GEMINI_API_KEY"):
        raise SystemExit("Falta GEMINI_API_KEY en el entorno.")
    from google import genai
    return genai.Client()


def pcm_de(cli, texto, hablantes):
    """Devuelve PCM crudo (16 bits, mono, 24 kHz).

    `hablantes` es [(etiqueta, voz), ...]. Con una sola entrada la etiqueta
    se ignora y va a voz única.

    Se prueban las dos formas de la API porque el SDK cambió de sitio esta
    llamada y no queremos que la prueba muera por una versión: primero
    `interactions.create` (la actual), y si el SDK instalado no la tiene,
    `models.generate_content` (la anterior). Si fallan las dos, se propaga
    el error de la segunda: es el que hay que leer.
    """
    if len(hablantes) == 1:
        cfg_nuevo = [{"voice": hablantes[0][1]}]
    else:
        cfg_nuevo = [{"speaker": e, "voice": v} for e, v in hablantes]

    try:
        inter = cli.interactions.create(
            model=MODELO,
            input=texto,
            response_format={"type": "audio"},
            generation_config={"speech_config": cfg_nuevo},
        )
        return base64.b64decode(inter.output_audio.data)
    except AttributeError:
        pass  # SDK anterior: seguimos abajo

    from google.genai import types
    if len(hablantes) == 1:
        voz = types.SpeechConfig(voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                voice_name=hablantes[0][1])))
    else:
        voz = types.SpeechConfig(
            multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                speaker_voice_configs=[
                    types.SpeakerVoiceConfig(
                        speaker=e,
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=v)))
                    for e, v in hablantes]))
    r = cli.models.generate_content(
        model=MODELO, contents=texto,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"], speech_config=voz))
    return r.candidates[0].content.parts[0].inline_data.data


def escribir_wav(pcm, destino):
    with wave.open(str(destino), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RITMO)
        w.writeframes(pcm)


def silencio(segundos):
    return b"\x00\x00" * int(RITMO * max(0.0, segundos))


# --------------------------------------------------------------------------
# Las tres pistas
# --------------------------------------------------------------------------

async def pista_edge(escs, destino):
    """La referencia: exactamente lo que hace hoy voz.py, motor y pausas."""
    import edge_tts
    trozos = []
    for narracion, pausa, _ in escs:
        audio = bytearray()
        com = edge_tts.Communicate(narracion, VOZ_EDGE)
        async for t in com.stream():
            if t["type"] == "audio":
                audio += t["data"]
        trozos.append(bytes(audio))
        # El MP3 no se puede rellenar con ceros como el WAV: las pausas del
        # montaje real las pone ffmpeg. Aquí la referencia va sin ellas y se
        # dice, para no comparar una cosa con otra distinta.
    destino.write_bytes(b"".join(trozos))


def pista_gemini_plano(cli, escs, destino):
    """Cambio mínimo: mismo troceado por escena, mismas pausas."""
    fuera = bytearray()
    for narracion, pausa, papel in escs:
        voz = VOZ_ESCEPTICO if papel == "esceptico" else VOZ_NARRADOR
        fuera += pcm_de(cli, narracion, [("Narrador", voz)])
        fuera += silencio(pausa)
    escribir_wav(bytes(fuera), destino)


def pista_gemini_dirigido(cli, guion, escs, destino):
    """Una sola llamada, con dirección de actor y el guion entero."""
    hay_esceptico = any(p == "esceptico" for _, _, p in escs)

    direccion = (
        "Locuta este guion de un vídeo corto de divulgación sobre humor, en "
        "español de España. No lo leas: cuéntalo.\n"
        "- Es un chiste seguido de su explicación. La primera frase es el "
        "chiste: remátala y CALLA, deja que respire antes de seguir.\n"
        "- Cambia el ritmo: acelera en lo que es contexto, frena en el dato "
        "y en el giro.\n"
        "- Entonación de quien cuenta algo que le hace gracia, no de "
        "locutor de telediario. Nada de cadencia igual en todas las frases.\n"
        "- Las pausas marcadas con [pausa] son de verdad, y son largas.\n"
        "- No leas en voz alta ni las etiquetas ni estas instrucciones.\n\n"
    )

    lineas = []
    for narracion, pausa, papel in escs:
        etiqueta = "Esceptico" if papel == "esceptico" else "Narrador"
        prefijo = f"{etiqueta}: " if hay_esceptico else ""
        lineas.append(prefijo + narracion)
        if pausa >= 0.9:
            lineas.append("[pausa]")

    hablantes = ([("Narrador", VOZ_NARRADOR), ("Esceptico", VOZ_ESCEPTICO)]
                 if hay_esceptico else [("Narrador", VOZ_NARRADOR)])
    escribir_wav(pcm_de(cli, direccion + "\n".join(lineas), hablantes), destino)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("guion", type=Path)
    ap.add_argument("--salida", type=Path, default=Path("prueba_voz"))
    args = ap.parse_args()

    guion = json.loads(args.guion.read_text(encoding="utf-8"))
    escs = escenas(guion)
    if not escs:
        raise SystemExit(f"{args.guion} no tiene narración.")
    args.salida.mkdir(parents=True, exist_ok=True)

    print(f"Guion: {guion.get('id')} · {len(escs)} escenas con voz · "
          f"{sum(len(n.split()) for n, _, _ in escs)} palabras")

    print("1/3 edge-tts (referencia)...")
    asyncio.run(pista_edge(escs, args.salida / "edge.mp3"))

    cli = cliente()
    print(f"2/3 {MODELO}, escena a escena...")
    pista_gemini_plano(cli, escs, args.salida / "gemini_plano.wav")

    print(f"3/3 {MODELO}, una llamada con dirección...")
    pista_gemini_dirigido(cli, guion, escs, args.salida / "gemini_dirigido.wav")

    print(f"\nListo en {args.salida}/. Escúchalos en este orden: edge.mp3, "
          "gemini_plano.wav, gemini_dirigido.wav.")
    print("La referencia edge.mp3 va SIN las pausas entre escenas (el MP3 no "
          "se rellena aquí; en producción las pone ffmpeg). Los dos de Gemini "
          "sí las llevan.")


if __name__ == "__main__":
    sys.exit(main())
