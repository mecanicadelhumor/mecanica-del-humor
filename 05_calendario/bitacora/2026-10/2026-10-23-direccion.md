# Dirección · viernes 23 de octubre de 2026 (extraordinaria)

Rutina «Dirección» lanzada fuera de su día, con el codirector delante y contestando. Sin otra sesión de
dirección hoy (último commit de dirección en `main`: el mío del 22/10). Cuaderno procesado hasta `4986b5a`.
Versión **24** del plan.

## Lo roto, primero

- **El muestrario VRoid del 16/10 no se hizo, y nadie lo dijo hasta el 22/10.** Rastreado: el avatar
  entró el 13/10 (`4f95779`); la fila del calendario de la versión 21 no tenía dueño; la dirección del
  15/10 no lo hizo ni lo apuntó en «Sin mirar»; la del 19/10 no lo nombró; la revisión diaria no mira el
  plan. Con él, el muestrario 2D (12/10) y la prueba de Kaggle (13-15/10). Culpa de la dirección.
  Arreglo: C70, `05_calendario/compromisos.json` + paso 0 de la revisión diaria. Trampa 62.
- El canal publica: `MDS-047` hoy (estado del 22/10: OK). B1 sin cambios desde ayer.

## Hecho

1. **C70**: `compromisos.json` (14 filas), bloque del 23/10 y línea «Plazos vencidos» en
   `tareas/revision-diaria.md`, bloque en `tareas/planificacion-jueves.md`, fila en
   `PROPIEDAD_DE_FICHEROS.md`.
2. **Muestrario 2D** (`07_pruebas/personaje-2026-10/muestrario-2d-2026-10-23/`) y **VRoid**
   (`…/muestrario-2026-10-23/`), hechos hoy por subagentes y mirados (hoja de caras y fotogramas). Vídeos
   ligeros a 540×960 añadidos con `git add -f` (`.gitignore` excluye los `.mp4` de `07_pruebas/`).
3. **C51.3**: prueba de Kaggle preparada (`07_pruebas/presentador-2026-10/PRUEBA.md`); workflow en
   `00_estrategia/tareas/workflows_2026-10-23/`. Sin ejecutar: no hay claves aquí.
4. **C36 encendido** (`voz.py`), **C36.1** rótulo de situación (0,7 s antes y después; Whisper parte el
   trozo; probado con la toma real de `MDS-045` con Gemini simulado: una petición, «rótulo con 0.70s
   detrás»; y el caso que falla: frontera no encontrada → la escena se queda como estaba). Calibrado en las
   612 escenas: 5 rótulos. **C36.2** techo de ritmo 4,2 en la toma única (`voz.py`, `qa.py`).
   `VERSION_UNA_TOMA = 2` (la caché de tomas únicas anteriores no se reutiliza; no hay ninguna en
   producción). Muestra: `07_pruebas/c36-2026-10-23/c36_rotulo.mp3`.
5. **Planificación**: C17 no aplica a los largos; temas en reserva (`temas_en_reserva.md`, suyo; añadido a
   `entregar.py`).

## No hecho

- **La cola final** (≈3 s): pendiente de que el codirector elija (a/b/c). Compromiso `C36-cola`, lunes 26.
- Imagen horizontal y voz por tandas del largo: lunes 26, como estaba.
- Propuestas de iteración y calidad: escritas (plan v24 y sus tareas); nada cambia hasta que conteste.
