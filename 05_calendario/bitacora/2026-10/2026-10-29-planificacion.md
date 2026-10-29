**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación de la semana del 2 al 8 de noviembre de 2026, y el largo `MDH-008`

Escrita la noche del **jueves 29 de octubre** (el contenedor arrancó a las 22:09 UTC, las 23:09 de
España del jueves). **Última semana de B1 y primera de B2. Seis Shorts, no siete: el viernes 6/11 se
queda sin emisión** (apartado 6). Primera semana con el criterio nuevo de la lectura en frío (29/10).

```
$ git log --oneline -5 origin/main
9d92748 registro: sincronizado con YouTube 2026-10-29
0d42634 Visuales (C50): manifiestos y hojas de contactos
0558eac métricas 2026-10-29 (diaria)
8e331b8 medición de demanda 2026-10-29
9a357b5 métricas 2026-10-29 (diaria)

$ git ls-remote origin 'refs/heads/claude/entrega-*'
(nada)
```

Leído antes de empezar: `planificacion-jueves.md` entero (mandan los bloques del 29/10, 23/10, 22/10,
19/10, 15/10 y 05/10), `guionista_corto.md` entero (con la precisión del 29/10), `guionista.md` (bloque
del 22/10), `REGLAS_DE_PRODUCCION.md`, `bucle/ciclos.json` y `resultados.json`, `compromisos.json`,
`PLAN_DE_CAMBIOS.md` versiones 23 a 27, `08_comunicacion/` de los últimos siete días (`novedades.md`:
siguen los cambios visuales, nada para mí; la dirección del 29/10: el criterio nuevo y `MDH-008` hoy,
estreno el 15/11; los plazos de la revisión: `MDH-008-guion` vence hoy), mi bitácora del 22/10 con la
respuesta del codirector, y `revisiones/`.

---

## 0 · El bucle (C60): el marcador antes de empezar

`05_calendario/bucle/resultados.json` (leído el 29/10):

| Brazo | n | Se quedaron (media) | % visto | Vistas 48 h (mediana) | Ceros de feed |
|---|---|---|---|---|---|
| control | 5 (`037`, `041`, `044`, `047`, `050`) | 16,6 % | 74,2 % | 112 | 0 |
| A | 6 (`038`, `039`, `042`, `046`, `048`, `051`) | 29,6 % | 76,7 % | 15,5 | 3 |
| B | 5 (`036`, `040`, `043`, `045`, `049`) | 36,9 % | 160,0 % | 27 | 1 |

**Veredictos: B «GANA»** (+20,3 pp, prob. 0,94; decidido el 26/10 en `ciclos.json`). **A «sigue
midiendo»** (+13,0 pp, prob. 0,97, con n = 6; el reparo de los ceros de feed, 3 frente a 0, es lo que lo
frena). Pendientes: `MDS-052` a `056`. No decido nada: lo dice la regla.

**Asignación.** Veintiún guiones llevan `"ciclo": "B1"` (`MDS-036` a `056`), así que se sigue en la 22.
Elegí y ordené los temas antes de mirar el brazo:

| Posición | Día | Short | Brazo |
|---|---|---|---|
| 22 | Lun 2 | `MDS-057` | **B** |
| 23 | Mar 3 | `MDS-058` | control |
| 24 | Mié 4 | `MDS-059` | **A** (escenas 4 y 5 con `animar`) |
| — | Jue 5 | `MDS-060` | **B2**, receta B |
| — | Vie 6 | — | **sin emisión** |
| — | Sáb 7 | `MDS-062` | **B2**, receta B |
| — | Dom 8 | `MDS-063` | **B2**, receta B |

**B1 se cierra el miércoles 4** (el `orden` tiene 24). **Del 5 en adelante, B2**, que la dirección
escribe el lunes 2. Lo único decidido ya es que **su control es B** («decisiones», 26/10), así que los
cuatro van escritos con la receta B y etiquetados `"ciclo": "B2", "variante": "control"`. Si B2 es el
factorial 2×2 con un brazo corto, cada guion dice en `notas_humor` qué escena se quitaría (la 3 en los
cuatro). **No lo he elegido yo**: si la dirección asigna otros brazos, que cambie la etiqueta o me lo
diga y lo reescribo el jueves 5.

