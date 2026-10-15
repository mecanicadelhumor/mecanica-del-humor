**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación de la semana del 12 al 18 de octubre de 2026

Escrita la noche del **jueves 8 de octubre** (el contenedor arrancó a las 22:08 UTC, las 00:08 de
España del viernes, que para el paso 0 cuenta como jueves). No hacía falta comprobar si la semana
estaba hecha. **Primera semana del bucle (C60): siete Shorts, ciclo B1.**

```
$ git log --oneline -5 origin/main
daf1880 Visuales (C50): manifiestos y hojas de contactos
9bb37e4 métricas 2026-10-08 (diaria)
1013d8a medición de demanda 2026-10-08
263616a métricas 2026-10-08 (diaria)
fe3332b dirección 2026-10-08: C55.2 en el render (animacion.py), rutina «Animación», referentes sin cara, versión 19 (2/2)

$ git ls-remote origin 'refs/heads/claude/entrega-*'
9728d4d…  refs/heads/claude/entrega-direccion-20261008-1338
```

Ninguna entrega de planificación pendiente (la que hay es de la dirección).

Leído antes de empezar: `planificacion-jueves.md` entero (las secciones del 05/10 y del 08/10
mandan), `REGLAS_DE_PRODUCCION.md`, `bucle/ciclos.json` y `bucle/resultados.json`,
`08_comunicacion/` de los últimos siete días (`novedades.md`: siguen los cambios visuales con
imagen generada; no cambia nada de lo que escribo), `guionista_corto.md` entero, mi bitácora del
01/10 y las notas de la revisión diaria del 07 y el 08.

---

## 0 · El bucle (C60): el marcador antes de empezar

`05_calendario/bucle/resultados.json` (actualizado el 08/10 a las 19:30 UTC): el ciclo B1 aún no ha
empezado. **control, A y B: n = 0, medias nulas; veredictos A y B: «faltan datos».** La referencia
anterior (`MDS-026` a `MDS-032`, n = 7): «se quedaron viendo» **26,3 %** de media, visto 67,3 %,
mediana de vistas a 48 h 62, un cero de feed.

**Asignación.** Ningún guion llevaba todavía `"ciclo": "B1"`, así que se empieza en la posición 1
del `orden`. Primero elegí y ordené los siete temas (apartado 2); después apliqué el orden a los
huecos por fecha:

| Posición | Día | Short | Brazo |
|---|---|---|---|
| 1 | Lun 12 | `MDS-036` | **B** |
| 2 | Mar 13 | `MDS-037` | control |
| 3 | Mié 14 | `MDS-038` | **A** |
| 4 | Jue 15 | `MDS-039` | **A** |
| 5 | Vie 16 | `MDS-040` | **B** |
| 6 | Sáb 17 | `MDS-041` | control |
| 7 | Dom 18 | `MDS-042` | **A** |

La semana del 19 empieza en la posición 8 (`B`).

- **B** (`036`, `040`): la escena 1 es el hallazgo dicho como hecho, en 11 y 10 palabras, con su
  `fuente`, y el texto de pantalla es ese mismo dato. La situación va en la 2.
- **A** (`038`, `039`, `042`): las dos escenas que cuentan el mecanismo llevan `animar: true` y
  una línea `animacion` (ninguna es la última escena, que `animacion.py` no anima). Sin caras
  humanas en lo que se pide.
- Ninguna otra diferencia entre brazos: misma lectura en frío, mismo tipo de cierre, la música la
  pone la rueda.

---

## 1 · Lo que ha hecho el canal (C46)

`metricas.json` es del **06/10** (`control_c26` de ese día); `metricas_diarias.json`, del 08/10.

### Los últimos veinte Shorts, `vistas_48h`

| ID | Tema en cuatro palabras | `vistas_48h` |
|---|---|---|
| MDS-015 | por qué se contagia | 33 |
| **MDS-016** | **ironía por WhatsApp** | **1.115** |
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
| MDS-032 | risa de amigos | 16 |
| MDS-033 | anécdota que deja de hacer gracia | aún sin dato |
| MDS-034 | reírse cuando te lo piden | no se produjo el 08/10 |

**«Se quedaron viendo» a 48 h** (diaria del 08/10): `026` 17,7 · `027` 32,3 · `028` 40,0 ·
`029` 28,6 · `030` 37,8 · `031` 21,6 · `032` 6,2.

