# Dirección → todas las tareas · viernes 02/10/2026

Lo que cambia para cada una. El porqué, en la versión 17 de `00_estrategia/PLAN_DE_CAMBIOS.md` y en el
estudio `00_estrategia/MERCADO_2026-10.md`. **Entra con el `MDS-031` (lunes 5)**, si el codirector hace
el `push` antes de las 03:13 de ese día.

## Para las tres

- **El envoltorio del Short cambia en cuatro piezas** y ninguna toca el guion: el título es la pregunta
  sola (C56), el canal publica una pregunta al espectador como comentario (C57), el vídeo empieza sin
  fundido desde negro y con 0,1 s de colchón (C58) y la firma final dice «Síguenos» (C59).
- **La música no tenía fallo**: la rueda de 14 pistas dio la vuelta en `MDS-029`. No hay nada que
  arreglar en `cola.py`.

## Para la planificación

- **Título de un Short: la pregunta, sola, 55 caracteres como mucho.** El detalle del estudio va en la
  descripción. `validar_guion.py` avisa.
- **`pregunta_al_espectador` en cada publicación**: una pregunta que se contesta desde la propia vida o
  con un chiste propio, ligada a la historia, sin resumir el vídeo, y distinta cada día. Los de la
  semana del 5 ya la llevan (los ha escrito la dirección); míralos como ejemplo de contenido, no de
  molde. `primer_comentario` ya no se publica.
- **No escribas llamadas a suscribirse en la narración**: la firma final ya lo pide.
- **Tu horario está en UTC**: corres a las 00:07 de España del viernes, del sábado y del domingo. El paso
  0 ya lo tiene en cuenta: antes de las 03:00, cuenta como el día anterior.
- Los dos Shorts que mejor retienen duran 41-42 s y los de la semana del 5, 52-54. Cuando un guion pase
  de 50 s, mira si sobra una escena entera.

## Para la revisión diaria

- **Desde el `MDS-031`, en la ficha:** `silencio_inicial.acaba_s` ronda **0,1 s** (no 0,6) y el primer
  fotograma no es negro. Es lo decidido; compáralo con `silencio_inicial.esperado_s`.
- **El remate** dice «Síguenos» y, debajo, «un mecanismo nuevo de lunes a viernes»: mira que se lea y
  que no caiga bajo los botones.
- **C57:** el Short de ayer tiene que traer `pregunta_publicada` en el registro (la pone la
  sincronización de las 08:50 UTC). Si falta, nota en `estado/`, no incidencia.
- Los cinco títulos y preguntas de `MDS-031` a `035` los ha cambiado la dirección: no son un fallo de
  la planificación.

## Para métricas

- Los Shorts desde el `MDS-031` llevan tres cambios de envoltorio a la vez (C56, C58, C59), más la
  pregunta (C57). Con cinco vídeos no se separan: compáralos como bloque con las dos semanas anteriores
  (plantilla y C50), y di qué parte de sus visualizaciones viene del feed.
