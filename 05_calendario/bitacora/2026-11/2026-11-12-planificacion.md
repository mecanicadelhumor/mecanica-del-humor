**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación del jueves 12 de noviembre de 2026

El contenedor arrancó el **jueves 12 a las 22:08 UTC (23:08 de España)**: es la ejecución buena del jueves,
no un reintento. **Resultado: cuatro Shorts para la semana del 16 al 22/11** (`MDS-068` a `MDS-071`). Jueves 19,
sábado 21 y domingo 22 se quedan sin emisión; el domingo 15 sigue vacío.

```
$ git log --oneline -5 origin/main
5f5f7aa métricas 2026-11-12 (diaria)
7ad9c2b medición de demanda 2026-11-12
a198459 métricas 2026-11-12 (diaria)
473cf4e dirección 2026-11-12: plan v31 — el Short doble del 9/11 (MDS-067), la voz 3.8 lee en voz alta …
8c8a8cc dirección 2026-11-12: prueba de voz «voces:» (3.8, solo el texto, cuatro voces más) …

$ git ls-remote origin 'refs/heads/claude/entrega-*'
86a99d8… refs/heads/claude/entrega-direccion-20261112-1323   (de la dirección, fallida; no es mía)
73c4b17… refs/heads/claude/entrega-revision-20261104-1031    (de la revisión; no es mía)
```

Leído antes de empezar: `08_comunicacion/novedades.md` (cambios visuales en marcha; nada para mí), la nota de la
dirección del 12/11 (el domingo 15 sigue vacío; si se llena, con lectura en frío; el largo no antes del 22/11;
evitar que dos escenas repitan la anécdota, como `MDS-066`), su bitácora del 12/11 y la mía del 07/11.

---

## 1 · Lo que ha hecho el canal (C46)

Últimos veinte Shorts con `vistas_48h` (`metricas.json`, lectura más alta de cada uno):

| Short | Publicado | Pregunta | Vistas 48 h | Se quedaron % |
|---|---|---|---|---|
| `MDS-041` | 10-17 | ¿Por qué sentimos vergüenza ajena? | 191 | 6.8 |
| `MDS-042` | 10-18 | ¿Por qué nos da la risa en un funeral? | 9 | 33.3 |
| `MDS-043` | 10-19 | ¿Se pega más una risa o un bostezo? | 27 | 40.7 |
| `MDS-044` | 10-20 | ¿Qué significa el emoji de la sonrisa? | 112 | 13.4 |
| `MDS-045` | 10-21 | ¿Por qué todos se ríen de los chistes del jefe? | 10 | 80.0 |
| `MDS-046` | 10-22 | ¿Qué pasa si te aguantas la risa? | 4 | 25.0 |
| `MDS-047` | 10-23 | ¿Por qué dan miedo los payasos? | 35 | 37.1 |
| `MDS-048` | 10-24 | ¿Por qué discutir por WhatsApp sale peor? | 5 | 20.0 |
| `MDS-049` | 10-25 | ¿Por qué después de reírte cuentas de más? | 70 | 25.7 |
| `MDS-050` | 10-26 | ¿Por qué te ríes antes de las cosquillas? | **913** | 15.7 |
| `MDS-051` | 10-27 | ¿Sirve de algo escribir «jajaja» sin reírte? | 32 | 31.2 |
| `MDS-052` | 10-28 | ¿Se nota cuando alguien se ríe por compromiso? | 11 | 36.4 |
| `MDS-053` | 10-29 | ¿Hacer un chiste en una reunión te da puntos? | 16 | 37.5 |
| `MDS-054` | 10-30 | ¿Por qué escribimos en vez de llamar? | 30 | 36.7 |
| `MDS-055` | 10-31 | ¿Puede hacerte cosquillas una máquina? | **695** | 25.5 |
| `MDS-056` | 11-01 | ¿Por qué hay gente que se ríe de lo que cuenta? | 12 | 16.7 |
| `MDS-057` | 11-02 | ¿Los gorilas tienen cosquillas? | **428** | 43.5 |
| `MDS-058` | 11-03 | ¿Por qué duele que dejen de contestarte? | 10 | 60.0 |
| `MDS-059` | 11-04 | ¿Reírse adelgaza? | 4 | 50.0 |
| `MDS-060` | 11-05 | ¿Queda mal un emoji en un correo de trabajo? | 27 | 25.9 |

