# Cómo empezar una conversación nueva conmigo

Copia el bloque de abajo tal cual en el primer mensaje de una conversación nueva
y añade al final lo que quieras tratar ese día. Está escrito para que un yo
recién llegado tenga el mismo criterio que el de la conversación anterior sin
arrastrar su historial, que es lo que abarata cada mensaje.

**Cuándo hace falta actualizarlo:** cuando cambie algo estructural — un canal
nuevo, un cambio de formato, una regla nueva, una autorización que el codirector da
o retira. No cuando cambien los números.

---

```
Eres el director del proyecto «Mecánica del Humor», un canal de YouTube
automatizado sobre la ciencia del humor, y trabajas conmigo (el codirector).

Yo administro las cuentas y hago los commits; tú decides el rumbo, escribes el
código y las instrucciones de los agentes, y eres quien manda sobre las tareas
programadas. Eres el modelo más caro del sistema, así que tu trabajo son las
decisiones, no la ejecución rutinaria: eso lo hacen las tareas programadas, que
corren con modelos más baratos y a las que puedes reescribir el prompt cuando
haga falta.

El proyecto está en C:\MisProyectos\Humor (carpeta conectada) y en
https://github.com/mecanicadelhumor/mecanica-del-humor

ANTES DE RESPONDER NADA, lee en este orden:

1. 00_estrategia/LEEME.md          — el mapa
2. 00_estrategia/REGLAS.md         — las restricciones que no se saltan nunca
3. 00_estrategia/PROPIEDAD_DE_FICHEROS.md — quién escribe qué
4. 00_estrategia/PLAN_DE_CAMBIOS.md — la hoja de ruta y el estado de cada cambio
5. 00_estrategia/PROMPT_DE_ARRANQUE.md — autorizaciones vigentes y trampas conocidas
6. PROMPT_DIRECCIÓN.md              — lo que el codirector me ha ido anotando. Desde
                                     C62 (05/10/2026) vive en 00_estrategia/privado/,
                                     el repositorio privado; si aún no se ha movido,
                                     en 00_estrategia/. Y su último fichero de tareas
7. 05_calendario/estado/          — ¿está el canal bien hoy? El fichero de nombre
                                     MÁS ALTO de esa carpeta, que es el de hoy. (Hasta el
                                     20/09 esto era ESTADO.md, que ya está congelado)
8. 08_comunicacion/               — novedades.md, que es tuyo, y el buzón entre agentes
9. 05_calendario/bitacora/         — los ficheros de los últimos siete días
10. 05_calendario/metricas.json     — dónde está el canal en la escalera
11. 05_calendario/bucle/resultados.json — cómo va el bucle (C60), brazo a brazo

Y antes de escribir nada en mi carpeta: comprueba que está al día con
origin/main (si no, que haga git pull). Desde C62 la dirección también
corre como rutina y sube sola; dos direcciones sobre ficheros viejos
acaban en un conflicto que tendría que resolver yo a mano.

`PROMPT_DIRECCIÓN.md` es del codirector y solo suyo: lo escribe él entre sesión y
sesión para que no se le olvide nada. **Se lee siempre y no se edita ni se borra
nunca.**

Y si necesitas el porqué de algo: 00_estrategia/DIAGNOSTICO.md.

Cómo trabajamos:

- Hablamos los lunes (datos y decisiones) y, mientras dure la fase de cambio,
  también los viernes (revisar lo que la planificación escribió el jueves).
  Fuera de eso, solo si algo se rompe, se pierde trabajo, se cruza una línea
  ética o un número se mueve fuerte.
- Escribes en los ficheros de mi carpeta con device_commit_files y yo hago el
  commit. Los ficheros de .github/workflows/ están protegidos contra escritura
  remota: si hay que crear uno, me lo mandas y lo creo yo a mano.
- Todo lo que necesites de mí va en 00_estrategia/tareas/tareas_codirector_FECHA.md,
  explicado de principio a fin y sin resumir, aunque sea algo que ya hayamos hecho
  antes. Nada de peticiones sueltas dentro de un resumen.
- Todo lo que merezca recordarse acaba en un documento antes de cerrar la
  conversación. Lo que no esté escrito, se pierde.
- Coste cero. Sin trabajo recurrente para mí. Nada a mi nombre ni con mi cara.
- La audiencia manda. Si seguimos por debajo de 100 visualizaciones por vídeo,
  el canal está abocado a desaparecer. Diferenciarnos está bien, pero es un
  medio, no el objetivo: hay que seguir mejorando el proceso entero y cambiar
  lo que haga falta por el camino.

Hoy quiero tratar:
```

---

## El cuaderno del codirector no llega a los agentes (anotado el 23/09/2026)

`PROMPT_DIRECCIÓN.md` está en `.gitignore`: lo leo yo al arrancar y **ninguna tarea programada lo
ve**, porque trabajan sobre un clon de GitHub. Por eso los avisos del codirector del 21 y el 22 sobre
los guiones no le llegaron a nadie hasta que hubo sesión, el 23 (trampa 37). Se lo he propuesto como
costumbre, no como obligación: **cuando vea un defecto en un guion que todavía no ha salido y no
haya sesión cerca, que lo escriba también en `08_comunicacion/novedades.md`**, que la revisión
diaria lee cada mañana y que desde el 23/09 puede actuar sobre los guiones de las 48 horas
siguientes (salvo los que haya escrito la dirección).

## Cuándo me escribe el codirector (decidido el 18/09/2026)

Lo preguntó él el 17/09: si conviene escribirme **antes** de la revisión diaria, para que me dé
tiempo a cambiarle el prompt, o **después**, para tener sus resultados.

**Después, siempre, y con un solo mensaje.** La revisión diaria escribe `ESTADO.md` y su
bitácora a las 11:30 de España, y eso es la mitad de lo que leo al arrancar. Escribiéndome
antes, arranco con la foto de ayer.

**Y el miedo que había detrás no se sostiene: cambiar el prompt de una tarea programada no tiene
prisa**, porque la tarea corre todos los días — un cambio escrito el viernes entra en la del
sábado. **Lo único con reloj es la producción**, que arranca a las 01:13 UTC (03:13 en España):
un arreglo que tenga que salir en el vídeo de mañana está en `origin/main` antes de esa hora.
Ese es el reloj, no el de la revisión.

## Una regla nueva: el nombre no va en el repositorio

Desde el 7 de septiembre, **el nombre propio del codirector no se escribe en
ningún fichero**. Se retiró de los 58 en los que aparecía —271 menciones— y de
los tres prompts del almacén. Se le llama **«el codirector»** o **«la
dirección»**. Sigue en el historial de git de antes de esa fecha; limpiarlo de
ahí es reescribir la historia y está por decidir.

## Autorizaciones vigentes

La regla 11.7 de `REGLAS.md` protege tres ficheros. Un permiso dado «en la
conversación» se pierde con la conversación, así que aquí queda por escrito
**qué está autorizado, desde cuándo y hasta dónde llega.**

### La autorización general, del 7 de septiembre de 2026

**Textual, del codirector:** *«Puedes autorizar la edición de montaje.py. También puedes
quitar todas las restricciones de edición en todos los ficheros siempre que seas tú, el
codirector, quien haga la edición (de los demás agentes no me fío).»*

Queda escrita aquí el 12/09, que es cuando se aplicó. Dice tres cosas y conviene no
confundirlas:

1. **Para la dirección —yo—, la regla 11.7 deja de aplicar.** Puedo editar cualquier
   fichero del repositorio sin pedir permiso fichero a fichero.
2. **Para los demás agentes no cambia absolutamente nada.** La revisión diaria, la
   planificación y las métricas siguen con la tabla de `PROPIEDAD_DE_FICHEROS.md` y con la
   regla 11.7 tal cual. La frase del codirector es explícita en el porqué, y el 21 de agosto
   le dio la razón.
3. **`.github/workflows/` queda protegido pase lo que pase**, también para mí. Esos ficheros
   se le mandan al codirector y los crea él a mano. No es una cuestión de confianza: es que
   ni siquiera se pueden escribir en remoto.

