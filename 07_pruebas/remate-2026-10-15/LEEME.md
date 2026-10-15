# El remate del cierre, centrado y «cada día» (15/10/2026)

Último fotograma de la escena de cierre de `MDS-041`, renderizado en el contenedor con
`render.py --escena 6` (duraciones estimadas, sin voz).

- `antes.jpg`: como salió de `MDS-036` a `MDS-039`. Margen de 40 px a la izquierda y 150 a la
  derecha: el bloque queda centrado en x = 485 (el lienzo mide 1080, el centro es 540).
- `despues.jpg`: margen de 150 px a los dos lados y la firma «un mecanismo nuevo cada día».
  Centro medido de las tres líneas: 537, 540 y 539,5. Borde derecho del texto más ancho
  («MECÁNICA DEL HUMOR»): x = 896, fuera de la columna de botones de Shorts (~930 en adelante).
- `comparacion.jpg`: los dos, uno al lado del otro.

Entra en producción desde `MDS-040` (viernes 16). Para volver atrás: `escena.html`, regla
`html[data-fmt="v"] #remate`, y `REMATES` en `render.py`.
