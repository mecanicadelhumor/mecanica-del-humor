# Sesión de dirección — lunes 21 de septiembre de 2026

Sesión con el codirector delante, desde su ordenador (carpeta conectada). Arranque con
`PROMPT_DE_ARRANQUE.md` y `PROMPT_DIRECCIÓN.md`, y lectura completa del orden de siempre:
`LEEME.md`, `REGLAS.md`, `PROPIEDAD_DE_FICHEROS.md`, `PLAN_DE_CAMBIOS.md` (versión 10),
`ESTADO.md`, las bitácoras del 19 y el 20, y `metricas.json`.

**Una corrección de entrada:** el codirector escribió que faltaban las métricas semanales.
**Sí están**: `metricas.yml` corrió esta madrugada y el commit `9255666` («métricas
2026-09-21») las trae; `actualizado_utc` es `2026-09-21T05:33:19Z`. Toda la sesión se ha hecho
con esos números, no con los de la semana pasada.

Las cinco cosas que traía él, y qué ha salido de cada una:

---

## 1 · El choque de ficheros del 19 y el 20 → C45

**Causa encontrada, y es estructural.** La revisión diaria corre los siete días y entrega un
`.tar.gz` que el codirector aplica a mano. El sábado no lo aplicó; el domingo llegó el segundo
paquete; los dos traían **un `ESTADO.md` distinto del mismo fichero**. Nada más chocó porque
todo lo demás que entrega esa tarea es un fichero nuevo por ejecución.

**Va a repetirse todos los fines de semana** mientras la entrega sea manual y la tarea corra
los siete días.

**Y la regla que faltaba ya existía.** El 21 de agosto, tras el borrado de 188 líneas de
bitácora, se escribió: *un fichero nuevo no puede pisar nada*. El 31 de agosto se le dio a ese
mismo agente `ESTADO.md`, **que se reescribe entero cada día**: la figura exacta que la regla
existía para eliminar, diez días después. Trampa 36.

**Hecho hoy:** nace `05_calendario/estado/` (un fichero por día, el estado de hoy es el de
nombre más alto) con su `LEEME.md`; `ESTADO.md` queda **congelado** como `MEJORAS.md`;
`ESTADO_old.md` pasa a `estado/2026-09-19.md` con `git mv` y el del domingo a
`estado/2026-09-20.md`; paso 6 de `revision-diaria.md` reescrito.

### Y un hallazgo lateral: la incidencia del domingo era falsa

`ESTADO.md` del 20/09 daba `MDH-007` por ausente del registro. **Estaba subido desde las
09:37:31 UTC** (`6sAuU_OHxwI`, `public`); la revisión escribió a las 09:53 UTC sobre un clon
anterior a ese commit. **Dieciséis minutos.** El tercer intento de producción (08:23 UTC, con
los retrasos habituales de Actions) cae justo encima de la ventana de la revisión de las 11:30.

Consecuencia real: el codirector llegó el lunes con un pendiente —«mover `MDH-007` de día en
`parrilla.json`»— para un vídeo publicado hacía veinticuatro horas. **Anulado**, y escrito como
corrección al pie de `estado/2026-09-20.md`.

**Arreglo:** `revision-diaria.md` ahora obliga a `git fetch` y releer
`registro_publicaciones.json` de `origin/main` **inmediatamente antes** de escribir una
incidencia de «falta el vídeo del día», diciendo en la bitácora a qué hora se releyó.

---

## 2 · «Las visitas se han hundido y el largo tiene cero» → C42

Medido antes de opinar. Lectura del 21/09, visualizaciones a 48 horas:

- **Los cinco últimos Shorts: 1.210 · 161 · 135 · 27 · 0.** Los quince anteriores: mediana 10,
  ninguno por encima de 50.
- **Los siete episodios largos, vida entera: 18 · 34 · 13 · 10 · 6 · 33 · 0 = 114.**

**Dos cosas que el codirector no tenía y cambian la lectura:**

1. **Que un largo tenga 0 a las 48 horas no es nuevo.** `MDH-004`, `MDH-005` y `MDH-006`
   tuvieron **los tres** 0 en su lectura a 48 h. Es el comportamiento normal del formato en este
   canal desde agosto; lo ha visto hoy porque hoy lo ha mirado.
2. **El precacheo del largo se estaba comiendo el respaldo de voz de los Shorts.** La cabecera
   de `voz_precache.py` dice «cuota propia, nunca la de los Shorts (C7)». Era verdad el 14/09 y
   es **falsa desde el 15**, cuando C33.1 escribió
   `MODELOS_CORTO = (MODELO_GEMINI, MODELO_GEMINI_LARGO)`: `gemini-2.5-flash-preview-tts` pasó a
   ser el **peldaño (b)** del respaldo de los Shorts. Y `voz_adelantada.yml` corre **todos los
   días** con `PRESUPUESTO_POR_DEFECTO = 9` sobre una cuota de 10. **Nueve de cada diez
   peticiones de la red de seguridad de los Shorts se gastaban en el largo.** Un Short necesita
   seis. Trampa 35.

