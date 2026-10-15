**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación de la semana del 19 al 25 de octubre de 2026

Escrita la noche del **jueves 15 de octubre** (el contenedor arrancó a las 22:08 UTC, las 00:08 de
España del viernes, que para el paso 0 cuenta como jueves). No hacía falta comprobar si la semana
estaba hecha. **Segunda semana del bucle (C60): siete Shorts, ciclo B1, posiciones 8 a 14.**

```
$ git log --oneline -5 origin/main
1973c08 registro: sincronizado con YouTube 2026-10-15
df3734a Visuales (C50): manifiestos y hojas de contactos
a6f9e40 métricas 2026-10-15 (diaria)
45c4a76 medición de demanda 2026-10-15
de020a2 dirección 2026-10-15: nota corregida (rama vieja)

$ git ls-remote origin 'refs/heads/claude/entrega-*'
9728d4d…  refs/heads/claude/entrega-direccion-20261008-1338
```

Ninguna entrega de planificación pendiente (la que hay es de la dirección, inofensiva según su nota
del 15/10).

Leído antes de empezar: `planificacion-jueves.md` entero (mandan los bloques del 15/10, 05/10 y
08/10), `REGLAS_DE_PRODUCCION.md`, `bucle/ciclos.json` y `bucle/resultados.json`, `guionista_corto.md`
entero, `08_comunicacion/` de los últimos siete días (`novedades.md`: siguen los cambios visuales con
imagen generada; no cambia nada de lo que escribo. La dirección del 15/10: solo las carpetas por mes;
los largos vuelven el 8/11 pero no escribo ninguno), mi bitácora del 08/10 y las notas de
`revisiones/` de `MDS-038` y `MDS-039`.

---

## 0 · El bucle (C60): el marcador antes de empezar

`05_calendario/bucle/resultados.json` (actualizado el 15/10 a las 17:54 UTC):

| Brazo | n | Se quedaron viendo (media) | % visto | Vistas 48 h (mediana) |
|---|---|---|---|---|
| control | 0 | — | — | — |
| A | 0 | — | — | — |
| B | 1 (`MDS-036`) | 15,6 % | 35,4 % | 321 |

**Veredictos A y B: «faltan datos».** Referencia anterior (`MDS-026` a `MDS-035`, n = 10): se quedaron
34,2 %, visto 57,5 %, mediana 62. Pendientes: `MDS-037` a `MDS-041` sin «se quedaron» a 48 h todavía;
`MDS-042` sin ficha. No decido nada con esto: lo dice la regla.

**Asignación.** Siete guiones llevan ya `"ciclo": "B1"` (`MDS-036` a `MDS-042`), así que se sigue en
la posición 8. Primero elegí y ordené los siete temas (apartado 2); después apliqué el orden:

| Posición | Día | Short | Brazo |
|---|---|---|---|
| 8 | Lun 19 | `MDS-043` | **B** |
| 9 | Mar 20 | `MDS-044` | control |
| 10 | Mié 21 | `MDS-045` | **B** |
| 11 | Jue 22 | `MDS-046` | **A** |
| 12 | Vie 23 | `MDS-047` | control |
| 13 | Sáb 24 | `MDS-048` | **A** |
| 14 | Dom 25 | `MDS-049` | **B** |

`MDS-049` es el último Short del ciclo B1 (termina el 25/10). Al final: control 4, A 5, B 5.

- **B** (`043`, `045`, `049`): la escena 1 es el hallazgo dicho como hecho, en 11, 10 y 9 palabras,
  con su `fuente`, y la pantalla dice lo mismo. En `043` la escena 1 es una `comparacion` (risa |
  bostezo): el dato son dos mitades y así se lee de un golpe.
- **A** (`046`, `048`): las escenas 4 y 5 (qué midieron y qué encontraron) llevan `animar: true` y una
  línea `animacion`, ninguna en la última escena, sin caras humanas.