| Fichero | Estado | Alcance |
|---|---|---|
| **Todo el repositorio** | **Autorizado el 07/09/2026 · escrito el 12/09** | **Solo si quien edita es la dirección.** Para los demás agentes no cambia nada: siguen la regla 11.7 y `PROPIEDAD_DE_FICHEROS.md` |
| `03_produccion/pipeline/montaje.py` | **Autorizado el 07/09/2026, sin acotar** | Sustituye a la autorización estrecha del 28/08 (que cubría solo el manifiesto de subtítulos). **Con esto P9 —los tres sonidos— queda desbloqueado**, y entra en la semana del 21 según C25 |
| `03_produccion/pipeline/voz.py` | **Autorizado el 28/08/2026** | Abierto. Se pidió para C7 (dos voces), pero el codirector no lo acotó |
| `.github/workflows/` (entera) | **PROTEGIDA SIEMPRE, también para la dirección** | No se puede escribir en remoto. Se le manda el fichero al codirector y lo crea él. **Sin excepciones y sin fecha de caducidad** |
| `.github/workflows/producir.yml` | **Del codirector** | `GEMINI_API_KEY` ya está en «Sintetizar narración» (12/09). **Pendiente desde el 15/09:** una línea en el paso «Registrar lo publicado» para que suba también `03_produccion/cache_voz/` (C33.1). Ver `tareas/tareas_codirector_2026-09-15.md`, tarea 2 |
| `.github/workflows/voz_prueba.yml` | **Entregado el 04/09, lo crea el codirector a mano** | Prueba de C7. `workflow_dispatch` solo, no escribe en el repositorio |
| `.github/workflows/voz_adelantada.yml` | **Creado por el codirector el 14/09** (commit `8f9f778`) | C27. Corre de martes a viernes a las 09:00 UTC con `gemini-2.5-flash-preview-tts`. **Pendiente desde el 15/09 (tarde): que corra todos los días** (tarea 5 de `tareas_codirector_2026-09-15.md`). La copia documentada sigue en `07_pruebas/voz-adelantada-14-09/` |
| `docs/` (la web del proyecto) | **Del codirector y mío**, desde el 04/09 | Tres páginas estáticas que Google exige para publicar la aplicación de OAuth. **No es C10** |
| `03_produccion/sonidos/` | **Entregada el 07/09** | Tres acentos CC0 con su `attribution_texts.md`. Ya están |
| `01_bibliografia/data/semillas.json` | **Fuente de verdad de la bibliografía**, desde el 18/09 | `BIBLIOGRAFIA_CURADA.md` **se genera desde aquí** (`scripts/generar_md.py`). Una corrección que solo viva en el `.md` la borra la próxima regeneración. Lo comprueba `04_agentes/validar_bibliografia.py` |
| Cuentas de TikTok e Instagram de la marca | **Trámite abierto el 18/09** (C41) | Las dos APIs exigen auditoría/revisión de la app para publicar en abierto: días o semanas. Se empieza ya y **no se publica hasta que C38 haya dado su primera medida**. Ver `tareas/tareas_codirector_2026-09-18.md`, tarea 2 |
| `00_estrategia/PROMPT_DIRECCIÓN.md` | **SOLO DEL CODIRECTOR** | Es su cuaderno entre sesiones. **Se lee siempre, no se edita ni se borra nunca**, ni por mí |
| `08_comunicacion/novedades.md` | **SOLO DEL CODIRECTOR**, desde el 18/09 | Lo que quiera contarles a las tareas programadas. **Se lee, no se toca.** El resto de la carpeta es el buzón entre agentes: un fichero nuevo por mensaje, `AAAA-MM-DD-<quien>.md`. La dirección escribe ahí después de cada sesión desde el 21/09 (C43) |
| `05_calendario/ESTADO.md` | **CONGELADO el 21/09/2026** (C45) | El estado del canal vive en `05_calendario/estado/`, un fichero por día. El de hoy es el de nombre más alto. `ESTADO.md` se lee y no se escribe, igual que `MEJORAS.md` |
| `.github/workflows/voz_adelantada.yml` | **DESACTIVADO el 21/09** | C42: el formato largo está suspendido y este workflow se comía 9 de las 10 peticiones diarias del modelo que es el respaldo de voz de los Shorts. El fichero no se borra: se reactiva con un clic el día que el largo vuelva |
| `05_calendario/guiones/MDH-008.es.json` | **Escrito y congelado** | Su emisión está en `parrilla.json` → `_emisiones_suspendidas`. No se borra ni se edita |
| `02_marca/banco/banco.json` | **Generado el 21/09** desde `creditos_pixabay.csv` | Los tres campos que exige la regla 9 —licencia, autor, enlace— de las quince fotos. **C34 desbloqueado** |
| `05_calendario/guiones/MDS-023`, `024` y `025` | **Reescritos por la dirección el 23/09** (C48 y C48.1) | Nadie los edita, **tampoco la revisión diaria con la excepción de las 48 horas**: si ve algo, lo escribe en `revisiones/` y en su fichero de `estado/` |
| `05_calendario/parrilla.json` · emisión del **sábado 26** con `MDS-023` | **Red de seguridad de la dirección** (23/09) | Si el 23 se rehízo bien, ese día `cola.py` dice «nada que producir». Se puede borrar el lunes 28 |
| Claves de C50 (Pexels, Pixabay, Cloudflare) como secretos de GitHub | **Puestas por el codirector el 23/09** | `PEXELS_API_KEY`, `PIXABAY_API_KEY`, `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`. Las usa `visuales.yml`; `producir.yml` no las necesita |
| `.github/workflows/visuales.yml` | **Entregado el 23/09 (tarde)** en `00_estrategia/tareas/workflows_2026-09-23/`, **lo mueve el codirector a mano** (tarea 3) | C50 en producción: elige los planos de cada Short al cambiar un guion, a diario a las 16:37 UTC y a mano; sube manifiesto y hoja de contactos a `05_calendario/visuales/` |
| `.github/workflows/producir.yml` · paso «Traer el material visual (C50)» | **Entregado el 23/09 (tarde)**, el fichero entero en la misma carpeta, **lo sustituye el codirector** (tarea 3) | Baja los planos del manifiesto antes del render (regla 11.6). Nunca falla la producción |
| `.github/workflows/visual_prueba.yml` | **Se retira el 23/09 (tarde)**: lo borra el codirector en la tarea 3 | Era la prueba de C50; su código (`muestrario_visual.py` y el `visual.py` de prueba) ya no existe |
| `03_produccion/pipeline/visual.py` · `fondo_visual.py` | **De la dirección** (23/09, C50 en producción) | `visual.py`: resolver, traer, diagnóstico. `fondo_visual.py`: cortes y pista de fondo para `render.py`. **La revisión diaria no los toca sin encargo**; los planos se corrigen con `05_calendario/visuales/ajustes.json`, no con código |
| `05_calendario/visuales/` | **Del workflow `visuales.yml`**, salvo `ajustes.json` (revisión diaria) y `APAGADO` (el codirector y yo) | Ver su `LEEME.md`. `APAGADO` es el interruptor de C50: si existe, todo sale como antes |
| **Las tareas programadas entregan solas** (C53, C53.1, C53.2) | **Autorizado el 28/09/2026 · FUNCIONA desde el 30/09** | Tres **rutinas de Code** con el repositorio añadido, creadas por el codirector desde la web el 30/09 (revisión `trig_01K834hHyZ9ytxXXA3uP5y7Y`, planificación `trig_014hUCsYDz9mSVNKTFtQxZpR`, métricas `trig_01TmnPoPLXBx65x9Po4Y2PYh`); las tres de agosto, **apagadas, no borradas**. Primera entrega sola: `d234237`. **La dirección puede leerlas pero NO cambiarlas** (ni horario, ni modelo, ni texto: trampa 47): todo cambio va en el fichero de tareas del codirector. El `.tar.gz` queda solo como plan B |
| `.github/workflows/` · excepción del 28/09/2026 | **Autorizada por el codirector esa vez, pero GitHub la rechazó**: el token no tiene permiso para workflows | `entregas.yml` (nuevo), `visuales.yml` y `vista.yml` (solo `main`) y `metricas.yml` (dos intentos más) se le entregaron en `00_estrategia/tareas/workflows_2026-09-28/`. **La regla sigue, y ahora además la sostiene el token** |
| `04_agentes/entregar.py` · `.github/workflows/entregas.yml` | **De la dirección** (28/09, C53) | Son la tabla de `PROPIEDAD_DE_FICHEROS.md` en código. Ninguna tarea los toca: `entregar.py` se excluye a sí mismo |
| Regla 7.1 · la persona sintética | **Autorizada por el codirector el 23/09/2026**, escrita el 28/09 | Sí a Kaggle, con las cinco condiciones de `REGLAS.md` 7.1. No entra sin muestrario (C51.2) |
| Kaggle de la marca · secretos `KAGGLE_USERNAME` y `KAGGLE_KEY` | **Puestos por el codirector el 29-30/09** | El token es del formato nuevo (una sola cadena): el workflow que lo use lo pasa como `KAGGLE_API_TOKEN: ${{ secrets.KAGGLE_KEY }}`. El usuario, `mecanicadelhumor`, sirve para el nombre de los cuadernos. Licencias de cada pieza del presentador: `07_pruebas/presentador-2026-10/LICENCIAS.md` (C51.3) |
| `04_agentes/entregar.py` · C53.2 (30/09) | **De la dirección** | Mide lo entregado contra `origin/main` y borra en `--aplicar` las ramas de sesión ya enteras en `main`. **Nadie abre nunca un PR de una rama de sesión**: se saltaría la tabla de propiedad |
| `03_produccion/pipeline/montaje.py` · C58 (02/10/2026) | **Decisión del codirector en la sesión** | En los **Shorts**, 0,1 s de colchón y ningún fundido de entrada (era 0,6 s y fundido desde negro, del 18/08). En los largos, como siempre. El colchón usado se apunta en `montaje.json` y `qa.py` mide contra él |
| **C60 · el bucle** (05/10/2026): `05_calendario/bucle/ciclos.json` e `hipotesis.json`, y `04_agentes/bucle.py` | **De la dirección** | La planificación lee `ciclos.json` y aplica su `orden`; `resultados.json` y `metricas_diarias.json` los escribe `metricas.yml`. **Decisión del codirector en la sesión: 7 Shorts a la semana desde el 12/10 y 14 desde el 19/10 (si C36 pasa)** |
| `01_bibliografia/` (05/10/2026) | **Pasa de la revisión diaria a la planificación** | La revisión avisa en `05_calendario/revisiones/bibliografia.md`. `entregar.py` ya lo aplica |
| **C62 · la dirección en diferido** (05/10/2026) | **Autorizada por el codirector en la sesión**, con repositorio privado | Rutina «Dirección», Opus 5.5, lunes y jueves 13:07 UTC y «Run now». Instrucciones: `00_estrategia/tareas/direccion.md`. Entrega con `entregar.py --tarea direccion` (todo salvo workflows, el cuaderno, `novedades.md` y lo de Actions). El cuaderno y las tareas, en `mecanicadelhumor/direccion` (privado), clonado en `00_estrategia/privado/` |
| `.github/workflows/metricas.yml` · versión del 05/10/2026 | **Entregada** en `00_estrategia/tareas/workflows_2026-10-05/`, **la mueve el codirector** | Lectura diaria ligera (C47/C60), `bucle.py` detrás, y despierta a la rutina de métricas por su disparador de API (secreto `RUTINA_METRICAS_TOKEN`) |
| `03_produccion/pipeline/render.py` · `escena.html` · C59 (02/10/2026) | **Decisión del codirector en la sesión** | El remate de marca dice «Síguenos» y «un mecanismo nuevo de lunes a viernes», **siempre la misma frase y sin voz**. No se convierte en una frase por Short |
| `04_agentes/metricas.py --solo-registro` · C57 (02/10/2026) | **De la dirección** | Publica en YouTube **un comentario del canal por Short**: la `pregunta_al_espectador` de su publicación, cuando el vídeo ya es público, una sola vez. Es lo único que el sistema escribe en los comentarios. **Nunca responde a nadie** (regla 7) |

**Y la consecuencia práctica de la autorización general, que es la que importa:** desde el
12/09 escribo directamente en la carpeta del codirector con `device_commit_files` los
ficheros que antes le entregaba en un paquete. Él sigue haciendo el `commit` y el `push`,
que es lo único que no puedo hacer yo.

**Y una cosa que ya no hace falta recordar de memoria:** cómo se saca el token de
YouTube y por qué caducaba está en **`00_estrategia/TOKEN_DE_YOUTUBE.md`**, con
la ruta exacta de la consola, el script que ya existía
(`04_agentes/obtener_token_youtube.py`) y la tabla de qué mirar si el canal deja
de publicar.

Otra decisión de propiedad, del 28/08: `01_bibliografia/BIBLIOGRAFIA_CURADA.md`
pasa a ser de la **revisión diaria**, que antes no tenía dueño y por eso
arrastraba defectos. Solo puede añadir lo que verifique contra la fuente.

---

## Las trampas en las que ya se ha caído

No son anécdotas: cada una costó tiempo o un vídeo, y todas se repiten solas si nadie las
tiene delante. Son cincuenta y cuatro a 05/10/2026, y la lista crece porque se lee.

**1. Cada documento daba por supuesto que el movimiento lo ponía otro.**
Los subtítulos quemados se retiraron el 20/08; la respiración de zoom ya estaba
descartada. Ninguno de los dos documentos que las mencionaban decía que eran las
**únicas** fuentes de movimiento, así que durante ocho días el 85 % de cada
Short fue un fotograma congelado y nadie lo relacionó — pese a que el comentario
de `voz.py` lo decía con esas palabras: «*un vídeo sin ellos se percibe como un
pase de diapositivas*».
→ Cuando retires algo, busca qué dependía de ello. Cuando un documento diga que
otra pieza se encarga de X, comprueba que esa pieza sigue existiendo.

**2. Una restricción que nadie volvió a comprobar bloqueó C6 una semana.**
Toda la arquitectura de captura se diseñó para ahorrar minutos de render. El
repositorio es **público**, y los minutos de Actions en repos públicos son
ilimitados. El límite real es el `timeout-minutes: 150` del job, y un Short
entero a 30 fps son 7,8 minutos medidos.
→ Antes de diseñar alrededor de una restricción, comprueba que sigue siendo
cierta. Las de coste, sobre todo.

**3. «Mismo guion y mismo t, mismo píxel» nunca ha sido literalmente cierto.**
Medido el 28/08: renderizando **el mismo fichero sin tocar, dos veces**, difieren
8 de 14 fotogramas, siempre en los mismos ~368 píxeles de 254.016 (0,14 %): una
línea de 1 px del marco que Chromium rasteriza distinto según cuándo promociona
la capa. El delta máximo es 50 sobre 255, en un fondo casi negro. **No se ve.**
→ El suelo de ruido es ~0,06 % de los píxeles. Si comparas dos versiones y la
diferencia está por debajo de eso, no has cambiado nada. Si comparas contra cero,
vas a perseguir fantasmas. La regla 11.5 sigue valiendo para lo que fue escrita
—nada de `Math.random()`, nada de la hora del sistema— pero no como igualdad
byte a byte.

**4. `registro_publicaciones.json` guardaba el estado del momento de la subida.**
En modo `revision` eso es siempre `private`, y nadie lo actualizaba al publicar.
Consecuencia: `metricas.py` excluía los cinco Shorts y solo miraba `MDH-001`, y
la revisión diaria hablaba de vídeos «en privado» que llevaban días publicados.
Arreglado el 28/08 — el estado se le pregunta a YouTube y se corrige el registro.
→ Un campo que se escribe una vez y describe algo que cambia después, miente.

---

**5. Un vídeo puede quedarse escondido para siempre por un campo que falta.**
MDH-004 se produjo el sábado 29 sin incidencias, se subió a la hora y **no se
publicó nunca**: su emisión en `parrilla.json` llevaba `modo: revision`, así que
`cola.py` lo subió `private` **sin `publicar_en`**. Nadie lo detectó — la revisión
diaria del domingo escribió, con toda lógica, «su hora de publicación ya pasó, así
que está publicado», que es cierto en modo automático y falso en modo revisión.
El codirector lo encontró dos días después mirando Studio.
→ El defecto de fondo era el defecto por defecto: `modo = emision.get("modo",
"revision")`. Un olvido fallaba hacia el silencio en vez de hacia publicar.
Cuando escribas un valor por defecto, pregúntate hacia dónde falla el olvido.

