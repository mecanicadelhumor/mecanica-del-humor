# Dirección — martes 15 de septiembre de 2026

Sesión fuera de calendario, convocada por el codirector por la mañana: «algo se ha roto». En
modo Cowork con la carpeta conectada. `device_bash` sigue sin arrancar (la actualización de
Windows del 8 de septiembre, igual que el 12), así que se ha trabajado sobre un clon de
`origin/main` en el contenedor y se ha escrito en la carpeta con `device_commit_files`. Antes de
escribir se comprobó que los veinte ficheros tocados eran, en la carpeta, idénticos en tamaño a
los de `origin/main`: no había cambios locales sin commitear que pisar.

**Orden del día del codirector** (`PROMPT_DIRECCIÓN.md`, 15/09): la buena noticia de `MDS-016`,
la voz mezclada de `MDS-017`, preferencia por un Flash más antiguo o por otro proveedor antes que
`edge-tts`, arreglarlo rápido para volver a producir el vídeo esta tarde, y el guion de `MDS-017`,
«un desastre». Y del 14/09: las respuestas escritas dentro de `tareas_codirector_2026-09-14.md`,
que ahora está en `.gitignore`.

---

## 1 · El diagnóstico

- `qa/MDS-017.es/ficha.json`: `"motores_por_escena": {"edge (respaldo)": 3, "gemini": 3}`. Sin
  `direccion_voz`, que el 14/09 se prometió en la ficha y `qa.py` no copiaba.
- El código de C7 caía a `edge-tts` **escena a escena** ante cualquier fallo, sin reintentos, y
  no reconocía el mensaje de cuota diaria de Google («`per_model_per_day`»).
- No se puede saber qué falló en cada escena: los registros de Actions piden credenciales desde
  el contenedor. Hipótesis compatibles: los 500 aleatorios que documenta Google para sus modelos
  TTS, o la cuota. El panel que pegó el codirector el 14/09 marcaba `Gemini 3.1 Flash TTS · 4/3
  RPM · 10/10 RPD` a esa hora, y la producción de las 01:13 UTC del 15 cae en el mismo día de
  California que las pruebas del 14.
- Mismo agujero en el largo: `MDH-007` tiene 41 escenas y el precacheo da 36 como mucho.

## 2 · Lo hecho (versión 9 del plan)

- **C33.1 en `voz.py`:** una voz por vídeo, reintentos, clasificación de errores, escalera
  3.1 → 2.5 → fallo sin subir antes de las 08:00 UTC → `edge-tts` entero solo en el último cron.
  Comprobación de duración plausible (el modelo leyendo las instrucciones). El largo pide en vivo
  lo que falte con el modelo de su caché. `titulo` a mitad de episodio pasa a dirigirse como
  «sección».
- `voz_precache.py`: tope de tres fallos por ejecución y la clasificación de errores compartida.
- `qa.py`: `modelo_voz`, `voz_mezclada`, `origen_voz` y `direccion_voz` en la ficha.
- `cola.py`: `MARGEN_MIN` de 15 a 45 minutos (un cron tardío programaba un `publishAt` que ya
  había pasado al subir).
- `03_produccion/cache_voz/LEEME.md`: para que la carpeta exista siempre (el `git add` que se le
  pide al codirector en `producir.yml` fallaría si no).
- **Doce pruebas con dobles de la API**, todas en verde (lista en la versión 9).
- **`MDS-017` a `MDS-020` reescritos** contra las tres pruebas de cosido, con las afirmaciones
  comprobadas en el texto o el resumen de cada artículo. `MDS-019` afirmaba lo contrario de su
  fuente. Los cuatro pasan `validar_guion.py` sin avisos y la barrera de C21 con las fuentes
  reales; `MDS-017` renderizado entero (49,6 s de voz simulada a 2,2 palabras/s). Sus cuatro
  ficheros de `publicaciones/` reescritos. `CALENDARIO.md` actualizado (serie de `MDS-018`, `K03`
  fuera de `MDS-020`).
- **Bibliografía:** `E06`, `G05` y `G06` corregidas en `BIBLIOGRAFIA_CURADA.md` y en
  `data/semillas.json` (este último es el que usa `publicar.py` para la lista de fuentes de la
  descripción; con los datos viejos, `MDS-019` habría salido citando otra revista y otro DOI).
  Si alguien vuelve a generar el `.md` con `scripts/generar_md.py`, las notas de comprobación de
  esas tres fichas se pierden: están también en la versión 9 del plan.