Y la aritmética que hacía imposible a `MDH-007` desde el principio: 41 escenas ÷ 9 al día = cinco
días de precacheo perfecto, y los rechazos también gastan cuota (trampa 30). Llegó con 38 de 41.

**Decidido: se suspende el formato largo (C42).** `MDH-008` fuera de `parrilla.json` (guardado
en `_emisiones_suspendidas` con su motivo); su guion se queda escrito y sin tocar; la semana son
cinco Shorts y nada el fin de semana; `voz_adelantada.yml` lo desactiva el codirector. **Vuelve
cuando `control_c26.mediana_vistas_48h` llegue a 50.** Hoy 11,0.

### Sobre la gelotofobia, que es lo que de verdad le molestaba

Tiene razón y el canal tenía el recibo. `MDS-013` —«Miedo a que se rían de ti», el mismo asunto
en Short— hizo **6 visualizaciones a 48 horas** el 9 de septiembre, el peor de su semana.
`MDH-007` se planificó el 3 de septiembre, antes de que ese número existiera; pero **entre el 9
y el 20 nadie volvió sobre él**, porque no hay ninguna regla que mate un largo ya planificado
cuando su sonda en formato corto se hunde. Con el largo suspendido esa regla no hace falta
todavía; la versión general sí se ha escrito, y es C46.

---

## 3 · «Las voces de cada escena suenan distintas» → C44

**Tiene razón, y no es solo que pase: se lo estamos pidiendo.** Tres causas, medidas sobre el
código:

1. Cada escena es una llamada independiente. `voice_name: Charon` fija la identidad, no la
   toma: registro, velocidad, energía y distancia al micro las elige el modelo cada vez.
2. **`DIRECCION_POR_PAPEL` pide explícitamente que el timbre cambie**: «cambia claramente de
   color de voz» (contraste), «cambia de color de voz mientras las dices» (cita), «baja el tono»
   (enumeración, cierre). Bien pensado para una escena suelta; justo lo que no hay que pedir
   cuando la continuidad entre tomas ya es frágil.
3. **El volumen de cada toma no se iguala nunca.** `montaje.py` aplica `loudnorm=I=-14` **una
   sola vez sobre la mezcla final** — normaliza el programa contra el estándar de YouTube y no
   hace nada por que la escena 4 suene igual que la 3. Probablemente la mitad de lo que se oye
   como «voz distinta».

**Plan en tres capas (C44), y ninguna entra esta semana** porque la semana del 21 es la primera
medida limpia de C38 (regla 11.1): **A** igualar el volumen por escena antes de la mezcla (no
toca la caché); **B** ficha de voz fija y la dirección deja de pedir timbre, con
`VERSION_DIRECCION` 2→3 (asumible **porque el largo está suspendido**); **C** = C36 reactivado,
una sola toma por vídeo con corte por alineador local. A y B entran el **lunes 28**, juntas y
dicho por qué.

**Y algo que se arregla solo:** el 20/09 se publicó un episodio de 41 tomas distintas. Con C42,
el peor caso pasa a ser de seis.

---

## 4 · «¿Convertimos la dirección en tarea programada?» → C43

**No.** Razonamiento entero en C43. El resumen: la frontera ya la escribió él —*las tareas
programadas tienen que ejecutarse enteras y solas*— y una sesión de dirección es por definición
lo que no se puede hacer sin una persona; esta misma tiene tres puntos donde la respuesta es «en
esto tienes razón y en esto no». Y la lectura de los nueve documentos no es la parte cara: la
cara es decidir, y delegarla a un modelo barato es quedarse con el gasto y perder el criterio.

**Lo que sí se automatiza desde hoy es la salida**, que es su idea del 18/09 llevada a su sitio:
después de cada sesión de dirección queda `08_comunicacion/AAAA-MM-DD-direccion.md`, y los tres
prompts ya dicen que esa carpeta se lee antes de trabajar. Hasta hoy, lo decidido en dirección
llegaba a los agentes por reescritura de prompts: lento, a medias (trampas 12, 18, 32) y sin
rastro de cuándo se enteró cada uno.

---

## 5 · «No vamos bien de cara a los hitos» → la respuesta no es la que esperaba

**El punto de control del 27 de septiembre ya está contestado, y con un sí.** Su pregunta, sin
tocar desde la versión 4, es: *¿algún Short ha pasado de 100 visualizaciones en 48 horas?*
**Tres**: `MDS-016` (1.210), `MDS-019` (161), `MDS-018` (135). El desenlace escrito para ese sí
es «el formato funciona, toca escalarlo».

