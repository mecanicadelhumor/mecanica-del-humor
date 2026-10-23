#!/usr/bin/env python3
"""
prueba_presentador.py — C51.3: lo que ejecuta el workflow «Prueba del presentador».

Dirección, 23/10/2026. Dos pasos, cada uno a mano desde Actions:

  caras                genera las ocho caras candidatas (caras.py) y su hoja.
  kaggle --cara N      con la cara N y ~3 s de voz ya publicada:
                         1. prepara la entrada (cara.jpg, audio.wav, parametros.json);
                         2. la sube como dataset PRIVADO <usuario>/presentador-entrada
                            (versión nueva si ya existe);
                         3. sube y lanza el cuaderno kaggle/ como <usuario>/presentador-prueba
                            (privado, GPU, internet);
                         4. espera a que termine (tope --tope-min, 150 por defecto);
                         5. baja la salida a 07_pruebas/presentador-2026-10/salida/.

Claves (secretos de GitHub, nunca en el repositorio):
  caras   CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN
  kaggle  KAGGLE_USERNAME y KAGGLE_API_TOKEN (el secreto KAGGLE_KEY: LICENCIAS.md §1)

Cero peticiones a Gemini: la voz sale de 07_pruebas/c36-2026-10-22/c36.mp3, que
es la del Short MDS-045 tal como la oyó el codirector el 22/10.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
CARAS = AQUI / "caras"
SALIDA = AQUI / "salida"
VOZ = RAIZ / "07_pruebas" / "c36-2026-10-22" / "c36.mp3"
DATASET, KERNEL = "presentador-entrada", "presentador-prueba"


def sh(cmd, comprobar=True, **kw):
    print("$", " ".join(map(str, cmd)), flush=True)
    r = subprocess.run(list(map(str, cmd)), capture_output=True, text=True, **kw)
    salida = (r.stdout + r.stderr).strip()
    if salida:
        print(salida[-4000:], flush=True)
    if comprobar and r.returncode != 0:
        raise SystemExit(f"Falló (código {r.returncode}): {' '.join(map(str, cmd))}")
    return r.returncode, salida


def paso_caras(args):
    return subprocess.call([sys.executable, str(AQUI / "caras.py")])


def preparar_entrada(destino, args, usuario):
    cara = CARAS / f"cara_{args.cara}.jpg"
    if not cara.exists():
        raise SystemExit(f"No existe {cara.relative_to(RAIZ)}: lanza antes el paso «caras».")
    shutil.copy(cara, destino / "cara.jpg")
    sh(["ffmpeg", "-y", "-v", "error", "-ss", f"{args.desde:.2f}", "-t", f"{args.segundos:.2f}",
        "-i", VOZ, "-ac", "1", "-ar", "16000", destino / "audio.wav"])
    (destino / "parametros.json").write_text(json.dumps({
        "cara": args.cara, "segundos": args.segundos, "wan_tope_s": args.wan_tope_min * 60,
        "voz": f"{VOZ.relative_to(RAIZ)} desde {args.desde} s"}, ensure_ascii=False, indent=1), "utf-8")
    (destino / "dataset-metadata.json").write_text(json.dumps({
        "title": DATASET, "id": f"{usuario}/{DATASET}", "licenses": [{"name": "other"}]}, indent=1), "utf-8")


def estado_kernel(usuario):
    _, txt = sh(["kaggle", "kernels", "status", f"{usuario}/{KERNEL}"], comprobar=False)
    txt = txt.lower()
    for clave in ("complete", "error", "cancel"):
        if clave in txt:
            return clave
    return "running" if ("running" in txt or "queued" in txt) else txt[-80:]


def paso_kaggle(args):
    usuario = os.environ.get("KAGGLE_USERNAME")
    if not (usuario and (os.environ.get("KAGGLE_API_TOKEN") or os.environ.get("KAGGLE_KEY"))):
        print("Faltan KAGGLE_USERNAME o KAGGLE_API_TOKEN: no se lanza nada.")
        return 2
    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        entrada, cuaderno = tmp / "entrada", tmp / "cuaderno"
        entrada.mkdir()
        preparar_entrada(entrada, args, usuario)

        # Dataset privado: si ya existe, versión nueva.
        codigo, txt = sh(["kaggle", "datasets", "create", "-p", entrada], comprobar=False)
        if codigo != 0 or "already" in txt.lower() or "exist" in txt.lower():
            sh(["kaggle", "datasets", "version", "-p", entrada, "-m", f"cara {args.cara}"])
        for _ in range(60):                      # hasta 10 min a que Kaggle lo procese
            _, txt = sh(["kaggle", "datasets", "status", f"{usuario}/{DATASET}"], comprobar=False)
            if "ready" in txt.lower():
                break
            time.sleep(10)

        shutil.copytree(AQUI / "kaggle", cuaderno)
        meta = json.loads((cuaderno / "kernel-metadata.json").read_text("utf-8"))
        meta["id"] = f"{usuario}/{KERNEL}"
        meta["dataset_sources"] = [f"{usuario}/{DATASET}"]
        (cuaderno / "kernel-metadata.json").write_text(json.dumps(meta, indent=1), "utf-8")
        sh(["kaggle", "kernels", "push", "-p", cuaderno])

    time.sleep(30)
    final, limite = "running", time.time() + args.tope_min * 60
    while time.time() < limite:
        final = estado_kernel(usuario)
        print(f"[{int(time.time() - t0)} s] estado: {final}", flush=True)
        if final in ("complete", "error", "cancel"):
            break
        time.sleep(60)

    # Se vacía salida/ menos su .gitignore (el que deja subir los .mp4; el 23/10 el
    # rmtree se lo llevó en el commit del bot).
    SALIDA.mkdir(parents=True, exist_ok=True)
    for viejo in SALIDA.iterdir():
        if viejo.name != ".gitignore":
            shutil.rmtree(viejo) if viejo.is_dir() else viejo.unlink()
    sh(["kaggle", "kernels", "output", f"{usuario}/{KERNEL}", "-p", SALIDA], comprobar=False)
    # El cuaderno escribe en /kaggle/working/salida/; la CLI lo baja con esa carpeta delante.
    anidada = SALIDA / "salida"
    if anidada.is_dir():
        for f in anidada.iterdir():
            shutil.move(str(f), SALIDA / f.name)
        anidada.rmdir()
    tiempos = {}
    if (SALIDA / "tiempos.json").exists():
        tiempos = json.loads((SALIDA / "tiempos.json").read_text("utf-8"))
    videos = sorted(p.name for p in SALIDA.glob("b_labios_*.mp4"))
    resumen = {"cara": args.cara, "estado_kaggle": final, "minutos": round((time.time() - t0) / 60, 1),
               "resultado": tiempos.get("resultado", "sin tiempos.json"), "videos": videos,
               "errores": tiempos.get("errores", {}),
               "ficheros": sorted(p.name for p in SALIDA.iterdir() if p.name != ".gitignore")}
    (SALIDA / "estado.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1), "utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=1))
    # En rojo si no hay vídeo con labios: el 23/10 salió en verde sin nada dentro.
    return 0 if final == "complete" and videos else 1


def main():
    ap = argparse.ArgumentParser(description="Prueba del presentador sintético (C51.3)")
    sub = ap.add_subparsers(dest="paso", required=True)
    sub.add_parser("caras", help="las ocho caras candidatas y su hoja")
    k = sub.add_parser("kaggle", help="movimiento + labios en Kaggle con la cara elegida")
    k.add_argument("--cara", type=int, default=1, help="número de la cara (1-8), de la hoja")
    k.add_argument("--desde", type=float, default=0.3, help="segundo de c36.mp3 donde empieza la voz")
    k.add_argument("--segundos", type=float, default=3.0)
    k.add_argument("--wan-tope-min", type=int, default=60, help="tope para Wan 2.2 dentro de Kaggle")
    k.add_argument("--tope-min", type=int, default=150, help="cuánto se espera al cuaderno")
    args = ap.parse_args()
    return paso_caras(args) if args.paso == "caras" else paso_kaggle(args)


if __name__ == "__main__":
    sys.exit(main())
