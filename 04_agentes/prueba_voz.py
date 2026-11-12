#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prueba_voz.py — La prueba de las voces (C7, escalón 2).

NO forma parte de la producción. Lo llama a mano el workflow `voz_prueba.yml`.

# LA CUOTA MANDA SOBRE EL DISEÑO, Y ESO YA ESTÁ DECIDIDO

La primera versión de este script (04/09, mañana) pedía **una llamada por
escena** y murió con `RESOURCE_EXHAUSTED`. El nivel gratuito de los modelos TTS
de Gemini da, por modelo:

    3 peticiones por minuto (RPM)   ·   10 peticiones por día (RPD)
    10.000 tokens de entrada por minuto (TPM)

El TPM sobra —un Short entero son ~400 tokens de entrada, y el propio panel
marcaba 62 de 10.000— y el RPD también, si se pide poco. **Lo que no cabe es
pedir mucho.** Seis escenas eran seis peticiones seguidas: el RPM de 3 salta a
la cuarta, y dos intentos fallidos se comieron 4 de las 10 del día.

Y esto no es un problema de la prueba: **es el que decide la arquitectura de
C7.** Con 10 peticiones al día, un episodio largo de 40 escenas troceado por
escena es imposible. Una llamada por vídeo son 6 peticiones a la semana. Así
que, si Gemini entra, entra **con el guion entero en una sola llamada** — que
además es la forma en la que el modelo puede decidir el ritmo, que es justo lo
que le falta a la voz de hoy.

Eso abre la pregunta técnica que esta prueba también contesta, sin gastar ni
una petición más: si el audio viene de una sola pieza, **¿cómo sabe `render.py`
cuánto dura cada escena?** Midiendo los silencios. El script analiza la onda
que devuelve el modelo, cuenta los tramos de voz separados por pausas y los
compara con el número de escenas del guion. Si cuadran, C7 escalón 2 es viable
tal cual. Si no cuadran, el plan B es partir el guion en dos o tres llamadas
(sigue cabiendo de sobra en 10 al día) y cerrar el corte donde nos convenga.

# QUÉ GENERA (dos peticiones en total)

    edge.mp3            lo que sale hoy. La referencia.
    gemini_plano.wav    el guion entero, sin dirección. El modelo por defecto.
    gemini_dirigido.wav el guion entero, con dirección de actor y pausas marcadas.
    informe.txt         el análisis de silencios de los dos anteriores.

    python3 04_agentes/prueba_voz.py 05_calendario/guiones/MDS-010.es.json

