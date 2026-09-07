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
6. 05_calendario/ESTADO.md         — ¿está el canal bien hoy? (cinco líneas)
7. 05_calendario/bitacora/         — los ficheros de los últimos siete días
8. 05_calendario/metricas.json     — dónde está el canal en la escalera

Y si necesitas el porqué de algo: 00_estrategia/DIAGNOSTICO.md.

Cómo trabajamos:

- Hablamos los lunes (datos y decisiones) y, mientras dure la fase de cambio,
  también los viernes (revisar lo que la planificación escribió el jueves).
  Fuera de eso, solo si algo se rompe, se pierde trabajo, se cruza una línea
  ética o un número se mueve fuerte.
- Escribes en los ficheros de mi carpeta con device_commit_files y yo hago el
  commit. Los ficheros de .github/workflows/ están protegidos contra escritura
  remota: si hay que crear uno, me lo mandas y lo creo yo a mano.
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

| Fichero | Estado | Alcance |
|---|---|---|
| `03_produccion/pipeline/voz.py` | **Autorizado el 28/08/2026** | Abierto. Se pidió para C7 (dos voces), pero el codirector no lo acotó |
| `03_produccion/pipeline/montaje.py` | **Autorizado el 28/08/2026, solo para una cosa** | El manifiesto de subtítulos (`montaje.json`), ya aplicado. Cualquier otro cambio necesita permiso nuevo |
| `.github/workflows/producir.yml` | **Sigue protegido** | Y además `.github/workflows/` no se puede escribir en remoto: se le manda el fichero al codirector |
| `.github/workflows/voz_prueba.yml` | **Entregado el 04/09, lo crea el codirector a mano** | Prueba de C7. `workflow_dispatch` solo, no escribe en el repositorio |
| `docs/` (la web del proyecto) | **Del codirector y mío**, desde el 04/09 | Tres páginas estáticas que Google exige para publicar la aplicación de OAuth. **No es C10** |
| `03_produccion/sonidos/` | **Entregada el 07/09** | Tres acentos CC0 con su `attribution_texts.md`. Ya están |
| `03_produccion/pipeline/montaje.py` **para P9** | **PENDIENTE — hace falta autorización nueva** | La del 28/08 cubría solo el manifiesto de subtítulos. Montar los tres sonidos es otro cambio y necesita permiso escrito aquí. **Hasta que esta fila diga «Autorizado», P9 no entra** |

**Y una cosa que ya no hace falta recordar de memoria:** cómo se saca el token de
YouTube y por qué caducaba está en **`00_estrategia/TOKEN_DE_YOUTUBE.md`**, con
la ruta exacta de la consola, el script que ya existía
(`04_agentes/obtener_token_youtube.py`) y la tabla de qué mirar si el canal deja
de publicar.

Otra decisión de propiedad, del 28/08: `01_bibliografia/BIBLIOGRAFIA_CURADA.md`
pasa a ser de la **revisión diaria**, que antes no tenía dueño y por eso
arrastraba defectos. Solo puede añadir lo que verifique contra la fuente.

---

## Seis trampas en las que ya se ha caído

No son anécdotas: cada una costó tiempo o un vídeo, y las cuatro se repiten
solas si nadie las tiene delante.

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

## Dónde está el proyecto a 7 de septiembre de 2026

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
