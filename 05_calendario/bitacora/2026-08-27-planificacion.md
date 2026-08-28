# Planificación semanal — 27 de agosto de 2026 (jueves noche)

Semana planificada: **lunes 31 de agosto a sábado 5 de septiembre**. Es la primera
que sale en modo `automatico`.

---

## 0. Comprobación de entregas pendientes

Primera acción de cualquier tarea (`PROPIEDAD_DE_FICHEROS.md`, punto 3).

`git log --oneline -8` sobre `origin/main`:

    6dc8bcd Registro y expediente de calidad: MDS-004
    4ae53e9 revisión diaria 27/08
    664f57f revisión del día 26/08/26, retoques en dos guiones
    8ddefc2 Registro y expediente de calidad: MDS-003
    d05ee69 revisión diaria 25/08/26

**Sin entrega pendiente sin aplicar.** El trabajo de la planificación anterior
(`ffdd581` y `4c0ee2b`, «guiones para la semana del 24 de agosto») está en `main`, y la
revisión diaria de esta mañana también. La base es la buena.

**Entorno:** sin acceso al ordenador de Silvestre —tarea programada, ejecución en la nube—,
así que se trabaja sobre un clon del repositorio público y se entrega un `.tar.gz`. La
lista de ficheros va en el resumen, como pide el punto 4.

---

## 1. La demanda: lo que ha fallado

**`05_calendario/demanda_bruta.json` no existe en el repositorio.**

El workflow `.github/workflows/demanda.yml` está programado para los jueves a las 12:00 UTC
y hoy es jueves. No hay ni fichero en el árbol ni commit «medición de demanda» en el
historial. Era la primera semana en la que debía haber corrido: `demanda.yml` entró en el
repositorio con `15b94e2`, después de la planificación anterior.

Comprobado también que la API de GitHub no es accesible desde esta sesión (403 del proxy
con «GitHub access to this repository is not enabled for this session»), así que **no se ha
podido mirar el estado del job**. Eso lo tiene que hacer Silvestre desde la pestaña Actions.

Hipótesis, por orden de probabilidad, anotadas en `demanda.json`:

1. El cron no llegó a registrarse: GitHub tarda en activar un workflow programado recién
   añadido, y `demanda.yml` es de esta semana.
2. El paso «Commit» falló al hacer push y el fichero se quedó en el runner.
3. Faltan los secretos de YouTube — pero eso solo debería haber vaciado la señal principal,
   no impedir que se escribiera el fichero con el autocompletar y la Wikipedia.

**No se ha tocado `demanda_bruta.json` ni se ha simulado su contenido.** Es de otro dueño.

### Lo que sí ha cambiado respecto al 20/08

**`WebSearch` funcionó en esta sesión desatendida.** La tanda anterior y la cabecera de
`explorador_de_demanda.py` dan por hecho que en modo desatendido no hay red, y hoy no ha
sido así: el clon por HTTPS funcionó y `WebSearch` devolvió resultados en las cuatro
consultas que se le hicieron. `WebFetch` no se ha probado.

Esto **no cambia el reparto de responsabilidades**: `WebSearch` devuelve títulos y URLs, no
métricas. Sirve para juzgar cómo formula la gente la pregunta y quién la está respondiendo
ya; no sirve para saber cuánta gente busca. `vistas_top10` sigue en `null` en los catorce
candidatos y no se ha inventado ni una cifra.

### Lo que se ha decidido con eso

`demanda.json` reescrito con catorce candidatos: diez aptos, tres no aptos por falta de
fuente y uno rechazado por criterio editorial. Cuatro reservas del 20/08 pasan a producción
esta semana, cada una con su consulta nueva de confirmación:

| Pregunta | Competencia | Respaldo | Va a |
|---|---|---|---|
| si te hace gracia el humor negro eres más inteligente | alta en cantidad, nula en fondo | B04, C02 | MDS-007 |
| por qué unos chistes hacen gracia y otros no | media | I02, L01 | MDS-008 |
| cómo caer bien a la gente (ángulo: humor compartido) | alta en general, media en el ángulo | D05 | MDS-009 |
| si tienes que explicar un chiste pierde la gracia | baja | A05, A06, A07 | MDS-010 |