Requiere GEMINI_API_KEY. Con `--modelo gemini-2.5-flash-preview-tts` se usa el
otro modelo TTS, que tiene **su propia cuota**: si el de 3.1 se ha agotado hoy,
esa es la salida para no esperar a mañana.
"""
import argparse
import asyncio
import base64
import json
import os
import sys
import time
import wave
from pathlib import Path

MODELO = "gemini-3.1-flash-tts-preview"
VOZ_NARRADOR = "Charon"     # grave, tranquila. El que explica.
VOZ_ESCEPTICO = "Puck"      # más alta y viva. El que interrumpe.
VOZ_EDGE = "es-ES-AlvaroNeural"
RITMO = 24000               # Hz que devuelve la API
ESPERA_ENTRE_PETICIONES = 25.0   # RPM = 3, o sea una cada 20 s. 25 con margen.


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
    from google.genai import types
    # 15/10/2026: con gemini-2.5-pro-preview-tts la primera llamada se quedó 20 min
    # sin respuesta y el workflow la canceló sin dejar nada. Cuatro minutos por
    # llamada sobran (una toma de un Short tarda menos de uno) y, si se pasa, el
    # error dice qué modelo no contestó en vez de perder la ejecución entera.
    # 09/11/2026: la versión de la API, fija. google-genai 3.0.0 (06/11) cambió el valor por defecto a
    # «v1», donde los modelos TTS (preview) no existen: 404 «model not found» con todos.
    return genai.Client(http_options=types.HttpOptions(api_version="v1beta", timeout=240_000))


def _solo_pcm(datos):
    """02/11/2026 · los modelos TTS de Gemini 3.8 (los que sustituyen a los de hoy, que Google
    apaga el 17/11/2026) pueden devolver WAV con cabecera en vez de PCM crudo. Si llega un WAV,
    se le quita la cabecera; si no es mono, 16 bits y 24 kHz, se para (mejor un error que una
    voz a otra velocidad). Si llega PCM, sale tal cual: con los modelos de hoy no cambia nada."""
    if isinstance(datos, str):
        datos = base64.b64decode(datos)
    if not (len(datos) > 12 and datos[:4] == b"RIFF" and datos[8:12] == b"WAVE"):
        return datos
    import io
    with wave.open(io.BytesIO(datos), "rb") as w:
        forma = (w.getnchannels(), w.getsampwidth(), w.getframerate())
        if forma != (1, 2, 24000):
            raise RuntimeError(f"Gemini devolvió un WAV {forma} (canales, bytes, Hz); se esperaba (1, 2, 24000).")
        return w.readframes(w.getnframes())


def _una_peticion(cli, modelo, texto, hablantes):
    """Una llamada, probando las dos formas de la API.

    El SDK cambió de sitio esta llamada: primero `interactions.create` (la
    actual) y, si el SDK instalado no la tiene, `models.generate_content`.
    """
    if len(hablantes) == 1:
        cfg = [{"voice": hablantes[0][1]}]
    else:
        cfg = [{"speaker": e, "voice": v} for e, v in hablantes]

    if hasattr(cli, "interactions"):
        inter = cli.interactions.create(
            model=modelo, input=texto,
            response_format={"type": "audio"},
            generation_config={"speech_config": cfg})
        return _solo_pcm(base64.b64decode(inter.output_audio.data))

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
        model=modelo, contents=texto,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"], speech_config=voz))
    return _solo_pcm(r.candidates[0].content.parts[0].inline_data.data)


def pcm_de(cli, modelo, texto, hablantes, intentos=3):
    """Como `_una_peticion`, reintentando si salta el límite por minuto.

    El RPM se recupera solo en menos de un minuto; el RPD no se recupera hasta
    mañana. Se distinguen por el texto del error para no gastar tres intentos
    en algo que no va a mejorar.
    """
    for n in range(1, intentos + 1):
        try:
            return _una_peticion(cli, modelo, texto, hablantes)
        except Exception as e:
            msg = str(e)
            agotado = "RESOURCE_EXHAUSTED" in msg or "429" in msg
            por_dia = "per day" in msg or "PerDay" in msg
            if not agotado or n == intentos:
                raise
            if por_dia:
                raise SystemExit(
                    "Se ha agotado la cuota DIARIA de este modelo (10 peticiones "
                    "en el nivel gratuito). No se arregla esperando: o se prueba "
                    "mañana, o se relanza con "
                    "--modelo gemini-2.5-flash-preview-tts, que tiene su propia "
                    f"cuota.\n\nError original:\n{msg}")
            espera = 65 * n
            print(f"   límite por minuto alcanzado; espero {espera} s "
                  f"(intento {n} de {intentos - 1})...", flush=True)
            time.sleep(espera)


def escribir_wav(pcm, destino):
    with wave.open(str(destino), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RITMO)
        w.writeframes(pcm)


# --------------------------------------------------------------------------
# El análisis que decide si esto se puede sincronizar con el vídeo
# --------------------------------------------------------------------------

def tramos_de_voz(pcm, pausa_min_s=0.30, ventana_s=0.02):
    """Trocea la onda en tramos de voz separados por silencios.

    Sin dependencias: RMS por ventana de 20 ms sobre el PCM de 16 bits, umbral
    relativo al pico. Devuelve [(inicio_s, fin_s), ...].
    """
    import array
    m = array.array("h")
    m.frombytes(pcm[:len(pcm) - (len(pcm) % 2)])
    n = max(1, int(RITMO * ventana_s))
    niveles = []
    for i in range(0, len(m) - n, n):
        t = m[i:i + n]
        niveles.append((sum(x * x for x in t) / n) ** 0.5)
    if not niveles:
        return []
    umbral = max(180.0, 0.035 * max(niveles))
    minv = max(1, int(pausa_min_s / ventana_s))

    tramos, ini, callado = [], None, 0
    for i, v in enumerate(niveles):
        if v >= umbral:
            if ini is None:
                ini = i
            callado = 0
        elif ini is not None:
            callado += 1
            if callado >= minv:
                tramos.append((ini * ventana_s, (i - callado) * ventana_s))
                ini, callado = None, 0
    if ini is not None:
        tramos.append((ini * ventana_s, len(niveles) * ventana_s))
    return tramos


def informe(pcm, escs, etiqueta, salida):
    tramos = tramos_de_voz(pcm)
    dur = len(pcm) / 2 / RITMO
    lin = [f"--- {etiqueta} ---",
           f"duración total: {dur:.1f} s",
           f"escenas con voz en el guion: {len(escs)}",
           f"tramos de voz detectados:    {len(tramos)}",
           ""]
    if len(tramos) == len(escs):
        lin.append("✅ CUADRAN. Se puede repartir el audio por escena cortando "
                   "por los silencios, así que render.py puede sincronizar el "
                   "vídeo sin pedir una llamada por escena.")
    else:
        lin.append("⚠️ NO CUADRAN. Cortar por silencios no basta tal cual: hay "
                   "que forzar pausas más largas entre escenas, o partir el "
                   "guion en dos o tres llamadas (sigue cabiendo en 10 al día).")
    lin.append("")
    for i, (a, b) in enumerate(tramos, 1):
        texto = escs[i - 1][0][:48] + "…" if i <= len(escs) else "(sobra)"
        lin.append(f"  {i:2d}. {a:6.2f}–{b:6.2f} s  ({b - a:5.2f} s)  {texto}")
    lin.append("")
    salida.write_text("\n".join(lin) + "\n", encoding="utf-8")
    print("\n".join(lin))
    return "\n".join(lin)


# --------------------------------------------------------------------------
# Los textos
# --------------------------------------------------------------------------

def guion_plano(escs, hay_esceptico):
    return "\n".join(
        (("Esceptico: " if p == "esceptico" else "Narrador: ") if hay_esceptico
         else "") + n
        for n, _, p in escs)


def guion_dirigido(escs, hay_esceptico):
    direccion = (
        "Locuta este guion de un vídeo corto de divulgación sobre humor, en "
        "español de España. No lo leas: cuéntalo.\n"
        "- Es un chiste seguido de su explicación. La primera frase es el "
        "chiste: remátala y CALLA, deja que respire antes de seguir.\n"
        "- Cambia el ritmo: acelera en lo que es contexto, frena en el dato y "
        "en el giro.\n"
        "- Entonación de quien cuenta algo que le hace gracia, no de locutor "
        "de telediario. Nada de cadencia igual en todas las frases.\n"
        "- Deja una pausa clara y silenciosa entre una línea y la siguiente. "
        "Donde ponga [pausa], la pausa es larga.\n"
        "- No leas en voz alta ni las etiquetas ni estas instrucciones.\n\n")
    lineas = []
    for n, pausa, p in escs:
        lineas.append((("Esceptico: " if p == "esceptico" else "Narrador: ")
                       if hay_esceptico else "") + n)
        if pausa >= 0.9:
            lineas.append("[pausa]")
    return direccion + "\n".join(lineas)


async def pista_edge(escs, destino):
    """La referencia: el mismo motor y la misma voz que la producción de hoy."""
    import edge_tts
    trozos = []
    for narracion, _, _ in escs:
        audio = bytearray()
        async for t in edge_tts.Communicate(narracion, VOZ_EDGE).stream():
            if t["type"] == "audio":
                audio += t["data"]
        trozos.append(bytes(audio))
    destino.write_bytes(b"".join(trozos))


def prueba_c36(guion, salida):
    """22/10/2026 · C36 con el código de producción: `voz.py` pide el Short entero
    en UNA llamada, lo parte por palabras y le pone las pausas del guion. Gasta
    una petición. Sin vuelta a la voz escena a escena: si la toma no vale, falla.
    Deja `c36/voz.mp3` (lo que sonaría en el vídeo) y `c36/voz/toma_entera.mp3`."""
    import subprocess
    # voz_prueba.yml solo instala edge-tts y google-genai; Whisper hace falta aquí.
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "faster-whisper",
                    "numpy", "av<19"], check=True)
    # Ni ffmpeg: el runner de este workflow no lo trae (producir.yml lo instala).
    import shutil
    if shutil.which("ffmpeg") is None:
        subprocess.run("sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg",
                       shell=True, check=True)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "03_produccion" / "pipeline"))
    import voz
    voz.C36_SOLO = True
    asyncio.run(voz.principal(str(guion), salida / "c36", motor="gemini"))
    print(f"\nListo: {salida}/c36/voz.mp3 es lo que sonaría en el vídeo.")


# 12/11/2026 · voz-3.8-acento. La muestra 3.8 del 05/11 se hizo con las dos
# variantes de esta prueba (plano: el guion sin nada; dirigido: la dirección
# larga de arriba). El codirector oyó que la dirigida leía las instrucciones y
# que el acento era latino. Ninguna de las dos es lo que haría la producción:
# voz.py (C36) pide el Short entero con un preámbulo corto que dice «en español
# de España» y marca el texto con «TEXTO:» (la receta de Google). Esta prueba es
# eso, con el modelo nuevo, y con dos voces: Charon (la de siempre) y otra
# grave. Se lanza escribiendo «acento:» delante del guion en «Prueba de voces».
VOCES_ACENTO = ("Charon", "Orus")
PALABRAS_DE_INSTRUCCION = {"lee", "voz", "alta", "texto", "notas", "dirección",
                           "direccion", "españa", "acento", "narrador", "pausa",
                           "instrucciones", "línea", "linea"}


def _palabras(s):
    import re
    return re.findall(r"[a-záéíóúüñ]+", (s or "").lower())


def prueba_acento(guion_ruta, salida, modelo):
    import shutil
    import subprocess
    guion = json.loads(guion_ruta.read_text(encoding="utf-8"))
    del_guion = set(_palabras(" ".join(n for n, _, _ in escenas(guion))))
    lineas = [f"Muestra voz-3.8-acento · {guion.get('id')} · modelo {modelo}",
              "Código de producción (voz.py, C36: una toma con el preámbulo «Lee en voz alta, "
              "en español de España…»).", ""]
    for i, voz_nombre in enumerate(VOCES_ACENTO):
        if i:
            print(f"\n   esperando {ESPERA_ENTRE_PETICIONES:.0f} s (3 peticiones por minuto)...",
                  flush=True)
            time.sleep(ESPERA_ENTRE_PETICIONES)
        destino = salida / f"c36_{voz_nombre.lower()}"
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "03_produccion" / "pipeline"))
        if i == 0:
            subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "faster-whisper",
                            "numpy", "av<19"], check=True)
            if shutil.which("ffmpeg") is None:
                subprocess.run("sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg",
                               shell=True, check=True)
        import voz
        voz.C36_SOLO = True
        voz.MODELO_GEMINI = modelo
        voz.VOZ_GEMINI_NARRADOR = voz_nombre
        print(f"{i + 1}/{len(VOCES_ACENTO)} C36 con {modelo}, voz {voz_nombre}...", flush=True)
        try:
            asyncio.run(voz.principal(str(guion_ruta), destino, motor="gemini"))
        except BaseException as e:          # SystemExit incluido: que la otra voz salga igual
            lineas.append(f"--- {voz_nombre}: NO SALIÓ ({e})")
            continue
        toma = destino / "voz" / "toma_entera.mp3"
        oido = ""
        try:
            from faster_whisper import WhisperModel
            m = WhisperModel("small", device="cpu", compute_type="int8")
            trozos, _ = m.transcribe(str(toma), language="es", beam_size=1)
            oido = " ".join(t.text.strip() for t in trozos)
        except Exception as e:
            oido = f"(sin transcripción: {e})"
        sobran = [w for w in _palabras(oido) if w not in del_guion]
        leidas = sorted(set(sobran) & PALABRAS_DE_INSTRUCCION)
        lineas += [f"--- {voz_nombre}: {destino.name}/voz.mp3 (lo que sonaría en el vídeo)",
                   f"palabras oídas que no están en el guion: {len(sobran)} "
                   f"{sorted(set(sobran))[:20]}",
                   ("⚠️ PARECE QUE LEE INSTRUCCIONES: " + ", ".join(leidas)) if leidas
                   else "✅ no se oyen palabras de las instrucciones",
                   f"transcripción: {oido}", ""]
    (salida / "informe_acento.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))


# 12/11/2026, segunda muestra. La primera («acento:») demostró que gemini-3.8-flash-tts
# lee en voz alta TODO el encabezado y las notas de dirección de voz.py (C36): 128 s
# (Charon) y 211 s (Orus, dos veces) para 84 palabras; la producción la rechazó por
# duración. Así que con 3.8 la dirección no puede ir dentro del texto. Esta prueba
# pide el guion sin nada (solo las frases) y con UNA línea de idioma delante, al
# estilo que documenta Google para los modelos TTS («Say cheerfully: …»).
LINEA_ACENTO = "Con acento de España: "
VARIANTES_BREVE = (("solo_texto_charon", "Charon", ""),
                   ("acento_charon", "Charon", LINEA_ACENTO),
                   ("acento_orus", "Orus", LINEA_ACENTO))


def _whisper(ruta):
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "faster-whisper"],
                   check=False)
    try:
        from faster_whisper import WhisperModel
        m = WhisperModel("small", device="cpu", compute_type="int8")
        trozos, _ = m.transcribe(str(ruta), language="es", beam_size=1)
        return " ".join(t.text.strip() for t in trozos)
    except Exception as e:
        return f"(sin transcripción: {e})"


# 12/11/2026, tercera muestra. La segunda dejó claro que 3.8 lee en voz alta
# cualquier indicación, también una sola línea («Con acento de España.»): con 3.8
# solo vale el texto desnudo, y el acento no se puede pedir. Lo único que queda
# para que suene a España es la voz: «voces:» locuta el texto solo con otras voces.
VOCES_SOLO_TEXTO = ("Orus", "Iapetus", "Algenib", "Schedar")


def prueba_breve(guion_ruta, salida, modelo, variantes=None):
    guion = json.loads(guion_ruta.read_text(encoding="utf-8"))
    escs = escenas(guion)
    texto = "\n".join(n for n, _, _ in escs)
    del_guion = set(_palabras(texto))
    n_pal = len(_palabras(texto))
    cli = cliente()
    lineas = [f"Muestra voz-3.8 sin dirección · {guion.get('id')} · modelo {modelo} · "
              f"{n_pal} palabras", ""]
    for i, (nombre, voz_nombre, prefijo) in enumerate(variantes or VARIANTES_BREVE):
        if i:
            time.sleep(ESPERA_ENTRE_PETICIONES)
        print(f"{i + 1}. {nombre}...", flush=True)
        try:
            pcm = pcm_de(cli, modelo, prefijo + texto, [("Narrador", voz_nombre)])
        except BaseException as e:
            lineas += [f"--- {nombre}: NO SALIÓ ({e})", ""]
            continue
        wav = salida / f"{nombre}.wav"
        escribir_wav(pcm, wav)
        dur = len(pcm) / 2 / RITMO
        oido = _whisper(wav)
        sobran = [w for w in _palabras(oido) if w not in del_guion]
        leidas = sorted(set(sobran) & PALABRAS_DE_INSTRUCCION)
        lineas += [f"--- {nombre} ({voz_nombre}{', con «' + prefijo.strip() + '»' if prefijo else ', solo el texto'})",
                   f"duración {dur:.1f} s · {n_pal / dur * 60 if dur else 0:.0f} palabras/min",
                   f"palabras oídas que no están en el guion: {len(sobran)} {sorted(set(sobran))[:20]}",
                   ("⚠️ PARECE QUE LEE INSTRUCCIONES: " + ", ".join(leidas)) if leidas
                   else "✅ no se oyen palabras de las instrucciones",
                   f"transcripción: {oido}", ""]
    (salida / "informe_breve.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--c36", action="store_true",
                    help="C36 con el código de producción (voz.py): una petición")
    ap.add_argument("guion", type=Path, help="«c36:<guion>» equivale a --c36 <guion>")
    ap.add_argument("--salida", type=Path, default=Path("prueba_voz"))
    ap.add_argument("--modelo", default=MODELO,
                    help="por defecto %(default)s; "
                         "gemini-2.5-flash-preview-tts tiene su propia cuota")
    args = ap.parse_args()

    # El workflow «Prueba de voces» no tiene casilla para --c36 (y los workflows
    # no los toca la dirección): escribir «c36:» delante del guion es lo mismo.
    if str(args.guion).startswith("c36:"):
        args.c36, args.guion = True, Path(str(args.guion)[4:])
    if str(args.guion).startswith("voces:"):
        args.salida.mkdir(parents=True, exist_ok=True)
        return prueba_breve(Path(str(args.guion)[6:]), args.salida, args.modelo,
                            [(f"solo_texto_{v.lower()}", v, "") for v in VOCES_SOLO_TEXTO])
    if str(args.guion).startswith("breve:"):
        args.salida.mkdir(parents=True, exist_ok=True)
        return prueba_breve(Path(str(args.guion)[6:]), args.salida, args.modelo)
    if str(args.guion).startswith("acento:"):
        args.salida.mkdir(parents=True, exist_ok=True)
        return prueba_acento(Path(str(args.guion)[7:]), args.salida, args.modelo)
    if args.c36:
        args.salida.mkdir(parents=True, exist_ok=True)
        return prueba_c36(args.guion, args.salida)
    guion = json.loads(args.guion.read_text(encoding="utf-8"))
    escs = escenas(guion)
    if not escs:
        raise SystemExit(f"{args.guion} no tiene narración.")
    args.salida.mkdir(parents=True, exist_ok=True)
    hay_esceptico = any(p == "esceptico" for _, _, p in escs)

    print(f"Guion: {guion.get('id')} · {len(escs)} escenas con voz · "
          f"{sum(len(n.split()) for n, _, _ in escs)} palabras")
    print(f"Modelo: {args.modelo}")
    print("Peticiones a Gemini en esta ejecución: 2 "
          "(el nivel gratuito da 3 por minuto y 10 por día)\n")

    print("1/3 edge-tts (referencia, sin cuota)...", flush=True)
    asyncio.run(pista_edge(escs, args.salida / "edge.mp3"))

    cli = cliente()
    partes = []

    print("2/3 Gemini, guion entero SIN dirección...", flush=True)
    pcm = pcm_de(cli, args.modelo, guion_plano(escs, hay_esceptico),
                 [("Narrador", VOZ_NARRADOR), ("Esceptico", VOZ_ESCEPTICO)]
                 if hay_esceptico else [("Narrador", VOZ_NARRADOR)])
    escribir_wav(pcm, args.salida / "gemini_plano.wav")
    partes.append(informe(pcm, escs, "gemini_plano (sin dirección)",
                          args.salida / "informe_plano.txt"))

    print(f"\n   esperando {ESPERA_ENTRE_PETICIONES:.0f} s por el límite de "
          "3 peticiones por minuto...", flush=True)
    time.sleep(ESPERA_ENTRE_PETICIONES)

    print("3/3 Gemini, guion entero CON dirección de actor...", flush=True)
    pcm = pcm_de(cli, args.modelo, guion_dirigido(escs, hay_esceptico),
                 [("Narrador", VOZ_NARRADOR), ("Esceptico", VOZ_ESCEPTICO)]
                 if hay_esceptico else [("Narrador", VOZ_NARRADOR)])
    escribir_wav(pcm, args.salida / "gemini_dirigido.wav")
    partes.append(informe(pcm, escs, "gemini_dirigido (con dirección)",
                          args.salida / "informe_dirigido.txt"))

    (args.salida / "informe.txt").write_text(
        "\n\n".join(partes) + "\n", encoding="utf-8")

    print(f"\nListo en {args.salida}/. Escúchalos en este orden: edge.mp3 "
          "(lo de hoy), gemini_plano.wav, gemini_dirigido.wav.")
    print("La referencia edge.mp3 va SIN las pausas entre escenas: en "
          "producción las pone ffmpeg. Las de Gemini las decide el modelo, que "
          "es justo lo que se está probando.")


if __name__ == "__main__":
    sys.exit(main())
