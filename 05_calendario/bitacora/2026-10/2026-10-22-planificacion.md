**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación de la semana del 26 de octubre al 1 de noviembre de 2026

Escrita la noche del **jueves 22 de octubre** (el contenedor arrancó a las 22:08 UTC, las 00:08 de
España del viernes, que para el paso 0 cuenta como jueves). **Tercera semana del bucle (C60): siete
Shorts, ciclo B1, posiciones 15 a 21.** Primera semana con la versión 23 del plan: manda el feed.

```
$ git log --oneline -5 origin/main
b283a11 registro: sincronizado con YouTube 2026-10-22
cf6780e Visuales (C50): manifiestos y hojas de contactos
9ba4abb métricas 2026-10-22 (diaria)
54c1e8d medición de demanda 2026-10-22
91e8a5d dirección 2026-10-22: brazo A recupera MDS-038/039 (bucle.py), C36 en voz.py apagado …

$ git ls-remote origin 'refs/heads/claude/entrega-*'
(nada)
```

Ninguna entrega pendiente (la rama vieja de la dirección ya no está).

Leído antes de empezar: `planificacion-jueves.md` entero (mandan los bloques del 22/10, 19/10, 15/10 y
05/10), `REGLAS_DE_PRODUCCION.md`, `bucle/ciclos.json` y `bucle/resultados.json`, `guionista_corto.md`
entero, `08_comunicacion/` de los últimos siete días (`novedades.md`: siguen los cambios visuales; no
cambia nada de lo que escribo. La dirección del 22/10: feed primero, escena 1 con el mejor plano, el
largo el jueves 29. La revisión del 22/10: editó `MDS-047` por la excepción de 48 h), mi bitácora del
15/10 y `revisiones/` (nada nuevo: ver 7).

---

## 0 · El bucle (C60): el marcador antes de empezar

`05_calendario/bucle/resultados.json` (actualizado el 22/10 a las 18:11 UTC):

| Brazo | n | Se quedaron viendo (media) | % visto | Vistas 48 h (mediana) |
|---|---|---|---|---|
| control | 2 (`037`, `041`) | 8,4 % | 102,2 % | 106 |
| A | 3 (`038`, `039`, `042`) | 34,6 % | 66,8 % | 22 |
| B | 3 (`036`, `040`, `043`) | 26,2 % | 252,3 % | 27 |

**Veredictos A y B: «faltan datos»** (el control tiene n = 2; la regla temprana pide 4). Referencia
anterior (`MDS-026` a `035`, n = 10): se quedaron 34,3 %, visto 57,3 %, mediana 62. Pendientes:
`MDS-044` a `049`. No decido nada con esto: lo dice la regla.

**Asignación.** Catorce guiones llevan ya `"ciclo": "B1"` (`MDS-036` a `049`), así que se sigue en la
posición 15. Primero elegí y ordené los siete temas (apartado 2); después apliqué el orden:

| Posición | Día | Short | Brazo |
|---|---|---|---|
| 15 | Lun 26 | `MDS-050` | control |
| 16 | Mar 27 | `MDS-051` | **A** |
| 17 | Mié 28 | `MDS-052` | **B** |
| 18 | Jue 29 | `MDS-053` | control |
| 19 | Vie 30 | `MDS-054` | **B** |
| 20 | Sáb 31 | `MDS-055` | **A** |
| 21 | Dom 1 | `MDS-056` | control |

Al final de la semana: control 7, A 7, B 7 (de 24, quedan B, control y A para el 2-4/11).

- **B** (`052`, `054`): la escena 1 es el hallazgo dicho como hecho, en 12 palabras, con su `fuente`, y
  la pantalla dice lo mismo. Ninguna tarjeta de marca en la escena 1: vídeo detrás del dato.
- **A** (`051`, `055`): las escenas 4 y 5 (qué midieron y qué encontraron) llevan `animar: true` y una
  línea `animacion`, sin caras humanas.
- **`MDS-055` es el tercer tema de su hueco** (ver 6): el brazo es el del hueco, no lo elegí yo.

---

## 1 · Lo que ha hecho el canal (C46)

