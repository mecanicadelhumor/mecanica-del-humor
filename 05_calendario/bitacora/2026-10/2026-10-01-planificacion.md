**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53), primera vez como rutina de Code.** El `--comprobar` previo listó 17 ficheros, todos míos, ninguno fuera. Sin plan B.

# Bitácora · Planificación de la semana del 5 al 9 de octubre de 2026

Escrita la noche del **jueves 1 de octubre** (el contenedor arrancó a las 22:08 UTC). Hoy es
jueves, así que el paso 0 no aplica: no hay que comprobar si la semana ya está hecha.

**Primera acción, antes de tocar nada:**

```
$ git log --oneline -5 origin/main
98c67a1 medición de demanda 2026-10-01
b725cb0 registro: sincronizado con YouTube 2026-10-01
89da65e Visuales (C50): manifiestos y hojas de contactos
6b022c5 revisión diaria 2026-10-01
6161564 Registro y expediente de calidad: MDS-029

$ git ls-remote origin 'refs/heads/claude/entrega-*'
(nada)
```

Ninguna entrega pendiente. `origin/main` trae la medición de demanda de hoy y la revisión
diaria de hoy.

Leído antes de empezar: `planificacion-jueves.md` entero, `08_comunicacion/` de los últimos
siete días (`novedades.md` dice que vienen cambios visuales con imagen y vídeo generados por
IA; no cambia nada de lo que escribo esta noche, y la dirección del 29 y el 30 dice que
`"estilo": "animacion"` no existe todavía: no lo he usado), `guionista_corto.md` entero, la
bitácora de la planificación del 25/09 y la de métricas del 30/09.

---

## 1 · Lo que ha hecho el canal (C46)

`metricas.json` es del **29/09** (`actualizado_utc: 2026-09-29T11:23:23Z`). Los cinco Shorts
de la semana pasada (`MDS-026` a `MDS-030`) **no tienen todavía ninguna lectura**: los temas de
esta semana se han elegido sin saber cómo les fue.

### Los últimos veinte Shorts, `vistas_48h`

| ID | Tema en cuatro palabras | `vistas_48h` |
|---|---|---|
| MDS-006 | reírse cuando no debes | 4 |
| MDS-007 | humor negro e inteligencia | 35 |
| MDS-008 | dos versiones del chiste | 27 |
| MDS-009 | reírse de lo mismo | 21 |
| MDS-010 | el chiste explicado pierde | 4 |
| MDS-011 | la prueba que puntúa gracia | 20 |
| MDS-012 | contar bien un chiste | 9 |
| MDS-013 | broma o burla | 6 |
| MDS-014 | test de estilos de humor | 1 |
| MDS-015 | por qué se contagia la risa | 33 |
| **MDS-016** | **ironía por WhatsApp** | **1.115** |
| MDS-017 | cosquillas y ratas (resubida) | 0 |
| MDS-018 | profesor gracioso enseña mejor | 113 |
| MDS-019 | anuncios graciosos venden más | 137 |
| MDS-020 | la IA escribiendo chistes | 37 |
| MDS-021 | personalidad de los cómicos | 122 |
| **MDS-022** | **chiste, la segunda vez** | **244** |
| MDS-023 | reírse y salud (resubida) | 2 |
| MDS-024 | conversación sin quedarse en blanco | 4 |
| MDS-025 | humor y memoria | 68 |

### Mejores y peores de las últimas cuatro semanas (04/09 – 01/10)

- **Mejores:** `MDS-016` (1.115) y `MDS-022` (244). Detrás, `MDS-019` (137) y `MDS-021` (122).
- **Peores:** `MDS-017` (0) y `MDS-023` (2), las dos resubidas (C54: no cuentan como temas
  hundidos). Después de ellas, `MDS-024` (4) y `MDS-010` (4).

### `control_c26`

`mediana_vistas_48h` **24,0** · `n_videos` 20 · `sobre_100_vistas` **5** · `sobre_50_vistas` **6**.
Por debajo de 50: el largo sigue suspendido y el sábado y el domingo siguen vacíos.

### Derecho de tanteo: ejercido en `MDS-033`

`MDS-016` ya tuvo el suyo (`MDS-027`), así que, como dice la dirección del 28/09, recae en
**`MDS-022`** («por qué un chiste hace menos gracia la segunda vez»). Su ficha, `A06`, no puede
volver a ser central hasta el 03/11, y las otras dos de su asunto (`A05`, `A07`) hasta el 16/10.
`MDS-033` («¿por qué una anécdota graciosa deja de hacer gracia?») mira **el mismo asunto —lo que
tuvo gracia y deja de tenerla— desde la distancia en lugar de la repetición**, con `A03`.

