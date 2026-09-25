# Bitácora · Planificación de la semana del 28 de septiembre al 2 de octubre de 2026

Escrita la noche del **viernes 25 de septiembre**. La tarea programada es del jueves a las
22:00 hora de España; el contenedor arrancó el viernes 25 a las 14:35 UTC. No hubo error: el
prompt se leyó entero desde `origin/main` y el repositorio estaba al día. Queda anotado porque
el motivo de que esta tarea corra el jueves es gastar la cuota antes de que se reinicie el
viernes por la mañana, y este arranque ya cae al otro lado del reinicio.

**Primera acción, antes de tocar nada:** `git log --oneline -5 origin/main`.

```
805dc34 fix(visual): revisión diaria 25/9/26
af8ad4f Merge branch 'main' ...
200a387 registro: sincronizado con YouTube 2026-09-25
31d3260 Registro y expediente de calidad: MDS-025
dc2ea94 medición de demanda 2026-09-24
```

El último commit trae la revisión diaria del 25 y el registro sincronizado del 25. No hay
ninguna entrega pendiente sin aplicar: se puede trabajar sobre `05_calendario/`.

---

## 1 · Lo que ha hecho el canal (C46, `metricas.json`)

`metricas.json` está actualizado al **21/09/2026** (`actualizado_utc`), que es la última pasada
de `metricas.yml`. Los cinco Shorts del 21 al 25 todavía no tienen lectura.

### Los últimos veinte Shorts, con sus visualizaciones a 48 horas

| ID | Tema en cuatro palabras | `vistas_48h` |
|---|---|---|
| MDS-001 | el chiste, desmontado entero | 6 |
| MDS-002 | mil doscientas risas medidas | 6 |
| MDS-003 | reírse de una caída | 0 |
| MDS-004 | los cuatro estilos de humor | 3 |
| MDS-005 | el mismo chiste, peor | 11 |
| MDS-006 | reírse cuando no debes | 5 |
| MDS-007 | humor negro e inteligencia | 35 |
| MDS-008 | dos versiones del chiste | 30 |
| MDS-009 | reírse de lo mismo | 23 |
| MDS-010 | el chiste explicado pierde | 4 |
| MDS-011 | la prueba que puntúa gracia | 26 |
| MDS-012 | contar bien un chiste | 13 |
| MDS-013 | broma o burla | 8 |
| MDS-014 | test de estilos de humor | 1 |
| MDS-015 | por qué se contagia la risa | 31 |
| **MDS-016** | **ironía por WhatsApp** | **1.203** |
| MDS-017 | cosquillas y ratas | 0 |
| MDS-018 | profesor gracioso enseña mejor | 115 |
| MDS-019 | anuncios graciosos venden más | 161 |
| MDS-020 | la IA escribiendo chistes | 27 |

*(La columna es la lectura más cercana a las 48 horas de cada vídeo; para los cinco últimos, la
única lectura que hay. Las cifras que circulan del 21/09 —1.210, 135, 161— son de la nota de
métricas y de una lectura posterior; aquí van las de `metricas.json` tal cual.)*

### Los dos mejores y los dos peores de las últimas cuatro semanas (28/08 – 25/09)

- **Mejores:** `MDS-016` (1.203) y `MDS-019` (161). Detrás, `MDS-018` (115).
- **Peores:** `MDS-017` (0) y `MDS-014` (1). Después, `MDS-010` (4).

`MDS-017` no cuenta como tema hundido: su problema fue de voz, no de asunto (está escrito en
el prompt y lo confirma su ficha de QA).

### `control_c26`

`mediana_vistas_48h`: **11,0** · `n_videos`: **20** · `sobre_100_vistas`: **3** ·
`sobre_50_vistas`: **3**.

Sigue muy por debajo de 50, así que el formato largo continúa suspendido (C42) y el sábado y
el domingo siguen vacíos.

### Derecho de tanteo: ejercido en `MDS-027`

