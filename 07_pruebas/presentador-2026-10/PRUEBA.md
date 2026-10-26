# La prueba de la persona sintética (C51.3) — lista para lanzar

**Dirección, 23/10/2026.** Esta prueba estaba en el plan para el 13-15/10 (versión 18, C51.3) y
**se cayó sin que nadie lo dijera**, igual que los muestrarios del presentador del 16/10. Hoy se deja
hecha y lista para lanzar. Lo que no podía hacer yo es ejecutarla: las claves de Kaggle y Cloudflare
solo existen como secretos de GitHub, y los workflows los copia el codirector a mano (regla 11.7).
Las licencias de cada pieza, y por qué se eligieron, están en `LICENCIAS.md`. Las condiciones que tiene
que cumplir la cara, en la regla 7.1 de `REGLAS.md`.

---

## Qué hay en esta carpeta

| Fichero | Qué hace |
|---|---|
| `caras.py` | Ocho retratos de personas **ficticias** con FLUX.1 [schnell] en Cloudflare Workers AI (el mismo servicio y las mismas claves que la imagen de los Shorts, C50). Cuatro mujeres y cuatro hombres, de 28 a 55 años, con fondo azul marino liso, mirando a cámara. Las semillas son fijas: la misma cara se puede volver a generar igual. Deja `caras/cara_1.jpg` … `cara_8.jpg`, `caras/caras.json` (modelo, prompt, semilla y licencia de cada una) y **`caras/hoja.jpg`**, que es la que miras tú |
| `kaggle/presentador.py` + `kaggle/kernel-metadata.json` | El cuaderno de Kaggle: privado, con GPU y con internet. Con la cara elegida y 3 s de voz: **(a)** la cabeza en reposo y **(b)** los labios encima. Guarda los vídeos y lo que tardó cada paso |
| `prueba_presentador.py` | Lo que ejecuta el workflow. `caras` → `caras.py`; `kaggle --cara N` → sube la entrada a Kaggle como dataset privado, lanza el cuaderno, espera y baja el resultado a `salida/` |
| `00_estrategia/tareas/workflows_2026-10-23/presentador_prueba.yml` | El workflow, para que lo copies (abajo) |

### Lo que hace el cuaderno de Kaggle, paso a paso

1. **La voz** son 3 s de `07_pruebas/c36-2026-10-22/c36.mp3`, la voz de `MDS-045` que ya oíste el 22/10.
   Es una sola voz (regla 7.1.2) y no gasta **ninguna** petición a Gemini.
2. **(a) La cabeza en reposo**, de dos formas, para poder compararlas:
   - **Wan 2.2 TI2V-5B** (Apache 2.0), unos 3 s a 480p. **Puede no caber**: el modelo está pensado
     para tarjetas de 24 GB y la GPU gratuita de Kaggle es una T4 de 16 GB (o una P100), sin el formato
     numérico que usa el modelo. Va con la CPU ayudando y con un tope de 60 minutos. Si no termina, se
     apunta por qué y la prueba sigue.
   - **Plan B, siempre**: un vaivén muy suave de la foto (gira menos de un grado, respira un 1 % y se
     mueve 4 píxeles). No usa ningún modelo. Es la versión barata, y sirve para ver si Wan aporta algo.
3. **(b) Los labios**: MuseTalk 1.5 (MIT) encima de cada vídeo de (a). Lleva **dos cambios** respecto al
   original, por licencia:
   - **La máscara de la boca no usa BiSeNet** (`79999_iter.pth`), porque está entrenada con fotos de uso
     no comercial (LICENCIAS.md §3). Se cambia por una **elipse fija** sobre la mitad de abajo de la
     cara. Probada en el contenedor con una cara de ejemplo: cubre de mejilla a mejilla y de la nariz al
     mentón.
   - **La caja de la cara no usa DWPose ni mmpose.** Su dependencia (mmcv 2.0.1) pide una versión de
     torch que Kaggle ya no tiene. En su lugar va el detector S3FD que MuseTalk ya trae dentro
     (BSD-3), que es lo mismo que el original usa cuando DWPose falla. También probado en el contenedor.
4. **La salida**, en `salida/`: `cara.jpg`, `a_movimiento_afin.mp4`, `a_movimiento_wan.mp4` (si Wan
   cupo), **`b_labios_afin.mp4`** y **`b_labios_wan.mp4`** (los que tienes que ver), `tiempos.json`
   (cada paso, la GPU que tocó y las versiones) y `registro.txt`.

---

