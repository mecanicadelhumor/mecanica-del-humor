# Registro de mejoras

Historial de lo observado en los vídeos ya producidos y de lo que se ha hecho al
respecto. Se **añade al final**, nunca se reescribe: sirve para no repetir
errores y para no volver a discutir decisiones ya tomadas.

Lo alimenta la revisión diaria de las 07:00 y cualquier sesión que mire un vídeo.

---

## 18 de agosto · MDH-002.es (producción de prueba, sin subir)

Primera revisión con fotogramas reales, a partir de `05_calendario/qa/MDH-002.es/`.

### Lo que está bien

- Audio correcto: −14,25 LUFS (objetivo −14), pico −1,22 dBTP (límite −1,0),
  rango 3,1 LU. La normalización de `montaje.py` funciona.
- Colchón de entrada: el silencio inicial acaba en 0,629 s, justo donde debe.
  **El falso arranque de la voz no aparece** — al menos en español.
- La rotación de música eligió `cama_02_dusk_next_route.mp3`, la que le tocaba
  al episodio 02.
- Las escenas de tipo `comparacion` y `lista` se leen bien y con jerarquía clara.

### Fallos encontrados

1. **No hay subtítulos quemados.** Seis fotogramas repartidos por todo el vídeo,
   ninguno con subtítulo en pantalla. Es grave por partida doble: se pierde la
   accesibilidad y, sobre todo, los subtítulos palabra a palabra son *lo único
   que se mueve* durante el tramo central de cada escena, que es estático por
   diseño. Sin ellos el vídeo se percibe como un pase de diapositivas — que es
   exactamente el diagnóstico que dio Silvestre sobre los dos primeros vídeos.

   Causa probable: `voz.py` construye los subtítulos con las marcas de tiempo por
   palabra que devuelve el sintetizador (`WordBoundary`), y si esa lista viene
   vacía escribe un `.ass` con cabecera y sin una sola línea. `montaje.py` lo
   quema sin error y sin efecto. Nadie avisaba.

   *Hecho:* `voz.py` avisa y cuenta las marcas; `montaje.py` avisa si monta sin
   subtítulos y dice por qué; `qa.py` registra en la ficha `subtitulos.quemados`
   y el número de líneas, que es lo que distingue si el fallo está en la voz o en
   el montaje. El `.ass` se guarda ya entre los artefactos. **Pendiente de
   confirmar con la producción del 19.**

2. **Los titulares nunca se han visto como estaban diseñados.** `escena.html`
   pide Archivo Black; el runner solo instalaba `fonts-inter` y
   `fonts-jetbrains-mono`, y Archivo Black no está en los repositorios de Ubuntu.
   Los titulares caían a Inter en peso 700 mientras los enunciados piden 800: la
   jerarquía visual estaba invertida.

   *Hecho:* se descarga la fuente en el propio job, con aviso si falla.

3. **El ámbar ha perdido su función.** La regla es un resaltado por pantalla. En
   la escena 9 había dos (*quién* y *dónde*) y en la 18, tres. Cuando todo está
   resaltado, nada lo está.

   *Hecho:* corregido en MDH-002.es. Los guiones siguientes lo respetan.

4. **Escena 18 de 20,4 s reales**, por encima del máximo de 20 que impone el
   validador. La estimación a 150 palabras por minuto se queda corta frente a la
   voz real, que va a −4 %.

   *Hecho:* recortada. **Pendiente:** calibrar `PPM` en `validar_guion.py` con
   las duraciones reales de varios episodios, en vez de dejarlo en 150.

5. **Los fotogramas de QA se tomaban a ciegas.** El primero cayó en mitad de un
   fundido entre escenas y salió al 20 % de opacidad: inservible.

   *Hecho:* `qa.py` calcula los instantes a partir de `guion.timed.json` y apunta
   al 60 % de cada escena, cuando la entrada ya terminó y la salida no ha
   empezado.

### Error editorial, detectado por Silvestre y no por el sistema

El arranque de MDH-002.es era **un calco del chiste inglés**: «un hombre entra en
un bar… y se agacha, porque el bar es de hierro». En inglés *bar* significa a la
vez local y barra, y el chiste existe; en español no hay doble sentido y la
escena no era un chiste, era una frase rara. El cierre remataba con el mismo
calco.

*Hecho:* sustituido por un chiste nativo en español cuya gracia no depende de
ninguna palabra concreta, sino de que rompe una norma social sin que pase nada
—es decir, el propio gancho **es ya** una violación benigna, que es lo que el
vídeo explica después. El cierre lo desmonta con las dos condiciones.

*Lección de sistema:* `validar_guion.py` comprueba estructura, no si un chiste
funciona. Ningún agente estaba leyendo el guion antes de producirlo. La revisión
de las 07:00 pasa a revisar **también el episodio del día siguiente**, que
todavía no se ha producido y da veinte horas de margen. Un calco del inglés al
español, o al revés, es motivo de bloqueo.

---

## 19 de agosto · revisión de las 07:00

Equipo de Silvestre apagado: trabajo hecho sobre un clon del repositorio público
y entregado como paquete. Mirado: `parrilla.json`, `registro_publicaciones.json`,
los seis fotogramas y la `ficha.json` de `qa/MDH-002.es/`, la vista previa del
18/08, y los guiones `MDH-003.es` y `MDH-003.en` de principio a fin.

