# Dirección — sábado 12 de septiembre de 2026

Sesión desplazada desde el viernes 11 (cuota y tiempo). En modo Cowork, con la carpeta
`C:\MisProyectos\Humor` conectada, así que los ficheros se escriben directamente allí y el
codirector hace el commit. Él se ausentó a media sesión; el resto se completó sin nadie
delante.

**Nota de entorno, por si vuelve a pasar:** `device_bash` no arranca en esta máquina —una
actualización de Windows del 8 de septiembre impide que el espacio de trabajo monte las
carpetas—. Se ha trabajado con `device_list_dir` / `device_stage_files` /
`device_commit_files`, que sí funcionan. Es más lento pero no cambia nada del resultado.

**Orden del día del codirector:** cinco puntos, más las dos autorizaciones pendientes de
escribir y una revisión de `producir.yml`. Se cerraron los siete.

---

## 0 · Las dos autorizaciones, escritas

Estaban dadas en `PROMPT_DIRECCIÓN.md` el 7/9 y no habían llegado a `PROMPT_DE_ARRANQUE.md`,
que es donde una autorización sobrevive a la conversación en la que se dio.

1. **`montaje.py`, autorizado sin acotar.** Sustituye a la autorización estrecha del 28/08
   (solo el manifiesto de subtítulos). **Consecuencia inmediata: P9 —los tres sonidos— queda
   desbloqueado** y entra en la semana del 21 según C25, sin esperar nada más.
2. **Levantadas las restricciones de edición en todo el repositorio, solo para la dirección.**
   Para los demás agentes no cambia nada: siguen con `PROPIEDAD_DE_FICHEROS.md` y la regla
   11.7 tal cual. Y **`.github/workflows/` queda protegida siempre**, también para la
   dirección: esos ficheros ni siquiera se pueden escribir en remoto.

Escrito además en `REGLAS.md` (regla 11.7 reformulada) y `PROMPT_DIRECCIÓN.md` añadido al
orden de lectura del prompt de arranque, con la nota de que es del codirector y no se toca.

---

## 1 · Vídeo largo sin depender de la cuota de voz

**Decisión: ninguna de las tres opciones, y el motivo es que la (a) ya está hecha.**

La planificación del jueves ya escribe el episodio largo del sábado **siguiente**: la del 10
escribió `MDH-007`, que se produce el 19. Son nueve días, que es exactamente lo que pedía la
opción (a). **El calendario ya da los días; lo que falta es la máquina que los gasta**, y esa
está diseñada desde el 7 (C27: la caché de `voz.py` más `voz_adelantada.yml`) y bloqueada
solo porque el workflow lo tiene que crear el codirector.

La (b) —mover el día— no compra nada que la caché no compre, y el jueves es el día correcto
por cuotas.

La (c) acierta en la forma y falla en el quién, y eso queda escrito como criterio general:
**construir el vídeo día a día no necesita juicio, así que no debe ser un agente.** Un agente
es la forma más cara de ejecutar un bucle determinista, la única que puede equivocarse de
forma creativa, y añade un cuarto prompt, un cuarto dueño y una cuarta cuota. Un workflow de
Actions es gratis, tiene red, tiene los secretos y ya corre todos los días.

**Dos correcciones a C27 que salen de lo que dijo el codirector:**

- **Un episodio largo sale con UNA sola voz, nunca mezclada.** La versión 6.1 decía que un
  mal día «deja alguna escena con voz peor» — que es literalmente la chapuza que él descartó
  el 7. Se decide **una vez, el viernes por la noche**: caché completa → todo Gemini; falta
  una sola escena → todo `edge-tts`.
- **La ventana pasa de martes-viernes a viernes-viernes.** Cuatro días × 10 peticiones son 40
  llamadas para ~40 escenas: cero margen. Como el guion queda cerrado el jueves anterior, la
  ventana real es de ocho días: **80 llamadas para 41 escenas.**

---

## 2 · El guionista — los dos prompts reescritos

Lo más urgente según el codirector, con tres avisos en cuatro días.

**El diagnóstico, y es lo que justifica reescribir en vez de parchear: los tres guiones
cumplían el prompt entero.**

- **MDS-013 (9/09)**, «un recorte de un recorte»: seis escenas y **cuatro asuntos**. El
  ejemplo concreto entra en el segundo cero, desaparece cuatro escenas y vuelve en las
  últimas seis palabras. Las dos ideas nuevas entran en los segundos 32 y 36 de un vídeo de
  52. No le falta un principio y un final: **tiene cuatro principios.**
- **MDS-014 (10/09)**, el «martes»: la voz dice «domingo» en la escena 2 y «hoy» en la 4,
  mientras la pantalla de la 4 pone «martes». El mismo dato con tres palabras. La regla 14.1
  no lo cazaba porque el dato sí estaba en las dos mitades.
