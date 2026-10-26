# Muestra · la cola del final con la opción (b) (26/10/2026, C36-cola)

El codirector eligió el 23/10 la opción **(b)**: ~1,8 s sin voz al final (antes, 2,95 s) y la tarjeta
«Síguenos · un mecanismo nuevo cada día» legible ~1,3 s. Regla 11.2: **no entra en producción hasta que
él lo vea**. Esta carpeta es lo que tiene que ver.

- **`cola_despues.mp4`** — el final del cierre de `MDS-045` con la voz de verdad (la toma única de C36,
  `07_pruebas/c36-2026-10-22/c36.mp3`, del segundo 28,4 al final de la voz, 36,3) y la cola nueva.
- **`cola_antes.mp4`** — lo mismo con la cola de ahora (2,95 s), para comparar.
- **`fotogramas_finales.jpg`** — cinco fotogramas de cada uno (arriba antes, abajo después) a 2,0 · 1,2 ·
  0,8 · 0,4 · 0,1 s del final.

La etiqueta negra de arriba a la izquierda **no sale en el vídeo**: dice si suena la voz o es cola, y
cuánto falta para el final. El fondo gris verdoso hace de vídeo de archivo (aquí no se bajan los
planos) y **no lleva música** (en el Short, la cola lleva la música de fondo).

## Qué cambia (en `cola_b.diff`, sin aplicar)

| | Antes (19/10) | Después (b) |
|---|---|---|
| Cola sin voz tras el cierre (`voz.COLA_REMATE_S`) | 2,95 s | **1,8 s** |
| Tarjeta de marca (`REMATE_S`, `escena.html` y `fondo_visual.py`) | 2,2 s | **1,5 s** |
| El texto del cierre se va | 0,3 s después de la voz, en 0,45 s | **nada más acabar la voz, en 0,3 s** |
| La tarjeta se lee entera | ~1,7 s | **~1,2-1,3 s** (entra en 0,45 s) |

El texto del cierre y la tarjeta siguen **sin cruzarse** (lo que se pidió el 16/10). Cada Short dura
1,15 s menos.

`cola_muestra.py` es el guion que hizo los dos vídeos (con las rutas del contenedor del 26/10).