### 1. El canal inglés se quedó sin vídeo. Hace falta mirar el log

La parrilla pedía `["es", "en"]` para hoy y solo hay **MDH-002.es**
(`youtu.be/NYNKFNJAsLc`, privado, subido a las 03:42 UTC). De **MDH-002.en** no
hay ni entrada en el registro ni carpeta en `qa/`, y su guion existe desde el 18.

Lo que se puede deducir sin el log, por cómo está escrito `producir.yml`:

- `registrar.py` omite lo que no tenga `publicado.json`, y el paso de expediente
  omite lo que no tenga `final.mp4`. Que falten **las dos cosas** dice que el
  inglés no llegó a montarse, no que fallara al subirse.
- Pero los pasos de voz, render y montaje son bucles `while` con `set -e`: si el
  inglés hubiera reventado en cualquiera de ellos, el job habría muerto **antes**
  de subir el español. Y el español se subió.

Las dos cosas juntas solo encajan si **en el plan nunca hubo trabajo inglés**.
Las dos causas compatibles con eso son (a) el job se lanzó a mano con
`--guion .../MDH-002.es.json`, que produce un plan de uno solo, o (b) se agotó el
`timeout-minutes: 150` — el commit sale 2 h 42 min después de la hora del cron.

**No se toca nada.** Hay que abrir el run de esta noche y leer el paso «Recuperar
el plan»: ahí está escrito, literalmente, si el plan traía uno o dos trabajos.

### 2. Subtítulos quemados: confirmado, y el fallo está en `voz.py`

Era lo que quedaba pendiente del 18. La ficha de hoy lo cierra:

    "subtitulos": { "ass_existe": true, "lineas_ass": 0, "quemados": false }

Con `lineas_ass` a 0, el `.ass` se escribió con cabecera y sin una sola línea de
diálogo, así que `montaje.py` no tiene nada que quemar: **el fallo no está en el
quemado, está en la síntesis**. `edge_tts` no devolvió ni un solo evento
`WordBoundary`, pese a que el audio salió entero (338,3 s).

Lo confirman los seis fotogramas: ninguno lleva subtítulo. El tramo central de
cada escena vuelve a ser una diapositiva quieta.

Dato que apunta a la causa y que no estaba anotado: **`requirements.txt` no fija
la versión de `edge-tts`** (`edge-tts` a secas). Cada producción instala la
última que haya publicada, así que un cambio de comportamiento aguas arriba entra
solo, de un día para otro, sin que nadie toque el repositorio. Es la explicación
más simple de que esto funcionara y dejara de funcionar.

No se toca `voz.py` sin permiso, como manda el encargo. Propuesta para Silvestre
en el resumen.

### 3. Lo que sí está bien en MDH-002.es

- Audio: −14,24 LUFS y pico −1,3 dBTP. Dentro de objetivo, mejor que ayer en pico.
- Colchón de entrada: 0,629 s. Sin falso arranque.
- **Los titulares ya salen en Archivo Black.** Se ve en el fotograma de portada:
  «Por qué te ríes» es pesado y los enunciados quedan por debajo. La jerarquía
  está del derecho por primera vez. La descarga de la fuente en el runner
  funciona.
- El muestreo de fotogramas ya no cae en fundidos: los seis son legibles.

Dos cosas menores: en `qa/MDH-002.es/` hay **doce** .jpg y la ficha solo declara
seis — los otros seis son de la prueba del 18 y nadie los limpia, porque la poda
del workflow borra carpetas enteras, no ficheros sueltos dentro de una carpeta
que se reescribe. Y el fotograma de la escena «Tres formas de hacer algo benigno»
sigue llevando dos resaltados ámbar; ya estaba producido, no se toca.

### 4. Guion de mañana (MDH-003): corregido en los dos idiomas

Leídos enteros. No hay ningún calco como el del 002: el inglés está construido
sobre «too soon», que es expresión hecha y meme propio, no una traducción del
título español; y la cita de Steve Allen va en su idioma original. Las cifras
tienen fuente y las fuentes existen y son las correctas (A03 = «Too close for
comfort», A04 = el estudio del huracán Sandy). El callback cierra: el que se
tropieza en la escena 1 vuelve en la penúltima, y se entiende.

Lo que sí había, y se ha corregido:

**Español** — era la versión más floja de las dos, y las correcciones son en su
mayoría cosas que el guion inglés ya resolvía bien:

- Escenas 6, 11 y 21: cuatro, dos y tres resaltados ámbar en la misma pantalla.
  Reducidos a uno, siguiendo el criterio que el inglés ya aplicaba (resaltar solo
  el primer elemento de la enumeración).
- **Cinco escenas `enunciado` seguidas (24 a 28)**, justo antes del cierre: el
  tramo más quieto del vídeo, y encima el que más peso emocional lleva. Y otras
  tres seguidas al principio (2-3-4). Se han convertido la 3 en `comparacion`
  («La misma acera. Dos finales.»), la 25 en `comparacion` y la 26 en `lista`.
  Son las mismas soluciones que el guion inglés ya usaba en esos tres puntos: se
  ha traído la estructura, no la traducción. Ninguna racha pasa ya de dos.
- Escena 28: el texto en pantalla repetía la narración palabra por palabra. Ahora
  el ojo recibe «Ya se había *levantado*.» y el oído la frase entera.