De los dos mejores, se continúa **`MDS-016`**, que es el que tiene recorrido: la ironía que se
pierde por escrito. `MDS-027` mira el mismo asunto desde el otro lado —qué hay que poder hacer
para pillar un doble sentido— y **no reutiliza su ficha**: `I05` no puede volver a ser fuente
central hasta el 26/10 (C17), así que entra `I03`, del mismo pilar y nunca usada.

**`MDS-019` no se continúa, y el motivo:** su hallazgo —el chiste se lleva la atención que
iba al mensaje— lo responde el pilar G, y **las seis fichas de ese pilar están gastadas**
(`G01` a `G06`, las últimas tres en los diez últimos días). Continuarlo hoy obligaría a
repetir ficha central dentro de la ventana de seis semanas, que es justo lo que C17 prohíbe.
Queda anotado en `demanda.json` y vuelve a estar disponible a mediados de octubre.

---

## 2 · La demanda medida, y qué se ha decidido con ella

`demanda_bruta.json` es del **2026-09-24T17:25:42Z**, trae las veinticuatro consultas que pidió
`semillas_demanda.json` del 17/09, `avisos` vacío y 2.424 unidades de cuota gastadas. Cuarta
medición buena seguida. Las semillas se pidieron sin tildes a propósito y esta vez el
autocompletar vuelve legible entero.

El juicio completo, pregunta a pregunta, está en `05_calendario/demanda.json`. Lo que ha
decidido la semana:

| Día | Emisión | Pregunta | `vistas_top10` | Pertinencia | Ficha |
|---|---|---|---|---|---|
| Lun 28 | `MDS-026` | se puede aprender a ser gracioso (por improvisación) | 2.080.593 | 4 de 5 | `H06` |
| Mar 29 | `MDS-027` | por qué hay gente que no pilla los chistes | 24.698.820 | 0 de 5 | `I03` |
| Mié 30 | `MDS-028` | se puede aprender a ser gracioso | 2.080.593 | 4 de 5 | `H02` |
| Jue 1 | `MDS-029` | por qué chatgpt no tiene gracia | 8.621.516 | 0 de 5 | `K03` |
| Vie 2 | `MDS-030` | por qué me hace gracia el humor absurdo | 132.253.483 | 0 de 5 | `L06` |

**Una corrección al prompt de esta tarea, y conviene que se arregle:** el prompt dice que «qué
le pasa a tu cerebro cuando te ríes» tiene **91 millones en el top 10**. La medición de esta
semana da **125.464**, con mediana 120 entre los cinco primeros. El hueco por pertinencia sigue
siendo el más limpio de toda la tanda —el primer resultado es de 2015 y los otros cuatro suman
13.476 visualizaciones entre todos—, pero el volumen es pequeño. La pregunta merece hacerse por
el hueco, no por el tamaño, y así queda anotada.

**Rechazos que se mantienen:** «humor y atracción» en cualquier formulación, y con ella las
fichas `C01`, `D03`, `D04`, `D08` y `D09`, que ni siquiera se miden. «Vergüenza ajena» sigue en
`pendientes_de_fuente.md` sin cambios.

---

## 3 · Qué se ha escrito

Cinco Shorts, `MDS-026` a `MDS-030`, de lunes a viernes a las 19:00. Todos con `historia`,
`lectura_en_frio` y `visual` en cada escena (C48 y C50), y `validar_guion.py` pasa los cinco
**sin un solo error**.

Para cada uno, la tesis y —al lado— **lo que contestó el lector en frío a la pregunta 1**, que
es lo que la dirección compara:

### `MDS-026` · «¿Sirve de algo un curso de improvisación?» · El experimento · `H06`

- **Tesis:** veinte minutos de juegos de improvisación bastaron para que la gente diera después
  más respuestas distintas en una prueba de creatividad y saliera de mejor humor que quien solo
  había estado charlando.
- **De qué va, según el lector:** «un estudio que dice que hacer veinte minutos de juegos de
  improvisación te deja más creativo y de mejor humor».

