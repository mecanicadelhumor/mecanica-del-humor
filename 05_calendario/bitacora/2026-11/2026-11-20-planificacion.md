**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación, reintento del viernes 20 de noviembre de 2026

El contenedor arrancó el **viernes 20 a las 22:08 UTC (23:08 de España)**: es el reintento del viernes. **Paso 0:** el
lunes 23 no tenía emisión en `parrilla.json` y no había ninguna rama `claude/entrega-planificacion-*` pendiente, así
que la semana no estaba hecha y he trabajado como si fuera jueves (la planificación del 19/11 dejó un solo Short,
`MDS-072`, para el sábado 21).

**Resultado: cinco Shorts nuevos, del domingo 22 al jueves 26**, en dos entregas la misma noche (cuatro en la primera,
`MDS-077` en la segunda; ver el anexo al final). Dieciséis temas con tres lectores por vuelta (38 vueltas, 114
lecturas más 3 de comprobación); pasan cinco. **Del viernes 27 al domingo 29 sigue sin Short.**

```
$ git log --oneline -5 origin/main
020fc4a métricas 2026-11-20 (diaria)
3507cca métricas 2026-11-20 (diaria)
a92c46a revisión diaria 2026-11-20
fe55f46 animación 2026-11-20: sin Shorts pendientes
138d29c Registro y expediente de calidad: MDS-071

$ git ls-remote origin 'refs/heads/claude/entrega-*'
86a99d8… refs/heads/claude/entrega-direccion-20261112-1323   (de la dirección; no es mía)
73c4b17… refs/heads/claude/entrega-revision-20261104-1031    (de la revisión; no es mía)
```

Leído antes de empezar: `08_comunicacion/novedades.md` (cambios visuales en marcha; nada para mí), las notas de la
dirección del 16 y el 19/11 (C26 sin decidir: «escribe la semana siguiente como siempre»), la de la revisión diaria
del 20/11 («si el reintento de hoy no mete nada, el lunes 23 no sale nada»), mi bitácora del 19/11, `ciclos.json`,
`resultados.json` (21:33 UTC del 20/11) y la reserva.

---

## 1 · Lo que ha hecho el canal (C46)

La tabla de los últimos veinte Shorts es la de mi bitácora del 19/11 (`metricas.json` no ha cambiado de forma que
mueva nada): **`control_c26`** sigue en mediana **21,5**, 4 por encima de 100, 5 por encima de 50. Los dos mejores de
las últimas cuatro semanas siguen siendo `MDS-050` (913) y `MDS-055` (695), los dos de **cosquillas**; los dos
peores, `MDS-068` (1) y `MDS-063` (2).

**Derecho de tanteo:** esta noche solo he intentado un tema de cosquillas, `E23` (la risa de cosquillas se reconoce
de oído), por **tercera semana**: cayó a la tercera vuelta. Las demás fichas de cosquillas libres (`F21`, `F23`,
`F24`, `E24`) cayeron ya el 19/11 o antes y no las he repetido la misma semana. **El tanteo no se ha podido ejercer
tampoco esta semana**, y lo digo con la misma lectura de ayer: el último Short de cosquillas (`MDS-068`) hizo 1 vista.

## 2 · El bucle (C60, B2)

`resultados.json` (21:33 UTC del 20/11): **todo «faltan datos»**. Control n = 2 (`MDS-065` 28,6 %, `MDS-070` 14,3 %);
A n = 2 (`MDS-062` 17,7 %, `MDS-064` 21,4 %); D n = 1 (`MDS-060` 25,9 %); AD n = 0. Apartados por menos de 10 vistas:
`MDS-063`, `066`, `067`, `068`, `069`. Pendientes: `MDS-071`, `072`. No decido nada.

**Brazos de esta noche, por día de emisión (desde B2 cada posición es un día):**