**Y lo que más pesa de las métricas para escribir, y no lo he conseguido del todo:** los dos
mejores en retención (`MDS-021` y `MDS-022`, 59-64 % en el segundo 30) son los más cortos del
canal, 41-42 s. **Mis cinco guiones estiman entre 52 y 54 s.** Los escribí a unos 45 y fueron
creciendo con cada vuelta de lectura en frío, porque casi todo lo que piden los lectores es una
frase que cosa (quién es este, qué quiere decir esto). Es una tensión real entre C48 y lo que
dice la retención; va a «Para el codirector».

---

## 2 · La demanda medida, y qué se ha decidido con ella

`demanda_bruta.json` es del **2026-10-01T18:30:01Z**: las veinticuatro consultas de las semillas
del 25/09, `avisos` vacío, 2.424 unidades. Quinta medición buena seguida. El juicio pregunta a
pregunta está en `demanda.json`.

| Día | Emisión | Pregunta | Top 10 | En tema | Ficha |
|---|---|---|---|---|---|
| Lun 5 | `MDS-031` | qué le pasa a tu cerebro cuando te ríes (+ por qué nos gusta que nos hagan reír) | 159.304 (+66,5 M) | 2 de 5 (+0 de 5) | `F07` |
| Mar 6 | `MDS-032` | ¿se nota en la risa si dos personas son amigas? | sin número propio | — | `D07` |
| Mié 7 | `MDS-033` | por qué una anécdota graciosa deja de hacer gracia (cerca de «chistes que envejecen mal») | 3.856.586 | 0 de 5 | `A03` |
| Jue 8 | `MDS-034` | por qué no puedes reírte de verdad cuando te lo piden (hueco de «risa falsa») | 4.920.459 | 1 de 5 | `F08` |
| Vie 9 | `MDS-035` | ¿apuntar tres cosas graciosas al día te hace más feliz? | sin número propio | — | `H03` |

**Lo que ha mandado de verdad no es el volumen, es C17.** Las preguntas con más volumen están
hechas («puede una máquina entender un chiste», 426 M, la acaba de tocar `MDS-029`; «humor
absurdo», 207 M, `MDS-030`; «segunda vez», 127 M, `MDS-022`; «profesor gracioso», 114 M,
`MDS-018`), o no tienen ficha («memes», 159 M, sigue en `pendientes_de_fuente.md`), o su ficha
está dentro de la ventana de seis semanas: **«por qué me río cuando estoy nervioso» (76,6 M y
0 de 5)** con `A10` hasta el 12/10, y **«funcionan las risas enlatadas»** con `E01`/`E02`/`E04`
hasta el 10/10. **Esas dos son la cabeza de serie de la semana del 12**, y está escrito en
`demanda.json`.

**Dos de los cinco Shorts entran sin número propio** (`MDS-032` y `MDS-035`), por hueco y por
ficha libre. Van a las semillas para medirlas el jueves 8.

### Actualidad (C52): ningún gancho esta semana

Leído el radar entero. Los tres mejores candidatos y por qué no:

1. **«meme 67» / «por qué es viral 67»** (autocompletar). Es un meme sobre todo de niños, y no
   hay ficha que explique por qué hace gracia sin deducir (la de los memes no existe).
2. **«La bola negra»** y el debut del hijo de dos actores (Google Tendencias y lo más leído de
   la Wikipedia). Es una persona real y la película no va de humor: no hay mecanismo que
   explicar.
3. **«ChatGPT»** en lo más leído de la Wikipedia los tres días. Encajaría con `K03`/`K04`, pero
   `MDS-029` salió hoy mismo y la IA descansa hasta ver sus números (decisión del 25/09).

El calendario del 5 al 9 no trae nada; el **puente del 12** y el **cambio de hora del 25** van a
las semillas para medir si hay búsqueda de humor alrededor.

---

## 3 · Qué se ha escrito

Cinco Shorts, `MDS-031` a `MDS-035`, de lunes a viernes a las 19:00, con `historia`,
`lectura_en_frio` con `veredicto: "pasa"` y `visual` en cada escena. **`validar_guion.py` pasa
los cinco con cero errores y cero avisos C50.** Los únicos avisos que quedan son de referencia:
la duración de la serie, el remate de `MDS-031` en el segundo 9, y C17 de `A03` y `D07` (ver el
apartado 4: ninguno de los dos fue fuente central donde aparece).