- Escenas 14 y 21, las dos más largas (17,8 s y 17,3 s estimados): recortadas a
  16,6 y 16,9. La estimación va a 150 ppm y la voz real va a −4 %, así que 17,8
  estimados quedaban a un pelo del máximo duro de 20 s.
- Las `notas_humor` señalaban escenas que no eran: el literalismo del «mando»
  está en la 12, no en la 9, y la rebaja está en la 18, no en la 21. Corregido.

**Inglés** — estaba mejor, y los arreglos son de sistema de color:

- Escenas 3, 10 y 25 usaban el cian (`_así_`) como énfasis, cuando el cian es
  para datos. En la 3 el resalte sí era el mecanismo y ha pasado a ámbar
  (`*evaporates*`); en la 10 y la 25 se ha quitado la marca.
- Pronombre inconsistente: el gancho decía «Somebody… laughs with **them**» y
  luego las escenas 3 y 29 pasaban a «he». Unificado en «they».
- Escena 29: mismo problema que la 28 española, texto en pantalla igual a la
  narración. Cambiado.

`validar_guion.py` pasa los dos sin errores. En español ya no queda ningún aviso
de ámbar ni de racha de tipo; quedan los de escenas por encima de 14 s, que son
inherentes al ritmo de este episodio.

### 5. Mejora visual del día: V2, variantes de composición de `enunciado`

Antes, la comprobación pendiente: la vista previa del 18 (`_entorno.json` dice
`Archivo Black` presente, o sea que es fiable) confirma que el arreglo de la
tipografía funcionó. El muestrario de `enunciado` se lee bien y no desborda. Se
da por bueno.

Elegido V2 y **no V1**, que va antes en el backlog: V1 exige invocar un
`figura.py` nuevo desde `producir.yml`, y ese fichero no se toca sin permiso de
Silvestre. Queda anotado como bloqueado en `MEJORA_VISUAL.md`, no como pendiente.

V2 ataca justo lo que el validador viene señalando: el 48 % (es) y el 50 % (en)
de las escenas de MDH-003 son `enunciado`, y todas se veían igual. Ahora la
composición rota con el número de escena — centrada, a la izquierda con aire a la
derecha, y alta con la mitad inferior despejada — de forma determinista.

Desviación consciente respecto al backlog: la tercera variante iba a ser «a pie
de pantalla» y se ha hecho **anclada arriba**. La banda de abajo está reservada a
los subtítulos quemados (alineación 1, `MarginV 96`, cuerpo 58: de ~900 px hacia
abajo). Apoyar un enunciado en el suelo habría creado una colisión el mismo día
en que los subtítulos vuelvan a funcionar.

**Coste de render: sin cambios.** La escena `enunciado` sigue teniendo una sola
unidad animable — comprobado con `vista.py`, que informa «1 unidades» en las
tres variantes—, así que `render.py` captura exactamente los mismos fotogramas
que antes. No hay antes/después que anotar.

Se han añadido dos `enunciado` más al muestrario de `vista.py`, al final para no
correr la numeración de los ocho PNG que ya existen. Con eso el ejemplo de arriba
cae en n=2 y los nuevos en n=9 y n=10, así que la vista previa enseña las tres
variantes de una vez.

**Pendiente para mañana:** mirar `03_produccion/vista_previa/muestrario_02`, `_09`
y `_10_enunciado.png` con las tipografías reales y revertir si alguna variante
desborda o queda peor. La variante de la izquierda es la que menos se nota con
textos cortos: lo suyo es juzgarla con el enunciado largo del muestrario.

### Para Silvestre, que no decido yo

1. **`edge-tts` sin versión fijada en `requirements.txt`.** Fijarla a la última
   que se sepa que devolvía `WordBoundary` es de una línea y es reversible, pero
   toca la reproducibilidad de todo el pipeline. Y si al fijarla siguen sin salir
   las marcas, entonces el cambio está en el servicio de Microsoft y hay que
   pensar el plan B dentro de `voz.py`, que es fichero protegido.
2. **Las comillas angulares « » en los guiones ingleses.** Están en los cuatro
   (001, 002, 003 y 004), así que es convención de casa, no un descuido del 003.
   Pero en inglés no se usan y en pantalla parecen francesas. Cambiarlo es
   decisión de canal y afecta a episodios ya publicados, así que no se toca.
3. **Los cuatro ejes de la distancia psicológica** (tiempo, espacio, social,
   hipotético) se citan como A03. A03 los usa, pero la taxonomía es de la teoría
   del nivel de constructo (Trope y Liberman), que no está en la bibliografía.
   No es un error de dato; es una entrada que falta.

---

## 19 de agosto · segunda vuelta, con feedback de Silvestre

Silvestre revisó MDH-002.es, lo borró de YouTube para reproducirlo, y pidió
sacar el inglés hoy mismo. Tres cosas encontradas, dos de ellas graves.

### 1. La escena 24 estaba truncada en el guion, en los dos idiomas

Silvestre lo describió como un fallo de audio: «en el ejemplo del avión la
segunda parte, el chiste en sí, no se lee, la voz dice "cero" y nada más».

No es audio. Es el guion. La narración decía, literalmente y completa:

    "La misma queja, dos versiones. «Los aviones son incómodos»: cero."

Y ahí se acababa. El chiste —el del brazo del asiento del medio— está escrito
en el panel B de la escena, o sea **en pantalla**, pero nunca estuvo en la
narración. La voz leyó exactamente lo que había. El fallo estaba a la vista en
el JSON desde el principio.

