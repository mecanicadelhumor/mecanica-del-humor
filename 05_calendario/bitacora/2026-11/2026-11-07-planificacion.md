**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación, reintento del sábado 7 de noviembre de 2026

El contenedor arrancó el **sábado 7 a las 22:07 UTC (23:07 de España)**. Es la ejecución de reintento
(paso 0 del bloque del 28/09). **Resultado: un Short más, `MDS-067`, el lunes 9.** Martes 10, sábado 14 y
domingo 15 siguen sin emisión.

```
$ git log --oneline -5 origin/main
6af3fb4 Visuales (C50): manifiestos y hojas de contactos
b9fe8b9 métricas 2026-11-07 (diaria)
c0b3dab métricas 2026-11-07 (diaria)
f529152 revisión diaria 2026-11-07
4484b39 Visuales (C50): manifiestos y hojas de contactos

$ git ls-remote origin 'refs/heads/claude/entrega-*'
73c4b17… refs/heads/claude/entrega-revision-20261104-1031   (de la revisión, no mía)
```

---

## 0 · Por qué he trabajado hoy (paso 0)

- Hoy es **sábado** en España, así que toca el paso 0: el **lunes siguiente es el 9/11**.
- `parrilla.json` en `origin/main` **no tenía emisión el lunes 9**: el jueves 5 lo dejó vacío a propósito,
  con el martes 10, el sábado 14 y el domingo 15 (tres aprobados de catorce temas).
- **No hay ninguna rama `claude/entrega-planificacion-*`** (la del jueves ya está en `main`, commit `0958ad5`).
- Leído al pie de la letra, el paso 0 dice «la semana no está hecha: trabaja como si fuera jueves». Lo he
  leído así, pero **sin planificar dos veces**: no he tocado nada de lo que hizo el jueves (`MDS-064`,
  `MDS-065`, `MDS-066`, sus brazos y sus fechas). **Solo he intentado llenar los cuatro días vacíos.** Lo
  que pidió el codirector el 02/11 («un día sin vídeo es información que no tenemos») es justo eso.
- **Si la dirección prefiere que el reintento no toque una semana ya entregada** con huecos a propósito, el
  paso 0 debería decir «emisión el lunes **o** bitácora de planificación de esa semana». Lo dejo en
  sugerencias.

## 1 · El bucle (C60)

`resultados.json` (18:21 UTC del 07/11): **B2 todavía sin un solo dato** (control, A, D y AD con n = 0;
todas las comparaciones «faltan datos»). Referencia anterior: n 14, «se quedaron» 31,7 %. No decido nada.

**Los cuatro huecos son brazos cortos**: lunes 9 = D (5), martes 10 = AD (6), sábado 14 = D (10), domingo
15 = AD (11). Así que **esta noche todos los guiones se han escrito con cinco escenas y 45 s como mucho**, y
la lectura en frío se ha hecho sobre esa versión, la que sale (receta de `ciclos.json`). En `notas_humor`
cada guion dice qué escena tendría una versión de seis. No ha sido ciego del todo: sabía que los cuatro
huecos eran cortos antes de elegir temas, y no había otra forma de llenarlos.

## 2 · Lo que se ha escrito, y la lectura en frío con tres lectores

**Siete temas, 60 lecturas (veinte vueltas de tres), un aprobado.** Encargo literal de `guionista_corto.md`,
tres subagentes nuevos por vuelta (modelo `sonnet`, como el jueves), decide la mayoría. Criterio igual que el
jueves: bloquea lo que dos de tres copian diciendo que no lo entendieron o que lo entendieron tarde; «lo
entiendo, pero…» va a `notas`; la firma de la fuente siempre a `notas`.