Por cada uno, la tesis y, al lado, lo que contestó **el lector que lo aprobó** a «¿de qué va?»:

### `MDS-031` · «¿Qué le pasa a tu cerebro cuando te ríes?» · El experimento · `F07`

- **Tesis:** cuando un chiste te hace gracia se enciende el circuito de recompensa del cerebro,
  y cuanta más gracia te hace, más se enciende.
- **Según el lector:** «un chiste viejo de médicos sirve de excusa para contar que, cuando algo
  te hace gracia, el cerebro activa el circuito del placer, según un experimento con escáner».

### `MDS-032` · «¿Se nota en la risa si dos personas son amigas?» · El experimento · `D07`

- **Tesis:** con oír un segundo de dos personas riéndose a la vez, gente de 24 sociedades
  acertaba si eran amigas o desconocidas más que a cara o cruz, aunque a veces por muy poco.
- **Según el lector:** «si puedes saber que dos personas son amigas con solo oírlas reír juntas».

### `MDS-033` · «¿Por qué una anécdota graciosa deja de hacer gracia?» · Ríete primero · `A03`

- **Tesis:** un percance pequeño tiene gracia cuando queda cerca y la pierde al alejarse; con
  una desgracia grande pasa al revés.
- **Según el lector:** «por qué algo que te hizo llorar de risa un día deja de tener gracia
  cuando lo cuentas un año después».

### `MDS-034` · «¿Por qué no puedes reírte de verdad cuando te lo piden?» · Esto no tiene gracia y esto sí · `F08`

- **Tesis:** la risa que mandas y la que se te escapa no son la misma risa hecha mejor o peor:
  parecen salir por dos caminos del cerebro casi independientes.
- **Según el lector:** «la risa que te piden y la risa que se te escapa no son lo mismo: según
  una investigadora, salen de partes distintas del cerebro».

### `MDS-035` · «¿Apuntar tres cosas graciosas al día te hace más feliz?» · El experimento · `H03`

- **Tesis:** apuntar cada noche, una semana, tres cosas que te hicieron gracia subió la
  felicidad frente a un placebo, y seis meses después todavía se notaba.
- **Según el lector:** «apuntar cada noche tres cosas que te hayan hecho gracia te hace más
  feliz, y según un estudio el efecto dura meses».

Los cinco «de qué va» dicen la misma idea que su `historia`.

### Variedad (C48.1)

- **Aperturas:** «Un paciente entra en la consulta» / «Tras la mampara» / «Tu amigo baja del
  autobús» / «Foto de grupo en una boda» / «Esta noche, antes de dormir». **Ninguna en primera
  persona.**
- **Cierres:** «Eso sí: …» / «O sea, que tu apuesta…» / «Así que el charco…» / «¿Y puede el
  fotógrafo…?» / «La letra pequeña: …». Ninguno empieza como otro ni como los cuatro anteriores
  (el validador no avisa).
- **Series:** tres «El experimento» (lunes, martes, viernes). No se fuerza la rotación; las
  secuencias de tipos de escena son distintas en los tres.

---

## 4 · Las fichas: usadas y evitadas

**Usadas como fuente central, ninguna lo había sido nunca:** `F07`, `D07`, `A03`, `F08`, `H03`.

- `A03` fue fuente de `MDS-003` el 26/08: la ventana de C17 se cierra el 07/10, **el mismo día de
  `MDS-033`**. El validador avisa porque mira desde hoy.
- `D07` salió de apoyo en `MDH-004` (3 de 31 escenas; la central era `E02`) y en `MDH-006` (una
  escena). Nunca fue central.
- `F07` es el mismo artículo que `F01`, que fue apoyo en `MDH-002` (19/08). `H03` fue apoyo en
  `MDH-001` (18/08). Las dos fuera de ventana.

**Evitadas a propósito:** `A06`, `A05` y `A07` (el tanteo de `MDS-022` se hace con `A03`);
`A10` (risa nerviosa, libre el 12/10); `E01`, `E02`, `E04` (risas enlatadas, libres el 10/10);
`A01`, otra vez, por ser la más gastada; `F03`, que se cayó tres veces el 25/09 en la misma
pregunta que ahora responde `F08` por otro lado; `H01` y `H02`, porque `MDS-028` fue hace una
semana; `K01`–`K04`, porque la IA descansa.

### Lo que se ha leído esta noche y cómo (regla del 15/09)

- **`F07`, `F08`:** su `resumen_verificado` en `semillas.json`, del 25/09. El guion no dice nada
  que no esté ahí.