## Lo que tienes que hacer tú (una vez, unos 10 minutos más la espera)

### 1 · Copiar el workflow (2 minutos)

1. En GitHub, en el repositorio `mecanica-del-humor`, abre
   `00_estrategia/tareas/workflows_2026-10-23/presentador_prueba.yml` y copia todo su contenido.
2. Ve a **Add file → Create new file** y escribe como nombre exactamente
   **`.github/workflows/presentador_prueba.yml`**. Pega el contenido y pulsa **Commit changes** en `main`.
3. No hace falta ningún secreto nuevo. Usa `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`,
   `KAGGLE_USERNAME` y `KAGGLE_KEY`, que ya pusiste en septiembre.

### 2 · Las caras (2 minutos de máquina)

1. **Actions → «Prueba del presentador (C51.3)» → Run workflow**, con **paso = `caras`** (la cara no
   importa en este paso). Pulsa **Run workflow**.
2. Cuando termine (en verde), abre en el repositorio **`07_pruebas/presentador-2026-10/caras/hoja.jpg`**.
   Son ocho caras numeradas del 1 al 8.
3. Elige una, o ninguna. Antes de elegir, mira tres cosas (regla 7.1):
   - **que no se parezca a nadie conocido**. Si te recuerda a alguien, descártala;
   - que sea adulta y neutra: un presentador, no un anuncio;
   - que se le vea bien la cara a tamaño de móvil.

   Si no te vale ninguna, escríbelo en el cuaderno. Cambio el prompt y se vuelven a generar.

### 3 · La prueba en Kaggle (de 30 minutos a 2 horas y media de máquina; tú no haces nada mientras)

1. **Actions → «Prueba del presentador (C51.3)» → Run workflow**, con **paso = `kaggle`** y **cara =**
   el número que hayas elegido. Pulsa **Run workflow**.
2. Cuando termine, mira **`07_pruebas/presentador-2026-10/salida/b_labios_afin.mp4`** y, si existe,
   **`b_labios_wan.mp4`**. También están en el artefacto de la ejecución.
3. **Contesta en el cuaderno, en una línea**: ¿esto podría salir dos o tres segundos en un Short?
   Sí / no / sí, pero con la versión de Wan o con la del vaivén. Puede que la respuesta sea «no»: con
   piezas gratuitas, lo razonable es esperar algo peor que lo que hacen los servicios de pago
   (LICENCIAS.md §5). **Ese «no» también es un resultado**, y cierra C51.3 con datos.

**Si algo sale en rojo**, no hace falta que lo arregles tú: lo leo en la siguiente dirección. Si Wan no
cabe, la prueba no sale en rojo: se queda solo la versión del vaivén y `tiempos.json` dice por qué.

---

## Las licencias, pieza a pieza (detalle en `LICENCIAS.md` §3)

| Pieza | Licencia | Comprobado |
|---|---|---|
| FLUX.1 [schnell] (las caras) | Apache 2.0 | 30/09 (ya en uso en C50) |
| Wan 2.2 TI2V-5B (el movimiento) | **Apache 2.0** | **23/10, en la ficha de Hugging Face** de `Wan-AI/Wan2.2-TI2V-5B` y de `-Diffusers` (en LICENCIAS.md estaba «a confirmar») |
| MuseTalk 1.5, código y pesos | MIT | 30/09; commit fijado `0a89dec` |
| sd-vae-ft-mse · whisper-tiny | MIT | 30/09 |
| S3FD (`face_alignment`, dentro de MuseTalk) | BSD-3 | 30/09 |
| ~~BiSeNet `79999_iter.pth`~~ | CelebAMask-HQ, no comercial | **No se baja**: la sustituye la elipse |
| ~~DWPose / mmpose~~ | Apache 2.0 | No se usa, porque no se instala en Kaggle (ver arriba) |
| ~~SyncNet de LatentSync~~ | — | No se baja (solo sirve para entrenar) |

## Lo probado y lo no probado, dicho

- **Probado en el contenedor el 23/10:**
  - la sintaxis de todo, y que el workflow y el JSON son válidos;
  - `caras.py` con Cloudflare simulado: 8 llamadas a `flux-1-schnell`; una cara que falla no tira las
    demás; la hoja sale con sus números (el simulador no sabía que `seed` ya no vale: ver abajo);
  - sin claves, `caras.py` y `prueba_presentador.py` paran con el código 2 y lo dicen;
  - la entrada de Kaggle: 3,0 s de voz mono a 16 kHz, `parametros.json` y el `dataset-metadata.json`
    del dataset privado;
  - el plan B del movimiento: 75 fotogramas a 25 fps, 512×512;
  - la caja S3FD y la elipse metidas en el código real de MuseTalk (commit `0a89dec`), sobre la cara de
    su ejemplo: caja (290, 308, 712, 827) y máscara de mejilla a mejilla, de la nariz al mentón.
