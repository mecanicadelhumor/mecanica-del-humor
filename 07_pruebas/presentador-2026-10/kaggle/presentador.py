"""
presentador.py — C51.3, paso 2: el cuaderno de Kaggle de la persona sintética.

Dirección, 23/10/2026. Corre en Kaggle (GPU gratuita, internet activado), lo
sube `prueba_presentador.py` con la CLI de Kaggle. Entrada, en el dataset
privado `<usuario>/presentador-entrada` (montado en /kaggle/input/…):
    cara.jpg          la cara elegida por el codirector (caras.py)
    audio.wav         ~3 s de la voz de un Short ya publicado (cero peticiones a Gemini)
    parametros.json   {"cara": n, "wan_tope_s": 3600, ...}

Hace, y apunta lo que tarda cada paso:
  (a) MOVIMIENTO · ~3 s de cabeza en reposo a partir de la foto.
      - Wan 2.2 TI2V-5B (Apache 2.0, ficha de Hugging Face comprobada el 23/10/2026)
        con Diffusers, a 480p, en un proceso aparte con tope de tiempo: el modelo
        está pensado para 24 GB y bf16, y en Kaggle hay T4 (16 GB, sin bf16
        nativo) o P100. Si no cabe, no contesta a tiempo o falla, se dice y se sigue.
      - PLAN B, siempre (es barato y sirve de comparación): un vaivén sutil de la
        foto (giro de ±0,8°, escala ±1 %, 4 px), determinista, sin modelo.
  (b) LABIOS · MuseTalk 1.5 (MIT, código y pesos) sobre cada vídeo de (a), con
      DOS cambios por licencia (LICENCIAS.md §3):
      - la máscara de la boca NO usa BiSeNet `79999_iter.pth` (entrenado con
        CelebAMask-HQ, no comercial): es una elipse fija centrada en la cara;
      - la caja de la cara NO usa DWPose/mmpose (mmcv 2.0.1 pide torch 2.0 y no
        se instala en el torch de Kaggle): es la del detector S3FD que MuseTalk
        ya trae (face_alignment, BSD-3; sus pesos los baja él mismo la primera
        vez), que es lo que el original usa cuando DWPose no le sirve.
      Ni `syncnet` (LatentSync, solo para entrenar) ni `face-parse-bisent` se bajan.
  (c) SALIDA en /kaggle/working/salida/: los mp4, `tiempos.json` (cada paso, la
      GPU, las versiones) y `registro.txt`.

Nada de aquí entra en un vídeo sin que el codirector lo mire (C51.2).
"""
import json
import os
import shutil
import subprocess
import sys
import textwrap
import time
import traceback
from pathlib import Path

# Dónde monta Kaggle el dataset ha cambiado (/kaggle/input/<nombre>/ o más hondo, p. ej.
# /kaggle/input/datasets/<usuario>/<nombre>/): se busca la carpeta que tenga cara.jpg.
# El primer intento (23/10/2026) no la encontró en /kaggle/input/presentador-entrada.
ENTRADA = next((p.parent for p in sorted(Path("/kaggle/input").rglob("cara.jpg"))),
               Path("/kaggle/input/presentador-entrada"))
# Lo pesado (MuseTalk, pesos, fotogramas) va a /tmp: todo lo que quede en
# /kaggle/working se lo baja después la CLI, y serían varios GB.
TRABAJO = Path("/tmp/presentador")
TRABAJO.mkdir(parents=True, exist_ok=True)
SALIDA = Path("/kaggle/working/salida")
SALIDA.mkdir(parents=True, exist_ok=True)
MUSETALK_COMMIT = "0a89dec45a0192b824e3cf4daf96c239440c5ed8"   # el que se leyó el 23/10/2026

T = {"pasos": {}, "errores": {}}
REGISTRO = open(SALIDA / "registro.txt", "a", encoding="utf-8")


def log(*a):
    texto = " ".join(str(x) for x in a)
    print(texto, flush=True)
    REGISTRO.write(texto + "\n")
    REGISTRO.flush()


def sh(cmd, timeout=None, cwd=None, env=None):
    log("$", cmd if isinstance(cmd, str) else " ".join(cmd))
    r = subprocess.run(cmd, shell=isinstance(cmd, str), cwd=cwd, env=env, timeout=timeout,
                       capture_output=True, text=True)
    for linea in (r.stdout + r.stderr).splitlines()[-40:]:
        log("   ", linea)
    if r.returncode != 0:
        raise RuntimeError(f"código {r.returncode}: {cmd}")
    return r


