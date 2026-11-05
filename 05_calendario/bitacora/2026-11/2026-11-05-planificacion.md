**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación de la semana del 9 al 15 de noviembre de 2026

Escrita la noche del **jueves 5 de noviembre** (el contenedor arrancó a las 22:08 UTC, las 23:08 de
España). Primera semana con **tres lectores por vuelta y mayoría** y con **B2** (factorial 2×2).
**Resultado: tres Shorts, no siete.** Lunes 9, martes 10, sábado 14 y domingo 15 se quedan sin emisión.

```
$ git log --oneline -5 origin/main
a32aeb5 métricas 2026-11-05 (diaria)
ecd2ac2 medición de demanda 2026-11-05
7dc0b99 métricas 2026-11-05 (diaria)
45b24f6 dirección 2026-11-05: bitácora, cierre de la prueba de voces
5f577a5 dirección 2026-11-05: las imágenes que no pegaban eran un fallo de visual.py (…)

$ git ls-remote origin 'refs/heads/claude/entrega-*'
73c4b17… refs/heads/claude/entrega-revision-20261104-1031   (de la revisión, no mía: su contenido ya está en main, dice la dirección)
```

Leído antes de empezar: `planificacion-jueves.md` entero (mandan los bloques del 02/11, 29/10, 23/10,
22/10, 19/10, 15/10 y 05/10), `guionista_corto.md` entero (precisiones del 02/11 y 29/10),
`REGLAS_DE_PRODUCCION.md`, `bucle/ciclos.json` y `resultados.json`, `compromisos.json`,
`08_comunicacion/` de los últimos siete días (`novedades.md`: siguen los cambios visuales; la dirección del
05/11: búsquedas con sujeto explícito y siempre con `prompt`, tres lectores y banco; la revisión del 05/11:
nota de `MDS-062`), mi bitácora del 29/10, `temas_en_reserva.md` y `revisiones/`.

---

## 0 · El bucle (C60)

**B1, cerrado** (`ciclos.json`, decisión del 05/11): control n = 7-8 (19,6-24,1 %), A n = 7 (29,4 %, gana
con reparo → factor de B2), **B n = 8 (37,6 %, GANA → es el control de B2)**. **B2 empezó hoy** con
`MDS-060` (posición 1, D); todavía no hay ningún dato de B2. No decido nada: lo dice la regla.

**Asignación de esta semana** (las posiciones van por día de emisión desde el 5/11):

| Día | Posición | Brazo | Short |
|---|---|---|---|
| Lun 9 | 5 | D | **vacía** |
| Mar 10 | 6 | AD | **vacía** |
| Mié 11 | 7 | A | `MDS-064` (escenas 4 y 5 con `animar`) |
| Jue 12 | 8 | control | `MDS-065` |
| Vie 13 | 9 | control | `MDS-066` |
| Sáb 14 | 10 | D | **vacía** |
| Dom 15 | 11 | AD | **vacía** |

**Lo que no ha sido ciego, y lo digo:** los brazos de las posiciones 5-11 ya estaban escritos en el
`orden` cuando elegí los temas. Ordené los temas por criterio editorial (tanteo el lunes, `mensajes`
martes y jueves…) antes de mirar el brazo de cada día, pero los vi. Al final el orden lo decidió la lectura
en frío: **los tres que pasaron eran guiones de seis escenas**, y solo caben sin tocarlos en los días A y
control (en un A la animación no cambia el texto). Para un día D o AD habría que quitar una escena y volver
a leer, y ya no quedaban vueltas. Por eso los tres van miércoles, jueves y viernes, y por eso los cuatro
días cortos se quedan vacíos.

---

## 1 · Lo que ha hecho el canal (C46)

`metricas.json` y `metricas_diarias.json` del 05/11.

| ID | Tema | `vistas_48h` | Se quedaron |
|---|---|---|---|
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
| **MDS-050** | **reírte antes de las cosquillas** | **913** | 15,7 % |
| MDS-051 | el «jajaja» sin reírte | 32 | 31,2 % |
| MDS-052 | risa por compromiso | 11 | 36,4 % |
| MDS-053 | chiste en una reunión | 16 | 37,5 % |
| MDS-054 | escribir en vez de llamar | 30 | 36,7 % |
| MDS-055 | cosquillas de una máquina | 498 | 23,7 % |
| MDS-056 | reírse de lo que cuenta | 0 (12 en `resultados.json`) | 16,7 % |