Fuera de la tabla, del bucle: `MDS-062` (la comedia a solas, 10/11) **280** a 48 h; `MDS-067` (la ironía, 9/11) 3.

- **Los dos mejores de las últimas cuatro semanas:** `MDS-050` (913) y `MDS-055` (695), **los dos de cosquillas**
  (y el tercero, `MDS-057`, 428, también). **Los dos peores:** `MDS-046` y `MDS-059` (4 cada uno).
- **`control_c26`** (10/11): mediana **27**, 5 por encima de 100, 6 por encima de 50.
- **Derecho de tanteo:** `MDS-068` (¿las ratas se ríen con las cosquillas?) continúa el asunto de las cosquillas.
  Se intentaron **siete** temas de cosquillas esta noche (ratas que se ríen, ratas que piden y huyen, contagio
  en ratas, cosquillas y risa por cuestionario, la risa de cosquillas de oído, el truco de hacerte cosquillas tú,
  y los perros que «se ríen» al jugar y con cosquillas); pasaron dos (`MDS-068` y, de lado, `MDS-071`).

## 2 · El bucle (C60, B2)

`resultados.json` (21:08 UTC del 12/11): **todo «faltan datos»**. Control n = 0; A n = 1 (`MDS-062`, 18,2 %); D n = 1
(`MDS-060`, 25,9 %); AD n = 0. `MDS-067` (D) apartado por pocas vistas (3). Pendientes de 48 h: `MDS-063` a `066`.
Referencia anterior: n 14, «se quedaron» 32,9 %. No decido nada.

**Brazos de la semana** (posición = día; la 1 es el 5/11): 15/11 AD (11) · 16 A (12) · 17 AD (13) · 18 control (14)
· 19 D (15) · 20 A (16) · 21 control (17) · 22 A (18).

Los guiones se escribieron **con seis escenas y sin mirar el brazo**; el orden de los temas lo decidí antes de
asignar (ratas → sonrisa → «Qué bien» → perros). Al aplicar el orden por fecha, **el jueves 19 (D) pedía una
versión corta de los perros y no pasó a la tercera vuelta**, así que los perros van al viernes 20 (A), el
siguiente día libre de seis escenas. Lo digo porque es la única vez que el brazo ha movido un tema de día: no
cambié el tema de brazo, me salté un día. Si la dirección prefiere que en ese caso el día se quede vacío y el
tema espere al banco, una línea en el prompt lo arregla.

## 3 · Lo que se ha escrito, y la lectura en frío con tres lectores

**Catorce temas, dos versiones cortas, 42 vueltas (125 lecturas: en una vuelta solo llegaron dos lectores por el
límite de veinte subagentes a la vez; se dice en su guion). Pasan cuatro.** Encargo literal de `guionista_corto.md`,
subagentes nuevos en cada vuelta (modelo `sonnet`), decide la mayoría.