`metricas.json` es del **20/10**; `metricas_diarias.json` y `resultados.json`, del 22/10 (se usan para
`MDS-036` a `043`, que la semanal aún no tenía completos).

### Los últimos veinte Shorts, `vistas_48h`

| ID | Tema en cuatro palabras | `vistas_48h` |
|---|---|---|
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
| MDS-034 | reírse cuando te lo piden | 99 |
| MDS-035 | tres cosas graciosas al día | 106 |
| MDS-036 | risas grabadas | 392 |
| MDS-037 | «vale.» con punto | 20 |
| **MDS-038** | **no hacerte cosquillas** | **933** |
| MDS-039 | caer bien a un desconocido | 22 |
| MDS-040 | ironía por escrito | 9 |
| MDS-041 | vergüenza ajena | 192 |
| MDS-042 | risa en un funeral | 9 |
| MDS-043 | risa o bostezo | 27 |

`MDS-044` a `046`: 0 en la diaria (aún sin 48 h).

- **Mejores de las últimas cuatro semanas:** `MDS-038` (933) y `MDS-036` (392). Detrás, `MDS-041`
  (192) y `MDS-031` (171).
- **Peores:** `MDS-033` (1), `MDS-024` (4), `MDS-028` (5), y `MDS-040` y `MDS-042` (9).
- **`control_c26`** (20/10): mediana **62,0** · n 20 · sobre 100: **6** · sobre 50: **11**.

**Derecho de tanteo: ejercido en `MDS-050`**, para `MDS-038`: las cosquillas, ahora por qué te ríes
antes de que te toquen (`F19`, ficha nueva; `F10` está en cuarentena hasta el 25/11). `MDS-055` sale del
mismo caso (¿puede hacerte cosquillas una máquina?). `MDS-036` tuvo el suyo la semana pasada
(`MDS-043`, 27 vistas).

**Temas hundidos que no repito:** `MDS-040` (la ironía por escrito: por eso descarto `I08`, el emoji de
la lengua, aunque estaba guardada para esta semana), `MDS-037` (el «vale.» con punto: por eso no `D10`),
`MDS-033`, `MDS-028`, `MDS-024`.

---

## 2 · La demanda medida y lo que he decidido con ella

`demanda_bruta.json` del **2026-10-22T17:26:38Z**, veinticuatro consultas, `avisos` vacío. El juicio
está en `demanda.json`.

**Cómo he elegido (versión 23): primero la situación que se reconoce sin sonido, después la ficha, y la
demanda solo ha desempatado y ordenado.** Los siete abren con algo que se ve en un segundo: un dedo que
se acerca, un móvil en el grupo, una carcajada en una cena, un proyector apagado, un teléfono que suena,
cosquillas en el sofá, la comida del domingo.

| Día | Short | Pregunta | Top 10 | Ficha |
|---|---|---|---|---|
| Lun 26 | `MDS-050` | ¿Por qué te ríes antes de las cosquillas? | sin número propio (tanteo de `MDS-038`) | `F19` |
| Mar 27 | `MDS-051` | ¿Sirve de algo escribir «jajaja» sin reírte? *(mensajes)* | sin número propio | `I12` |
| Mié 28 | `MDS-052` | ¿Se nota cuando alguien se ríe por compromiso? | 28.025.319 («se nota una risa falsa») | `E11` |
| Jue 29 | `MDS-053` | ¿Hacer un chiste en una reunión te da puntos? | sin número propio | `D01` |
| Vie 30 | `MDS-054` | ¿Por qué escribimos en vez de llamar? *(mensajes)* | 3.459.601 («por qué es mejor llamar que escribir») | `I10` |
| Sáb 31 | `MDS-055` | ¿Puede hacerte cosquillas una máquina? | sin número propio | `F15` |
| Dom 1 | `MDS-056` | ¿Por qué hay gente que se ríe de lo que cuenta? | sin número propio | `E02` |

**Por qué este orden** (antes de mirar los brazos): el tanteo el lunes; las dos de «mensajes»
separadas (martes y viernes); las dos de cosquillas en los extremos de la semana; la comida familiar el
domingo, que es cuando pasa.