**El guion inglés tenía el mismo corte, palabra por palabra:** «Same complaint,
two versions. Flying is uncomfortable: zero.» De haberse producido anoche, el
vídeo inglés habría salido con el mismo agujero.

Corregidas las dos. Y una lección de sistema: `validar_guion.py` no detecta
esto. Comprueba estructura, ámbares, fuentes y duraciones, pero no que la
narración cubra lo que hay en pantalla. Un aviso barato sería *escena de tipo
`comparacion` cuyo panel B no aparece de ninguna forma en la narración*, o más
simple, *narración de menos de X caracteres en una escena que no es `titulo`*.
Ninguna de las dos se ha implementado hoy: hacía falta sacar el vídeo. Queda
propuesto.

### 2. «Violación» fuera del canal español

Decisión de Silvestre: la palabra tiene en español una segunda acepción que no
tiene en inglés, y basta para que un clasificador entierre el vídeo. Sustituida
por **«ruptura»**, que es la misma idea, funciona igual como sustantivo y encaja
en todas las construcciones donde estaba.

Tocadas nueve escenas de MDH-002.es (4, 5, 8, 9, 18, 23, 28, 31 y 32) y la 12
de MDH-003.es. En la 8 «una violación de tu espacio» pasa a «invade tu espacio»,
que en español es lo natural. El diagrama de las dos condiciones ahora dice
«Ruptura / Benigna». El cierre, «Ruptura *más* algo benigno. Nada más.»

También la descripción y las etiquetas de `publicaciones/MDH-002.es.json`.
Escribí primero «teoría de la ruptura benigna (benign violation theory)» para no
perder la búsqueda del término académico, y lo quité: metía en la descripción
del vídeo español justo la palabra que se quería evitar, en otro idioma pero
igual de legible para un clasificador. La atribución se sostiene con los nombres
de McGraw y Warren.

**En inglés no se toca.** «Benign violation» es el término académico y en inglés
no arrastra la segunda acepción. Los metadatos ingleses se dejan como estaban.

### 3. Comillas: angulares en español, inglesas en inglés

Ayer lo dejé como pregunta y Silvestre lo ha resuelto. Convertidas « » → “ ” en
`MDH-002.en`, `MDH-003.en`, `MDH-004.en` y en los metadatos de publicación
correspondientes. **MDH-001.en no se toca: ya está publicado.**

Faltaba una pieza que no estaba en los guiones: `escena.html` pone las comillas
de las escenas de tipo `cita` **por CSS**, con `blockquote::before/after`, así
que el canal inglés las habría sacado angulares aunque el guion no llevara
ninguna. MDH-002.en tiene una `cita` (escena 22), o sea que habría salido hoy
mismo. Ahora dependen de `html[lang]`, que `cargar()` ya fijaba con el idioma
del guion.

### 4. Sobre por qué no salió el inglés: lo que descarta el propio repositorio

Sigue sin poder confirmarse sin el log. Pero conviene anotar lo que **no** es,
para no volver a mirarlo: no es que faltara el guion (existe desde el 18), no es
la poda de `qa/` (borra carpetas enteras, y con dos no borra ninguna), y no es
un fallo de voz, render o montaje del inglés, porque esos pasos son bucles con
`set -e` y habrían tumbado el job antes de subir el español, que sí se subió.

Queda una hipótesis nueva que encaja mejor que las de ayer: que el inglés **sí
se montara y fallara al subirse**, por el secreto `YT_REFRESH_TOKEN_EN`. El paso
de subida hace `exit 1` explícito si ese token está vacío. Eso explicaría que no
haya `publicado.json` ni entrada en el registro. Lo que no explica del todo es
que tampoco haya carpeta en `qa/`, salvo que `qa.py` fallara después. Es lo
primero que hay que mirar en el log, y es de comprobación inmediata: si el
secreto no existe, no hay nada más que investigar.

Por eso la recomendación para relanzar es **un idioma por ejecución**, no los
dos en la misma. Aísla el fallo y quita de en medio el `timeout-minutes: 150`.

---

## 19 de agosto · tercera vuelta: el fallo estaba en las instrucciones

Silvestre, sobre lo de «cero»: *«no tiene ningún sentido. Queda mal y no se
entiende si no tienes la pantalla delante. Yo mismo consumo vídeos de YouTube
sin tener la pantalla delante, por lo que el audio debe ser autosuficiente.»*

Eso no es un incidente, es una regla de canal, y al ir a escribirla apareció de
dónde salía el fallo. `04_agentes/prompts/guionista.md` decía:

> **Nunca leas lo que está en pantalla.** El texto de la escena y la narración
> dicen cosas complementarias, jamás la misma.

La intención era buena —que el ojo y el oído no reciban lo mismo—, pero leída al
pie de la letra dice exactamente lo que el guionista hizo: el chiste estaba en
pantalla, así que no lo leyó. **El bug estaba en las instrucciones, no en la
ejecución.** Y por eso salió idéntico en los dos idiomas: los dos guiones
obedecieron la misma frase.

Reescrita en tres reglas que no se pueden malinterpretar: el audio es
autosuficiente; la pantalla no se lee palabra por palabra; y el criterio que
resuelve la tensión entre ambas, *lo que la pantalla enseña, la narración lo
dice con otras palabras — nunca se lo salta*. Con el caso de la escena 24
escrito debajo, para que la próxima vez que alguien lea ese prompt sepa por qué
está redactado así.

