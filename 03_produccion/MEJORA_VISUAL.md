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

Lo que sí da vida al tramo central sin coste: los **subtítulos quemados palabra a
palabra**, que se aplican en `montaje.py` sobre el vídeo ya renderizado.

---

## Backlog, por orden de valor sobre riesgo

### Nivel 0 — mejor imagen, cero coste de render

**V1. Gráficas de verdad (`tipo: figura`).** El esquema ya contempla escenas de
tipo `figura` con una imagen, y `escena.html` ya sabe pintarlas. No existe quien
las genere. Falta `03_produccion/pipeline/figura.py`: matplotlib con la paleta de
marca (fondo `#0B1220`, ámbar `#FFB020`, cian `#4CC9F0`, sin marco superior ni
derecho, tipografía Inter), invocado desde el workflow antes del render.

Es la mejora de mayor impacto y la más segura, porque añade un tipo de escena en
vez de modificar los ocho existentes. Hay episodios que la piden a gritos: la
curva del humor sobre el huracán Sandy en el 003, el reparto de estilos de humor
en el 005.

**V2. Variantes de composición para `enunciado`.** Es el tipo de escena que ocupa
la mitad del vídeo y siempre se ve igual: un bloque de texto centrado. Tres
variantes alternándose por posición (texto a la izquierda con aire a la derecha,
centrado, y a pie de pantalla con la parte superior despejada) rompen la
monotonía sin tocar nada más. La variante se elige por el número de escena, de
forma determinista: mismo guion, mismo resultado.

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
| Un solo resaltado ámbar por pantalla | corregido en MDH-002, vigilar en el resto |
| V1 gráficas · V2 variantes de enunciado · V3 pictogramas · V4 acento por episodio | pendientes |
| V5–V7 | pendientes |
| V8–V9 | sin decidir |

La revisión diaria de las 07:00 avanza este backlog de uno en uno y deja lo que
observa en `05_calendario/MEJORAS.md`.