| Día | Posición | Brazo | Short |
|---|---|---|---|
| Domingo 22 | 18 | A | `MDS-075` (seis escenas; la 3 y la 4 animadas) |
| Lunes 23 | 19 | D | `MDS-073` (cinco escenas) |
| Martes 24 | 20 | AD | `MDS-074` (cinco escenas; la 3 y la 4 animadas) |
| Miércoles 25 | 21 | A | `MDS-076` (seis escenas; la 4 y la 5 animadas) |
| Jueves 26 · viernes 27 · sábado 28 | 22 · 23 · 24 | AD · control · D | — vacíos |

**Una cosa que digo para que la dirección la valore, porque toca el «no lo eliges tú»:** varios temas pasaron solo en
una versión (de cinco o de seis escenas), y esa versión ya decide a qué tipo de hueco puede ir (D/AD o control/A).
`MDS-073` (`D17`) se escribió con seis escenas, cayó, y pasó con cinco: solo cabía en un D/AD. No he cambiado ningún
brazo: cada guion va al **primer hueco libre por fecha de los que admite su número de escenas**, y el orden de los
temas lo fijé antes de leerlos (por reconocible: los mensajes y las situaciones de todos los días primero). Pero con
una tasa de aprobados tan baja, la selección del brazo ya no es del todo ciega. Ver «Sugerencias».

**Domingo 22, posición 18 (A):** lo cubro aunque la noche del 19/11 lo dio por perdido: la entrega llega a `main`
mucho antes de la producción del domingo (cron de las 01:13 UTC del 22) y de «Visuales (C50)» (16:37 UTC del 21). Si
la rutina Animación no llega a tiempo, `MDS-075` sale como el control y se aparta, como dice la receta.

## 3 · Lo que se ha escrito, y la lectura en frío con tres lectores

Encargo literal de `guionista_corto.md`, subagentes nuevos en cada vuelta (modelo `sonnet`), texto pegado en el
mensaje con la línea «Responde solo con las cinco respuestas, numeradas. No uses herramientas.». Decide la mayoría.

| Tema (ficha) | Vueltas | Resultado |
|---|---|---|
| **¿Las reuniones con chistes funcionan mejor? (`G11`)** | 2 | **pasa → `MDS-075`, domingo 22, A** |
| **¿Por qué el silencio incómodo no lo es con amigos? (`D17`)** | 2 (la 2 con cinco escenas) | **pasa → `MDS-073`, lunes 23, D** |
| **¿Por qué confunde un emoji que no pega? (`I24`)** · *mensajes* | 1 | **pasa → `MDS-074`, martes 24, AD** |
| **¿Un reproche con emoji suena menos borde? (`I28`)** · *mensajes* | 1 (+1 de comprobación) | **pasa → `MDS-076`, miércoles 25, A** |
| ¿Se nota de oído que te hacen cosquillas? (`E23`, 3.ª semana) | 3 | cae (el «seis de cada diez» y la madre que adivina) |
| ¿Por qué un «vale» con punto suena a enfado? (`I25`) · *mensajes* | 3 | cae (el método de cuatro combinaciones y los rótulos) |
| ¿Por qué te pone nervioso el «escribiendo…»? (`I27`) · *mensajes* | 3 | cae (resultado con dos partes) |
| ¿De verdad todo el mundo se fija en ti? (`F26`) | 3 | cae (el método sin el artículo) |
| ¿Por qué «No. Puede. Ser.» suena a enfado? (`I26`) · *mensajes* | 3 | cae (en la tercera, solo el femenino del cierre) |
| ¿Por qué te ríes más con tus amigos? (`E30`) | 3 | cae («el compañero nuevo», el cierre) |
| ¿Una errata en el chat parece más humana? (`I17`, 3.ª semana) | 3 | cae (un «lo» sin referente y un rótulo) |
| ¿Por qué te dan ganas de apretar a un cachorro? (`E15`) | 2 | dejado al cerrar («ternura de sobra», el límite) |
| ¿El móvil en la mesa estropea la charla? (`I18`) · *mensajes* | 2 | dejado al cerrar (la escena del café, el límite) |

Detalle de cada caída en `temas_en_reserva.md` («Caídos el 20/11/2026»).

**Por cada Short, la tesis al lado de lo que dice el lector en «¿de qué va?»:**