**Aplazada a propósito:** «por qué la risa es contagiosa». Se solapa con MDS-002 (ya
emitido), con MDH-004 (sábado 29) y con MDS-009 de esta tanda. Repetir la misma cifra tres
semanas seguidas cansa antes que informa.

**Corregida una clasificación del 20/08.** «A las mujeres les atraen los hombres graciosos»
figuraba como *«apto pero congelado»*. Eso está mal: si no se puede producir, no es apto.
Pasa a `apto: false`, rechazado **en la fase de demanda**, que es donde `REGLAS.md` dice que
se rechaza. Y no entra en `pendientes_de_fuente.md`, porque su problema no es la
bibliografía: es el criterio editorial. Una pregunta de aquella lista sale de ella en cuanto
llegue la fuente; esta no sale con ninguna.

**Escrito `semillas_demanda.json`** con veinte preguntas y trece semillas para la medición
del jueves que viene, en tres bloques: las ya producidas (para tener por fin una cifra con
la que comparar cuando lleguen las métricas de Studio), las tres pendientes de fuente (para
saber cuánta demanda estamos dejando en la mesa) y los dos candidatos a largo del 12 de
septiembre, que compiten entre sí y necesitan un desempate que no sea mi intuición. Nada
sobre humor y atracción: no se mide lo que no se puede producir.

---

## 2. Revisiones aplicadas

De `05_calendario/revisiones/`, leídas antes de escribir nada.

### `MDS-006.md` — aplicada y borrada

El personaje estaba en cinco de las seis escenas, incluida la 1, que es el chiste de
apertura. Quitado de la 1 y la 5. Quedan tres reacciones —`duda`, `piensa` y el `no` del
cierre—, espaciadas y ninguna compitiendo con el chiste. Mismo patrón que `MDS-001`.
Anotado en `notas_humor` del propio guion para que no se vuelva a colar.

La nota avisaba además de que el comentario del 24/08 sobre «personaje después del remate y
no en todas las escenas» no se sostenía al contar escena por escena. **Tomado en cuenta:**
los cuatro Shorts nuevos de esta noche llevan el personaje en dos o tres escenas y ninguno
lo pone sobre el chiste de apertura, y `MDH-005` lo lleva en cuatro de treinta y nueve.

### `MDH-004.md` — aplicada y borrada, sin tocar el guion

La revisión verificó las tres cifras heredadas contra fuentes externas y su recomendación
es explícita: **el guion no se cambia**, las cifras son correctas en orden de magnitud y
dirección y ninguna es inventada. Lo pendiente es de la bibliografía.

Lo que se ha hecho: reescribir el aviso `_verificar_en_la_bibliografia` de
`MDH-004.es.json` para que recoja el estado real —qué se verificó, con qué resultado y qué
queda— en vez de decir «no se ha podido comprobar». El aviso **no se borra** porque la
condición que lo justifica sigue viva: la ficha de `E02` sigue sin recoger las tres cifras,
y el DOI de la ficha sigue sin coincidir con el que devuelve Wiley.

`01_bibliografia/` no es de la planificación, así que **no se toca**. Va en el resumen.

### `MDH-005.md` — aplicada y borrada

Es la adaptación entera del guion. Ver apartado 4.

### `MDH-006.md`, `MDH-007.md`, `MDH-008.md` — se quedan

**Decisión consciente: no se adaptan esta semana.** Ninguno tiene fecha en la parrilla y
adaptar los tres ahora es trabajo especulativo: en dos o tres semanas las métricas dirán
qué formato aguanta y habría que rehacerlo. Se adapta uno por semana, el del sábado
siguiente. Las notas siguen en el buzón, que es donde tienen que estar.

---

## 3. Los cinco Shorts

Lunes ya estaba escrito (`MDS-006`, corregido arriba). Escritos los cuatro de martes a
viernes.

| ID | Día | Serie | Duración | Fuentes |
|---|---|---|---|---|
| MDS-006 | lun 31 | Ríete primero, te explico después | 51,7 s | E02, A10 |
| MDS-007 | mar 1 | Diagnósticos | 53,2 s | B04, C02 |
| MDS-008 | mié 2 | Esto no tiene gracia y esto sí | 47,9 s | I02, L01 |
| MDS-009 | jue 3 | El experimento | 44,3 s | D05 |
| MDS-010 | vie 4 | Desmonta el chiste | 50,7 s | A05, A07 |