---

## 1 · Lo que ha hecho el canal (C46)

`metricas.json` del 27/10 y `metricas_diarias.json` del 29/10 (para `MDS-044` a `051`).

### Los últimos veinte Shorts con `vistas_48h`

| ID | Tema | `vistas_48h` | Se quedaron |
|---|---|---|---|
| MDS-032 | risa de amigos | 17 | 11,8 % |
| MDS-033 | anécdota que deja de hacer gracia | 1 | — |
| MDS-034 | reírse cuando te lo piden | 99 | 30,3 % |
| MDS-035 | tres cosas graciosas | 106 | 22,6 % |
| MDS-036 | risas grabadas | 392 | 15,8 % |
| MDS-037 | «vale.» con punto | 20 | 10,0 % |
| **MDS-038** | **no hacerte cosquillas** | **933** | 20,6 % |
| MDS-039 | caer bien a un desconocido | 22 | 50,0 % |
| MDS-040 | ironía por escrito | 9 | 22,2 % |
| MDS-041 | vergüenza ajena | 191 | 6,8 % |
| MDS-042 | risa en un funeral | 9 | 33,3 % |
| MDS-043 | risa o bostezo | 27 | 40,7 % |
| MDS-044 | emoji de la sonrisa | 112 | 13,4 % |
| MDS-045 | chistes del jefe | 10 | 80,0 % |
| MDS-046 | aguantarse la risa | 4 | 25,0 % |
| MDS-047 | miedo a los payasos | 35 | 37,1 % |
| MDS-048 | discutir por WhatsApp | 5 | 20,0 % |
| MDS-049 | contar de más tras reírte | 70 | 25,7 % |
| **MDS-050** | **reírte antes de las cosquillas** | **916** | 15,8 % |
| MDS-051 | el «jajaja» sin reírte | 28 | 28,6 % |

- **Los dos mejores de las últimas cuatro semanas: `MDS-038` (933) y `MDS-050` (916), las dos de
  cosquillas.** El tanteo del 22/10 funcionó: la continuación sacó casi lo mismo que el original.
- **Los peores:** `MDS-046` (4), `MDS-048` (5), `MDS-040` y `MDS-042` (9), `MDS-045` (10).
- **`control_c26`** (27/10): mediana **24,5** · n 20 · sobre 100: **7** · sobre 50: **8**. Con la tabla de
  arriba sale **27,5**. Lejos de 50; el 15/11 es el punto de control.

**Derecho de tanteo: ejercido en `MDS-057`** (los gorilas y las cosquillas, `E03`). Es el tercer tema de
cosquillas que intenté para el lunes: la risa floja (`F14`) y las ratas (`F16`) cayeron (apartado 6).
Además el largo entero es de cosquillas, y `MDS-055` (la máquina) sale el sábado 31.

**Temas hundidos que no repito** (seis semanas): la ironía y los emojis de ironía (`MDS-040`), el
«vale.» (`MDS-037`), discutir por WhatsApp (`MDS-048`), aguantarse la risa (`MDS-046`), los chistes del
jefe (`MDS-045`), la risa de amigos que se nota (`MDS-032`, hasta el 17/11: por eso no `E17`), la IA y
el humor (`MDS-029`), el jajaja (`MDS-051`).

---

## 2 · La demanda medida y lo que he decidido con ella

`demanda_bruta.json` del **2026-10-29T18:34:56Z**, veinticuatro consultas, `avisos` vacío. Juicio en
`demanda.json`. Como la semana pasada, las sumas del top 10 casi nunca miden respuestas (los cinco
primeros son sketches, canciones o retos); sirven para ver huecos.