- **Dos sustituciones en su hueco, no reasignaciones** (ver 6): `MDS-043` y `MDS-047` cambiaron de
  tema porque el primero no pasó la lectura en frío; el brazo es el del hueco, no lo elegí yo.

---

## 1 · Lo que ha hecho el canal (C46)

`metricas.json` es del **13/10** (`control_c26` de ese día); `metricas_diarias.json`, del 15/10.

### Los últimos veinte Shorts, `vistas_48h`

| ID | Tema en cuatro palabras | `vistas_48h` |
|---|---|---|
| MDS-017 | cosquillas y ratas (resubida) | 0 |
| MDS-018 | profesor gracioso enseña mejor | 113 |
| MDS-019 | anuncios graciosos venden más | 137 |
| MDS-020 | la IA haciendo chistes | 37 |
| MDS-021 | personalidad de los cómicos | 122 |
| **MDS-022** | **chiste, la segunda vez** | **244** |
| MDS-023 | reírse y salud (resubida) | 2 |
| MDS-024 | conversación sin quedarse blanco | 4 |
| MDS-025 | humor y memoria | 66 |
| MDS-026 | curso de improvisación | 62 |
| MDS-027 | no pillar los chistes | 62 |
| MDS-028 | aprender a ser gracioso | 5 |
| MDS-029 | la IA pilla chistes | 14 |
| MDS-030 | humor absurdo | 156 |
| MDS-031 | cerebro cuando te ríes | 171 |
| MDS-032 | risa de amigos | 17 |
| MDS-033 | anécdota que deja de hacer gracia | 1 |
| MDS-034 | reírse cuando te lo piden | 100 |
| MDS-035 | tres cosas graciosas al día | 106 |
| **MDS-036** | **risas grabadas** | **321** |

`MDS-037` a `MDS-039`: 0 en la diaria del 15/10 (aún sin lectura a 48 h).

- **Mejores de las últimas cuatro semanas** (desde el 17/09): `MDS-036` (321) y `MDS-022` (244).
  Detrás, `MDS-031` (171) y `MDS-030` (156).
- **Peores:** `MDS-017` (0) y `MDS-023` (2), resubidas (C54, no cuentan); después `MDS-033` (1) y
  `MDS-024` (4).
- **`control_c26`** (13/10): mediana **64,0** · n 20 · sobre 100: **8** · sobre 50: **12**. **La
  mediana ha pasado de 50** (era 35 el 06/10): según el paso 3, esa es la condición para que vuelva
  el largo. La dirección ya lo ha decidido (uno a la semana desde el 8/11, `LARGOS_2026-10.md`) y me
  dice que todavía no escriba ninguno: no lo escribo.

**Derecho de tanteo: ejercido en `MDS-043`**, para `MDS-036`: las risas de los demás, ahora cómo se
pegan y cuándo se gastan (`E12`). `MDS-022` tuvo el suyo en `MDS-033` (7/10), que hizo 1 vista a 48 h;
no sé por qué (no lo dice ninguna nota) y no lo cuento como tema hundido todavía.

**Temas hundidos que no repito:** `MDS-024` (conversación), `MDS-028` (aprender a ser gracioso),
`MDS-029` (IA), `MDS-032` (risa de amigos) y `MDS-033` (la anécdota con distancia). Por eso aplazo
«cómo distinguir una risa falsa» (5,1 M), aunque tengo `E11` y `F13`: es el terreno de `MDS-032` y
`MDS-034`, de hace dos semanas.

---

## 2 · La demanda medida y lo que he decidido con ella

`demanda_bruta.json` del **2026-10-15T17:14:14Z**, veinticuatro consultas, `avisos` vacío. El juicio
está en `demanda.json`.