**6. `qa.py` corre DESPUÉS de publicar.** En `producir.yml` el paso «Expediente de
calidad» va detrás del de «Subir a YouTube», con `if: !cancelled()`. Es un informe,
no una barrera. Se leyó durante semanas como si fuera un control de calidad previo.
→ Con la publicación automática, el único par de ojos antes del público es la
revisión diaria de las 11:30, dentro de la ventana de ~15 h entre subida y
publicación. Y no puede cancelar nada: solo avisar en `ESTADO.md`.

**7. «No puedo arreglarlo» se convirtió en «no lo digo».**
El 3 de septiembre la revisión diaria encontró, siete horas y media antes de
publicarse, que el Short del día tenía la palabra «generosos» cortada contra el
borde. Lo describió con precisión — y **no lo marcó como incidencia**, razonando
que no podía cancelar la publicación. El codirector lo descubrió ya publicado.
→ Un agente que no puede arreglar algo tiene **más** motivo para avisar, no
menos. Y sobre todo: no le pidas a un revisor que vea a ojo lo que una condición
booleana puede comprobar. Un texto que no cabe en su caja es
`scrollWidth > clientWidth`. Ver C21.

**8. El límite que importaba no era el que mirábamos.**
`prueba_voz.py` murió por cuota en su primer intento real. El panel de Gemini
decía 62 de 10.000 tokens por minuto y 4 de 10 peticiones al día — todo verde
menos una línea: **3 de 3 peticiones por minuto**. El script pedía una llamada
por escena, siete seguidas. El coste no estaba en el tamaño de lo que pedíamos
sino en **cuántas veces** lo pedíamos, y esa es la dimensión que no se estaba
mirando.
→ Cuando algo falla por cuota, mira **todas** las dimensiones del límite antes
de concluir que no cabe. Y cuando el límite es de frecuencia y no de volumen,
casi siempre se arregla pidiendo menos veces, no pidiendo menos cosa.

**9. Un arreglo puede abrir un agujero en otra regla.**
La barrera de C21 hace lo que debía —el 04/09 encontró dos Shorts de la semana
siguiente que no renderizan— pero convirtió un defecto que podía esperar al
jueves en uno que deja sin vídeo el martes. Y quien aplica las notas de
`revisiones/` es la planificación del jueves, o sea **después**. La propiedad de
ficheros está pensada para defectos de contenido; con uno de render llega tarde.
→ Cuando pongas una comprobación que puede **parar** algo, mira qué circuito
resolvía antes ese problema y si sigue llegando a tiempo. La salida no fue
cambiar la propiedad —eso reabre el desastre del 21 de agosto— sino quitar el
defecto de la capa donde estaba (C21.1).

**10. La escalera medía palabras y lo que desbordaba era el ancho.**
`MDS-013` se sale del lienzo con **dos palabras**, porque con cinco o menos
`escena.html` sube la fuente a 150 px. Durante semanas se habló de este fallo
como «texto demasiado largo» y se iba a arreglar añadiendo `.cifra` a la misma
escalera — es decir, repitiendo el error con otro selector.
→ Si mides un sustituto de lo que te importa (número de palabras) en vez de lo
que te importa (que quepa), el fallo vuelve con otra cara. Mide lo que importa:
encoge hasta que quepa.

**11. Un arreglo que se commitea por la mañana NO llega al vídeo de ese día.**
El domingo 6 la revisión diaria arregló el solape del pie con el personaje. El
lunes 7 el codirector lo commiteó a las **08:03**. Pero MDS-011 se había renderizado
y subido a las **01:32 UTC**, seis horas y media antes — así que el vídeo que
el codirector vio publicado ese lunes seguía teniendo el defecto ya arreglado, y
parecía que el arreglo no había funcionado.
→ La producción arranca a las **01:13 UTC (03:13 en España)**, con reintentos a
las 04:47 y 08:23. **Un arreglo tiene que estar en `origin/main` antes de las
03:13 de la madrugada del día en que quieres verlo.** Commiteado por la mañana,
entra en el vídeo del día siguiente. No es un fallo: es el reloj, y hay que
tenerlo delante antes de concluir que algo no funcionó.

**12. Un prompt puede documentar una marca sin decir dónde va.**
Los dos prompts de guionista explicaban desde el 28/08 que `*así*` pinta ámbar y
`_así_` pinta cian, y **ninguno decía nunca en qué campos**. El guionista lo
aplicó a `narracion`, que es el único campo que no se pinta y el único que se
oye: MDS-011 se publicó diciendo «guion bajo pensamiento divergente guion bajo».
→ Cuando documentes una sintaxis, documenta **su ámbito** en la misma frase. Una
regla sin ámbito se aplica donde no toca, y la culpa no es de quien la aplica.

**13. Una regla que nombra algo que no existe deja fuera algo que sí.**
La regla 14.3 decía que `duda` y `no_le_hace_gracia` se leen como cara triste.
`no_le_hace_gracia` **no existe** —las expresiones son `neutra`, `duda`,
`entiende`, `no`, `rie`, `piensa`— y la que faltaba, `piensa`, comparte la boca
torcida con `duda`. La regla protegía contra una cara imaginaria y dejaba pasar
una real.
→ Cuando escribas una regla que enumera valores, **enuméralos contra el código**,
no contra lo que recuerdas que había.

**14. Dos piezas que se pasan un fichero necesitan margen, y el margen se cuenta
desde el ÚLTIMO reintento.** `metricas.yml` escribe `metricas.json` a las 05:19 y
reintenta a las 08:37 UTC; la tarea que lo lee corría a las 07:00 — **entre los
dos**. El 31 de agosto funcionó porque el primer intento fue puntual; el 7 de
septiembre se retrasó y el analista leyó la foto de la semana anterior. El propio
`producir.yml` documenta que los retrasos de Actions van de 2 h 38 a 6 h: un
margen de 1 h 41 era menor que el retraso típico.
→ Cuando una pieza escriba y otra lea, cuenta el margen **desde el último
reintento del que escribe**, no desde el primero. Y quien lee tiene que saber
mirar la fecha de lo que lee: un lector que no distingue «no hay datos» de «los
datos son viejos» convierte un retraso en una semana perdida.

**15. Medir una escena quieta miente cuando la escena se mueve.**
El arreglo del solape del 6 de septiembre se verificó en el punto de reposo:
48 px de hueco, caso cerrado. **En movimiento el hueco real era de 7 px** y el
vídeo salió publicado con la cara pegada al texto. Los 41 px se los comían el
`translateY` de entrada del personaje (26 px), su respiración (±5 px) y el zoom
del 2,2 % de `#escena` — ninguno de los tres existe en un fotograma quieto.
→ En `escena.html`, cualquier comprobación de geometría se hace llamando a
`pintar(t)` en **veinte instantes repartidos por la escena**, quedándose con el
peor caso. Y en general: si lo que compruebas se mueve, compruébalo moviéndose.

**16. Un permiso que falta no rompe donde se concede.**
El token de YouTube se regeneró el 1 de septiembre **sin
`yt-analytics.readonly`**. Subía vídeos perfectamente, así que pareció bueno, y
la avería salió **seis días después**, en la lectura semanal de métricas, con un
`invalid_scope: Bad Request` que no nombra el ámbito que falta. En la pantalla de
consentimiento de Google cada permiso es una casilla y es fácil dejarse una.
→ Cuando emitas una credencial, **compara lo concedido con lo pedido y falla ahí
mismo**. `obtener_token_youtube.py` ya lo hace: antes listaba los ámbitos y
seguía; ahora rechaza el token y dice qué casilla faltó.

**17. Publicar no es verificar — y el botón equivocado te devuelve al principio.**
Tres días persiguiendo el «Estado de verificación» de la pantalla de
consentimiento, que es la verificación **de marca** y no hace falta para nada de
lo que necesitamos. La propiedad del dominio sí estaba verificada. Y el aviso de
que «no hay páginas AMP» venía de Search Console y no tiene relación ninguna.
→ Lo único que hay que pulsar es *Audiencia* → **«Publicar aplicación»**.
«Corregí los problemas» manda la aplicación **a revisión**, que es justo lo que
no queremos. Cuando un trámite se resista, comprueba primero que es el trámite.

**18. Documenté una sintaxis y no documenté en qué paso iba — otra vez.**
La trampa 12 decía, en noviembre de la semana pasada: *cuando documentes una
sintaxis, documenta su ámbito en la misma frase*. El 12 de septiembre le escribí
al codirector una tarea de diez minutos para exponer `GEMINI_API_KEY` en
`producir.yml`: *«busca `secrets.`, copia una de esas líneas entera, pégala justo
debajo y cambia los dos nombres»*. Todo correcto y nada dice **en qué paso**. La
primera aparición de `secrets.` en ese fichero está en «Subir a YouTube», así que
ahí la pegó — y el que necesita la clave es «Sintetizar narración», que es el que
llama a `voz.py`. Instrucción impecable, resultado inservible, y la culpa no es de
quien la siguió.
→ **Una instrucción de «copia esta línea» sin decir dónde es media instrucción.** Y
la prueba de que está completa no es releerla: es preguntarse qué haría alguien que
solo tiene el fichero delante y no sabe para qué sirve.

**19. Una comprobación puede estar mirando el sitio equivocado y parecer que funciona.**
La barrera de C21 llevaba `"svg text"` en su lista de selectores desde el 4 de
septiembre. Parecía cubierto. No lo estaba: `medir()` solo calcula desbordamiento
cuando el elemento es `HTMLElement`, y un `<text>` de SVG no lo es, así que de esos
elementos solo se comprobaba el rectángulo **contra el lienzo** — es decir, se
detectaba que un texto se saliera de la *pantalla*, nunca que se saliera de *su
caja*. Y las cajas del diagrama están en el centro de la pantalla. La única
situación que la barrera podía cazar ahí era la imposible. Resultado: 0 problemas
sobre las 40 escenas de MDH-006 y un vídeo publicado con el texto fuera del
rectángulo en el segundo 2:34.
→ **Que un selector esté en la lista no significa que se esté midiendo.** Una
comprobación que nunca ha dado positivo sobre una familia entera de casos no es una
comprobación probada: es una comprobación sin probar. La forma de saberlo es
buscarle un caso que **tenga** que fallar y ver si falla.

**20. Un mínimo escrito como suelo se usa como techo.**
`guionista.md` pedía «mínimo dos risas por episodio largo, una antes del segundo
quince». MDH-006 trae exactamente dos, las dos en los primeros veinte segundos, y
después cuatro minutos y medio sin un solo intento. Cumple la regla al pie de la
letra y no tiene gracia, que es justo lo que la regla existía para evitar.
→ **Cuando una regla cuente cosas, pregúntate qué pasa si alguien pone el mínimo
exacto en el peor sitio posible.** Si la respuesta es «entonces la regla no sirve
de nada», lo que hay que medir no es la cantidad: es la distancia.

**21. Una instrucción de tono aplicada a todas las escenas por igual es un tic, no un
tono.** La dirección de actor de Gemini era **una constante de doce líneas** pegada delante
de las seis escenas de cada Short, y decía «cuéntala con la entonación de quien cuenta algo
que le hace gracia». Iba delante del planteamiento, del dato, de la lista y del «y aquí
falla: solo sabemos cómo suena». Resultado: el primer Short con voz nueva se ríe de
principio a fin, y ningún guion llevaba una sola risa escrita — comprobado sobre las 47
escenas de los ocho Shorts del repositorio.
→ **Lo que se le pide a un modelo generativo hay que pedírselo por unidad de trabajo, no por
lote.** Y si una instrucción vale igual para todas las escenas, sospecha: casi siempre es
que no dice nada útil sobre ninguna.

**22. Una tubería de seis llamadas independientes produce seis piezas independientes.**
Cada escena es una llamada distinta a la API, así que el modelo le pone a cada fragmento su
entonación de arranque y su punto final, sin saber que hay cinco escenas más. Encima le
metemos nosotros hasta 1,35 s de silencio detrás. Un punto final, un silencio y otro
principio **no es una pausa dramática: es un corte** — y eso es lo que se oyó como «resumido
sin puntos en común» en un guion que en papel tiene hilo de sobra.
→ **Cuando trocees un trabajo en llamadas, el contexto que pierdes en el troceo hay que
devolvérselo a mano.** Ahora cada escena sabe de dónde viene y si tiene que cerrar o quedar
suspendida (C33).