| Día | Short | Pregunta | Top 10 | Ficha |
|---|---|---|---|---|
| Lun 2 | `MDS-057` | ¿Los gorilas tienen cosquillas? | sin número propio (tanteo) | `E03` |
| Mar 3 | `MDS-058` | ¿Por qué duele que dejen de contestarte? *(mensajes)* | 2.690.138 («por qué me molesta que me dejen en visto», respuestas sin estudio) | `I13` |
| Mié 4 | `MDS-059` | ¿Reírse adelgaza? | sin número propio | `G10` |
| Jue 5 | `MDS-060` | ¿Queda mal un emoji en un correo de trabajo? *(mensajes)* | 6.211.003 («por qué mandar un emoji cambia el mensaje», fuera de tema) | `I15`, `I14` |
| Vie 6 | — | **sin emisión** | — | — |
| Sáb 7 | `MDS-062` | ¿Por qué casi no te ríes cuando estás solo? | 187.909.617 («por qué nos reímos en grupo», nadie responde) | `E16` |
| Dom 8 | `MDS-063` | ¿Qué le pasa a tu cerebro al reírte con amigos? | sin número propio | `E10` |

**Por qué este orden** (antes de mirar los brazos): el tanteo el lunes; las dos de «mensajes» separadas
(martes y jueves); la cena el miércoles, el trabajo el jueves; reírse en grupo y la sobremesa, en el
fin de semana, que es cuando pasa.

**Familia `mensajes` (R-TE-03): dos**, con ficha real: `I13` (el chat de tres que deja de contestarte)
e `I15`/`I14` (el emoji en el correo). **Etiqueta `chiste`:** las seis son `otro`.

**Una pregunta no la escribo como la escribe la gente, a propósito:** «por qué me molesta que me dejen
en visto» → «¿por qué duele que dejen de contestarte?». El estudio no midió el visto (SMS de 2004); el
título pregunta lo que el estudio contesta (regla 5 de la historia, precisión del 29/10).

### Actualidad (C52): ningún gancho

1. **Las tendencias de Google:** tenis, toros (una muerte), la casa real; Wikipedia: política y
   accidentes ferroviarios. Nada (regla 1 y C52).
2. **«meme 67»** (autocompletar de «meme»): un meme infantil, sin ficha que lo explique y con niños
   detrás. No.
3. **«chiste/broma de Óscar Puente»**: un político. No.

---

## 3 · Qué se ha escrito

**Seis Shorts** (`MDS-057` a `060`, `062`, `063`), con `historia`, `lectura_en_frio` con `veredicto:
"pasa"` del 29/10, `visual` en cada escena (la escena 1 con tres búsquedas y su `prompt`), `ciclo`,
`variante`, `familia_tema` y `chiste`; sus seis publicaciones (títulos de 17 a 47 caracteres,
`pregunta_al_espectador`); la parrilla; el calendario legible. **`validar_guion.py`: cero errores en los
seis.** Un aviso en todos: la duración de referencia de la serie (salen de 47,8 a 54,3 s estimados).

**El largo `MDH-008`** (apartado 8), su publicación, **trece fichas nuevas** (apartado 5),
`demanda.json`, `semillas_demanda.json`, `pendientes_de_fuente.md` y un fichero nuevo,
**`temas_en_reserva.md`** (nueve temas en espera y uno que salió).

Por cada Short, la tesis y lo que contestó el lector que lo aprobó a «¿de qué va?»:

- **`MDS-057` (B1, B)** · Tesis: las crías de los grandes simios se ríen con las cosquillas, y su risa
  se parece más a la nuestra cuanto más parientes somos: es la misma risa, heredada. · Lector: «las crías
  de gorila y de otros simios se ríen con las cosquillas igual que nosotros, porque esa risa viene de
  un antepasado común».
- **`MDS-058` (B1, control)** · Tesis: basta con que en una conversación de tres por el móvil dejen de
  escribirte para que te sientas fuera y escribas más borde. · Lector: «lo mal que sienta que te dejen
  sin contestar en un chat de grupo, y que un estudio dice que eso te pone de mal humor y te vuelve más
  borde».
- **`MDS-059` (B1, A)** · Tesis: reírse gasta algo más que estar quieto, pero 10-15 minutos al día son
  2-10 calorías. · Lector: «si reírse adelgaza de verdad: sí, pero tan poco que no compensa ni una
  croqueta».
- **`MDS-060` (B2, receta B)** · Tesis: una carita en un correo de trabajo te hace parecer más cercano
  pero menos competente. · Lector: «poner una carita en un correo de trabajo, sobre todo en el primero
  a un cliente nuevo, hace que parezcas más cercano pero menos competente».