| Día | Short | Pregunta | Top 10 | Ficha |
|---|---|---|---|---|
| Lun 19 | `MDS-043` | ¿Se pega más una risa o un bostezo? | 37.739.550 («por qué se nos pega la risa de otro») | `E12` |
| Mar 20 | `MDS-044` | ¿Qué significa el emoji de la sonrisa? *(mensajes)* | 4.221.071 | `I09` |
| Mié 21 | `MDS-045` | ¿Por qué todos se ríen de los chistes del jefe? | 285 M, pero 0 de 5 en tema | `D12` |
| Jue 22 | `MDS-046` | ¿Qué pasa si te aguantas la risa? | sin número propio (cerca: «risa floja», 41 M, 0 de 5) | `F12` |
| Vie 23 | `MDS-047` | ¿Por qué dan miedo los payasos? *(Halloween)* | sin número propio («chistes de halloween», 16,4 M) | `J07` |
| Sáb 24 | `MDS-048` | ¿Por qué discutir por WhatsApp sale peor? *(mensajes)* | 529.433 («mensajes de texto se malinterpretan») | `I11` |
| Dom 25 | `MDS-049` | ¿Por qué después de reírte cuentas de más? | sin número propio | `D13` |

**Por qué este orden** (antes de mirar los brazos): el de más volumen el lunes; las dos de «mensajes»
separadas (martes y sábado); el jefe y la videollamada (trabajo) no seguidos del todo, y la cena de
compañeros el domingo. Los dos sustitutos ocuparon el hueco de los que cayeron.

**Familia `mensajes` (R-TE-03): sí, dos**, con ficha real: `I09` (el emoji según la edad, que ya
estaba) e `I11` (la voz frente al texto, nueva). Para la semana del 26 quedan `I08` (emoticonos y
sarcasmo: responde justo la pregunta con la que cerró `MDS-040`), `I10` (llamar o escribir) y `D10`.

**Etiqueta `chiste`:** las siete son `otro`. El ex-preso (`045`) es un juego de palabras, no un dicho
tomado al pie de la letra que escala; no he forzado ninguno.

### Actualidad (C52): un gancho

**Halloween (sábado 31/10), en `MDS-047`**, por calendario: el disfraz de payaso de un compañero en la
fiesta de la oficina, y la ficha `J07` explica de dónde sale el miedo a los payasos. Va en
`gancho_actualidad` del guion y en la nota de la parrilla. Descartados:

1. **El cambio de hora del domingo 25** («chistes del cambio de hora», 2,2 M): sigue sin una ficha que
   explique un mecanismo.
2. **Las tendencias de Google y lo más leído de la Wikipedia**: fútbol, un fallecimiento, un
   empresario, política. Nada utilizable (regla 1 y C52).
3. **«chistes de halloween» como chiste**: un recopilatorio no es un Short nuestro; el gancho entra
   por el payaso.

---

## 3 · Qué se ha escrito

Siete Shorts, `MDS-043` a `MDS-049`, con `historia`, `lectura_en_frio` con `veredicto: "pasa"`,
`visual` en cada escena, `ciclo`, `variante`, `familia_tema` y `chiste`, y sus siete publicaciones con
título de 31 a 47 caracteres y `pregunta_al_espectador`. **`validar_guion.py`: cero errores y cero
avisos en los siete**, salvo el aviso de referencia de la duración de la serie (48-54 s; ver
«Sugerencias»).

Por cada uno, la tesis y lo que contestó el lector que lo aprobó a «¿de qué va?»:

- **`MDS-043` (B)** · Tesis: la risa se pega sobre todo al oírla y el bostezo al verlo; la risa se gasta
  y el bostezo no. · Lector: «la risa se te pega más cuando la oyes y el bostezo cuando lo ves, y la
  risa contagiada se va gastando y el bostezo no».
- **`MDS-044` (control)** · Tesis: la carita sonriente no significa lo mismo según la edad. · Lector:
  «los jóvenes y los mayores no entienden igual la carita sonriente, y por eso el ‹qué bien› de tu
  madre te sienta mal aunque ella no lo diga con mala intención».
- **`MDS-045` (B)** · Tesis: nos reímos más de los chistes de quien decide sobre nuestro dinero. ·
  Lector: «nos reímos más de los chistes de quien manda sobre nuestro dinero, aunque el chiste sea el
  mismo».