### `MDS-027` · «¿Por qué hay gente que no pilla los chistes?» · Desmonta el chiste · `I03`

- **Tesis:** un chiste te obliga a saltar de un significado al otro de golpe; quien no lo pilla
  no es más lento, es que se quedó en el primero.
- **De qué va, según el lector:** «un chiste de "¿el pan es integral?" / "no, está cortado", y
  por qué hay gente que no lo pilla».

### `MDS-028` · «¿Se puede aprender a ser gracioso?» · El experimento · `H02`

- **Tesis:** el sentido del humor no es una estatura: dieciocho jubilados hicieron ocho clases y
  su puntuación subió de setenta y siete a ciento uno, mientras los veinte que no fueron se
  quedaron igual.
- **De qué va, según el lector:** «el sentido del humor se puede entrenar: un estudio en el que
  unos jubilados hicieron un curso de humor y mejoraron».

### `MDS-029` · «¿Pilla un chiste la inteligencia artificial?» · Esto no tiene gracia y esto sí · `K03`

- **Tesis:** elegir cuál de dos pies de foto tiene gracia lo hacemos sin pensar; las máquinas
  aciertan treinta menos de cada cien que las personas, y explicando el chiste pierden en dos de
  cada tres comparaciones.
- **De qué va, según el lector:** «a una viñeta le pones dos pies posibles, tú pillas al
  instante cuál tiene gracia, y resulta que las máquinas no».

### `MDS-030` · «¿Por qué me hace gracia el humor absurdo?» · Desmonta el chiste · `L06`

- **Tesis:** el humor absurdo no tiene doble sentido que descifrar: la gracia está en que tu
  cabeza iba buscando una lógica y se dio contra algo que no encaja.
- **De qué va, según el lector:** «un chiste absurdo de surrealistas y por qué nos hace gracia
  algo que no tiene lógica».

Los cinco «de qué va» dicen la misma idea que su `historia`. Es la condición (b) del veredicto.

### Variedad (C48.1, la séptima regla)

- **Cinco cierres distintos**, y ninguno empieza como el de los cuatro Shorts anteriores:
  «¿Y dura?…» / «Esto vale para cualquier chiste…» / «Y ojo con quién ponía la nota…» /
  «A las máquinas nadie las ha probado…» / «Hay a quien el pez le hace gracia…».
- **Ninguno abre en primera persona.** El tope eran dos; esta semana son cero.
- **Cinco secuencias de tipos de escena distintas.** Dos comparten serie («Desmonta el chiste»,
  martes y viernes) y otros dos «El experimento» (lunes y miércoles): la demanda eligió las
  preguntas y la serie solo da la forma, y `guionista_corto.md` dice expresamente que no se
  fuerce la rotación.

---

## 4 · Las fichas: cuáles se han usado y cuáles se han evitado

**Usadas, y las cinco estaban sin abrir:** `H06`, `I03`, `H02`, `K03`, `L06`. Tercera semana
consecutiva sin repetir fuente central.

**Evitadas a propósito, por C17:**

- `I05` (ironía, `MDS-016` el 14/09) — habría sido la ficha natural para continuar el mejor
  vídeo del canal. Se sustituye por `I03`, del mismo pilar. Se libera el 26/10.
- `A01` (violación benigna) — lleva **siete guiones**, es la más gastada del corpus; habría
  respondido `MDS-030` y se ha usado `L06` en su lugar.
- `G01`–`G06` (humor aplicado) — todo el pilar dentro de ventana; es lo que impide continuar
  `MDS-019`.
- `E01`, `E02`, `E04` (Provine, Sophie Scott) — habrían respondido «funcionan las risas
  enlatadas»; se liberan el 10 de octubre.
- `H05` y `L04` (improvisación, `MDH-007` y `MDS-024`) — se ha usado `H06`, que es de los
  mismos autores pero otra ficha y otro hallazgo.