- **MDH-006 (12/09)**, «el chiste no entra»: cumple «mínimo dos risas, una antes del segundo
  quince» **exactamente** — y las dos caen en los primeros veinte segundos, seguidas de
  cuatro minutos y medio sin nada, y un callback final que remite a una premisa de hace
  cuatro minutos **y pide una resta** (doce menos dos). Un suelo usado como techo.

**Lo que cambia, en una frase:** el prompt decía qué tenía que **contener** un guion y nunca
qué tenía que **sostenerlo**. Una lista de ingredientes se puede cumplir entera y que el
plato no ligue.

**En `guionista_corto.md`**, tres pruebas que van delante de todo y se pasan antes de
escribir la primera escena: *el hilo* (un solo sujeto, tres frases en `notas_humor` que lo
nombran las tres, y el ejemplo vuelve por su nombre en una escena del medio), *nada nuevo
después de la mitad*, y *el detalle concreto con la misma palabra*. Más una lista de
comprobación de seis líneas al final.

**En `guionista.md`**, la regla de la risa deja de contar y pasa a medir distancias: **nunca
más de noventa segundos sin algo construido para hacer reír** —cuatro o cinco por episodio,
no dos—, la primera sigue antes del segundo quince, un callback a más de noventa segundos
vuelve a decir su premisa en la misma frase, y un chiste no le pide aritmética al espectador.
Más un apartado nuevo sobre el `diagrama` horizontal (ver punto 3).

**Lo que no se ha tocado, a propósito:** las cinco series, el chiste primero y la prueba del
WhatsApp, el máximo de tres `enunciado`, C19 y el campo `icono`, el ámbito del resaltado y el
cierre que dice dónde falla. Nada de eso ha fallado esta semana.

---

## 3 · Las revisiones fallan por los dos lados

### 3a · Inventan — el falso positivo de MDS-011

**Por qué no lo comprueba en YouTube: porque no puede.** La revisión diaria corre en un
contenedor en la nube **sin red**, y el permiso que el codirector concedió a mano es el del
token de OAuth, que usan `publicar.py` y `metricas.py` **desde GitHub Actions**. La revisión
diaria no lo ha tenido nunca.

Lo que lee es `registro_publicaciones.json`, que guarda el estado **del momento de la
subida** y solo corrige `metricas.py`, **los lunes**. MDS-011 se subió `private` el 07/09, el
codirector lo publicó a mano, y nada lo escribió de vuelta. Seis días de incidencia. **No
estaba leyendo mal el fichero: estaba leyendo un fichero caduco como si fuera el mundo.** Es
la trampa 4 otra vez.

**Arreglado en dos capas.** En el prompt, ya: «no lo sé» no es «no publicado» — la primera
vez INCIDENCIA, a partir de la segunda baja a la bitácora, y si el codirector ha dicho en
cualquier sitio que lo publicó él, el asunto está cerrado. El motivo de fondo no es de
precisión sino de ruido: **una incidencia que se repite idéntica seis días deja de ser un
aviso, y entonces el séptimo no se lee.** Y encargado el arreglo de raíz (C31): sacar a una
función suelta la parte de `metricas.py` que ya sabe preguntarle a YouTube, y un workflow
diario que la llame antes de las 11:28.

### 3b · Dejan pasar — el texto del segundo 2:34

**Medido, no deducido.** `MDH-006` escena 22, diagrama horizontal, tres cajas de 533 px y
texto a 46 px: «Espera a que lo abra el otro» mide **604 px**. Se sale 70 px, 35 por cada
lado. Y «Y solo con esa persona» mide 520: **13 px de margen, una palabra de distancia del
mismo fallo.**

**Por qué la barrera de C21 lo dejó pasar, que es lo interesante:** `comprobarDesbordes()`
llevaba `"svg text"` en su lista de selectores desde el 4 de septiembre. **Parecía cubierto y
no lo estaba.** El cálculo de desbordamiento está dentro de un `if (el instanceof
HTMLElement)`, y un `<text>` de SVG no lo es: de esos elementos solo se comprobaba el
rectángulo **contra el lienzo**, nunca contra su propia caja. Y las cajas del diagrama están
en el centro de la pantalla. **La única situación que la barrera podía cazar ahí era la
imposible.** Comprobado: 0 problemas sobre las 40 escenas de MDH-006.

Lo mismo con `ajustarTamano()` (C21.1): su lista no incluye `svg text` en absoluto. **El
diagrama horizontal era el único tipo de escena del motor sin ninguna protección de anchura,
en las dos capas.**

