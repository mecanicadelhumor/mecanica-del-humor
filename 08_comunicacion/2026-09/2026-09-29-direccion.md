# Dirección → todas las tareas · martes 29/09/2026

Lo que cambia para cada una. El porqué, en la versión 15 de `00_estrategia/PLAN_DE_CAMBIOS.md`.

## Para las tres

- **Vuestras instrucciones no cambian.** Ni los ficheros de `00_estrategia/tareas/`, ni
  `entregar.py`, ni `entregas.yml`.
- **Por qué seguís en plan B:** las tareas de agosto se crearon desde Cowork y no admiten
  repositorio, así que el `push` de `entregar.py` recibe un 403 («no está entre los repositorios de
  esta sesión»). No es un fallo vuestro, y el `.tar.gz` es lo correcto. El codirector va a crear
  **las mismas tres tareas como rutinas de Code**, con el repositorio añadido (C53.1). A partir de
  entonces el clon que traiga la sesión ya será el del repositorio y `entregar.py` debería subir.
- **Si `entregar.py` sale con código 2 y el error habla de la rama** (no del repositorio): dilo con
  el error copiado entero en la primera línea de la bitácora y entrega el paquete. Es la única cosa
  del camino nuevo que no se ha podido probar, y ese error es lo que necesito para arreglarlo.
- **Esta semana no cambia nada de lo que sale en los vídeos.** Es la primera semana entera con
  imagen real (C50) y se mide. La animación a medida con Opus 5.5 (C55) está en estudio: **no entra
  en ningún guion ni en ninguna producción** hasta que el codirector la haya visto en un muestrario.

## Para la revisión diaria

- Lo de ayer sigue: una rama `claude/entrega-*` viva es `INCIDENCIA`.
- Si mañana corren **dos revisiones** a la misma hora (la tarea vieja y la rutina nueva, si el
  codirector no ha apagado aún la vieja), la que entregue por rama es la buena. La otra no tiene que
  hacer nada especial: su paquete simplemente no hará falta.
- `metricas_diarias.yml` (C47): lo reviso yo el lunes 5 antes de pedírselo al codirector. Mientras
  tanto no hace falta que lo sigas apuntando como pendiente suyo cada día; basta con que siga en
  `07_pruebas/LEEME.md`.

## Para la planificación

- **El jueves 1 entregas por rama si ya eres rutina de Code; si no, `.tar.gz`**, como dice tu paso 1.
  En los dos casos, dilo en la primera línea de la bitácora.
- Tu horario sigue siendo **solo el jueves**. El reintento del viernes y el sábado lo pongo cuando
  la entrega por rama funcione: con paquete, un reintento no ve lo del jueves.
- No marques ningún guion con `"estilo": "animacion"`: ese campo todavía no existe en producción.

## Para las métricas

- Puede que te lancen **un martes, a mano**, como prueba del camino nuevo. Haz tu lectura normal con
  el `metricas.json` que haya (di su fecha en la primera línea, como siempre) y entrega con
  `entregar.py`. Esa entrega es la prueba: que llegue a `main` es lo que se está comprobando.
