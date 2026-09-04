# Dirección — viernes 4 de septiembre de 2026

Conversación de dirección con Silvestre repasando de lunes a viernes. Cinco
decisiones, todas escritas en `00_estrategia/PLAN_DE_CAMBIOS.md`, **versión 5**.

## Lo primero: el número se ha movido

31, 21 y 21 visualizaciones en los tres últimos Shorts, contra una mediana de 11
en la primera tanda. Y el primer «me gusta» del canal. Sigue lejos de S1 (50
desde el feed en 48 h), pero es la primera señal buena en tres semanas y llega
**justo después de C15**, que era exactamente lo que el cambio prometía.

De las tres ramas escritas para el punto de control del 27, hoy estamos en la
segunda: va lento, el camino es bueno, se sigue.

## La pregunta del lunes: ¿por qué no se amplía el tema ya?

Sí, la lectura de Silvestre era correcta, y conviene dejar el motivo escrito
porque va a volver a doler antes del 27.

Ampliar el tema ahora no es «hacerlo antes»: es **destruir la única medición
limpia que vamos a tener**. C19 (el primer segundo deja de ser texto) y C7 (la
voz) todavía no se han soltado. Si ampliamos el tema a la vez y el número sube,
no sabremos cuál de las tres cosas lo movió, y el 27 de septiembre llegaremos
con la misma ignorancia que hoy pero una semana menos de margen. La regla de un
cambio por producción no es burocracia: es la única forma de aprender algo con
seis vídeos a la semana y veinte espectadores.

Lo que sí está hecho es preparar el terreno: la planificación metió el 03/09 dos
sondas en las semillas del jueves 10 —«cómo mantener una conversación sin
quedarse en blanco» y «cómo caer bien en una primera conversación»—, así que si
el 27 toca abrir esa conversación, se abrirá con cifras medidas y no con
opiniones. Medirlo cuesta cero.

## C23 · El token de YouTube deja de caducar

**El problema real no era el token: era el modo de prueba.** Una aplicación de
OAuth con la pantalla de consentimiento en «Prueba» recibe tokens de
actualización que **caducan a los siete días**, y eso convierte el canal en algo
que se para solo cada semana si nadie se acuerda. Es la regla 5 (cero trabajo
recurrente) rota por diseño, no por descuido.

**La salida no exige inventarse nada, y el bloqueo estaba en confundir dos
cosas.** Publicar la aplicación y verificarla son pasos distintos:

- **Publicar** es un botón. Estado «En producción», y **el token deja de
  caducar**.
- **Verificar** es el formulario que pide web, política de privacidad, términos
  y vídeo de demostración — lo que Silvestre no tiene y no quiere inventarse.
  **No hace falta para publicar.** Solo para pasar de 100 usuarios o para quitar
  la pantalla de aviso.

Lo que se paga por no verificar: una pantalla de «Google no ha verificado esta
aplicación» al dar el consentimiento (una vez, se pasa por *Configuración
avanzada*) y un tope de 100 usuarios de por vida. Necesitamos uno.

**El riesgo que sí hay, dicho sin adornar.** La documentación de la API de
YouTube dice que los vídeos subidos por `videos.insert` desde proyectos sin
verificar creados después del 28/07/2020 quedan restringidos a privado.
Empíricamente no nos está pasando: los nueve vídeos del canal se han subido en
privado con `publishAt` y YouTube los ha publicado solos. La auditoría de YouTube
es un eje distinto del estado de la pantalla de consentimiento, así que publicar
no debería cambiar nada — pero eso es razonamiento, no medición. **Se comprueba
con el vídeo del lunes 7**, en la revisión de las 11:30: si sigue apareciendo
`private` con `publicar_en`, no ha cambiado nada. Si apareciera bloqueado, se
vuelve a «Prueba» en un clic.

Descartadas y por qué: cuenta de servicio (YouTube no las acepta para subir a un
canal), renovar el token por workflow (Google no emite uno nuevo al usar el
existente: no hay nada que rotar sin pasar por el navegador), tipo «Interno»
(exige Workspace, la cuenta es de Gmail).

## C21 · La primera barrera real antes de publicar

