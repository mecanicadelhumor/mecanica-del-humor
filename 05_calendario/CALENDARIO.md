# Calendario editorial — tanda 1

## Cuántos vídeos y por qué ocho

Ocho vídeos en cuatro semanas, dos por semana, en los dos idiomas: **16 subidas**.

No son ocho por capricho. Es el número mínimo que permite responder a las tres preguntas que decidirán
el futuro del canal, y el máximo que se puede producir con calidad antes de saber si algo funciona:

- **Con menos de 6 no hay señal.** YouTube necesita varias piezas para entender de qué va el canal y a
  quién enseñárselo. Con tres vídeos solo se sabe si tuviste suerte.
- **Con más de 10 se produce a ciegas.** Escribir doce guiones antes de ver un solo dato de retención
  es tirar trabajo. La tanda 2 se decide con los números de la tanda 1, no antes.
- **Ocho permite probar cuatro formatos distintos por duplicado**: tesis, mecanismo, autodiagnóstico y
  técnica pura. Cada uno aparece dos veces, así que si uno destaca, no será casualidad.

Dos por semana es sostenible con este pipeline (el coste marginal de un vídeo es un guion) y suficiente
para que el canal parezca vivo desde el primer mes.

## Parrilla

> **Cambio de ritmo, 18 de agosto.** El vídeo 001 salió el 18 en los dos canales, no el 11. A partir
> del 19 se pasa de dos vídeos por semana a **uno al día**: los guiones ya estaban escritos y el
> workflow no va cargado, así que la parrilla original solo servía para retrasar el momento de saber
> si el canal funciona. Con ritmo diario la tanda 1 cierra el **25 de agosto** en vez del 4 de
> septiembre, y la decisión sobre la tanda 2 se toma unos diez días antes.

Publicación **diaria a las 18:00 (hora española)**. El canal en inglés publica el mismo episodio a las
**17:00 CEST** (11:00 ET), que es cuando despierta el grueso de la audiencia estadounidense.

La parrilla ejecutable —la que lee el sistema— es `05_calendario/parrilla.json`. Esta tabla es su
versión legible; si las dos no coinciden, manda el JSON.

| # | Fecha | Vídeo | Pilares | Formato | Modo | Fuentes clave |
|---|---|---|---|---|---|---|
| 001 | mar 18 ago | Nadie nace gracioso | H, C | Tesis | publicado a mano | H01, H03, C02, C01 |
| 002 | **mié 19 ago** | Por qué te ríes: el mecanismo | A, F | Mecanismo | revisión | A01, A02, F01, F02 |
| 003 | **jue 20 ago** | «Todavía es pronto para reírse de eso» | A | Mecanismo | revisión | A03, A04 |
| 004 | **vie 21 ago** | Casi nadie se ríe de los chistes | E, D | Tesis | revisión | E01, E02, D07, A10 |
| 005 | **sáb 22 ago** | Tu estilo de humor (y el que te está costando amigos) | B | Autodiagnóstico | automático | B01, B02, D08 |
| 006 | **dom 23 ago** | Humor en el trabajo sin arruinarte la carrera | D, G | Técnica | automático | D01, D02, G01 |
| 007 | **lun 24 ago** | El miedo a que se rían de ti tiene nombre | J, H | Autodiagnóstico | automático | J01, J02, H05 |
| 008 | **mar 25 ago** | Cómo se construye un chiste, pieza a pieza | I, L | Técnica | automático | I01, A05, L01 |

**Los dos modos.** En *revisión*, el vídeo se sube en privado y sin fecha: Silvestre lo mira y le da a
publicar. En *automático*, se sube en privado con `publishAt`, y es YouTube quien lo hace público a la
hora de la parrilla — entre la subida (03:00) y la publicación (18:00) hay quince horas para
cancelarlo si algo no cuadra. Del 19 al 21 se revisa; del 22 en adelante, vuela solo.

### Por qué este orden

El vídeo 1 planta la tesis del canal (**se entrena**) porque sin eso todo lo demás es trivia. El 2 da la
herramienta que se usará en los seis restantes (violación benigna). El 3 la pone a prueba con el caso
más incómodo posible, que es también el más comentable. El 4 es el vídeo diseñado para viralizar: un
dato contraintuitivo, fácil de contar en una cena.