- **Los dos mejores de las últimas cuatro semanas: `MDS-038` (933) y `MDS-050` (913)**, los dos de
  cosquillas, y `MDS-055` (498), también. **Los peores:** `MDS-056`, `MDS-046` (4), `MDS-048` (5).
- **`control_c26`:** mediana **28,5** · n 20 · sobre 100: **6** · sobre 50: **7**. El punto de control es
  el 15/11.
- **Derecho de tanteo: intentado tres veces y no ha salido.** `F20` (pedir cosquillas y huir), `F17`
  (cosquillas contagiosas) y, del banco, `F14` (risa floja). Los tres cayeron a la tercera vuelta (apartado
  3). Las tres fichas centrales libres de cosquillas que quedan son de ratas, y abrir con el dato de unas
  ratas (brazo B) es justo lo que los lectores no entienden en el segundo cero. **La semana que viene
  ninguna semana sin cosquillas**: `F14` estaba cerca.

---

## 2 · La demanda medida

`demanda_bruta.json` del **2026-11-05T20:10:38Z**, veinticuatro consultas, `avisos` vacío; juicio en
`demanda.json`. Como siempre, las sumas del top 10 son sketches y canciones; sirven para ver huecos.
**Esta semana no ha decidido la demanda: ha decidido la lectura en frío.** De las tres preguntas que
salen, dos tienen número propio en la medición del 29/10 o de hoy («por qué se contagia la risa», cerca
de «por qué nos reímos a la vez con los amigos», 140 M fuera de tema; «por qué lloramos de risa», 2,7 M);
la tercera (el chiste malo y la carcajada) va a las semillas.

**Actualidad (C52): ningún gancho.** Las tendencias son fútbol (una muerte), tenis y una detención de una
periodista; Wikipedia, sucesos. Nada cumple C52.

---

## 3 · Lo que se ha escrito, y la lectura en frío con tres lectores

**Catorce temas, 108 lecturas, tres aprobados.** Encargo literal de `guionista_corto.md`, tres subagentes
nuevos por vuelta, al mismo tiempo, y decide la mayoría. **Cuento como bloqueo lo que dos de tres copian
en la pregunta 3 diciendo que no lo entendieron o que lo entendieron después**; lo que copian diciendo «lo
entiendo, pero…» va a `notas` (criterio del 28/09). **La firma de la fuente la copian casi todos los
lectores en casi todos los guiones**: va siempre a `notas`.

| Tema (ficha) | Brazo previsto | Vueltas | Resultado |
|---|---|---|---|
| Pedir cosquillas y huir (`F20`) | D | 3 | cae |
| La errata en el chat (`I17`) · *mensajes* | AD | 3 | cae |
| ¿Los graciosos son más listos? (`C05`) | A | 3 | cae |
| El móvil en la mesa (`I18`) · *mensajes* | control | 3 | cae |
| **La risa que se pega (`E09`)** | control | 3 | **pasa → `MDS-066`** |
| El cachorro (`E15`, reserva) | D | 3 | cae (2.ª semana) |
| Las cosquillas contagiosas (`F17`) | AD | 3 | cae |
| La risa floja (`F14`, reserva) | banco | 3 | cae (2.ª semana) |
| Mirar el WhatsApp mientras te hablan (`I19`) · *mensajes* | banco | 3 | cae |
| «Es del trabajo» (`I20`) · *mensajes* | banco | 3 | cae |
| La pareja que se ríe (`D08`, reserva) | banco | 3 | cae (2.ª semana) |
| El emoji del banco (`I22`) · *mensajes* | banco | 3 | cae |
| **El chiste malo y la carcajada (`E22`)** | banco | 1 | **pasa → `MDS-064`** |
| **Llorar de alegría (`E20`)** | banco | 3 | **pasa → `MDS-065`** |

Por cada aprobado, la tesis al lado de lo que dijeron los lectores a «¿de qué va?»:

- **`MDS-064` (A)** · Tesis: oír reír hace más graciosos un chiste, un eructo o una caída, y más si la
  risa es de verdad. · Lectores: «oír a alguien reírse hace que un chiste (o una caída, un eructo) nos
  parezca más gracioso» (los tres, casi con las mismas palabras).