**Y la previsión del 15 de noviembre, que es lo que él preguntaba.** La mediana de hoy (11,0) no
predice nada: quedan 55 días y ~39 Shorts más, así que **el 15 de noviembre ninguno de los
veinte Shorts publicados hasta hoy estará en la ventana de veinte**. Lo que pronostica es el
régimen de la última semana: mediana 135 con el outlier, 81 sin él, 148 sin el cero.

**Conclusión: no estamos fracasando, estamos en la frontera** entre «se amplía el tema» y «se
sigue». Y el lado en el que caigamos **no lo deciden los vídeos buenos, lo deciden los ceros**:
subir un 161 a 200 mueve la mediana menos que evitar un 0. Por eso casi todo lo decidido hoy va
contra los ceros.

**Y una cosa que había que decir hoy y no en noviembre:** la tercera puerta de C26 —«algún Short
por encima de 1.000»— **ya está abierta** desde el 14/09. Creo que está mal escrita y propongo
cambiarla por «dos Shorts por encima de 1.000 en semanas distintas». Es decisión del codirector
y tiene fecha tope el **8 de noviembre**, que es lo que la propia C26 exige: los umbrales se
discuten antes de ver los datos, no después.

---

## 6 · Lo que apareció sin que nadie lo buscara → C46 y C47

**C46 · el canal no se lee a sí mismo.** La planificación de los jueves elige la semana con
`demanda.json` y **no lee `metricas.json`** — su propio prompt dice «no eres dueño de
`metricas.json`» y de ahí nadie dedujo que sí tenía que leerlo. Precio con nombre: `MDS-016`
hizo 1.210 el 14/09 y **una semana después no hay ni un vídeo que lo continúe**. Nadie lo
decidió: el número no llegaba a quien elige los temas. Arreglado con el paso 1 bis
(derecho de tanteo de los dos mejores temas de las últimas cuatro semanas).

Y de paso, dos datos falsos en ese mismo prompt: su sección «dónde está el canal» estaba
congelada en el 7 de septiembre, y seguía diciendo que la búsqueda es la única superficie que
responde — **corregido por C40 el 18/09** (feed 54,6 %, búsqueda 27,7 %) sin propagarse a los
prompts. Trampa 32 otra vez.

**C47 · las métricas solo se leen los lunes.** `metricas.yml` tiene cron `19 5 * * 1` y
`37 8 * * 1`. La revisión diaria comprueba que el vídeo se publicó y **no mira nunca cuánta
gente lo vio**. Un Short puede hacer 0 seis días sin que nadie se entere: es literalmente lo que
ha pasado con `MDS-017`. Encargo de la semana para la revisión diaria (lectura ligera diaria,
sin curvas de retención, en `metricas_diarias.json`), y el cambio de cron va al codirector
**cuando el script exista**, no antes: un cron diario sobre el `metricas.py` actual pondría el
fichero en varios megas de churn en git.

---

## Y una cosa desbloqueada de paso

**C34, el banco de imágenes, estaba parado desde el 15/09 esperando los enlaces de origen.** El
codirector dejó `02_marca/banco/creditos_pixabay.csv` el 18/09 con archivo, enlace y autor de
las quince fotos. Lo que faltaba era el fichero que la regla 9 exige —licencia, autor y enlace
por imagen, escritos **antes** de usarse una sola vez—: generado hoy,
`02_marca/banco/banco.json`, con licencia Pixabay Content License y el sha256 de cada archivo.
**C34 deja de estar bloqueado.**

---

## Ficheros tocados en esta sesión

**Creados:**
- `05_calendario/estado/LEEME.md`, `estado/2026-09-19.md` (renombrado de `ESTADO_old.md`),
  `estado/2026-09-20.md`
- `02_marca/banco/banco.json`
- `08_comunicacion/2026-09-21-direccion.md`
- `00_estrategia/tareas/tareas_codirector_2026-09-21.md`
- `05_calendario/bitacora/2026-09-21-direccion.md` (este)

**Modificados:**
- `00_estrategia/PLAN_DE_CAMBIOS.md` (versión 11 añadida al final; nada anterior tocado)
- `00_estrategia/PROMPT_DE_ARRANQUE.md`, `00_estrategia/LEEME.md`
- `00_estrategia/tareas/revision-diaria.md`, `planificacion-jueves.md`, `metricas-lunes.md`
- `05_calendario/parrilla.json` (`MDH-008` a `_emisiones_suspendidas`)
- `05_calendario/ESTADO.md` (congelado)

**No tocados a propósito:** ningún guion, `demanda.json`, `CALENDARIO.md`,
`registro_publicaciones.json`, `qa/`, `metricas.json`, `.github/workflows/` ni
`PROMPT_DIRECCIÓN.md` (que es del codirector y no se edita nunca).

**Pendiente de él:** `tareas_codirector_2026-09-21.md` — el `push`, las impresiones en Studio,
desactivar `voz_adelantada.yml`, el `ESTADO.md` de hoy si llega antes del push, y la decisión
sobre la puerta de los 1.000.
