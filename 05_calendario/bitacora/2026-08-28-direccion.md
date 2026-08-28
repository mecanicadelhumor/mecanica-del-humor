# Dirección — 28 de agosto de 2026 (viernes)

Conversación con Silvestre. Lo que se decidió, con el porqué y las mediciones,
para que no haya que volver a razonarlo.

---

## 1. El cron nunca ha funcionado. No es que fallara dos días

Silvestre lo vivió como «el cron falló el 27 y el 28». Los datos dicen otra cosa,
y es peor y más fácil de arreglar. Horas UTC del commit del bot al terminar la
producción, sobre un cron programado a las **01:00 UTC**:

| Día | Producción terminada | Retraso |
|---|---|---|
| 24/08 | 04:05 | **+3 h 05** |
| 25/08 | 03:38 | **+2 h 38** |
| 26/08 | 04:03 | **+3 h 03** |
| 27/08 | 07:55 | no salió; la lanzó Silvestre a mano |
| 28/08 | 07:00 | **+6 h 00** |

**Ni una sola vez a su hora.** El retraso venía creciendo y nadie lo vio porque el
vídeo siempre llegaba antes de las 19:00. El 27 se pasó de largo y el 28 llegó a
las 09:00 de la mañana en España — diecisiete minutos después de que Silvestre
mirara y lo diera por perdido. **MDS-005 existe**: `14KLEyZ26-0`, privado, sin
programar.

**La causa.** El `schedule` de GitHub Actions no es una promesa, es una cola de
prioridad baja: se retrasa cuando hay carga y **se pierde sin avisar**, y el
momento de más carga es el minuto 0 de cada hora. Los tres workflows del
proyecto estaban en minuto 0 (`0 1`, `0 5`, `0 12`) y **los tres han fallado**:
producción con retrasos crecientes, `metricas.yml` sin correr nunca y
`demanda.yml` sin dejar `demanda_bruta.json` el jueves 27.

**La decisión: tres intentos al día y ninguno en punto.**

- `producir.yml`: `13 1`, `47 4`, `23 8` (UTC). El último, once horas antes de la
  publicación de las 19:00.
- `metricas.yml`: `19 5` y `37 8` los lunes.
- `demanda.yml`: `26 12` y `52 15` los jueves — el segundo, cuatro horas antes de
  que despierte la planificación.

**Lo que hace seguro reintentar: `cola.py` ya no repite lo que está subido.**
Lee `05_calendario/registro_publicaciones.json` y descarta cualquier trabajo cuyo
`id` ya tenga `video_id`. El segundo y el tercer intento del día salen con
`hay_trabajo=false` en segundos y sin arrancar el runner. `--rehacer` lo fuerza.
Probado en vivo: con MDS-005 ya registrado, `cola.py --fecha 2026-08-28` devuelve
`hay_trabajo: false`.

Esto no es una tirita: es la diferencia entre un canal que depende de la suerte y
uno que no. Un solo intento a una hora popular era el punto único de fallo de todo
el sistema.

---

## 2. Por qué los Shorts parecen un pase de diapositivas — y no es una opinión

Silvestre: «los shorts siguen estando bien de contenido, pero la calidad de la
presentación es muy baja». Tiene razón, y la causa estaba escrita en el propio
código desde hace diez días. En `voz.py`, línea 333:

> «los subtítulos quemados son lo único que se mueve durante el tramo central de
> cada escena, que es estático por diseño. **Un vídeo sin ellos se percibe como un
> pase de diapositivas**.»

Los subtítulos quemados **se retiraron el 20/08** por decisión editorial (C6.1) y
**no se puso nada en su lugar**. La respiración de zoom de `montaje.py`, la otra
fuente de movimiento, **se había descartado antes**. Así que desde el 20 de agosto
el tramo central de cada escena no tiene absolutamente nada que se mueva, y ese
tramo es **el 85 % del vídeo**.

Medido, no supuesto. Renderizando MDS-005 (53 s) con el motor tal como está hoy:

- **185 fotogramas capturados en total.** Para una escena de 9,1 s, `render.py`
  captura 25: veinticuatro de la entrada y **uno solo estirado sobre los ocho
  segundos restantes**.