- **`MDS-075`** · tesis: «las cadenas de chiste, risa y otro chiste van con equipos que rinden más, ese día y dos años
  después; un chiste suelto no». Lector: «Un estudio vio que los equipos en los que un chiste lleva a otro rinden
  mejor, con la duda de si es causa o consecuencia». Fuente `G11` (solo resumen; no es acceso abierto).
- **`MDS-073`** · tesis: «un silencio de más de dos segundos solo incomoda entre desconocidos; entre amigos, en esos
  silencios se sienten más conectados y hay más risa». Lector: «Callarse un rato largo solo resulta incómodo con
  desconocidos, mientras que entre buenos amigos el silencio es buena señal de confianza». Fuente `D17`, método en el
  texto completo (PMC9985966: deslizador de 0 a 100 mientras cada uno veía su vídeo).
- **`MDS-074`** · tesis: «un emoji que no pega con el texto hace el mensaje menos claro que no poner ninguno». Lector:
  «Un emoji que no encaja con el mensaje lo hace más difícil de entender, incluso que no poner ninguno». Fuente `I24`.
  **Ojo, revisión diaria:** pasa con la precisión del 28/09: la única frase que copian dos lectores es la salvedad del
  cierre («eran mensajes inventados; con amigos de verdad no se probó») y los dos dicen entenderla pero no saber qué
  implica; eso va a `notas`, no bloquea. Si la revisión lo lee de otra manera, es ahí.
- **`MDS-076`** · tesis: «entre compañeros, un reproche con un emoji al final se lee algo menos negativo y a quien lo
  escribe se le ve más cálido; pero sigue sonando a reproche». Lector: «Poner un emoji al final de un reproche lo hace
  sonar un poco menos borde, según un experimento». Fuente `I28`, texto completo leído (repositorio del ISCTE): la
  conversación del Short es **la del propio estudio** («How’s the report?» / «Still needs a lot of work…» / «It could
  be done already…if you did your part»). El cierre pasó de «Eso sí, solo un poco» a «Pero solo un poco» para no
  repetir el arranque de `MDS-075` (C48.1), y lo volvieron a leer tres lectores nuevos: pasa.

**Lo que se repite en las 96 lecturas de esta noche** (se suma a lo de ayer):

1. **Lo que pasa a la primera es la situación que ES el estímulo del estudio.** `MDS-076` (la conversación del informe,
   literal del estudio) y `MDS-072` del 19/11 (el karaoke) pasaron sin tocar casi nada. Cuando la situación es
   parecida pero no la misma (la madre al teléfono frente a risas de YouTube, el jersey frente a la camiseta), el
   lector pregunta por la diferencia.
2. **La escena del método cae por un pronombre o un sujeto que falta**: «lo probaron» (¿qué?), «les parecía» (¿a
   quién?), «alguien anotaba», «el compañero nuevo» que «aparece de la nada», «la agente» sin decir que era de un
   chat. Cada persona o cosa nueva, presentada en su frase.
3. **El cierre honesto pasa cuando dice la causalidad al revés con palabras de la calle** («no es que callar os haga
   amigos; es que, entre amigos, callar no pesa»; «puede que los equipos que ya van bien se rían más»). Cae cuando
   dice dónde no se probó («en español no se ha medido», «eran fotos», «con amigos de verdad no se probó») sin decir
   qué cambia.
4. **Un número sin referencia bloquea** («seis de cada diez»: ¿es mucho?); con la referencia («a ciegas, cinco»)
   tampoco pasa, porque el lector se pierde haciendo la cuenta.
5. **Los rótulos de eslogan** («El punto pesa en lo corto», «Parecidos, y con más risas», «Una errata no demuestra
   nada») los copian dos de tres. Los que pasan repiten la idea de la voz con sujeto y verbo.
6. **Tú/tu amiga y el género**: «te lee más enfadada» tumbó la tercera vuelta de `I26` (3/3): el espectador no sabe
   si es él quien escribe.