### La comprobación automática: lo que se ha hecho y lo que se ha descartado

Primero probé lo obvio: comprobar que el texto de pantalla está cubierto por la
narración, midiendo solapamiento de palabras. **Descartado.** Con ventana de una
escena marcaba 11 de 21 `comparacion` del repositorio; ampliando la ventana a
las dos siguientes (porque la narración a menudo continúa en la escena de al
lado) seguía marcando 10. Casi todos eran falsos positivos, y por una razón de
fondo: castiga la paráfrasis, que es justamente lo que un guion bien escrito
hace y lo que la regla de «ojo y oído distintos» exige. Un aviso que se equivoca
la mitad de las veces es un aviso que nadie mira.

Lo que sí se ha metido es una comprobación estrecha de la **firma** de una
narración truncada: que acabe en dos puntos y una sola palabra
(«…incómodos: cero.»), o colgando de dos puntos, coma o conjunción. Medido
contra los doce guiones del repositorio: **cero falsos positivos**, y pilla las
dos escenas 24 rotas.

Va como **error**, no como aviso: para la producción. Parar una producción se
arregla relanzándola; publicar un vídeo con el remate mudo, no. Si algún día
estorba, bajarlo a aviso es cambiar una palabra, y está dicho en el comentario.

Lo que **no** hace, y conviene tenerlo claro: no comprueba que el audio se
entienda con los ojos cerrados. Eso exige entender el guion, y para eso está la
lectura diaria. El portero solo reconoce la forma del corte.

---

## 19 de agosto · feedback del vídeo inglés ya publicado

MDH-002.en quedó en estado aceptable y Silvestre lo programó para las 17:00. Seis
observaciones suyas. Van por orden, con lo que se ha hecho en cada una.

### 1. Sigue habiendo una sílaba suelta al empezar el audio inglés

Confirmado que **la métrica actual no lo veía**. La ficha de MDH-002.en da
`silencio_inicial.acaba_s = 0.629`, exactamente el valor correcto, y el defecto
estaba ahí igual. La razón es que `silencio_inicial()` se para en el primer
`silence_end` y devuelve. Si la secuencia real es «colchón, sílaba, hueco,
narración», el primer silencio acaba justo donde debe y la medida sale limpia.

*Hecho:* `qa.py` gana `arranque()`, que lista **todos** los silencios de los
primeros 4 s con umbral de 0,12 s y marca el patrón. Probado contra dos casos
sintéticos: audio continuo → `fragmento_antes_de_la_narracion: false`; audio con
una sílaba de 0,18 s y un hueco de 0,35 s delante → `true`, y además devuelve
`duracion_fragmento_s: 0.18`, que es exactamente la que se había inyectado.

A partir de la próxima producción el fragmento deja de depender del oído de
nadie y sale como un booleano en la ficha, en los dos idiomas. Eso es lo que
permitirá saber si es solo del inglés, y si una eventual corrección funciona.

*No hecho, y por qué:* la corrección en sí va en `voz.py`, que es fichero
protegido, y **no se puede probar desde aquí**: el contenedor no llega al índice
de paquetes, así que no hay `edge-tts` con el que reproducir el fallo. Proponer
a ciegas un cambio en el fichero que ya costó un vídeo es exactamente lo que no
hay que hacer. Primero el dato, luego el arreglo.

### 2. La música se cortaba en seco al final — arreglado y medido

Encontrado, y no era falta de fundido: **el fundido existía y actuaba sobre el
silencio.**

`amix` lleva `duration=first` y su primera entrada es la voz, así que la mezcla
termina en `dur_voz`. El colchón posterior añade `apad` de 1 s de silencio, y el
`afade=t=out` se calcula sobre `dur_total` arrancando en `dur_total - 0,6`, que
cae **0,4 s después** de que la mezcla ya se haya cortado. Atenuaba el relleno.

Medido sobre material sintético, envolvente en ventanas de 0,1 s:

    ANTES     ...  10,4 s: −32,8 dB   10,5 s: −32,8 dB   10,6 s: silencio
    DESPUÉS   ...  10,4 s: −51,0 dB   10,5 s: −57,6 dB   10,6 s: silencio

*Hecho (pendiente de tu visto bueno, es `montaje.py`):* la música se apaga ella
sola antes del corte, con un `afade` de 1,5 s aplicado a `[musduck]` —después
del ducking, así que el sidechain sigue funcionando igual—. La voz **no** se
toca: comprobado en el peor caso, con narración sonando hasta el último
fotograma, la diferencia antes/después es de 0,0 dB en todo el tramo final.

### 3. La llamada a comentar: sí, pero con pregunta concreta

Recomendación: mantenerla, y que **no** sea una fórmula. La regla de «cero
muletillas de YouTube» del prompt del guionista sigue vigente y no choca con
esto: la muletilla es «déjamelo en los comentarios»; una pregunta que pide una
historia propia es contenido.

Funciona mejor porque el episodio ya le ha hecho recordar la historia al
espectador: al terminar el 003 cualquiera tiene en la cabeza la anécdota que
tardó en poder contar. Y el comentario que genera se lee bien, que es lo que
hace que otros comenten debajo.

*Hecho:* añadido al prompt del guionista, enganchado a la tarea de 24 horas que
el cierre ya pedía, con ejemplos de lo que vale y lo que no.