- **Mejores de las últimas cuatro semanas:** `MDS-016` (1.115) y `MDS-022` (244). Detrás,
  `MDS-031` (171) y `MDS-030` (156).
- **Peores:** `MDS-017` (0) y `MDS-023` (2), resubidas (C54, no cuentan); después `MDS-024` (4)
  y `MDS-028` (5).
- **`control_c26`** (06/10): mediana **35,0** · n 20 · sobre 100: **6** · sobre 50: **9**.
  Sigue por debajo de 50: el largo sigue suspendido.

**Derecho de tanteo: ejercido en `MDS-040`**, para `MDS-016`: la ironía que se pierde por escrito,
esta vez desde quien la escribe (Kruger y otros, 2005, `I07`), con otro chiste (el jefe y la
reunión de las ocho) y otra ficha (no `I05`). `MDS-022` tuvo el suyo en `MDS-033` hace una semana.
Además, la familia «mensajes» entera (R-TE-03) es, en la práctica, un segundo tanteo de `MDS-016`.

**Temas hundidos que no repito:** `MDS-024` (conversación), `MDS-028` (aprender a ser gracioso) y
`MDS-029` (IA). `MDS-039` (caer bien a un desconocido) está cerca de `MDS-024`, pero ese hundimiento
no se explica por el asunto que yo sepa y la pregunta es otra («hacer reír», no «no quedarse en
blanco»); lo dejo dicho por si la dirección lo ve de otra manera. `MDS-038` toca cosquillas como
`MDS-017`, que es resubida y no cuenta (C54).

---

## 2 · La demanda medida y lo que he decidido con ella

`demanda_bruta.json` del **2026-10-08T18:56:40Z**, veinticuatro consultas, `avisos` vacío. El juicio
está en `demanda.json`. Esta semana **ha mandado la bibliografía**, no el volumen: con diez fichas
nuevas se abren preguntas que llevaban semanas bloqueadas, y R-TE-01 dice ya que la demanda
correlaciona 0,17 con las vistas.

| Día | Short | Pregunta | Top 10 | Ficha |
|---|---|---|---|---|
| Lun 12 | `MDS-036` | ¿Por qué las series ponen risas grabadas? | 57.944.215 (0 de 5 en tema) | `E07` |
| Mar 13 | `MDS-037` | ¿Por qué un «vale.» con punto suena a enfado? *(mensajes)* | sin número propio | `I06` |
| Mié 14 | `MDS-038` | ¿Por qué no puedes hacerte cosquillas a ti mismo? | sin número propio | `F10` |
| Jue 15 | `MDS-039` | ¿Hacer reír ayuda a caer bien a un desconocido? | 4.773.663 («caer bien en una primera conversación») | `D11` |
| Vie 16 | `MDS-040` | ¿Por qué nadie pilla tu ironía por escrito? *(mensajes)* | 374.171 | `I07` |
| Sáb 17 | `MDS-041` | ¿Por qué sentimos vergüenza ajena? | 186.924 | `F09` |
| Dom 18 | `MDS-042` | ¿Por qué nos da la risa en un funeral? | 22.962.202 (+18,4 M «momentos serios») | `E08` |

**Por qué este orden** (decidido antes de mirar los brazos): el de más volumen el lunes festivo;
las dos de «mensajes» separadas (martes y viernes); el funeral, que es el más delicado, en domingo.

**Familia `mensajes` (R-TE-03): sí, dos.** Con ficha real y nueva: `I06` (el punto final) e `I07`
(la ironía escrita). Quedan otras tres para las semanas siguientes (`I08`, emojis y sarcasmo; `I09`,
el emoji de la sonrisa según la edad; `D10`, emojis y cercanía).

**Etiqueta `chiste`:** las siete son `otro`. Ninguno de los chistes es un dicho tomado al pie de la
letra que escala solo, como los de `MDS-016` y `MDS-022`; no he forzado ninguno para cumplir.

### Actualidad (C52): ningún gancho

1. **El 12 de octubre (festivo, «chistes del puente»):** 180 K, y nada que explicar con una ficha.
2. **El cambio de hora del 25/10** («chistes del cambio de hora», 1,9 M, 5 de 5 en tema): hay
   búsqueda, pero de sketches, y no tengo ficha que explique un mecanismo. Se vuelve a mirar el 15.