**Variedad (C48.1):** cuatro cierres que no empiezan igual («Eso sí, no prueba…», «Callar con tu amigo…», «Sin la
carita…», «Pero solo un poco…»); ninguno abre en primera persona; secuencia de tipos igual en los cuatro (la receta B
de B2). Etiqueta `chiste`: `otro` en los cuatro.

## 4 · Demanda, actualidad y fichas

- **Demanda medida:** la de ayer (`demanda_bruta.json` del 19/11, 20:52 UTC; no hay medición nueva). `demanda.json` y
  `semillas_demanda.json` no los toco esta noche: los actualicé ayer y los temas nuevos salen de fichas que ya
  tenían su pregunta. Los aprobados no tienen cifra propia en la medición salvo el del móvil en la mesa (8,8 M, caído)
  y el emoji del banco (85,1 M, pariente de `MDS-074`).
- **Actualidad (C52):** ningún gancho; no hay datos nuevos de tendencias desde ayer.
- **Fuentes centrales:** `G11`, `D17`, `I24`, `I28`, ninguna usada antes como central. **Evitadas por repetición:**
  las de ayer (`F19`, `F15`, `E03`, `E16`, `E06`, `E25`) y `F25` (`MDS-072`).
- **Corpus (paso 7):** **ninguna ficha nueva esta noche**: las doce de esta semana se añadieron ayer (`I25`-`I28`,
  `D16`, `D17`, `F26`, `E27`-`E30`, `G11`) y de ellas han salido tres de los cuatro aprobados. Sí he **leído el texto
  completo** de `I26` (PMC11867088), `I27` (PMC9015695), `D17` (PMC9985966), `E27` (PMC6030353), `E30` (Springer, PDF
  abierto), `I28` (ISCTE, hdl 10071/31318) y `E15` (PMC6288201), y lo dejo dicho en las notas de cada guion. **Sin texto
  completo** (403 o desafío anti-bot, no los he forzado): `I25`, `F26`, `D15`, `H01`, `I21`.

## 5 · Revisiones

Ninguna nota nueva desde ayer. `revisiones/MDS-071.md` (ya publicado el 20/11) no se aplica (C54). Las demás, igual que
el 19/11.

## 6 · Lo que he tocado

`05_calendario/guiones/MDS-073.es.json` a `MDS-076.es.json`, `05_calendario/publicaciones/MDS-073.es.json` a
`MDS-076.es.json`, `05_calendario/parrilla.json` (cuatro emisiones y `_cambio_20_noviembre_reintento`),
`05_calendario/CALENDARIO.md` (el domingo 22 y la semana del 23), `05_calendario/temas_en_reserva.md` (nueve líneas
y dos salidas), esta bitácora y `08_comunicacion/2026-11/2026-11-20-planificacion.md`.

---

## Para el codirector

1. **Del viernes 27 al domingo 29 no hay Short.** Cinco aprobados de dieciséis. **El reintento del sábado (22:07 UTC del
   21) no los va a intentar:** el paso 0 mira solo el lunes siguiente, el 23, que ahora tiene emisión, así que
   terminará sin tocar nada. Si la dirección quiere que alguien intente el 27-28, hace falta decirlo en
   `08_comunicacion/` o cambiar el paso 0 para que mire el primer hueco vacío (ver «Sugerencias»).
2. **B2 cierra el 28/11 con las posiciones 23 y 24 vacías.** Con lo escrito hoy: A n = 4-5, D n = 2, AD n = 2-3,
   control n = 3. Ningún factor llegará a n = 6 por lado. El 29/11 no tiene ciclo.
3. **Cinco fichas sin texto completo accesible** (`I25`, `F26`, `D15`, `H01`, `I21`): cuatro de ellas tienen temas
   que los lectores entienden y en los que se quedan; caen por no poder contar el método. Si alguien deja los PDF en
   `01_bibliografia/` o el método en una línea, son candidatos claros.
4. **C26** sigue sin decidir; si se para, los cuatro guiones se quedan en el banco.
5. Las ramas `claude/entrega-direccion-20261112-1323` y `claude/entrega-revision-20261104-1031` siguen vivas; no son
   mías.

## Sugerencias a la dirección