- **`MDS-046` (A)** · Tesis: quien se aguanta la risa dice que le ha hecho menos gracia. · Lector: «si
  te aguantas la risa, luego la cosa te parece menos graciosa».
- **`MDS-047` (control)** · Tesis: los payasos dan miedo por no saber si quieren hacer daño ni qué van a
  hacer, y por su cara; casi nunca por un mal recuerdo. · Lector: «por qué a la gente le dan miedo los
  payasos» y, en la respuesta, «casi nunca viene de algo malo que te pasara».
- **`MDS-048` (A)** · Tesis: oídas, las palabras de quien no piensa como tú le hacen parecer más
  sensato que leídas. · Lector: «si oyes la voz de alguien que no piensa como tú, te parece más sensato
  que si lees lo mismo por escrito».
- **`MDS-049` (B)** · Tesis: después de reírse, la gente cuenta cosas más íntimas y no se da cuenta. ·
  Lector: «después de reírte con alguien, le cuentas cosas más personales sin darte cuenta».

### Variedad (C48.1)

- **Aperturas:** ninguna en primera persona. «La risa se pega más al oírla…» / «Le escribes a tu
  madre…» / «Te ríes más de los chistes…» / «Videollamada de trabajo…» / «Fiesta de Halloween…» /
  «Grupo de la familia…» / «Después de reírte…».
- **Cierres**, en columna: «Por eso en el tren…» / «Así que tu madre…» / «El chiste del ex-preso no
  mejoró…» / «Así que aguantándote…» / «Sin la pintura, Andrés…» / «Con tu tío, la próxima vez…» /
  «Lo de las palomas…». Dos empiezan por «Así que» (`044` y `046`, a dos días): el validador no avisa
  y lo que sigue es distinto, pero lo apunto. Los límites van cada uno con su fórmula: «Lo que no se
  midió», «Aunque en el estudio», «La letra pequeña», «La pega», «Aunque ojo», «Eso sí», «Ojo».
- **Series:** dos «Ríete primero», tres «El experimento», dos «Esto no tiene gracia y esto sí».

---

## 4 · Las fichas: usadas y evitadas

**Las siete fuentes centrales son fichas que nunca habían sido centrales** (C17 sin excepción): `E12`,
`I09`, `D12`, `F12`, `J07`, `I11`, `D13`. Cada guion lleva en `notas_humor` las frases del resumen
copiadas literal.

**Evitadas a propósito:** `E07` (la de `MDS-036`: el tanteo va con `E12`); `I05` e `I07` (ironía, en
ventana); `D07` (amigos y risa, `MDS-032`); `E11` y `F13` (risa falsa: tema reciente); `B03` (caído dos
veces); `K01`, `K04` (la IA descansa).

**Usadas y retiradas esta noche:** `E09` (Warren y otros, 2006) y `D06` (Dunbar y otros, 2012) fueron
las fuentes de los dos guiones que cayeron a la tercera lectura (ver 6). Siguen libres y nunca
centrales. `validar_guion.py` avisaba (C17) de que `D06` salía en una escena de `MDS-015`: era un apoyo
de pasada.

---

## 5 · El corpus (paso 7): doce fichas nuevas y una verificada

**La red sigue llegando** a `api.crossref.org` y Europe PMC. **OpenAlex, 429** otra vez (sin
presupuesto desde esta IP). `jneurosci.org` da 403 y `pmc.ncbi.nlm.nih.gov` devuelve un captcha: no he
podido leer textos completos, solo resúmenes.

**Doce fichas nuevas en `semillas.json`** (regenerado el `.md`; `validar_bibliografia.py`: «los dos
ficheros dicen lo mismo»), todas con título y DOI vistos juntos en el registro de Crossref **y** en
Europe PMC, y las frases del resumen copiadas en `resumen_verificado`:

