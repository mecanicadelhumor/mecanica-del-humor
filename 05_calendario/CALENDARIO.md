# Calendario editorial

**Vigente desde el 20 de agosto de 2026. Última actualización: 3 de septiembre.** Sustituye por completo al calendario de la
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

## La semana del 7 al 12 de septiembre, pieza a pieza

**La primera semana elegida con demanda medida.** El workflow `demanda.yml` dejó
`demanda_bruta.json` el jueves 3 a las 12:42 UTC, sin avisos y con las veinte consultas
medidas. Hasta ahora la serie repartía y la pregunta salía después; desde el 31/08 manda
la pregunta y la serie solo pone la forma, y esta es la primera semana en que eso se ha
podido hacer con cifras.

| Día | ID | Serie | La pregunta que responde | Fuentes |
|---|---|---|---|---|
| **lun 7** | MDS-011 | El experimento | «cómo ser más gracioso» | C04, C03 |
| **mar 8** | MDS-012 | Esto no tiene gracia y esto sí | «cómo contar un chiste bien» | L02, L03 |
| **mié 9** | MDS-013 | Desmonta el chiste | «miedo a que se rían de ti» | J04, J05 |
| **jue 10** | MDS-014 | Diagnósticos | «estilos de humor test» | B05, B06 |
| **vie 11** | MDS-015 | Ríete primero, te explico después | «por qué se contagia la risa» | E03, D06 |
| **sáb 12** | MDH-006 | Mecanismos (largo, 4m47s) | «bromas en el trabajo» | D01, D02, G01, G02, D07 |

**Dos series se repiten y ninguna se fuerza.** No hay «El experimento» el jueves porque
tocara: hay lo que cada pregunta pedía. Y falta una de las cinco series —ninguna pregunta
apta pedía su forma esta semana—, que es exactamente lo que la regla del 31/08 autoriza.

**Nueve fichas nuevas de once.** De las once fuentes de la semana, **nueve no se habían
abierto nunca**: C03, C04, L02, L03, J04, J05, B05, B06 y E03, más D06. Quedan 36 fichas
sin estrenar de las 77. Es la aplicación directa de C17, paso 2: se empieza a elegir por
las libres.

Tres decisiones editoriales de esta tanda que conviene tener escritas:

- **Se ha tirado un Short entero, ya redactado.** «Cómo distinguir una risa falsa de una
  de verdad» tenía demanda, tenía tres fuentes (`D07`, `E04`, `F03`) y pasaba el validador.
  Y no se hace: **MDH-004, producido el 29 de agosto, ya lo cuenta con casi las mismas
  escenas** —la comparación «Las dos risas» con E04, el dato «24 sociedades» con D07 y el
  matiz de «algo más que el azar»—. Cuatro escenas calcadas ocho días después es
  precisamente lo que C17 existe para impedir. Vuelve a estar disponible a partir del 10 de
  octubre, y mejor con `F03` de columna.
- **MDS-011 no es una lista de trucos.** «Cómo ser más gracioso» es la pregunta con más
  demanda limpia de todo el corpus, y en cuarenta segundos se convierte justo en el manual
  de sobremesa que este canal no quiere ser. El Short entra por el único ángulo que no lo
  es: cómo se puntúa la gracia en un laboratorio, y qué aparece al lado de las
  puntuaciones altas.
- **MDS-014 corrige a los dos vídeos anteriores del canal.** MDS-004 y MDH-005 usan los
  cuatro estilos de `B01`. Este Short no los toca: cuenta que un test de estilos mezcla el
  rasgo con el estado, o sea, que parte del resultado es el día que tenías. Es la letra
  pequeña de nuestro propio material.

**Los seis terminan diciendo dónde falla** lo que acaban de explicar. `MDS-015` es el caso
extremo de esta semana: admite en el cierre que **nadie ha medido el contagio de la risa**
y que lo anterior son dos hallazgos alrededor y ninguno encima.

---

## La semana del 31 de agosto al 5 de septiembre, pieza a pieza

**Es la primera semana en modo automático.** No tienes que hacer nada: cada vídeo se sube
en privado a las 03:00 con la hora de publicación puesta y YouTube lo hace público solo.

| Día | ID | Serie | La pregunta que responde | Fuentes |
|---|---|---|---|---|
| **lun 31** | MDS-006 | Ríete primero, te explico después | «por qué me río cuando no debo» | E02, A10 |
| **mar 1** | MDS-007 | Diagnósticos | «si te hace gracia el humor negro eres más inteligente» | B04, C02 |
| **mié 2** | MDS-008 | Esto no tiene gracia y esto sí | «por qué unos chistes hacen gracia y otros no» | I02, L01 |
| **jue 3** | MDS-009 | El experimento | «cómo caer bien a la gente» | D05 |
| **vie 4** | MDS-010 | Desmonta el chiste | «si tienes que explicar un chiste pierde la gracia» | A05, A07 |
| **sáb 5** | MDH-005 | Diagnósticos (largo, 4m44s) | «qué dice de mí mi sentido del humor» | B01, B02 |

