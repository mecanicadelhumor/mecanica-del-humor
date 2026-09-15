# cache_voz — tomas de voz de Gemini ya pagadas

Cada fichero `<sha256>.mp3` es una escena sintetizada con Gemini. El nombre es el
`sha256` de `narración | modelo | voz | dirección de actor` (ver `_cache_voz_ruta()` en
`03_produccion/pipeline/voz.py`), así que una escena solo se reutiliza si no ha cambiado
nada de eso.

**Quién escribe aquí:**

- `voz_precache.py`, desde `.github/workflows/voz_adelantada.yml` (martes a viernes): las
  escenas del episodio largo del sábado, con `gemini-2.5-flash-preview-tts`.
- `voz.py`, desde `.github/workflows/producir.yml`: cada toma de un Short que sale bien.
  Desde el 15/09/2026 (C33.1) el paso «Registrar lo publicado» también sube esta carpeta,
  para que una producción que falla por cuota a las 01:13 UTC no pierda lo que ya había
  sintetizado y el cron de las 08:23 UTC solo pida lo que falta.

**Por qué existe este fichero:** para que la carpeta exista siempre en el repositorio.
`git add -A 03_produccion/cache_voz` falla si la carpeta no existe, y ese `git add` va en
el mismo paso que guarda el registro de publicaciones.

**No se borra a mano** salvo que pese demasiado. Si hay que podarla, se puede borrar
entera: lo único que se pierde es cuota ya gastada, nunca un vídeo.