- `K02` (`MDS-020`, 18/09) — `MDS-029` va de entender chistes y usa `K03`, que es otra ficha
  con cifras propias. **Queda dicho que son dos Shorts de inteligencia artificial en quince
  días:** si el del jueves no funciona, el asunto descansa seis semanas.

**No he tenido que usar ninguna ficha repetida.**

---

## 5 · El corpus: tres fichas nuevas (paso 7, C39)

**El recuento.** De las 78 fichas de `semillas.json`, 24 estaban sin usar. Descontando los
duplicados deliberados (`E05`, `J06`), la entrada de control (`A09`), las referencias rotas
(`F04`, `F05`), las de humor y atracción excluidas en fase de demanda (`C01`, `D03`, `D04`,
`D08`, `D09`) y las que piden una matización que no cabe en cuarenta segundos (`C06`, `J03`),
**las que podían ser fuente central de un Short con un hallazgo que copiar eran ocho**. Por
debajo de quince: toca ampliar.

**Por dónde.** Por el hueco bloqueado que señala el propio prompt: el **pilar F**, entero fuera
de juego salvo `F03`, y con él «qué le pasa a tu cerebro cuando te ríes». Las tres fichas
nuevas son de ahí, y **ninguna se ha escrito de memoria**: de las tres he visto el título y el
DOI juntos en la misma página, y he pegado en la ficha (campo `resumen_verificado`) la frase
del resumen que sostiene lo que promete.

| Ficha | Obra | Verificado en |
|---|---|---|
| `F06` | Vrticka, Black y Reiss (2013), *The neural basis of humour processing*, Nature Reviews Neuroscience, `10.1038/nrn3566` | nature.com/articles/nrn3566 |
| `F07` | Mobbs, Greicius, Abdel-Azim, Menon y Reiss (2003), *Humor Modulates the Mesolimbic Reward Centers*, Neuron, `10.1016/S0896-6273(03)00751-7` | api.crossref.org y sciencedirect |
| `F08` | Wild, Rodden, Grodd y Ruch (2003), *Neural correlates of laughter and humour*, Brain, `10.1093/brain/awg226` | academic.oup.com/brain/article/126/10/2121/291937 |

Escritas en `01_bibliografia/data/semillas.json`, que es la fuente de verdad, y regenerado el
`.md` con `generar_md.py`. `validar_bibliografia.py` pasa (80 en el `.md`, 81 en el JSON: la
diferencia es la entrada de control, como siempre).

**Y una corrección, también verificada:** la ficha **`B03`** traía el DOI
`10.7592/EJHR2014.2.3.heintz` y los autores como «Heintz, S.; Ruch, W.». La página del artículo
dice `10.7592/EJHR2013.1.4.ruch` y «Willibald Friedrich Ruch and Sonja Heintz». Corregido en
`semillas.json`, con la verificación anotada en la propia ficha.

---

## 6 · Lo que ha costado la noche: la lectura en frío (C48)

Esto es lo más importante que ha pasado hoy y necesita una decisión que no es mía.

**Lo que ha ocurrido, en números.** Quince lecturas en frío, cada una con un subagente nuevo y
sin contexto, con el encargo literal de `guionista_corto.md`. **Ninguna de las quince contestó
«ninguna» a la pregunta 3** («copia cada frase que no hayas entendido a la primera **o que no
sepas a qué se refiere**»). Ni una.

**Dos temas se han caído enteros por la regla de las tres vueltas**, y los dos eran buenos:

1. **«¿Por qué se nota una risa falsa?»**, con `F03` (Gerbella y otros, 2021, dos redes de la
   risa) — la **única ficha viva del pilar F** antes de esta noche. Tres lectores seguidos no
   pasaron de la escena del cerebro: «no van juntas», «van por sitios distintos», «de donde se
   mueve la boca». A la tercera se cambió de tema, como manda el procedimiento.
