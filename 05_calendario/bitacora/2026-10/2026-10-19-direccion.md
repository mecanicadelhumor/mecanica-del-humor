# Dirección · lunes 19 de octubre de 2026 (rutina C62)

Sin sesión interactiva hoy (ningún commit de «dirección» ajeno en `main`). Cuaderno leído hasta `324e3cd`
(nuevo: errores de `MDS-040`, OpenAlex, resumen semanal). Respuesta del codirector a las tareas del 15/10:
tarea 1 hecha y muestra del remate bien. Versión **22** del plan.

## Hecho

- **C69.1** `fondo_visual._una_superficie()`: una escena con archivo no pasa a tarjeta a mitad. Probado
  con cinco casos de tramos (marca detrás, delante, en medio, escena entera de marca, varias).
- **C69.2** `escena.html`: `rico()` envuelve el resalte y lo pegado sin espacio en `.nw`. Reproducido el
  defecto en Chromium (el `»` cae solo entre 354 y 370 px de ancho) y comprobado que con `.nw` no cae.
- **C69.3** firma final: `REMATE_S` 2,2 s (`escena.html`, `fondo_visual.py`), el texto del cierre sale
  antes; `voz.py` `COLA_REMATE_S` = 2,95 s tras el cierre de un Short (`cola_remate_s` en el guion
  cronometrado); `qa.py` la descuenta en `escenas_por_encima_de_14s`. Muestra antes/después en
  `07_pruebas/remate-2026-10-19/`. Ningún desborde en las escenas de `MDS-040`, `044`, `045` y `049` en
  los dos modos.
- `validar_guion.py` avisa de tarjeta mezclada con archivo; `guionista_corto.md` y los prompts de
  planificación y revisión, con su bloque del 19/10.
- `metricas.py`: `control_c26` ignora lecturas de menos de 3 días. Sobre el `metricas.json` de hoy: 62
  (fichero: 42). Trampa 60.
- `ciclos.json`: B1 hasta el 4/11 (sin tocar orden, brazos ni regla).
- C36: `2.5-pro` cancelado a los 20 min (run 39258914315); `3.1` en 65 s (run 39261841151); 8 de 8 cortes
  en silencio. `07_pruebas/c36-2026-10-19/`.
- Privado: ficheros de tareas del codirector movidos a `tareas/2026-09/` y `tareas/2026-10/`.

## No hecho

- Trampa 55 y prompt del guionista largo: jueves 22. `bucle.py --imprimir` reescribe `resultados.json`;
  lo ejecuté para comprobar el ciclo y deshice el fichero (es del workflow).
- Un plano que falla al montarse (`pista_de_fondo`) todavía puede salir como tarjeta a mitad de escena:
  es raro y no lo he tocado.
