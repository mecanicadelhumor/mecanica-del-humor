# Revisión diaria → la dirección / el codirector, 29/09/2026

Nota corta; el detalle completo está en `05_calendario/bitacora/2026-09-29-revision.md`.

## 1 · Sin incidencias hoy

Lectura en frío de MDS-028 (mañana): pasa. Los tres guiones pendientes
(MDS-028, MDS-029, MDS-030) pasan la revisión editorial completa. El vídeo de
hoy, MDS-027, sale limpio en `qa/`. `MDS-026` (ayer) ya está `public`: la cara
tapada por el texto que avisé ayer no la retiraste, así que doy el asunto por
cerrado y no lo vuelvo a abrir.

## 2 · Hoja de contactos (C50): tres planos corregidos

`MDS-028` escena 2.1 (dieciocho jubilados en clases de humor) seguía saliendo
mal por segunda vez — el ajuste de ayer cambió la búsqueda y el reemplazo
tampoco encajaba (un hombre solo, «two people dancing together»). Y en
`MDS-029`, escena 1.2 (el buzón del náufrago) y escena 3.2 (las máquinas en
el centro de datos) salieron con clips que no muestran lo que dice la frase.
En los tres he forzado `"fuente": "ia"` en `ajustes.json` en vez de insistir
con otra búsqueda, usando el `prompt` que ya trae cada guion para ese plano.
Ninguna he podido verlo con la hoja nueva porque no hago `push`: que la
revisión de mañana lo compruebe antes de dar los planos por buenos.

## 3 · Un cambio de código: `metricas.py` no vuelve a machacar una lectura buena

Encargo pendiente desde la sesión del 28/09 (el caso de `MDS-022` sin curva
de retención por una segunda pasada del día). Hecho: si una lectura del mismo
día para el mismo vídeo llega con `retencion.puntos` en 0 o `trafico_pct`
vacío y la pasada anterior de ESE MISMO día sí tenía datos, se conserva el
dato bueno y se avisa por consola. Verificado con una simulación aislada
(sin API, sin tocar `metricas.json`); no he podido probarlo con una lectura
real porque esta sesión no tiene credenciales de YouTube.

## 4 · Nada más pendiente de mí

P9 (mezcla de sonidos en `montaje.py`) y el encargo 8 (`lista` + personaje en
`escena.html`) siguen abiertos, sin urgencia. La música sigue bloqueada por
red. `metricas_diarias.yml` y `voz_adelantada.yml` siguen sin subir a
`.github/workflows/` — eso es tuyo, no mío.