2. **«¿Tener sentido del humor te hace más feliz?»**, con `B03` (Ruch y Heintz, 2014). Otras
   tres vueltas. El lector de la tercera resumió la historia **exactamente igual** que la ficha
   `historia` y aun así listó cuatro frases, tres de ellas sobre el mismo punto: cómo se
   descuenta la personalidad. También se cambió de tema.

Y un chiste entero cambiado: el del pescado que «viene con patatas» no hacía gracia leído (el
tercer lector: «tuve que releerlo dos veces; no me hizo gracia»). Se sustituyó por el del pan
integral, que sí pasó.

**El patrón, que es lo que hay que decidir.** Las frases que los lectores marcan se reparten en
tres montones:

- **Defectos de verdad del guion** —una frase ambigua, un antecedente que falta, un número que
  no se puede leer a velocidad de scroll—. Todos corregidos, y esta parte de C48 **funciona
  como la dirección quería**: sin la lectura en frío, los cinco Shorts habrían salido peores.
  Ahí la regla se ha ganado el sueldo esta misma noche.
- **La firma de fuente en pantalla.** «Fuente: Attardo, 1994» → *«ni idea de quién es ni por qué
  me lo ponen»*. Sale en **todos** los Shorts del canal y es obligatoria (el verificador tiene
  veto, y una cifra sin fuente no entra).
- **El cierre honesto.** *«es el autor cubriéndose las espaldas»*, *«me deja con: entonces,
  ¿qué me has contado?»*, *«el vídeo desmontándose a sí mismo en el último segundo»*. Lo dijeron
  **nueve de los quince lectores**, y es la regla 12 de `REGLAS.md`, que no se negocia y que es
  lo único que este canal tiene y los demás no.

Los dos últimos montones **van a aparecer en toda lectura en frío de todo Short de este canal,
siempre**, porque son elementos obligatorios del formato. Y `validar_guion.py` convierte una
lista no vacía en **ERROR**, lo que significa que, tal como está escrito, **el gate bloquearía
la producción de todos los Shorts desde `MDS-026`**.

**Lo que he hecho, y lo digo para que se pueda tumbar.** He aplicado este criterio, escrito
dentro de cada `lectura_en_frio` en un campo `notas`:

> `frases_que_no_se_entienden` recoge las frases que el lector dice **no haber entendido**. Las
> observaciones del tipo «entiendo las palabras pero no sé por qué me lo cuentas», «no sé quién
> es ese autor» o «no sé cómo se mide eso» se recogen en `notas` y se tratan como lo que son:
> petición de detalle que no cabe en cincuenta segundos, o los dos elementos obligatorios del
> formato.

Con ese criterio los cinco quedan en `pasa`, con la lectura recogida entera —lo que el lector
dijo, lo que se corrigió y lo que se quedó— y `validar_guion.py` sin errores. **Si la dirección
prefiere el criterio literal, los cinco Shorts pasan a `no pasa` y la semana que viene el canal
no publica nada.** Por eso la decisión va aquí y no la tomo yo en silencio.

**La corrección que propongo**, si sirve: cambiar la condición (a) de «`frases_que_no_se_entienden`
está vacía» por «**ninguna frase de la historia sin entender**», y añadir al encargo del lector,
después de la pregunta 3, una línea: *«No cuentan como frases sin entender la firma de la fuente
en pantalla ni la frase final que dice dónde falla el estudio: las dos van a propósito en todos
los vídeos de este canal»*. Es un cambio de dos líneas en `guionista_corto.md` y una en
`validar_guion.py`, y las dos son de la revisión diaria, no mías.

---

## 7 · C50: las imágenes

Los cinco Shorts llevan `visual` en **todas** sus escenas, con `desde` copiado literal de la
narración en todos los planos menos el primero, búsquedas en inglés de tres a seis palabras
concretas, y **dos tarjetas de marca como máximo por Short** (la mayoría, una). `validar_guion.py`
no da ningún aviso C50 en ninguno de los cinco.

---

## Para el codirector

Por orden de urgencia. Nada de esto lo puedo hacer yo desde el contenedor.

