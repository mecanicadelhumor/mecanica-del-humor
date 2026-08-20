# Mejora visual progresiva

Los dos primeros vídeos son correctos y austeros. Correcto no basta: en un canal
donde la voz es sintética y la cara no existe, la imagen es lo único que sostiene
la atención entre un dato y el siguiente. Este documento es la lista de lo que hay
que mejorar, en orden, y las reglas para hacerlo sin romper lo que ya funciona.

No se toca todo a la vez. Un cambio por vídeo, verificado antes de publicarse.

---

## La restricción que manda sobre todo lo demás

`render.py` no graba un vídeo: **captura solo los fotogramas en los que algo se
mueve** y deja que FFmpeg estire los tramos quietos. Un episodio de siete minutos
necesita unas 2.000 capturas en vez de 13.000, y por eso una producción entera
cabe en los minutos gratuitos de Actions.

Cada escena tiene tres tramos:

| Tramo | Qué pasa | Coste |
|---|---|---|
| Entrada | las unidades aparecen escalonadas (0,16 s de desfase) | ~1 captura por fotograma |
| **Centro** | **nada se mueve: una sola captura estirada** | ~0 |
| Salida | la escena se va | ~1 captura por fotograma |

**Consecuencia práctica:** todo lo que se anime *durante el centro* multiplica el
coste del render. Las mejoras del nivel 0 y 1 son gratis porque ocurren en la
entrada, que ya se captura. Las del nivel 2 hay que medirlas antes de adoptarlas.

~~Lo que sí da vida al tramo central sin coste: los **subtítulos quemados palabra a
palabra**, que se aplican en `montaje.py` sobre el vídeo ya renderizado.~~

**Ya no.** El 20/08, viendo MDH-003.es terminado, Silvestre decidió quitarlos:
palabra a palabra y sobre un diseño que ya es tipográfico, distraen más de lo que
aportan. Los subtítulos de verdad los sube `publicar.py` a YouTube como pista
aparte, así que la accesibilidad no se pierde —se gana: se pueden traducir,
buscar y leer al tamaño de cada uno—.

Lo que sí se pierde es lo otro: **el tramo central de cada escena vuelve a estar
completamente quieto.** Era el único movimiento que había ahí y era gratis. Eso
cambia las prioridades de este documento: los ítems de animación de la entrada
(V5, V6, V7) dejan de ser adorno y pasan a ser lo que sostiene la atención, y V8
—el acento a mitad de escena, el único que anima el tramo central— pasa de
«sin decidir» a merecer la medición de coste que pide, porque ahora no compite
con nada.

---

## Backlog, por orden de valor sobre riesgo

### Nivel 0 — mejor imagen, cero coste de render

**V1. Gráficas de verdad (`tipo: figura`).** ~~No existe quien las genere.~~
**Hecho el 19/08.** `03_produccion/pipeline/figura.py` dibuja con matplotlib en
la paleta de marca, **fondo transparente** —un PNG opaco taparía la retícula y
dejaría un rectángulo plano en mitad de la pantalla—, sin marco superior ni
derecho, Inter con respaldo. Dos clases: `linea` (con `marca` opcional para
anotar un punto, p. ej. el máximo) y `barras` (con `destacar` para pintar una en
ámbar y el resto en cian).

Va en el workflow **entre `voz.py` y `render.py`**: necesita `guion.timed.json`,
que lo crea voz.py, y le escribe dentro la ruta absoluta de cada PNG, que es lo
que lee render.py. Sobre un guion sin escenas de tipo `figura` no hace nada y
sale con código 0.

Coste de render **cero**: la figura es una imagen estática, entra con el
escalonado que render.py ya captura y no anima nada en el tramo central.

También se tocaron `escena.html` (la plantilla de `figura` ignoraba el `titulo`;
una gráfica sin enunciado obliga a deducir qué se está mirando), el esquema y el
validador, que ahora acepta `figura` sin `imagen` si trae los datos —el validador
corre antes que figura.py— y da error si no trae ninguna de las dos.