**Cinco series distintas de lunes a viernes**, una por día. Sigue sin haber datos para
monocultivar ninguna: `metricas.json` está vacío a día de hoy.

Dos decisiones editoriales de esta tanda que conviene tener escritas:

- **MDS-007 no nombra el estudio que todo el mundo cita.** La creencia «si te gusta el
  humor negro eres más inteligente» viene de un estudio vienés de 2017 que **no está en las
  77 obras**. Comentar por su nombre un artículo que no hemos leído es exactamente lo que
  prohíbe la regla 2, así que el Short responde la pregunta con lo que sí tenemos: el 3WD
  de Ruch para el gusto y el metaanálisis de Greengross para la producción. La distinción
  entre *apreciar* humor y *producir* humor es el desmontaje entero.
- **MDS-009 no lleva ninguna cifra en pantalla.** La escena de tipo `dato` pone «Más
  generosos» en vez de un número porque la ficha de `D05` recoge la dirección del efecto y
  no las magnitudes. Antes un hueco que un dato inventado.

**Los seis terminan diciendo dónde falla** lo que acaban de explicar. `MDS-010` es el caso
extremo de la semana: un canal que se dedica a desmontar chistes explicando por qué
explicar un chiste lo mata, y admitiendo que por eso el chiste va siempre antes del
despiece.

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

> ⚠️ **Esta tabla quedó sustituida el 31/08** por las dos escaleras de la versión 4 de
> `00_estrategia/PLAN_DE_CAMBIOS.md` —una para Shorts, sin impresiones ni CTR, porque
> Studio no los da para el formato vertical; otra para el episodio largo—. Se deja aquí
> porque el resto del apartado sigue valiendo. El canal está en el peldaño **S1**.

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
- **MDH-005** — ✅ adaptado al formato nuevo el 27/08 para el sábado 5 de septiembre.
  39 escenas (antes 27), 4m44s, personaje en cuatro escenas, dos intervenciones del
  escéptico, «enunciado» del 62 % al 41 %, primera risa sobre el segundo nueve. Serie
  «Diagnósticos».
- **MDH-006** — ✅ adaptado al formato nuevo el 03/09 para el sábado 12 de septiembre.
  40 escenas (antes 26), 4m47s, personaje en cinco escenas, dos intervenciones del
  escéptico, «enunciado» del 65 % al 42 %, primera risa sobre el segundo ocho. Serie
  «Mecanismos».
- **MDH-007** — ✅ adaptado al formato nuevo el 10/09 para el sábado 19 de septiembre.
  41 escenas (antes 27), 5m16s, personaje en cuatro escenas, dos intervenciones del
  escéptico, «enunciado» del 66 % al 39 %, primera risa sobre el segundo doce y segunda en
  el bloque de improvisación. Serie «Diagnósticos». Y **título nuevo**: de «El miedo a que
  se rían de ti tiene nombre» a **«Por qué se ríen de mí»**, que es lo que la gente
  escribe — «gelotofobia» reúne 9.025 visualizaciones entre diez resultados. Su nota de
  `revisiones/` está aplicada y retirada.
- **MDH-008** — escrito y validado, **sin adaptar**: 48 % de «enunciado», rótulo por
  delante, ningún personaje y doce escenas por encima de 14 s. Su nota sigue en
  `05_calendario/revisiones/`. Le toca en la planificación del 17, para el sábado 26.

**Se adapta uno por semana, no los cuatro de golpe.** Adaptar por adelantado los que aún no
tienen fecha es trabajo especulativo: dentro de dos o tres semanas las métricas dirán qué
formato aguanta y habría que rehacerlo. Cada jueves se adapta el del sábado siguiente y
nada más.

**El largo del 12 de septiembre, decidido el 3 con la demanda medida delante: MDH-006.**
El calendario reservaba la decisión entre dos candidatos y los dos han caído por el mismo
sitio, que no era el que se esperaba:

- El candidato «largo nuevo sobre *cómo ser más gracioso* (`H01`, `H03`)» **ya existe**:
  es `MDH-001`, «Nadie nace gracioso», publicado el 18 de agosto, con H01 en cinco
  escenas, H03 en cuatro y C02 en tres. Escribirlo otra vez tres semanas después sería un
  remake, no un episodio. Descartado por C17.
