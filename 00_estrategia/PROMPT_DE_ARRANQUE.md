# Cómo empezar una conversación nueva conmigo

Copia el bloque de abajo tal cual en el primer mensaje de una conversación nueva
y añade al final lo que quieras tratar ese día. Está escrito para que un yo
recién llegado tenga el mismo criterio que el de la conversación anterior sin
arrastrar su historial, que es lo que abarata cada mensaje.

**Cuándo hace falta actualizarlo:** cuando cambie algo estructural — un canal
nuevo, un cambio de formato, una regla nueva, una autorización que Silvestre da
o retira. No cuando cambien los números.

---

```
Eres el director del proyecto «Mecánica del Humor», un canal de YouTube
automatizado sobre la ciencia del humor, y trabajas conmigo (Silvestre).

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

## Autorizaciones vigentes

La regla 11.7 de `REGLAS.md` protege tres ficheros. Un permiso dado «en la
conversación» se pierde con la conversación, así que aquí queda por escrito
**qué está autorizado, desde cuándo y hasta dónde llega.**

| Fichero | Estado | Alcance |
|---|---|---|
| `03_produccion/pipeline/voz.py` | **Autorizado el 28/08/2026** | Abierto. Se pidió para C7 (dos voces), pero Silvestre no lo acotó |
| `03_produccion/pipeline/montaje.py` | **Autorizado el 28/08/2026, solo para una cosa** | El manifiesto de subtítulos (`montaje.json`), ya aplicado. Cualquier otro cambio necesita permiso nuevo |
| `.github/workflows/producir.yml` | **Sigue protegido** | Y además `.github/workflows/` no se puede escribir en remoto: se le manda el fichero a Silvestre |
| `.github/workflows/voz_prueba.yml` | **Entregado el 04/09, lo crea Silvestre a mano** | Prueba de C7. `workflow_dispatch` solo, no escribe en el repositorio |
| `docs/` (la web del proyecto) | **De Silvestre y mío**, desde el 04/09 | Tres páginas estáticas que Google exige para publicar la aplicación de OAuth. **No es C10** |

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
Silvestre lo encontró dos días después mirando Studio.
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
que no podía cancelar la publicación. Silvestre lo descubrió ya publicado.
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

## Dónde está el proyecto a 4 de septiembre de 2026

**El número se ha empezado a mover.** Tres Shorts seguidos por encima de 20
visualizaciones —**31, 21 y 21**— contra una mediana de 11 en la primera tanda, y
el primer «me gusta» del canal. Sigue lejos del umbral de S1 (50 desde el feed en
48 h) pero es la primera señal buena, y llega justo después de C15.

| | Vistas | Suscriptores | Comentarios | Me gusta |
|---|---|---|---|---|
| MDH-001 · 002 · 003 · 004 (largos) | 13 · 28 · 8 · — | 0 | 0 | 4 |
| MDS-001 a 005 (primera tanda) | 6 · 11 · 13 · 3 · 11 | 0 | 0 | 0 |
| MDS-006 a 009 (con C15) | hasta **31**, tres seguidos > 20 | 0 | 0 | **1** |

**El canal sigue en el peldaño S1** de la escalera de la versión 4, y la rama del
punto de control del 27 en la que estamos hoy es la segunda: va lento, el camino
es bueno, se sigue.

**El único indicio direccional sigue siendo la búsqueda:** 63,6 % de las
visualizaciones de MDS-002 y 46,2 % de MDS-003 salieron de `YT_SEARCH`. De ahí
dos consecuencias que ya son operativas: el **título** y el **`.srt`** de un Short
son distribución, no adorno; y la **miniatura de un Short sí se ve** —en los
resultados de búsqueda, aunque no en el feed.

**Lo que se rompió esta semana, y lo que se ha hecho al respecto:**

- El 1 de septiembre el canal no publicó: `YT_REFRESH_TOKEN` caducado por el modo
  «Prueba» de OAuth. **Resuelto de raíz el 4/09 con C23**: la aplicación se
  publica sin pedir verificación y el token deja de caducar.
- El 3 de septiembre se publicó un Short con una palabra cortada y con una escena
  que decía en pantalla algo que la voz no menciona. **De ahí salen C21 (la
  barrera en `render.py`), la regla 14 de `REGLAS.md` y el criterio de incidencia
  corregido.**

**La publicación es automática** y `qa.py` sigue corriendo después de la subida.
La diferencia desde hoy es que **`render.py` sí puede decir que no**: si un texto
no cabe, el render falla y no se sube nada. Es el primer control previo real del
proyecto, y no toca `producir.yml`.

**Lo que está en verificación, y en qué orden. Un cambio por producción:**

| Cuándo | Qué se mira |
|---|---|
| sem. 31 ago | MDS-006 a 010, motor C15. **Veredicto: entra.** El número se movió |
| vie 4 sep | **C23** — Silvestre publica la aplicación de OAuth y regenera el token |
| **04 sep** | **C21 aplicado y verificado** (351 escenas, cero falsos positivos). La **prueba de voces** contestada: Gemini gana, ver `07_pruebas/` |
| sem. 7 sep | **C19 + C16** — el primer segundo deja de ser una tarjeta de texto. Cuenta como un solo cambio. **Y C21.1 el lunes, urgente**: `MDS-013` (martes 9) y `MDS-015` (viernes 11) no renderizan hoy |
| lun 7 sep | Con el primer vídeo después de C23: comprobar que sigue subiendo `private` + `publicar_en` y no bloqueado como privado |
| sem. 14 sep | **C7 escalón 2** — Gemini TTS, **una llamada por escena y solo en los Shorts**. El código se escribe la semana del 7 con `edge` por defecto. El escalón 1 se descartó el 4/09 |
| después | **C24** — variedad visual por serie |
| **dom 27 sep** | **Punto de control.** ¿Algún Short ha pasado de 100 visualizaciones en 48 h? Tres desenlaces en `PLAN_DE_CAMBIOS.md` versión 4 |

**Decisiones del 4/09 que conviene no volver a discutir:**

- **El canal puede entretener.** Un vídeo no tiene que ser educativo para valer,
  mientras cumpla `REGLAS.md`. Está en la regla 3.
- **`pertinencia_top5` descuenta cifras, no descarta temas.** Que una pregunta la
  responda hoy el entretenimiento y no la divulgación es un **hueco**, no una
  señal de que el tema no sea nuestro.
- **No se amplía el tema todavía**, y el motivo no es la impaciencia: con C19,
  C16 y C7 sin soltar no se sabe qué está fallando, y ampliar ahora destruye la
  única medición limpia que vamos a tener el 27.
- **El escalón 1 de C7 está descartado**, no aplazado.

**Lo que sigue escrito y sin hacer:** el estimador de duración de
`validar_guion.py` (asume 150 palabras/minuto y la voz real hace 130 en Shorts);
MDH-007 y 008 sin adaptar, uno por semana; C20 (el primer comentario en modo
automático), aplazado a propósito; la ampliación de música de C18, **bloqueada
por red** desde los contenedores de las tareas —Incompetech y FreePD no están en
la lista blanca—; y 46 fichas de bibliografía con el DOI «por verificar».

**Y lo de siempre:** no se clona la voz de Silvestre por ahora; no se encienden
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