- **No probado, porque hacen falta las claves o la GPU:**
  - Cloudflare de verdad;
  - la CLI de Kaggle (crear el dataset, `push`, `status`, `output`);
  - si Wan 2.2 cabe y cuánto tarda en una T4;
  - MuseTalk de punta a punta en GPU;
  - cómo se ve.

  Es la primera ejecución la que lo dice. Si falla algo de la CLI de Kaggle, el log del workflow trae
  el mensaje exacto.

## 23/10, mañana: el primer intento de «caras» falló, y el arreglo

El codirector creó el workflow y lanzó `paso = caras`. Las ocho caras volvieron con **HTTP 400** de
Cloudflare: `Additional or unevaluated properties '/seed' at '/' not allowed`. **FLUX.1 [schnell] ya no
admite semilla** en Workers AI, y el simulador de la prueba de arriba la aceptaba.

- **`caras.py` usa ahora FLUX.2 [klein] 4B** (`visual.MODELO_IA`, el mismo que hace la imagen de los
  Shorts cada día, Apache 2.0), que sí admite `seed`, por formulario multipart y a 1024×1024. Mismas
  semillas y mismo prompt: la cara elegida se puede regenerar idéntica.
- Si klein falla, prueba **schnell sin semilla**: la cara sale, pero `caras.json` lo dice con
  `"semilla": null` (no se podría regenerar igual).
- **El workflow no cambia.** Basta con volver a lanzarlo con `paso = caras`.
- Probado con Cloudflare simulado que **rechaza `seed` en schnell** como el de verdad: con klein, 8 caras
  con sus semillas (101…808) y hoja; con klein caído, 8 caras con schnell y semilla `null`; con el código
  de antes, el mismo 400 que vio el codirector.
- Lo mismo estaba roto, sin que se notara, en el **respaldo de producción** (`visual.generar`): schnell
  solo corre si klein falla, y entonces habría fallado también. Quitada la semilla ahí (trampa 63).

## 23/10, 08:41 UTC: las caras salieron, pero no llegaron al repositorio

El segundo intento de `caras` fue bien: ocho caras con FLUX.2 [klein] 4B y sus semillas (101…808), y la
hoja. **Pero el paso «Dejarlo en el repositorio» no subió nada**: hace `git add -A caras salida`, y como
`salida/` aún no existía, git rechaza la orden **entera** («pathspec 'salida' did not match any files»);
el `|| true` del workflow se tragó el error y el paso salió en verde sin commit. Las caras solo quedaron
en el artefacto. (El enlace al artefacto que imprime el log lleva `***` en lugar del dueño, porque GitHub
oculta los secretos: ese no abre. El bueno está en la página del run, abajo, «Artifacts».)

- **Las caras, en el repositorio**: copiadas del artefacto (run 39926374698) a `caras/` por la dirección.
- **El arreglo, sin tocar el workflow**: `salida/.gitignore` (con `!*.mp4`). Hace que `salida/` exista
  siempre, así que el `git add` ya no falla, y que los `.mp4` del paso `kaggle` sí se suban (el
  `.gitignore` de la raíz los excluía: el `kaggle` habría tenido el mismo problema). Probado en una copia
  del repositorio: antes, el mismo «did not match any files» y nada en el índice; después, las caras, el
  `.gitignore` y un `.mp4` de prueba.

## 23/10, 09:04 UTC: el primer «kaggle» (cara 2) acabó en dos minutos sin vídeo

Kaggle ejecutó el cuaderno, pero **sin GPU** (`torch 2.11.0+cpu`), **sin internet** («Could not resolve host:
github.com») y **sin encontrar la entrada** en `/kaggle/input/presentador-entrada` (por eso los
parámetros dicen `cara: 1`, el valor por defecto). Cada paso falló en segundos y el run salió en verde.

- **GPU e internet**: el `kernel-metadata.json` los pide (`enable_gpu`, `enable_internet`) y la CLI 2.2.5 los
  manda bien (leído su código). Kaggle **solo los da a cuentas con el teléfono verificado** y, si no, los
  ignora sin avisar. Es lo que tiene que comprobar el codirector (Settings → Phone verification).
