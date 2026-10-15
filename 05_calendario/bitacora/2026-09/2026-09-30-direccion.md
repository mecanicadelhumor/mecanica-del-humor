# Bitácora · dirección · miércoles 30/09/2026

Sesión adelantada por el codirector (el viernes quizá no pueda), de tarde. Versión **16** del plan.

## 1 · Lo que se leyó

El arranque entero: `LEEME.md`, `REGLAS.md`, `PROPIEDAD_DE_FICHEROS.md`, la versión 15 de
`PLAN_DE_CAMBIOS.md`, `PROMPT_DE_ARRANQUE.md`, el cuaderno del codirector (solo el título de la
semana), `estado/2026-09-30.md`, `08_comunicacion/` (novedades y la nota de la revisión de hoy), la
bitácora de la revisión de hoy y, en `origin/main`, la bitácora de la prueba de métricas. Y la
respuesta del codirector en `tareas_codirector_2026-09-29.md`.

## 2 · El estado del canal

- `MDS-028` subido (06:49 UTC) y con publicación a las 17:00 UTC; su expediente, limpio. La revisión
  de hoy, sin incidencias, entregó en plan B (fue la **tarea vieja**, a las 09:28 UTC; el codirector
  creó las rutinas a las 13:48-13:51 UTC) y el codirector aplicó su paquete (`cf307e0`).
- Números, sin cambios: mediana C26 24,0.

## 3 · C53.1, comprobado

- Listadas las tareas: tres rutinas nuevas (`created_via: http_api`), con los prompts de siempre;
  las tres viejas, `enabled: false` desde las 13:58-13:59 UTC.
- Modelos: revisión y métricas `claude-sonnet-5-5`; **planificación, vacío**. Preguntado al
  codirector: **Opus 5.5**. Horarios: 11:28 diario, jueves 22:07, lunes 12:03 (hora de España).
- En GitHub: «Entregas (C53)» en verde sobre `claude/entrega-metricas-20260930-1354` (13:55 UTC),
  commit `d234237` en `main`, la rama de entrega borrada. **Y una rama más**:
  `claude/charming-mccarthy-ztub1k` (`4b40fb8`, mismo contenido que `d234237`), la de la sesión, que es
  sobre la que la página le ofrecía «Crear PR» al codirector.
- **Intenté poner el modelo y el horario de la planificación y la herramienta lo rechazó**: *«Agents
  can only update routines they created»*. Las rutinas creadas desde la web no las puede cambiar la
  dirección (trampa 47). Pasa a la tarea 2 del codirector, con la documentación de las rutinas leída
  antes de escribirla (frecuencias fijas; varios disparadores por rutina; si no deja tres semanales,
  uno diario).

## 4 · C53.2, `entregar.py`

Al leer por qué había una rama de sesión apareció un fallo que aún no había pasado (trampa 48): con
un commit previo del modelo, «no hay nada que entregar» con código 0. Cambiado: se entrega contra la
base común con `origin/main`; lo ajeno se deshace contra esa base; `--aplicar` borra al final las
ramas de sesión de más de dos horas cuyo contenido ya está en `main`. Probado con un repositorio de
juguete (origen desnudo local) en cinco casos, los cinco bien. Notas de tres líneas en
`revision-diaria.md` y `planificacion-jueves.md` (y el paso 0 de la planificación: de domingo a
miércoles, termina). Cabeceras de los ficheros de `tareas/` actualizadas con los identificadores de
las rutinas nuevas.

## 5 · C55.1, el muestrario

`07_pruebas/animacion-2026-10/`. Voz de la caché (6 de 6, cero llamadas), instantes de palabra con
`fondo_visual.mapa_de_tiempo()` (el reconocedor local no se pudo usar: Hugging Face está cerrado en el
contenedor), fuentes de producción (Inter, JetBrains Mono, Archivo Black), captura con Chromium y
`montaje.py` tal cual con `cama_13`. Barrera de textos: cero problemas en 120 instantes. 43,3 s,
−14,1 LUFS. Tres vueltas. Unos 110.000 tokens de conversación. Lo que le veo, en su `LEEME.md` y en la
versión 16.

## 6 · C51.3, Kaggle y licencias

El token nuevo va en `KAGGLE_API_TOKEN` y no necesita usuario (documentación de `kaggle-api`, PR
#863); los secretos valen como están. Licencias miradas en el código de cada repositorio:
`07_pruebas/presentador-2026-10/LICENCIAS.md`.

## 7 · Lo que se ha escrito

`04_agentes/entregar.py`; `00_estrategia/tareas/` (`LEEME.md`, `metricas-lunes.md`,
`planificacion-jueves.md`, `revision-diaria.md`); `00_estrategia/PLAN_DE_CAMBIOS.md` (versión 16),
`PROMPT_DE_ARRANQUE.md` (trampas 47 y 48, autorizaciones, estado), `LEEME.md`,
`PROPIEDAD_DE_FICHEROS.md`; `.gitignore` (los `.mp4` de `07_pruebas/`); `07_pruebas/animacion-2026-10/`
y `07_pruebas/presentador-2026-10/`; esta bitácora y `08_comunicacion/2026-09-30-direccion.md`. Y fuera
de git, `tareas/tareas_codirector_2026-09-30.md`.