- **`MDS-062` (B2, receta B)** · Tesis: la risa pasa casi siempre con alguien delante; reírse funciona
  como hablar. · Lector: «nos reímos casi siempre porque estamos con alguien, no tanto porque algo
  tenga gracia».
- **`MDS-063` (B2, receta B)** · Tesis: reírte con amigos te da placer y hace que tu cerebro suelte sus
  propios opioides. · Lector: «reírte con tus amigos hace que el cerebro suelte opioides, unos
  calmantes que fabrica el propio cuerpo».

### Variedad (C48.1)

- **Aperturas:** ninguna en primera persona. «Las crías de gorila…» / «Tres amigos en un chat…» /
  «Cena con amigos…» / «Un emoji en un correo…» / «Casi toda la risa del día…» / «Reírte con tus
  amigos…».
- **Cierres**, en columna: «Cuando te ríes con cosquillas…» / «Si te sale un «¿hola?» borde…» / «Gana
  la croqueta…» / «Con el cliente nuevo…» / «A esa comedia le faltaba compañía…» / «Quizá por eso
  nadie quería irse…». Los límites: «Eso sí: solo compararon esa risa», «Eso sí, el estudio usó SMS de
  2004», «Eso sí: se midió en un laboratorio», «Eso sí: era el primer correo a un desconocido», «Una
  pega del estudio», «La pega: eran doce hombres». **«Eso sí» sale en cuatro de seis**: lo dejo dicho;
  en las lecturas fue la entrada que menos dudas dio («Lo malo» y «Ojo» se leyeron como otra cosa).
- **Series:** dos «Ríete primero» y cuatro «El experimento».
- **Personaje en el cierre:** `piensa` (3), `duda` (3, donde el límite resta).

---

## 4 · Las fichas: usadas y evitadas

**Seis fuentes centrales, ninguna repetida en seis semanas** (C17): `E03` (central en `MDS-015` el
11/09: libre desde el 23/10), `I13` y `E10` (nunca centrales), `G10`, `I15` y `E16` (nuevas esta noche).

**Evitadas a propósito:** `F10` (cuarentena hasta el 25/11), `F19` y `F15` (centrales el 26 y el 31/10),
`D10` y `I08` (terreno de los emojis: ya va `MDS-060`; e ironía, hundida), `E17` (terreno de `MDS-032`),
`I16` (el resumen no dice en qué dirección va el efecto), `D14` (teoría sin cifras), `C02` (DOI
equivocado, apartado 5).

**Usadas esta noche en guiones que cayeron** (siguen libres; ver `temas_en_reserva.md`): `F14`, `F16`,
`G07`, `E15`, `E18`, `F18`, `G09`, `D08`.

---

## 5 · El corpus (paso 7): trece fichas nuevas y cuatro arregladas

**Red abierta**: Crossref, Europe PMC y **OpenAlex con clave** (`OPENALEX_API_KEY` en el entorno; no
se ha escrito en ningún sitio). Crossref devolvió **429** al final de la noche; no ha bloqueado nada.

**Trece fichas nuevas en `semillas.json`** (regenerado el `.md`; `validar_bibliografia.py`: «los dos
ficheros dicen lo mismo»), todas con título y DOI vistos juntos y la frase del resumen copiada en
`resumen_verificado`:

| Ficha | Trabajo | Para qué |
|---|---|---|
| `I14` | Glikson, Cheshin y van Kleef, 2018 · el smiley en el correo de trabajo | `MDS-060` |
| `I15` | Lai y Mayiwar, 2023 · su réplica preregistrada (847 personas) | `MDS-060` (central) |
| `I16` | Kalman y Rafaeli, 2011 · tardar en contestar un correo | libre |
| `G07` | Cogan y otros, 1987 · la risa sube el umbral de molestia, y no por distraer | cayó (reserva) |
| `G08` | Mahony y otros, 2001 · humor, relajación y expectativas | apoyo |
| `G09` | Romundstad y otros, 2016 · humor y mortalidad, 53.556 noruegos | cayó (reserva) |
| `G10` | Buchowski y otros, 2007 · lo que gasta reírse (con la fe de erratas) | `MDS-059` |
| `E15` | Stavropoulos y Alba, 2018 · las ganas de apretar a un cachorro | cayó (reserva) |
| `E16` | Provine y Fischer, 1989 · el diario de risas: casi siempre con gente | `MDS-062` |
| `E17` | Smoski y Bachorowski, 2003 · risa a la vez entre amigos | libre (tras el 17/11) |
| `E18` | Coles y otros (Many Smiles), 2022 · sonreír a propósito alegra | cayó (reserva) |
| `D14` | Flamson y Barrett, 2008 · los chistes internos | marco |

