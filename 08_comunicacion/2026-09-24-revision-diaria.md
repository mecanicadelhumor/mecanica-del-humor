# Revisión diaria → la dirección / el codirector, 24/09/2026

Nota corta; el detalle completo está en `05_calendario/bitacora/2026-09-24-revision.md`.

## Lo importante: C50 estaba roto desde el primer día, y ya está corregido — falta el `push`

**MDS-024 (hoy) salió sin vídeo de archivo detrás. `MDS-025` (mañana) le iba a pasar
lo mismo si nadie lo tocaba.** No es un fallo de guion ni de las claves de Pexels o
Pixabay (`diagnostico.json` las da por buenas): es un `AttributeError` en
`caras()` (`03_produccion/pipeline/visual.py`) — en el runner de «Visuales (C50)»,
`cv2` se importa pero **no trae `CascadeClassifier`** («module 'cv2' has no
attribute 'CascadeClassifier'»). Antes de hoy esa función solo tenía cubierto el caso
de que `cv2` no estuviera instalado (`ImportError`); este es distinto y no estaba
cubierto.

Efecto en cascada, visto en los dos manifiestos de ayer (`MDS-024.json` y
`MDS-025.json`, `resuelto_utc` 23/09 11:5x UTC): **todos y cada uno de los candidatos
de Pexels y Pixabay fallaban en `mirar()`** con ese mismo error (143 y 127
descartes, uno por candidato), y el respaldo de imagen generada fallaba igual (llama
a la misma `caras()`). Sin un solo candidato que pasar por movimiento o relevancia,
cada plano caía en `sin_imagen` → tarjeta de marca — 11 de 12 planos en `MDS-024`, 10
de 11 en `MDS-025` (la hoja de contactos de `MDS-025` lo enseña: «10 sin_imagen» en
la cabecera). Con todos los planos vacíos, `fondo_visual.hay_archivo(plan)` da falso
y `render_archivo()` lanza `FalloArchivo("ningún plano de archivo utilizable")` — que
es exactamente lo que dice `render.py` que pasa (línea 167) y por lo que `ficha.json`
de `MDS-024` trae `"visual": null` a pesar de tener manifiesto en
`05_calendario/visuales/`. El Short salió con el fondo de siempre: seguro (nunca ha
costado un vídeo), pero sin la novedad que se quería estrenar hoy.

**No he podido leer el paso «Renderizar vídeo mudo» de `producir.yml` para copiar la
línea exacta que empieza por `C50 ·`** (sin red a la API de Actions desde aquí), pero
el manifiesto y `render.py` explican el mecanismo completo sin ambigüedad, así que lo
doy por diagnosticado.

**Corregido en `03_produccion/pipeline/visual.py` (mío, dentro de `03_produccion/`):**
`caras()` ahora atrapa cualquier fallo al montar los detectores o al detectar (no
solo `ImportError`) y sigue sin caras el resto de la pasada — «una imagen nunca
cuesta un vídeo» vale también aquí, no solo en `render_archivo`. Probado con un `cv2`
simulado que falla exactamente igual que en el runner (sin `CascadeClassifier`):
`caras()` ya no lanza, devuelve `[]`, y no vuelve a intentar el detector roto en el
resto de la pasada. **Y subida `VERSION` de 1 a 2** (`# subirla obliga a volver a
resolver todo lo pendiente`, ya estaba pensado para esto) para que los manifiestos ya
resueltos con el código roto —`MDS-024` y `MDS-025`— se rehagan enteros en cuanto
corra «Visuales (C50)», no solo los que cambien de guion.

**Es urgente aplicarlo hoy, antes de la madrugada.** `03_produccion/pipeline/visual.py`
es una de las rutas que dispara «Visuales (C50)» al hacer `push`
(`.github/workflows/visuales.yml`, `on.push.paths`), así que en cuanto se aplique el
paquete y se suba, el propio `push` vuelve a resolver `MDS-025` con el código
arreglado — y `MDS-025` se produce esta madrugada (el paso «Traer el material visual»
de `producir.yml` necesita el manifiesto nuevo antes de esa hora). Si el `push` llega
tarde, `MDS-025` sale otra vez sin imagen, seguro pero sin la novedad, igual que hoy.
No puedo comprobar desde aquí si el `cv2` roto es solo de hoy o va a repetirse
(entorno del runner, no algo que yo controle: no toco `.github/workflows/`), así que
convendría mirar mañana si `MDS-025` sí trajo vídeo de archivo (`ficha.json.visual`
no `null`) para saber si con esto basta o si además hay que mirar la instalación de
`opencv-python-headless` en `visuales.yml`.

## Lo otro: `MDS-025` no pasa del todo la lectura en frío (C48)

Detalle y propuesta de arreglo en `05_calendario/revisiones/MDS-025.md`. No lo toco
—es de los tres guiones de la dirección del 23/09—, solo lo dejo dicho: el lector no
supo a qué se refería «mejoraron casi la mitad» en la escena de cierre (¿la mitad de
qué?). El resto de la lectura, incluida la pregunta y respuesta, coincide con la
`historia` del guion.

## Y de paso

`MDS-023` (de ayer) sigue `private` con `publicar_en` correcto a estas horas: patrón
normal, se corrige por la tarde con `sincroniza_registro.yml`. No es incidencia.
