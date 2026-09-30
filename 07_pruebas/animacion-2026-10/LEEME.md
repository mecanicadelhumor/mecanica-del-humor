# C55.1 · El muestrario de la animación a medida · `MDS-027`

**Dirección (Opus 5.5), miércoles 30/09/2026.** Versión 16 del plan. **No se sube a YouTube**
(C54, regla 11.9: el mismo Short dos veces es lo que mató a `MDS-017` y `MDS-023`).

## Qué hay en esta carpeta

| Fichero | Qué es |
|---|---|
| `MDS-027.animacion.mp4` | **El Short entero, animado a medida**: 43,3 s, 1080×1920, 30 fps. Misma voz, misma música, mismo montaje que el publicado. **No va al repositorio** (pesa 13 MB; `.gitignore` deja fuera los `.mp4` de `07_pruebas/`): está solo en la carpeta del codirector |
| `comparacion.jpg` | Arriba, seis fotogramas del publicado (los de `05_calendario/qa/MDS-027.es/`); abajo, la animación **en los mismos segundos del vídeo final** |
| `hoja_de_contactos.jpg` | 24 instantes de la animación, cuatro por escena |
| `MDS-027.animacion.html` | **La animación en sí**: una página autónoma (712 líneas, sin red) con el mismo contrato que `escena.html`: `pintar(t)` deja el lienzo como tiene que estar en el segundo `t`. Es lo que escribiría la rutina de C55.2 |
| `capturar.py` | Lo que la convierte en vídeo: Chromium sin pantalla, fotograma a fotograma, igual que `render.py`. También pasa la barrera de C21 a este lienzo (20 instantes por escena) |

El publicado, para verlo al lado: **https://youtu.be/qlvJWEGc8hM**

## Qué es igual y qué cambia

**Igual, a propósito, para que solo cambie la imagen:** el guion (`05_calendario/guiones/MDS-027.es.json`,
sin tocar), **la voz** (las seis escenas salen de `03_produccion/cache_voz/`: cero peticiones a
Gemini), la música (`cama_13`, la misma que llevó el publicado), el montaje (`montaje.py` tal cual:
colchón, fundidos, volumen −14,1 LUFS contra −14,2 del publicado) y **los textos de pantalla**, que
son los del guion palabra por palabra, con el ámbar donde lo marca el guion (regla 14: la pantalla no
dice nada que no diga la voz).

**Lo que cambia es todo lo que se ve.** En vez de vídeo de archivo detrás de la frase, un plano
técnico dibujado a mano para esta historia, escena a escena, que **enseña el mecanismo** en vez de
ilustrar la situación:

1. **La cafetería** se dibuja como un plano: la barra, la cafetera, la gente, el camarero y el pan
   aparecen **en la palabra que los nombra**.
2. **«No, está cortado»**: la cámara se acerca al pan y el cuchillo lo corta **en la sílaba de
   «cortado»**; la hogaza se abre en rebanadas.
3. **La mesa**: cuatro se ríen («ja») y uno no; a él le sale un bocadillo con una interrogación, y en
   «cortado» una rebanada al lado.
4. **Los dos sentidos**: «No es que sea lento» es un caracol que se tacha; cae **INTEGRAL** y se abre en
   una vía que se bifurca: harina completa a un lado, la hogaza entera al otro; en «se quedó en la
   primera» un punto baja por la vía y se queda en la 1.
5. **El salto**: dos vías y un cambio de agujas. En «de golpe» un punto salta de la 1 a la 2; en «y él
   no saltó» otro pasa por el cambio sin cambiar y se para con una interrogación.
6. **El cierre**: una lupa recorre un chiste hecho de bloques, se para en una palabra y esa palabra se
   bifurca en dos; en «no se sabe», la interrogación en coral. Firma con el Engranaje.

El Engranaje está arriba a la derecha desde la escena 3 con las caras que pide el guion (duda, ríe,
piensa, duda).

## Lo que cuesta (lo que preguntaba C55)

- **En euros, cero.** Sin licencias (no hay material de nadie), sin red en el render.
- **En tokens de Opus 5.5: unos 110.000** para el muestrario entero, medidos como lo que creció la
  conversación entre empezarlo y terminarlo (de ellos, unos 18.000 escritos por el modelo: la página y
  sus arreglos; el resto, leer el guion, la voz, la marca y mirar tres hojas de contactos). **Es la
  mitad baja de lo que estimé** (150.000-400.000). Una rutina que lo haga cada semana empieza sin
  contexto y tendría que leer lo mismo, así que **el orden realista es 120.000-200.000 por Short**. La
  cifra que manda es la del medidor del codirector (claude.ai/settings/usage), que cuenta distinto
  (las lecturas de caché pesan menos que las escritas).
- **De render: 1.260 capturas y unos 7 minutos y medio** (regla 11.3), frente a los ~8 minutos de un
  Short de plantilla (trampa 2). Cabe de sobra en el `timeout` de producción.
- **Tres vueltas**: una primera versión y dos de arreglos mirando la hoja de contactos. Los ejemplos
  que circulan necesitaron también «unas cuantas rondas»: con una rutina sin nadie delante, el número
  de vueltas es la pregunta abierta de C55.2.

## Lo que yo le veo, para que el codirector no tenga que adivinarlo

**A favor:** cada imagen cuenta exactamente lo que dice la frase, y en el segundo exacto (el corte del
pan, el salto de vía); enseña *por qué* hace gracia, que es el nombre del canal; y es de marca de
arriba abajo, sin caras que tapar ni planos genéricos.

**En contra, y es serio:**

1. **Hay menos estímulo que en el publicado.** La imagen real llena la pantalla de textura, gente y
   luz; el plano técnico es línea sobre azul y deja mucho vacío, sobre todo en el tercio de abajo. El
   codirector pidió el 14/09 *«mucha más densidad de estímulos visuales»*, y esto va en la dirección
   contraria aunque se mueva más.
2. **El primer segundo es tranquilo**: una barra y una cafetera dibujadas, sin frase. El publicado
   abre con una cafetería de verdad. Si la hipótesis de siempre es cierta (lo que decide es el primer
   segundo), aquí se pierde.
3. **Se parece a la plantilla** —mismo fondo, misma retícula, mismos colores— y ese era el reproche
   del 14/09 (*«fondo azul con letras amarillas no compite con imágenes reales»*). Es otra cosa por
   dentro, pero en el feed, en un vistazo, puede leerse igual.

**Mi recomendación, si le gusta:** no sustituir a C50, sino **mezclar**: vídeo de archivo para la
situación (escenas 1-3) y animación a medida para el mecanismo (escenas 4-5). En las escenas de
explicación el vídeo de archivo no tiene nada concreto que enseñar —en el publicado, la 5 es una
tarjeta de marca y la 4 un cuenco de harina detrás de dos cajas de texto—, y ahí es donde la
animación gana. Eso es un cambio de C55.2: en vez de «un Short de cada cinco, entero animado»,
«las escenas de mecanismo de un Short de cada cinco». Lo decide el codirector mirando esto.

## Qué se decide con esto

La tarea 3 de `tareas_codirector_2026-09-30.md`: **¿sigue C55.2?** Y si sigue, ¿entero animado o
mezclado? Nada entra en producción antes de la semana del 12/10 (la del 5 es la segunda de C50), y
nada entra sin que las rutinas entreguen solas (C53.1: ya funciona).