**Familia `mensajes` (R-TE-03): sí, dos**, con ficha real: `I12` (la risa escrita, nueva) e `I10`
(llamar o escribir). `I13` (el visto) queda para la semana del 2/11.

**Etiqueta `chiste`:** las siete son `otro`. Ninguna escena 1 es un dicho tomado al pie de la letra.

**Cinco de las siete preguntas no tienen número propio:** van a `semillas_demanda.json` para el jueves
29. No es un descuido: con la versión 23 la situación reconocible pesa más que el volumen de búsqueda.

### Actualidad (C52): ningún gancho

Descartados:

1. **Halloween (sábado 31):** ya tuvo su gancho en `MDS-047` (los payasos); dos semanas seguidas sería
   fórmula. `Playing With Fear` (Andersen y otros, 2020) mide el disfrute del miedo, no la risa: no es
   un mecanismo del humor y no la he usado.
2. **Las tendencias de Google:** fútbol europeo, política y los premios Princesa de Asturias. Nada
   utilizable (regla 1 y C52).
3. **«chistes del cambio de hora»** (1,96 M): el cambio ya habrá pasado el lunes, y sigue sin ficha.

---

## 3 · Qué se ha escrito

Siete Shorts, `MDS-050` a `MDS-056`, con `historia`, `lectura_en_frio` con `veredicto: "pasa"`,
`visual` en cada escena (la escena 1 con tres búsquedas y su `prompt`), `ciclo`, `variante`,
`familia_tema` y `chiste`, y sus siete publicaciones con título de 37 a 47 caracteres y
`pregunta_al_espectador`. **`validar_guion.py`: cero errores en los siete.** Avisos: el de referencia
de la duración de la serie en todos (48-53 s estimados; ver «Sugerencias») y el de C17 en `MDS-053`
(ver 4).

Por cada uno, la tesis y lo que contestó el lector que lo aprobó a «¿de qué va?»:

- **`MDS-050` (control)** · Tesis: las cosquillas empiezan antes de que te toquen; el cerebro se prepara
  en la espera y cuanto más se prepara, más risa sale después. · Lector: «va de por qué te dan
  cosquillas antes de que te toquen siquiera».
- **`MDS-051` (A)** · Tesis: la risa escrita va con conversaciones más felices casi igual que la de
  verdad. · Lector: «si escribir ‹jajaja› en el chat cuenta como reírse de verdad. Según un estudio,
  casi sí».
- **`MDS-052` (B)** · Tesis: una risa fingida cuela más de lo que creemos (56-69 % de aciertos). ·
  Lector: «si la gente sabe distinguir una risa fingida de una de verdad, con el ejemplo de reírle un
  chiste malo a un amigo».
- **`MDS-053` (control)** · Tesis: un chiste que sale bien sube tu estatus porque pareces seguro y
  capaz; uno fuera de tono te hace parecer igual de seguro pero menos capaz. · Lector: «una chica nueva
  hace un chiste en su primera reunión cuando falla el proyector, y un estudio explica por qué eso hizo
  que la tomaran más en serio».
- **`MDS-054` (B)** · Tesis: escribimos porque creemos que llamar será más incómodo, y no lo es; hablar
  une más. · Lector: «que llamar a un amigo une más que escribirle y no resulta más incómodo de lo que
  crees».
- **`MDS-055` (A)** · Tesis: las cosquillas no necesitan que creas que hay una persona detrás. · Lector:
  «un experimento en el que a la gente le hacían cosquillas creyendo que era una máquina, y se reían
  igual que con una persona».
- **`MDS-056` (control)** · Tesis: reírse de lo que uno cuenta es lo normal; quien habla se ríe más que
  quien escucha, al final de las frases y muchas veces sin nada gracioso. · Lector: «por qué tu tío se
  ríe contando algo que no tiene gracia: quien cuenta algo se ríe más que quien lo escucha».

### Variedad (C48.1)