**Y un defecto que nadie había visto, encontrado por el camino:** esa rama pintaba los pasos
con `esc()` en vez de `rico()`, porque un `<span>` no existe dentro de un `<svg>`. **El
resaltado salía con los asteriscos a la vista.** Está publicado en MDH-004 escena 15 y
**estaba a punto de publicarse el 19/09** en MDH-007 escenas 10 («*Usarla*») y 20 («Buscas
*tres*»).

**Lo que entra (C29):** `ajustarTextoSVG()` mide con `getComputedTextLength()` y encoge
**en bloque** —el factor del peor para todos, porque tres tamaños de letra distintos en tres
cajas se leen como un fallo de maquetación—, con suelo de 32 px; la barrera gana una rama
para el texto SVG contra su propio `<rect>`; `ricoSVG()` pinta el resaltado con `<tspan
fill>`; y un aviso en `validar_guion.py` cuando un paso de diagrama trae más palabras de las
que caben.

**Verificado contra el motor (regla 11.2), no imaginado:**

- Las 302 escenas de los 28 guiones con el motor nuevo: **0 paran el render**.
- MDH-006 escena 22 después: los tres títulos a 37,89 px, el que se salía en **497 px dentro
  de 533**. Mirado en captura.
- Diferencia de píxeles contra el motor viejo: cambian **cuatro escenas**, y son exactamente
  las cuatro que tenían un defecto real. Todas las demás, idénticas al píxel.
- Determinista: dos pasadas del motor nuevo, diferencia 0,0000 %.

### 3c · Y el que faltaba: C22 nunca se escribió

Buscando por qué el «martes» no saltó, apareció que **la red determinista de C22 —el encargo
3, «señala las palabras de pantalla que no estén en la narración de su escena»— no existe en
el código.** Está dada por entregada en la cola desde el 10/09.

Se midieron las dos variantes contra los 302 guiones antes de escribir nada:

| Variante | Escenas señaladas | |
|---|---|---|
| C22 como se especificó (toda palabra de contenido, por raíz) | **222 · 73,5 %** | ruido |
| días, meses **y cifras** | 44 · 14,6 % | cinco falsos positivos de números, ningún acierto |
| **días y meses solos** | **3 · 1,0 %** | las tres reales, cero falsos positivos |

**C22 no se escribió porque no se puede escribir como estaba especificada.** Queda cerrada
así, dicho, en vez de seguir abierta para siempre. La versión estrecha entra como **C28** y
es **error**, no aviso: aquí no hay nada aguas abajo que lo sanee. Las tres que señala están
ya publicadas; **los seis guiones de la semana del 14 pasan limpios.**

---

## 4 · La revisión semanal no puede volver a bloquearse

**La causa estaba escrita en el prompt.** `planificacion-jueves.md`, regla 1: *«Si
`mcp__remote-devices__device_list_dir` sobre `C:\MisProyectos\Humor` responde: trabaja ahí»*.
Y lo mismo en la revisión diaria.

Una tarea programada corre en la nube y **el puente de dispositivos no existe en ese modo**
—lo dicen todas las bitácoras, incluida la del 3 de septiembre con esas palabras—. Lo único
que consigue esa llamada es **abrir una petición de autorización** en el ordenador del
codirector. A las diez de la noche de un jueves, nadie la contesta. La optimización compraba
no tener que descomprimir un `.tar.gz`; costó una semana de planificación.

**Fuera la sonda de los dos prompts**, y delante de todo lo demás la regla que pidió el
codirector: *no pidas nunca una autorización, un permiso ni una confirmación a nadie; lo que
no puedas hacer tú solo, no lo intentas: lo escribes, y sigues.*

**Y de paso, lo que hacía esto difícil de arreglar: se acaban las dos copias.** Hasta hoy el
prompt que corría vivía en el almacén y `00_estrategia/tareas/` era un espejo — y el propio
`LEEME.md` de esa carpeta avisaba de que un día no coincidirían. **Ahora el fichero del
repositorio ES el prompt**, y el del almacén es un arranque de una página que dice: clona,
lee `00_estrategia/tareas/<tu fichero>.md`, síguelo. Cambiar lo que hace un agente pasa a ser
editar un fichero y commitearlo; el prompt se versiona con git y se revisa en un diff, que es
lo único del proyecto que no se podía revisar así.

El precio, dicho: **un cambio no surte efecto hasta que está en `origin/main`** (trampa 11
aplicada a los prompts). Y por si el clon falla, el arranque lleva repetidas dentro las reglas
cuyo incumplimiento hace daño irreversible.

**Aplicado y verificado hoy** en `trig_015qkb2sqbbJwJE1qgoNMK95` (planificación) y
`trig_019QjtovuzeUocmx1P8NJH3F` (revisión diaria). **Métricas
(`trig_01GhNrF8nA2w2nXSfetcrHkQ`) sigue con el prompt entero en el almacén**: pendiente.

---