Y **arregladas**: **`E03`** tenía mal el título («The evolution of laughter…»; es «Reconstructing the
evolution of laughter in great apes and humans», *Current Biology* 19(13)) y ahora lleva resumen;
**`H04`** tenía el DOI de un artículo sobre rasgos psicopáticos en adolescentes (corregido a
10.1016/j.paid.2016.02.056; sin resumen accesible, no vale como central); **`D08`** lleva resumen.
**Sin arreglar: `C02`**, cuyo DOI (10.1037/aca0000158) es de un artículo sobre aptitud musical; el bueno
no salió esta noche (Crossref en 429). Queda en `semillas_demanda.json`.

**Probado y descartado:** Myrick, 2015 (los vídeos de gatos): existe, pero su resumen no se puede leer
desde aquí. Sin resumen no hay ficha.

---

## 6 · La lectura en frío con el criterio del 29/10: cuarenta y dos lectores, catorce temas, seis pasan

Encargo literal de `guionista_corto.md`, subagente nuevo en cada vuelta, sin avisarle de nada. **El
criterio nuevo cambia mucho las cosas**: en la semana del 22/10, con el criterio viejo, pasaron 7 de 9
temas; esta noche, **6 de 14**. Lo que bloquea ahora casi siempre es lo que antes iba a `notas`: «tuve
que releerla», «lo entendí en la escena siguiente», «¿qué es ‹eso›?».

| Hueco | Temas intentados (vueltas) | Resultado |
|---|---|---|
| Lun 2 | `F14` risa floja (3) · `F16` ratas (3) · **`E03` gorilas (3)** | pasa el tercero |
| Mar 3 | **`I13` el chat de tres (3)** | pasa |
| Mié 4 | `G07` reírse quita el dolor (3) · **`G10` reírse adelgaza (3)** | pasa el segundo |
| Jue 5 | **`I15` el emoji en el correo (3)** | pasa |
| Vie 6 | `E15` cachorro (3) · `E18` sonrisa forzada (3) · `F18` reírte con cosquillas (3) | **ninguno** |
| Sáb 7 | **`E16` reírse solo (3)** | pasa |
| Dom 8 | `G09` humor y vivir más (3) · `D08` la pareja (3) · **`E10` reírse con amigos (3)** | pasa el tercero |

**Cómo he aplicado el criterio, para que la dirección lo pueda corregir:** bloquea lo que el lector
dice no haber entendido, lo que entendió **más tarde** (en otra escena o releyendo), lo que contradice
al título y cualquier «me iría en la escena N». **No bloquea** una duda de un instante que el lector
resolvió **dentro de la misma frase** y que puede repetir con sus palabras («tardé un segundo en ver
que…», «lo entendí, pero el ‹antes› me sonó raro»): va a `notas`, copiada. Los cuatro aprobados que
tienen notas así son `MDS-058`, `MDS-060`, `MDS-062` y `MDS-057`. **Si eso es demasiado blando, esos
cuatro no pasan y la semana se queda en dos Shorts**: lo dejo dicho en «Para el codirector».

**Lo que se repite en las cuarenta y dos lecturas:**

1. **El brazo B y «me iría en la 4».** Con el dato en la escena 1, el lector llega a la escena del
   estudio sabiendo la respuesta y desliza: `MDS-060` (v2), `E18` (v1-v3), `D08` (v2-v3), `G09` (v2),
   `E16` (v1). Se arregló **dándole a la escena 4 su propia pregunta** («¿Es risa de verdad?», «¿Cómo
   se sabe?») o **algo nuevo que el dato no decía** (la mitad con carita y la mitad sin). Como B es el
   control de B2, esto va a pasar en todos los Shorts: lo propongo abajo.