3. **Halloween (31/10):** va a las semillas; sin ficha todavía.

---

## 3 · Qué se ha escrito

Siete Shorts, `MDS-036` a `MDS-042`, con `historia`, `lectura_en_frio` con `veredicto: "pasa"`,
`visual` en cada escena, `ciclo`, `variante`, `familia_tema` y `chiste`. **`validar_guion.py`: cero
errores en los siete y cero avisos C50.** Quedan dos clases de aviso de referencia: la duración de la
serie (los siete pasan de su referencia: 48-54 s) y el remate de `MDS-039` en el segundo 9.

Por cada uno, la tesis y lo que contestó el lector que lo aprobó a «¿de qué va?»:

- **`MDS-036` (B)** · Tesis: oír reír detrás hace que un chiste malo parezca más gracioso, y más si
  la risa suena espontánea. · Lector: «un chiste malo parece más gracioso si se oyen risas de
  fondo, y por eso las series usan risas grabadas».
- **`MDS-037` (control)** · Tesis: en un mensaje, la respuesta corta con punto final se lee como
  menos sincera; a mano, no. · Lector: «por qué un ‹Vale.› con punto en un mensaje suena seco o
  enfadado, y un estudio que lo comprueba».
- **`MDS-038` (A)** · Tesis: el cerebro predice lo que va a sentir tu propio movimiento y lo atenúa.
  · Lector: «por qué no puedes hacerte cosquillas a ti mismo: tu cerebro predice lo que vas a
  sentir y eso lo amortigua».
- **`MDS-039` (A)** · Tesis: entre desconocidos, compartir algo con humor hace que se caigan mejor
  y se sientan más cerca. · Lector: «reírse juntos hace que dos desconocidos conecten».
- **`MDS-040` (B)** · Tesis: quien escribe con ironía cree que se nota mucho más de lo que se nota,
  porque oye su propio tono. · Lector: «cuando escribes con ironía, el otro la pilla mucho menos de
  lo que tú crees».
- **`MDS-041` (control)** · Tesis: la vergüenza ajena aparece aunque el otro no lo sepa, y en el
  cerebro se parece al dolor ajeno. · Lector: «por qué te da apuro que otro haga el ridículo aunque
  él ni se entere: es empatía».
- **`MDS-042` (A)** · Tesis: en el duelo, la risa de verdad va con menos enfado, alivio y mejores
  relaciones; la de compromiso, no; es una correlación. · Lector: «reírse en un velatorio no es
  faltar al respeto: quien se ríe de verdad en pleno duelo está mejor».

Los siete «de qué va» dicen la misma idea que su `historia`.

### Variedad (C48.1)

- **Aperturas:** ninguna en primera persona. «Un chiste malo parece…» / «Propones ir al cine…» /
  «Hazte cosquillas…» / «Dos desconocidos…» / «Tu ironía por escrito…» / «En una boda…» / «En un
  velatorio…».
- **Cierres**, en columna: «Así que al chiste del pez…» / «Eso sí: el estudio mide…» / «Lo que no
  enseña el escáner…» / «La pega: en el laboratorio…» / «¿Te habría librado un emoji…?» / «Tu
  servilleta, entonces…» / «Esa risa no es falta de respeto…». Ninguno empieza como otro ni como los
  cuatro anteriores (el validador no avisa).
- **Series:** dos «Esto no tiene gracia y esto sí», dos «Ríete primero», tres «El experimento». Con
  secuencias de tipos de escena distintas.

---

## 4 · Las fichas: usadas y evitadas

**Las siete fuentes centrales son fichas nuevas** (C17 cumplido sin excepción): `E07`, `I06`, `F10`,
`D11`, `I07`, `F09`, `E08`. Cada guion lleva en `notas_humor` la frase del resumen copiada literal.

**Evitadas a propósito:** `I05` (fuente de `MDS-016`: el tanteo va con `I07`); `A10` (libre desde el
12/10, pero no explica la risa en el duelo ni la nerviosa sin deducir); `E01`, `E02`, `E04`
(Provine, libres desde el 10/10: `E07` mide justo las risas grabadas); `E03`/`D06` (contagio, en
ventana y tema de `MDS-015`); `K04` (la IA descansa); `B03` (caído dos veces).