| Tema (ficha) | Hueco previsto | Vueltas | Resultado |
|---|---|---|---|
| El emoji del banco (`I22`, reserva) · *mensajes* | lun 9 · D | 3 | cae (2.ª semana) |
| La risa floja y las cosquillas (`F14`, reserva) | mar 10 · AD | 3 | cae (3.ª semana) |
| Mirar el móvil mientras te hablan (`I19`, reserva) · *mensajes* | sáb 14 · D | 3 | cae (2.ª semana) |
| ¿Son más listos los cómicos? (`C05`, reserva, historia nueva) | dom 15 · AD | 2 | cambiado de tema |
| Reírse a la vez con amigos (`E17`, nuevo) | dom 15 · AD | 3 | cae |
| El «Qué bien» sin emoji (`D10`, nuevo) · *mensajes* | lun 9 · D | 3 | cae |
| **La ironía por WhatsApp (`I08`, nuevo) · *mensajes*** | **lun 9 · D** | **3** | **pasa → `MDS-067`** |

**`MDS-067`** · Tesis: para la ironía escrita la gente usa sobre todo la carita de la lengua y la del guiño;
los puntos suspensivos van más con el reproche. · Lectores (vuelta 3): «cómo marcar la ironía en un
mensaje escrito: la gente usa sobre todo la carita de la lengua o la del guiño, y los puntos suspensivos
suenan más a reproche» (los tres, casi igual). Los tres: «me quedo». Las tres respuestas, el recuento y el
historial de vueltas están en `lectura_en_frio`. **`validar_guion.py`: sin errores ni avisos, 45,0 s.**

**Lo que se repite en las 60 lecturas** (para quien escriba el jueves 12):

1. **La escena del método es la que cae.** Pasa cuando cuenta qué tuvo delante la gente y qué tenía que
   hacer, con un objeto de la historia («frases como ese «Qué puntual»… hacerlas irónicas solo con caritas
   o signos»). Cae cuando el resumen no dice el método y hay que contarlo en abstracto («compararon a
   quien…», «preguntaron qué impresión daba», «un test de palabras»): el lector pregunta «¿quién juzgaba?,
   ¿en vivo o en vídeo?, ¿cada uno veía una versión o las dos?». **Con resúmenes de tres líneas, eso no
   tiene arreglo en el guion: hace falta el artículo.**
2. **La salvedad del cierre bloquea si no dice qué cambia para el espectador.** «Eran mensajes
   imaginados», «eran charlas de experimento, no rupturas», «eran juegos de un rato» cayeron (2-3/3). Pasó
   «vieron qué ponemos, no si tu amiga pillará la broma»: dice qué no se midió con el sujeto del Short.
3. **«Lo peor de las dos cosas», «la peor carita posible», «lo más fuera de lugar», «es lo normal», «es
   eso»**: cualquier cierre que resume con una etiqueta en vez de repetir la idea cae.
4. **Los rótulos telegráficos siguen cayendo** («Cosquillas antes y después», «La misma frase · Sin
   cambiar palabras», «Sin tocar las palabras»). Pasó «Solo podían añadir caritas o signos» (con verbo).
   Confirma el `H-rotulo-con-verbo` del jueves.
5. **Con cinco escenas y el dato delante (brazo B), la escena 4 repite la 1**, y casi todos los lectores
   la proponen como la frase que sobra. No bloquea, pero deja menos sitio al método. Cinco escenas y 45 s
   es muy justo para un estudio de dos factores (`I22`).

**Variedad (C48.1):** `MDS-067` no abre en primera persona; el cierre empieza «A tu amiga, entonces…», que
no repite a ninguno de los cuatro anteriores. **Etiqueta `chiste`:** `otro`.

## 3 · Demanda, actualidad y fichas

- **La demanda medida no ha cambiado desde el jueves** (no hay medición nueva; `demanda.json` y
  `semillas_demanda.json` no los toco). Esta noche no ha decidido la demanda: ha decidido la lectura en frío.
  La ironía por escrito es la familia de `MDS-016` (el mejor del canal) y del `R-TE-03`.
- **Actualidad (C52):** no he buscado gancho para un hueco suelto; ninguno de los temas lo lleva.
- **Fuente central:** `I08` (Thompson y Filik, 2016), nunca central; **resumen releído hoy en OpenAlex**
  (título y DOI en el mismo registro) y frases copiadas en `notas_humor`. También releí hoy el de `I19`.
  **Evitadas por repetición:** las mismas del jueves (`F10`, `F15`, `F19`, `I11`, `E07`). `I05` (la ironía
  de `MDS-016` y `MDS-040`) no se usa: `I08` es otro estudio.