| Tema (ficha) | Vueltas | Resultado |
|---|---|---|
| **¿Las ratas se ríen con las cosquillas? (`E06`)** | 3 | **pasa → `MDS-068`, lunes 16, A** |
| ¿Por qué pides que paren las cosquillas y luego más? (`F20`, 2.ª semana) | 3 | cae |
| ¿Por qué te retuerces al ver cosquillas a otro? (`F17`, 2.ª) | 3 | cae |
| ¿Ver algo gracioso te quita el dolor? (`G08`, 4.ª del tema) | 3 | cae |
| ¿Por qué te ríes justo cuando se ríe tu amigo? (`E17`, 2.ª) | 3 | cae |
| ¿Por qué queda tan mal un emoji del banco? (`I22`, 3.ª) · *mensajes* | 2 | cae (cambio de tema) |
| **¿Por qué un «Qué bien» sin emoji suena frío? (`D10`, reserva) · *mensajes*** | 2 | **pasa → `MDS-070`, miércoles 18, control** |
| ¿Los animales también se ríen? (`E19`) | 1 | sustituido por `E25` |
| ¿Quien tiene más cosquillas se ríe más? (`F11`) | 3 | cae |
| **¿Sonreír a la fuerza te pone contento? (`E18`, reserva)** | 3 + 3 (corta) | **pasa → `MDS-069`, martes 17, AD (cinco escenas)** |
| **¿Los perros se ríen? (`E25`, nueva)** | 1 + 3 (corta) | **pasa la de seis → `MDS-071`, viernes 20, A**; la corta cae |
| ¿Por qué molesta tanto que tarden en contestar? (`I23`, nueva) · *mensajes* | 3 | cae |
| ¿La risa de las cosquillas suena distinta? (`E23`, nueva) | 3 | cae |
| ¿Hay un truco para aguantar las cosquillas? (`F21`, nueva) | 3 | cae |

**Respuesta 1 del lector («¿de qué va?») al lado de la tesis**, para la comparación del viernes:

- `MDS-068` · Tesis: con cosquillas las ratas chillan tan agudo que no se oye, y quienes las estudian dan razones
  para pensar que es una especie de risa. · Lector: «Las ratas chillan en ultrasonidos cuando les haces cosquillas,
  y unos científicos creen que es como una risa que no oímos».
- `MDS-069` · Tesis: poner cara de sonrisa a propósito alegra algo (3.878 personas, 19 países). · Lector:
  «Sonreír a propósito, aunque no tengas ganas, te deja un poco más contento, según un estudio con casi cuatro mil
  personas».
- `MDS-070` · Tesis: la misma respuesta con emoji parece más atenta, y eso la hace más cercana. · Lector: «Una
  respuesta con emoji hace que un amigo parezca más atento y cercano que la misma frase sin él, aunque se probó con
  chats imaginados».
- `MDS-071` · Tesis: los perros tienen un jadeo de juego que sale al jugar, con cosquillas y mimos, y casi nunca
  al entrenar o descansar. · Lector: «Los perros tienen un jadeo especial que solo les sale cuando juegan, y se
  parece a una risa».

**Dos decisiones de criterio que la dirección puede querer revisar** (están en el `recuento` de cada guion):

1. `MDS-069` (vuelta 3 de la corta): dos lectores dicen de «Eso el estudio no lo dice» que no saben «a qué estudio
   se refiere». Los dos lo identifican con «los psicólogos» de la escena 3 y lo que echan en falta es el nombre; lo
   he tratado como la firma de la fuente (criterio del 28/09, a `notas`), no como frase no entendida.
2. `MDS-071`: después de la lectura cambié el rótulo de la escena 2, «Sienta… quieto» → «Serio y atento», porque lo
   marcaron dos lectores (uno lo entendía por el contexto) y además incumplía la regla 14 (la pantalla decía algo que
   la voz no dice). No toca la narración. `MDS-070`: quitado «Sin nada más.» de la escena 3, que un lector nombró como
   la frase que sobra (criterio c del punto 4).

**Lo que se repite en las 125 lecturas** (para el próximo jueves):

1. **El brazo B castiga el arranque cuando el dato llega antes que la situación.** En `G08` (el dolor), `I22` (el
   banco) y `F11` (cosquillas y risa) la mayoría no entendió la escena 1 hasta la 2 o la 3 («¿qué brazo?», «¿qué
   carita?», «¿reírse por las cosquillas o en general?»). Pasa cuando el dato usa una palabra del estudio que la
   situación aún no ha presentado. Los que pasaron dicen el dato con palabras que se entienden solas («sonreír a
   propósito», «los perros tienen un jadeo especial», «las ratas chillan tan agudo que no las oyes»).
