# Dirección — lunes 28/09/2026

Sesión de los lunes. Lo que manda está en la **versión 14** de `00_estrategia/PLAN_DE_CAMBIOS.md`;
aquí va lo que se miró, lo que se hizo y cómo se comprobó.

## 1. Qué traía el codirector (cuaderno del 28/09)

Poco tiempo esta semana y varios días sin `push`; `MDS-026` es el primero con vídeo de verdad y lo
deja como está; el punto de control del 27 lo tiene que hacer la dirección; estudiar la actualidad
como gancho. Y en la sesión contestó tres preguntas: que lo de hoy lo suba la dirección, que las
tareas entreguen solas con una comprobación de propiedad, y que esta vez la dirección suba los
cambios de `.github/workflows/` necesarios. Con un cuarto «sí» para el workflow nuevo «Entregas».

## 2. Lo que se encontró al leer

- **`metricas.yml` no había corrido a las 10:57 UTC**: ni el intento de las 05:19 ni el de las 08:37
  aparecían en Actions (el resto de workflows sí corrió). Lanzado a mano a las 10:57 UTC;
  `metricas.json` nuevo a las 10:58 (commit `087f22c`). Uno de los dos programados apareció al fin a
  las 11:47 (`3a7aabc`) y machacó esa lectura con otra peor: `MDS-022` se quedó sin curva de
  retención (la buena sigue en `087f22c`). Trampa 43, y encargo 4 de la revisión diaria.
- **La planificación del jueves 24 falló** a los siete segundos (estado de la tarea programada); la
  semana se planificó el viernes 25 (`6ccf959`).
- **Las revisiones del 26 y el 27** entregaron su `.tar.gz` en su conversación y no se aplicaron.
  Una sesión no puede leer las de otra: no se pueden rescatar desde aquí. La revisión del 28 rehízo
  lo que dependía de ellas. Detalle en el plan.
- **Ni una cara detectada en 51 planos** de `MDS-024` a `MDS-030` (`"caras": []` en todos los
  manifiestos). Causa: `opencv-python-headless` 5.0 sin `CascadeClassifier`, comprobado en el
  contenedor (`5.0.0`: no está; `4.14.0`: está). Trampa 42.
- **La respuesta del codirector a la tarea 3.5 del 23/09** (sí a Kaggle y a cambiar la regla 7; el
  Engranaje no) llevaba cinco días sin leer. C51.2.
- **La planificación del 25/09 pedía ratificar su criterio de la lectura en frío.** Ratificado (C48.2).

## 3. El punto de control

Con la lectura del 28/09: mediana C26 24,0 (de 11,0); 5 de 20 por encima de 100 y 6 por encima de
50; mediana de los últimos diez 90,5 y de los últimos cinco 68. Semanas: 21 · 9 · 113 · 68. Retención
a 30 s: `MDS-021` 59,5 %, `MDS-022` 64,4 % (máximos del canal). 2.283 visualizaciones de Shorts,
27 «me gusta», 0 suscriptores, 0 comentarios, 1 compartido. Tráfico de los recientes: feed 93-98 %.

Los tres casi ceros de los últimos diez: `MDS-017` (0, resubido), `MDS-023` (2, resubido) y
`MDS-024` (4, sin causa conocida). Veredicto y previsión: versión 14, «El punto de control».

## 4. Lo que se hizo

**Código** (subido por la dirección, autorizado en la sesión). **Los workflows no**: el token no
tiene permiso para escribirlos y GitHub rechazó el primer `push` («refusing to allow a Personal
Access Token to create or update workflow … without `workflow` scope»). Van al codirector en
`00_estrategia/tareas/workflows_2026-09-28/` (fuera de git), tarea 1:

- `04_agentes/entregar.py` (nuevo, C53): la entrega de las tareas. Dos mitades: la tarea sube lo
  suyo a `claude/entrega-<tarea>-<fecha>`; el workflow lo aplica en `main` con la copia de `main`
  del script, mezcla a tres bandas, validación de guiones y lista de lo que se quedó fuera.
- *(para el codirector)* `entregas.yml` (nuevo, C53); `visuales.yml` y `vista.yml`, el `push` solo
  en `main`; `metricas.yml`, intentos nuevos el lunes a las 11:07 y el martes a las 05:19 UTC.
