# Calendario editorial

**Vigente desde el 20 de agosto de 2026.** Sustituye por completo al calendario de la
tanda 1 (ocho episodios largos, dos idiomas, ritmo diario), que queda derogado. El porqué
está en `00_estrategia/DIAGNOSTICO.md`.

> La parrilla **ejecutable** —la que lee el sistema— es `05_calendario/parrilla.json`.
> Esta tabla es su versión legible. Si las dos no coinciden, manda el JSON.

---

## Qué se publica, y cuándo

**Un solo canal: `@mecanicadelhumor`, en español.** El inglés lo sirve el doblaje
automático de YouTube, que ya está activado. `@humormechanics` está en pausa.

| Día | Qué sale | Hora | Formato |
|---|---|---|---|
| **Lunes a viernes** | **un Short** (`MDS-###`) | 19:00 | vertical 1080×1920, 30–50 s |
| **Sábado** | **un episodio largo** (`MDH-###`) | 12:00 | horizontal 1920×1080, 4–6 min |
| Domingo | nada | — | — |

**Seis piezas por semana en vez de catorce.** No es bajar el ritmo: es dejar de producir
en el formato que no llega a nadie. Los canales de referencia con millones de
suscriptores publican entre tres y once veces al mes; este publicaba treinta.

**Por qué el Short manda.** Es la única superficie de YouTube donde el reparto no depende
de cuántos suscriptores tienes. Un canal de menos de mil suscriptores saca entre 50 y 500
visualizaciones por Short en las primeras 48 horas; los episodios largos de este canal
sacaban entre 1 y 9. El largo del sábado ya no es la puerta de entrada: es el sitio al que
va quien te ha conocido por un Short y quiere más.

---

## Cómo funciona un día, de principio a fin

| Hora | Quién | Qué pasa |
|---|---|---|
| **03:00** | GitHub Actions | `cola.py` mira la parrilla. Si toca emisión: voz, figuras, render, montaje, miniatura, **subida en privado** y expediente de calidad |
| **07:00** | Cowork | Revisión de calidad: lee el expediente de la producción de esta noche y **los guiones que aún no se han producido**, y corrige lo que encuentra antes de que llegue a cámara |
| **19:00** (o 12:00 el sábado) | YouTube | El vídeo se hace público |
| **Jueves 22:00** | Cowork | Planificación de la semana siguiente: investigación de demanda, cinco Shorts, un largo, metadatos y parrilla |
| **Lunes 09:00** | Cowork | Métricas: en qué peldaño está el canal y qué cambio se lanza esta semana |

**El vídeo siempre se sube en privado**, nunca directo a público. Lo que cambia entre los
dos modos es quién aprieta el botón.

---

## Los dos modos, y cuándo tienes que hacer algo tú

### Modo REVISIÓN — del 24 al 29 de agosto

El vídeo se sube en privado **y sin fecha**. Se queda ahí hasta que tú entras y le das a
publicar.

**Lo que te toca:** entrar en YouTube Studio por la mañana, mirar el vídeo del día y
publicarlo o no. Unos **dos minutos al día durante seis días**. Si un día no puedes, no
pasa nada: el vídeo se queda en privado y no se pierde.

Es una semana. Sirve para que veas el formato nuevo antes de que vuele solo: el vertical,
el personaje, las miniaturas nuevas y las dos voces son cambios grandes y conviene que los
apruebes con los ojos, no con la confianza.

### Modo AUTOMÁTICO — a partir del 31 de agosto

El vídeo se sube en privado **con fecha de publicación programada**, y es YouTube quien lo
hace público a la hora que toca.

**Lo que te toca: nada.** Entre la subida (03:00) y la publicación (19:00) hay dieciséis
horas en las que puedes entrar a cancelarlo si algo no te cuadra, pero no tienes que hacer
nada para que salga. Si te olvidas del canal una semana, el canal publica igual.

El paso de un modo a otro ya está escrito en `parrilla.json`. No hay que acordarse.

---

## Esta semana concreta (20 al 23 de agosto)

| Día | Qué |
|---|---|
| **jue 20** | MDH-003 programado como estreno a las 18:00. Es el último vídeo del formato antiguo |
| **jue 20, 22:00** | ✅ **Hecho.** La planificación escribió MDS-002 a MDS-006 y adaptó MDH-004 al formato nuevo |
| **vie 21 · sáb 22 · dom 23** | **Nada.** Tres días de pausa para cambiar de formato |

Tres días sin publicar no cuestan nada con la audiencia que hay ahora, y evitan sacar dos
vídeos más en el formato que ya sabemos que no funciona.

---

## La semana del 24 al 29, pieza a pieza

**Todos los temas salen de `05_calendario/demanda.json`**, no de la bibliografía. Es el
cambio de fondo del canal: la demanda elige la pregunta y la bibliografía decide si podemos
responderla honestamente. Tres preguntas con demanda real se quedaron fuera por falta de
fuente y están anotadas en `pendientes_de_fuente.md`.