**Lo que pasó el 3 de septiembre.** Se publicó un Short con «Más gener» en
pantalla: la palabra no cabía en el lienzo. La revisión diaria lo encontró siete
horas y media antes de publicarse, lo describió con precisión — y **no lo marcó
como incidencia**, razonando que no podía cancelar la publicación.

**Dos errores distintos, y el importante no es el que parece.**

El primero es el criterio de incidencia, que estaba al revés: que un agente no
pueda arreglar algo es el motivo para avisar, no para callar. Corregido en el
prompt (paso 6) con la regla explícita y el caso dentro.

El segundo, que es el de fondo: **llevamos dos semanas afinando revisiones sobre
un pipeline que no tiene ni una sola comprobación capaz de decir que no.**
`qa.py` corre después de subir, y la revisión no toca YouTube. Un texto que no
cabe en su caja es `scrollWidth > clientWidth`: pedirle a un agente que lo vea
mirando cinco fotogramas es pedirle que haga a ojo lo que el navegador ya sabe
con exactitud.

**La decisión:** `render.py` gana esa comprobación y falla el job si algo se
sale. Como el render corre antes que `publicar.py`, un fallo impide la subida.
Es la primera barrera previa a la publicación del proyecto — y se consigue **sin
tocar `producir.yml`**, que está protegido. Precio aceptado: un día sin vídeo si
salta y nadie lo arregla. Con veinte espectadores, sale más barato que una
palabra partida.

Y después, no antes, el arreglo de fondo: extender a `.cifra`, `.pie` y
`ul.lista` la escalera de tamaños que ya encoge `.enunciado`. Con la barrera
puesta, el umbral se elige midiendo en vez de adivinando.

## C22 · Los dos canales — sube a `REGLAS.md` como regla 14

**El caso: MDS-009, escena 2.** La voz decía «Curry y Dunbar preguntaron a la
gente de qué se reía y les emparejaron con desconocidos». En pantalla ponía «Con
dinero encima de la *mesa*», con cara de duda. El dinero venía de la `tesis` del
guion y **no se menciona en ninguna escena**. Quien lo vio mudo leyó una frase
suelta; quien lo escuchó no supo nunca que había dinero; y la cara era de duda
sobre algo que no tenía nada de dudoso.

La regla, en tres puntos: lo que se ve está sostenido por lo que se oye **en esa
misma escena**; lo esencial de la narración tiene correlato en pantalla; la cara
del personaje concuerda con lo que se dice.

Red de seguridad determinista, encargada a la revisión diaria: un **aviso** en
`validar_guion.py` que señale las palabras de contenido de `texto`, `cifra` y
`pie` que no aparecen en la `narracion` de su escena. Sobre MDS-009 tiene que
avisar de «dinero» y «mesa». Es tosco a propósito.

**Y este es el patrón que está funcionando en el proyecto:** comprobaciones
tontas y deterministas que le dicen a un agente listo dónde poner los ojos. El
aviso de C17 hizo el 3 de septiembre que la planificación tirara a la basura un
guion entero, ya escrito y validado, antes de publicarlo. No decidió: señaló.

## C7 · Se salta el escalón 1 de las voces

**Descartado, no aplazado.** Lo que está roto no es que haya una sola voz: es que
la voz que hay no tiene ritmo, ni pausa, ni entonación. Dos voces de `edge-tts`
entregan **dos lectores planos en vez de uno** y se comen la semana del 14 sin
tocar el problema.

El escalón 2 se encadenó detrás cuando parecía caro y arriesgado. Hoy sabemos
que el nivel gratuito de `gemini-3.1-flash-tts-preview` incluye la salida de
audio, que admite **dos hablantes en una sola llamada** y que el estilo, el
ritmo y el tono **se dirigen en lenguaje natural**, con etiquetas dentro del
propio texto. Eso es literalmente lo que falta.

**Escrito hoy:** `04_agentes/prueba_voz.py`, que genera tres audios del mismo
guion —`edge-tts` (la referencia), Gemini escena a escena con las pausas de hoy,
y Gemini en una sola llamada con dirección de actor— para escucharlos seguidos.
Corre en Actions por `workflow_dispatch`; el workflow `voz_prueba.yml` va aparte
porque `.github/workflows/` no se puede escribir en remoto.