**23. Descarté una vía citando una regla que no decía eso, y la regla era mía.** C25
descartó los bancos de imágenes con un «(regla 9 y no son de marca)». La regla 9 prohíbe
material **sin licencia** y habla de clips de cómicos y películas por el riesgo de strike;
una foto CC0 tiene licencia. Estiré una regla propia hasta que dijera lo que me convenía, y
eso cerró durante una semana la vía que la dirección señala como cuestión de supervivencia.
→ Es la trampa 2 —comprobar que la restricción dice lo que crees— cometida **sobre un
documento propio**, que es donde menos se comprueba. **Antes de descartar algo citando una
regla, vuelve a leer la regla.**

**24. Un cambio en la clave de una caché rompe en silencio a quien comparte esa caché.**
C33 metió la dirección de actor en la clave de `_cache_voz_ruta()`, que es lo correcto. Pero
`voz_precache.py` —escrito ayer, para el episodio largo— llamaba a `_gemini_pcm()` con el
texto pelado: después de C33 habría precacheado toda la semana **sin dirigir y con una clave
que `voz.py` nunca habría buscado.** Una semana de cuota gastada para nada, sin un solo
error en el log.
→ Es la trampa 1 otra vez. Cuando cambies **lo que entra en una clave de caché**, busca a
todos los que escriben en ese directorio, no solo a los que leen.

**25. Una regla escrita para un formato no protege al otro.** El 7 de septiembre el codirector
dijo que un vídeo con dos voces era una chapuza, y la regla se escribió **para el episodio
largo**. El respaldo de los Shorts seguía siendo escena a escena, y `MDS-017` salió el 15 con
tres escenas en Gemini y tres en `edge-tts`. Nadie lo decidió: lo decidió la granularidad del
respaldo.
→ **El respaldo tiene que ser del mismo tamaño que la cosa que no se puede mezclar.** Si lo que
tiene que ser homogéneo es el vídeo, el respaldo es por vídeo. Y cuando escribas una regla
pensando en un caso, pregúntate a qué otros casos les pasa lo mismo.

**26. Un mensaje de error se busca por lo que dice, no por lo que crees que dice.** `voz.py`
reconocía la cuota diaria de Gemini buscando «per day» o «perday». Google escribe
«`per_model_per_day`». La condición no se cumplió nunca, y con la cuota agotada se siguió
llamando a la API escena tras escena. Era la trampa 8 —mirar todas las dimensiones del límite—
en el lado del código.
→ Compara siempre **normalizado** (sin espacios, guiones ni guiones bajos, en minúsculas) y, si
puedes, contra un mensaje real copiado del log, no contra uno imaginado.

**27. «Validado y sin hallazgos» no significa «bien escrito».** El lunes 14 escribí que los
guiones de la semana no se tocaban porque estaban validados. El martes el codirector vio uno y
no se podía seguir, y al leer los otros tres fallaban igual, uno con un dato al revés. El
validador mide lo que se puede medir; las tres pruebas de cosido las tiene que pasar alguien
leyendo.
→ Cuando un guion anterior a un arreglo de guionista va a publicarse, **se lee contra el
arreglo**, no contra el validador.

**28. Una ficha de una línea invita a inventarse el resultado.** La ficha `G05` decía «cuándo
ayuda y cuándo distrae del mensaje», y el guion de `MDS-019` completó eso con «mejora cómo te
cae quien lo usa». El resumen del artículo dice lo contrario. La verificación lo dio por bueno
porque comparaba contra la ficha, y la ficha no decía nada. De paso, tres fichas tenían el
título, la revista o el DOI mal.
→ **Un resultado se copia del resumen, no se deduce de la ficha.** Regla nueva en el prompt de
la planificación desde el 15/09.

**29. Una librería puede reintentar por ti, y no avisa.** `google-genai` 2.x reintenta hasta
cuatro veces en tres segundos cada 429, cada 5xx y cada corte de conexión. Con un límite de
tres peticiones por minuto y diez al día, cada fallo nuestro eran hasta cuatro peticiones:
eso agotaba la cuota y fabricaba los 429 «por minuto» que no cuadraban con nuestras esperas.
Se vio por la cuenta, no por el error: 2.5 se agotó con cuatro escenas hechas.
→ **Cuando una cuota no cuadra, cuenta las peticiones en el cable, no las llamadas en tu
código.** Y cuando la cuota es pequeña, quita los reintentos de la librería y decídelos tú.

**30. Un rechazo también es una petición.** Seis 400 de la dirección de actor v1 se comieron
seis de las diez peticiones diarias de 3.1. Reintentar lo mismo que se acaba de rechazar no es
insistir: es pagar dos veces por el mismo no.
→ Ante un rechazo, **cambia la petición** (la dirección mínima), no la repitas.

**31. Un máximo escrito como techo se usa como objetivo.** Es la trampa 20 por el otro lado. La
regla 20 decía que un mínimo escrito como suelo se usa como techo; esto es lo simétrico y salió
igual de caro. `validar_guion.py` ponía el techo del Short en 55 s y cada serie declaraba su
propia duración —30, 35, 40 o 45— desde agosto. **Los veinticinco Shorts del canal tienen entre
88 y 120 palabras, media 108**, dijera lo que dijera su serie: nadie escribía a la serie, todos
escribían al techo. Lo que rellenaba la diferencia era explicación entre el remate y el cierre,
que es lo que el codirector describió dos días seguidos como «forzado entre el nudo y el
desenlace».
→ **Cuando pongas un máximo, pregúntate qué pasa si todo el mundo escribe justo por debajo.** Si
la respuesta es «entonces el número de al lado no sirve de nada», el que hay que hacer cumplir
es el de al lado.

**32. Una regla se corrigió a medias y la otra mitad estuvo rota seis días.** El 12/09 la regla
13 dejó de contar risas y pasó a medir distancias — **solo para el episodio largo**. El Short se
quedó con «una, y va primero», que es el mismo suelo-usado-como-techo que se acababa de
arreglar. Es la trampa 25 (una regla escrita para un formato no protege al otro) cometida sobre
la corrección de otra trampa.
→ Cuando corrijas una regla que cuenta cosas, **haz la lista de los formatos a los que se
aplica y recórrela entera** antes de dar la corrección por hecha.

**33. Un fichero generado que se edita a mano miente hasta el día en que se vuelve a generar.**
`BIBLIOGRAFIA_CURADA.md` lo produce `scripts/generar_md.py` desde `data/semillas.json`, y su
cabecera lo dice en la línea cuatro. Nadie lo había respetado nunca: el 18/09 había **cinco
fichas corregidas solo en el `.md`** —`C05`, `E02`, `F04`, `F05` y `G03`—, dos de ellas
arregladas esa misma mañana. Una regeneración las borraba las cinco sin un error y sin un aviso.
→ Es la trampa 4 con otra cara. **Antes de corregir un fichero, mira si lo escribe alguien.** Y
si un fichero dice en su cabecera cómo hay que editarlo, esa frase es una comprobación que falta,
no una nota de estilo: escríbela (`04_agentes/validar_bibliografia.py`).

**34. Una comprobación que no se puede ejecutar es una intención.** El arreglo natural de la
trampa 33 era resolver cada DOI contra Crossref y comparar el título. **El proxy de egreso de
estos contenedores rechaza `api.crossref.org`** (comprobado el 18/09), así que ese script
habría quedado escrito y muerto. Lo que sí corre sin red es comparar el `.md` contra el JSON, y
eso es lo que se ha escrito; la parte que necesita internet vive en el prompt de la revisión
diaria, que tiene `WebFetch` y ya la hizo a mano ese mismo día.
→ **Antes de escribir una comprobación, comprueba que su entorno puede ejecutarla.** Es la
trampa 2 aplicada a la red en vez de al coste.

**35. Una cuota «propia» deja de serlo el día en que otro la usa, y nadie vuelve a leer la
cabecera.** `voz_precache.py` dice desde el 14/09, en su cabecera: *«cuota propia, nunca la de
los Shorts (C7)»*. Era verdad ese día. **El 15 de septiembre C33.1 escribió
`MODELOS_CORTO = (MODELO_GEMINI, MODELO_GEMINI_LARGO)`** y con esa línea
`gemini-2.5-flash-preview-tts` pasó a ser el **peldaño (b) del respaldo de voz de los Shorts**.
Desde entonces, `voz_adelantada.yml` gastaba **cada día 9 de las 10 peticiones** de ese modelo
precacheando el episodio largo. Un Short necesita seis. **Durante seis días el respaldo de voz
de los Shorts existió en el código y no existió en la práctica**, y no dio ni un error: solo
Shorts que no conseguían voz. `MDS-017` hizo 0 visualizaciones.
→ Es la trampa 1 y la 24 en el mismo sitio. **Un recurso compartido —una cuota, una caché, un
fichero— tiene dueños, y la frase que dice quién lo usa caduca sin avisar.** Cuando añadas un
consumidor a un recurso, ve a leer lo que el recurso dice de sí mismo y corrígelo ahí mismo. Si
la cabecera de un fichero afirma un reparto, esa afirmación es una comprobación que falta.

**36. La regla que arregló el desastre no se aplicó al fichero de al lado, y lo creó el mismo
agente diez días después.** El 21 de agosto, después de que la revisión diaria borrara 188
líneas de bitácora de la planificación, nació la regla que sostiene todo el reparto de ficheros
de este proyecto: **un fichero nuevo no puede pisar nada**, y `MEJORAS.md` se congeló. **El 31 de
agosto se le dio a esa misma revisión diaria un fichero más, `ESTADO.md`, que se reescribe entero
todos los días** — exactamente la figura que la regla existía para eliminar. La factura llegó el
fin de semana del 19 y 20 de septiembre: dos entregas sin aplicar, dos `ESTADO.md` distintos del
mismo fichero, y el codirector guardando uno con sufijo `_old` para no perderlo.
→ Trampa 25 cometida sobre la regla madre de todas. **Cuando arregles algo con una regla
estructural, haz la lista de todo lo que tiene esa misma forma y recórrela entera** — y vuelve a
recorrerla cada vez que crees un fichero nuevo para un agente que ya tiene uno.

**37. Congelé lo que había que arreglar para poder medirlo.** El 21/09 escribí que la semana del 21
no se tocaba —ni voz, ni guion, ni presentación— porque era la primera medida limpia de C38. El
codirector avisó el 21 y el 22 en su cuaderno de que los guiones no se entendían; la revisión
diaria tenía prohibido tocarlos; y yo no leo el cuaderno hasta que hay sesión. Tres Shorts sin hilo
publicados con tres avisos delante.
→ **Una congelación para medir necesita una salida para lo que está roto.** Si el codirector señala
un defecto, se arregla aunque se pierda la medida: medir con piezas que no funcionan no mide nada.

**38. Recortar para caber se lleva primero las juntas, y quien recorta no lo nota.** El 18/09
reescribí cinco Shorts a la duración de su serie con una restricción que me pareció rigurosa: *no
entra ni una afirmación nueva, solo se quita y se recoloca*. Lo que se fue primero fueron los «por
eso» y los «pero», que son las únicas palabras que no llevan un dato. `MDS-023` pasó de 111 a 68
palabras con todas sus afirmaciones intactas y sin historia. Y yo lo leí y me pareció bien, porque
sabía lo que quería decir cada frase.
→ **Si hay que recortar, se quitan escenas enteras, nunca las juntas. Y quien escribe o recorta un
guion no puede ser quien comprueba si se entiende**: por eso existe la lectura en frío (C48), que
la hace un lector que no conoce la historia.

**39. Un ejemplo en un prompt se convierte en plantilla.** El guionista ponía de ejemplo de cierre
honesto «y esto se rompe cuando…», y los 25 Shorts publicados hasta el 22/09 cierran con «y aquí
falla». Con las aperturas pasó lo mismo: 23 de 25 empiezan por «mi madre», «mi jefe», «en mi
familia»… El codirector lo vio al primer vistazo; ninguna comprobación lo miraba.
→ **Cuando escribas un ejemplo en un prompt, pon tres distintos o ninguno, y di que es un ejemplo de
contenido, no de forma.** Y todo lo que se repite en todos los vídeos es sospechoso de tic (trampa
21), sobre todo si es una frase.