| Ficha | Trabajo | Para qué |
|---|---|---|
| `E09` | Warren y otros, 2006 · oír alegría prepara los gestos de la cara | risa contagiosa (cerebro) |
| `E10` | Manninen y otros, 2017 · la risa con amigos libera opioides | risa en grupo |
| `E11` | Bryant y otros, 2018 · risa espontánea y fingida en 21 sociedades | risa falsa |
| `E12` | De Weck y otros, 2022 · la risa se pega al oírla, el bostezo al verlo | `MDS-043` |
| `D12` | Stillman, Baumeister y DeWall, 2007 · el poder y la risa | `MDS-045` |
| `D13` | Gray, Parkinson y Dunbar, 2015 · reírse y contar de más | `MDS-049` |
| `I10` | Kumar y Epley, 2021 · llamar une más que escribir | *mensajes* |
| `I11` | Schroeder, Kardas y Epley, 2017 · la voz humaniza | `MDS-048` |
| `F11` | Fridlund y Loftis, 1990 · cosquillas y risa | apoyo |
| `F12` | Gross y Levenson, 1997 · esconder lo que sientes | `MDS-046` |
| `F13` | McGettigan y otros, 2015 · el cerebro ante la risa de compromiso | risa falsa |
| `J07` | Tyson y otros, 2023 · el miedo a los payasos | `MDS-047` |

Y **`D06`** (Dunbar y otros, 2012), que llevaba «por verificar automáticamente» desde agosto, tiene ya
autores completos, revista y `resumen_verificado`.

**Recuento de libres con hallazgo y nunca centrales, después de esta semana:** `E09`, `E10`, `E11`,
`F11`, `F13`, `I08`, `I10`, `D10`, `D06`, `H04`, `F03`, y por la regla de seis semanas las de agosto y
primeros de septiembre. Da para la semana del 26; habrá que volver a añadir diez.

---

## 6 · La lectura en frío: veinticuatro lectores, dos temas caídos

Encargo literal, subagente nuevo en cada vuelta, sin avisarle de nada.

| Short | Vueltas | Qué cambió |
|---|---|---|
| `MDS-043` (1.º, `E09`, risa contagiosa) | 3 · **no pasa** | «Sola», «responder», «¿Y la risa entera?»; luego «se adelantó al chiste» (no había chiste) y, en la tercera, «lo que mueve tu cara» y «el escáner vio la cara» (miraba el cerebro). El hallazgo era de escáner y la historia de una carcajada: no casaban. **Tema cambiado.** |
| `MDS-043` (2.º, `E12`, risa y bostezo) | 2 | «Sobre todo en sonrisa», «no tiene la culpa» (¿de qué?) y «¿un bostezo oído no se pega?» → «se pega **más** al oírla / **más** al verlo» y el cierre vuelve al tren. |
| `MDS-044` | 2 | El «al revés» sin decir de qué, y un límite (las caritas «sencillas») que hacía dudar de la de la madre → el límite es ahora lo que de verdad no se midió: qué quería decir quien la manda. |
| `MDS-045` | 3 | El rótulo «El becario: cubiertos»; el cierre en pregunta («¿Y con un sueldo?») y «premio de laboratorio»; el entrevistador que salía de golpe. |
| `MDS-046` | 2 | «Su cuerpo se ponía en alerta» (¿qué es?) y un cierre que chocaba con la historia: fuera la frase del cuerpo. |
| `MDS-047` (1.º, `D06`, risa y dolor) | 3 · **no pasa** | «¿Te ayudaron tus amigos?» (¿a levantarse?), el rótulo que daba el resultado antes de tiempo y, en la tercera, si se comparaba a la misma gente antes y después o a dos grupos, y quién «ponía» el dolor. **Tema cambiado.** |
| `MDS-047` (2.º, `J07`, payasos) | 2 | «Y su cara» suelto, «le sobraba la cara pintada», «no cuánta lo tiene». |
| `MDS-048` | 2 | Por qué se iba la tía y no el tío; «más persona»; «Lo malo:». |
| `MDS-049` | 2 | «Lo notaban los que lo leían; ellos, no» y un cierre que repetía la escena 4. |

