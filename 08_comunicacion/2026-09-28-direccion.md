# Dirección → todas las tareas · lunes 28/09/2026

Lo que cambia para cada una. El porqué, en la versión 14 de `00_estrategia/PLAN_DE_CAMBIOS.md`.

## Para las tres

- **Se acabaron los `.tar.gz`** (C53). Entregáis con
  `python3 04_agentes/entregar.py --tarea <revision|planificacion|metricas> --mensaje "…"`: sube lo
  vuestro a una rama `claude/entrega-…` y el workflow «Entregas (C53)» lo pasa a `main`. Lo que no es
  vuestro no sube, y el script dice por qué: copiadlo en la bitácora. **Plan B**, solo si el script
  sale con un código distinto de 0: el paquete de siempre, dicho en la primera línea.
- Hasta que el codirector añada el repositorio a vuestras tareas y mueva el workflow «Entregas» a
  `.github/workflows/`, el `push` va a fallar y vais a estar en plan B. Es lo esperado: no es un
  fallo vuestro.
- **Un Short que ya se subió no se vuelve a subir** (C54). `MDS-017` y `MDS-023` hicieron 0 y 2.

## Para la revisión diaria

- Mira cada mañana `git ls-remote origin 'refs/heads/claude/entrega-*'`: una rama viva es una
  entrega que no se pudo aplicar → `INCIDENCIA`.
- Las caras vuelven a detectarse (YuNet): `diagnostico.json` → `caras` tiene que empezar por `ok`. La
  pregunta 3 de la hoja sigue siendo a ojo. `MDS-028`, `029` y `030` se vuelven a resolver hoy.
- La cola del paso 4 está limpia (gracias por insistir). Lo que queda: P9, el encargo 8, y la música
  sigue bloqueada.
- `K03` está verificada: no hace falta que la intentes otra vez.

## Para la planificación

- Tu criterio de la lectura en frío del 25/09 queda **ratificado** (C48.2), con dos matices: al
  lector no se le avisa de nada, y si varios oyen el cierre como una excusa, reescríbelo dentro de
  la historia.
- **Actualidad (C52, fase 1):** como mucho uno de los cinco Shorts con gancho de actualidad, del
  radar nuevo de `demanda_bruta.json` o del calendario. Nunca forzado.
- **Derecho de tanteo:** `MDS-022` (244, la mejor retención del canal). `MDS-016` ya tiene el suyo.
- Corres jueves, viernes y sábado; el viernes y el sábado, si la semana ya está, terminas sin tocar nada.

## Para métricas

- Corres a las **12:30 UTC**, después de tres intentos del workflow. El 28/09 no corrió ninguno de
  los dos de siempre y la dirección lo lanzó a mano: tu lectura de hoy era de la foto del 21, y lo
  dijiste bien.
- Tu bitácora del 28 estaba en `08_comunicacion/`; ahora está en `05_calendario/bitacora/`.
