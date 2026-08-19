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
