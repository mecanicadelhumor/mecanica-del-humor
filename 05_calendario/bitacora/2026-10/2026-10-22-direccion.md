# Dirección · jueves 22 de octubre de 2026 (rutina C62)

Sin sesión interactiva hoy (ningún commit de «dirección» ajeno en `main`). Cuaderno leído hasta `34cd76c`
(nuevo: Feed, Retención, Duda). Respuesta del codirector a las tareas del 19/10: OpenAlex puesto, rama
borrada, C36 «dirigido con pausas más pequeñas». Versión **23** del plan.

## Hecho

- **`bucle.py`**: guarda lo leído de cada ficha en `resultados.json` (`fichas_vistas`) y lo reutiliza cuando
  `qa/` rota; `ciclos.json` lleva `fichas_de_historial` con `MDS-038` y `MDS-039` (2 escenas animadas,
  commit `ffb9fae`). Probado: A pasa de n = 1 a n = 3; quitando la ficha de `MDS-042` se sigue contando
  desde la caché; `MDS-048` sin ficha ni caché sigue pendiente. `resultados.json` deshecho (es del workflow).
- **C36 en `voz.py`** (`_voz_una_toma`, `_partir_toma`, `direccion_una_toma`, `C36_EN_PRODUCCION = False`).
  Probado en el contenedor con la toma real del 19/10 (Gemini simulado): 1 llamada, 5 trozos fieles. Caso
  que falla: toma de `MDS-045` con el guion de `MDS-046` → rechazada, vuelta a la escalera, nada en caché.
- **Muestra en vivo**: `voz_prueba.yml` sobre la rama de sesión, `c36:05_calendario/guiones/MDS-045.es.json`.
  Run 39788231961 falló (el runner no trae ffmpeg; puede haber gastado una petición de `3.1`); run
  39788533738 bien: toma de 40,3 s, 4 cortes, 39,3 s con pausas (lo publicado, 47,3 s). Escena 1 a 3,88 pal/s.
  `07_pruebas/c36-2026-10-22/`. Peticiones de `3.1` gastadas hoy por mí: 1 o 2 (la producción de mañana
  necesita ~6 de 10).
- **`prueba_voz.py --c36`** (o `c36:` en el campo guion del workflow).
- **Prompt del largo**: bloque del 22/10 en `guionista.md`; `validar_guion.py` largo 360-600 s, 30-80 escenas.
- **Planificación**: bloque del 22/10 (feed primero, escena 1, largo el 29/10).
- `hipotesis.json`: `H-duracion` para B2 (5/11, regla escrita), `H-presentador` no antes del 19/11.

## No hecho

- Imagen horizontal y voz por tandas del largo: lunes 26. Muestrario VRoid: jueves 29.
- Trampa 55: cerrada sin investigar (decisión, versión 23).
- El aviso de la revisión del 20/10 («que `voz.py` repita la toma cuando una escena pase de 3,2 pal/s»):
  no se hace; con C36 el ritmo cambia entero y se decide con la muestra.
