# LatentSync como tercera variante de labios (C51.3) — investigación del 23/10/2026

Lo pidió el codirector tras ver `salida/b_labios_afin.mp4` (MuseTalk): boca algo pixelada y movimiento muy
rápido. LatentSync ataca justo eso: **la 1.6 genera la boca a 512×512** (MuseTalk, a 256) y **la 1.5 añadió
capas temporales** (coherencia entre fotogramas: la boca no «tiembla»). Leído el repositorio
`bytedance/LatentSync` (commit `a229c39`, 20/06/2025) y las fichas de Hugging Face.

## Licencias (regla: solo lo que permita uso comercial)

| Pieza | Licencia | Veredicto |
|---|---|---|
| Código de LatentSync | Apache 2.0 | ✅ |
| Pesos `ByteDance/LatentSync-1.6` y `-1.5` (`latentsync_unet.pt`, 5 GB) | CreativeML **OpenRAIL++-M** | ✅ Permite uso comercial, con restricciones de uso (nada de engañar ni suplantar). Encaja con la regla 7.1: persona ficticia y declarada como sintética |
| VAE `stabilityai/sd-vae-ft-mse` | MIT | ✅ |
| Whisper `tiny.pt` (audio) | MIT | ✅ |
| **Detector de caras InsightFace** (`FaceAnalysis`, detección + 106 puntos) | Código MIT, **modelos solo para investigación no comercial** | ❌ **Hay que sustituirlo**, como hicimos con DWPose y BiSeNet en MuseTalk |
| `auxiliary/` (i3d, koniq, vgg16, syncnet…) | — | No hacen falta: solo sirven para evaluar el entrenamiento |

**La sustitución**: `latentsync/utils/face_detector.py` solo usa de InsightFace la caja y unos pocos de sus
106 puntos (centro de cada ceja, centro de la nariz y el contorno de la mandíbula, para recortar y alinear).
Se puede sacar lo mismo de **MediaPipe Face Mesh** (Apache 2.0, ya está en sus dependencias) con una tabla
de correspondencia de puntos. Con una sola foto que se mueve poco, el recorte es estable.

## Memoria y la GPU de Kaggle (T4, 15 GB)

- Ellos dan como mínimo para inferencia: **18 GB con la 1.6** y **8 GB con la 1.5**.
- **Ojo**: `scripts/inference.py` usa fp16 solo si la GPU es de capacidad > 7; **la T4 es 7.5, así que
  correría en fp32** (el doble de memoria y más lento). La T4 hace fp16 sin problema: hay que forzarlo.
  En fp16, la 1.6 tiene opciones de caber; si no, la 1.5 (a 256, pero con la boca coherente entre
  fotogramas) cabe de sobra.
- Plan: **1.6 en fp16; si no cabe, 1.5**, igual que Wan con sus tamaños. DeepCache activado (lo trae).

## Dependencias

Pide versiones viejas (`torch 2.5.1`, `diffusers 0.32.2`, `transformers 4.48`, `huggingface-hub 0.30.2`)
que chocan con las de Kaggle (torch 2.11, transformers 5.16): es el problema que ya nos rompió Wan y MuseTalk
hoy. Por eso irá **en un entorno virtual propio** dentro del cuaderno de Kaggle, sin tocar el del sistema.
Descarga: unos 2,5 GB de torch y 5 GB de pesos. Tiempo estimado: 10-20 minutos más por ejecución.

## Lo que se hará (dirección, lunes 26)

1. Paso `b.3 · LatentSync` en `kaggle/presentador.py`, en su entorno virtual, sobre los mismos movimientos
   (vaivén y, si sale, Wan) y la misma voz: deja `b_latentsync_afin.mp4` (y `_wan`).
2. Detector de MediaPipe en lugar de InsightFace; fp16 forzado; 1.6 y, si no cabe, 1.5.
3. Probado en el contenedor todo lo que no necesita GPU (el detector sustituto sobre la cara 2, el recorte,
   la instalación del entorno). El codirector lanza `kaggle` con cara 2 y compara MuseTalk y LatentSync.

## Hecho el 26/10/2026 (dirección en diferido)

Montado en `kaggle/presentador.py` (pasos `b.1`-`b.3`) tal como estaba previsto, con dos ajustes:

- El entorno propio se hace con **uv** y **Python 3.10** (Kaggle trae 3.13, y `numpy 1.26`, `decord` y
  `mediapipe 0.10.11` no tienen ruedas para 3.13). Se instala lo de su `requirements.txt` menos
  `insightface`, `onnxruntime-gpu` (sustituidos), `gradio` (la demo) y `lpips` (entrenar).
- **El detector**: de los 106 puntos de InsightFace, `image_processor.py` solo usa tres medias (centro de
  cada ceja y de la nariz). Salen de MediaPipe Face Mesh: cejas `70, 63, 105, 66, 107, 46, 53, 52, 65, 55`
  y `300, 293, 334, 296, 336, 276, 283, 282, 295, 285`; nariz `197, 195, 5`, que en la cara 2 la dejan a ~0,5
  veces la distancia entre cejas por debajo de ellas, como la plantilla de `AlignRestore` (20/41).
- fp16 forzado con un parche de una línea en `scripts/inference.py` (`> 7` → `>= 7`); si cambia el código
  de arriba, el cuaderno se para y lo dice.
- 1.6 (`stage2_512.yaml`); si falla por lo que sea, 1.5 (`stage2.yaml`, boca a 256). 20 pasos, guía 1,5,
  DeepCache, semilla 1247 (los de su `inference.sh`).

Probado en CPU de punta a punta con la 1.5 (ver `PRUEBA.md`, 26/10).