**Criterio (C48.2):** lo que el lector dice haber entendido «releyendo» o «tardando un segundo» va a
`notas`; lo que no supo interpretar, bloquea. Los dos que cayeron tenían, a la tercera, frases que el
lector no sabía interpretar, no solo dudas.

**Lo que se repite en las veinticuatro lecturas, para quien escriba la semana que viene:**

1. **La escena 4 («Unos psicólogos…») es donde se irían**, en casi todas: «suena a clase». Lo que
   menos lo nota es cuando la escena del estudio usa la misma palabra de la situación (el
   entrevistador y el dinero, la cara grabada y el tren).
2. **El límite al final se oye como letra pequeña que «rebaja» lo anterior**, aunque se entienda.
   Funciona mejor cuando dice algo concreto que **no** se midió y que el espectador ya tenía en la
   cabeza (qué quería decir tu madre; un tren lleno) que cuando dice cómo se hizo el estudio.
3. **Las preguntas en pantalla o en voz al final** («¿Y con un sueldo?», «¿Y en el pádel?») se leen
   como preguntas sin contestar. Mejor en afirmativo.
4. **El brazo B vuelve a tener el coste que se vio el 08/10:** «la primera frase ya me había dado la
   respuesta» (`MDS-043`). No lo toco: es lo que mide el ciclo.

---

## 7 · Revisiones

- **`revisiones/MDS-038.md` y `MDS-039.md`:** son de Shorts ya producidos (14 y 15/10). No hay nada
  que aplicar a esos guiones (C54), pero las dos sugerencias se han aplicado a los siete de esta
  semana: **menos nombre propio en la escena del estudio** («unos psicólogos», «unos neurocientíficos»,
  y el nombre solo en la fuente de pantalla) y decir qué se comparaba. **Retiro las dos notas** a
  `revisiones/_aplicadas/` con la fecha.
- La nota de la revisión diaria del 15/10 sobre `MDS-040` (la escena 6 del emoji desinfla el cierre)
  es opcional y el Short sale mañana: no lo toco. La pregunta del emoji tiene su Short propio la
  semana que viene (`I08`).
- No hay `revisiones/bibliografia.md`.

---

## Para el codirector

1. **OpenAlex sigue sin presupuesto** desde esta IP (429). Una clave gratuita en el entorno
   (`api_key`) daría a esta tarea su propia cuota. Crossref y Europe PMC han bastado otra semana.
2. **La mediana de `control_c26` ha pasado de 50 (64,0 el 13/10)**: es la condición que el paso 3 de
   mi prompt pone para que vuelva el largo. Ya está decidido por la dirección; lo apunto solo para que
   el paso 3 del prompt se actualice cuando llegue el guionista largo.
3. La rama `claude/entrega-direccion-20261008-1338` sigue viva (lo dice la dirección; no la toco).

## Sugerencias a la dirección

- **`H-cierre-concreto`** · Regla afectada: R-GU-07 (el cierre dice dónde falla). Propuesta: que el
  límite del cierre nombre **algo de la propia historia que el estudio no midió** (el tren lleno, lo
  que quería decir tu madre) y no el método («se hizo en un laboratorio»). Por qué: en veinticuatro
  lecturas, los límites de método se oyen como «letra pequeña que rebaja»; los de la historia, como
  final. Cómo se mediría: porcentaje visto entre dos brazos iguales salvo el cierre.
- **`H-duracion` (ya en cola)**: los siete de esta semana salen de 48 a 54 s y las lecturas no
  señalan ninguna escena que sobre de verdad (solo frases de cierre que son el límite obligatorio).
  Para bajar a 40 s habría que quitar una escena entera de situación o del estudio: es una regla que
  tiene que probarse como brazo, no algo que yo pueda hacer por mi cuenta.

## Lo que falta

- `MDS-046`, `MDS-047` y `MDS-049` entran sin número de demanda propio: se miden el jueves 22.
- La semana del 26 tiene `I08`, `I10` y `D10` para «mensajes» y Halloween cae el sábado 31.
- `MDH-008` sigue escrito, sin tocar y fuera de la parrilla.