### 4. «violation» en inglés se queda

De acuerdo con el criterio de Silvestre: en inglés el delito es *rape*, palabra
distinta, así que *violation* no arrastra la segunda acepción. Los metadatos y
el guion ingleses se quedan como están. En español sigue siendo «ruptura».

Limpiados de paso los dos últimos «violación benigna» que quedaban en las
`notas_humor` del guion español. Son internas —no salen ni en pantalla ni en
audio— pero conviene que el término sea uno solo en todo el proyecto.

*Cambio de rutina, a petición suya:* la revisión diaria pasa a leer **todos los
guiones pendientes de producir**, no solo el del día siguiente. Recogido en las
tareas programadas.

### 5. La música repetida del 001 y el 002: no es la rotación

Comprobado con los hashes de los ficheros:

    cama.mp3                            3f93cfef…  ← la del episodio 1
    cama_02_dusk_next_route.mp3         3f93cfef…  ← la del episodio 2

Son **el mismo fichero byte a byte**. `cama.mp3` es la copia por defecto que ya
estaba antes de que existiera la rotación, y da la casualidad de que es copia de
la pista 02, que es justo la que a la rotación le tocaba dar al episodio 2. O
sea: el 001 no pasó por la rotación, y el 002 sí, y coincidieron.

**No hay nada que arreglar.** La rotación funciona. Los próximos:

    MDH-003 → Haru (LoFi version), de Roa
    MDH-004 → Crying Over You, de christophermorrow
    MDH-005 → Dusk, de Next Route

Tres episodios seguidos con tres pistas distintas.

### 6. Sin figuras ni imágenes

Sigue siendo V1 del backlog y sigue bloqueado por lo mismo: `figura.py` hay que
invocarlo desde `producir.yml`, que no se toca sin permiso. Es la mejora de más
impacto que queda pendiente y ya hay episodios que la piden a gritos —la curva
del huracán Sandy en el 003, el reparto de estilos de humor en el 005—. Propuesta
concreta en el resumen a Silvestre.

---

## 19 de agosto · fundido de música aplicado y V1 (figuras) construido

Silvestre da el visto bueno a los dos cambios que estaban esperándolo.

**`montaje.py`:** aplicado el `afade` de 1,5 s sobre `[musduck]`. Vuelto a medir
con el fichero ya en su sitio: la cola pasa de −33 dB a −58 dB en el último
segundo y medio en vez de caer de golpe. La voz sigue sin tocarse.

**V1, figuras.** Hecho `figura.py` y probado de punta a punta: genera el PNG,
escribe la ruta en el guion, y la escena renderizada por `escena.html` se ve
como debe —transparente sobre la retícula, ámbar para lo que importa, cian para
el resto, sin marco superior ni derecho—. Comprobadas las dos clases con datos
de ejemplo, curva y barras.

De paso, tres cosas que hacían falta y no estaban:

- `escena.html`: la plantilla de `figura` ignoraba el campo `titulo`. Una gráfica
  sin enunciado obliga al espectador a deducir qué está mirando. Ahora lo pinta
  como ya hacían `lista` y `comparacion`.
- `esquema_guion.json`: descrito el bloque `figura` (clase, x, y, etiquetas,
  `destacar`, `marca`).
- `validar_guion.py`: `imagen` deja de ser obligatorio en las escenas `figura`,
  porque **el validador corre antes que figura.py** y la imagen todavía no
  existe. A cambio, error si la escena no trae ni datos ni imagen. Los doce
  guiones del repositorio siguen pasando.

### Lo que NO se ha hecho, y es deliberado

**Ningún guion usa todavía una escena `figura`.** El motor está, pero meter una
exige números reales, y no los tengo.

La curva del huracán Sandy del 003 es la candidata evidente: el episodio la
describe en tres escenas seguidas («al principio casi nada, luego cada vez más,
luego otra vez menos») y una gráfica la contaría mejor que las tres juntas. Pero
los puntos de esa curva están en el artículo A04, no en mi cabeza. Dibujarla «a
ojo» y ponerle debajo `fuente: A04` sería fabricar un dato con aspecto de dato
verificado, que es justo lo que el criterio editorial del canal prohíbe y lo
contrario de lo que el nombre del canal promete.

Así que queda pendiente de que alguien saque las cifras del artículo. Es trabajo
del verificador o de Silvestre, no mío desde aquí. Mientras tanto el paso del
workflow es inocuo: sin escenas `figura`, no hace nada.

---

## 19 de agosto · feedback del vídeo español, y la sílaba no era del arranque

MDH-002.es producido en **8 minutos** —dato útil: la producción entera es
barata, así que el `timeout-minutes: 150` del job sobra con muchísimo margen y
producir dos idiomas en la misma ejecución nunca fue un problema de tiempo—.
Programado para las 17:00.

### 1. La sílaba suelta NO es un falso arranque

Es el hallazgo del día. Silvestre: *«en el minuto 5:35 se ha colado una sílaba
suelta en el audio como las que tenía el vídeo en inglés al principio»*.

Las dos veces anteriores apareció al empezar el vídeo, y de ahí salió el
diagnóstico de «falso arranque de la voz» y el cambio a la voz monolingüe. Era
un diagnóstico incompleto: **aparece al principio de cualquier escena**, no del
vídeo. Encaja con cómo funciona `voz.py`, que hace una petición por escena — y
también explica que el cambio a la voz monolingüe no lo arreglara del todo.