2. **El cierre honesto se lee como «lo malo de mi vida».** «Lo malo», «Ojo», «La pega» y «Eso ya se
   sabía» se leyeron tres veces como si hablaran de la situación y no del estudio. «Eso sí, el estudio…»
   (con la palabra «estudio») nunca dio problemas.
3. **Lo que el resumen no dice, el lector lo pregunta.** «¿Qué presión, dónde?» (`G07`), «¿qué sitio les
   daba miedo?» (`F16`), «¿quién hacía la caricia de fuera?» (`F10`, en el largo). No se puede contestar
   sin inventar: hay que elegir fichas cuyo resumen cuente el cómo.
4. **Los pronombres y los tiempos verbales.** «Y se ríe igual» (¿quién?), «Esos científicos grababan»
   (cambio de presente a pasado), «este estudio no lo probó» (¿lo?). Media docena de bloqueos esta
   noche fueron solo eso.
5. **Las imágenes a medias de un experimento con animales** («cuando una rata se toca a sí misma»)
   piden un «cómo» que en cincuenta segundos no cabe.

---

## 7 · Revisiones

- **`revisiones/MDS-052.md`, `MDS-053.md` y `MDS-054.md`** (opcionales, de la revisión del 27, 28 y
  29/10): son de Shorts ya publicados o que salen mañana con la voz hecha. **No los aplico** (regla
  11.4 y C54) y **no los retiro**: la nota de `MDS-054` («Antes de llamar, los participantes
  esperaban…») y la de `MDS-053` me han servido esta noche (apartado 6, puntos 2 y 4).
- **`revisiones/MDH-008.md`** es del guion viejo de `MDH-008` (septiembre, «cómo se construye un
  chiste»), que ya no existe: el `MDH-008` de esta noche es otro guion. No aplica; la dejo para que la
  revisión la archive (ya hay una copia en `_aplicadas/`).
- No hay `revisiones/bibliografia.md`.

---

## 8 · El largo `MDH-008`: «¿Por qué no puedes hacerte cosquillas? El caso entero»

**Escrito y entregado hoy, como pedía `compromisos.json` (`MDH-008-guion`, 29/10).** Sustituye en
`guiones/MDH-008.es.json` al guion de septiembre, que nunca se emitió (sigue en la historia de git y en
`_emisiones_suspendidas` de la parrilla).

- **Short de partida:** `MDS-038` (`fuente_short`), con `MDS-050`, `MDS-055` y `MDS-057` alrededor.
- **8 min 34 s estimados, 45 escenas, ~1.100 palabras.** Cuatro capítulos: «Tu cerebro, aguafiestas»
  (`F10`, `F20`), «¿Hace falta otro?» (`F15`, `F19`), «Las ratas que ríen» (`E06`, `F16`, `F17`, `F18`,
  `F20`) y «¿Cosquillas o chistes?» (`F11`, `F14`). Apertura con la pregunta grande antes del segundo
  15 (dos preguntas: por qué de fuera, por qué risa), respuesta y cierre con los límites y la pregunta
  para los comentarios.
- **Diez risas** con su segundo en `notas_humor`; ningún hueco de más de 90 s. **El escéptico, tres
  veces** (escenas 9, 18 y 30). **Seis escenas con `animar`** (6, 7, 11, 20, 26 y 38).
- **C17 no se aplica** (respuesta del codirector del 22/10): por eso vuelven `F10`, `F15`, `F19` y `F14`.
  `validar_guion.py` avisa de `F10` y `F19`; es lo esperado.
- **`validar_guion.py`: cero errores.** Avisos: escenas de más de 10 s (el largo los tolera) y 64 %
  de `enunciado`.
- **Lectura en frío: tres vueltas de cinco lectores** (uno por capítulo y uno del vídeo entero), quince
  lectores. Los quince dicen «me quedo» o «seguiría viendo», y entienden de qué va. **Pero tras la
  tercera vuelta seguían quedando frases sueltas** en cada capítulo («¿quién hace la caricia de
  fuera?», «se contagia… ¿la risa o los chillidos?»). Las he corregido **sin volver a leerlas**:
  `lectura_en_frio` lo dice capítulo por capítulo («no pasa todavía: corregido tras la vuelta 3, sin
  releer»). **El guion no está cerrado:** hay margen hasta el ensayo (9/11).