- **`MDS-065` (control)** · Tesis: ante las lágrimas de alegría la gente intenta calmar; ante una sonrisa,
  sumarse. · Lectores: «cuando alguien llora de alegría, solemos intentar calmarlo; las lágrimas llevan a
  querer calmar aunque sean de felicidad».
- **`MDS-066` (control)** · Tesis: al oír reír se activan las zonas del cerebro que mueven la cara. ·
  Lectores: «oír reír a alguien hace que tu cerebro prepare tu cara para sonreír, y por eso la risa se
  pega».

Las tres respuestas completas, con el historial de vueltas, en `lectura_en_frio` de cada guion.
**`validar_guion.py`: cero errores en los tres**; un aviso en cada uno (duración de referencia de la
serie: 51-54 s estimados). `MDS-065` sale en 54,3 s estimados; los tres lectores quitarían «Tu «ya está»
no era raro…», y se queda porque es la vuelta a la amiga del principio (lo explico en el guion).

**Lo que se repite en las 108 lecturas, para quien escriba la semana que viene:**

1. **Los rótulos de pantalla se leen sueltos.** El lector los ve entre corchetes, separados de la voz, y
   los rótulos de dos o tres palabras («Ganas… y miedo», «Por si acaso», «Le suena / Sin que suene»,
   «22 remitentes») caen casi siempre. Los rótulos con sujeto y verbo pasan.
2. **El arranque con el dato (brazo B, control de B2) se lee como «la conclusión sin contexto».** Pasa
   cuando el dato es de personas en una situación de todos (la risa que se pega, el chiste malo); cae
   cuando es de ratas o de un concepto («desbordado», «fuera de lugar»).
3. **Cualquier «Eso sí», «Ojo» o «La letra pequeña» que no diga en la misma frase qué cambia** («…no con
   amigas de años», «…solo en chats de empresas») se copia como no entendido: el lector pregunta «¿y
   entonces?». Los cierres que pasaron dicen la salvedad y qué no se midió («no comprobaron si la gente
   sonreía: solo miraron su cerebro»).
4. **El «¿y si es al revés?»** no se entendió ni una vez en tres semanas (`I18`, `D08`, `C05`).
5. **Las escenas de método con «unos psicólogos…»** sin decir qué vio la gente ni con qué se comparó.
6. **Lo que los tres aprobados tienen en común:** una situación de todos con una persona concreta
   (el desconocido del autobús, el primo y la tía, la amiga del trabajo), un estudio que es esa misma
   situación en pequeño, y ningún animal.

**Variedad (C48.1):** ninguno abre en primera persona; aperturas «Oír a alguien reír…» / «Si alguien llora
de alegría…» / «Cuando oyes reír a alguien…» (dos empiezan por oír reír: lo dejo dicho). Cierres: «Así
que el chiste de tu primo…» / «Tu «ya está» no era raro…» / «Por eso acabaste sonriendo…», con «Eso sí»
en dos y «Aunque» en uno. **Ojo, que dos de los tres hablan de oír reír** (`MDS-064` y `MDS-066`): los he
separado (miércoles y viernes), y no son el mismo hallazgo (uno es la gracia del chiste; el otro, la
cara). **Familia `mensajes`: cero** (los cinco temas cayeron). **Etiqueta `chiste`:** los tres, `otro`.

**El banco: vacío.** No sobró ningún aprobado. La meta era que sobraran dos o tres.

---

## 4 · Las fichas

**Fuentes centrales:** `E22` y `E20` (nuevas esta noche) y `E09` (nunca central). Ninguna repetida en
seis semanas (C17). **Evitadas:** `F10` (cuarentena hasta el 25/11), `F15` y `F19` (centrales el 31/10 y
el 26/10), `I11` (central en `MDS-048`, hundido), `E07` (central en `MDS-036`; uso `E22`, otro estudio).

