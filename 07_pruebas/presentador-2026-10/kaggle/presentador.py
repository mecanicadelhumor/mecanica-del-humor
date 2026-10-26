"""
presentador.py — C51.3, paso 2: el cuaderno de Kaggle de la persona sintética.

Dirección, 23/10/2026. Corre en Kaggle (GPU gratuita, internet activado), lo
sube `prueba_presentador.py` con la CLI de Kaggle. Entrada, en el dataset
privado `<usuario>/presentador-entrada` (montado en /kaggle/input/…):
    cara.jpg          la cara elegida por el codirector (caras.py)
    audio.wav         ~3 s de la voz de un Short ya publicado (cero peticiones a Gemini)
    parametros.json   {"cara": n, "wan_tope_s": 3600, ...}

Hace, y apunta lo que tarda cada paso:
  (a) MOVIMIENTO · ~3 s de cabeza en reposo a partir de la foto, EN VERTICAL a
      704x1280 (la resolución nativa de Wan 2.2 5B; el Short es 1080x1920).
      - PLAN B, siempre (es barato y sirve de comparación): un vaivén sutil de la
        foto (giro de ±0,8°, escala ±1 %, 4 px), determinista, sin modelo.
      - Wan 2.2 TI2V-5B (Apache 2.0, ficha de Hugging Face comprobada el 23/10/2026)
        con Diffusers, en un proceso aparte con tope de tiempo. 26/10/2026: SIN
        bajar la resolución nunca (lo pidió el codirector: si sale pixelado no vale).
        Por qué fallaba: en la T4 (Turing) no hay bf16 de verdad, y con bf16 PyTorch
        no puede usar la atención eficiente en memoria: cae en la «matemática», que
        guarda la matriz de atención entera (por eso pedía 1,6 GB más incluso a
        320x320, con la memoria aún ocupada por el intento anterior). Ahora:
          1. el transformador en fp16 (la T4 lo hace nativo y con atención
             eficiente) y **por bloques**: solo el bloque que se está usando vive
             en la GPU (el modelo entero son 10 GB de los 14,5 de la tarjeta, y
             con él dentro no caben las activaciones: así falló el primer intento
             del 26/10). Si aún falta memoria, capa a capa («hojas»);
          2. si fp16 se desborda (NaN en los primeros pasos, se mira en cada
             paso), bf16 con la atención calculada en fp32 (también eficiente en T4).
        Cada intento en un proceso nuevo: la memoria del que falla no se arrastra.
  (b) LABIOS · LatentSync 1.6 (código Apache 2.0, pesos OpenRAIL++-M: uso
      comercial permitido) sobre cada vídeo de (a): genera la boca a 512x512 y con
      capas temporales (no tiembla). En su propio entorno (Python 3.10 y las
      versiones que pide, con uv), fp16 forzado (su código solo lo usa si la GPU
      es de capacidad > 7 y la T4 es 7.5), y SIN InsightFace (sus modelos son
      solo para investigación): los tres puntos que usa para alinear (centro de
      cada ceja y de la nariz) salen de MediaPipe Face Mesh (Apache 2.0). Si la
      1.6 no cabe, la 1.5 (boca a 256). LATENTSYNC.md.
  (b') MuseTalk 1.5, solo si parametros.json trae "musetalk": true (el codirector
      ya lo vio el 23/10: pixelado; queda para comparar). MIT, con
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
Orden (26/10/2026): vaivén → LatentSync sobre el vaivén → Wan → LatentSync sobre
Wan → (MuseTalk). Así, aunque Wan se coma el tiempo, ya hay un vídeo bueno.
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
# Ningún pip install puede subir huggingface_hub a la 2.x: el transformers de Kaggle
# (5.16) pide >=1.5,<2.0 y, si no, no importa (Wan y MuseTalk lo usan). 23/10/2026.
HUB = "'huggingface_hub>=1.5,<2'"

T = {"pasos": {}, "errores": {}}
REGISTRO = open(SALIDA / "registro.txt", "a", encoding="utf-8")


def log(*a):
    texto = " ".join(str(x) for x in a)
    print(texto, flush=True)
    REGISTRO.write(texto + "\n")
    REGISTRO.flush()


def sh(cmd, timeout=None, cwd=None, env=None):
    log("$", cmd if isinstance(cmd, str) else " ".join(cmd))
    # stderr dentro de stdout: el 23/10 el registro ponía los avisos de Wan (stdout)
    # después de las barras de progreso (stderr) y no se veía en qué tamaño falló.
    r = subprocess.run(cmd, shell=isinstance(cmd, str), cwd=cwd, env=env, timeout=timeout,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for linea in r.stdout.replace("\r", "\n").splitlines()[-60:]:
        log("   ", linea)
    if r.returncode != 0:
        cola = " / ".join(l.strip() for l in r.stdout.splitlines()[-4:] if l.strip())
        raise RuntimeError(f"código {r.returncode}: {cmd if isinstance(cmd, str) else cmd[:3]} · {cola[-500:]}")
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


# 26/10/2026: 704x1280 vertical (nativa de Wan 2.2 5B) y 50 pasos (los de su ficha).
# Los tamaños de respaldo (384, 320) se han quitado: más pequeño no vale.
PARAM = {"cara": 1, "wan_tope_s": 4500, "wan_alto": 1280, "wan_ancho": 704, "wan_fotogramas": 77,
         "wan_pasos": 50, "segundos": 3.0, "latentsync_pasos": 20, "musetalk": False}
if (ENTRADA / "parametros.json").exists():
    PARAM.update(json.loads((ENTRADA / "parametros.json").read_text("utf-8")))
ANCHO, ALTO = int(PARAM["wan_ancho"]), int(PARAM["wan_alto"])
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
    # La cara es cuadrada (1024): se recorta en vertical (9:16 centrado, no se deforma)
    # y se escala a 704x1280. Esta misma imagen es la que recibe Wan.
    cw = min(w, int(round(h * ANCHO / ALTO)))
    im = im[:, (w - cw) // 2:(w - cw) // 2 + cw]
    im = cv2.resize(im, (ANCHO, ALTO), interpolation=cv2.INTER_LANCZOS4)
    cv2.imwrite(str(TRABAJO / "cara_vertical.png"), im)
    n = int(round(PARAM["segundos"] * 25))
    destino = TRABAJO / "mov_afin.mp4"
    vw = cv2.VideoWriter(str(destino), cv2.VideoWriter_fourcc(*"mp4v"), 25, (ANCHO, ALTO))
    for i in range(n):
        t = i / 25.0
        ang = 0.8 * np.sin(2 * np.pi * t / 3.1)           # grados: un balanceo lento
        esc = 1.0 + 0.01 * np.sin(2 * np.pi * t / 2.3)    # respiración
        dx = 4 * np.sin(2 * np.pi * t / 3.7)
        dy = 2 * np.sin(2 * np.pi * t / 2.9)
        M = cv2.getRotationMatrix2D((ANCHO / 2, ALTO * 0.62), ang, esc * 1.03)  # 3 % de zoom: sin bordes
        M[0, 2] += dx
        M[1, 2] += dy
        vw.write(cv2.warpAffine(im, M, (ANCHO, ALTO), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT))
    vw.release()
    sh(["ffmpeg", "-y", "-v", "error", "-i", str(destino), "-c:v", "libx264", "-crf", "16", "-pix_fmt",
        "yuv420p", str(SALIDA / "a_movimiento_afin.mp4")])
    MOVIMIENTOS["afin"] = destino

# ---------------------------------------------------------------------------
# (b) LatentSync 1.6 (26/10/2026): su propio entorno, fp16, MediaPipe en vez de InsightFace
# ---------------------------------------------------------------------------
LS = TRABAJO / "LatentSync"
LS_VENV = TRABAJO / "lsvenv"
LS_PY = LS_VENV / "bin" / "python"
LS_COMMIT = "a229c3948406bc2cf6eaf4873e662e70c6a04746"   # el que se leyó el 23/10/2026
# Lo que pide su requirements.txt, sin lo que no hace falta para generar: insightface y
# onnxruntime (sustituidos), gradio (la demo), lpips (entrenar). OpenCV sin ventanas.
LS_PAQUETES = ("diffusers==0.32.2 transformers==4.48.0 decord==0.6.0 accelerate==0.26.1 einops==0.7.0 "
               "omegaconf==2.3.0 opencv-python-headless==4.9.0.80 mediapipe==0.10.11 "
               "python_speech_features==0.6 librosa==0.10.1 scenedetect==0.6.1 ffmpeg-python==0.2.0 "
               "imageio==2.31.1 imageio-ffmpeg==0.5.1 huggingface-hub==0.30.2 numpy==1.26.4 kornia==0.8.0 "
               "DeepCache==0.1.1 soundfile")
LS_VERSIONES = (("1.6", "configs/unet/stage2_512.yaml"), ("1.5", "configs/unet/stage2.yaml"))

DETECTOR = textwrap.dedent(r'''
    """Sustituye a latentsync/utils/face_detector.py (dirección, 26/10/2026): sin
    InsightFace (sus modelos son solo para investigación no comercial). Los puntos
    salen de MediaPipe Face Mesh (Apache 2.0). image_processor.py solo usa de los
    106 puntos de InsightFace tres medias: el centro de cada ceja (43, 48-51 y
    101-105) y el centro de la nariz (74, 77, 83, 86); aquí se rellenan esas
    posiciones con lo mismo medido en la malla de MediaPipe, y la caja sale de la
    malla. Nariz: 197, 195 y 5 (puente medio), que en la cara 2 dejan la nariz a
    ~0,5 veces la distancia entre cejas por debajo de ellas, como la plantilla de
    AlignRestore (20/41). Probado en el contenedor el 26/10 con la cara 2: el
    recorte de 512 sale como los de LatentSync (cejas arriba, barbilla abajo)."""
    import mediapipe as mp
    import numpy as np

    CEJA_IMAGEN_IZQ = [70, 63, 105, 66, 107, 46, 53, 52, 65, 55]          # ceja derecha de la persona
    CEJA_IMAGEN_DER = [300, 293, 334, 296, 336, 276, 283, 282, 295, 285]  # ceja izquierda de la persona
    NARIZ = [197, 195, 5]


    class FaceDetector:
        def __init__(self, device="cuda"):
            self.malla = mp.solutions.face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1,
                                                         refine_landmarks=False, min_detection_confidence=0.5,
                                                         min_tracking_confidence=0.5)

        def __call__(self, frame, threshold=0.5):
            # LatentSync pasa los fotogramas en RGB (read_video_cv2), que es lo que pide MediaPipe.
            f_h, f_w = frame.shape[:2]
            r = self.malla.process(np.ascontiguousarray(frame))
            if not r.multi_face_landmarks:
                return None, None
            p = np.array([(l.x * f_w, l.y * f_h) for l in r.multi_face_landmarks[0].landmark])
            x1, y1 = np.maximum(p.min(0), 0)
            x2, y2 = np.minimum(p.max(0), (f_w, f_h))
            if x2 - x1 < 50 or y2 - y1 < 80:
                return None, None
            lmk = np.zeros((106, 2))
            lmk[[43, 48, 49, 50, 51]] = p[CEJA_IMAGEN_IZQ].mean(0)
            lmk[101:106] = p[CEJA_IMAGEN_DER].mean(0)
            lmk[[73, 74, 77, 83, 86]] = p[NARIZ].mean(0)
            return (int(x1), int(y1), int(x2), int(y2)), np.round(lmk).astype(np.int_)
''')


def ls_pesos(version):
    """Baja (una vez) el UNet de esa versión y el Whisper tiny que usan las dos."""
    destino = LS / "checkpoints" / version
    sh([str(LS_PY), "-c",
        "from huggingface_hub import hf_hub_download as d; "
        f"d('ByteDance/LatentSync-{version}', 'latentsync_unet.pt', local_dir='{destino}'); "
        f"d('ByteDance/LatentSync-{version}', 'whisper/tiny.pt', local_dir='checkpoints')"],
       cwd=LS, timeout=1800)
    return destino / "latentsync_unet.pt"


def latentsync(nombre, mov):
    """Labios con LatentSync sobre un vídeo de movimiento: 1.6 y, si falla, 1.5."""
    fallos = []
    for version, cfg in LS_VERSIONES:
        destino = SALIDA / f"b_latentsync_{nombre}.mp4"
        try:
            ckpt = ls_pesos(version)
            sh([str(LS_PY), "-m", "scripts.inference", "--unet_config_path", cfg,
                "--inference_ckpt_path", str(ckpt), "--inference_steps", str(PARAM["latentsync_pasos"]),
                "--guidance_scale", "1.5", "--enable_deepcache", "--seed", "1247",
                "--video_path", str(mov), "--audio_path", str(AUDIO), "--video_out_path", str(destino),
                "--temp_dir", str(TRABAJO / f"ls_tmp_{nombre}")],
               cwd=LS, timeout=2400, env=dict(os.environ, CUDA_VISIBLE_DEVICES="0"))
            if not destino.exists():
                raise RuntimeError("terminó sin dejar vídeo")
            T.setdefault("latentsync", {})[nombre] = version
            if fallos:
                T["latentsync_fallos_" + nombre] = fallos
            return version
        except Exception as ex:
            fallos.append(f"{version}: {type(ex).__name__}: {str(ex)[-600:]}")
            log(f"LatentSync {version} sobre «{nombre}» falló; se prueba la siguiente si la hay")
    raise RuntimeError(" | ".join(fallos))


with paso("b.1 · LatentSync: entorno, código y pesos"):
    if not LS.exists():
        sh(f"git clone -q https://github.com/bytedance/LatentSync.git {LS}")
    sh(f"git checkout -q {LS_COMMIT}", cwd=LS)
    (LS / "latentsync/utils/face_detector.py").write_text(DETECTOR, "utf-8")
    inferencia = LS / "scripts/inference.py"
    codigo = inferencia.read_text("utf-8")
    viejo = "torch.cuda.get_device_capability()[0] > 7"
    assert viejo in codigo, "scripts/inference.py ha cambiado: revisar el parche de fp16"
    inferencia.write_text(codigo.replace(viejo, "torch.cuda.get_device_capability()[0] >= 7"), "utf-8")
    sh(f"{sys.executable} -m pip install -q uv", timeout=600)
    if not LS_PY.exists():
        sh(f"{sys.executable} -m uv venv -q -p 3.10 {LS_VENV}", timeout=600)
    sh(f"{sys.executable} -m uv pip install -q --python {LS_PY} torch==2.5.1 torchvision==0.20.1 "
       "--index-url https://download.pytorch.org/whl/cu121", timeout=1800)
    sh(f"{sys.executable} -m uv pip install -q --python {LS_PY} {LS_PAQUETES}", timeout=1800)
    sh([str(LS_PY), "-c", "import torch, mediapipe, decord, diffusers; "
        "print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), "
        "torch.cuda.get_device_name(0) if torch.cuda.is_available() else '-')"], cwd=LS)
    ls_pesos("1.6")

with paso("b.2 · LatentSync sobre «afin»"):
    latentsync("afin", MOVIMIENTOS["afin"])

# ---------------------------------------------------------------------------
# (a.2) Wan 2.2 TI2V-5B, después de tener ya un vídeo con labios
# ---------------------------------------------------------------------------
WAN = textwrap.dedent(r'''
    """Un intento de Wan 2.2 TI2V-5B en la T4 (dirección, 26/10/2026).
    «fp16_bloques»: fp16 (atención eficiente nativa de la T4) y el transformador por bloques,
       uno cada vez en la GPU. «fp16_hojas»: igual pero capa a capa, si aún falta memoria.
       «bf16_atencion_fp32_bloques»: si fp16 se desborda; bf16 con la atención en fp32.
    Escribe los fotogramas en PNG (sin pérdida) y un informe JSON con lo que pasó."""
    import json, sys, time, traceback
    from pathlib import Path
    import numpy as np
    import torch
    import torch.nn.functional as F

    p = json.loads(sys.argv[1])
    informe = {"modo": p["modo"]}
    Path(p["informe"]).write_text(json.dumps(informe), "utf-8")
    t0 = time.time()
    try:
        # ¿Hay atención eficiente en fp16 en esta GPU? (si no, nada de lo demás cabe)
        from torch.nn.attention import SDPBackend, sdpa_kernel
        q = torch.randn(1, 24, 4096, 128, device="cuda", dtype=torch.float16)
        with sdpa_kernel([SDPBackend.EFFICIENT_ATTENTION]):
            F.scaled_dot_product_attention(q, q, q)
        informe["atencion_eficiente_fp16"] = True
        del q

        from diffusers import AutoencoderKLWan, WanImageToVideoPipeline, WanTransformer3DModel
        from diffusers.utils import load_image
        from transformers import UMT5EncoderModel

        dt = torch.bfloat16 if p["modo"].startswith("bf16") else torch.float16
        if p["modo"].startswith("bf16"):
            # bf16 en Turing: la atención eficiente no lo acepta y PyTorch caería en la
            # «matemática» (la matriz entera: lo que no cupo el 23/10). En fp32 sí la acepta.
            _sdpa = F.scaled_dot_product_attention
            def sdpa_fp32(q, k, v, *a, **kw):
                if q.dtype == torch.bfloat16:
                    return _sdpa(q.float(), k.float(), v.float(), *a, **kw).to(q.dtype)
                return _sdpa(q, k, v, *a, **kw)
            F.scaled_dot_product_attention = sdpa_fp32

        mid = "Wan-AI/Wan2.2-TI2V-5B-Diffusers"
        transformer = WanTransformer3DModel.from_pretrained(mid, subfolder="transformer", torch_dtype=dt)
        texto = UMT5EncoderModel.from_pretrained(mid, subfolder="text_encoder", torch_dtype=torch.bfloat16)
        vae = AutoencoderKLWan.from_pretrained(mid, subfolder="vae", torch_dtype=torch.float32)
        pipe = WanImageToVideoPipeline.from_pretrained(mid, transformer=transformer, text_encoder=texto,
                                                       vae=vae, torch_dtype=dt)
        # 26/10/2026, segundo intento: con el modelo entero en la GPU (enable_model_cpu_offload) el
        # transformador son 10 GB de 14,5 y las activaciones no cabían (pico 14,0; pedía 1,21 más).
        # Descarga por grupos: solo los bloques que se están usando viven en la GPU, y el siguiente se
        # trae mientras se calcula el actual (use_stream). «bloques» = bloque a bloque; «hojas» = capa
        # a capa (lo más pequeño que hay, y más lento). El VAE, en la GPU y por trozos.
        grupo = dict(onload_device=torch.device("cuda"), offload_device=torch.device("cpu"),
                     use_stream=True, low_cpu_mem_usage=True)
        # apply_group_offloading, no enable_group_offload: el codificador de texto es de
        # transformers, no de diffusers, y no tiene ese método (fallo del primer intento de las 14:06).
        from diffusers.hooks import apply_group_offloading
        if p["modo"].endswith("hojas"):
            apply_group_offloading(pipe.transformer, offload_type="leaf_level", **grupo)
        else:
            apply_group_offloading(pipe.transformer, offload_type="block_level",
                                   num_blocks_per_group=1, **grupo)
        apply_group_offloading(pipe.text_encoder, offload_type="block_level",
                               num_blocks_per_group=1, **grupo)
        pipe.vae.to("cuda")
        pipe.vae.enable_tiling()
        informe["cargado_s"] = round(time.time() - t0, 1)
        print("cargado en", informe["cargado_s"], "s; modo", p["modo"], flush=True)

        def vigila(pipe_, i, t, kw):
            # fp16 puede desbordar: si sale un NaN, se para en el acto, no al final.
            if not torch.isfinite(kw["latents"]).all():
                raise FloatingPointError(f"NaN o infinito en los latentes en el paso {i}")
            if i == 0:
                informe["primer_paso_s"] = round(time.time() - t0 - informe["cargado_s"], 1)
                print("primer paso hecho; pico de memoria",
                      round(torch.cuda.max_memory_allocated() / 2**30, 1), "GB", flush=True)
            return kw

        img = load_image(p["imagen"])
        frames = pipe(image=img,
                      prompt=("a friendly science presenter looks at the camera and stays still, calm breathing, "
                              "subtle natural head movement, blinks once, mouth closed, static camera, "
                              "plain dark navy blue background, sharp focus, high detail"),
                      negative_prompt=("talking, open mouth, camera movement, zoom, text, subtitles, distorted face, "
                                       "blurry, low quality, pixelated, deformed eyes"),
                      height=p["wan_alto"], width=p["wan_ancho"], num_frames=p["wan_fotogramas"],
                      num_inference_steps=p["wan_pasos"], guidance_scale=5.0, output_type="np",
                      generator=torch.Generator("cpu").manual_seed(20261023),
                      callback_on_step_end=vigila, callback_on_step_end_tensor_inputs=["latents"]).frames[0]
        frames = np.asarray(frames)
        if not np.isfinite(frames).all() or float(frames.std()) < 0.02:
            raise FloatingPointError(f"vídeo vacío o con NaN (desviación {float(np.nanstd(frames)):.4f})")
        import cv2
        carpeta = Path(p["fotos"])
        for i, f in enumerate(frames):
            cv2.imwrite(str(carpeta / f"{i:03d}.png"),
                        cv2.cvtColor((np.clip(f, 0, 1) * 255).round().astype(np.uint8), cv2.COLOR_RGB2BGR))
        informe.update(ok=True, fotogramas=len(frames), segundos=round(time.time() - t0, 1),
                       pico_gb=round(torch.cuda.max_memory_allocated() / 2**30, 1))
    except BaseException as ex:
        informe.update(ok=False, error=f"{type(ex).__name__}: {ex}"[:800],
                       pico_gb=round(torch.cuda.max_memory_allocated() / 2**30, 1) if torch.cuda.is_available() else None)
        traceback.print_exc()
    Path(p["informe"]).write_text(json.dumps(informe, ensure_ascii=False), "utf-8")
    print("INFORME", json.dumps(informe, ensure_ascii=False), flush=True)
    sys.exit(0 if informe.get("ok") else 1)
''')

with paso("a.2 · Wan 2.2 TI2V-5B"):
    (TRABAJO / "wan.py").write_text(WAN, "utf-8")
    # 23/10/2026: diffusers de git main subió huggingface_hub a 2.3.0 y el transformers de
    # Kaggle (5.16, pide <2.0) dejó de importar: cayeron Wan y MuseTalk. Diffusers de PyPI
    # (Wan 2.2 desde la 0.35) y huggingface_hub atado a lo que pide transformers.
    sh(f"pip install -q 'diffusers>=0.35' accelerate ftfy {HUB}", timeout=1200)
    r = subprocess.run("pip freeze | grep -i -E '^(torch|diffusers|transformers|accelerate)=='",
                       shell=True, capture_output=True, text=True)
    T["versiones"] = r.stdout.split()
    fotos, informe = TRABAJO / "wan_png", TRABAJO / "wan_informe.json"
    limite = time.time() + int(PARAM["wan_tope_s"])
    T["wan"] = []
    for modo in ("fp16_bloques", "fp16_hojas", "bf16_atencion_fp32_bloques"):
        if modo.endswith("hojas") and T.get("wan_siguiente") != "hojas":
            continue
        if modo.startswith("bf16") and T.get("wan_siguiente") not in (None, "bf16"):
            continue
        resto = int(limite - time.time())
        if resto < 600:
            T["wan"].append({"modo": modo, "ok": False, "error": "sin tiempo para intentarlo"})
            break
        shutil.rmtree(fotos, ignore_errors=True)
        fotos.mkdir()
        args = dict(PARAM, modo=modo, imagen=str(TRABAJO / "cara_vertical.png"), fotos=str(fotos),
                    informe=str(informe))
        try:
            sh([sys.executable, str(TRABAJO / "wan.py"), json.dumps(args)], timeout=resto,
               env=dict(os.environ, PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True", CUDA_VISIBLE_DEVICES="0"))
        except subprocess.TimeoutExpired:
            T["wan"].append({"modo": modo, "ok": False, "error": f"no terminó en {resto} s (tope)"})
            break
        except RuntimeError:
            pass
        T["wan"].append(json.loads(informe.read_text("utf-8")) if informe.exists() else {"modo": modo, "ok": False})
        guardar()
        if T["wan"][-1].get("ok"):
            break
        fallo = T["wan"][-1].get("error", "")
        T["wan_fallo"] = fallo[:200]
        desborda = "NaN" in fallo or "vacío" in fallo
        sin_memoria = "out of memory" in fallo.lower()
        if not (desborda or sin_memoria):
            break                               # otro error se repetiría igual en los demás modos
        # fp16_hojas solo tiene sentido si faltó memoria; bf16, solo si fp16 se desbordó.
        T["wan_siguiente"] = "hojas" if sin_memoria else "bf16"
    if not (T["wan"] and T["wan"][-1].get("ok")):
        raise RuntimeError("Wan sin vídeo: " + json.dumps(T["wan"], ensure_ascii=False)[:1500])
    # Los fotogramas de Wan se ponen a 25 por segundo tal cual (77 a 25 = 3,08 s, un 4 % más
    # rápido): convertir 24 → 25 repetiría un fotograma cada segundo y se notaría un tirón.
    destino = TRABAJO / "mov_wan.mp4"
    sh(["ffmpeg", "-y", "-v", "error", "-framerate", "25", "-i", str(fotos / "%03d.png"), "-c:v", "libx264",
        "-crf", "14", "-pix_fmt", "yuv420p", str(destino)])
    sh(["ffmpeg", "-y", "-v", "error", "-i", str(destino), "-c", "copy", str(SALIDA / "a_movimiento_wan.mp4")])
    MOVIMIENTOS["wan"] = destino

if "wan" in MOVIMIENTOS:
    with paso("b.3 · LatentSync sobre «wan»"):
        latentsync("wan", MOVIMIENTOS["wan"])

T["movimientos"] = sorted(MOVIMIENTOS)

# ---------------------------------------------------------------------------
# (b') MuseTalk 1.5, sin BiSeNet ni DWPose: solo si parametros.json trae "musetalk": true
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

def musetalk_preparar():
    if not MT.exists():
        sh(f"git clone -q https://github.com/TMElyralab/MuseTalk.git {MT}")
    sh(f"git checkout -q {MUSETALK_COMMIT}", cwd=MT)
    (MT / "musetalk/utils/preprocessing.py").write_text(PREPROCESADO, "utf-8")
    fp = MT / "musetalk/utils/face_parsing"
    for f in fp.glob("*.py"):
        f.unlink()
    (fp / "__init__.py").write_text(MASCARA, "utf-8")
    sh("pip install -q omegaconf einops librosa soundfile "
       f"{HUB} ffmpeg-python", timeout=900)
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

def musetalk(nombre, mov):
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

if PARAM.get("musetalk"):
    with paso("c.1 · MuseTalk: código, dependencias y pesos"):
        musetalk_preparar()
    for nombre, mov in list(MOVIMIENTOS.items()):
        with paso(f"c.2 · MuseTalk sobre «{nombre}»"):
            musetalk(nombre, mov)

# ---------------------------------------------------------------------------
# (c) Resumen
# ---------------------------------------------------------------------------
T["salida"] = sorted(p.name for p in SALIDA.iterdir())
CON_LABIOS = sorted(p.stem[2:] for p in SALIDA.glob("b_*.mp4"))   # latentsync_afin, labios_afin (MuseTalk)…
T["resultado"] = ("con labios: " + ", ".join(CON_LABIOS)) if CON_LABIOS else "sin vídeo con labios"
guardar()
log("\nRESUMEN:", json.dumps(T, ensure_ascii=False, indent=1))