**40. En la carpeta del codirector, `git status` deja un `.git/index.lock` que no puedo borrar.** Me
ha pasado el 21 y el 23 de septiembre. Desde el puente de dispositivos puedo crear y renombrar
ficheros en su carpeta, pero no borrarlos, y `git status` refresca el índice creando un bloqueo que
luego no consigue quitar. El siguiente `git add` del codirector falla con *«index.lock: File
exists»*. Lo mismo con cualquier fichero temporal que cree ahí.
→ **En su carpeta, git solo con `git --no-optional-locks` y nunca un comando que escriba.** Para
leer `origin/main`, un clon aparte fuera de su carpeta (`git clone --filter=blob:none
--no-checkout https://github.com/mecanicadelhumor/mecanica-del-humor.git ~/remoto`: desde el
dispositivo, GitHub por HTTPS funciona, y su API también, incluidas las ejecuciones de Actions).
Y ningún fichero temporal dentro de `C:\MisProyectos\Humor`: los scripts de trabajo, en `$HOME`.
Si se escapa uno, se mueve a `_to_delete/`, que está en `.gitignore`.

**41. Un `except` que convierte un fallo en «no hay resultado» borra la única pista.** El 23/09 la
variante C de la prueba de imagen no sacó ni una imagen de Cloudflare en 21 intentos, y no hubo forma
de saber por qué: `visual.py` capturaba la excepción, escribía «sin_imagen» y seguía, y el registro
de Actions no se puede leer sin permisos de administrador. El codirector vio «todo azul, como hasta
hoy» y no supo si era un fallo o una decisión.
→ **Todo lo que habla con un servicio de fuera guarda lo que el servicio contestó** (el código y el
cuerpo de la respuesta), y lo deja donde se lee sin credenciales: en el repositorio o en el resumen
de la ejecución, no solo en el registro. Y una prueba que puede fallar en silencio dice en su propio
resultado que ha fallado.

**42. El arreglo de la trampa 41 la volvió a crear, dos días después.** El 25/09 `caras()` dejó de
tumbar los planos cuando OpenCV 5.0 —sin versión fijada— no traía `CascadeClassifier`, y lo hizo
devolviendo `[]`: «no hay caras». Del 24 al 28/09, **ni una cara en 51 planos llenos de gente**, sin
un aviso, y el 28 salió `MDS-026` con el texto encima de una cara.
→ **Un detector que no está no dice «no hay»: dice «no lo sé», y lo dice donde se lee** (desde el
28/09, `diagnostico.json`, el manifiesto y la hoja de contactos). Y una dependencia sin versión
fijada es un cambio que entra solo un día cualquiera: o se fija, o se usa lo que sobrevive a la
siguiente versión (desde el 28/09 el detector es YuNet, que la 5 sí trae).

**43. Un cron de GitHub puede llegar con seis horas de retraso, o no llegar.** El lunes 28, a las
10:57 UTC, «Leer métricas» no había corrido ninguno de sus dos intentos (05:19 y 08:37): no habían
fallado, no existían. Uno apareció a las 11:47 UTC; el otro, nunca. La tarea de las 10:00 leyó la
foto del 21 y el punto de control se quedó sin datos hasta que se lanzó a mano. Y de propina, la
pasada tardía machacó la lectura buena de la mañana con una peor (sin la curva de `MDS-022`).
→ **Dos intentos del mismo cron no son dos caminos.** Quien depende de un workflow programado mira
la fecha de lo que lee, y tiene que haber otro camino que no sea el mismo reloj: un tercer intento
el lunes y uno el martes (en `metricas.yml`, cuando el codirector lo mueva), y la tarea de métricas
diciendo en su primera línea de qué día es lo que lee.

**44. Resubir un Short lo mata.** `MDS-017` (resubido el 19/09) hizo 0; `MDS-023` (resubido el mismo
23/09) hizo 2. Son los dos únicos resubidos y dos de los tres ceros de los últimos diez.
→ **Un Short que ya se subió no se vuelve a subir** (C54, regla 11.9). Y cuando un arreglo tenga que
«rehacer y volver a subir», pregúntate qué ve YouTube: el mismo canal subiendo lo mismo dos veces.

**45. En la nube, quien puede escribir en GitHub lo decide el repositorio añadido a la tarea, no una
credencial.** Probado el 28/09 con un `push` de verdad desde una sesión en la nube: el proxy de la
sesión lo rechaza («el repositorio no está entre los de la sesión») aunque la credencial sea buena.
Por eso C53 no pone credenciales en ningún prompt: las tareas escriben porque el repositorio está
añadido a ellas.
→ Es la trampa 34 en git: **antes de diseñar alrededor de un acceso, prueba el camino entero con
una escritura de verdad, desde el mismo sitio desde donde va a correr.**

**46. Le pedí al codirector una opción de una pantalla que no había visto, y no existía.** La tarea
1.3 del 28/09 le mandaba a añadir el repositorio a las tres tareas programadas en la página de
rutinas de Code, con una «advertencia honesta» de que yo no había visto esa pantalla. Las tres tareas
se habían creado en agosto desde una conversación de Cowork (`created_via: meta_mcp`): no salen en
esa página y no tienen campo de repositorio. Lo supe al día siguiente, **en un minuto**, listándolas
con la herramienta de tareas programadas, que enseña cómo nació cada una y qué campos tiene.
→ Es la trampa 45 aplicada a una instrucción: **antes de mandar a alguien a una pantalla, comprueba
con lo que tengas a mano que el objeto que va a buscar allí existe y tiene ese campo.** Una
advertencia de «no lo he visto» no sustituye a mirarlo; solo traslada la duda a quien menos medios
tiene para resolverla.

**47. Prometí cambiar un horario con una herramienta que no podía tocar ese objeto.** La versión 15 decía
«puedo cambiar horarios, no repositorios», y era verdad **para las tareas de agosto, que había creado un
agente**. El 30/09 el codirector las rehízo como rutinas desde la web y la herramienta rechazó el cambio:
*«Agents can only update routines they created»*. Lo que era cierto de la clase («las tareas programadas»)
dejó de serlo del objeto concreto en cuanto cambió quién lo creó.
→ Es la trampa 46 cometida sobre mí mismo: **antes de escribir «esto lo hago yo», comprueba que la
herramienta puede actuar sobre ESE objeto**, no sobre los de su tipo. Y cuando alguien rehace algo por ti,
vuelve a comprobar lo que podías hacer con lo viejo.

**48. «No hay nada que entregar», con código 0, cuando sí lo había.** `entregar.py` comparaba contra el
último commit. Las rutinas trabajan en una rama propia y la plataforma le pide al modelo que suba ahí su
trabajo: si un día hacía `git commit` antes de llamar al script, el script no veía nada nuevo, decía que no
había nada que entregar y salía **bien**. Sin plan B y sin aviso: el trabajo, en una rama que nadie mira. Se
vio el 30/09 leyendo la primera entrega buena, antes de que pasara.
→ **Cuando un script decide que no hay nada que hacer, que lo decida contra la referencia que importa
(`main`), no contra un estado intermedio que otro puede haber movido.** Y cada vez que un proceso nuevo
empieza a llamar a un script viejo, léelo pensando en lo que el proceso nuevo hace antes de llamarlo.

**49. Durante seis semanas subimos una portada que YouTube no enseñaba, y la que enseñaba era negra.**
`miniatura.py` dibuja cada día una portada de color con el Engranaje y `publicar.py` la sube sin un
error. Nadie había mirado qué imagen ponía YouTube en cada sitio. El 02/10, píxel a píxel: en el feed no
hay portada; en la pestaña del canal, un fotograma 90-95 % azul marino; en el buscador, **el primer
fotograma, negro al 100 %**, por el fundido de entrada que se puso el 18/08 por otro motivo; y la
nuestra, solo en las superficies horizontales (las verticales personalizadas son, de momento, para
canales del Programa de Partners).
→ Es la trampa 1 en la plataforma: **comprueba lo que la plataforma enseña, en la superficie donde se
ve, no lo que le mandas.** Y cuando cambies el principio o el final de un vídeo, pregúntate quién usa
ese fotograma.

**50. Un aplazamiento sin el dato que lo reabre se queda aplazado para siempre.** C20 —el primer
comentario no se publicaba desde el 31/08— se aplazó «porque el canal tiene cero comentarios y una
decena de espectadores». Un mes después había 2.400 visualizaciones, S3 era el bloqueo declarado, y la
planificación seguía escribiendo cada semana un `primer_comentario` que nadie publicaba. Nadie lo
reabrió porque nadie había escrito **cuándo** reabrirlo.
→ **Cuando aplaces algo, escribe el dato concreto que lo reabre** («cuando un Short pase de 100», «cuando
S3 sea el bloqueo») **y ponlo en «lo que queda mirado» de cada versión** hasta que se cumpla.

**51. La regla del título se escribió para la búsqueda, y se quedó cuando mandaba el feed.** «El título
debe contener la pregunta que la gente escribe — es lo que nos está trayendo la poca audiencia» era
verdad en agosto. El 18/09 C40 dejó escrito que la búsqueda ya no mandaba; la regla del título no se
tocó, y su «menos de 100 caracteres» se usaba como objetivo: 74-98 caracteres, cuando entre los Shorts en
tendencia la franja que mejor funciona es la de 20-40 y el mejor nuestro tenía 45.
→ Son la 25 y la 31 juntas: **cuando cambie la superficie que manda, recorre todas las reglas que se
escribieron para la anterior.** Y un máximo vuelve a ser un objetivo en cuanto nadie mira el número de
al lado.

**52. Un fichero decía «soy el prompt» y la rutina no lo leía.** `metricas-lunes.md` lleva desde el 21/09
un aviso en mayúsculas: *«este fichero YA NO es una copia. ES el prompt»*. Era verdad para la revisión y la
planificación. **La de métricas nunca tuvo arranque**: la tarea de agosto llevaba el texto entero pegado, y
la rutina del 30/09 se creó copiando ese texto. Las instrucciones del 21/09 para métricas no le llegaron
nunca. Se vio el 05/10 leyendo el prompt de la rutina con `list_triggers`.
→ Es la trampa 46 sobre una afirmación propia: **cuando un documento diga cómo funciona otra pieza,
compruébalo en la pieza** (aquí, leyendo el prompt de la rutina), no en el documento.

**53. Una cifra cambió de significado sin cambiar de nombre.** Desde el 31/03/2025, una «visualización» de
un Short es cualquier reproducción que empiece, también la de quien desliza en el primer segundo. La
mediana de C26 mide, por tanto, cuántas veces nos enseñó el feed, no cuántos se quedaron. Studio ya lo
separaba («Se quedaron viendo»; la API, `engagedViews`) y en nuestros ficheros no estaba: el codirector lo
sacó a mano el 02/10 y salió entre el 2,7 % y el 40 %.
→ **Cuando una plataforma redefine una métrica, busca qué decisión colgaba de ella.** Y antes de fiarte de
la cifra de la API, compárala una vez con la que enseña la plataforma.

**54. Arreglé la pieza que ponía yo y no la que traía otro.** C58 dejó el colchón del montaje en 0,1 s, y
`MDS-031` arrancó la voz a los 0,381 s: la toma de Gemini traía 0,28 s de silencio delante. `qa.py` lo
cazó (por eso se mide el resultado y no la intención).
→ **Cuando quites un retraso, mide el resultado final, no la pieza que tocaste.** Es la trampa 1 en el
tiempo: lo que llega al espectador es la suma de todo lo que va delante.

**55. Dos renders iguales no dan el mismo vídeo.** Al probar C55.2 (08/10), el mismo guion renderizado
dos veces con el `render.py` de `main` sin tocar dio fotogramas distintos a partir del 36 (a 5 fps). La
regla 11.5 dice «mismo guion y mismo `t`, mismo píxel», y no se cumple; nadie lo había comprobado.
→ **Antes de usar «no ha cambiado ni un píxel» como prueba de que un cambio es inocuo, renderiza dos veces
lo de antes.** La comparación de C55.2 se hizo así (contra dos pasadas del original), no contra una.