Consecuencia inmediata: `arranque()`, que añadí esta misma mañana, mira solo los
primeros 4 segundos. **No habría visto esta.**

*Hecho:* `qa.py` gana `fragmentos()`, que recorre el vídeo **entero** buscando
islas de sonido de menos de 0,45 s rodeadas de silencio, y devuelve el instante
en `mm:ss` para ir a escucharlo. Probado con audio sintético: pilla una sílaba
de 0,22 s metida a los 12,5 s y la reporta con el instante y la duración
exactos; sobre audio limpio y sobre el vídeo de prueba, cero. `arranque()` se
queda, porque comprueba además que el colchón de 0,6 s esté donde debe, pero el
que manda ahora es `fragmentos()`.

*Propuesto y no aplicado:* el recorte en `voz.py`, escena a escena. La detección
está probada (una escena con sílaba de 0,20 s + hueco de 0,25 s devuelve 0,45 s;
una limpia devuelve 0). Lo que **no** se puede probar aquí es el recorte sobre
audio real de edge-tts, porque el contenedor no llega al índice de paquetes.
`voz.py` ya costó un vídeo una vez, así que se queda como propuesta con el diff
escrito. Ojo con un detalle que no es obvio: al recortar hay que **restar el
mismo desplazamiento a las marcas de palabra**, o los subtítulos quedan
adelantados esa cantidad durante toda la escena.

### 2. Los subtítulos siguen rotos, y ya no hay duda de dónde

El log de esta producción lo dice con todas las letras:

    El sintetizador no ha devuelto marcas de tiempo por palabra (WordBoundary).
    Montando SIN subtítulos quemados: subtitulos.ass no tiene líneas.

Tercera producción seguida. Sigue siendo el defecto abierto más importante y
sigue sin poder reproducirse desde el contenedor. La sospecha de siempre:
`requirements.txt` no fija la versión de edge-tts.

### 3. «Cero» seguía sin entenderse, y el arreglo de esta mañana era a medias

Silvestre: *«lo de "cero" sigo sin entenderlo y creo que no se entiende»*. Tenía
razón y el diagnóstico de la mañana se quedó corto. El problema no era solo que
faltara la segunda mitad —eso ya se arregló—, sino que **«X: cero» es una
construcción de texto escrito**. En una diapositiva se entiende; dicha en voz
alta no significa nada.

Reescrita en español hablado en los dos idiomas: «La primera: "los aviones son
incómodos". Ahí no se ha reído nadie. La segunda: … Con esa sí.»

*Regla nueva en el prompt del guionista:* nada de construcciones que solo
funcionan escritas. Si al leerlo en alto hace falta ver la pantalla, está mal
escrito.

### 4. Transiciones entre bloques: el salto de ritmo

Silvestre: *«hay un cambio abrupto cuando se pasa de la parte de ruptura/benigno
a cuando habla de reconocimiento y familiaridad»*.

Es un defecto de guion que ningún validador va a detectar. La causa de fondo es
que la estructura se apoya en los rótulos de «Parte 2», «Parte 3» para marcar el
cambio de bloque — y **el rótulo lo ve el ojo**. Quien escucha sin mirar, que es
justo el caso que nos ocupa desde esta mañana, solo tiene la narración, y en la
narración no hay puente ninguno.

*Regla nueva en el prompt del guionista:* cada bloque entra desde el anterior con
una frase de transición que diga de dónde vienes y adónde vas. No vale el rótulo.

### 5. La voz suena robótica, sobre todo en español

Anotado como objetivo abierto, con las palabras de Silvestre: *«los chistes no
tienen mucha gracia porque están contados sin gracia»*. Es un límite real del
formato, no un fallo puntual: `es-ES-AlvaroNeural` es correcta y plana.

No hay decisión hoy porque no puedo escuchar candidatas desde aquí. Lo que se
puede hacer cuando toque, y sin coste: `voz.py` ya acepta `--voz`, así que
sintetizar el mismo párrafo con dos o tres voces y compararlas es una ejecución
manual del workflow, no un cambio de código. Cuando Silvestre quiera, se prepara
esa comparativa.

### 6. Lo que ya estaba bien

Sin cortes bruscos de entrada ni de salida: el fundido de música de esta mañana
funciona. El cambio de «violación» por «ruptura» le parece elegante. El
contenido, interesante.

Pendientes que se resuelven solos en el 003, sin hacer nada más: la rotación de
música (le toca Haru, de Roa — comprobado con `cola.py --fecha 2026-08-20`) y la
pregunta de los comentarios, que ya está en el prompt del guionista pero solo
afecta a los guiones que se escriban a partir de ahora. **Los guiones del 003 al
008 no la llevan**, así que si se quiere en ellos hay que añadirla a mano en el
cierre. Queda anotado para la revisión de mañana.

### Comprobado antes de cerrar

Simulacro de la producción de esta noche con lo que hay en GitHub: `cola.py`
resuelve MDH-003 en los dos idiomas, modo revisión, música Haru, y
`validar_guion.py` —con el nuevo error de narración cortada ya activo— pasa los
dos guiones con código 0. **La producción de las 03:00 no se va a bloquear.**

---

## 19 de agosto, noche · los subtítulos: causa raíz encontrada y arreglada

Tres producciones seguidas sin subtítulos quemados. Ya se sabe por qué, y no era
ni la red ni el montaje.

