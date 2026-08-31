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

## Dónde está el proyecto a 31 de agosto de 2026

**Ya hay números, y son duros.** Tres semanas de canal, dos de Shorts:

| | Vistas de por vida | Suscriptores | Comentarios | Me gusta |
|---|---|---|---|---|
| MDH-001 · 002 · 003 (largos) | 13 · 28 · 8 | 0 | 0 | 4 |
| MDS-001 a 005 (Shorts) | 6 · 11 · 13 · 3 · 11 | 0 | 0 | **0** |

**El canal está en el peldaño S1 de la escalera nueva —que el feed de Shorts nos
pruebe— a un factor diez del umbral.** El criterio de aceptación de C2 (al menos
un Short por encima de 50 visualizaciones en 48 h) falló y se siguió produciendo
igual; queda dicho en `PLAN_DE_CAMBIOS.md`, versión 4.

**El único indicio bueno es la búsqueda:** MDS-002 sacó el 63,6 % de sus
visualizaciones de `YT_SEARCH` y MDS-003 el 46,2 %, mientras el feed de Shorts
—la superficie sobre la que se construyó toda la fase 1— aporta entre el 9 % y el
23 %. Números minúsculos, pero es la única señal direccional que hay.

**La publicación es automática desde hoy.** `parrilla.json` lleva `modo:
automatico` de MDS-006 en adelante; `cola.py` sube en privado con `publishAt` y
YouTube publica solo. MDH-004 (sábado 29) fue el último en modo `revision`: se
quedó oculto dos días hasta que Silvestre lo vio. Nadie mira el vídeo antes de que
salga y **`qa.py` corre después de la subida, así que es un informe y no una
barrera**: decisión consciente de Silvestre, tomada con la audiencia actual
delante.

**Lo que está en verificación, y en qué orden. Un cambio por producción:**

| Cuándo | Qué se mira |
|---|---|
| sem. 31 ago | **MDS-006, primer Short con C15.** La revisión diaria lo mira todos los días. Ningún cambio visual más entra hasta verlo |
| jue 3 sep | Prueba real del cron de `demanda.yml` con dos horas |
| sem. 7 sep | **C19 + C16** — el primer segundo deja de ser una tarjeta de texto, y entra el vocabulario dibujado empezando por la escena 1. Cuenta como un solo cambio |
| sem. 14 sep | **C7 escalón 1** — dos voces (`voz.py` autorizado desde el 28/08) |
| **dom 27 sep** | **Punto de control.** ¿Algún Short ha pasado de 100 visualizaciones en 48 h? Los tres desenlaces están escritos en `PLAN_DE_CAMBIOS.md`, versión 4 |

**Cambios de gobierno del 31/08:**

- **Se acabaron las notificaciones.** Las `PushNotification` que mandaban los
  agentes no le llegaban a Silvestre, y él no las quiere. Los tres prompts las
  tienen prohibidas. En su lugar, la revisión diaria mantiene
  **`05_calendario/ESTADO.md`**, un fichero de cinco líneas que sobrescribe cada
  día: estado OK o incidencia, último vídeo, próxima emisión, y una línea
  «Pendiente de Silvestre» que **casi siempre dice «nada»**.
- **Nadie vuelve a pedir el CSV de Studio.** Era trabajo recurrente (regla 5) y
  además nunca iba a medir los Shorts, porque Studio no da impresiones ni CTR para
  ellos. La escalera de Shorts se mide entera con la API.
- **Los prompts de las tres tareas programadas están espejados en
  `00_estrategia/tareas/`.** Vivían solo en el almacén de tareas programadas y no
  se podían leer sin arqueología. Ahora se leen en el repositorio — pero **la copia
  que corre es la del almacén**: si editas el fichero, actualiza también la tarea.

**Lo que está escrito y sin hacer:** el estimador de duración de
`validar_guion.py`, que asume 150 palabras/minuto cuando la voz real hace 130 en
Shorts; MDH-006, 007 y 008 sin adaptar al formato nuevo, a propósito, uno por
semana; el arreglo de C20 (el primer comentario ya no se publica en modo
automático), aplazado a propósito hasta que haya comentarios; y 46 fichas de la
bibliografía con el DOI «por verificar».

**Lo que se decidió y conviene no volver a discutir:** no se clona la voz de
Silvestre por ahora; no se encienden los subtítulos quemados; no se usan fotos de
banco de imágenes; no hace falta tarjeta, porque `gemini-3.1-flash-tts-preview`
tiene nivel gratuito con la salida de audio incluida; y no entra C10 (una página
por episodio) aunque la búsqueda funcione — sigue detrás del peldaño S1.

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