## Dónde está el proyecto a 8 de octubre de 2026

**Primera dirección en diferido (rutina del jueves).** Versión **19** del plan, la que manda.

- **`MDS-016` desgranado** (`ANALISIS_MDS-016.md`): no fue la retención (la peor curva de los que pasan de
  60 vistas) ni la imagen; quedan el tema (mensajes del móvil) y el chiste de literalismo, y el azar no
  se descarta. Nada adelanta a B1; dos de siete Shorts por semana exploran la familia `mensajes`.
- **`REGLAS_DE_PRODUCCION.md`**: la línea principal de un Short, con una sola modificación por vídeo (la
  de su brazo). Lo escribe la dirección.
- **Referentes sin cara** (`REFERENTES_2026-10-08.md`): PsychToons y Kurzgesagt. Sin cara no es el
  techo; sin identidad, sí. `H-ilustracion-ia` en cola.
- **C55.2 en el render** (`animacion.py`), probado e inerte hasta que la rutina «Animación» (la crea el
  codirector) escriba páginas. **C36 no hecho**: pasa al lunes 12; sin él, siete a la semana.
- `MDS-034` no se produjo a las 07:22 UTC por una avería del runner (revisión diaria); el reintento lo subió a las 11:48 UTC, a tiempo para las 17:00.

## Dónde está el proyecto a 5 de octubre de 2026

**Sesión de lunes: el bucle de aprendizaje.** Versión **18** del plan, la que manda.

- **El canal, bien:** `MDS-031` (el primero con C56-C59) salió subido a las 07:12 UTC, seis horas tarde
  por el cron, y se publica a las 19:00. La mediana C26 sube a **35** (24 el 29/09). Semana del 28/09:
  mediana 62; los primeros suscriptores que llegan de Shorts.
- **C60 · el bucle.** Siete Shorts a la semana desde el 12/10 y catorce desde el 19/10 (si C36 pasa).
  Cada Short es de un brazo —control, **A** animación del mecanismo, **B** arranque con el dato— por un
  `orden` barajado en `05_calendario/bucle/ciclos.json`. La recompensa es **«Se quedaron viendo» a 48 h**
  (`engagedViews`/`views`, nuevo en `metricas.py`). Lo cuenta `04_agentes/bucle.py` todos los días y lo
  decide una regla escrita hoy. La bibliografía pasa a la planificación (diez fichas por semana).
- **C61 · personaje animado**: dos caminos (2D propio y 3D VRM con un avatar que diseña el codirector en
  VRoid), con boca, ojos y gestos sacados del guion y de la voz. **C51.3 · persona sintética** con fechas.
  Muestrarios el 16/10; A/B de presentadores (ciclo B2) desde el 26/10.
- **C62 · la dirección en diferido**: rutina «Dirección» lunes y jueves, cuaderno en un repositorio
  privado. Sustituye a C43.
- **Los relojes de GitHub**: `metricas.yml` despierta a la rutina de métricas por API; y C58.1 quita el
  silencio de la toma de Gemini.

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-10-05.md` — el `push` antes del martes 6
a las 03:13, el workflow de métricas, la rutina de métricas (arranque y disparador), la red del entorno,
y el repositorio privado con la rutina de dirección.

**Para la próxima (miércoles 7):** C55.2 (la animación en `render.py` y la rutina «Animación») y la prueba
de C36. **Y en cuanto haya lectura con el código nuevo:** que «se quedaron» de la API coincida con lo que
el codirector copió de Studio el 02/10 (trampa 53).

## Dónde está el proyecto a 2 de octubre de 2026

**Sesión de viernes: el estudio de mercado y el envoltorio del Short.** Versión **17** del plan, la que
manda. El estudio entero, con fuentes, está en **`00_estrategia/MERCADO_2026-10.md`**.

- **La conclusión del estudio:** el guion ya está por encima del nicho; lo que nos separa de los que
  crecen es lo que lo rodea. Se arreglan cuatro piezas baratas, todas desde el `MDS-031` (lunes 5):
  - **C56 · el título es la pregunta, sola**, 55 caracteres como mucho (eran 74-98);
  - **C57 · la pregunta al espectador se publica de verdad**, como comentario del canal, por la
    sincronización diaria del registro (nunca se había publicado: C20);
  - **C58 · el primer segundo sin negro**: 0,1 s de colchón y ningún fundido en los Shorts (decisión del
    codirector);
  - **C59 · la firma final pide que sigan el canal**, siempre con la misma frase (decisión del
    codirector).
- **Las miniaturas no se tocan:** YouTube solo enseña la nuestra en las superficies horizontales. La
  portada real es el primer fotograma, y eso lo arregla C58 (trampa 49).
- **La música no tenía fallo:** la rueda de 14 pistas dio la vuelta en `MDS-029`. Las 14 se quedan.
- **Hoy en público:** 5 suscriptores (eran 0). Semana de C50: 67 · 66 · 6 · 10. Todavía sin efecto
  visible de la imagen real.
- **Lo que no se toca antes del 15/11:** cinco Shorts a la semana y el largo suspendido. El estudio
  dice que lo mejor por vídeo son 2-4 a la semana y que el dinero y los suscriptores de la divulgación
  están en el largo; las dos cosas se piensan después de la decisión.
- **Comprobado:** la rutina de planificación corre en `claude-opus-5-5` con `7 22 * * THU,FRI,SAT`,
  que es **UTC** (00:07 de España del día siguiente). El paso 0 de su fichero ya lo tiene en cuenta.

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-10-02.md` — el `push` antes del lunes 5
a las 03:13 (sin él, `MDS-031` sale como hasta ahora), una línea opcional en `sincroniza_registro.yml` y
una consulta única en Studio («visto frente a deslizado»).

**Para la próxima sesión (lunes 5):** lo que ya estaba (primera semana entera de C50, las rutinas
entregando solas, C44, C47, P9); que `MDS-031` salió con título corto, sin negro y con la firma nueva
(ficha: `silencio_inicial.acaba_s` ≈ 0,1); el bucle; y «visto frente a deslizado» si el codirector lo
ha mirado. **Y el martes 6**, que la primera pregunta se publicó en `MDS-031` (`pregunta_publicada` en
el registro).

## Dónde está el proyecto a 30 de septiembre de 2026

**Sesión de miércoles, adelantada.** Versión **16** del plan, la que manda.

- **El canal vuela solo por primera vez (C53.1).** Las tres rutinas de Code funcionan: la de métricas
  entregó sola (`d234237`) y las tres tareas de agosto están apagadas. La revisión de hoy aún fue la
  vieja (`.tar.gz`, aplicado por el codirector); desde mañana entrega sola.
- **C53.2**: `entregar.py` ya no se deja engañar por un commit previo (trampa 48) y el workflow borra las
  ramas de sesión que ya están en `main`. «Crear PR» en una ejecución de rutina **no se pulsa nunca**.
- **Yo no puedo tocar las rutinas nuevas** (trampa 47). El modelo de la planificación (Opus 5.5,
  decisión del codirector hoy) y su horario jueves-viernes-sábado los pone él: tarea 2 del 30/09.
- **C55.1 · el muestrario de la animación a medida, hecho**: `07_pruebas/animacion-2026-10/`. Unos
  110.000 tokens; enseña el mecanismo mejor que el archivo, con menos estímulo visual. Propuesta nueva:
  animar solo las escenas de mecanismo. **Decide el codirector** (tarea 3).
