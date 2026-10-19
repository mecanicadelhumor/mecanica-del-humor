# Muestra · la firma final, más tiempo en pantalla (19/10/2026)

El final de `MDS-040` (escena de cierre, «¿Y con un emoji?») renderizado con `escena.html` antes y
después del cambio. El fondo verde grisáceo hace de vídeo de archivo (aquí no se bajan los planos);
la etiqueta «voz» de arriba a la izquierda se ve mientras suena la narración.

- `antes.gif` (en movimiento) / `antes.jpg`: lo que salió el 16/10. La firma entra mientras la voz todavía habla y el
  vídeo termina 0,2 s después de la última palabra: se lee menos de un segundo.
- `despues.gif` / `despues.jpg`: la voz termina, el texto del cierre se queda 0,3 s, se va, y la
  tarjeta con «Síguenos / un mecanismo nuevo cada día» se lee unos dos segundos (los últimos 2,2 s).

Cambio en `escena.html` (`REMATE_S`), `fondo_visual.py` (`REMATE_S`) y `voz.py` (`COLA_REMATE_S`).
Cada Short dura unos 2,7 s más, de música sola. Pedido por el codirector en su cuaderno del 16/10.