- **NO lo pongo en la parrilla.** El estreno pasó al 15/11 y la imagen horizontal y la voz por tandas
  son de la dirección el 5/11. La fecha la pone la dirección.

**Historial de las vueltas del largo** (lo que dijo cada lector, en resumen):

- **Vuelta 1:** cap. 1, «a una rata tampoco le funciona tocarse», «deja de chillar» (¿quién?);
  cap. 2, «máquina creída», el salto a «no poder predecir», la pega sin sentido; cap. 3, «zona del
  tacto», «Las ratas también lo tienen», no contesta por qué dan risa; cap. 4, «antes y después», «¿qué
  amiga?», la pregunta sin sí o no; entero, «no es el mismo interruptor», «la tienen las ratas» frente
  a «hipótesis».
- **Vuelta 2:** cap. 1, la caricia «de dos maneras», «se apaga» frente a «baja el volumen»; cap. 2,
  «la máquina que creían de verdad», «se activaba antes»; cap. 3, «el hocico en un agujero», «señal de
  juego» sin puente; cap. 4, «colorados», «Pero eso era preguntar»; entero, «hasta una máquina, si crees
  que es de verdad».
- **Vuelta 3:** ver `lectura_en_frio` en el guion.

---

## Para el codirector

1. **El criterio nuevo de la lectura en frío ha costado un Short esta semana.** El viernes 6/11 se
   queda sin emisión: tres temas cayeron a la tercera vuelta y la cuarta ficha candidata tenía el DOI
   mal. Con 6 de 14 temas aprobados, **si la semana que viene son catorce Shorts (B2), harán falta
   unos treinta temas escritos para llenarlos.** Lo digo antes de que llegue, no como queja: cada
   bloqueo de esta noche era real («¿qué presión, dónde?» lo diría cualquiera en el metro).
2. **Cómo he trazado la línea** (apartado 6): una duda de un instante resuelta en la misma frase va a
   `notas`; lo que se entiende en otra escena o releyendo, bloquea. Si la dirección quiere que también
   eso bloquee, `MDS-057`, `058`, `060` y `062` no pasan. Necesito saberlo antes del jueves 5.
3. **`MDS-061` está libre para el viernes 6.** Si la dirección quiere llenarlo, el tema con más papeletas
   de la reserva es la sonrisa forzada (`E18`), con el lápiz contado en la escena 4 como la duda que el
   estudio resuelve. Yo no vuelvo a correr hasta el jueves 5 a las 22:07 UTC, después de la producción
   del viernes.
4. **B2:** he escrito del 5 al 8 con la receta B (su control) y la etiqueta `B2 / control`. Si el
   factorial pone a alguno en un brazo corto, cada guion dice qué escena se quita (la 3); la lectura en
   frío habría que repetirla.
5. **`MDH-008` no está en la parrilla** (apartado 8), y el guion necesita una lectura más.

## Sugerencias a la dirección

- **`H-escena-4-con-pregunta` (nueva, sale del brazo B):** con el dato en la escena 1, la escena del
  estudio solo funciona si abre con su propia pregunta («¿Es risa de verdad?», «¿Cómo se sabe?»). En
  esta noche, las tres escenas 4 que abrían así no tuvieron ni un «me iría»; las que empezaban por
  «Unos psicólogos…», cinco. Regla afectada: R-GU-01 (en B2, el control es B). Se mediría con «se
  quedaron» de dos brazos iguales salvo esa frase.
- **`H-cierre-concreto` (tercera semana con datos):** «Eso sí, el estudio…» con la palabra «estudio»
  dentro no se confunde con la vida del espectador; «Lo malo» y «Ojo» sí. Regla afectada: R-GU-07.
- **El femenino genérico** (`MDS-062`, «la comedia que viste sola»): un lector se sintió fuera. Lo dejo
  porque varía con los demás guiones, pero la dirección puede querer una regla.

## Lo que falta

- **El viernes 6/11** (ver «Para el codirector», 1 y 3).
- **Una cuarta lectura del largo** antes del 9/11.
- **El DOI de `C02`.**
- **Las preguntas de esta semana sin número propio** se miden el jueves 5 (`semillas_demanda.json`).

## Respuesta del codirector