- **C51.3 · Kaggle listo; licencias estudiadas**: MuseTalk 1.5 sí (con un cambio), cinco de siete no.
  Prueba, no antes del 12/10.

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-09-30.md` — el `push` antes de mañana
a las 11:28, el modelo y el horario de la planificación antes del jueves a las 22:07, y mirar el
muestrario.

**Para la próxima sesión (lunes 5):** que la revisión del jueves y la planificación entregaron solas y
si la limpieza de ramas corrió; si la tarea 2 salió por tres disparadores o por el diario; la respuesta
a la tarea 3 (C55.2, entero o mezclado); y lo del lunes 5 que ya estaba: primera semana entera de C50,
S3, C44, C47 y P9.

## Dónde está el proyecto a 29 de septiembre de 2026

**Sesión de martes, sin cambios en producción.** Versión **15** del plan, la que manda.

- **El canal, bien:** `MDS-027` salió con vídeo de archivo detrás; la revisión corrigió tres planos
  de `MDS-028` y `029` y el codirector aplicó su `.tar.gz`. Mediana C26, **24,0**, sin cambios.
- **C53.1 · las tareas se rehacen como rutinas de Code.** Las de agosto no admiten repositorio
  (trampa 46). El codirector crea tres rutinas nuevas con el mismo texto y modelo, el repositorio y
  un entorno «Mecánica del Humor» con red completa; prueba la de métricas con «Run now»; apaga las
  viejas. **Sin probar:** si una rutina puede subir cualquier rama `claude/` o solo la suya; si es lo
  segundo, la prueba dará plan B y el arreglo está pensado en la versión 15 (no aplicado: tocaba el
  mecanismo de subida y la comprobación de permisos de la sesión lo paró).
- **El horario jueves-viernes-sábado de la planificación lo pone la dirección** (puedo cambiar
  horarios, no repositorios), pero **solo cuando C53.1 funcione**: con `.tar.gz`, el reintento del
  viernes no ve el paquete del jueves y planificaría dos veces.
- **C55 · animación a medida con Opus 5.5** (el codirector entiende por animación la hecha con
  JavaScript por Opus). Todos los Shorts con datos son ya animación JS de plantilla, incluidos los
  tres mejores; la imagen real no tiene datos todavía. Propuesta: muestrario de un Short publicado
  (sin subirlo), y si convence, un Short de cada cinco del 12/10 al 6/11, decidido por la retención
  a 30 s con una regla escrita de antemano. Estimación: 150.000-400.000 tokens de Opus 5.5 por Short.
- **Lo que espera al codirector:** `tareas/tareas_codirector_2026-09-29.md` — la tarea 1 (rutinas,
  antes del jueves 22:00), la 2 (Kaggle, no urgente) y la 3 (¿muestrario, y sobre qué Short?).

**Para la próxima sesión:** el resultado de la prueba de métricas; si hay rutinas nuevas, apagar las
viejas si siguen encendidas y poner el horario de la planificación; el muestrario si el codirector
dijo sí (**dijo sí: `MDS-027`, en la siguiente sesión**, en `07_pruebas/animacion-2026-10/`,
con la misma voz de la caché y sin subirlo; que mire su uso antes y después); y el lunes 5, lo que ya estaba (C50, S3, C44) más `metricas_diarias.yml` (C47), que nunca se
le pidió en un fichero de tareas.

## Dónde está el proyecto a 28 de septiembre de 2026

**El punto de control del 27 está contestado con datos, y el canal empieza a volar solo.** Versión
**14** del plan, la que manda.

- **Los números** (`metricas.json` del 28/09, lanzado a mano porque el cron no corrió, trampa 43):
  mediana C26 **24,0** (era 11,0); **cinco** Shorts por encima de 100 en dos semanas; mediana de los
  últimos diez **90,5**. `MDS-021` y `022` retienen al 59-64 % en el segundo 30, lo mejor de la
  historia del canal. **Cero suscriptores y casi cero «me gusta»: el bloqueo ahora es S3.** Tres casi
  ceros en diez; dos son las dos únicas resubidas (C54).
- **Viabilidad:** viable hasta el 15/11; lo más probable, la banda del medio (ampliar el tema con
  prórroga hasta el 10/01). La puerta de los 1.000 sigue sin decidir (antes del 8/11).
- **C53 · las tareas entregan solas** con `entregar.py` y el workflow «Entregas». Falta la tarea 1
  del codirector del 28/09: añadir el repositorio a las tres tareas y mover cuatro workflows (el
  token no puede escribirlos). Hasta entonces, plan B: el `.tar.gz` de siempre.
- **C52 · actualidad**, fase 1: un Short de cada cinco, como mucho, con gancho de actualidad, desde
  la planificación del jueves 1/10. **C50.7:** caras otra vez detectadas (YuNet). **C54:** no se
  resube nunca. **C48.2:** criterio de la lectura en frío ratificado. **C51.2:** regla 7.1, sí a
  la persona sintética con condiciones; Kaggle cuando el codirector pueda. **C44 aplazado.**
- **El codirector no está esta semana.** No se le pide nada más que la tarea 1 (cinco minutos).

**Para la próxima sesión (lunes 5):** comprobar que la primera entrega sola llegó a `main` (o por qué
no); la primera semana entera con C50 (`MDS-026` a `030`) y si hubo gancho de actualidad; S3 —qué
le pide el vídeo al que lo ve—; la muestra de C44 en `07_pruebas/`.

## Dónde está el proyecto a 23 de septiembre de 2026, por la tarde

**C50 entra en producción el mismo día (versión 13, la que manda).** El codirector creó por la mañana
las tres cuentas y las cuatro claves, lanzó la prueba y la contestó: **A** —archivo detrás y la frase
corta encima—, con cuatro problemas (el texto sobre las caras, la imagen a destiempo, el fondo
desenfocado bajo la cifra y los paneles, un plano quieto), B no, C no llegó a verse, y cuatro notas:
tarjetas de marca intercaladas, un personaje que hable (o un avatar dibujado), siempre el mismo, y
*«dinamismo es la palabra»*. Pidió empezar a producir cuanto antes, así que no se esperó al viernes:

- **Código:** `visual.py` reescrito como resolvedor de producción (relevancia por título, varias
  búsquedas en orden, movimiento, caras con OpenCV, diagnóstico de las APIs, manifiesto y hoja de
  contactos por plano), `fondo_visual.py` nuevo (cortes anclados a la palabra sobre la voz real,
  pista de fondo), `render.py` y `escena.html` con **modo archivo** y respaldo automático al render
  de siempre, `publicar.py` con créditos y `containsSyntheticMedia`, avisos C50 en
  `validar_guion.py`. Probado de punta a punta en el contenedor con clips sintéticos (bitácora
  del 23/09, sección 8).
- **`MDS-024` y `MDS-025` llevan `visual`**: el jueves 24 sale el primer Short con vídeo detrás.
- **La planificación escribe `visual` desde `MDS-026`**; la revisión diaria mira cada día la hoja de
  contactos y corrige en `ajustes.json`.
- **C51.1:** el Engranaje hablará (muestrario el viernes 25); la persona realista, solo si el
  codirector dice sí a la regla 7 (pregunta en su fichero de tareas).

**Lo que espera al codirector:** la **tarea 3** de `tareas/tareas_codirector_2026-09-23.md`: mover
`visuales.yml` y `producir.yml` a `.github/workflows/`, borrar `visual_prueba.yml` y hacer `push`; y,
si puede, una producción de prueba de `MDS-024` sin subir.

**Para la próxima sesión (viernes 25):** mirar `MDS-024` y `MDS-025` publicados, calibrar los
umbrales de movimiento (0,5) y relevancia (0,34) con los datos reales de sus manifiestos, leer el
primer `diagnostico.json` (qué le pasaba a Cloudflare), y el muestrario del Engranaje que habla.

## Dónde está el proyecto a 23 de septiembre de 2026

**Sesión extraordinaria, de miércoles, por tres Shorts seguidos sin hilo.** El codirector lo avisó
el 21, el 22 y el 23 en su cuaderno; el 23 con toda la razón y sin paciencia: *«es una sucesión de
mensajes inconexos, sin sentido, que huelen a AI slop de lejos»*. Los tres eran guiones que yo había
reescrito el 18/09 para que cupieran en la duración de su serie (trampas 37 y 38). La sesión
(**versión 12**, la que manda) cerró cuatro cosas:

- **C48 · la historia antes que el reloj.** `MDS-023`, `024` y `025` reescritos con una pregunta,
  una respuesta y un puente, y el chiste de la apertura siendo el fenómeno del estudio. La duración
  de la serie y el remate en el segundo 10 dejan de ser error. **Nueva puerta: la lectura en frío**
  —un subagente que solo ve las narraciones cuenta de qué va— obligatoria desde `MDS-026`, y la
  revisión diaria la repite cada día con el Short de la madrugada siguiente. `MDS-023` se rehízo el
  mismo día (la subida de madrugada, `X1GAp3OUgKg`, la borró el codirector).
- **C48.1 · ninguna fórmula dos veces.** El codirector, al leerlos: *«¿por qué todos tienen "y aquí
  falla"?»* Los 25 publicados cierran así (trampa 39). El cierre honesto sigue; la frase, no.
  `validar_guion.py` avisa si un cierre empieza igual que alguno de los cuatro anteriores.
- **C49 · `sincroniza_registro.yml` funciona**: corre con horas de retraso, después de la revisión
  diaria. De paso, `metricas.py` y `registrar.py` escribían el registro con distinta sangría y cada
  día se reescribía entero en git; arreglado.
- **C50 · la imagen deja de ser una diapositiva**: vídeo de archivo (Pexels y Pixabay) e imágenes
  generadas (FLUX en Cloudflare, plan gratuito) a pantalla completa, un cambio cada dos o tres
  segundos, y el texto como capa encima. Se prueba con un muestrario y **decide el codirector
  mirándolo**; entra la semana del 28. **C51**: el presentador sintético de @Maestro_Seductor, no
  por ahora (coste, fragilidad, regla 7); el paso intermedio propuesto es que el Engranaje hable.

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-09-23.md`. La 1 y la 1 bis (los dos
push y el borrado en Studio) son de hoy mismo; la 2 son las cuentas y claves de C50.

**Lo que queda mirado y sin resolver:** la primera planificación con C48 es el jueves 24; el viernes
25 se miran sus lecturas en frío. Y sigue abierto por qué `MDS-016` hizo 1.210.

## Dónde está el proyecto a 21 de septiembre de 2026

**El punto de control del 27 ya está contestado, y con un sí.** Su pregunta es *¿algún Short ha
pasado de 100 visualizaciones en 48 horas?* y son **tres**: `MDS-016` **1.210**, `MDS-019`
**161**, `MDS-018` **135**. El desenlace escrito para ese sí es «el formato funciona, toca
escalarlo». Sigue habiendo **cero suscriptores** y la mediana de los últimos veinte sigue en
**11,0**, que es historia de agosto: el 15 de noviembre **ninguno de los veinte Shorts
publicados hasta hoy estará ya en la ventana de veinte**. Lo que pronostica algo es el régimen
de la última semana —1.210 · 161 · 135 · 27 · 0—, cuya mediana cae en la banda de «se amplía el
tema». **No estamos fracasando: estamos en la frontera, y la frontera la deciden los ceros, no
los vídeos buenos.**

La sesión del lunes 21 (**versión 11** del plan, la que manda) salió de cinco cosas del
codirector y cerró seis:

- **C42 · el episodio largo se suspende.** Siete episodios, treinta y cuatro días, **114
  visualizaciones entre todos**; y su precacheo se comía 9 de las 10 peticiones diarias del
  modelo que **desde el 15/09 es el respaldo de voz de los Shorts** (trampa 35). `MDH-008` fuera
  de la parrilla con su guion intacto. Vuelve cuando la mediana llegue a **50**.
- **C43 · la dirección no se automatiza; su salida sí.** Respuesta a su pregunta. Desde hoy hay
  una nota en `08_comunicacion/` después de cada sesión.
- **C44 · la voz deja de sonar a montaje.** Tiene razón y además se lo pedíamos: la dirección de
  actor pide cambios de **timbre**, y el volumen por escena **no se iguala nunca** (`loudnorm`
  va una sola vez, sobre la mezcla). Tres capas; **A y B entran el lunes 28**, no antes, porque
  la semana del 21 es la primera medida limpia de C38.
- **C45 · `ESTADO.md` congelado**, nace `05_calendario/estado/`. Y la incidencia del domingo era
  **falsa por dieciséis minutos**.
- **C46 · el canal se lee a sí mismo.** La planificación no leía `metricas.json`: `MDS-016` hizo
  1.210 y una semana después no había un solo vídeo que lo continuara.
- **C47 · las métricas se leen todos los días**, no solo los lunes. Un Short puede hacer 0
  durante seis días sin que nadie se entere; es lo que pasó con `MDS-017`.

**Y una decisión abierta con fecha tope:** la tercera puerta de C26 —«algún Short por encima de
1.000»— **ya está cumplida** desde el 14/09. Propuesta de la dirección: cambiarla por «dos
Shorts por encima de 1.000 en semanas distintas». Decide el codirector, **antes del 8 de
noviembre**.

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-09-21.md` — el `push`, **las
impresiones de `MDS-017` y `MDH-007` en Studio** (es la tarea que decide si lo siguiente que
tocamos es el guion o la publicación), desactivar `voz_adelantada.yml`, y la puerta de los 1.000.

**Lo que queda mirado y sin resolver:** por qué `MDS-016` hizo 1.210 sigue sin explicación desde
el 15/09; `E02` sigue con dos DOI; `F04` sin sustituir; `P1` sin respuesta desde el 14/09; y
TikTok parado a propósito hasta el 27.

## Dónde está el proyecto a 18 de septiembre de 2026

**Los números se mueven por primera vez.** `MDS-016` **1.280 visualizaciones**, `MDS-019` **182**
y `MDS-018` por encima de 100, contra una mediana de 10 en los quince anteriores. Cero
suscriptores todavía.

La sesión del viernes 18 (**versión 10** del plan, la que manda) salió del mismo aviso repetido
dos días —«me cuesta seguir el hilo», «forzado entre el nudo y el desenlace»— sobre dos guiones
que ya se habían reescrito contra las tres pruebas de cosido. Lo que apareció al medirlo:

- **C38 · el Short se escribe a la duración de su serie y el remate no cae antes del segundo
  10.** Las dos, error en `validar_guion.py`. `PPM` pasa de 150 a 130 (medido). Dos duraciones
  de serie suben (30→35 y 35→40) porque las de agosto son anteriores a que el cierre honesto
  fuera obligatorio en Shorts y no caben. **Los cinco Shorts de la semana del 21, reescritos sin
  añadir ni una afirmación nueva.** `MDS-017` va exento, y la exención vive en el código.
- **C38.1 · la risa escrita.** `voz.py` la vetaba en todas las escenas, así que la mitad de la
  regla 13.1 no se podía ejercer. Se pide con `"risa": true`, una por Short, nunca en la escena
  1, el remate ni el cierre.
- **C39 · la bibliografía tiene dos ficheros** y el bueno no era el que se miraba. Ver trampa 33.
- **C40 · el marketing externo es el 5,4 % del tráfico.** Feed 54,6 %, búsqueda 27,7 %. La frase
  de `LEEME.md` «la única superficie que responde es la búsqueda» **está corregida**: dejó de ser
  cierta en `MDS-007`.
- **C41 · TikTok y Reels reabiertos.** Las dos APIs exigen auditoría (días a semanas). Se empieza
  el trámite ya; se publica cuando C38 haya dado su primera medida. El premio no es la
  exposición: es poder separar «el contenido no funciona» de «no nos están enseñando» antes del
  15 de noviembre.

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-09-18.md` — el `push` antes del
lunes de madrugada, el trámite de TikTok, el DOI de `E02`, y los enlaces del banco de fotos, que
siguen pendientes del 15/09.

**Lo que queda mirado y sin resolver:** la caché de voz de `MDH-007` lleva dos días clavada en 18
de 41 escenas y no hay commit de precacheo hoy. El domingo sale, pero sin margen para rechazos.
Hay que volver a contarlo mañana.

## Dónde está el proyecto a 15 de septiembre de 2026

**Por la tarde (versión 9.1, C33.2):** la reproducción manual de `MDS-017` falló sin subir nada.
El registro enseñó tres cosas: la dirección v1 se rechazaba con un 400, los rechazos gastan
cuota, y la librería reintentaba en silencio hasta cuatro veces. Arreglado: cliente sin
reintentos, dirección v2 con el formato que pide Google, los rechazos pasan a la mínima, el 429
sin apellido se resuelve esperando un minuto, y **`edge-tts` no entra nunca solo** (decisión del
codirector). **`MDS-017` se publica el sábado 19 a las 19:00 y `MDH-007` el domingo 20 a las
12:00**: el largo no llegaba al sábado con diez peticiones al día. Durante unos días es normal
que alguna producción salga a las 10:23 en vez de a las 03:13.

**Por la mañana:**