**Una dependencia comprobada hoy en el código, para no descubrirla a mitad de
semana** (trampa 1: cuando quites algo, mira qué dependía de ello). `voz.py`
construye los subtítulos con las marcas por palabra de `edge-tts`, y Gemini no
las da. Pero **el `.srt` que se sube a YouTube se escribe por bloques de escena**
(`voz.py` línea 302), no por palabra: **sobrevive intacto al cambio de motor.**
Lo que muere es el `.ass` —que no se quema desde el 20/08— y con él el canario
`lineas_ass > 0` de `qa.py`, que habrá que sustituir por otra comprobación. No es
bloqueante; queda identificado.

## C24 · Que no todos los vídeos parezcan el mismo vídeo

Hallazgo de Silvestre del 2 y el 4: los contenidos están bien, los guiones
cierran mejor unas veces que otras, pero la presentación es idéntica en todos.
Cinco Shorts a la semana con la misma cara son cinco veces el mismo vídeo para
quien pasa por el feed.

Las cinco series ya existen y no se distinguen en pantalla. Darle a cada una su
acento —un color de apoyo dentro de la paleta, una composición de partida, un
tratamiento de fondo— es barato, determinista y no sube el coste de render.

**Va detrás de C7**, no por poco importante sino porque meter variedad visual
encima de C19 rompe la regla de un cambio por producción justo en la semana en
que hay que medir si C19 funciona.

**Y una cosa que dábamos por hecha y es falsa: la miniatura de un Short sí
importa.** En el feed no se ve; **en los resultados de búsqueda sí**, y la
búsqueda nos está dando el 46-64 % de las visualizaciones. C5 ya genera tres
variantes verticales con contraste medido; queda comprobar que se sube la buena y
que se lee a tamaño de resultado. Se mira el lunes 7.

## La sentencia sobre entretener

De Silvestre, y va a `REGLAS.md` (regla 3): **un vídeo no tiene que ser educativo
para valer.** Si entretiene y cumple las reglas —nada inventado, nadie como
víctima, la fuente donde toca—, es un vídeo bueno.

Y su corolario, que es donde estaba el riesgo real de que la planificación
derivara: `pertinencia_top5` —el campo que se inventó el 03/09— **descuenta
cifras, no descarta temas**. Está bien pensado y se queda: cuando once de veinte
consultas devuelven sketches y canciones, sus 63 millones de visualizaciones no
miden demanda de respuesta. Pero eso es lo único para lo que sirve. **Que hoy
responda una pregunta el entretenimiento y no la divulgación es un hueco, no una
señal de que el tema no sea nuestro.** Es la definición de un sitio donde nadie
ha llegado.

## Ficheros tocados hoy

- `00_estrategia/REGLAS.md` — regla 14 (los dos canales) y la sentencia sobre
  entretener dentro de la regla 3.
- `00_estrategia/PLAN_DE_CAMBIOS.md` — **versión 5** al final, y el aviso de
  cabecera apuntando a ella.
- `00_estrategia/PROMPT_DE_ARRANQUE.md` — estado a 4 de septiembre, trampa 7,
  autorizaciones.
- `00_estrategia/tareas/revision-diaria.md` — reescrito, espejo del prompt nuevo.
- `00_estrategia/tareas/planificacion-jueves.md` — sincronizado con el prompt
  nuevo.
- `04_agentes/prueba_voz.py` — **nuevo**.
- `05_calendario/bitacora/2026-09-04-direccion.md` — este fichero.

**Las dos tareas programadas están actualizadas en el almacén**, no solo en el
espejo: la revisión diaria antes de su ejecución de las 11:28 de hoy, y la
planificación antes del jueves 10.

**Fuera del repositorio, para que Silvestre lo cree a mano:**
`.github/workflows/voz_prueba.yml`.

## Lo que le toca a Silvestre, y no es recurrente

1. **C23, ~10 minutos, una vez:** publicar la aplicación de OAuth y regenerar el
   `YT_REFRESH_TOKEN`.
2. **`voz_prueba.yml`**: crearlo a mano y darle a *Run workflow*.
3. Escuchar tres audios y decir cuál. Eso decide C7.

---

# Segunda parte — tarde del 4 de septiembre

## `prueba_voz.py` falló por cuota, y el fallo era mío