- **Aperturas:** ninguna en primera persona. «Tu hermana, en el sofá…» / «Tu amigo manda un meme…» /
  «Adivinar si una risa es fingida…» / «Primera reunión de la nueva…» / «Llamar a un amigo une más…» /
  «Tú no puedes hacerte cosquillas…» / «Comida del domingo…».
- **Cierres**, en columna: «Así que ese dedo…» / «O sea, que tu fila de jotas…» / «Con tu amigo del
  chiste malo, tranquilo…» / «A la nueva le salió bien…» / «La próxima vez que te llame…» / «Las
  cosquillas, por tanto…» / «Lo de tu tío no es raro…». Los límites, cada uno con su entrada: «Aunque
  fue», «Lo malo», «Lo único», «Fuera de tono», «Eso sí», «Ojo», «La pega». **«Eso sí» salía en cuatro
  cierres después de las lecturas:** en tres lo he cambiado por otra palabra, sin tocar el sentido, y lo
  dice cada guion.
- **Series:** dos «Ríete primero» (`050`, `051`) y cinco «El experimento». Lo pide la forma: cinco
  son un estudio con protagonista y su cifra.
- **Ningún nombre propio de investigador en la voz** («unos neurocientíficos», «unos psicólogos», «un
  psicólogo»): la firma va en la pantalla del cierre.

---

## 4 · Las fichas: usadas y evitadas

**Siete fuentes centrales, ninguna repetida en seis semanas** (C17): `F19`, `I12`, `F15` (nuevas esta
noche), `E11`, `I10` (nunca centrales), `D01` y `E02`.

- **`D01`:** nunca fue central en un Short, pero sí en el largo `MDH-006` (12/09). El validador avisa
  porque cuenta seis semanas desde hoy; el Short sale el jueves 29, a 47 días. Lo dejo.
- **`E02`** (Provine, 1993) fue central en `MDS-002` y `MDS-006` (agosto): libre por la regla de seis
  semanas. Tenía la ficha sin resumen: ahora lo lleva.

**Evitadas a propósito:** `F10` (cuarentena, `MDS-038`); `I08` y `D10` (terreno de `MDS-040` y
`MDS-037`, hundidos); `F13` (risa falsa por el cerebro: con `E11` en la misma semana era repetir);
`D06` (cayó el 15/10).

**Usadas y retiradas esta noche** (cayeron a la tercera lectura; ver 6): `E10` (la risa con amigos) y
`E14` (la sonrisa de vergüenza). Siguen libres y nunca centrales.

---

## 5 · El corpus (paso 7): once fichas nuevas y tres verificadas

**La red llega a todo:** Crossref, Europe PMC y **OpenAlex con clave** (`OPENALEX_API_KEY` está en el
entorno desde esta semana: ni un 429; la clave no se ha escrito en ningún sitio).

**Once fichas nuevas en `semillas.json`** (regenerado el `.md`; `validar_bibliografia.py`: «los dos
ficheros dicen lo mismo»), todas con título y DOI vistos juntos en Crossref y en Europe PMC u OpenAlex,
y las frases del resumen copiadas en `resumen_verificado`:

| Ficha | Trabajo | Para qué |
|---|---|---|
| `F14` | Harris y Christenfeld, 1997 · cosquillas, humor y Darwin-Hecker | largo `MDH-008` |
| `F15` | Harris y Christenfeld, 1999 · ¿puede una máquina hacer cosquillas? | `MDS-055` y el largo |
| `F16` | Ishiyama y Brecht, 2016 · las cosquillas en el cerebro de la rata | largo |
| `F17` | Kaufmann, Brecht e Ishiyama, 2022 · las cosquillas se contagian (ratas) | largo |
| `F18` | Hinchcliffe y otros, 2020 · los chillidos de la rata miden el gusto | largo |
| `F19` | Wattendorf y otros, 2019 · la espera de las cosquillas | `MDS-050` |
| `F20` | Ishiyama, Kaufmann y Brecht, 2019 · la rata tampoco puede hacerse cosquillas | largo |
| `I12` | Vlahovic, Roberts y Dunbar, 2012 · la risa escrita y la felicidad | `MDS-051` |
| `I13` | Smith y Williams, 2004 · el silencio en los mensajes excluye | *el visto* (2/11) |
| `E13` | Aragón y otros, 2015 · llorar de alegría, apretar al cachorro | apoyo |
| `E14` | Keltner, 1995 · la cara de la vergüenza no es la de la risa | apoyo |