2. **La escena del método sigue siendo donde «me iría»**, y el arreglo que funciona es el de la semana pasada: qué
   tuvo delante la gente y qué contestó, con el objeto de la historia. Cuando el resumen no lo dice (`E17`, los
   juegos; `I23`, la tarea y el «ayudante»; `E23`, qué comparó el ordenador), cae siempre. **`D10` pasó por leer el
   texto completo** (PLOS ONE, acceso abierto): «la misma respuesta, con o sin emoji» era la frase del artículo.
3. **Fundir método y resultado en una escena para hacer la versión corta no funciona** (dos de dos cayeron por
   «¿con qué se comparaba?»). Quitar la escena del chiste o la del contraste, sí (`MDS-069`).
4. **La salvedad del cierre bloquea cuando parece desmentir el ejemplo** («eran risas de desconocidos, no la de tu
   hermana», «solo se ha visto en ratas» detrás de «tú haces lo mismo»). Pasa cuando dice lo que no se sabe sin
   negar la escena («¿Y cuánto más contento? Eso el estudio no lo dice»; «a una rata no se le pregunta»).
5. **La firma de la fuente sale en todas las lecturas** (casi todos los lectores: «no sé quién es Fulano»); va a notas.

**Variedad (C48.1):** ninguno abre en primera persona. Cierres: «Esa rata quizá se esté riendo…», «¿Y cuánto más
contento?…», «A tu amigo, quizá…», «Así que con la pelota…»: ninguno repite. **Etiqueta `chiste`:** `otro` en los
cuatro. **Escenas que repiten la anécdota** (aviso de la dirección por `MDS-066`): mirado en los cuatro.

## 4 · Demanda, actualidad y fichas

- **Demanda medida:** `demanda_bruta.json` de hoy (20:14 UTC), 25 consultas, sin avisos. Tres aprobados salen de
  preguntas medidas: «sonreír a la fuerza te hace feliz» (144 M en el top 10), «los perros se ríen» (29 M) y «las
  ratas tienen cosquillas» (6 M). `demanda.json` y `semillas_demanda.json` actualizados (salen las dos contestadas;
  entran siete preguntas de los Shorts y de las fichas nuevas).
- **Actualidad (C52):** ningún gancho. Tendencias: fútbol, una muerte, política y un programa de televisión con
  polémica electoral. Ninguno cumple C52.
- **Fuentes centrales:** `E06` (libre por C17 desde el 31/10), `E18` y `D10` (nunca centrales), `E25` (nueva).
  **Evitadas por repetición:** `F10` (central en `MDS-038`, 14/10: libre el 25/11), `F15` (`MDS-055`), `F19`
  (`MDS-050`), `E03` (`MDS-057`), `I08` (`MDS-067`). `F14` no se reintenta (tres semanas en la reserva).
- **Corpus (paso 7): doce fichas nuevas**, todas con título y DOI vistos juntos en OpenAlex, la frase del resumen
  copiada **y, por primera vez, una línea de método en `por_que`** («Metodo: …»), como pedía mi sugerencia del 07/11:
  `E23` (la risa de cosquillas suena distinta), `E24` (bonobos que se hacen cosquillas), `E25` (el jadeo de juego de
  los perros), `E26` (orangutanes que copian la cara de juego), `F21` (la reacción a las cosquillas y el truco de
  hacértelas tú), `F22` (el hipotálamo y la risa de cosquillas), `F23` (ratas con cosquillas, más optimistas),
  `F24` (ratas que asocian un olor con las cosquillas), `F25` (ruborizarse en el karaoke), `D15` (quien se ruboriza
  cae mejor), `I23` (tardar en contestar en el chat), `I24` (el emoji que no pega con el texto). Lo hizo un subagente
  con el encargo y las reglas de la ficha; **comprobé yo de nuevo en OpenAlex el título y el DOI de las cuatro que
  he usado o intentado** (`E23`, `E25`, `F21`, `I23`). `validar_bibliografia.py`: pasa. Nada útil encontrado para la
  risa nerviosa, llorar de risa, el «visto» o los audios.
