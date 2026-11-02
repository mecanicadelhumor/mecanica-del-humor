# Presentador sintético: alternativas de «imagen + audio → vídeo» (informe 2026-11-02)

Contexto: Wan 2.2 TI2V 5B en T4 + LatentSync 1.6 dio una «boca cosida que intenta gritar», y MuseTalk quedó descartado. Buscamos modelos que generen **cara y boca a la vez** (talking head / speech-to-video) a partir de una imagen y un audio, para clips de 2-3 s. Hay una regla fija: **coste cero**.

**Cómo leer este informe**
- **Fuentes.** Todas las cifras de VRAM y de tiempo vienen de **terceros** (README oficiales, papers, blogs). **No las he medido.** Las fuentes están enlazadas.
- **Licencias.** Las he comprobado en la ficha de Hugging Face (campo `license`) o en el README/LICENSE de GitHub. «No verificado» significa que no encontré el dato. No es asesoramiento legal.
- **Red.** Desde esta sesión no pude abrir algunos repos de GitHub (404 o acceso bloqueado). En esos casos lo indico.

---

## 1. Tabla de candidatos

Leyenda de la columna «¿Comercial?»:
- **Sí**: licencia permisiva (Apache-2.0/MIT) en los pesos.
- **Condicionado**: hay restricciones.
- **No**: licencia no comercial.