- **Prompts:** la planificación gana dos reglas (un resultado se copia del resumen; una
  referencia que se nombra se explica). La revisión diaria sabe qué ha tocado hoy la dirección,
  qué significa `voz_mezclada` y que un fallo de las 01:13 con código 3 es el diseño.
- `PLAN_DE_CAMBIOS.md` versión 9 (con C36 y C37 propuestos), `PROMPT_DE_ARRANQUE.md` (trampas 25
  a 28, estado a 15/09, tabla de autorizaciones al día) y `LEEME.md`.

## 3 · Respuestas del codirector a las tareas del 14

- Cuota de imagen: todo `0/0`. **La vía 3 de C34 se cae.**
- Muestrario: **tratamiento 1, duotono ámbar.** C34 se escribe el viernes 18.
- Fotos: quince en `02_marca/banco/`, de Pixabay, sin `origen.txt`. Se le piden solo los enlaces.

## 4 · Lo que queda para el codirector

`00_estrategia/tareas/tareas_codirector_2026-09-15.md`: `pull` + `push` (y sacar de git los tres
ficheros privados, que estaban versionados y el `.gitignore` no los oculta), una línea en
`producir.yml` antes de esta noche, volver a producir `MDS-017` esta tarde, y los enlaces de las
fotos.

## 5 · Lo que queda para la dirección

- **Viernes 18:** C34 en `escena.html` (duotono ámbar, escena 1 de los Shorts) con su
  muestrario; C36 escrito y probado con `voz_prueba.yml`; revisar lo que escriba la planificación
  el jueves 17.
- **Lunes 21:** abrir la lectura de métricas por `MDS-016` (fuentes de tráfico y retención contra
  `MDS-015`) y comprobar en las fichas de la semana que `voz_mezclada` fue `false` las cinco veces.

---

## 6 · Tarde: la reproducción de `MDS-017` falla, y lo que enseña (versión 9.1, C33.2)

El codirector volvió a producir `MDS-017` a mano con C33.1 ya en `origin/main` (commits
`77c6922` y `7a00e7d`, 07:38 y 07:43 UTC). El paso de voz terminó con código 3 y no subió
nada. El registro, que copió en `PROMPT_DIRECCIÓN.md`:

- 3.1: 11 peticiones. Escenas 3, 4 y 5 rechazadas dos veces cada una con un 400 usando la
  dirección v1; la 3 y la 4 salen con la mínima; la petición 11 da 429.
- 2.5: 10 peticiones. Dos cortes de conexión; la escena 5 da 429 tres veces con un minuto de
  espera entre ellas.
- El bot guardó las ocho tomas en `cache_voz/` (commit `b405078`): **la línea de
  `producir.yml` funciona**.

El codirector borró en Studio el vídeo de las dos voces (`9H2xEZnFeHA`) y decidió que hoy no se
publica nada: *«Mejor eso que colocar el vídeo con la voz edge-tts»*.

**Lo comprobado aquí:** `google-genai` 2.23 reintenta por su cuenta 408, 409, 429, 5xx y cortes
de conexión, hasta 4 peticiones en ~3 s (medido con un transporte simulado). Con
`HttpRetryOptions(attempts=0, http_status_codes=[599])` es una sola. La librería convierte el 0
en 1 al crear el cliente, pero con el cerrojo de códigos sigue sin reintentar nada.

**Lo hecho:** C33.2 en `voz.py` y `voz_precache.py` (detalle en la versión 9.1); `cola.py` con
`rehacer_video_id`; `parrilla.json` con `MDS-017` el sábado 19 y `MDH-007` el domingo 20;
`CALENDARIO.md`; los dos prompts de las tareas; `PLAN_DE_CAMBIOS.md` 9.1,
`PROMPT_DE_ARRANQUE.md` (trampas 29 y 30) y `LEEME.md`. Veintiún casos de prueba en verde.

**No se ha podido comprobar** que la dirección v2 no se rechace: probarla cuesta cuota, y hoy
no queda. Lo dirá `origen_voz` en las fichas de `MDS-018` a `MDS-020`.

**Para el codirector:** segunda parte de `tareas_codirector_2026-09-15.md` (el `push` antes de
mañana a las 10:00, mejor esta noche, y el cron diario de `voz_adelantada.yml`, sin prisa).