- **`MDS-108` y `MDS-110` en la noche** (referencias de trabajo) no ocupan número: se renumeró al cerrar.

## 5 · Revisiones

- **`revisiones/MDS-064.md`** (09/11): `MDS-064` se publicó el 11/11; no se rehace (C54). No la retiro para que la
  dirección la vea; la lección (no anunciar una explicación que el estudio no da) está aplicada a los cuatro nuevos.
- **`MDS-062.md` y `MDS-063.md`**: igual que el 05 y el 07/11 (no se aplican; siguen ahí).

## 6 · Lo que he tocado

`05_calendario/guiones/MDS-068` a `071.es.json`, `05_calendario/publicaciones/MDS-068` a `071.es.json`,
`05_calendario/parrilla.json` (cuatro emisiones nuevas y `_cambio_12_noviembre_noche`), `05_calendario/CALENDARIO.md`
(la semana del 16 y una corrección de la del 9), `05_calendario/temas_en_reserva.md` (once líneas nuevas y dos
que salen), `05_calendario/demanda.json`, `05_calendario/semillas_demanda.json`,
`01_bibliografia/data/semillas.json` y `BIBLIOGRAFIA_CURADA.md` (regenerado), esta bitácora y
`08_comunicacion/2026-11/2026-11-12-planificacion.md`.

---

## Para el codirector

1. **Tres días sin Short la semana que viene: jueves 19, sábado 21 y domingo 22** (y el domingo 15 sigue vacío).
   Esta noche se intentaron catorce temas y pasaron cuatro. La tasa sigue en torno a uno de cada cuatro.
2. **El reintento del viernes y el sábado no va a llenar esos huecos**: el paso 0 dice que si el lunes tiene
   emisión, termina. Si se quiere que el reintento llene días vacíos (como hizo el sábado 7), hace falta decirlo
   en el prompt.
3. **El 15/11 se decide si el canal sigue (C26).** Si se decide que no, estos cuatro guiones se quedan escritos y no
   hace falta tocar nada más que la parrilla. Si sigue, lo que más ha movido el canal en cuatro semanas son las
   cosquillas (913, 695, 428); esta semana va una (`MDS-068`) y otra de lado (`MDS-071`, perros y cosquillas).
4. **Las ramas `claude/entrega-direccion-20261112-1323` y `claude/entrega-revision-20261104-1031`** siguen vivas; no
   son mías y no las toco.

## Sugerencias a la dirección

- **`H-dato-con-palabras-de-la-situacion`** (brazo B): la escena 1 dice el hallazgo **sin ninguna palabra que solo
  presente el estudio** (ni «una molestia», ni «remitentes», ni «facilidad»). Regla afectada: la receta B. Se mediría
  con la tasa de aprobados y con «me iría en la 1» en la lectura en frío.
- **`H-texto-completo`**: cuando el artículo es de acceso abierto, leer el método en el texto completo antes de
  escribir la escena 4 (como `D10` esta semana). Regla afectada: la del 15/09, ampliada al método.
- **Versión corta**: en `ciclos.json`, decir que la escena que se quita es **una escena entera** y nunca la fusión de
  dos (fundir método y resultado cayó dos veces de dos).

## Lo que falta

- **Cuatro días vacíos** (15, 19, 21 y 22/11). **Banco vacío.**
- **Familia `mensajes`: uno** esta semana (`MDS-070`); la regla pide dos (cayeron `I22` e `I23`).
- **El largo `MDH-008`** no lo he tocado: es de la dirección y no se estrena antes del 22/11.