- Tres capturas de la misma escena a t=15 %, 50 % y 85 % de su duración salen
  **idénticas píxel a píxel**.

Tres documentos distintos daban por hecho que el movimiento lo ponía otro. No lo
ponía nadie.

---

## 3. La razón para no arreglarlo ya no existe

Toda la arquitectura de captura («capturar solo lo que se mueve, 2.000 fotogramas
en vez de 13.000») se construyó sobre un supuesto de coste, y ese supuesto es
falso en este repositorio: **`mecanica-del-humor` es público, y los minutos de
GitHub Actions en runners estándar sobre repositorios públicos son ilimitados y
gratuitos** — confirmado contra la nota de precios de 2026 de GitHub, que mantiene
la gratuidad explícitamente. El único límite real es el `timeout-minutes: 150` del
job.

Medido en un contenedor comparable a un runner: **259 ms por captura a 1080×1920**.

| | Capturas | Render |
|---|---|---|
| Short de 60 s a 30 fps | 1.800 | **7,8 min** |
| Largo de 5 min a 30 fps | 9.000 | 38,8 min |

Siete minutos y medio de los 150 disponibles. **El presupuesto de render nunca fue
el problema; era una restricción heredada que nadie volvió a comprobar.**

---

## 4. C15 · El Short se mueve

Cinco capas, todas deterministas (`pintar(t)`, cero `Math.random`, regla 11.5),
todas **solo en formato vertical**: el episodio largo no se toca hasta tener las
métricas del Short delante (regla 11.1).

1. **Revelado palabra a palabra.** El texto en pantalla ya no aparece de golpe:
   llega a la velocidad a la que se lee (entre 0,11 y 0,30 s por palabra, ajustado
   al número de palabras de la escena) y sigue llegando durante el ~60 % de la
   escena. La palabra resaltada entra con un pequeño rebote.
2. **Barra de avance** arriba, que se llena a lo largo del vídeo **entero**. Es lo
   único que se mueve el 100 % del tiempo y cuesta cero.
3. **Acercamiento lento del bloque de contenido**, 2,2 % por escena. Es
   exactamente lo que C6.3 quería hacer con `zoompan` de FFmpeg. La bitácora del
   24/08 midió que `zoompan` necesita preescalar a ×4 para no temblar y que eso
   cuesta 5,3× — porque FFmpeg trunca a píxel entero. **El navegador no**: lo hace
   con precisión subpíxel, gratis. Era el problema correcto resuelto en la capa
   equivocada.
4. **Deriva de la retícula**, 2,2 px/s en diagonal sobre una trama de 64 px: da la
   vuelta cada 29 s y no se ve saltar. El barrido rápido que mareaba el 18/08 era
   ocho veces más rápido que esto. Y **el personaje respira y su engranaje gira**:
   la marca prometiendo mecánica y moviéndose como tal.
5. **Remate de marca.** El vídeo dejaba de existir sobre una negación
   («*No es un test.*», MDS-004). Ahora, en los últimos 1,25 s de la escena de
   cierre, el texto se retira, el personaje se queda mirando y entran el nombre
   del canal y la cita del día siguiente. **La regla 12 no se toca**: la crítica
   sigue ahí; simplemente deja de ser lo último que se ve.

Además, dos arreglos de composición que salieron al mirarlo:

- **El encuadre estaba medio vacío.** `padding: 300px 76px 700px` con anclaje
  arriba dejaba el 40 % inferior en negro y el personaje flotando en medio. Ahora
  el contenido ocupa la banda segura real y el personaje se apoya abajo a la
  izquierda, fuera de la columna de botones de Shorts, a 250 px en vez de 172.
- **El cuerpo de letra se ajusta a cuánto texto hay.** «Chiste número uno» a
  100 px dejaba el 70 % del encuadre vacío; ahora una frase de hasta cinco
  palabras sube a 150 px. Lo decide el recuento de palabras, no el ojo.
- **El diagrama en vertical se apila.** Tres cajas repartidas sobre 1920 px metidas
  en 1080 px dejaban la letra en 26 px, ilegible en un móvil. MDS-005 tiene una
  escena de ese tipo y habría salido así hoy.