- `03_produccion/modelos/face_detection_yunet_2023mar.onnx` (+ licencia MIT) y `.gitattributes`
  (`*.onnx binary`).
- `03_produccion/pipeline/visual.py`: detector de caras YuNet (funciona con OpenCV 5 y 4), Haar de
  respaldo, y `detector_caras()` con estado visible en `diagnostico.json`
  (`caras`), en el manifiesto (`detector_caras`) y en la hoja de contactos; la falsa alarma diaria
  de `cloudflare_token_de_cuenta` pasa a «no aplica» cuando el token de usuario está bien.
- `04_agentes/explorador_de_demanda.py`: radar de actualidad (C52) en `demanda_bruta.json` →
  `actualidad`.
- `01_bibliografia/data/semillas.json` + `.md` regenerado: `K03` verificada contra
  aclanthology.org/2023.acl-long.41 (título, autores, DOI). Sus cifras en `MDS-029` coinciden con el
  resumen («30 accuracy points», «more than 2/3 of cases»). `validar_bibliografia.py` pasa.

**Documentos:** `PLAN_DE_CAMBIOS.md` (versión 14), `REGLAS.md` (7.1, nota en la 10, 11.9),
`PROPIEDAD_DE_FICHEROS.md` (cómo se entrega desde hoy), `PROMPT_DE_ARRANQUE.md` (autorizaciones,
trampas 42-45, estado a 28/09), `LEEME.md`, `tareas/revision-diaria.md` y
`tareas/planificacion-jueves.md` (entrega con `entregar.py`, C52, C54, C48.2),
`04_agentes/prompts/guionista_corto.md` (C48.2), y esta bitácora, la nota de `08_comunicacion/` y
`05_calendario/bitacora/2026-09-28-metricas.md` (la bitácora de métricas, que había llegado a
`08_comunicacion/`).

**Tareas programadas** (almacén): los arranques de la revisión y la planificación dicen «entrega con
`entregar.py`; plan B el paquete»; la planificación corre jueves, viernes y sábado; métricas pasa a
las 12:30 UTC y deja de decir que pruebe el puente de dispositivos.

## 5. Cómo se comprobó

- **`entregar.py`**, en local contra un origen simulado (clon *bare* del repositorio):
  1. entrega normal de la revisión (bitácora, estado, `ajustes.json` y un guion dentro de las 48 h):
     sube, «Entregas» la aplica **encima de un commit del bot** hecho entre medias, y borra la rama;
  2. ficheros ajenos (`00_estrategia/`, una bitácora con fecha vieja, un guion fuera de las 48 h,
     `parrilla.json`): no suben, y el commit de `main` los lista con el motivo;
  3. un guion roto (`validar_guion.py` da error): fuera;
  4. `ajustes.json` cambiado a la vez por la tarea y por la dirección: **no se aplica** y la rama se
     queda;
  5. sin token: sale con 2 y pide el plan B.
- **El proxy de la nube**, con un `push --dry-run` real desde el contenedor: rechazado porque el
  repositorio no está entre los de la sesión (trampa 45). Lo que no se ha podido probar: que con el
  repositorio añadido a la tarea el `push` de una rama `claude/` pasa. Se verá en la primera entrega.
- **`visual.py`** con OpenCV 5.0 y 4.14: YuNet monta en las dos y da el mismo resultado sobre las
  quince fotos del banco (28 caras; Haar veía 21, con falsos positivos, y ninguna en el grupo). Sin
  el modelo: la 4.14 cae a Haar y lo dice; la 5.0 dice «SIN DETECTOR» y por qué. Sobre el fotograma
  de `MDS-026` escena 1 ninguno ve la cara (desenfocada y tapada por una mano): la pregunta 3 de la
  hoja sigue siendo a ojo.
- **El radar de actualidad**, con datos sintéticos (el contenedor no llega a Google Trends ni a
  Wikimedia; Actions sí). Cada fuente falla por su lado sin tumbar la medición.

## 6. Para la próxima sesión

Ver la versión 14, «El calendario» y «Lo que queda mirado y sin resolver».