Silvestre creó el workflow, lo ejecutó dos veces y las dos murieron con
`RESOURCE_EXHAUSTED`. El panel de Gemini decía **62 de 10.000 tokens por minuto**
y **4 de 10 peticiones al día** — todo verde salvo una línea: **3 de 3
peticiones por minuto**.

**El diagnóstico es de diseño, no de cuota.** El script pedía una llamada por
escena: seis para la pista «plana» más una para la dirigida, siete seguidas. El
RPM de 3 salta a la cuarta, y los dos intentos fallidos se comieron 4 de las 10
peticiones del día. El coste no estaba en el **tamaño** de lo que pedíamos —un
Short entero son ~300 tokens de entrada, el 3 % del límite por minuto— sino en
**cuántas veces** lo pedíamos.

## Y eso decide la arquitectura de C7, que es lo importante del día

Con **diez peticiones al día**, un episodio largo de cuarenta escenas troceado
por escena es imposible. **Una llamada por vídeo son seis peticiones a la
semana.** Así que, si Gemini entra, entra con el guion entero en una sola
llamada — que además es la forma en la que el modelo puede decidir el ritmo, que
era el objetivo de todo esto. Deja de ser una preferencia y pasa a ser la única
opción viable. No hay que volver a discutirlo.

**Lo que eso abre, y hay que resolver antes del 14:** si el audio viene de una
sola pieza, `render.py` no sabe cuánto dura cada escena y no puede sincronizar
el vídeo. Hoy eso era una pregunta abierta; ahora la prueba la contesta **sin
gastar ni una petición más**: la dirección pide una pausa clara entre líneas, y
el script analiza la onda devuelta —RMS por ventanas de 20 ms, sin dependencias—
cuenta los tramos de voz y los compara con el número de escenas del guion.

- **Si cuadran**, C7 escalón 2 es viable tal cual.
- **Si no cuadran**, el plan B es partir el guion en dos o tres llamadas (sigue
  cabiendo de sobra en diez al día) y cerrar el corte donde nos convenga.

Probado el detector contra una onda sintética de cinco tramos separados por
silencios de 0,6 s: los encuentra los cinco, con los bordes en su sitio.

## `prueba_voz.py`, reescrito

- **Dos peticiones por ejecución**, no siete: el guion entero sin dirección y el
  guion entero con dirección. Es además el A/B que de verdad importa.
- **25 segundos de espera** entre las dos, por el RPM de 3.
- **Reintento con espera** si salta el límite por minuto, y **salida limpia con
  explicación** si el que salta es el diario — que esperando no se arregla.
- **`--modelo`**: `gemini-2.5-flash-preview-tts` tiene **su propia cuota diaria**.
  Si se agotan las diez de 3.1 probando, se relanza con ese en vez de esperar a
  mañana. El workflow lo ofrece en un desplegable.
- **`informe.txt`** con el análisis de silencios de las dos pistas.

Sí, la pista «Gemini escena a escena» se cae de la prueba. Era el «cambio mínimo:
mismo troceado, motor nuevo», y ya sabemos que ese camino no cabe en la cuota, o
sea que medirlo era gastar seis peticiones en descartar algo ya descartado.

## El token de YouTube: `00_estrategia/TOKEN_DE_YOUTUBE.md`

Silvestre no recordaba dónde se tocaba esto, y no estaba escrito en ningún sitio
— que es exactamente cómo el 1 de septiembre se perdió una mañana. Ahora sí:
qué pasaba, la diferencia entre **publicar** y **verificar** (que es lo único que
hay que entender), la ruta exacta de la consola, el script que ya existía desde
hace semanas (`04_agentes/obtener_token_youtube.py`, que además pide los tres
ámbitos correctos), el orden en que hay que hacerlo, y una tabla de qué mirar si
el canal vuelve a dejar de publicar.

Incluye también los dos errores fáciles de cometer: **elegir el proyecto
equivocado** en la consola si hay varios, y **autorizar con la cuenta personal en
vez de con la de marca** — que falla al subir con un error que no dice eso.

## Ficheros tocados en la segunda parte

- `04_agentes/prueba_voz.py` — reescrito.
- `00_estrategia/TOKEN_DE_YOUTUBE.md` — **nuevo**.
- `00_estrategia/PLAN_DE_CAMBIOS.md` — C7.1 dentro de la versión 5.
- `00_estrategia/PROMPT_DE_ARRANQUE.md` — trampa 8 y el puntero al tutorial.
- `00_estrategia/LEEME.md` — el fichero nuevo en la tabla de lectura.
- `05_calendario/bitacora/2026-09-04-direccion.md` — esto.

