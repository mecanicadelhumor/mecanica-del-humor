#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
corte_palabras.py — C36: partir una toma de voz entera en escenas, por palabras.

NO está en la producción todavía. Es la pieza de C36 (versión 9 del plan, 15/09;
escrita el 12/10/2026) que hacía falta antes de probar «un Short, una llamada»:
si Gemini dice el Short entero de una vez, ¿dónde empieza cada escena?

Por silencios no (04/09: 16 y 33 tramos para 6 escenas, ningún umbral daba 6).
Por palabras: Whisper (`faster-whisper`, el mismo `tiny` en CPU que ya usa
voz.py para C66) devuelve cada palabra con su instante; el texto de cada escena
se conoce, así que se casan las dos secuencias (difflib, sobre palabras
normalizadas) y la frontera entre la escena k y la k+1 es el hueco entre la
última palabra casada de una y la primera de la otra. Se corta en el punto más
silencioso de ese hueco.

    python3 corte_palabras.py toma.mp3 guion.json      # imprime los cortes

Devuelve también, por escena, lo que Whisper oyó: es la misma comprobación de
C66 (la voz dice el guion) hecha sobre la toma entera.
"""
import difflib
import json
import re
import subprocess
import sys
import unicodedata
from array import array

HZ = 16000            # para medir silencios basta con esto
VENTANA_S = 0.02
HUECO_MINIMO_S = 0.2


def tokens(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9ñ]+", s)


def _muestras(mp3):
    crudo = subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-i", str(mp3), "-f", "s16le", "-ac", "1",
         "-ar", str(HZ), "-"], capture_output=True, check=True,
        stdin=subprocess.DEVNULL).stdout
    a = array("h"); a.frombytes(crudo[: len(crudo) // 2 * 2])
    return a


def _mas_silencioso(muestras, desde, hasta):
    """El instante (s) de la ventana de menos energía entre desde y hasta."""
    paso = int(VENTANA_S * HZ)
    i0, i1 = int(desde * HZ), int(hasta * HZ)
    if i1 - i0 < paso:
        return (desde + hasta) / 2
    mejor, donde = None, i0
    for i in range(i0, i1 - paso + 1, paso // 2):
        e = sum(x * x for x in muestras[i:i + paso])
        if mejor is None or e < mejor:
            mejor, donde = e, i
    return (donde + paso / 2) / HZ


def palabras_oidas(mp3, modelo=None):
    if modelo is None:
        from faster_whisper import WhisperModel
        modelo = WhisperModel("tiny", device="cpu", compute_type="int8")
    trozos, _ = modelo.transcribe(str(mp3), language="es", beam_size=1,
                                  word_timestamps=True, vad_filter=False,
                                  condition_on_previous_text=False)
    out = []
    for t in trozos:
        for w in (t.words or []):
            for tok in tokens(w.word):
                out.append((tok, w.start, w.end))
    return out


def cortar(mp3, textos, modelo=None):
    """Cortes (s) entre escenas y un informe por escena.

    `textos` es la narración de cada escena, en orden. Devuelve (cortes, informe):
    len(cortes) == len(textos) - 1. Lanza ValueError si alguna frontera no se
    puede situar (ninguna palabra casada a uno de los dos lados): en ese caso la
    toma no se usa y se vuelve a una llamada por escena.
    """
    escritas, escena_de = [], []
    for k, t in enumerate(textos):
        for tok in tokens(t):
            escritas.append(tok); escena_de.append(k)
    oidas = palabras_oidas(mp3, modelo)
    sm = difflib.SequenceMatcher(a=escritas, b=[o[0] for o in oidas], autojunk=False)
    casada = {}                      # índice escrito -> índice oído
    for bl in sm.get_matching_blocks():
        for j in range(bl.size):
            casada[bl.a + j] = bl.b + j
    muestras = _muestras(mp3)
    cortes, informe = [], []
    for k in range(len(textos) - 1):
        de_k = [i for i, e in enumerate(escena_de) if e == k and i in casada]
        de_sig = [i for i, e in enumerate(escena_de) if e == k + 1 and i in casada]
        if not de_k or not de_sig:
            raise ValueError(f"frontera {k + 1}-{k + 2}: sin palabras casadas a un lado")
        fin = oidas[casada[max(de_k)]][2]
        ini = oidas[casada[min(de_sig)]][1]
        if ini < fin:                # Whisper solapa a veces unas centésimas
            ini, fin = fin, ini
        # Hueco demasiado estrecho: Whisper ha pegado las dos palabras (MDS-023,
        # 4-5: las dos en 27,8 s y el silencio de verdad entre 27,9 y 28,5). Se
        # busca un poco a cada lado.
        if ini - fin < HUECO_MINIMO_S:
            fin, ini = max(0.0, fin - 0.15), ini + 0.6
        cortes.append(round(_mas_silencioso(muestras, fin, ini), 3))
    for k, t in enumerate(textos):
        n = sum(1 for e in escena_de if e == k)
        c = sum(1 for i, e in enumerate(escena_de) if e == k and i in casada)
        informe.append({"escena": k + 1, "palabras": n, "casadas": c})
    return cortes, informe


if __name__ == "__main__":
    toma, guion = sys.argv[1], sys.argv[2]
    g = json.load(open(guion, encoding="utf-8"))
    textos = [e.get("narracion", "") for e in g["escenas"] if (e.get("narracion") or "").strip()]
    c, inf = cortar(toma, textos)
    print(json.dumps({"cortes_s": c, "escenas": inf}, ensure_ascii=False, indent=1))