**Verificación (regla 11.2, mirar antes de publicar).** Se renderizó MDS-005
completo con el cambio: **1.274 fotogramas frente a 185**, y de 59 pares de
fotogramas consecutivos, **cero idénticos** (antes, todo el tramo central era el
mismo fotograma repetido). Se comparó con el vídeo actual lado a lado antes de
tocar nada del repositorio.

---

## 5. Decisiones sobre lo que estaba pendiente desde el 24/08

**El diff de `montaje.py`: aprobado y aplicado.** La revisión del 24/08 encontró
que `qa.py` no puede saber si se quemaron subtítulos de verdad, porque
`montaje.py` no deja rastro de lo que hizo (sí lo deja de la música, en
`musica.json`). Propuso cinco líneas para que `montar()` escriba
`montaje.json` con `subtitulos_quemados`. No cambia ni un fotograma del vídeo:
solo escribe un fichero al terminar, para que el expediente de calidad diga
`true`/`false` en vez de `null`. `montaje.py` está protegido (regla 11.7) y
Silvestre delegó la decisión en esta conversación: **aplicado**.

**C6.3 (zoom preescalado en FFmpeg): rechazado y cerrado.** Lo resuelve la capa 3
de C15 en el navegador, sin preescalar y sin coste. La medición del 24/08 no se
tira: es la que demuestra por qué no se hace en FFmpeg.

**C6.2 (capa viva): entregado por C15.2, 15.3 y 15.4.** Se cierra.

**La regla del resaltado, aclarada.** La práctica se había ido de la norma y la
norma estaba mal escrita. Queda así:

- **Ámbar (`*palabra*`)** — el acento de la frase. La palabra sobre la que cae el
  énfasis. **Una por escena**, o deja de ser un acento.
- **Cian (`_palabra_`)** — el término del oficio: el nombre que la investigación
  le da a la cosa («conector», «autodestructivo», «ruptura benigna»). No es
  decoración: es el vocabulario que el espectador se lleva.
- **Coral** — lo que falla. Reservado al cierre.
- Se retira «el cian es para cifras». Las cifras tienen su propio tipo de escena
  (`dato`) y no necesitan color.

Con esta regla, el `autodestructivo` en cian de MDS-004 **estaba bien**, y lo que
estaba mal era la norma.

**Las miniaturas con cara de duda: ni prueba ni error, un descuido.**
`miniatura.py` tenía `expresion="duda"` escrito a fuego en la firma de la función
y **nadie le pasaba nunca otra cosa**. Las tres miniaturas salieron con la cara que
el canal usaba de avatar antes porque era el valor por defecto, no porque alguien
lo eligiera. Arreglado: ahora manda el guion — `miniatura_expresion` si la trae,
si no la expresión del personaje en la primera escena que lo use, y `neutra` como
último recurso.

**`DESCRIPCION_SERIE` de «Ríete primero, te explico después»: añadida.** La lista
de reproducción se crea una sola vez, el lunes 31 con MDS-006; sin esa entrada se
habría creado con la descripción vacía y ya no se arregla sola.

**Fin de línea: `.gitattributes` nuevo.** El 28/08 `git status` daba 587 líneas
modificadas en ocho ficheros que nadie había tocado: CRLF de Windows contra LF del
bot. Esos ficheros son justo los que el workflow hace `pull --rebase` y `push` al
terminar cada producción. Un día se cruzan y el rebase falla en mitad de una
publicación.

---

## 6. Lo que sigue sin resolverse, y de quién es

- **`demanda_bruta.json`** — no existe porque `demanda.yml` no llegó a correr el
  jueves 27. Con los crons nuevos debería correr el 3 de septiembre. Si vuelve a
  fallar, el problema no es la hora y hay que mirar el workflow.
- **`metricas.json` sigue vacío.** `metricas.yml` entró en el repositorio el 24 de
  agosto **después** de su hora de lunes, así que su primera ejecución programada
  sería el 31. **Es el cuello de botella real del proyecto**: tres semanas
  publicando y cero lecturas. Se lanza a mano hoy en vez de esperar al lunes —
  entre otras cosas, para saber hoy si el token nuevo tiene de verdad permiso de
  analítica, y no descubrirlo el lunes.
