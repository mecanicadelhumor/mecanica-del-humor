# `metricas_diarias.yml` — diseño de C47, 21/09/2026

**Qué hay aquí:** el `.yml` completo de un workflow nuevo. Cópialo a
`.github/workflows/metricas_diarias.yml` y súbelo cuando quieras encenderlo —
esa carpeta está protegida contra escritura remota, igual que
`producir-yml-07-09/` y `registro-diario-15-09/`.

**No hace falta nada más para que funcione.** El código del que depende
(`escribir_metricas_diarias()` y el flag `--diario` en `04_agentes/metricas.py`)
ya está en el repositorio, escrito hoy y probado con un cliente de YouTube
simulado (filtra el vídeo sin `video_id`, filtra el publicado hace más de
`DIAS_VENTANA_DIARIA` = 10 días, y deja `visualizaciones`/`vistas_48h`
correctos — ver `escribir_metricas_diarias()` en `metricas.py` para el porqué
de cada decisión). El secreto que necesita es el mismo que ya usa
`metricas.yml` (`YT_REFRESH_TOKEN` + `YT_CLIENT_ID` + `YT_CLIENT_SECRET`).

## Qué hace, en una frase

Todos los días a las 09:15 UTC (antes de que despierte la revisión diaria)
lee, para los vídeos publicados en los últimos diez días, solo
`visualizaciones` y `vistas_48h`, y sobrescribe entero
`05_calendario/metricas_diarias.json`. No toca `metricas.json` (que sigue
siendo la única fuente de la mediana de C26 y solo se calcula el lunes) ni
`registro_publicaciones.json` (de eso ya se ocupa `sincroniza_registro.yml`).

## Qué pregunta contesta

**¿Hace falta una lectura diaria de visualizaciones para no repetir el caso
`MDS-017`** (0 visualizaciones seis días sin que nadie lo viera, porque
`metricas.yml` solo corre el lunes), **o basta con mirarlo a ojo en Studio de
vez en cuando?**

La dirección ya ha decidido que sí hace falta (C47, versión 11 del plan) —
esta prueba no es sobre si hacerlo, es sobre si el diseño concreto (ventana de
diez días, hora, qué NO se guarda) es el que conviene.

## Qué pasa con cada respuesta

- **Si el diseño sirve tal cual:** se sube a `.github/workflows/` y, en
  cuanto exista, la revisión diaria empieza a leer
  `05_calendario/metricas_diarias.json` cada mañana y a marcar `INCIDENCIA`
  si un Short pasa de 24 horas con 0 visualizaciones — tal como pide C47.
  Hasta entonces, la revisión diaria no tiene ese fichero que leer y lo dice
  en su bitácora en vez de suponerlo.
- **Si la ventana de diez días es demasiado corta o demasiado larga:** es una
  constante (`DIAS_VENTANA_DIARIA` en `04_agentes/metricas.py`), cambiarla no
  toca el resto del script.
- **Si 09:15 UTC llega demasiado pronto o demasiado tarde:** el cron es la
  única línea que cambia; no afecta a `metricas.yml` ni a
  `sincroniza_registro.yml`, que corren en sus propias franjas.

## Una cosa que se ha dejado fuera a propósito

**No marca `INCIDENCIA` ni decide nada por sí mismo.** Solo lee y escribe el
fichero. Que un vídeo con 24 horas y 0 visualizaciones sea `INCIDENCIA` es una
regla de lectura de la revisión diaria (paso 2 de
`00_estrategia/tareas/revision-diaria.md`), no de este workflow — igual que
`sincroniza_registro.yml` corrige el registro pero no decide si eso es bueno
o malo.

---

*(Respuesta del codirector, cuando la haya, se añade aquí debajo con fecha y
firma — regla de `07_pruebas/LEEME.md`.)*