Y **`E02`**, **`E06`** (las ratas que ríen, Panksepp y Burgdorf) y **`D01`** tienen ya
`resumen_verificado`.

**Libres con hallazgo y nunca centrales, después de esta semana:** `E09`, `E10`, `E13`, `E14`, `F11`,
`F13`, `F14`, `F16`-`F18`, `F20`, `I08`, `I13`, `D06`, `D10`, `H04`, `F03`; `E06` desde el 27/10; y las de
agosto y primeros de septiembre por la regla de seis semanas.

---

## 6 · La lectura en frío: veintitrés lectores en siete huecos, dos temas caídos

Encargo literal, subagente nuevo en cada vuelta, sin avisarle de nada.

| Short | Vueltas | Qué cambió |
|---|---|---|
| `MDS-050` | 2 | «Por eso unos neurocientíficos…» (sonaba a causa), «se ponía en marcha», la pantalla «Más espera» que decía otra cosa que la voz, y «sin tocarla» en la escena 1, que se comía el remate. |
| `MDS-051` | 3 | «¿Mentira?» sin decir de qué; el diario confuso; «los canales» (no sabía cuáles eran). |
| `MDS-052` | 3 | El dato de la escena 1 sin sujeto; «Por eso cuela»; «Lo midieron…» (¿qué?); un límite que no decía qué cambiaba. |
| `MDS-053` | 2 | «seguro» leído como «seguramente»; «Por eso a la nueva le salió bien» (al revés); el rótulo «El chiste apuesta». |
| `MDS-054` | 2 | «Esperaban…» (¿quién?), «era la voz en directo», «suene tu amigo». |
| `MDS-055` (1.º, `E10`, risa con amigos) | 3 · **no pasa** | El sábado y la película no casaban con los opioides; y a la tercera, «media hora solos en una sala: ¿haciendo qué?». El resumen no lo dice, así que no se puede aclarar sin inventar. **Tema cambiado.** |
| `MDS-055` (2.º, `E14`, vergüenza) | 3 · **no pasa** | «Te delató, ¿ante quién?»; «caras reales, sin actuar: ¿de dónde salían?». El resumen tampoco lo dice. **Tema cambiado.** |
| `MDS-055` (3.º, `F15`, la máquina) | 3 | Un cierre que metía una idea nueva; «la trampa»; y una conclusión que no se seguía (lo probado es que no hace falta *creer* que hay alguien). Pasa con una nota. |
| `MDS-056` | 2 | El «por eso» de la escena del estudio y un esquema de flechas en pantalla que no se leía. |

**Criterio (C48.2), el mismo que el 15/10:** lo que el lector dice haber entendido «releyendo» o
«tardando un segundo» va a `notas`; lo que no supo interpretar, bloquea. Los siete aprobados llevan notas de ese
tipo, copiadas en el guion. Donde el lector nombró como sobrante el
cierre honesto o el remate, se queda y lo dice `frase_que_sobra`.

**Lo que se repite en las veintitrés lecturas, para quien escriba la semana que viene:**

1. **«Por eso unos psicólogos…» falla siempre.** Cinco lectores distintos en la primera vuelta leyeron
   el «por eso» como si el estudio fuera consecuencia de la anécdota. «Para entenderlo», «para saber si
   se nota» o sin conector funcionan.
2. **La escena 4 sigue siendo donde se irían** («suena a clase»), en casi todos. Lo que menos lo nota:
   una frase corta con una cifra que se queda (1.200 risas).
3. **El límite final se oye como «bajón»** en cinco de siete. Funciona mejor si dice algo concreto que
   no se probó (una risa en directo, los audios) que si dice dónde se hizo (un laboratorio).
4. **Los diseños con grupo de control no caben en una frase.** Los dos temas caídos esta semana, y
   `D06` la pasada, cayeron por lo mismo: el lector quiere saber con qué se compara, y el resumen no lo
   cuenta. Antes de elegir una ficha, mirar si el resumen dice qué hacía el grupo de comparación.