- **La entrada**: Kaggle ya no la monta siempre en `/kaggle/input/<nombre>/`. El cuaderno la busca ahora
  en cualquier carpeta de `/kaggle/input` que tenga `cara.jpg`, y apunta en `tiempos.json` lo que ve ahí.
- **Si falta GPU o internet**, el cuaderno para al momento y dice por qué, en `tiempos.json` → `resultado`.
- **El run sale en rojo si no hay vídeo con labios**, y `estado.json` copia el resultado y los errores.
- **`salida/.gitignore` ya no se borra** al vaciar la carpeta (el commit del bot de las 09:06 se lo llevó).
- Probado en el contenedor: el cuaderno con la entrada en `/kaggle/input/datasets/u/presentador-entrada/`
  y sin GPU la encuentra, lee `cara: 2` y para con el aviso; el lanzador con la CLI simulada da 1 sin
  vídeo y 0 con vídeo, y conserva el `.gitignore` en los dos casos.

## 23/10, ~09:33 UTC: segundo «kaggle» (cara 2, teléfono ya verificado)

Ya hay **dos Tesla T4**, internet y la entrada (en `/kaggle/input/datasets/<usuario>/presentador-entrada/`).
Salió el **plan B del movimiento** (`a_movimiento_afin.mp4`), pero **Wan y MuseTalk fallaron por lo mismo**:
el `pip install` de diffusers **desde git main** subió `huggingface_hub` a **2.3.0**, y el `transformers`
de Kaggle (5.16.1) exige `>=1.5,<2.0`: dejó de importar, y los dos lo usan.

- **Arreglo**: diffusers **de PyPI** (`>=0.35`; la última, 0.41.0, pide `huggingface-hub>=1.32,<2.0` y trae
  Wan 2.2) y `huggingface_hub>=1.5,<2` en los dos `pip install` (constante `HUB` en `kaggle/presentador.py`).
- Comprobado en PyPI: diffusers 0.41.0 pide `huggingface-hub<2.0,>=1.32.0`; transformers 5.16.1 pide
  `huggingface-hub<2.0,>=1.5.0`. Lo que no se puede probar aquí (sin GPU): que Wan quepa en una T4 y que
  MuseTalk 1.5 funcione con transformers 5; se verá en el tercer intento.

## 23/10, ~09:52 UTC: tercer «kaggle» (cara 2): primer vídeo con labios

**MuseTalk funciona**: `b_labios_afin.mp4` (512×512, 25 fps, 3 s, con la voz de `MDS-045`). Lo que vio el
codirector, «un poco pixelado y el movimiento muy rápido, no natural», es el límite de este montaje, no un
fallo del programa:

- **Pixelado**: MuseTalk rehace solo la boca y la barbilla, a 256×256, y la pega sobre una cara de 512: la
  zona de la boca sale más blanda que el resto. Además el vídeo es pequeño (512, ~260 kb/s).
- **Rapidez**: MuseTalk genera cada fotograma por separado, sin suavizado entre uno y otro, y la toma de
  C36 va a ~3,9 palabras/s. La boca «tiembla» de un fotograma a otro.
- **Wan falló otra vez, ahora por memoria**: a 480×480 y 73 fotogramas pidió 1,63 GB en la atención con
  1,41 libres en la T4, tras 6 minutos. Arreglo: si no cabe, prueba 384 y 320 (mismo número de
  fotogramas), con `expandable_segments`. Se verá en el cuarto intento.

## 23/10, ~10:10 UTC: cuarto «kaggle» (cara 2) — Wan no cupo ni a 320×320

Salió otra vez `b_labios_afin.mp4` (MuseTalk); **Wan, «no cabe en la GPU ni a 320×320»**, en el primer paso.

## 26/10 · dirección en diferido: por qué fallaba Wan de verdad, y el cambio de rumbo

El codirector (cuaderno del 26/10, escrito el 23): *«Volvió a fallar lo de WAN con Kaggle. Que funcione esta
vez. Y antes de bajar la calidad busquemos soluciones alternativas: si va a salir pixelado no merece la
pena. Queremos algo de verdad creíble.»* Tiene razón, y bajar a 384 y 320 era justo lo contrario.

**La causa** (no era el tamaño): la T4 es de la generación Turing, que **no tiene bf16 de verdad**.
PyTorch dice que sí (lo emula), así que el script elegía bf16; y con bf16 en Turing **la atención eficiente
en memoria no existe**, y PyTorch cae en la atención «matemática», que guarda la matriz de atención entera.
Eso es lo que no cabía. Y a 320 tampoco cabía porque el intento anterior, al fallar dentro de un `try`,
seguía reteniendo su memoria.