| Día | ID | Serie | La pregunta que responde | Fuentes |
|---|---|---|---|---|
| **lun 24** | MDS-001 | Desmonta el chiste | por qué nos reímos de un chiste | A01 |
| **mar 25** | MDS-002 | El experimento | «por qué me río solo» | E01, E02 |
| **mié 26** | MDS-003 | Esto no tiene gracia y esto sí | «por qué nos reímos cuando alguien se cae» | A01, A03 |
| **jue 27** | MDS-004 | Diagnósticos | «qué dice de mí mi sentido del humor» | B01, B02 |
| **vie 28** | MDS-005 | Desmonta el chiste | «por qué mis chistes no dan risa» | A01, A05, D01 |
| **sáb 29** | MDH-004 | Mecanismos (largo, 5m02s) | «por qué nadie se ríe de mis chistes» | E01, E02, E04, D07, A10 |
| **lun 31** | MDS-006 | Ríete primero, te explico después | «por qué me río cuando no debo» | E02, A10 |

Cinco series distintas en seis Shorts. `MDS-006` estrena la quinta, que era la única sin
estrenar, y con eso hay un dato de cada una antes de decidir cuál sobrevive.

**Los seis siguen la misma regla de cierre:** todos terminan diciendo dónde falla lo que
acaban de explicar. `MDS-006` es el caso extremo y el más de marca: termina admitiendo que
no tenemos ni un estudio sobre la risa nerviosa y que lo anterior es la mejor explicación
disponible, no la comprobada.

---

## Las cinco series de Shorts

Cada Short pertenece a una y solo una. La serie decide la estructura, y `publicar.py` mete
el vídeo en su lista de reproducción solo.

| Serie | Qué hace | Duración |
|---|---|---|
| **Desmonta el chiste** | Chiste, silencio, y el despiece: qué expectativa se rompió, por qué fue inofensiva, dónde estaba la bisagra | 40 s |
| **Ríete primero, te explico después** | El chiste en el segundo cero. La explicación es el premio | 30 s |
| **El experimento** | Un estudio real con un resultado que no te esperas, con su DOI | 45 s |
| **Esto no tiene gracia y esto sí** | Dos chistes casi idénticos; uno funciona y otro no | 35 s |
| **Diagnósticos** | Qué dice de ti la clase de humor que usas, según la taxonomía real | 40 s |

La primera semana usa al menos tres series distintas. Al cabo de dos o tres semanas los
números dirán cuál aguanta mejor, y la parrilla se reconstruye alrededor de esa.

---

## Con qué se decide seguir o cambiar

La tabla completa está en `00_estrategia/PLAN_DE_CAMBIOS.md`, apartado C14. Lo esencial:
**cada peldaño solo se mira si se pasó el anterior.** Con veinte visualizaciones totales,
medir CTR y retención es medir ruido.

| Nivel | Métrica | Umbral |
|---|---|---|
| 1 | Impresiones por semana | ≥ 5.000 |
| 2 | CTR de miniatura | ≥ 4 % |
| 3 | Retención a los 30 s / % visto | ≥ 60 % |
| 4 | Retención media | ≥ 45 % largo, ≥ 70 % Short |
| 5 | Suscriptores por mil vistas | ≥ 5 |

Revisión **semanal**, los lunes. La tanda cerrada de cuatro semanas desaparece: con un
sistema automatizado no hay motivo para esperar un mes a saber algo.

**El punto de parada honesto:** si a las doce semanas el peldaño 1 sigue sin superarse, el
problema no son los Shorts ni las miniaturas — es que «la ciencia del humor» no es lo que
la gente quiere ver, y toca ampliar el tema sin renunciar ni al método ni a las fuentes.
Eso se decide con la tabla delante, no por agotamiento.

---

## Material ya escrito, en reserva

- **MDH-004** — ✅ adaptado al formato nuevo el 20/08 para el sábado 29. 30 escenas, 5m02s,
  personaje en cuatro escenas, dos intervenciones del escéptico, «enunciado» al 43 %.
- **MDH-005** — «Tu estilo de humor». Escrito y validado, pero **todavía en formato viejo**
  (27 escenas, 62 % «enunciado», sin personaje ni escéptico, rótulo por delante). Está
  programado para el **sábado 5 de septiembre**, así que hay que pasarlo por la misma
  adaptación que MDH-004 antes de esa fecha. Da además material para la serie
  «Diagnósticos».
- **MDH-006, 007 y 008** — escritos y validados, mismo caso: 65 % de «enunciado», rótulo de
  ocho segundos por delante y ningún personaje. Entran como largos de sábados siguientes
  después de la adaptación.

**Cómo se adapta un largo viejo** (el patrón está aplicado en MDH-004, cópialo de ahí):
sacar el rótulo de la escena 1 y poner en su sitio una escena concreta con la primera risa
antes del segundo quince; partir las escenas de más de catorce segundos; convertir
«enunciado» en `comparacion`, `cita` y `diagrama` hasta bajar del 45 %; meter al personaje
en tres o cuatro escenas, siempre reaccionando *después*; añadir una o dos intervenciones
del escéptico de menos de doce palabras; y reescribir el título de publicación a la
pregunta que la gente escribe.
- **Los guiones ingleses** (`.en.json`) quedan archivados sin borrar, por si se reabre
  `@humormechanics`.