- **`A03`:** solo la ficha. Su hallazgo está en el propio título («Finding humor in distant
  tragedies and close mishaps»). El guion no da ninguna cifra.
- **`H03` y `D07`: el resumen se ha leído como lo reproduce el buscador web**, no en la página de
  la revista, porque **el proxy del contenedor devuelve 403 a `doi.org`, `api.crossref.org`,
  `pubmed`, `pnas.org` y las editoriales.** La frase copiada está en `notas_humor` de cada guion,
  con de dónde sale. Es menos que lo que pide la regla y lo digo para que la revisión diaria lo
  compruebe antes de producir, si su entorno sí llega.

### Un error en la bibliografía, encontrado esta noche

**`D07` lleva un título que no es el de su DOI.** El DOI `10.1073/pnas.1524993113` es el de
Bryant y otros (2016), «Detecting affiliation in colaughter across 24 societies», PNAS —que es
el título que tiene `E05`, el duplicado de prueba—; `D07` dice «Convergent evidence that laughter
serves as a signal of cooperation and affiliation across societies». Su comentario («24
sociedades distinguen risa real de fingida») tampoco es exacto: lo que distinguen es amigos de
desconocidos. Lo de «real o fingida» es otro trabajo del mismo grupo. `MDS-032` cita `D07` y dice
solo lo que dice el resumen del de 2016. Además, `F06` y `F07` son el mismo artículo que `F02` y
`F01`.

---

## 5 · El corpus (paso 7, C39): no se ha podido ampliar

**El recuento.** Sin usar nunca como fuente central y con un hallazgo que copiar quedan `F03`,
`F06`, `H04`, `K01`, `K04` y `B03`: **seis**, y `B03` se ha caído dos semanas seguidas. Muy por
debajo de quince: tocaba añadir tres fichas.

**Por qué no lo he hecho, y son dos motivos, cada uno suficiente:**

1. **No llego a ninguna página donde ver juntos el título y el DOI** (la condición de C39). El
   proxy de salida bloquea `doi.org`, `api.crossref.org`, `pubmed.ncbi.nlm.nih.gov`, el
   repositorio de Europa PMC, OpenAlex y Semantic Scholar. Una ficha a partir de lo que resume
   un buscador es justo lo que C39 prohíbe.
2. **`entregar.py` no deja subir `01_bibliografia/` a la planificación** (su lista
   `planificacion` no la incluye), aunque el paso 7 de mi fichero dice que escriba en
   `01_bibliografia/data/semillas.json`. La semana pasada eso no se notaba porque iba en paquete.

Va a «Para el codirector».

---

## 6 · La lectura en frío (C48): diecisiete lectores, un tema caído

Cada lectura con un subagente nuevo, el encargo literal y sin avisarle de nada.

| Short | Vueltas | Qué cambió |
|---|---|---|
| `MDS-031` | 3 | Chiste nuevo: el del perro que sabe restar no se pillaba («nada» es cero) y dos lectores lo llamaron flojo; entra el del médico («que pase el siguiente»). Fuera la escena puente («algo que alguien ya midió»), que dos lectores llamaron vaga. Cierre reescrito. |
| `MDS-032` (B03) | 3, **no pasa** | Ver abajo. |
| `MDS-032` (D07) | 3 | «Se van juntos a desayunar» no se leía como «son amigos»; el cierre contradecía al principio («sabes» y luego «es suerte»). Ahora el principio es una apuesta y el cierre la resuelve. «Sociedades» → «culturas». |
| `MDS-033` | 2 | Un «pero» que anunciaba una contradicción que no había, y un cierre sin conclusión. |
| `MDS-034` | 3 | «De más adentro» (¿qué zonas?), el «tú» de «la pediste» cuando pide el fotógrafo, y «el repaso» del cierre. |
| `MDS-035` | 3 | «Placebo» con un ejercicio de escribir → «un ejercicio de relleno, para comparar»; el cierre, que no se sabía si era broma o pega. |

**El tema caído: «¿tener sentido del humor te hace más feliz?» (`B03`), por segunda semana.**
En tres vueltas los lectores marcaron siempre la escena del estudio: «otras cosas» (¿cuáles?),
qué es lo que «casi dejaba de importar», y en la tercera, qué hicieron los psicólogos con el
test («¿lo pasaron a gente o lo analizaron?»). El chiste funcionó las tres veces («eso no es
humor, es buen carácter»). El procedimiento dice que a la tercera se cambia de tema, y he
cambiado. **Propuesta:** que `B03` no se intente una tercera vez hasta que haya número de
demanda propio (va a las semillas) y, si se intenta, que sea con «El experimento» y una persona
concreta que hace el test, no con el test como sujeto. La versión caída está en mi carpeta de
trabajo y no se entrega.

