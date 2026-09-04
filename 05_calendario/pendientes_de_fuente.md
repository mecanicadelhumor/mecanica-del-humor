# Pendientes de fuente

Preguntas con demanda demostrada que **no se pueden responder** con las 77 obras de
`01_bibliografia/BIBLIOGRAFIA_CURADA.md`.

Esto no es una lista de deseos: es el freno que impide que el canal degenere en clickbait
(`00_estrategia/REGLAS.md`, regla 3). Una pregunta entra aquí cuando la demanda dice que sí
y la bibliografía dice que no. Sale de aquí **solo** cuando se incorpora al corpus una obra
que la responda de verdad — nunca porque la pregunta nos siga apeteciendo.

**La regla que no se invierte:** nunca se busca una fuente para justificar un tema ya
decidido. Primero la evidencia, luego el vídeo.

Se añade al final. No se reescribe.

---

## 20 de agosto de 2026 · primera tanda de demanda

Las tres salen de `05_calendario/demanda.json`, generado esta noche.

### 1. «Por qué sentimos vergüenza ajena» / «qué es el cringe»

**Demanda:** alta y actual. Dos búsquedas devuelven casi solo resultados dentro de tema,
con publicaciones de agosto de 2026 (ABC Color) y cobertura de Gizmodo en español. Tiene
además una segunda puerta de entrada por el lado joven —«cringe»— con NeuroClass, Ethic,
El Financiero y un episodio de pódcast titulado exactamente así.

**Por qué no se hace:** el corpus cubre el miedo a que se rían **de ti** (`J01`, `J02`,
gelotofobia) y la burla como amenaza a la imagen (`J04`). La vergüenza **ajena** es otra
cosa: es vergüenza vicaria, sentida por cuenta de otra persona, y no hay ni una ficha que
la trate. Responderla hoy sería citar de memoria.

**Qué haría falta:** literatura sobre *empathic embarrassment* / *vicarious embarrassment*.
El punto de partida obvio es el trabajo de Krach y Paulus sobre sus correlatos neurales, que
es acceso abierto. Con dos o tres obras sólidas, el tema es de los mejores de la lista:
demanda alta, competencia repetitiva y una conexión natural con el pilar J que el canal ya
tiene.

### 2. «Por qué no puedo hacerme cosquillas a mí mismo»

**Demanda:** alta. Ocho resultados dentro de tema, con National Geographic España, The
Conversation en español y el blog de neuropediatría de Quirónsalud.

**Por qué no se hace:** `E06` (Panksepp y Burgdorf) cubre cosquillas y evolución de la risa
—las ratas que «ríen» a 50 kHz— pero **no la autocosquilla**. El mecanismo que cuenta todo
el mundo, que el cerebelo predice el movimiento propio y cancela la sensación, no tiene
ficha. `A07` (Hurley y Dennett) da un marco general de error de predicción, y la tentación
es usarlo como si respondiera esta pregunta. No la responde: sería estirar una fuente hasta
que diga lo que nos conviene.

**Qué haría falta:** el trabajo de Blakemore, Wolpert y Frith sobre la atenuación
sensorial del movimiento autogenerado.

**Aviso adicional:** aunque llegue la fuente, este es el tema con **peor competencia** de
toda la tanda. NatGeo y The Conversation ya lo explican bien. Entrar aquí exige tener algo
que ellos no digan, no solo permiso para decirlo.

### 3. «Por qué los memes nos hacen gracia»

**Demanda:** media-alta y —único caso de la tanda— **creciente**: es el único tema con
publicaciones nuevas de 2025 y 2026, y no tiene referente en español.

**Por qué no se hace:** no hay ni una obra sobre memes en las 77. Sí se puede explicar por
qué algo hace gracia (`A01`, `A07`, `F01`), pero en cuanto el vídeo dijera algo específico
del meme —por qué se comparte, por qué se vuelve viral, qué tiene de distinto respecto a un
chiste— estaría inventando. Y un vídeo titulado «por qué los memes nos hacen gracia» que no
dice nada de los memes es exactamente el clickbait que la regla 3 existe para impedir.

**Qué haría falta:** literatura sobre humor digital y difusión de contenido humorístico.
Es el hueco más rentable de los tres: demanda en crecimiento, competencia floja y ningún
canal ocupándolo.

---

## Nota de método sobre esta primera tanda

La medición de demanda salió **coja** y conviene que quede escrito, porque afecta a la
confianza de todo lo de arriba.

La planificación corre como tarea programada en la nube y en ese modo `WebFetch` está
bloqueado: toda URL devuelve `PROVENANCE_REQUIRED`, una petición de permiso que, sin nadie
delante, nadie contesta. Probado contra cuatro dominios distintos, los cuatro igual.

Consecuencia: **no hay autocompletar de YouTube, no hay visualizaciones del top 10, no hay
comentarios y no hay Reddit.** Solo `WebSearch`, que da títulos y URLs pero ninguna métrica.
Por eso `vistas_top10` va a `null` en los dieciséis candidatos: preferimos un hueco a una
cifra inventada.

Lo que esto significa para esta lista: las tres exclusiones de arriba son **firmes**, porque
dependen de la bibliografía y la bibliografía sí se ha podido leer entera. Lo que no es
firme es el orden de prioridad entre ellas, que depende de un volumen de búsqueda que no
hemos podido medir.

**Cómo arreglarlo:** lanzar la planificación semanal como tarea programada local, en el
ordenador de Silvestre, donde el autocompletar y YouTube sí son accesibles.