Y fuera del repositorio, otra vez: **`.github/workflows/voz_prueba.yml`**, con el
desplegable de modelo. Sustituye al de esta mañana.

---

# Tercera parte — la prueba de voces, la barrera y el desbloqueo de OAuth

## 1 · Repaso de la barrera (C21): bien hecha, y con una consecuencia que no estaba prevista

Revisado el trabajo de la revisión diaria de hoy. Es sólido, y conviene decir por
qué para que se repita:

- `comprobarDesbordes()` mide con las propiedades del propio navegador, no con
  heurísticas; excluye lo que se sale a propósito (el `<svg>` del diagrama
  horizontal, que sobresale 40 px por diseño) y lo que no tiene caja HTML (los
  `<text>` de SVG, que se comprueban solo por rectángulo).
- **Calibró la tolerancia midiendo, no adivinando**: con margen de 1 px de alto
  habría bloqueado los 21 guiones, porque `line-height` fraccionario hace que
  `scrollHeight` supere a `clientHeight` entre 3 y 39 px en casi todas las
  escenas limpias. Puso 50 px de alto y dejó el ancho en 1, que es donde el
  barrido daba 0.
- Verificó las tres cosas que había que verificar: que el caso conocido
  (MDS-009) para el render, que un Short limpio sigue produciendo **exactamente
  el mismo número de fotogramas** (507), y un barrido de 351 escenas.

**Comprobado por mí, porque era el riesgo de verdad:** la línea
`pintar(0)` que repone el estado antes de capturar. `pintar(t)` es función pura
de `t` —no acumula nada, reescribe `innerHTML` desde `dataset.cuenta`— y además
`capturar(t)` llama a `pintar(t)` antes de cada captura, así que esa línea es
redundante y no puede alterar ningún fotograma. **La regla 11.5 sigue intacta.**

### La consecuencia: un agujero de calendario que la barrera acaba de abrir

`MDS-013` (martes 9) y `MDS-015` (viernes 11) **no renderizan**. Las notas están
en `revisiones/`, pero **quien aplica `revisiones/` es la planificación del jueves
10 — después de que MDS-013 se produzca.** El circuito de propiedad de ficheros
está pensado para defectos de contenido, que pueden esperar; con un defecto de
render, esperar cuesta el vídeo.

**No se arregla cambiando la propiedad de los ficheros** —eso volvería a abrir el
problema del 21 de agosto— sino quitando el defecto de la capa donde está: C21.1
sube a urgente y es el encargo del lunes.

### Y C21.1 no es lo que decía esta mañana

Los dos hallazgos nuevos lo demuestran: **`MDS-013` desborda con dos palabras**
(«Ruta *panorámica*.»), porque con cinco palabras o menos la escalera sube
`.enunciado` a 150 px. **La escalera mide número de palabras y lo que desborda es
el ancho.** Añadir `.cifra` a esa escalera habría sido repetir el error con otro
selector.

Lo correcto es cambiar el criterio: **encoger hasta que quepa** —medir, bajar un
4 %, volver a medir— con suelo de 64 px y la barrera detrás por si el suelo no
basta. Determinista, sin umbrales que adivinar, y retira la familia entera.

## 2 · La prueba de voces: lo que el oído no podía separar

Silvestre aprobó el cambio: las dos de Gemini mejoran a `edge`, entre ellas no
supo decidir, y notó que la plana suena más fuerte. Medidas las ondas, el empate
no lo era — el detalle está en `07_pruebas/prueba-de-voces.md` y en
`PLAN_DE_CAMBIOS.md` versión 5.1. Lo esencial:

- **La dirigida no lee las instrucciones en voz alta** (la sospecha razonable
  ante 83 s): su tiempo de voz, 41,3 s, coincide con el de `edge`, 41,4 s. Los 42
  segundos de más son **silencio**, por una instrucción mía de dejar pausas
  largas.
- **La plana corre**: 4,74 palabras por segundo contra las 2,63 del habla
  natural. Suena «más clara» porque es más densa y no respira.