def paso(nombre):
    """Cronometra un paso; si falla, apunta el error y deja seguir a los demás."""
    class _P:
        def __enter__(self):
            self.t0 = time.time()
            log(f"\n=== {nombre} ===")
        def __exit__(self, tipo, ex, tb):
            T["pasos"][nombre] = round(time.time() - self.t0, 1)
            if ex is not None:
                T["errores"][nombre] = f"{tipo.__name__}: {ex}"
                log("".join(traceback.format_exception(tipo, ex, tb))[-3000:])
            guardar()
            return True
    return _P()


def guardar():
    (SALIDA / "tiempos.json").write_text(json.dumps(T, ensure_ascii=False, indent=1), "utf-8")


PARAM = {"cara": 1, "wan_tope_s": 3600, "wan_alto": 480, "wan_ancho": 480, "wan_fotogramas": 73,
         "wan_pasos": 30, "segundos": 3.0}
if (ENTRADA / "parametros.json").exists():
    PARAM.update(json.loads((ENTRADA / "parametros.json").read_text("utf-8")))
T["parametros"] = PARAM
CARA = ENTRADA / "cara.jpg"
AUDIO = ENTRADA / "audio.wav"

# ---------------------------------------------------------------------------
with paso("0 · la máquina"):
    r = subprocess.run("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader",
                       shell=True, capture_output=True, text=True)
    T["gpu"] = r.stdout.strip() or "sin GPU"
    import socket
    try:
        socket.create_connection(("github.com", 443), timeout=10).close()
        T["internet"] = True
    except OSError as ex:
        T["internet"] = False
        log("Sin internet:", ex)
    T["entrada"] = str(ENTRADA)
    T["kaggle_input"] = sorted(str(p) for p in Path("/kaggle/input").rglob("*"))[:40]
    log("Entrada:", ENTRADA, "· en /kaggle/input:", T["kaggle_input"])
    import torch
    T["torch"] = torch.__version__
    T["cuda"] = torch.version.cuda
    T["bf16_nativo"] = bool(torch.cuda.is_available() and torch.cuda.is_bf16_supported())
    log("GPU:", T["gpu"], "· torch", T["torch"], "· bf16:", T["bf16_nativo"])
    assert CARA.exists() and AUDIO.exists(), f"faltan cara.jpg o audio.wav en {ENTRADA}"
    shutil.copy(CARA, SALIDA / "cara.jpg")

# Sin GPU o sin internet no hay nada que probar: Kaggle los da solo a cuentas con el
# teléfono verificado (kaggle.com → Settings → Phone verification), y si no, ignora en
# silencio enable_gpu y enable_internet. Mejor decirlo claro que fallar en cada paso.
FALTA = [n for n, ok in (("GPU", T["gpu"] != "sin GPU"), ("internet", T.get("internet"))) if not ok]
if FALTA:
    T["resultado"] = ("sin vídeo: Kaggle no ha dado " + " ni ".join(FALTA) + ". Casi seguro, la cuenta no "
                      "tiene el teléfono verificado (kaggle.com → Settings → Phone verification).")
    guardar()
    log("\nRESUMEN:", json.dumps(T, ensure_ascii=False, indent=1))
    sys.exit(0)

# ---------------------------------------------------------------------------
# (a) Movimiento
# ---------------------------------------------------------------------------
MOVIMIENTOS = {}   # nombre -> mp4 a 25 fps