5. **El brazo B vuelve a costar lo mismo:** «la primera frase ya me da la conclusión» (`054`, dos
   lectores). No lo toco: es lo que mide el ciclo.

---

## 7 · Revisiones

- **No hay notas nuevas en `revisiones/`** desde el 15/10. Las que hay son de Shorts y largos ya
  producidos (C54) y siguen como estaban. **`revisiones/MDH-008.md`** la leeré el jueves 29, con el largo.
- La revisión del 22/10 editó `MDS-047` (excepción de 48 h, escenas 3, 5 y 6): no lo toco.
- No hay `revisiones/bibliografia.md`.

---

## 8 · El largo `MDH-008` (domingo 8/11): el Short de partida y las fichas

**Propongo `MDS-038`** («¿Por qué no puedes hacerte cosquillas a ti mismo?»): 933 vistas a 48 h, 20,6 %
se quedaron, el mejor de las últimas cuatro semanas con diferencia. Y **hay fichas para cuatro
capítulos**, todas con resumen leído:

1. **Por qué no puedes hacértelas** (el cerebelo cancela lo que predice): `F10`, con `F20` (la rata
   tampoco puede: tocarse apaga la corteza).
2. **¿Hace falta otra persona?** (la máquina): `F15`.
3. **Las ratas que ríen** (chillidos, saltos de alegría, el contagio y la ansiedad que las apaga):
   `E06`, `F16`, `F17`, `F18`.
4. **¿Cosquillas y chistes son lo mismo?** (Darwin-Hecker: van juntos, pero uno no enciende el otro):
   `F11`, `F14`, y la espera de `F19` como puente con el humor.

**Lo que hay que decidir antes del jueves 29, y no es mío:** `F10` (central de `MDS-038`, 14/10),
`F19` (`MDS-050`, 26/10) y `F15` (`MDS-055`, 31/10) estarían a menos de seis semanas el 8/11. Si C17
vale también para el largo, el capítulo 1 se sostiene con `F20` y el 2 tendría que contarse sin
`F15`. Si el largo, que es «el caso, entero», puede volver sobre las fichas de sus Shorts, no hay
problema. Lo pregunto en «Para el codirector».

---

## Para el codirector

1. **C17 y el largo:** ¿la regla de seis semanas vale también para `MDH-008`? El caso de `MDS-038` se
   cuenta con `F10`, y dos Shorts de esta semana usan `F19` y `F15` (ver 8). Lo necesito el jueves 29.
2. **OpenAlex con clave funciona:** ni un 429 esta noche. Gracias.
3. **Dos huecos han necesitado tres temas** (el sábado) por lo mismo: resúmenes que no dicen qué hacía
   el grupo de comparación. Es trabajo de la planificación, no de nadie más; lo dejo dicho porque la
   noche se fue en eso.

## Sugerencias a la dirección

- **`H-cierre-concreto` (repetida del 15/10, con más datos):** en cinco de siete Shorts, el lector
  final oyó el límite como un bajón. Los que menos: los que nombran algo concreto que no se probó (la
  risa en directo, los audios de WhatsApp). Regla afectada: R-GU-07. Se mediría con «se quedaron» de
  dos brazos iguales salvo el cierre.
- **`H-escena-4` (nueva):** la escena del estudio es donde dicen que se irían en casi todas las
  veintitrés lecturas. Propuesta para probar como brazo: el estudio contado dentro de la situación (el
  protagonista de la escena 1 pasa a ser el participante), sin «unos psicólogos». Regla afectada:
  R-GU-04/05. Métrica: «se quedaron viendo».
- **`H-duracion` (ya en cola):** los siete salen de 48 a 53 s estimados (51-56 reales con la firma).

## Lo que falta

- **El largo `MDH-008`:** el jueves 29, con `guionista.md` (bloque del 22/10) y la respuesta al punto 1.
- Cinco preguntas sin número propio: se miden el jueves 29.
- Quedan tres posiciones del ciclo B1 (B, control, A) para el 2, 3 y 4/11.