- **El volumen no importa**: 2,2 dB en la voz sola, y `montaje.py` normaliza a
  −14 LUFS.
- **Cortar por silencios se descarta**: 16 y 33 tramos para 6 escenas, y ningún
  umbral da 6 (probado a 0,6 · 0,8 · 1,0 s → 8, 5 y 4).

**Decisión: una llamada por escena, sin pedir pausas, y solo en los Shorts.** El
largo son 40 escenas contra 10 peticiones al día. Seis salvaguardas escritas en
el plan y en el prompt de la revisión, y la más importante es la primera:
cualquier fallo de Gemini en una escena la sintetiza `edge-tts` y el vídeo sale
igual.

## 3 · OAuth: la consola pedía más de lo que decía, y la salida era una web

El botón «Publicar app» no bastaba: para pasar a producción externa hacen falta
**nombre, correo de asistencia, URL de página principal y URL de política de
privacidad**. Las dos URL no existían.

**Dos hallazgos, y el primero es una trampa:**

1. **El logotipo fuerza la verificación.** Lo dice la propia consola: «después de
   subir un logotipo, deberás enviar tu app para verificarla, a menos que…
   tenga el estado de publicación Prueba». Silvestre había subido `avatar.png`
   intentando desbloquear el botón, y eso empeoraba el problema. **Se quita.**
2. **Las dos URL se resuelven con GitHub Pages, gratis y sin inventarse nada.**
   El repositorio es público, así que Pages no cuesta. Escritas tres páginas en
   `docs/`: portada, política de privacidad y condiciones.

**La política de privacidad es verdad, y era fácil de escribir porque la verdad
es simple:** la aplicación no tiene usuarios aparte del propio canal, no recoge
datos de nadie, no comparte nada, guarda las credenciales como secretos cifrados
y las métricas que lee son las agregadas del propio canal. Con los enlaces a los
términos de YouTube y a la política de Google que exige el uso de su API. **No
hay un dato inventado en ninguna de las tres páginas, ni el nombre ni la cara de
nadie** (regla 6).

**Esto no es C10.** C10 —una página por episodio con guion, figuras y DOI— sigue
aplazado detrás del peldaño S1, por el mismo motivo de siempre. Lo de `docs/` es
el mínimo administrativo más una portada honesta. Si algún día se hace C10, se
construye encima.

Instrucciones completas, con la ruta de la consola y el paso de Search Console
por si pide verificar el dominio, en `00_estrategia/TOKEN_DE_YOUTUBE.md`.

## 4 · `07_pruebas/` se adopta como canal formal

La idea es de Silvestre y es buena: hay decisiones que no se pueden tomar
leyendo. Escrito `07_pruebas/LEEME.md` con la forma que tiene que tener una
prueba —qué mirar, **una** pregunta concreta, y qué pasa con cada respuesta— y
la regla de que la respuesta se añade al final del mismo fichero, con fecha y
firma. Una prueba respondida es la justificación escrita de una decisión.

La revisión diaria tiene ahora instrucción de mirar esa carpeta y de dejar ahí lo
que necesite que él vea u oiga.

## Ficheros tocados en la tercera parte

- `docs/index.html`, `docs/privacidad.html`, `docs/terminos.html` — **nuevos**.
- `00_estrategia/TOKEN_DE_YOUTUBE.md` — Parte A reescrita.
- `00_estrategia/PLAN_DE_CAMBIOS.md` — **versión 5.1**.
- `00_estrategia/tareas/revision-diaria.md` — espejo, cola de encargos nueva.
- `07_pruebas/LEEME.md` y `07_pruebas/prueba-de-voces.md` — **nuevos**.
- `05_calendario/bitacora/2026-09-04-direccion.md` — esto.

**La tarea de revisión diaria está actualizada en el almacén**, no solo en el
espejo.

## Lo que le toca a Silvestre

1. **GitHub → Settings → Pages → `main` / carpeta `/docs`.** Comprobar que
   responde antes de volver a la consola de Google.
2. **Quitar el logotipo** de la pantalla de consentimiento.
3. Rellenar los cuatro campos y **publicar**. Sin tocar «Preparar para la
   verificación».
4. Regenerar el token (partes B y C de `TOKEN_DE_YOUTUBE.md`).
