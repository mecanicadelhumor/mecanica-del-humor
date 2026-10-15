# Revisión diaria · 2026-10-06 · para la planificación y la dirección

- **Planificación (jueves):** MDS-033 la editó la revisión (esc. 4 y 6, 54,2 s). Si se toca de nuevo, ojo con el techo de 55 s; la esc. 4 («suena a clase») es donde el lector se iría. Para el futuro: «estudió la distancia» hay que anclarlo antes con la historia (cerca/lejos en el tiempo) en vez de en la frase de la fuente.
- **Dirección:** `ficha.json` de MDS-032 trae `arranque.fragmento_antes_de_la_narracion: true` (0,812 s) y no trae `modelo_voz`/`voz_mezclada`/`origen_voz` (null). Posible regresión de `qa.py` tras el cambio del 05/10 o simple falso positivo de la coma; si está pasando también en las siguientes fichas, conviene mirar el detector.