- **Ficha `E02` de `01_bibliografia/BIBLIOGRAFIA_CURADA.md`** — le faltan las tres
  cifras de MDH-004 y el DOI no coincide con el de Wiley. No es de ninguna tarea
  programada: no tiene dueño asignado. **Se le asigna a la revisión diaria**, que
  es quien encuentra estos defectos, con la regla de que solo puede añadir lo que
  verifique contra la fuente.
- **MDH-004 con 19 escenas por encima de 10 s.** La planificación hizo bien en no
  tocarlo: el umbral bajó después de adaptarlo y se produce mañana. Son avisos, no
  errores. Se decide con el vídeo del sábado delante.
- **El estimador de duración de `validar_guion.py` se queda corto** (asume 150
  palabras/minuto; la voz real hace 130 en Shorts). La revisión del 28/08 lo midió
  bien y acertó al no tocarlo con cuatro muestras. Se retoma cuando haya ocho.

---

## 7. Cambios en las tareas programadas

**La revisión diaria pasa de las 07:00 a las 11:30 (hora española).** Dos motivos,
los dos medidos esta semana:

1. **A las 07:00 el vídeo del día muchas veces no existe todavía.** La revisión del
   27 miró MDS-003 y la del 28 miró MDS-004: dos días seguidos revisando el vídeo
   de anteayer. Con la producción terminando entre las 03:38 y las 09:00, a las
   11:30 ya está.
2. **Los viernes, la entrega de la planificación del jueves aún no está en
   GitHub.** Silvestre no va a hacer un commit de madrugada y no tiene por qué:
   commitea sobre las 08:40. La revisión del viernes 28 se encontró la base caduca
   y **se saltó los pasos 1 y 2 enteros**. A las 11:30 ya está aplicada.

Se le añaden además tres cosas al prompt: que el `estado` de
`registro_publicaciones.json` es el del **momento de la subida** y no el actual
—por eso el 28 hablaba de MDS-004 «en privado» cuando ya estaba publicado—; que
desde el 31 el modo es `automatico` y esa ambigüedad desaparece sola; y la ficha
`E02` como tarea suya.

---

## 8. Infraestructura: las dos preguntas de Silvestre

**La tarjeta. No hace falta, y por eso no se hace.**
La tarjeta era para Gemini TTS (C7 escalón 2). Resulta que
**`gemini-3.1-flash-tts-preview` tiene nivel gratuito, con la salida de audio
incluida**, y la `GEMINI_API_KEY` ya está en los secretos. Seis piezas por semana
no se acercan a los límites del nivel gratuito. Meter una tarjeta —virtual o
real— para algo que no cuesta dinero es añadir el riesgo sin comprar nada: choca
con la regla 4 y con el sentido común. Si algún día hace falta de verdad, se
vuelve a plantear entonces, con la cifra delante.

Aviso técnico para cuando se haga el cambio de voz: **Gemini TTS no devuelve marcas
por palabra** y `voz.py` calcula la duración de cada escena con la marca de la
última palabra. Antes de cambiar de voz hay que sacar esa duración del propio MP3
(`ffprobe`), que es un cambio pequeño y contenido. Los subtítulos quemados, que
eran el otro consumidor de esas marcas, ya no se usan, y C15 no las necesita: el
revelado va por tiempo.

**El conector de GitHub: sí, pero sabiendo qué resuelve y qué no.**
Resuelve el trabajo manual de Silvestre en las conversaciones con él delante.
**No resuelve el problema de las entregas pendientes**, que era la esperanza: las
tareas programadas corren en la nube, sin el ordenador de Silvestre conectado, y
los conectores del escritorio pasan por ese puente. La planificación del jueves va
a seguir entregando un `.tar.gz`. Por eso la revisión diaria se mueve a las 11:30
en vez de esperar a que el conector lo arregle.

Recomendaciones: limitar la instalación de la app de GitHub **a este repositorio**
y no a toda la cuenta; y para otros proyectos con otras cuentas de GitHub, no
apilar conectores, sino un **token de acceso personal de grano fino con alcance a
un solo repositorio** por proyecto. Es lo que se replica bien.