- **MDH-007** (gelotofobia) sigue siendo bueno, y va el 19. Pero el cierre de `MDH-005`,
  que se produce el sábado 5, promete literalmente «el sitio donde equivocarse sale más
  caro: el trabajo», y el cierre de `MDH-006` promete a su vez la gelotofobia. Respetar
  ese orden mantiene las dos promesas y no obliga a tocar un guion que entra en
  producción en menos de treinta horas.

La demanda no desempata entre los dos: «humor en el trabajo» no se midió, y «miedo a que
se rían de ti» devolvió 74 millones de visualizaciones sin un solo resultado en tema. Con
la demanda callada, decide la coherencia de la serie.

**El largo del 19 de septiembre: MDH-007, y ahora la demanda sí habla.** La medición del
10/09 incluyó por primera vez «por qué se ríen de mí» y el resultado cambia el juicio del
3 de septiembre: de los 66.269.561 del top 10, 65,8 millones son **un solo** vídeo viral
de treinta segundos que no responde nada. Quitado ese, quedan cuatro respuestas reales
—140.816, 126.198, 88.449 y 28.403 visualizaciones— y ninguna nombra el rasgo ni cita un
estudio. Demanda real y competencia de consejo genérico: el mejor perfil de toda la tanda
para un episodio largo. El cierre de MDH-006 ya lo promete, así que la coherencia de serie
y la demanda apuntan al mismo sitio.

**Cómo se adapta un largo viejo** (el patrón está aplicado en MDH-004 y MDH-005, cópialo de
ahí): sacar el rótulo de la escena 1 y poner en su sitio una escena concreta con la primera
risa antes del segundo quince; partir las escenas largas —el validador avisa por encima de
10 s desde el 27/08— en escenas de una sola idea; convertir «enunciado» en `comparacion`,
`lista`, `dato` y `diagrama` hasta bajar del 45 %; meter al personaje en tres o cuatro
escenas, siempre reaccionando *después* y nunca sobre el chiste mientras se cuenta; añadir
una o dos intervenciones del escéptico de menos de doce palabras; y reescribir el título de
publicación a la pregunta que la gente escribe.
- **Los guiones ingleses** (`.en.json`) quedan archivados sin borrar, por si se reabre
  `@humormechanics`.


---

## Semana del 14 al 19 de septiembre de 2026

Escrita la noche del jueves 10. Todo en `parrilla.json` con `"modo": "automatico"` y
`"idiomas": ["es"]`.

| Día | Emisión | Hora | Serie | Pregunta de demanda | Ficha |
|---|---|---|---|---|---|
| Lunes 14 | `MDS-016` | 19:00 | Esto no tiene gracia y esto sí | por qué la ironía no se entiende por whatsapp | `I05` |
| Martes 15 | `MDS-017` | 19:00 | Ríete primero, te explico después | por qué nos hacen gracia las cosquillas | `E06` |
| Miércoles 16 | `MDS-018` | 19:00 | El experimento | un profesor gracioso enseña mejor | `G06` |
| Jueves 17 | `MDS-019` | 19:00 | Ríete primero, te explico después | los anuncios graciosos venden más | `G05` |
| Viernes 18 | `MDS-020` | 19:00 | El experimento | puede la inteligencia artificial hacer chistes | `K02` · `K03` |
| Sábado 19 | `MDH-007` | 12:00 | Diagnósticos | por qué se ríen de mí | `J02` · `J01` · `H05` · `H06` |

**Las seis fichas de los Shorts estaban sin abrir.** Es la primera semana del canal en la
que ningún Short repite una fuente ya usada: C17, paso 2, aplicado empezando por las
libres y no por las conocidas. Quedan treinta fichas sin usar de setenta y siete.

**Las series no se reparten por turno.** Desde el 31/08 la demanda elige el tema y la
serie solo da la forma, así que «El experimento» y «Ríete primero» salen dos veces cada
una — alternadas, nunca en días seguidos. El motivo está en los números: el feed de Shorts
no nos empuja y la búsqueda sí, y a la búsqueda le importa la pregunta, no la serie.

**Estrena el campo `icono` (C19 + C16).** Comprobado en `04_agentes/esquema_guion.json`:
el campo existe y admite los ocho dibujos de `02_marca/iconos.svg`. La escena 1 de los
cinco Shorts entra con icono y cuatro palabras o menos, y ninguna es ya una tarjeta de
texto sobre fondo. Se reparten además por dentro de los guiones, donde el mecanismo tiene
uno: `i-grieta` en los cierres que dicen dónde falla, `i-balanza` donde algo se pesa,
`i-bisagra` donde está el punto que lo decide todo.