**Lo que cambia en `kaggle/presentador.py`:**

1. **Todo en vertical a 704×1280**, la resolución nativa de Wan 2.2 5B (el Short es 1080×1920: 1,5 veces).
   La cara (1024×1024) se recorta a 9:16 centrado, sin deformar, y la misma imagen sirve al vaivén y a Wan.
   **Ya no hay tamaños de respaldo**: si no sale a su resolución, no sale.
2. **Wan en fp16** (la T4 lo hace nativo y con atención eficiente), con el codificador de texto en bf16
   (11 GB: va solo a la GPU, uno cada vez) y el VAE en fp32 por trozos. **50 pasos** (los de su ficha) y
   **77 fotogramas** puestos a 25 por segundo tal cual (3,08 s; convertir de 24 a 25 repetiría un fotograma
   cada segundo). Los fotogramas se guardan en PNG y se codifican una vez con calidad alta (crf 14).
3. **Si fp16 desborda** (sale un NaN: se mira en cada paso y se para en el primero), segundo intento en
   **bf16 con la atención calculada en fp32**, que la T4 sí hace con el algoritmo eficiente. Más lento,
   misma calidad. Cada intento en un proceso nuevo: la memoria del que falla no se arrastra. Un informe
   (`tiempos.json` → `wan`) dice qué modo funcionó, el pico de memoria y cuánto tardó el primer paso.
4. **Labios con LatentSync 1.6 en lugar de MuseTalk** (lo que pidió el codirector tras ver MuseTalk:
   `LATENTSYNC.md`): boca a 512×512 y con coherencia entre fotogramas. MuseTalk queda apagado (se enciende
   con `"musetalk": true` en `parametros.json` si se quiere comparar).
5. **Orden nuevo**: vaivén → LatentSync sobre el vaivén → Wan → LatentSync sobre Wan. Aunque Wan se coma el
   tiempo, ya hay un vídeo bueno.
6. El registro mezcla por fin la salida de error en orden (antes las barras de progreso tapaban los
   avisos) y cada error trae sus últimas líneas.

**Probado en el contenedor (sin GPU)**: el vaivén vertical con la cara 2 (704×1280, 75 fotogramas, sin
deformar); el entorno de LatentSync con las versiones exactas en Python 3.10; el detector sustituto
(MediaPipe) sobre la cara 2: el recorte de 512 sale como los de LatentSync; y **LatentSync 1.5 de punta a
punta en CPU** (2 pasos, 1 s de voz) sobre el vaivén vertical: lee, alinea, genera, pega la boca y escribe el
vídeo con audio. **No se puede probar aquí**: Wan en la T4 (sin GPU) ni la 1.6 a 512 en la T4.

**Salida nueva** en `salida/`: `a_movimiento_afin.mp4`, `a_movimiento_wan.mp4` (si sale),
**`b_latentsync_afin.mp4`** y **`b_latentsync_wan.mp4`** (los que hay que ver).

## 26/10, 13:48-14:02 UTC: quinto «kaggle» (cara 2), lanzado por la dirección

**LatentSync 1.6 funciona y se ve mucho mejor**: `salida/b_latentsync_afin.mp4` (704×1280 vertical, 77
fotogramas a 25 fps, 3,08 s, con la voz de `MDS-045`). 4,7 minutos de GPU. Frente a MuseTalk del 23/10:
la boca y los dientes se leen, y no «tiembla» de un fotograma a otro. Lo tiene que ver el codirector.
El entorno propio (uv, Python 3.10), el detector de MediaPipe y fp16 forzado: los tres, bien a la primera.

**Wan falló otra vez, pero por lo que faltaba por ver**: la atención eficiente en fp16 **sí existe** en la
T4 (el cuaderno lo comprueba y lo apunta: `atencion_eficiente_fp16: true`), así que el diagnóstico del
bf16 era correcto. Lo que no cabe es el modelo: **el transformador en fp16 son unos 10 GB de los 14,5 de la
tarjeta**, y `enable_model_cpu_offload()` lo deja entero dentro mientras genera. Pico 14,0 GB y pedía
1,21 GB más, ya en el primer paso.