with paso("a.1 · plan B: vaivén de la foto"):
    import cv2
    import numpy as np
    im = cv2.imread(str(CARA))
    h, w = im.shape[:2]
    c = min(h, w)                                   # cuadrado central: no se deforma
    im = im[(h - c) // 2:(h - c) // 2 + c, (w - c) // 2:(w - c) // 2 + c]
    lado = 512
    im = cv2.resize(im, (lado, lado), interpolation=cv2.INTER_AREA)
    n = int(round(PARAM["segundos"] * 25))
    destino = TRABAJO / "mov_afin.mp4"
    vw = cv2.VideoWriter(str(destino), cv2.VideoWriter_fourcc(*"mp4v"), 25, (lado, lado))
    for i in range(n):
        t = i / 25.0
        ang = 0.8 * np.sin(2 * np.pi * t / 3.1)           # grados: un balanceo lento
        esc = 1.0 + 0.01 * np.sin(2 * np.pi * t / 2.3)    # respiración
        dx = 4 * np.sin(2 * np.pi * t / 3.7)
        dy = 2 * np.sin(2 * np.pi * t / 2.9)
        M = cv2.getRotationMatrix2D((lado / 2, lado * 0.62), ang, esc * 1.03)  # 3 % de zoom: sin bordes
        M[0, 2] += dx
        M[1, 2] += dy
        vw.write(cv2.warpAffine(im, M, (lado, lado), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT))
    vw.release()
    sh(["ffmpeg", "-y", "-v", "error", "-i", str(destino), "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(SALIDA / "a_movimiento_afin.mp4")])
    MOVIMIENTOS["afin"] = destino

WAN = textwrap.dedent(r'''
    import json, sys, time, torch
    from diffusers import AutoencoderKLWan, WanImageToVideoPipeline
    from diffusers.utils import export_to_video, load_image
    p = json.loads(sys.argv[1])
    t0 = time.time()
    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    mid = "Wan-AI/Wan2.2-TI2V-5B-Diffusers"
    vae = AutoencoderKLWan.from_pretrained(mid, subfolder="vae", torch_dtype=torch.float32)
    pipe = WanImageToVideoPipeline.from_pretrained(mid, vae=vae, torch_dtype=dtype)
    pipe.enable_model_cpu_offload()          # 16 GB: el codificador de texto vive en la CPU
    try:
        pipe.vae.enable_tiling()
    except Exception:
        pass
    print("cargado en", round(time.time() - t0, 1), "s; dtype", dtype, flush=True)
    img = load_image(p["cara"]).resize((p["wan_ancho"], p["wan_alto"]))
    out = pipe(image=img,
               prompt=("a friendly presenter looks at the camera and stays still, calm breathing, "
                       "subtle natural head movement, blinks once, mouth closed, static camera, "
                       "plain dark blue background"),
               negative_prompt="talking, open mouth, camera movement, zoom, text, subtitles, distorted face",
               height=p["wan_alto"], width=p["wan_ancho"], num_frames=p["wan_fotogramas"],
               num_inference_steps=p["wan_pasos"], guidance_scale=5.0,
               generator=torch.Generator("cpu").manual_seed(20261023)).frames[0]
    export_to_video(out, p["salida"], fps=24)
    print("hecho en", round(time.time() - t0, 1), "s; pico de memoria",
          round(torch.cuda.max_memory_allocated() / 2**30, 1), "GB", flush=True)
''')

with paso("a.2 · Wan 2.2 TI2V-5B"):
    (TRABAJO / "wan.py").write_text(WAN, "utf-8")
    sh("pip install -q 'git+https://github.com/huggingface/diffusers' accelerate ftfy", timeout=1200)
    crudo = TRABAJO / "mov_wan_24.mp4"
    args = dict(PARAM, cara=str(CARA), salida=str(crudo))
    try:
        sh([sys.executable, str(TRABAJO / "wan.py"), json.dumps(args)], timeout=int(PARAM["wan_tope_s"]))
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Wan no terminó en {PARAM['wan_tope_s']} s (tope)")
    destino = TRABAJO / "mov_wan.mp4"
    sh(["ffmpeg", "-y", "-v", "error", "-i", str(crudo), "-vf", "fps=25", "-c:v", "libx264",
        "-pix_fmt", "yuv420p", str(destino)])
    shutil.copy(destino, SALIDA / "a_movimiento_wan.mp4")
    MOVIMIENTOS["wan"] = destino

T["movimientos"] = sorted(MOVIMIENTOS)

# ---------------------------------------------------------------------------
# (b) MuseTalk 1.5, sin BiSeNet ni DWPose
# ---------------------------------------------------------------------------
MT = TRABAJO / "MuseTalk"

PREPROCESADO = textwrap.dedent(r'''
    """Sustituye a musetalk/utils/preprocessing.py (dirección, 23/10/2026): sin
    DWPose/mmpose (mmcv 2.0.1 pide torch 2.0 y no se instala en el de Kaggle).
    La caja de la cara es la del detector S3FD que MuseTalk ya trae
    (musetalk/utils/face_detection, de face_alignment, BSD-3), que es lo mismo
    que el original usa cuando la caja de los puntos de DWPose no le sirve.
    `upperbondrange` (bbox_shift) mueve el borde de arriba, como en el original."""
    import cv2
    import numpy as np
    import torch
    from tqdm import tqdm
    from face_detection import FaceAlignment, LandmarksType

    coord_placeholder = (0.0, 0.0, 0.0, 0.0)
    fa = FaceAlignment(LandmarksType._2D, flip_input=False,
                       device="cuda" if torch.cuda.is_available() else "cpu")

    def read_imgs(img_list):
        return [cv2.imread(p) for p in tqdm(img_list, desc="leyendo")]

    def get_landmark_and_bbox(img_list, upperbondrange=0):
        frames = read_imgs(img_list)
        coords = []
        for f in tqdm(frames, desc="caras (S3FD)"):
            caja = fa.get_detections_for_batch(np.asarray([f]))[0]
            if caja is None:
                coords.append(coord_placeholder)
                continue
            x1, y1, x2, y2 = caja
            y1 = max(0, min(y2 - 1, y1 + int(upperbondrange)))
            coords.append((x1, y1, x2, y2))
        return coords, frames
''')

MASCARA = textwrap.dedent(r'''
    """Sustituye a musetalk/utils/face_parsing (dirección, 23/10/2026): sin BiSeNet
    `79999_iter.pth` (CelebAMask-HQ, uso no comercial). La máscara es una elipse
    fija: get_image() le pasa el recorte ampliado 1,5x alrededor de la cara, así
    que la cara ocupa los dos tercios centrales; la elipse cubre de mejilla a
    mejilla y del medio de la nariz al mentón. Luego get_image() se queda con la
    mitad de abajo y la difumina, como con el original."""
    import cv2
    import numpy as np
    from PIL import Image

    class FaceParsing:
        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, image, size=(512, 512), mode="raw"):
            w, h = size
            m = np.zeros((h, w), dtype=np.uint8)
            cv2.ellipse(m, (w // 2, int(h * 0.56)), (int(w * 0.26), int(h * 0.30)), 0, 0, 360, 255, -1)
            return Image.fromarray(m)
''')

with paso("b.1 · MuseTalk: código, dependencias y pesos"):
    if not MT.exists():
        sh(f"git clone -q https://github.com/TMElyralab/MuseTalk.git {MT}")
    sh(f"git checkout -q {MUSETALK_COMMIT}", cwd=MT)
    (MT / "musetalk/utils/preprocessing.py").write_text(PREPROCESADO, "utf-8")
    fp = MT / "musetalk/utils/face_parsing"
    for f in fp.glob("*.py"):
        f.unlink()
    (fp / "__init__.py").write_text(MASCARA, "utf-8")
    sh("pip install -q omegaconf einops librosa soundfile "
       "'huggingface_hub>=0.30' ffmpeg-python", timeout=900)
    from huggingface_hub import hf_hub_download, snapshot_download
    modelos = MT / "models"
    modelos.mkdir(exist_ok=True)
    for f in ("musetalkV15/musetalk.json", "musetalkV15/unet.pth"):
        hf_hub_download("TMElyralab/MuseTalk", f, local_dir=modelos)                    # MIT
    snapshot_download("stabilityai/sd-vae-ft-mse", local_dir=modelos / "sd-vae",
                      allow_patterns=["config.json", "diffusion_pytorch_model.bin"])    # MIT
    snapshot_download("openai/whisper-tiny", local_dir=modelos / "whisper",
                      allow_patterns=["config.json", "pytorch_model.bin", "preprocessor_config.json"])  # MIT
    r = subprocess.run("pip freeze | grep -i -E '^(torch|diffusers|transformers)=='",
                       shell=True, capture_output=True, text=True)
    T["versiones"] = r.stdout.split()

for nombre, mov in list(MOVIMIENTOS.items()):
    with paso(f"b.2 · MuseTalk sobre «{nombre}»"):
        cfg = MT / f"tarea_{nombre}.yaml"
        cfg.write_text(f'tarea:\n  video_path: "{mov}"\n  audio_path: "{AUDIO}"\n'
                       f'  result_name: "b_{nombre}.mp4"\n', "utf-8")
        res = TRABAJO / f"res_{nombre}"
        sh([sys.executable, "-m", "scripts.inference", "--inference_config", str(cfg),
            "--result_dir", str(res), "--unet_model_path", "models/musetalkV15/unet.pth",
            "--unet_config", "models/musetalkV15/musetalk.json", "--version", "v15",
            "--ffmpeg_path", "/usr/bin", "--use_float16", "--batch_size", "8"],
           cwd=MT, timeout=1800)
        hecho = next(res.rglob(f"b_{nombre}.mp4"), None)
        if not hecho:
            raise RuntimeError("MuseTalk terminó sin dejar vídeo (mira registro.txt)")
        shutil.copy(hecho, SALIDA / f"b_labios_{nombre}.mp4")

# ---------------------------------------------------------------------------
# (c) Resumen
# ---------------------------------------------------------------------------
T["salida"] = sorted(p.name for p in SALIDA.iterdir())
T["resultado"] = ("con labios: " + ", ".join(n for n in MOVIMIENTOS if (SALIDA / f"b_labios_{n}.mp4").exists())) \
    if any((SALIDA / f"b_labios_{n}.mp4").exists() for n in MOVIMIENTOS) else "sin vídeo con labios"
guardar()
log("\nRESUMEN:", json.dumps(T, ensure_ascii=False, indent=1))