---

## 27 de agosto de 2026 · segunda tanda de demanda

**Ninguna pregunta nueva entra en esta lista.** Se han vuelto a cruzar las tres de arriba
contra `BIBLIOGRAFIA_CURADA.md` y ninguna obra nueva ha entrado en el corpus esta semana,
así que las tres exclusiones siguen firmes y por el mismo motivo. Se anota aquí para dejar
constancia de que se han revisado, no para repetirlas.

### Una corrección de clasificación, que no es lo mismo que una exclusión

«A las mujeres les atraen los hombres graciosos» figuraba en la tanda del 20/08 como
**«apto pero congelado»**. Eso estaba mal etiquetado: si un tema no se puede producir, no
es apto. En `demanda.json` del 27/08 pasa a `apto: false`, rechazado en la fase de demanda
—que es donde `REGLAS.md` dice que se rechaza— y **no entra en esta lista**, porque esta
lista es de preguntas que la bibliografía no puede responder, y el problema de esa no es la
bibliografía: es el criterio editorial.

La diferencia importa para quien lea esto dentro de tres meses. Una pregunta de esta lista
sale de aquí en cuanto llegue la fuente. Aquella no sale con ninguna fuente.

### Nota de método sobre esta segunda tanda

Sigue sin haber medición de volumen. `demanda_bruta.json` **no existe** en el repositorio:
el workflow `demanda.yml`, que debía dejarlo hoy jueves a las 12:00 UTC, no ha producido ni
fichero ni commit. Segunda semana consecutiva con `vistas_top10: null`.

Lo que sí ha cambiado respecto al 20/08: `WebSearch` **funcionó** en esta sesión desatendida,
al contrario de lo que documentan `explorador_de_demanda.py` y la tanda anterior. Sigue sin
dar métricas —solo títulos y URLs—, así que sirve para juzgar competencia y formulación,
nunca volumen. Las cuatro consultas nuevas de esta noche están citadas candidato por
candidato en `demanda.json`.

**Lo que esto significa para esta lista:** las tres exclusiones son firmes, porque dependen
de la bibliografía y la bibliografía sí se lee entera. Lo que sigue sin ser firme es el
orden de prioridad entre ellas.

---

## 3 de septiembre de 2026 · tercera tanda, la primera con visualizaciones medidas

**Ninguna pregunta nueva entra en esta lista, y las tres de siempre siguen dentro.**
Se han vuelto a cruzar contra `BIBLIOGRAFIA_CURADA.md` y el corpus no ha cambiado:
`git log -- 01_bibliografia/` no tiene ningún commit posterior al inicial salvo el
cambio de horario de la revisión diaria. Setenta y siete obras, las mismas.

Lo que sí cambia hoy es que por fin sabemos **cuánta demanda estamos dejando en la
mesa**, que era justo el motivo de meterlas en `semillas_demanda.json`. El workflow
`demanda.yml` ha corrido y ha dejado `demanda_bruta.json`.

| Pregunta excluida | Vistas del top 10 | De los cinco primeros, cuántos responden |
|---|---|---|
| Por qué no puedo hacerme cosquillas a mí mismo | 3.858.288 | **5 de 5** |
| Por qué sentimos vergüenza ajena | 276.869 | **5 de 5** |
| Qué es el cringe | 9.508.802 | 2 de 5 |
| Por qué los memes nos hacen gracia | 128.623.642 | **0 de 5** |

Y con los números delante, el orden de prioridad —que las dos tandas anteriores
dejaron expresamente sin fijar porque no se podía medir— **sí se puede fijar ahora**:

1. **Vergüenza ajena / cringe.** Es la que más merece la pena. Demanda modesta pero
   entera en tema (de 17.705 a 106.128 visualizaciones, todos explicando), competencia
   de psicólogos generalistas y **ninguno lo cuenta desde el humor**, que es
   exactamente nuestro ángulo. Sigue haciendo falta literatura de *empathic
   embarrassment*; Krach y Paulus, acceso abierto, sigue siendo el punto de partida.
2. **Memes.** La tanda del 20/08 la llamaba «el hueco más rentable de los tres».
   **La medición lo desmiente:** 128 millones de visualizaciones y cero resultados que
   expliquen nada. La consulta devuelve memes, no explicaciones de memes. Si algún día
   entra la fuente, el vídeo competiría contra el entretenimiento puro, que es la pelea
   que este canal pierde. Baja de prioridad.
3. **Autocosquillas.** El aviso del 20/08 se confirma y se agrava: los cinco primeros
   responden la pregunta y dos son canales de ciencia grandes —CdeCiencia con 1.263.221
   y un vídeo de abril de 2026 con 2.365.233—. Aunque llegue Blakemore, entraríamos por
   detrás de gente que ya lo hace bien. Es la única pregunta de las veinte medidas donde
   eso pasa.

**Lo que no ha hecho falta escribir aquí, y conviene que se note:** esta semana se ha
descartado un Short entero (*cómo distinguir una risa falsa de una de verdad*) y no está
en esta lista, porque su problema no era la fuente. Tenía tres —`D07`, `E04` y `F03`— y
aun así no se hace: **MDH-004 ya lo contó el 29 de agosto con casi las mismas escenas**.
Eso es C17, no falta de bibliografía, y va anotado en `demanda.json` y en la bitácora.
Una lista no debe engordar con cosas que no le tocan.