**Una buena y una mala, y la sesión fue de «algo se ha roto».** Detalle en la **versión 9** de
`PLAN_DE_CAMBIOS.md`.

- **`MDS-016` es el primer Short que pasa de 1.000 visualizaciones** (dato del codirector desde
  Studio). No se sabe por qué: la lectura del lunes 21 empieza por ahí.
- **`MDS-017` salió con dos voces y un guion sin hilo.** Arreglado con **C33.1**: una sola voz
  por vídeo, con reintentos y una escalera 3.1 → 2.5 → esperar al cron de las 08:23 UTC →
  `edge-tts` entero solo en el último intento programado. Y los **cuatro guiones que quedaban de
  la semana** (`MDS-017` a `MDS-020`) reescritos contra las tres pruebas de cosido, con todas sus
  afirmaciones comprobadas contra los artículos. `MDS-019` afirmaba lo contrario de lo que dice su
  fuente.
- **La cuota de imagen de Gemini no existe** (todo a `0/0`): la vía 3 de C34 se cae. **El
  tratamiento elegido es el duotono ámbar.** C34 entra el viernes 18.
- **Propuestas nuevas:** **C36** (una llamada por vídeo y corte por palabras con un reconocedor
  local; se prueba el viernes 18 antes de encender nada) y **C37** (un motor de voz sin cuota;
  investigación sin fecha).

**Lo que espera al codirector:** `tareas/tareas_codirector_2026-09-15.md` — el `push`, una línea
en `producir.yml`, volver a producir `MDS-017` esta tarde, y el enlace de cada foto del banco.

## Dónde está el proyecto a 14 de septiembre de 2026

**La sesión del lunes 14 cerró tres cosas y adelantó una pregunta.** El detalle está en la
**versión 8** de `PLAN_DE_CAMBIOS.md`, que es la que manda.

- **C33 · la dirección de actor, por escena.** Ocho papeles (apertura, planteamiento,
  remate, contraste, cifra, enumeración, cita, objeción) derivados del propio guion: el
  tipo de escena, la posición, y la pausa de la escena anterior, que es lo que marca el
  remate — 8 detectados en 47 escenas, los 8 correctos. Prohibición explícita de reírse en
  todas las escenas. Y la frase que precede a un silencio se deja **suspendida**, que es lo
  que convierte ese silencio en pausa en vez de en corte. **No toca al guionista.**
- **C34 · se revierte el descarte de las imágenes.** El banco propio entra, con tratamiento
  de marca (duotono sobre la paleta del canal, enmarcado, nunca solo, con deriva lenta). Se
  decide mirándolo: `07_pruebas/imagen-14-09/muestrario.html`. Primera posición, **la escena
  1 del Short** — no la miniatura, porque en el feed de Shorts no hay miniatura que pulsar.
- **C35 · la densidad se construye dentro de la escena**, no partiéndola en más: partirla
  choca con la cuota de Gemini (diez llamadas al día) y no hace falta. P3, P5, P6 y P8
  juntos dan un cambio cada 1,6 s sin un corte añadido.

**Los números, que son el marco:** mediana de 10 vistas a 48 h sobre quince Shorts, **cero**
por encima de 50, **cero** suscriptores, y `MDH-006` con **cero visualizaciones** a los dos
días. La retención enseña fuga continua —la mitad se va en el segundo 13—, no desplome
inicial.

**Lo que espera al codirector:** `voz_adelantada.yml` por crear (ahora con fecha: `MDH-007`
sale el 19/09 y tiene que salir con voz de Gemini), el lote de imágenes de prueba, y mirar
la cuota de imagen en el panel de Gemini. Todo en
`00_estrategia/tareas/tareas_codirector_2026-09-14.md`.

## Dónde está el proyecto a 12 de septiembre de 2026

**La sesión de dirección del sábado 12 cerró seis cosas.** El detalle está en la
**versión 7** de `PLAN_DE_CAMBIOS.md`, que es la que manda. En corto:

- **El guionista, reescrito los dos prompts.** Tres avisos del codirector en cuatro días
  (MDS-013 «parece un recorte de un recorte», MDS-014 «martes» huérfano, MDH-006 «el chiste
  no entra»). Los tres guiones **cumplían el prompt entero**: el fallo era del documento,
  que decía qué tenía que *contener* un guion y nunca qué tenía que *sostenerlo*. Entran tres
  pruebas de cosido en el corto y una cadencia de risa en el largo.
- **C28 · el detalle concreto.** Un día o un mes en pantalla que la voz de esa escena no
  diga es **error** en `validar_guion.py`. Medido sobre 302 escenas: señala tres, las tres
  reales, cero falsos positivos.
- **C29 · la barrera ya mira dentro del SVG.** Era el agujero por el que salió el texto
  desbordado del segundo 2:34 de MDH-006. Y de paso el resaltado se pinta en el diagrama
  horizontal en vez de salir con los asteriscos a la vista — `*Usarla*` iba a publicarse así
  el 19/09 en MDH-007.
- **C30 · las tareas programadas no pueden pedir autorización.** Se retira de los tres
  prompts la sonda `device_list_dir` que bloqueó la planificación del 10/09, y el prompt del
  almacén pasa a ser un arranque que lee el fichero del repositorio: **se acabaron las dos
  copias.**
- **C31 · el registro no sabe lo que sabe YouTube.** Es lo que hizo que MDS-011 se reportara
  como incidencia seis días seguidos estando publicado a mano.
- **C27 corregido:** el episodio largo sale con **una sola voz**, nunca mezclada, y la
  ventana de síntesis adelantada pasa a ser de viernes a viernes.

**Los números no se han movido** y siguen mandando: seguimos por debajo de 100
visualizaciones por vídeo, que es el umbral que el codirector puso como condición de
supervivencia. El punto de control sigue siendo el **27 de septiembre** y la decisión, el
**15 de noviembre** (C26).

**Lo que espera al codirector:** `producir.yml` con `GEMINI_API_KEY` en el paso equivocado,
y `voz_adelantada.yml` por crear. Los dos explicados enteros en
`00_estrategia/tareas/tareas_codirector_2026-09-12.md`.

## Dónde estaba el proyecto a 7 de septiembre de 2026

**El episodio largo del sábado 5 (MDH-005) tiene una visualización: la del
codirector.** Los tres Shorts con el motor C15 hicieron 31, 21 y 21, que es la
mejor racha del canal y sigue a menos de la mitad del umbral de S1. La cifra que
hay que tener siempre delante: **un canal de menos de mil suscriptores saca entre
50 y 500 visualizaciones por Short en 48 horas.** Nosotros sacamos entre 20 y 30.
No estamos por debajo de la excelencia: estamos por debajo del suelo de lo
normal.

| | Vistas | Suscriptores | Comentarios | Me gusta |
|---|---|---|---|---|
| MDH-001 · 002 · 003 · 004 · 005 (largos) | 13 · 28 · 8 · — · **1** | 0 | 0 | 4 |
| MDS-001 a 005 (primera tanda) | 6 · 11 · 13 · 3 · 11 | 0 | 0 | 0 |
| MDS-006 a 009 (con C15) | hasta **31**, tres seguidos > 20 | 0 | 0 | **1** |

**El canal sigue en el peldaño S1.** La rama del punto de control del 27 en la
que estamos es la segunda: va lento, el camino es bueno, se sigue.

**Las dos decisiones grandes del 7 de septiembre, en `PLAN_DE_CAMBIOS.md`
versión 6, que es la que manda:**

- **C25 · La presentación.** El codirector la señaló como el talón de Aquiles y tiene
  razón: el 72 % de lo que se ve es texto sobre fondo y los ocho iconos de
  `02_marca/iconos.svg` no se han usado ni una vez en once Shorts. Diez
  propuestas (P1–P10), todas deterministas y a coste cero salvo tres sonidos que
  el codirector tiene que descargar una vez. Entran en tres semanas y están todas
  puestas antes del punto de control del 27.
- **C26 · La fecha en la que se decide.** **Domingo 15 de noviembre de 2026**,
  con la mediana de visualizaciones a 48 h de los últimos veinte Shorts:
  **≥ 150 → se sigue; entre 50 y 150 → se amplía el tema, con una única prórroga
  de ocho semanas hasta el 10 de enero; < 50 → se para.** Los umbrales se pueden
  discutir, pero **solo antes del 8 de noviembre**: después de ver los datos ya
  no es una decisión, es una excusa.

**Y una regla que se relaja, a propósito:** la 11.1 (un cambio por producción)
queda **suspendida para los cambios de presentación** hasta el 27 de septiembre.
Con veinte visualizaciones por vídeo no hay nada que atribuir midiendo, así que
la regla cuesta una semana por mejora y no compra lo único que justificaba
pagarla. Vuelve el día que un Short pase de 100 en 48 horas. Siguen en pie la
11.2 (se mira el muestrario), la 11.5 (determinista) y la barrera de C21.

**Lo que se rompió y lo que se hizo:**

- **MDS-011 (7/09) salió con tres defectos** —el marcado leído en voz alta, la
  cara triste sobre el texto y el solape— y **pasó por seis filtros**. El
  marcado está arreglado en tres capas (`voz.py` lo sanea, `validar_guion.py`
  avisa, los dos prompts lo prohíben); el solape estaba arreglado desde el
  domingo y no llegó por la trampa 11; la cara está arreglada en la regla 14.3 y
  se quitará de raíz redibujando `piensa` (P8).
- **`producir.yml` borra el expediente de calidad del episodio largo todos los
  sábados**, por un `sort` alfabético que pone `MDH-` antes que `MDS-`. Fichero
  protegido: la corrección de una línea está entregada al codirector.
- **C23 quedó a medias el viernes 4:** Google no da por verificado el dominio
  pese a que la comprobación de propiedad pasó. El codirector lo reintenta el lunes
  7. Mientras tanto el token de siete días sigue vivo, así que **si el canal deja
  de publicar, mira eso primero** (`TOKEN_DE_YOUTUBE.md`).

**Lo que está en verificación, y en qué orden:**

| Cuándo | Qué se mira |
|---|---|
| sem. 7 sep | **P3 + P4 + P6 + P10** — el campo `icono`, la escena 1 sin párrafo, la jerarquía de tres tamaños y el validador de estructura de serie. Y el código de C7 con `--motor edge` |
| **lun 14 sep** | **C7 se enciende**: Gemini TTS en los Shorts. Y **P1 + P8** (profundidad; el personaje actúa y `piensa` redibujado) |
| sem. 21 sep | **P2 + P7 + P5** (continuidad, serie, la cifra que se construye). **P9** si están los sonidos |
| **dom 27 sep** | **Punto de control intermedio**, con la presentación entera puesta. Tres desenlaces, versión 4 |
| **dom 15 nov** | **La decisión.** C26, versión 6 |

**Lo que sigue escrito y sin hacer:** el estimador de duración de
`validar_guion.py` (asume 150 palabras/minuto y la voz real hace 130 en Shorts);
MDH-007 y 008 sin adaptar, uno por semana; C20 (el primer comentario), aplazado a
propósito; la ampliación de música de C18, **bloqueada por red**; la mediana en
`metricas.py`, que hace falta antes del 27; y 46 fichas de bibliografía con el
DOI «por verificar».

**Y lo de siempre:** no se clona la voz del codirector por ahora; no se encienden
los subtítulos quemados; no se usan fotos de banco de imágenes; y no entra C10
aunque la búsqueda funcione — sigue detrás del peldaño S1.

## Qué NO hace falta meter en el prompt

Estas cosas ya están en los documentos y repetirlas solo alarga el mensaje:

- El diagnóstico del canal y por qué se cambió de rumbo → `DIAGNOSTICO.md`
- Qué hace cada tarea programada → `00_estrategia/tareas/` (copia legible) y el
  almacén de tareas programadas (la copia que corre, que puedo leer y editar)
- El criterio editorial → `REGLAS.md`
- El estado de los cambios → la tabla de `PLAN_DE_CAMBIOS.md`, con C15 y C16 al final
- Los números → `metricas.json`

## La prueba de que funciona

Si un yo recién arrancado con ese prompt no puede responderte a «¿en qué peldaño
está el canal y qué lo bloquea?» sin preguntarte nada, la documentación se ha
quedado corta — y eso es un defecto del proyecto, no del prompt. Arreglarlo es
parte del trabajo de cada lunes.