**Lo que falta, y no es código:** ningún guion usa todavía una escena `figura`,
porque **hacen falta los números reales**. La curva de Sandy del 003 y el reparto
de estilos del 005 son las dos candidatas obvias, pero inventarse los puntos de
la curva y ponerle `fuente: A04` sería fabricar un dato, que es exactamente lo
que el criterio editorial del canal prohíbe. Los números tienen que salir del
artículo, y eso es trabajo del verificador o de Silvestre.

Es la mejora de mayor impacto y la más segura, porque añade un tipo de escena en
vez de modificar los ocho existentes. Hay episodios que la piden a gritos: la
curva del humor sobre el huracán Sandy en el 003, el reparto de estilos de humor
en el 005.

**V2. Variantes de composición para `enunciado`.** ~~Es el tipo de escena que
ocupa la mitad del vídeo y siempre se ve igual: un bloque de texto centrado.~~
**Hecho el 19/08.** Tres variantes por número de escena (`d.n % 3`): centrada,
a la izquierda con aire a la derecha, y alta con la mitad inferior despejada.

Una desviación respecto a lo que proponía este documento: la tercera variante
iba a ser «a pie de pantalla» y se ha hecho **al revés, anclada arriba**. La
banda inferior no está libre: los subtítulos quemados van en alineación 1 con
`MarginV 96` y cuerpo 58, o sea de ~900 px hacia abajo. Un enunciado apoyado en
el suelo se les montaría encima en cuanto los subtítulos vuelvan a salir.
Despejar la mitad inferior rompe la monotonía igual y además les deja el sitio.

**Confirmado el 20/08** sobre `muestrario_02`, `_09` y `_10_enunciado.png`, que
se pintaron con Archivo Black presente: las tres variantes se leen, ninguna
desborda y la de la izquierda se distingue de la centrada incluso con el
enunciado largo.

**V2b. La viñeta iba encima del texto.** *Hecho el 20/08.* `#vineta` estaba
**después** de `#escena` en el DOM, los dos con `inset:0` y sin `z-index`, así
que el degradado radial que oscurece los bordes se pintaba también sobre las
letras. El texto pegado al borde izquierdo perdía contraste, y V2 lo empeoró al
mover el enunciado hacia ese lado. Movido `#vineta` justo detrás de `#reticula`:
ahora viñetea el fondo y la retícula, que es para lo que está, y no el contenido.

Medido con el muestrario entero antes y después, luminancia media de los píxeles
de glifo en la banda izquierda: `enunciado 09` 217,6 → 233,3; `enunciado 10`
216,8 → 233,4; `lista 04` 209,1 → 223,4; `comparacion 06` 206,9 → 219,9. En el
centro, sin cambio hasta el decimal. Fondo: esquina 9, centro 18 — la viñeta
sigue haciendo su trabajo. **Coste de render cero:** `vista.py` informa del
mismo número de unidades animables en las diez escenas, salida idéntica al byte.

**V3. Pictogramas en `lista` y `diagrama`.** Los números en caja de `lista` y las
cajas encadenadas de `diagrama` funcionan, pero son lo más genérico del sistema.
Un pequeño juego de iconos SVG propios —trazo de 3 px, mismo ámbar, dibujados en
el mismo lenguaje que el engranaje de marca— daría carácter. SVG en línea: cero
peticiones, cero dependencias.

**V4. Color de acento por episodio.** Mantener ámbar y cian como sistema, pero
dar a cada episodio un tercer color de apoyo (el coral ya existe y no se usa). El
canal se ve coherente y cada vídeo, distinto.

### Nivel 1 — animación dentro de la entrada, que ya se captura

**V5. Entradas que dibujan.** Las líneas y los marcos pueden trazarse con
`stroke-dasharray` en lugar de aparecer con un fundido. Es el gesto que más
«plano técnico» aporta y no cuesta ni una captura extra, porque ocurre durante la
entrada.

**V6. Barras que crecen en `comparacion`.** Los dos paneles ya entran; que además
crezcan desde su lado hacia el centro refuerza la idea de contraste.

**V7. La cifra que cuenta, extendida.** `dato` ya cuenta de 0 al número. Falta que
el pie entre después de que el número termine de contar, no a la vez.