**Cinco series distintas, una por día.** `metricas.json` sigue vacío —ni una lectura—, así
que no hay nada que diga cuál funciona mejor y no se monocultiva ninguna.

Los cinco: chiste o escena concreta en el segundo cero, pausa de 1,2-1,4 s antes del remate,
personaje en dos o tres escenas y siempre después, y cierre que dice dónde falla.

### Decisiones editoriales que conviene tener escritas

**MDS-007 no nombra el estudio que todo el mundo cita.** La creencia «si te gusta el humor
negro eres más inteligente» sale de un estudio vienés de 2017 que **no está en las 77
obras**. Comentarlo o desmontarlo por su nombre sería hablar de un artículo que no hemos
leído, que es justo lo que prohíbe la regla 2. Así que el Short responde la pregunta con lo
que sí tenemos: `B04` (el 3WD de Ruch reparte el *gusto* en dimensiones, no en una escala de
listo a tonto) y `C02` (el metaanálisis dice que lo que aparece junto a la inteligencia es
*producir* humor, no apreciarlo). La distinción producir/apreciar es el desmontaje entero, y
es honesta. `C01` no se usa: lleva ⚠️ por su afirmación sobre diferencias entre sexos.

**MDS-009 no lleva ninguna cifra en pantalla.** La serie «El experimento» pide terminar con
la cifra grande, y la ficha de `D05` recoge la dirección del efecto pero no las magnitudes.
La escena de tipo `dato` pone «Más generosos» en lugar de un número. Antes un hueco que un
dato inventado (regla 2). Está anotado en `notas_humor` para que nadie lo tome por un olvido.

**MDS-010 es el más de marca de la semana.** Un canal que se dedica a desmontar chistes
explicando por qué explicar un chiste lo mata: cuenta el chiste, lo explica en directo, y
señala el cadáver. Y el cierre admite las dos cosas incómodas: que esto es un modelo teórico
y no una cifra medida, y que por eso en este canal el chiste va siempre **antes** del
despiece, nunca después.

---

## 4. El largo del sábado: MDH-005 adaptado

**Solo ese.** MDH-006, 007 y 008 se quedan como están, por lo dicho arriba.

| | Antes | Ahora |
|---|---|---|
| Escenas | 27 | 39 |
| Duración | 6m10s | 4m43,7s |
| «enunciado» | 62 % | 41 % |
| Escena 1 | rótulo de portada | el chiste de la cena |
| Primera risa | no había | segundo ~9 |
| Personaje | ninguno | escenas 3, 19, 26 y 39 |
| Escéptico | ninguno | escenas 6 y 25 |
| Escenas > 10 s | siete por encima de 14 s | una (el cierre, 10,3 s) |

**El gancho.** La nota de la tarea es explícita en que no basta con abrir con una escena
concreta —el 006 y el 007 ya lo hacen y no hacen reír—, así que el episodio abre con un
chiste de verdad: la frase del invitado en la cena («¿esto lo has cocinado tú o ha sido un
accidente?»). Y no es decorado: es el caso clínico del episodio entero, porque ese chiste es
exactamente humor agresivo con técnica. La escena 2 remata en pantalla grande («Menos uno»)
y el personaje reacciona en la 3. El callback está en la escena 38, justo antes del cierre.

**Segunda risa** en la escena 19: «el agresivo tiene un público que se ríe mucho, y un
público de una sola persona que lleva la cuenta».

**El escéptico** entra dos veces, las dos con la objeción que el espectador está pensando y
antes de que el narrador la resuelva: «¿Y si simplemente soy una persona borde?» (7
palabras) y «Reírme de mí mismo es humildad, ¿no?» (7 palabras).

**Cómo se bajó el «enunciado» del 62 % al 41 %:** no partiendo escenas, sino **cambiando de
tipo visual** nueve de ellas — cada estilo de humor pasa a ser una `lista` de tres puntos,
los dos mensajes del humor agresivo pasan a `comparacion`, la crítica al cuestionario pasa a
`lista` y la advertencia correlacional a `comparacion`. Sale más movimiento sin alargar
nada, que es lo contrario de lo que pasaría fundiendo escenas.

