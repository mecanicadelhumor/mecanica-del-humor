# Bitácora · dirección · martes 29/09/2026

Sesión pedida por el codirector, de tarde (18:10 en España). Versión **15** del plan.

## 1 · Lo que se leyó

El orden del arranque entero: `LEEME.md`, `REGLAS.md`, `PROPIEDAD_DE_FICHEROS.md`, la versión 14 de
`PLAN_DE_CAMBIOS.md`, `PROMPT_DE_ARRANQUE.md`, el cuaderno del codirector, `estado/2026-09-29.md`,
`08_comunicacion/`, la bitácora de la revisión de hoy y `metricas.json` (del 29/09, 11:23 UTC).
Además, la respuesta del codirector en `tareas_codirector_2026-09-28.md`.

## 2 · El estado del canal

- `MDS-027` subido a las 07:03 UTC, privado con publicación a las 17:00 UTC: correcto. Nueve planos
  de archivo y una tarjeta; su expediente de calidad, sin incidencias.
- La revisión de hoy entregó en **plan B** (403: repositorio no añadido a la tarea) y el codirector
  aplicó su paquete a las 17:59 (`6bf8eff`). «Visuales» volvió a resolver después (`730a23e`).
- Números, sin cambios desde el punto de control: mediana C26 24,0; cinco por encima de 100.
  `MDS-026` aún no tiene sus 48 horas.

## 3 · Por qué C53 no funcionaba (C53.1)

Listadas las tres tareas programadas con la herramienta de tareas: las tres tienen
`created_via: meta_mcp` (nacieron en una conversación de Cowork en agosto) y ningún campo de
repositorio. La herramienta permite cambiar nombre, horario, texto, modelo y encendido; no
repositorios. La página de rutinas de Code no las enseña. **La tarea 1.3 del 28/09 era imposible**
(trampa 46).

Documentación consultada (code.claude.com, rutinas, entornos y sesiones en la nube): las rutinas de
Code sí llevan repositorios, entorno, modelo y conectores; horarios con cuatro modos predefinidos y
cron propio desde la línea de comandos (o desde la herramienta de la dirección). Dos puntos que
importan:

- **Ramas:** la página de rutinas dice que las ramas `claude/` se aceptan siempre; la de entornos,
  que el `push` solo se admite contra la rama de trabajo de la sesión. Sin probar.
- **Red:** el entorno «Default» solo deja llegar a GitHub y a repositorios de paquetes. Por eso se
  pide un entorno propio con red completa.

Intenté preparar el segundo camino por si mandara lo de la rama de trabajo (`entregar.py` subiendo
a la rama de la sesión con una línea `Entrega-C53: <tarea>`, y `entregas.yml` escuchando cualquier
`claude/`). **La comprobación de permisos de la sesión lo paró** —es el mecanismo que sube cosas a
GitHub— y no insistí: queda descrito en la versión 15 y se aplica solo si la prueba de la tarea 1.4
del codirector lo pide y él lo autoriza. **No se ha tocado ni `entregar.py` ni `entregas.yml`.**

Tampoco se ha cambiado el horario de la planificación: con el `.tar.gz`, un reintento del viernes
planificaría la semana dos veces.

## 4 · C55 · la animación a medida

- Comprobado en `05_calendario/qa/` y `05_calendario/visuales/`: hasta `MDS-025` todo es la
  plantilla `escena.html` (animación JavaScript); `MDS-024` y `025` intentaron C50 y cayeron a ella
  (11 y 10 planos sin imagen). `MDS-026` es el primero con imagen real.
- C50 en sus cinco primeros Shorts (`MDS-026` a `030`): 33 planos de archivo; la revisión ha
  corregido 4 (uno dos veces) por no contar lo que dice la frase, y `MDS-026` salió con texto sobre
  una cara. Ningún plano de FLUX.
- Documentación pública de cómo se hacen los vídeos de Opus 5.5: una página que se pinta en función
  del tiempo, capturada con un navegador sin pantalla y codificada con `ffmpeg`; unos 90.000 tokens
  de entrada y 15.000 de salida por pieza corta en la primera versión. Es nuestra misma tubería.
- Recomendación y regla de decisión en la versión 15, C55. El codirector lo decide (tarea 3).

## 5 · Ficheros tocados

- `00_estrategia/PLAN_DE_CAMBIOS.md` — versión 15, añadida al final.
- `00_estrategia/PROMPT_DE_ARRANQUE.md` — autorización de C53 precisada, trampa 46, «dónde está el
  proyecto a 29/09».
- `00_estrategia/LEEME.md` — la versión que manda y el estado a 29/09.
- `00_estrategia/tareas/tareas_codirector_2026-09-29.md` — nuevo (fuera de git).
- `08_comunicacion/2026-09-29-direccion.md` — nuevo.
- `05_calendario/bitacora/2026-09-29-direccion.md` — este fichero.

Nada de código, guiones, prompts de tareas, horarios ni workflows. `PROMPT_DIRECCIÓN.md` y
`08_comunicacion/novedades.md` solo se han leído.