### La causa

Como el contenedor no puede instalar `edge-tts` (sin acceso al índice de
paquetes), se clonó **el código fuente de la librería** desde GitHub, que sí se
puede leer. Y ahí estaba, en `src/edge_tts/communicate.py`:

    def __init__(self, text, voice=DEFAULT_VOICE, *, rate="+0%", volume="+0%",
                 pitch="+0Hz",
                 boundary: Literal["WordBoundary","SentenceBoundary"] = "SentenceBoundary",
                 ...)

**edge-tts cambió el 22/03/2026 el valor por defecto de `boundary`** de
`WordBoundary` a `SentenceBoundary` (commit `4bdb8e4`, versión 7.2.x). Ese
parámetro decide literalmente lo que la librería pide al servicio de Microsoft
en el mensaje `speech.config`. Reproducido ejecutando el mismo cálculo que hace
la librería en sus líneas 428-436:

    boundary por defecto (SentenceBoundary):
        "sentenceBoundaryEnabled":"true","wordBoundaryEnabled":"false"
    pidiéndolo explícitamente:
        "sentenceBoundaryEnabled":"false","wordBoundaryEnabled":"true"

Con `wordBoundaryEnabled` en `false`, **el servicio no manda ni un solo evento
WordBoundary**. `voz.py` solo escuchaba `trozo["type"] == "WordBoundary"`, así
que recogía cero marcas. El audio llega intacto —por eso el fallo era invisible
escuchando el vídeo— y `escribir_ass()` produce un `.ass` con cabecera y sin una
sola línea de diálogo, que `montaje.py` quema sin error y sin efecto.

Y entró **solo**, sin que nadie tocara este repositorio, porque
`requirements.txt` ponía `edge-tts` a secas: cada producción instalaba la última
versión publicada. La hipótesis de la mañana («la versión sin fijar») era
correcta; lo que faltaba era el mecanismo exacto.

### El arreglo

En `voz.py`, `_comunicar()` pide `boundary="WordBoundary"` de forma explícita,
con reintento sin el parámetro para versiones anteriores a la 7, donde no
existe. En `requirements.txt`, `edge-tts>=7,<8`: rango y no versión exacta,
porque edge-tts necesita actualizarse cuando Microsoft cambia el esquema de
tokens y congelarla pararía el canal el día que eso ocurra.

Y un diagnóstico para que esto no vuelva a costar tres vídeos: si llegan marcas
de frase y ninguna de palabra, `voz.py` escribe un `::error::` que nombra la
causa exacta en vez del aviso genérico de antes.

### Cómo se ha probado sin poder instalar edge-tts

Con un doble de la librería que devuelve mp3 reales generados con ffmpeg y
eventos `WordBoundary`, y que **registra con qué parámetros se le llama**. Se
ejecutó `voz.py` entero contra él:

- Las tres escenas piden `boundary="WordBoundary"`. Verificado leyendo el
  registro del doble, no el código.
- El `.ass` sale con **22 líneas `Dialogue`** donde antes salían 0.
- Regresión: forzando el doble a comportarse como la 7.2.8 (ignorar el
  parámetro), el `.ass` vuelve a salir con 0 líneas **y aparece el `::error::`
  nuevo** nombrando la causa. El diagnóstico funciona.

### De paso, el recorte de la sílaba suelta

Aplicado también a `voz.py` en la misma sesión, ya que estaba abierto. Detecta
el patrón —sonido de menos de 0,45 s seguido de silencio de al menos 0,15 s,
dentro del primer segundo— y recorta. Probado con el mismo doble: la escena
sucia se recorta 0,45 s y la limpia no se toca.

El detalle que importa y no es obvio: **las marcas de palabra se desplazan lo
mismo que el recorte**. Comprobado en el `.ass` generado: la primera marca de la
escena recortada cae en 4,50 s y no en 4,95 s, que es donde habría quedado sin
compensar — y con los subtítulos ya funcionando, ese desfase se habría visto en
pantalla durante toda la escena.

## Guiones 003 a 008

- **Un solo ámbar por pantalla:** corregidas 15 escenas repartidas entre el 004,
  005, 006, 007 y 008. La corrección quita la marca, no la palabra.
- **La pregunta de los comentarios:** añadida al 003, 004, 006, 007 y 008 (el
  005 ya tenía una, y es específica). Cada una pide **una historia propia**
  ligada al tema del episodio, no un «déjamelo en comentarios».

  Ojo con esto, que casi se cuela: al meterla dentro de la narración del cierre,
  **cinco guiones pasaron de 20 segundos en esa escena, que es error grave del
  validador**. Habría bloqueado la producción de esta noche. Corregido dándole
  escena propia justo antes del cierre, que además es mejor: una pregunta
  merece su pausa en vez de ir pegada al avance del episodio siguiente.

- **Pendiente para mañana:** las frases de transición entre bloques. La regla
  está en el prompt del guionista, pero aplicarla a los seis guiones exige
  leerlos enteros y encontrar los saltos reales, no adivinarlos por la longitud
  de la narración de los rótulos. Se hace en la lectura editorial de mañana.

### Comprobado antes de cerrar

`cola.py --fecha 2026-08-20` resuelve MDH-003 en los dos idiomas, modo revisión,
música Haru de Roa. `validar_guion.py` pasa los doce guiones del repositorio con
código 0. La producción de las 03:00 no se bloquea.