---

## 5 · El corpus (paso 7): diez fichas nuevas, y las correcciones

**La red ya llega** a `api.crossref.org` (con `mailto`), Europe PMC, PubMed y algunas editoriales.
**OpenAlex devuelve 429**: el presupuesto gratuito diario de la IP compartida está agotado («$0
remaining; resets at midnight UTC»). `doi.org` y ScienceDirect siguen dando 403; Semantic Scholar,
429.

**Diez fichas nuevas en `semillas.json`** (regenerado el `.md`; `validar_bibliografia.py`: «los dos
ficheros dicen lo mismo»). Todas con título y DOI vistos juntos en el registro de Crossref y la
frase del resumen copiada en `resumen_verificado`:

| Ficha | Trabajo | Resumen leído en |
|---|---|---|
| `I06` | Gunraj y otros, 2016 · el punto final en los mensajes | ficha de SUNY Research Connect |
| `I07` | Kruger, Epley, Parker y Ng, 2005 · egocentrismo en el correo | Europe PMC |
| `I08` | Thompson y Filik, 2016 · emoticonos y sarcasmo | academic.oup.com |
| `I09` | Cui y otros, 2026 · el emoji de la sonrisa según la edad | Europe PMC |
| `D10` | Huh, 2025 · emojis y cercanía | Crossref y Europe PMC |
| `D11` | Treger, Sprecher y Erber, 2013 · humor y simpatía entre desconocidos | Crossref |
| `E07` | Cai, Chen, White y Scott, 2019 · risas de fondo y chistes malos | Europe PMC |
| `E08` | Keltner y Bonanno, 1997 · la risa en el duelo | PDF del autor (greatergood.berkeley.edu) |
| `F09` | Krach y otros, 2011 · vergüenza ajena y empatía | Europe PMC |
| `F10` | Blakemore, Wolpert y Frith, 1998 · las cosquillas propias | Europe PMC |

**Localizadas y NO escritas** (sin resumen legible): Houghton y otros, 2018 (el punto y la
brusquedad; solo vi los «highlights» en un buscador), Provine, 1992 (risa contagiosa; Springer pide
sesión) y Oveis y otros, 2016 (risa y estatus).

**Correcciones pedidas por la dirección:** `D07` lleva ya el título de su DOI («Detecting
affiliation in colaughter across 24 societies») y un comentario que dice lo que encontró (amigos o
desconocidos, no risa real o fingida). `F06` y `F07` llevan `duplicado_de` (`F02` y `F01`) y el
aviso al principio de `por_que`; no las he borrado porque las citan guiones publicados.

**Recuento:** libres con hallazgo y nunca centrales, después de esta semana: `I08`, `I09`, `D10`,
`F03`, `F06`/`F02`, `H04`, `K01`, `K04`, `B03`, y por la regla de seis semanas `A10`, `E01`, `E02`,
`E04` y las de agosto. Da para dos semanas a siete; la semana que viene hay que volver a añadir
diez.

---

## 6 · La lectura en frío: diecinueve lectores, ningún tema caído

Encargo literal, subagente nuevo en cada vuelta, sin avisarle de nada.

| Short | Vueltas | Qué cambió |
|---|---|---|
| `MDS-036` | 3 | El nombre del estudio (Scott) no cuadraba con la fuente en pantalla (Cai): subtítulo con los cuatro autores. «A tu cuñado le faltaba público» no se entendía (el chiste lo cuentas tú): ahora es el chiste del pez. |
| `MDS-037` | 3 | Klin frente a Gunraj, igual que arriba; «no cambiaba nada» y «sonaban igual» (¿igual que qué?): ahora «en el móvil» y «en una nota escrita a mano». El cierre vuelve al amigo. |
| `MDS-038` | 2 | El texto de pantalla del cierre no se entendía; fuera «Ahora, en serio» y, en la segunda, la frase que repetía la anterior. |
| `MDS-039` | 3 | «Tareas con humor» y «parecidas» frente a «las mismas»; el «Pero» y el «Eso sí» del cierre sonaban a pega y eran un consejo: ahora «La pega:». Fuera «Como los dos del ascensor» (dos lectores). |
| `MDS-040` | 2 | El cierre condicional («Si un emoji te habría librado…») liaba: ahora es una pregunta. |
| `MDS-041` | 3 | «Las dos zonas», «¿qué escáner?» y, sobre todo, la mesa que se reía y salía de la nada en el cierre (prueba 2): el primo que se ríe entra ahora en la escena 3. |
| `MDS-042` | 3 | «Más distancia del dolor», «menos enfado» (¿con quién?), «mejor trato» (¿quién a quién?): ahora «estaba menos enfadado, sentía alivio y se llevaba mejor con su gente». |