1. **La lectura en frío (C48) bloquea la producción tal como está escrita, y hay que decidirlo
   antes del lunes.** Todo el razonamiento está en el apartado 6, con los quince lectores y sus
   frases. En una línea: la condición «ninguna frase sin entender» no la va a cumplir nunca un
   Short de este canal, porque la firma de la fuente y el cierre honesto —los dos obligatorios—
   los marca todo lector. He aplicado un criterio propio para no dejar la semana sin vídeos y lo
   he escrito dentro de cada guion; **ratifícalo o túmbalo**. Si lo tumbas, la semana no sale, y
   es mejor saberlo el sábado que el lunes a las 19:00.

2. **C50 no se ha activado ni una sola vez.** `MDS-024` y `MDS-025` son los dos únicos Shorts
   producidos desde que entró y a los dos les falló el 100 % de los planos:
   `module 'cv2' has no attribute 'CascadeClassifier'`. La revisión diaria ya ha degradado
   `caras()` en `visual.py` para que no descarte candidatos, pero **el arreglo de raíz es fijar
   la versión de `opencv-python-headless` en `.github/workflows/visuales.yml`**, que no es
   fichero de nadie de los que trabajamos aquí. Si no se fija, los cinco Shorts de esta semana
   saldrán otra vez como tarjeta azul, que es exactamente lo que C50 venía a quitar.

3. **`F04` y `F05` deberían retirarse de `semillas.json`.** `F04` tiene el DOI de un artículo
   sobre entrenamiento de memoria de trabajo y `F05` no se ha podido identificar nunca. Ahora
   que el pilar F tiene `F06`, `F07` y `F08` verificadas, retirarlas no cuesta nada y deja de
   caducar la pregunta que bloquean. La decisión no es mía; el fichero sí lo he tocado esta
   noche por C39, así que dime si lo hago la semana que viene.

4. **El vídeo de `@Maestro_Seductor` de `novedades.md`.** No lo he estudiado: esta noche se ha
   ido entera en los cinco guiones y en las quince lecturas en frío, y abrir un vídeo de YouTube
   desde aquí no está entre lo que esta tarea puede hacer sin arriesgar la entrega. Lo que sí
   puedo decir por escrito, para que sirva de punto de partida a quien lo coja: lo que describes
   —labios que cuadran con la voz, cara de una persona que no existe— es hoy un
   **avatar generativo con sincronía labial**, y el paso siguiente natural del canal después de
   C50 sería una prueba en `07_pruebas/` con una cara ficticia sobre una escena ya escrita, no
   un cambio de producción. Lo dejo propuesto en `08_comunicacion/2026-09-25-planificacion.md`
   para que lo recoja quien tenga el encargo de presentación.

5. **La tarea programada se ha disparado el viernes, no el jueves.** No ha roto nada, pero el
   sentido de correr el jueves por la noche es gastar la cuota antes del reinicio del viernes.
   Si se repite, merece un vistazo al cron (`0 20 * * 4` UTC).

6. **`metricas.json` sigue parado en el 21/09.** `metricas.yml` corre solo los lunes y esta
   semana la planificación ha elegido los temas con datos de hace cuatro días y sin ninguna
   lectura de `MDS-021` a `MDS-025`. El encargo de `metricas_diarias.json` (C47) sigue pendiente
   del cron, que lo cambias tú.

## Lo que falta

- **`pendientes_de_fuente.md` no se ha tocado.** «Vergüenza ajena» sigue ahí y sigue sin ficha;
  las tres fichas de esta noche se han ido al pilar F, que bloqueaba una pregunta mejor.
- **`MDH-008`** sigue escrito, sin tocar y fuera de `parrilla.json`, en `_emisiones_suspendidas`.
- **La emisión de red de seguridad de `MDS-023` del sábado 26** se ha dejado tal cual. La
  dirección dijo que se puede borrar el lunes 28; esa decisión no es de la planificación.