**Ni un dato nuevo.** Las fuentes siguen siendo `B01` y `B02` y las afirmaciones son las
mismas del guion original, repartidas y recortadas. Se ha añadido `_sin_figura` explicando
por qué no lleva gráfica: la única natural sería la relación de cada estilo con el bienestar
y la ficha de `B01` no da coeficientes. Dibujarla exigiría inventar la escala.

---

## 5. Metadatos, parrilla y calendario

Cinco ficheros nuevos en `publicaciones/`, todos con `serie` (para la lista de
reproducción), `primer_comentario` (la pregunta del episodio, que publica `publicar.py`) y
título por debajo de 100 caracteres **conteniendo la pregunta que la gente escribe**:

- MDS-007 — «¿Si te gusta el humor negro eres más inteligente? Lo que sí está medido» (71)
- MDS-008 — «¿Por qué unos chistes hacen gracia y otros no? Dos versiones del mismo» (70)
- MDS-009 — «Cómo caer bien: qué pasa cuando te ríes de lo mismo que el otro» (63)
- MDS-010 — «¿Por qué un chiste explicado pierde la gracia? Lo hago con el mío» (65)
- MDH-005 — «¿Qué dice de ti tu sentido del humor? Los cuatro estilos, y cuál sale caro» (74)

`parrilla.json`: las seis emisiones del 31 al 5 con `idiomas: ["es"]`, modo `automatico`,
19:00 los Shorts y 12:00 el largo del sábado, y nota por emisión con serie, pregunta de
demanda y fuentes. `_pendiente` reescrito para que diga la decisión de adaptar uno por
semana en vez de «hay que adaptar los cuatro».

`CALENDARIO.md`: sección nueva de la semana del 31 al 5 con la tabla pieza a pieza y las dos
decisiones editoriales; el bloque de reserva actualizado (MDH-005 ya adaptado); y el
apartado «cómo se adapta un largo viejo» corregido, porque decía «partir las escenas de más
de catorce segundos» y desde ayer el validador avisa a partir de diez.

---

## 6. Validación

    python3 04_agentes/validar_guion.py 05_calendario/guiones/MD*-0*.es.json

Los seis guiones de la semana, **sin errores graves**. Avisos que quedan y por qué:

- `MDH-005`, escena 39: 10,3 s. Es el cierre y necesita respirar. Se deja.
- `MDH-004`, 19 escenas por encima de 10 s. **No se toca, y conviene explicar por qué.** El
  umbral bajó de 14 a 10 ayer por la tarde (revisión diaria, commit `4ae53e9`); MDH-004 se
  adaptó el 20/08 contra el umbral anterior y **se produce el sábado 29**, dentro de 48
  horas. Repartir diecinueve escenas de un guion ya verificado, a dos días de cámara y sin
  poder ver el vídeo, es exactamente el tipo de cambio que la regla 11.4 desaconseja. Son
  avisos, no errores: no bloquean nada. Si el vídeo del sábado se ve quieto, se arregla el
  jueves que viene con el expediente de calidad delante.

---

## 7. Lo que queda fuera, para que conste

- **`demanda_bruta.json`**: no existe y no lo escribe esta tarea. Silvestre tiene que mirar
  Actions.
- **Ficha de `E02` en `01_bibliografia/BIBLIOGRAFIA_CURADA.md`**: le faltan las tres cifras
  de MDH-004 y tiene un DOI que no coincide. No es de esta tarea.
- **`DESCRIPCION_SERIE` en `03_produccion/pipeline/publicar.py`**: le falta la entrada
  «Ríete primero, te explico después», que estrena el lunes 31. La lista de reproducción se
  creará con descripción vacía. Es de la revisión diaria; se propone en el resumen.
- **`metricas.json`**: sigue con `lecturas: []`. Tres semanas de Shorts publicándose y cero
  lecturas de Studio. Sin eso, la decisión del largo del 12 de septiembre y la de qué serie
  sobrevive se toman a ciegas. Es el cuello de botella real del proyecto ahora mismo.
