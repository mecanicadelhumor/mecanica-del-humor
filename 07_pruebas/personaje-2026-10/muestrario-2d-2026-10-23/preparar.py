"""Muestrario 2D (C61) · paso 1: la pista de interpretación.

Saca del audio (y de nada más) lo que necesita la página para mover al personaje:
  - las palabras con su tiempo (faster-whisper «tiny», palabra a palabra, como C36/C66);
  - la envolvente de energía del audio a 30 fps (cuánto abre la boca).
Lo escribe en pista.json. Determinista: mismo audio, mismo fichero.

Uso: python preparar.py AUDIO.mp3 INICIO_S FIN_S
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

AQUI = Path(__file__).parent
FPS = 30


def muestras(audio, a, b, sr=16000):
    crudo = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(a), "-to", str(b), "-i", str(audio),
         "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
        check=True, capture_output=True).stdout
    return np.frombuffer(crudo, dtype=np.float32), sr


def main():
    audio, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    x, sr = muestras(audio, a, b)

    from faster_whisper import WhisperModel
    m = WhisperModel("tiny", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(x, language="es", word_timestamps=True)
    palabras = [{"w": w.word.strip(), "a": round(float(w.start), 3), "b": round(float(w.end), 3)}
                for s in segs for w in s.words]

    # Envolvente: RMS por fotograma, suavizada y normalizada al percentil 95.
    n = int((b - a) * FPS)
    paso = sr // FPS
    rms = np.array([np.sqrt(np.mean(x[i * paso:(i + 1) * paso] ** 2) + 1e-12) for i in range(n)])
    rms = np.convolve(rms, np.ones(3) / 3, mode="same")
    env = np.clip(rms / np.percentile(rms, 95), 0, 1)

    pista = {"fps": FPS, "duracion": round(b - a, 3), "palabras": palabras,
             "env": [round(float(v), 3) for v in env]}
    (AQUI / "pista.json").write_text(json.dumps(pista, ensure_ascii=False))
    print(len(palabras), "palabras,", n, "fotogramas")


if __name__ == "__main__":
    main()
