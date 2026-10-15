# Bitácora · dirección · lunes 05/10/2026

Sesión interactiva con el codirector, desde las 12:30 UTC. Versión **18** del plan.

## Lo que traía el cuaderno

Seis puntos (revisión general; Kaggle y animación con fechas; personaje tipo VTuber y A/B; el vídeo de
hoy sin programar; la dirección como rutina; las métricas que no vieron la lectura) y una tarea
especial: iterar más rápido con las métricas como recompensa.

## Lo comprobado

- **`MDS-031`**: producción `producir.yml` nº 185, programada, creada a las 07:01 UTC (la de las 01:13,
  ~6 h tarde). Registro: `RRhe-WDHgl0`, `private`, `publicar_en` 2026-10-05T17:00Z. El codirector lo vio
  «Programado» en Studio.
- **Métricas**: `metricas.yml` nº 18, evento `schedule`, creado a las 12:22:36 UTC (no fue a mano). La
  rutina corrió a las ~10:05 (`6568b62`) con la foto del 29/09; el codirector la relanzó a las 12:21
  (`5ae9ff3`), ya con la lectura de las 12:23 (`470c9c1`). El `pull` local no intervino.
- **`sincroniza_registro.yml`**: 39-41 el 04/10 a las 14:24, 14:45 y 20:13 UTC (crons de 08:50, 09:10 y
  17:25). Hoy, a las 12:31 UTC, todavía ninguno.
- **Rutinas** (`list_triggers`): revisión Sonnet 5.5 `28 9 * * *`; planificación Opus 5.5
  `7 22 * * THU,FRI,SAT`; métricas Sonnet 5.5 `3 10 * * 1` con **el prompt entero pegado** (trampa 52).
- **«Se quedaron viendo»** (Studio, del codirector, 02/10): MDS-029 15,4 · 028 40 · 027 34,9 · 026 19,7 ·
  025 2,7 · 024 100 (4 vistas) · 022 17,6 · 021 25. La API tiene `engagedViews` (comprobado en la
  documentación de métricas de YouTube Analytics).

## Lo hecho (todo en la carpeta del codirector; lo sube él)

- `03_produccion/pipeline/voz.py` — **C58.1**: recorte del silencio delantero de la toma de Gemini en la
  escena 1 de los Shorts, antes de medir duraciones. Probado con una toma sintética (0,28 s → limpia).
- `04_agentes/metricas.py` — **C60.1**: `se_quedaron()` y `se_quedaron_48h()` (`views,engagedViews`, en
  llamada aparte, guardando el error si falla); en la lectura semanal y en la diaria (que además trae %
  visto, «me gusta», suscriptores y compartidos). Probado con una API de mentira, incluido el caso de
  error.
- `04_agentes/bucle.py` — **nuevo**, el marcador. Probado con 18 Shorts inventados (apartado el A sin
  animación, medias, veredictos, `prob_mejor`).
- `04_agentes/entregar.py` — bibliografía a la planificación; tareas `animacion` y `direccion`
  (`NUNCA_DIRECCION`); `bucle.py`, `05_calendario/bucle/` y `metricas_diarias.json` protegidos; la rama
  de entrega acepta cualquier tarea de `PROPIEDAD`. Probado caso por caso con `clasificar()`.
- `05_calendario/bucle/ciclos.json` (ciclo B1, 12-25/10, orden barajado con semilla 20261012) e
  `hipotesis.json`.
- `00_estrategia/tareas/workflows_2026-10-05/metricas.yml` — para que lo mueva el codirector. YAML
  validado.
- Instrucciones: `planificacion-jueves.md`, `revision-diaria.md`, `metricas-lunes.md` (sección del 05/10
  arriba) y `direccion.md` (nuevo, C62).
- `PLAN_DE_CAMBIOS.md` v18, `PROMPT_DE_ARRANQUE.md` (autorizaciones, trampas 52-54, dónde está el
  proyecto), `LEEME.md`, `PROPIEDAD_DE_FICHEROS.md`, `.gitignore` (`00_estrategia/privado/`).
- Fichero de tareas del codirector del 05/10 (seis tareas).

## Decisiones del codirector en la sesión

7 Shorts/semana desde el 12/10 y 14 desde el 19/10 (si C36); dirección en diferido con repo privado; los
dos caminos de personaje (2D y 3D VRM); variante B del ciclo B1 = arranque con el dato.

## Para la próxima (miércoles 7)

C55.2 (render y rutina «Animación»), prueba de C36, y comparar «se quedaron» de la API con Studio en
cuanto haya lectura con el código nuevo.
