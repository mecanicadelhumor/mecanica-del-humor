# Dirección (en diferido) · 2026-11-16

- Sin sesión interactiva hoy. Cuaderno sin cambios desde `83c6c46`; tareas del 12/11 sin «Respuesta del codirector». Vencidos del codirector: `voz-3.8-oir-2`, `doble-subida-borrar`, `C26-decision`.
- **Voz 3.8 en producción** (`voz-3.8-cambio`): `voz.py` con `MODELO_GEMINI = gemini-3.8-flash-tts`, `MODELO_GEMINI_LARGO = gemini-3.8-flash-lite-tts`, `MODELOS_TEXTO_DESNUDO` (solo el guion, en C36 y en la escalera; firma de caché `texto-desnudo`); `voz_precache.py` con la misma clave. Voz Charon (sin elección del codirector).
- Pruebas en el contenedor (Gemini simulado, `MDS-069`): C36 → 1 llamada con el texto desnudo; escalera → 5 llamadas, todas con el texto desnudo, narración entera; caso que tiene que fallar (indicaciones dentro) → tomas rechazadas por duración en 3.8 y 3.8-lite, salida 3, no se sube.
- Entregado `970942d` (rama `claude/entrega-direccion-20261116-1317`). Prueba en vivo sobre esa rama: «Prueba de voces» nº 16 (run 43874350354), `c36:` sobre `MDS-069`: una llamada a 3.8, toma única de 33,5 s, Whisper la da por fiel, cortes 6,57 / 12,04 / 20,44 / 26,21 s, narración 34,3 s. Peticiones a 3.8-flash hoy: 1 de 10.
- C26: sin decisión. El canal sigue publicando; nada de mejoras hasta que decida. Compromisos de la dirección del 16/11 al 19/11; nuevo `voz-3.8-vigilar` (19/11).
- B2: sin veredictos (faltan datos). Plan v32; «Dónde está» del 16/11.