- **Corpus (paso 7):** no he añadido fichas. El jueves añadió once (meta de diez cumplida esta semana).

## 4 · Revisiones

- **`revisiones/MDS-063.md`** (06/11, un lector): propone fundir las escenas 2 y 3. **No la aplico**:
  `MDS-063` sale mañana domingo 8 como **control** de B2, que son seis escenas; con cinco sería un D y el
  Short dejaría de medir lo suyo. Además es un guion ya escrito (regla 11.4) y la nota la escribió un solo
  lector («orientación, no veredicto»). No la retiro, para que la dirección la vea.
- **`revisiones/MDS-062.md`**: igual que el jueves (brazo A, no se aplica, no se retira).

## 5 · Lo que he tocado

`05_calendario/guiones/MDS-067.es.json`, `05_calendario/publicaciones/MDS-067.es.json`,
`05_calendario/parrilla.json` (una emisión nueva, lunes 9; nada más), `05_calendario/CALENDARIO.md` (la fila del
lunes 9 y un párrafo), `05_calendario/temas_en_reserva.md` (seis líneas nuevas), esta bitácora y
`08_comunicacion/2026-11/2026-11-07-planificacion.md`.

---

## Para el codirector

1. **Siguen tres días sin Short la semana que viene: martes 10, sábado 14 y domingo 15** (posiciones 6, 10
   y 11 de B2, las tres cortas). Esta noche se intentaron siete temas y pasó uno. Con lo del jueves, la semana
   va **4 de 21 temas** con tres lectores y mayoría.
2. **El cuello de botella ya no es la escritura: son los resúmenes.** Cuatro de los seis temas caídos se
   cayeron por la escena del método, y el método no estaba en el resumen (`I19`, `C05`, `I22`, `D10`). Con
   el **texto completo** del artículo (no solo el resumen) esa escena se podría contar. Si la red lo permite,
   sería bueno que las fichas guardaran también **una línea del método** (quién, qué vio, qué contestó),
   copiada del artículo. Eso es trabajo del corpus (mío) pero necesita acceso al texto, que hoy no tengo de
   forma fiable.
3. **Los brazos cortos (D y AD) son más difíciles de llenar que los largos**: en 45 s, con el dato delante,
   la escena 4 repite la 1 y el método tiene que caber en una frase. Esta noche: un aprobado de siete, y los
   siete eran cortos. Es información para B2 (quizá el factor «corto» también mide lo difícil que es escribir
   corto), no una queja.
4. **El paso 0 del reintento** se puede leer de dos maneras cuando el jueves deja huecos a propósito (ver el
   apartado 0). Lo he leído para llenar huecos sin tocar lo hecho; si no es lo que quiere la dirección, una
   línea en el prompt lo arregla.
5. **La rama `claude/entrega-revision-20261104-1031`** sigue viva; no es mía y no la toco.

## Sugerencias a la dirección

- **`H-metodo-en-la-ficha`:** que cada ficha nueva lleve un campo `metodo_verificado` (una frase copiada del
  artículo: quién participó, qué vio o hizo, qué contestó). Regla afectada: la del 15/09 («se copia, no se
  deduce»), ampliada al método. Se mediría con la tasa de aprobados en la lectura en frío.
- **`H-salvedad-con-sujeto`** (complementa la del jueves): la salvedad del cierre dice qué no se midió
  **con el sujeto del Short** («no si tu amiga pillará la broma»), no con una etiqueta del estudio
  («mensajes imaginados»). Regla afectada: R-GU-07.
- **Paso 0 del reintento:** «emisión el lunes **o** bitácora de planificación de esta semana en `main`»
  si la dirección no quiere que el reintento rellene huecos.

## Lo que falta

- **Tres días vacíos** (martes 10, sábado 14, domingo 15).
- **El banco sigue vacío.**
- **Familia `mensajes`: uno** esta semana (`MDS-067`); la regla pide dos.
- **El largo `MDH-008`** no lo he tocado: es de la dirección hasta el estreno.

## Respuesta del codirector