**Criterio (C48.2):** lo que el lector dice haber entendido «tardando un segundo» o «con la frase
siguiente» va a `notas`; lo que no supo interpretar, bloquea. `MDS-037`, `039` y `041` han pasado
la tercera con una nota de ese tipo cada uno: son los tres casos más justos de la semana.

**Lo que se repite en las diecinueve lecturas, para quien escriba la semana que viene:**

1. **«No sé quién es» el investigador** salió en la primera vuelta de los siete. Presentarlo con su
   oficio («la neurocientífica…», «el psicólogo…») lo arregló en todos. Y si la fuente en pantalla
   es el primer autor y la voz nombra al último, el lector cree que son dos estudios.
2. **La escena del estudio es donde se irían** (cinco de diecinueve se irían ahí y casi todos los
   demás dicen que ahí dudaron: «pasa a clase»).
3. **Los cierres honestos se oyen «a medias»** cuando terminan en lo que no se sabe. Los que
   vuelven a la situación del principio (`037`, el amigo que solo quería ir al cine) se oyen como
   final. Ver «Sugerencias».
4. **El brazo B tiene un coste que el lector ve:** «la primera frase ya me da la conclusión y el
   estudio solo confirma» (`MDS-036`, vuelta 3). No lo he tocado: es justo lo que mide el ciclo.

---

## 7 · Revisiones

`05_calendario/revisiones/` no tiene notas sobre guiones pendientes (todas son de Shorts y largos
ya producidos; C54) y no hay `bibliografia.md`. No he aplicado ni retirado ninguna. La nota de la
revisión diaria del 08/10 sobre `MDS-035` (un callback a una escena de 40 s antes necesita decirse
en claro) la he aplicado al escribir: el primo de `MDS-041` entra en la escena 3 para que el cierre
no lo estrene.

---

## Para el codirector

1. **`MDS-034` no se produjo el jueves 8** (la revisión diaria lo dice: `producir.yml` se colgó en
   la instalación). No es mío ni lo he tocado; lo apunto porque la parrilla de la semana del 12 no
   deja huecos libres para recolocarlo: si se quiere publicar, la decisión es de la dirección.
2. **El brazo A depende de la rutina «Animación»** (viernes). Si aún no existe, `MDS-038`, `039` y
   `042` saldrán como el control y `bucle.py` los apartará: la primera semana del ciclo se quedaría
   sin datos del brazo A.
3. **OpenAlex está sin presupuesto** desde esta IP (429, «$0 remaining»). Una clave gratuita
   (parámetro `api_key`) en el entorno daría a esta tarea su propia cuota. Crossref y Europe PMC sí
   funcionan, y han bastado esta semana.

## Sugerencias a la dirección

- **`H-cierre-vuelta`** · Regla afectada: R-GU-07 (el cierre dice dónde falla). Propuesta: que el
  cierre diga el límite **y termine volviendo a la situación del principio** (no en «no se sabe»).
  Por qué: en diecinueve lecturas, los cierres que acaban en lo que no se sabe se oyen «a medias» o
  «fríos»; el único elogiado como final cierra con el amigo de la escena 1. Cómo se mediría:
  porcentaje visto (no «se quedaron viendo», que se decide antes) entre dos brazos iguales salvo el
  cierre.
- **Presentar al investigador por su oficio** se lo he aplicado a los siete porque arregla una
  frase que no se entendía (no es una modificación de brazo: es la lectura en frío haciendo su
  trabajo). Si la dirección lo quiere como regla, sería una línea en R-GU-06.

## Lo que falta

- `MDS-037` y `MDS-038` entran sin número de demanda propio: se miden el jueves 15.
- La familia «mensajes» tiene ficha para tres Shorts más (`I08`, `I09`, `D10`); la semana que viene
  hay que añadir otras diez fichas.
- `MDH-008` sigue escrito, sin tocar y fuera de la parrilla.