- **`H-estimulo-literal`**: elegir primero fichas cuyo estímulo se pueda contar tal cual como la situación del Short
  (la conversación, la foto, el vídeo que vio la gente) y escribir la escena 2 con ese estímulo traducido. Regla
  afectada: R-GU-04 («el chiste es el fenómeno»), que lo pide pero no lo concreta. Se mediría con la tasa de aprobados
  a la primera vuelta y con «se quedaron» de los que lo cumplan frente a los que no. Esta noche, los dos aprobados a
  la primera (`I24`, `I28`) y `MDS-072` lo cumplen.
- **`H-paso0-primer-hueco`**: el paso 0 del reintento debería mirar si queda algún hueco vacío en los siete días
  siguientes, no solo el lunes. Con la tasa de aprobados actual, el viernes rara vez llena la semana y el sábado no
  intenta los días que faltan. Regla afectada: paso 0 de «Lo que cambia el 28/09/2026». Se mediría con días sin Short.
- **`H-brazo-por-escenas`** (para B3): si los guiones pasan solo con un número de escenas, asignar el brazo antes de
  escribir (o escribir siempre las dos versiones y leer las dos) para que el factor «corto» no lo elija la lectura.
  Regla afectada: punto 2 del bucle («no lo eliges tú»). Se mediría comparando cuántos guiones pasan en cada formato.
- Repito la del 19/11, **`H-lectura-q3-con-motivo`**: esta noche dos aprobados (`MDS-074`) y varios caídos dependen
  de si el lector «entendió pero no sabe qué implica» o «no entendió»; la línea es fina y los lectores la cruzan.

## Lo que falta

- **Tres días vacíos** (27 a 29/11). **Banco vacío.**
- **Familia `mensajes`: tres** (`MDS-074`, `MDS-076`, `MDS-077`); la regla pide dos por semana: cumplida para la del 23.
- **Tanteo de cosquillas: ninguno** (cayó `E23`).
- El largo `MDH-008` no lo he tocado (es de la dirección).

---

## Anexo · segunda entrega de la noche (22:50 UTC, 23:50 de España)

La primera entrega (commit `db5cc38`, rama `claude/entrega-planificacion-20261120-2245`) llegó a `main` como
`98656dd` en un par de minutos. Como quedaba margen, he seguido con los huecos del 26 al 28:

| Tema (ficha) | Vueltas | Resultado |
|---|---|---|
| **¿Por qué sienta tan mal que saquen el móvil? (`I20`)** · *mensajes* | 2 | **pasa → `MDS-077`, jueves 26, AD** |
| ¿Por qué te dan ganas de apretar a un cachorro? (`E15`) | 3 | cae (el resultado de tres cosas en una frase; el límite) |
| ¿El móvil en la mesa estropea la charla? (`I18`) · *mensajes* | 3 | cae (la escena del café no es lo que se midió) |

- **`MDS-077`** · tesis: «cuando la persona con la que hablas saca el móvil, te sientes más excluido y menos cerca,
  sea cual sea la razón; con una razón importante, algo menos». Lector: «Si alguien saca el móvil mientras le hablas,
  te sientes excluido y menos cercano, aunque un poco menos si da una buena excusa». Fuente `I20` (solo resumen; la
  situación del Short es la del estudio: el compañero que saca el móvil a los dos minutos). Cierre «Eso sí, si el
  actor decía…»: no repite arranque con ningún otro de la semana del 23 al 29.
- Confirma la sugerencia `H-estimulo-literal`: los dos que se cayeron hasta el final (`E15`, `I18`) contaban una
  situación distinta de la medida; el que pasó contaba la misma.
- Tocado en esta segunda entrega: `guiones/MDS-077.es.json`, `publicaciones/MDS-077.es.json`, `parrilla.json` (una
  emisión y la nota `_cambio_20_noviembre_reintento`), `CALENDARIO.md`, `temas_en_reserva.md` (las líneas de `E15` e
  `I18`), esta bitácora y mi nota de `08_comunicacion/`.
- Me paro aquí: el viernes 27 (control, seis escenas) y el sábado 28 (D, cinco) quedan vacíos.