### Nivel 2 — hay que medir el coste antes de adoptarlo

**V8. Un acento en mitad de la escena.** Un solo gesto —un subrayado que barre
bajo la palabra en ámbar— a mitad del tramo estático. Cuesta unas 15 capturas por
escena, unas 500 por vídeo: un 25 % más de render. Antes de adoptarlo hay que
medir con un episodio real cuánto sube el tiempo del job.

**V9. Miniaturas.** Van aparte porque no son el vídeo: el CTR se juega ahí antes
que en ningún otro sitio. `miniatura.py` merece su propia ronda de trabajo y sus
propias variantes A/B cuando haya datos.

### Descartado, y por qué

- **Metraje de archivo (b-roll).** Rompe el lenguaje de plano técnico y añade un
  riesgo de licencias que este canal no necesita.
- **Fondo animado (partículas, ruido).** Anima el tramo central de todas las
  escenas: multiplica el render por seis para un beneficio decorativo.
- **Movimiento de cámara / zoom lento.** Ya se probó y se retiró: `zoompan` trunca
  el recorte a entero y la imagen salta un píxel entre fotogramas. Está explicado
  en el comentario largo de `montaje.py`. No reintentarlo sin resolver eso.

---

## Reglas para tocar el diseño

1. **Un cambio por vez.** Si dos cambios entran juntos y el resultado empeora, no
   se sabe cuál fue.
2. **Mirar antes de publicar.** Cualquier `push` que toque `escena.html`,
   `render.py` o `vista.py` dispara el workflow *Vista previa del diseño*, que
   pinta el muestrario completo con las tipografías reales y lo deja en
   `03_produccion/vista_previa/`. Se mira eso, no se imagina.
3. **Las tipografías mandan.** Archivo Black para titulares, Inter para el resto,
   JetBrains Mono para etiquetas y referencias. Ninguna está en el contenedor de
   Cowork, así que una vista previa hecha fuera de Actions no vale para juzgar
   medidas de línea ni desbordamientos.
4. **Nada que dependa de internet en tiempo de render.** Todo va en línea o en
   `assets/`.
5. **Determinista.** Mismo guion y mismo `t`, mismo píxel. Nada de `Math.random()`.
6. **Si sube el coste de render, se mide.** El número de capturas sale en la
   salida de `render.py`; anótalo antes y después en `05_calendario/MEJORAS.md`.
7. **Nunca sobre un episodio ya producido.** Los cambios visuales entran en la
   siguiente producción, no se relanza lo publicado.

---

## Estado

| Ítem | Estado |
|---|---|
| Tipografía de titulares (Archivo Black no se instalaba en el runner) | corregido el 18/08 |
| **Subtítulos quemados ausentes** — lo único que se movía en el tramo estático | instrumentado el 18/08, a confirmar el 19 |
| Muestreo de fotogramas de QA a ciegas (caían en fundidos) | corregido el 18/08 |
| Un solo resaltado ámbar por pantalla | corregido en MDH-002 y en MDH-003 (es) el 19/08 |
| **V2 variantes de composición de `enunciado`** | hecho el 19/08, **confirmado el 20/08** en la vista previa con tipografías reales |
| **Viñeta pintando encima del texto** (`#vineta` después de `#escena`) | corregido el 20/08, +7 % de contraste en el borde izquierdo, coste de render cero |
| **V1 gráficas (`figura.py`)** | motor hecho el 19/08. **Falta que un guion la use, y eso exige números reales de la fuente** |
| V3 pictogramas · V4 acento por episodio | pendientes — V3 es el siguiente |
| V5–V7 | pendientes |
| **Subtítulos quemados** | **retirados el 20/08 por decisión de canal.** El `.srt` va a YouTube como pista aparte |
| V8–V9 | sin decidir — **V8 sube de prioridad**: sin subtítulos quemados, nada se mueve en el tramo central |

La revisión diaria de las 07:00 avanza este backlog de uno en uno y deja lo que
observa en `05_calendario/MEJORAS.md`.