**Corpus (paso 7): once fichas nuevas** en `semillas.json` (regenerado el `.md`;
`validar_bibliografia.py`: «los dos ficheros dicen lo mismo»), todas con título y DOI vistos juntos en
OpenAlex y la frase del resumen copiada en `resumen_verificado`: `I17` (la errata corregida), `I18` (el
móvil en la mesa, Misra y otros), `I19` (contestar mensajes en una charla), `I20` (el «phubbing» con
excusa), `I21` (la mera presencia del móvil, Przybylski y Weinstein), `I22` (el emoji del banco), `E19`
(vocalizaciones de juego, revisión), `E20` (lágrimas de alegría), `E21` (vocalizaciones humanas, revisión),
`E22` (la risa que hace gracioso un chiste) y `J08` (gelotofobia, 863 personas). **Arreglada:** `C05`
lleva por fin su resumen (y la nota de que OpenAlex lo fecha en 2011). La red estaba abierta y
`OPENALEX_API_KEY` en el entorno (no se ha escrito en ningún sitio).

**Probado y descartado:** McGraw y otros, 2014 («The rise and fall of humor») y Huang y otros, 2015 (el
sarcasmo y la creatividad): ni OpenAlex, ni Crossref, ni Europe PMC dan el resumen. Sin resumen no hay
ficha. Schroeder y otros, 2017 (la voz y el texto) ya era `I11`.

---

## 5 · Revisiones

- **`revisiones/MDS-062.md`** (de hoy): propone quitar la escena 3 («parar la película»). **No la aplico**:
  `MDS-062` sale el sábado 7 como **brazo A**, que en B2 son seis escenas; con cinco sería un AD y el
  Short dejaría de medir lo que le toca. Además es un guion ya escrito (regla 11.4). **No la retiro**, para
  que la dirección la vea.
- Las notas de `MDS-048` a `MDS-059` son de Shorts publicados: no se aplican (C54).

---

## Para el codirector

1. **Cuatro días sin Short la semana que viene (lunes 9, martes 10, sábado 14 y domingo 15).** Con tres
   lectores y mayoría pasaron **3 de 14 temas** (la semana pasada, con un lector, 6 de 14). Las posiciones
   de B2 vacías son las 5, 6, 10 y 11: **los cuatro días cortos (D y AD)**. Sé que el codirector escribió
   que un día sin vídeo es información que no tenemos; lo he intentado con once temas más de lo previsto
   y 108 lecturas, y no he bajado el criterio para llenar.
2. **Los brazos cortos son el cuello de botella de esta semana.** Un tema que pasa con seis escenas no
   puede ir a un día D/AD sin quitarle una escena y volver a leerlo. Si quieres que el banco sirva para
   cualquier día, **cada aprobado necesitaría dos lecturas (la de seis y la de cinco)**: el doble de
   lecturas. O que el `orden` deje que un aprobado de seis vaya a un día A o control de la semana
   siguiente.
3. **Los lectores son subagentes del modelo `sonnet`.** Son muy exigentes con los rótulos de pantalla
   leídos sueltos y con la firma de la fuente (la copian casi siempre). Si la dirección leyó `MDS-062`
   con otros lectores y pasó, puede que la diferencia esté ahí. Lo digo para que se compare, no para
   cambiar nada yo.
4. **`MDS-062` (sábado 7): la nota de la revisión no la aplico** (apartado 5).
5. **La rama `claude/entrega-revision-20261104-1031`** sigue viva; no es mía y no la toco.

## Sugerencias a la dirección

- **`H-rotulo-con-verbo`:** los rótulos de pantalla de dos o tres palabras se leen sueltos y caen; los que
  tienen sujeto y verbo pasan. Regla afectada: la de texto en pantalla (R-IM-03). Se mediría con «se
  quedaron» de dos brazos iguales salvo los rótulos.
- **`H-salvedad-con-consecuencia`:** el cierre honesto que dice qué no se midió («no comprobaron si la
  gente sonreía») pasa; el que pone una etiqueta («Eso sí: era con desconocidos») sin decir qué cambia,
  no. Regla afectada: R-GU-07.
- **Que la lectura en frío pase el rótulo y la voz juntos** («voz — rótulo» en la misma línea, como se
  ven en el vídeo) en vez de entre corchetes: hoy el lector juzga el rótulo como si saliera solo, y en el
  vídeo sale debajo de la frase que lo explica. Es un cambio del encargo: lo decide la dirección.

## Lo que falta

- **Los cuatro días vacíos** (ver arriba).
- **Ningún Short de `mensajes`** esta semana (R-TE-03); los cinco intentos están en la reserva.
- **El derecho de tanteo de cosquillas** no se ha ejercido (tres intentos).
- **El largo `MDH-008`** no lo he tocado: es de la dirección hasta el estreno.

## Respuesta del codirector
