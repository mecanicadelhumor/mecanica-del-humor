# Cara del final, adelantada (02/11/2026) — aplicada en producción

El codirector vio la muestra del 29/10 (`07_pruebas/cara-final-2026-10-29/`) y contestó: *«Sí al cambio,
pero prefiero que cambie antes. Cambia muy tarde a la cara sonriente. […] cuando hayas adelantado el
cambio tienes permiso para implementarlo en producción directamente. Es un cambio menor.»*

**Qué cambia respecto a la muestra del 29/10:** el paso a «rie» ya no empieza al entrar la tarjeta (1,5 s
del final) sino **1,1 s antes** (`A_RISA_ANTES_S` en `escena.html`): empieza a **2,6 s del final**, en las
últimas palabras de la voz, y el personaje queda sonriendo **unos 2,2 s** (antes, 1,15 s). Lo demás,
igual: 0,35 s de paso, saltito del 7 %, solo en la escena de cierre y solo si no estaba ya riendo. La
duración del Short no cambia y el render no hace ni una captura más.

- `final_antes.mp4` — el cierre de `MDS-045` como sale desde hoy (cola (b) + sonrisa adelantada).
- `final_risa.mp4` — la muestra del 29/10, para comparar.
- `fotogramas_finales.jpg` — el personaje a 2,8 · 2,4 · 2,1 · 1,7 · 1,3 · 0,2 s del final; arriba la
  muestra del 29/10, abajo la de hoy.

`escena_antes.html` es una copia de `03_produccion/pipeline/escena.html` tal como entra hoy.
`python3 cara_muestra.py <carpeta temporal>` rehace los dos vídeos.