**Criterio aplicado (C48.2, el ratificado el 28/09) en cuatro de los cinco:** las frases que el
lector copia en la pregunta 3 pero **interpreta bien él mismo** («tardé un segundo», «deduje
que…») van a `notas` y no bloquean. Las que no sabe interpretar («¿lo pasaron o lo
analizaron?») bloquean. Con ese criterio `MDS-032` (B03) no pasa y `MDS-035` sí: es el caso más
justo de la semana, y lo dejo dicho para que la dirección lo mire.

**Frases que el lector propuso quitar y se han quedado** (condición c), cada una con su motivo en
`lectura_en_frio.frase_que_sobra`: la escena 5 de `MDS-031` (es la mitad del hallazgo), «Wild no
lo responde» en `MDS-034` (es el límite honesto), «¿Lo sabes de verdad…?» en `MDS-032` (es el
«pero» entre la apuesta y el experimento) y el ejercicio de relleno de `MDS-035` (es el grupo
de comparación).

**Una explicación rival que dio un lector de `MDS-033` y el Short no descarta:** que en la cena
nadie se ríe porque «tenías que estar allí». Es razonable y el estudio no la mide; no la he
metido porque sería una segunda idea en un Short de cincuenta segundos.

**Patrón de las diecisiete lecturas, para quien escriba la semana que viene:** doce de los
diecisiete lectores dijeron que se habrían ido, o casi, **en la escena donde entra el nombre del
investigador** («ahí pasa de anécdota a clase»). En los cinco Shorts esa escena va ahora lo más
tarde y lo más corta posible, pero sigue ahí porque la firma es obligatoria (regla 2).

---

## 7 · Revisiones

`05_calendario/revisiones/` no tiene ninguna nota sobre un guion pendiente: todas son de
episodios ya producidos (`MDH-004` a `MDH-008`, `MDS-006` a `MDS-025`). No he aplicado ni
retirado ninguna. La nota de la revisión diaria de hoy sobre `MDS-030` (editado por la
excepción de 48 h) queda vista; su criterio —que el «de qué va» del lector tiene que ser la
`historia.pregunta`— es el que he aplicado yo también.

---

## Para el codirector

Por orden de urgencia. Nada de esto lo puedo hacer yo.

1. **El paso 7 (C39, ampliar el corpus) no se puede cumplir desde esta rutina, por dos lados.**
   (a) La red del entorno «Mecánica del Humor» bloquea `doi.org`, `api.crossref.org`, PubMed,
   Europa PMC, OpenAlex, Semantic Scholar y las editoriales (403 en el proxy), así que no hay
   página donde ver juntos título y DOI. (b) `entregar.py` no incluye `01_bibliografia/` en la
   lista de la planificación. Para que vuelva a funcionar hacen falta las dos cosas: añadir esos
   dominios a la política de red del entorno y `01_bibliografia/data/semillas.json` y
   `01_bibliografia/BIBLIOGRAFIA_CURADA.md` a la lista `planificacion` de `entregar.py`. O
   decidir que el corpus lo amplía otra tarea. **Quedan seis fichas libres con hallazgo**, y las
   cabezas de serie de la semana del 12 tiran de fichas que se liberan, no de nuevas: eso aguanta
   dos o tres semanas, no más.
2. **Duración contra lectura en frío.** Los dos Shorts con mejor retención del canal duran 41-42
   s; los cinco de esta semana estiman 52-54 s. Lo que los ha alargado son las frases que piden
   los lectores en frío. Si la dirección quiere los 42 s, la lectura en frío tiene que poder
   aceptar algo menos de explicación, o hay que contar una cosa menos por Short. No lo decido yo.
3. **`D07` tiene el título de otro artículo** (apartado 4). Corregir en `semillas.json`, y de
   paso retirar o marcar `F06` y `F07` como duplicados de `F02` y `F01`.
4. **`H03` y `D07`: resúmenes leídos vía buscador**, no en la revista. Si la revisión diaria
   tiene red, que los compruebe antes del martes 6 y el viernes 9.

## Lo que falta

- Ninguna ficha nueva (apartado 5).
- `MDH-008` sigue escrito, sin tocar y fuera de la parrilla.
- `MDS-032` y `MDS-035` no tienen número de demanda propio: se miden el jueves 8.