| Modelo (fecha) | Licencia pesos / código | ¿Comercial? | VRAM según fuentes (terceros) | ¿Cuantizado ≤16 GB? | Tiempo aprox. (terceros) | Idiomas / labios no ingleses |
|---|---|---|---|---|---|---|
| **LongCat-Video-Avatar 1.5** (Meituan, 21-may-2026) | MIT / MIT ([ficha HF](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5), [repo](https://github.com/meituan-longcat/LongCat-Video)) | Sí (MIT). La licencia no cede marcas ni patentes de Meituan | Sin cifra oficial. Pico de 46.827 MiB en H200 ([tight.studio, ago-2026](https://tight.studio/blog/open-source-talking-avatar-models/)) | INT8 oficial (`--use_int8`). GGUF comunitario Q2_K 8,3 GB … Q4_K_M 12,1 GB … Q6_K 15,5 GB ([vantagewithai](https://huggingface.co/vantagewithai/LongCat-Video-Avatar-1.5-GGUF-ComfyUI), MIT). Que quepa en una T4 con activaciones **no está verificado** | 233 s para 3,63 s de audio en H200, carga incluida (≈64 s por segundo de vídeo). En ZeroGPU, ≈121 s por generación con DBCache, duración del clip no indicada ([blog HF](https://huggingface.co/blog/victor/building-zerogpu-spaces-autonomously)). Destilado a 8 pasos | Ficha: inglés y chino. Usa Whisper-large-v3, un codificador multilingüe. **Sin evidencia en español**. tight.studio: «el más expresivo», con algunos fotogramas de boca algo exagerados |
| **Kandinsky S2V 1.0** Lite 2B / Pro 21B (13-oct-2026) | MIT según el paper ([arXiv 2610.19290](https://arxiv.org/abs/2610.19290)) | Sí, según el paper. **No pude verificar los pesos**: en la API de HF de `kandinskylab` solo aparecen pipelines «tiny» de test, y `github.com/kandinskylab/kandinsky-s2v` me devolvió 404 | No publicada | No verificado | En H100, por bloque de 5 s a 512×768: Lite destilado 43 s, Pro destilado 173 s, Pro base 914 s (paper) | Datos de entrenamiento: 53,9 % inglés, 25,8 % ruso, **1,7 % español**. En el paper es el n.º 1 en EMTD, CelebV-HQ y HDTF, con LongCat 1.5 en segundo lugar |
| **EchoMimic V3 / V3-Flash** (Ant Group, ago-2025 / 22-ene-2026) | Apache-2.0 / Apache-2.0 ([ficha HF](https://huggingface.co/BadToBest/EchoMimicV3), [repo](https://github.com/antgroup/echomimic_v3)) | Sí | Mínimo de 12 GB según el README (Gradio y Flash). ComfyUI con 16 GB. **Probado en V100 16 GB**, una GPU que tampoco tiene bf16, como la T4 | Hay versión «cuantizada» oficial (Gradio) y repos comunitarios: NF4 ([siyah1](https://huggingface.co/siyah1/EchoMimicV3-NF4)) y [flash-transformer-quant](https://huggingface.co/lieding1994/echomimicv3-flash-transformer-quant). Es un modelo de 1,3B, así que debería caber en 16 GB | 252 s para 3,63 s en L40S, carga incluida (tight.studio). Flash: 8 pasos | El README solo muestra demos con audio en chino. V3-Flash usa chinese-wav2vec2. Sin evidencia en español. tight.studio: «identidad limpia y movimiento labial», la mejor relación calidad/coste |
| **InfiniteTalk** (MeiGen, 19-ago-2025) | Apache-2.0 / Apache-2.0 ([ficha HF](https://huggingface.co/MeiGen-AI/InfiniteTalk), [repo](https://github.com/MeiGen-AI/InfiniteTalk)). Se apoya en Wan2.1-I2V-14B, también Apache-2.0 | Sí | Sin cifra oficial. Tiene modo `--num_persistent_param_in_dit 0` y `--quant fp8` | Sí. GGUF de Kijai: InfiniteTalk Single Q4_K_M/Q6_K/Q8 ([WanVideo_comfy_GGUF](https://huggingface.co/Kijai/WanVideo_comfy_GGUF)) más Wan2.1-I2V-14B-480P GGUF Q4_K_M de 11,3 GB ([city96](https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf)). Admite LoRA lightx2v de 4 pasos | Sin cifras publicadas | Codificador chinese-wav2vec2-base. En español solo hay marketing de proveedores (WaveSpeed), nada independiente. En el paper de Kandinsky queda por debajo de Wan-S2V en EMTD |
| **MultiTalk** (MeiGen, jun-2025) | Apache-2.0 / Apache-2.0 ([repo](https://github.com/MeiGen-AI/MultiTalk)) | Sí | 480p en una RTX 4090 (24 GB) en modo low-VRAM. Wan2GP lo anuncia con 8 GB | INT8 oficial. GGUF Multi de Kijai | TeaCache da 2-3×. Sin cifras absolutas | chinese-wav2vec2. InfiniteTalk lo supera según sus autores. Penúltimo en el ranking del paper de Kandinsky |
| **Wan 2.2 S2V 14B** (Alibaba, 26-ago-2025) | Apache-2.0 / Apache-2.0 ([ficha HF](https://huggingface.co/Wan-AI/Wan2.2-S2V-14B)) | Sí | **80 GB** en una sola GPU con offload (ficha oficial). 58.681 MiB pico en H200 (tight.studio) | GGUF Q2_K 9,5 GB … Q4_K_M 13,9 GB … Q5_K_M 15 GB ([QuantStack](https://huggingface.co/QuantStack/Wan2.2-S2V-14B-GGUF)). FP8 en DiffSynth. «Corre en 16 GB en FP8» es solo un comentario de Reddit, **no verificado** | **780 s para 3,8 s** en H200 (≈205 s por segundo de vídeo): el más lento de la prueba de tight.studio. 16 fps | Codificador wav2vec2 «english». Sin evidencia en español. tight.studio: «movimiento conservador, menos fluido» |
| **LiveAvatar** (Alibaba-Quark, 2025-26) | Apache-2.0 ([ficha HF](https://huggingface.co/Quark-Vision/Live-Avatar)). Es un LoRA sobre Wan2.2-S2V-14B | Sí | 80 GB en una sola GPU, o 48 GB con FP8, según el README citado por buscadores (no pude abrir el repo) | No a 16 GB | 181 s para 3,63 s en H200 (tight.studio) | tight.studio lo considera la mejor calidad «pesada»: bocas convincentes y parpadeo. Sin datos de idiomas |
| **SoulX-FlashTalk 14B / FlashHead 1.3B** (Soul AI Lab, 2026) | FlashTalk: Apache-2.0. FlashHead: «other», con DiT Apache-2.0 y, en la variante Lite, VAE LTX bajo **Open-RAIL-M** ([ficha](https://huggingface.co/Soul-AILab/SoulX-FlashHead-1_3B)) | FlashTalk: sí. FlashHead Lite: sí, con las restricciones de uso de Open-RAIL-M | FlashTalk: 57,8 GB en H200. FlashHead Lite: 5,8 GB en L40S (tight.studio) | FlashHead sí cabe | FlashHead Lite: 96 fps en RTX 4090 (ficha) | tight.studio: FlashHead Lite es «el menos convincente». FlashTalk: «cara estable, boca clara» |
| **HunyuanVideo-Avatar** (Tencent, 28-may-2025) | **Tencent Hunyuan Community License** ([LICENSE](https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar/blob/main/LICENSE)) | **Condicionado: la licencia NO se aplica en la UE, el Reino Unido ni Corea del Sur.** Fuera de ese territorio es comercial salvo que se superen 100 M de MAU. **Si el canal opera desde España, no hay licencia** | 24 GB mínimo («muy lento») y 96 GB recomendado (README). 10 GB con Wan2GP | FP8 oficial. GGUF experimental ([lym00](https://huggingface.co/lym00/HunyuanVideo-Avatar-GGUF-Experiment)) | Sin cifras | Sin datos |
| **OmniAvatar** (jun/jul-2025) | Apache-2.0 / Apache-2.0 ([ficha HF](https://huggingface.co/OmniAvatar/OmniAvatar-14B), [repo](https://github.com/Omni-Avatar/OmniAvatar)) | Sí | 14B en A800: 36 GB a 16,0 s/it, 21 GB a 19,4 s/it, **8 GB a 22,1 s/it** (con offload). Hay versión de 1,3B | No hay cuantización oficial. El modo 8 GB descarga a CPU | Solo s/it, sin número de pasos ni tiempo total | wav2vec2-base-960h, entrenado en inglés. Sin evidencia de otros idiomas. Puesto bajo en el ranking del paper de Kandinsky |
| **FantasyTalking** (AMAP, 2025) | Apache-2.0 / Apache-2.0 ([ficha HF](https://huggingface.co/acvlab/FantasyTalking), [repo](https://github.com/Fantasy-AMAP/fantasy-talking)). Sobre Wan2.1-I2V-14B-720P | Sí | A100, 512×512, 81 fotogramas: 40 GB a 15,5 s/it, 20 GB a 32,8 s/it, **5 GB a 42,6 s/it** | No hay cuantización oficial | Solo s/it | wav2vec2-base-960h, inglés. Sin evidencia en español |
| **Hallo3** (Fudan, 2025) | Ficha HF: MIT. Código: MIT. Pero es **derivado de CogVideoX-5B**, cuya licencia exige **registro para uso comercial** y fija un tope de 1 M de visitas al mes ([LICENSE CogVideoX](https://huggingface.co/THUDM/CogVideoX-5b-I2V/blob/main/LICENSE)) | Condicionado (registro gratuito) | No publicada. Solo probado en H100 | No | Sin cifras | **El README dice que el audio debe estar en inglés.** Descartable para español |
| **Sonic** (Tencent, 2025) | **CC BY-NC-SA 4.0** ([repo](https://github.com/jixiaozhong/Sonic)) | **No** («our license is non-commercial») | Probado en una GPU de 32 GB | No | Sin cifras | Sin datos. **Descartado por licencia** |
| **EchoMimic V2** (Ant Group, nov-2024) | Código: Apache-2.0. Pesos: **sin licencia en la ficha**, con aviso de «academic research» ([ficha](https://huggingface.co/BadToBest/EchoMimicV2)) | No verificado. Mejor evitarlo | Probado en V100 16 GB | No | ≈50 s por 120 fotogramas en A100 con la versión acelerada | Inglés y mandarín. Además depende de una pose de referencia |
| **LivePortrait + audio** (JoyVASA, Ditto) | LivePortrait: MIT, pero **los modelos de InsightFace que usa son no comerciales**; para uso comercial hay que sustituir el detector ([LICENSE](https://github.com/KwaiVGI/LivePortrait/blob/main/LICENSE)). JoyVASA: MIT ([repo](https://github.com/jdh-algo/JoyVASA)). Ditto: Apache-2.0 ([repo](https://github.com/antgroup/ditto-talkinghead)) | Condicionado (InsightFace) | JoyVASA: probado en una RTX 4060 de 8 GB. Ditto: TensorRT en GPU Ampere o superior (la T4 es Turing, así que habría que convertir el ONNX) | Ya cabe | Ditto se anuncia como tiempo real. Sin cifras | JoyVASA: datos chinos e ingleses, con codificador hubert-chinese. Estética 2D/warping: no inventa dientes ni interior de boca como los modelos de difusión |
| **Kandinsky 5.0 / 6.0** | MIT en las fichas | — | — | — | — | **No son speech-to-video.** Son T2V/I2V. El S2V es el modelo de la fila de arriba |

**Lo que no pude verificar**
- La licencia del repo GitHub de LiveAvatar y la de SoulX-FlashTalk: me baso en sus fichas de HF y en resúmenes de buscadores.
- Si los pesos de Kandinsky S2V están realmente publicados hoy.
- Si alguna cuantización de modelos de 14B consigue generar 3 s en una T4 en un tiempo razonable.

**Lo que no existe en las fuentes**
- Ninguna fuente aporta una **medición independiente de la sincronía labial en español** para ninguno de estos modelos.
- Un paper de 2025 ([arXiv 2510.06612](https://arxiv.org/html/2510.06612v1)) advierte que los modelos de talking face rinden peor fuera del inglés.

### Nota técnica sobre la T4
Todos los modelos basados en Wan (14B) están pensados para **bf16**, y la T4 (arquitectura Turing) no lo soporta de forma nativa. Habría que usar fp16, con riesgo de desbordamiento, o emulación lenta. Parte del mal resultado anterior podría deberse a esto. **Es una hipótesis, no está medido.** Por eso conviene probar en una GPU Ampere o más reciente (L4, L40S, A100, H100, Blackwell), y **EchoMimic V3**, probado oficialmente en V100 (sin bf16), es el candidato natural si hay que quedarse en la T4.

---

## 2. GPUs gratuitas (noviembre de 2026) con más memoria que una T4

| Plataforma | Qué dan gratis | GPU / VRAM | ¿Automatizable desde GitHub Actions? | Uso comercial / condiciones |
|---|---|---|---|---|
| **Hugging Face ZeroGPU** ([docs](https://huggingface.co/docs/hub/spaces-zerogpu)) | **5 min de GPU al día** con cuenta gratuita (2 min sin login). Una cuenta gratuita con más de 30 días y email verificado puede **alojar hasta 2 Spaces ZeroGPU** propios | Media RTX Pro 6000 Blackwell (**48 GB**, por defecto) o entera (96 GB, cuesta el doble de cuota). Soporta bf16 | **Sí, en la práctica**: se llama al Space con `gradio_client` y un token HF guardado en los Secrets de Actions. La cuota se descuenta al usuario del token. Solo funciona con el SDK de Gradio. Duración por llamada: 60 s por defecto, ampliable con `duration=`. No encontré el máximo permitido a cuentas gratuitas | Los docs no prohíben el uso comercial. Mirar los ToS de HF. Ya hay Spaces comunitarios de LongCat-Video-Avatar 1.5 y de InfiniteTalk |
| **Lightning AI** ([precios](https://lightning.ai/pricing)) | **Hasta 30 créditos de una sola vez** (5 al registrarse y 25 al **añadir tarjeta**). Caducan a los 12 meses. Según la página equivalen a unas 5 h de L40S, 10 h de A100 40 GB o 31 h de L4 | L4 24 GB, **L40S 48 GB**, A100/H100/H200 (sesiones de 4 h como máximo) | Sí, tienen SDK/CLI (no lo he probado). Teléfono obligatorio | No vi restricciones comerciales en la página de precios. **No verificado** en los ToS. La tarjeta solo hace falta para los 25 créditos extra |
| **Modal** ([precios](https://modal.com/pricing)) | **30 $ al mes** en el plan Starter. L40S a 0,000542 $/s ≈ 15 h/mes; H100 ≈ 7,6 h/mes (cálculo propio con sus tarifas) | L4, A10, L40S, A100 40/80, H100, H200 | **Sí, es su caso de uso típico** (`modal run` desde CI con un token) | Según sus docs, **hace falta un método de pago registrado** ([billing](https://modal.com/docs/guide/billing)). Riesgo de cobro si se supera el crédito; no verifiqué si se puede fijar un tope de gasto. tight.studio hizo allí su comparativa |
| **Kaggle** | Unas 30 h semanales de GPU (cifra habitual que no aparece en la documentación oficial), sesiones de 12 h | **Solo T4 ×2** (2 × 16 GB, **no se suman**). La P100 se retiró el 15-sep-2026 ([anuncio](https://www.kaggle.com/discussions/product-announcements/735239)). La CLI menciona A100/L4/H100/RTX Pro 6000, pero **solo para competiciones concretas o administradores** | Sí (`kaggle kernels push` desde Actions). Es lo que ya usáis | No verificado. Algunos modelos (InfiniteTalk con torchrun/FSDP) pueden repartirse entre las 2 T4, pero seguiría sin haber bf16 |
| **Google Colab gratuito** ([FAQ](https://research.google.com/colaboratory/faq.html)) | Sin cuota publicada. Normalmente T4 | T4 16 GB: **no mejora a Kaggle** | **No.** La FAQ prohíbe en runtimes gratuitos «bypassing the notebook UI… for content generation» y el control remoto. También prohíbe «creating deepfakes» | Descartado para automatizar |
| **Google Cloud (prueba de 300 $)** | 300 $ durante 90 días | **Las GPU están excluidas en la prueba gratuita** y no se puede pedir cuota ([resumen y foros](https://gpuperhour.com/blog/free-cloud-gpus-and-credits)) | — | Inútil para GPU sin pasar a cuenta de pago |
| AWS Free Tier / Azure free | Créditos de 200 $ | No sirven para GPU (AWS). En Azure la elegibilidad de GPU es dudosa y exige tarjeta | — | No recomendable |
| SageMaker Studio Lab | Cerrado a nuevos usuarios | — | — | — |

Resumen GPU:
- **ZeroGPU** es la única opción que es a la vez gratis, sin tarjeta, con más de 16 GB, con bf16 y automatizable.
- Su límite es la cuota de **5 min/día**. Con 1-2 clips de 3 s por Short podría bastar si cada generación dura unos 2 min, que es la cifra publicada para LongCat en ZeroGPU **sin conocer la duración del clip**.
- **Lightning AI** (bolsa única de créditos) sirve bien **para la prueba comparativa**, no para producción continua.

---

## 3. Recomendación

**Probar primero:**

1. **LongCat-Video-Avatar 1.5** (MIT) en **Hugging Face ZeroGPU**.
   - Es la mejor posicionada entre los pesos que he podido confirmar como publicados: segunda en el ranking del paper de Kandinsky, por detrás solo de Kandinsky S2V Pro, y «la más expresiva» en tight.studio.
   - Está destilada a 8 pasos, tiene INT8 y GGUF, y usa Whisper-large-v3, un codificador multilingüe. Eso hace plausible un mejor resultado en español, **pero no está demostrado**.
   - Ya existe un Space ZeroGPU comunitario. Lo ideal es **duplicarlo** en vuestra cuenta (los 2 Spaces gratuitos) para controlar versión y parámetros.

2. **EchoMimic V3-Flash** (Apache-2.0, 1,3B) en la **T4 de Kaggle** que ya usáis.
   - Es el único candidato serio con requisito oficial de 12 GB y probado en una GPU sin bf16 (V100 16 GB).
   - tight.studio lo valora como la mejor relación calidad/coste.
   - Si convence, la tubería actual (Kaggle + GitHub Actions) sirve casi tal cual.

**Recambio y vigilancia:**
- **InfiniteTalk** (Apache-2.0) con GGUF Q4 y LoRA lightx2v de 4 pasos, si los dos anteriores fallan.
- **Kandinsky S2V 1.0 Pro destilado** (MIT): el mejor del paper (oct-2026), pero hoy no he podido confirmar que sus pesos estén descargables.
- **Evitar**:
  - Sonic (no comercial).
  - HunyuanVideo-Avatar (sin licencia en la UE).
  - Hallo3 (solo inglés).
  - Wan 2.2 S2V 14B (80 GB y ≈205 s por segundo de vídeo; no aporta nada frente a LongCat).

### Plan de prueba (misma cara, misma voz, 3 s)
1. **Entradas fijas.**
   - La misma imagen de cara ficticia (de `caras/`), recortada a 512×512 o a 480×832 vertical, con la boca cerrada y en reposo.
   - El mismo WAV mono de 16 kHz y exactamente 3,0 s en español. Mejor si incluye bilabiales (p/b/m) y vocales abiertas (a/o), por ejemplo «¿Pero a mí qué me cuentas, macho?».
   - Semilla fija.
2. **Ejecuciones.**
   - LongCat 1.5 en ZeroGPU (`large`, 48 GB), 480p, 8 pasos destilados, `duration=` ajustado.
   - EchoMimic V3-Flash en Kaggle T4, 8 pasos, fp16, `partial_video_length` reducido si falta memoria.
   - Opcional: los mismos dos modelos en una L40S de Lightning AI, con los créditos gratuitos, para separar «modelo malo» de «T4 mala».
3. **Medir y anotar** en un `PRUEBA.md` nuevo:
   - Tiempo total y tiempo de GPU (ZeroGPU muestra la cuota consumida).
   - VRAM pico (`torch.cuda.max_memory_allocated`).
   - Resolución y fps de salida.
4. **Evaluación ciega.** El codirector ve los clips sin saber de qué modelo es cada uno y puntúa de 1 a 5:
   - credibilidad de la boca (cierres en p/b/m, dientes, lengua);
   - identidad respecto a la imagen;
   - artefactos.
   Hay que incluir el resultado anterior (Wan 5B + LatentSync) como referencia.
5. **Criterio.** Pasa a producción el que saque ≥4 en boca, quepa en la cuota gratuita (ZeroGPU ≤5 min/día o Kaggle ≤30 h/semana) y tenga licencia Apache/MIT confirmada.

---

### Fuentes principales
- Comparativa con mediciones: [tight.studio, ago-2026](https://tight.studio/blog/open-source-talking-avatar-models/)
- [Paper Kandinsky S2V 1.0 (arXiv 2610.19290)](https://arxiv.org/html/2610.19290v1)
- [LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) · [InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) · [MultiTalk](https://github.com/MeiGen-AI/MultiTalk) · [EchoMimic V3](https://github.com/antgroup/echomimic_v3) · [Wan2.2-S2V](https://huggingface.co/Wan-AI/Wan2.2-S2V-14B) · [OmniAvatar](https://github.com/Omni-Avatar/OmniAvatar) · [FantasyTalking](https://github.com/Fantasy-AMAP/fantasy-talking) · [Hallo3](https://github.com/fudan-generative-vision/hallo3) · [Sonic](https://github.com/jixiaozhong/Sonic) · [HunyuanVideo-Avatar](https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar) · [LivePortrait](https://github.com/KwaiVGI/LivePortrait)
- [HF ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu) · [Lightning AI](https://lightning.ai/pricing) · [Modal](https://modal.com/pricing) · [Colab FAQ](https://research.google.com/colaboratory/faq.html) · [GPUPerHour, sep-2026](https://gpuperhour.com/blog/free-cloud-gpus-and-credits)