A partir del 5, el canal pasa de explicar a intervenir: qué tipo de humor usas tú, cómo aplicarlo donde
te juegas algo, qué hacer con el miedo, y por último la técnica desnuda. El 8 cierra el círculo: si el
1 prometía que se entrena, el 8 es el entrenamiento.

### Los cuatro formatos que se están probando

| Formato | Qué mide | Vídeos |
|---|---|---|
| **Tesis** | ¿Engancha una idea grande? | 001, 004 |
| **Mecanismo** | ¿Aguantan la explicación técnica? | 002, 003 |
| **Autodiagnóstico** | ¿Funciona el «esto va de ti»? | 005, 007 |
| **Técnica** | ¿Vuelven a por instrucciones? | 006, 008 |

Cada formato tiene dos representantes. Al terminar la tanda, el agente analista compara retención media
a los 30 s, retención al 50 % y CTR por formato, y el editor jefe construye la tanda 2 alrededor del
ganador.

## Cadencia diaria

| Cuándo | Quién | Qué |
|---|---|---|
| 03:00 · todos los días | GitHub Actions | `cola.py` mira la parrilla, y si toca emisión produce el episodio en los dos idiomas: voz, render, montaje, miniatura, subida y expediente de calidad |
| 07:00 · todos los días | Cowork | Revisión de calidad: lee el expediente del vídeo de esta noche, busca defectos y aplica las mejoras a los guiones que aún no se han producido |
| 18:00 / 17:00 | YouTube | Publicación (automática desde el 22 de agosto) |
| Jueves 22:00 | Cowork | Planificación de la tanda siguiente: ocho episodios en español y sus adaptaciones inglesas |

Nadie tiene que acordarse de lanzar nada. El cron de Actions es lo único que dispara producción, y lo
que produce lo decide la parrilla, no el workflow: cambiar el ritmo del canal es editar
`parrilla.json`, no tocar el YAML.

**Por qué el jueves por la noche.** Los límites de cómputo de Claude se reinician el viernes por la
mañana, así que planificar el jueves a última hora gasta lo que de todas formas iba a caducar.

### Qué te sigue tocando a ti

Del 19 al 21 de agosto, revisar el vídeo por la mañana y darle a publicar: diez minutos. A partir del
22 no hace falta que hagas nada. El sistema sube en privado con fecha programada, así que si un día
quieres frenar algo, tienes hasta las 18:00 para hacerlo desde YouTube Studio.

## Métricas de la tanda y qué decidiremos con ellas

| Métrica | Objetivo mínimo | Si no se cumple |
|---|---|---|
| Retención a los 30 s | ≥ 60 % | El problema está en el gancho: se reescriben los primeros 15 s de todos |
| Retención media | ≥ 40 % | Los vídeos son largos: bajar a 4–5 min |
| CTR | ≥ 4 % | Miniatura y título: el empaquetador genera nuevas variantes |
| Comentarios por cada mil vistas | ≥ 3 | Falta pregunta explícita al espectador en el cierre |
| Suscriptores por cada mil vistas | ≥ 5 | La promesa del canal no queda clara: reforzar el cierre |

**Decisión del 5 de septiembre:** si dos formatos superan los mínimos, la tanda 2 son 10 vídeos con esos
dos. Si ninguno lo hace, se cambia el formato de raíz antes de producir nada más — no se insiste con más
volumen.

## Reserva

Temas ya documentados y listos para entrar si algo se cae o si un vídeo dispara:

- Por qué las ratas se ríen cuando les haces cosquillas (`E06`)
- ¿Es la gente graciosa más inteligente? (`C01`, `C02`)
- El humor negro y quién lo entiende (`J05`, `B04`)
- Qué pasa en tu cerebro en los 200 ms de un chiste (`F02`, `F04`)
- ¿Puede una IA ser graciosa? Se lo preguntamos a 20 cómicos (`K02`, `K03`)
- La broma que sube tu estatus y la que lo hunde (`D01`)