## 5 · El formato de las peticiones

Queda como regla (C32), en `PROMPT_DE_ARRANQUE.md` y en el plan: todo lo que la dirección
necesite del codirector va en `00_estrategia/tareas/tareas_codirector_AAAA-MM-DD.md`,
explicado de principio a fin, sin resumir aunque ya se haya hecho antes, con tiempo estimado
y **con su sitio exacto**.

Lo último sale de un fallo propio de hoy, ver abajo.

---

## 6 · `producir.yml` — revisado, y está mal por mi culpa

La línea que añadió el codirector es **correcta letra por letra**, y está en el **paso
equivocado**: la pegó en el `env:` de «Subir a YouTube» (línea 294) y tiene que ir en
«Sintetizar narración» (línea 194), que es el que llama a `voz.py`. En Actions las variables
de un paso solo existen en ese paso, así que `publicar.py` recibe una clave que no usa y
`voz.py` arranca sin ella y cae al respaldo sin decir nada.

**Y es culpa mía.** Mis instrucciones de esta mañana decían «busca `secrets.`, copia una de
esas líneas y pégala justo debajo» **sin decir en qué paso**, y la primera aparición de
`secrets.` en el fichero está justamente en el paso de subir. Hizo exactamente lo que ponía.

Es la trampa 12 repetida —documentar una sintaxis sin documentar su ámbito— y queda anotada
como **trampa 18**. El corte exacto, con los dos bloques antes y después, está en
`tareas_codirector_2026-09-12.md`.

---

## Trampas nuevas

- **18. Documenté una sintaxis y no documenté en qué paso iba.** Una instrucción de «copia
  esta línea» sin decir dónde es media instrucción. Y la prueba de que está completa no es
  releerla: es preguntarse qué haría alguien que solo tiene el fichero delante.
- **19. Una comprobación puede estar mirando el sitio equivocado y parecer que funciona.**
  Que un selector esté en la lista no significa que se esté midiendo. Una comprobación que
  nunca ha dado positivo sobre una familia entera de casos no es una comprobación probada:
  es una comprobación sin probar.
- **20. Un mínimo escrito como suelo se usa como techo.** Cuando una regla cuente cosas,
  pregúntate qué pasa si alguien pone el mínimo exacto en el peor sitio posible. Si la
  respuesta es «entonces la regla no sirve de nada», lo que hay que medir no es la cantidad:
  es la distancia.

---

## Ficheros escritos hoy

Directamente en `C:\MisProyectos\Humor` con `device_commit_files`. El commit lo hace el
codirector.

- `04_agentes/prompts/guionista_corto.md` · `guionista.md` — reescritos
- `04_agentes/validar_guion.py` — C28 (error) y C29 (aviso)
- `03_produccion/pipeline/escena.html` — `ricoSVG()`, `ajustarTextoSVG()`, rama SVG de
  `comprobarDesbordes()`
- `00_estrategia/tareas/revision-diaria.md` · `planificacion-jueves.md` · `LEEME.md`
- `00_estrategia/PLAN_DE_CAMBIOS.md` (versión 7) · `PROMPT_DE_ARRANQUE.md` · `REGLAS.md` ·
  `LEEME.md`
- `00_estrategia/tareas/tareas_codirector_2026-09-12.md`
- `05_calendario/bitacora/2026-09-12-direccion.md` (este fichero)

**No se ha tocado** `00_estrategia/PROMPT_DIRECCIÓN.md` (es del codirector), nada de
`.github/workflows/`, ningún guion, `parrilla.json`, `ESTADO.md` ni nada de la revisión
diaria o de la planificación que no sea su prompt.

---

## Lo que queda pendiente, y por qué

1. **El commit** — del codirector, y corre prisa: la revisión diaria de mañana y la
   planificación del jueves leen `origin/main`.
2. **`producir.yml`** — del codirector. `.github/workflows/` está protegida siempre.
3. **`voz_adelantada.yml`** — el diseño lo escribe la revisión diaria en la semana del 14, en
   `07_pruebas/`; lo crea el codirector.
4. **C31, la parte de código** — encargado a la revisión diaria (encargo 11).
5. **`metricas-lunes.md`** — sigue con el prompt entero en el almacén. No se ha pasado al
   esquema nuevo hoy porque no ha dado fallos y no corría prisa; queda dicho para no darlo
   por hecho.
6. **El nivel de audio de MDH-006** (`pico_dbtp` −0,59) — el vídeo ya está publicado; queda a
   que el codirector lo escuche si quiere.

**Y lo que no se ha tocado hoy a propósito:** los números. Seguimos por debajo de 100
visualizaciones por vídeo y todo lo de hoy es proceso, no audiencia. El punto de control
sigue siendo el **27 de septiembre** y la decisión, el **15 de noviembre**.