**Arreglo (sin tocar la resolución)**: **descarga por grupos**. Solo el bloque del transformador que se
está usando vive en la GPU; el siguiente se trae mientras se calcula el actual (`use_stream`), así que se
pierde poco tiempo. El codificador de texto, igual. El VAE se queda en la GPU y decodifica por trozos.
Si aún faltara memoria, segundo intento **capa a capa** («hojas»), y si fp16 se desborda, bf16 con la
atención en fp32. Cada modo solo se prueba si el fallo anterior es el suyo (sin memoria → hojas;
desbordamiento → bf16).

**14:06-14:21, sexto «kaggle»**: el cambio anterior se cayó en una línea mía: `enable_group_offload` es un
método de los modelos de *diffusers*, y el codificador de texto es de *transformers* (`UMT5EncoderModel`),
que no lo tiene. Se usa `apply_group_offloading(...)`, la función suelta, que vale para cualquier módulo de
PyTorch. **Probado en el contenedor** (sin GPU) sobre un UMT5 y un transformador de Wan en miniatura: los
dos quedan enganchados y el UMT5 sigue dando su salida. LatentSync volvió a salir bien (4,7 min).

## 26/10, 14:58-16:07 UTC: **Wan funciona** (séptimo «kaggle», 66 minutos)

Antes, dos ejecuciones (14:35 y 14:47) murieron en el paso «Dependencias» del workflow: `apt-get update`
se colgó sin escribir nada y agotó sus 10 minutos. No es del cuaderno: es el runner. Queda un workflow
arreglado en `00_estrategia/tareas/workflows_2026-10-26/` para que lo mueva el codirector; mientras tanto,
relanzar basta.

**Resultado, con la cara 2, todo a 704×1280 y 77 fotogramas (3,08 s a 25 fps):**

| Paso | Tiempo | Qué salió |
|---|---|---|
| Vaivén de la foto | 5 s | `a_movimiento_afin.mp4` |
| LatentSync 1.6 sobre el vaivén | 4,0 min | `b_latentsync_afin.mp4` |
| **Wan 2.2 TI2V-5B, `fp16_bloques`** | **54,6 min** (4,5 de carga, 2 el primer paso, 50 pasos) | `a_movimiento_wan.mp4`, **pico de memoria 13,5 GB de 14,5** |
| LatentSync 1.6 sobre Wan | 4,3 min | **`b_latentsync_wan.mp4`** |

**La memoria, resuelta**: con el transformador por bloques el pico baja de «no cabe» a 13,5 GB y no hubo
que bajar ni un píxel. Primer modo (`fp16_bloques`), a la primera; no hizo falta ni «hojas» ni bf16.

**La calidad, medida** (`comparacion-2026-10-26.jpg`: tres fotogramas de cada uno):

- **Nitidez** (varianza del laplaciano, misma escala): Wan **329** frente a 308 del vaivén. No hay nada
  pixelado; la cara aguanta a tamaño de móvil y a pantalla completa.
- **Movimiento medio entre fotogramas**: Wan **0,28** frente a **0,87** del vaivén. Es decir: **Wan se
  mueve menos**, no más. Hace lo que se le pidió («mirando a cámara, quieto, respiración tranquila») y lo
  hace de verdad —parpadeo y gesto propios, no un desplazamiento de la foto entera—, pero es tan sutil
  que al lado del vaivén cuesta notarlo.
- Tras LatentSync la nitidez baja a 190 en los dos (la boca se regenera y se vuelve a comprimir): el
  límite está ahora en LatentSync, no en el movimiento.

**Lo que esto cuesta**: 54,6 minutos de T4 por **3,08 s** de vídeo ≈ **18 minutos de GPU por segundo**. A
14 Shorts por semana con 3 s de presentador cada uno serían ~12 h de GPU a la semana (Kaggle da 30 h).
Caro pero posible, siempre fuera de la producción diaria (esto no entra en `producir.yml`).

**Lo que decido yo (dirección), y por qué**: el camino está abierto —resolución completa, sin pixelar y
con licencia limpia— pero **Wan, tal como está pedido, no aporta todavía lo que cuesta**: un movimiento más
discreto que el truco barato. Antes de meterlo, el jueves 29:

1. **Pedirle movimiento de verdad**: la indicación actual le pide quietud. Probar una que pida un gesto
   claro (un ligero asentimiento, mirar un instante a un lado y volver) y comparar con la misma semilla.
2. **Bajar a 30-35 pasos** y medir si se nota: si no, el coste cae un tercio.
3. Solo entonces, decidir con el codirector si entra como brazo de un experimento.

Nada de esto entra en un vídeo sin que él lo vea (C51.2 y regla 11.2).
