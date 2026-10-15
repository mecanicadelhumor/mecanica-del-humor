# Revisión diaria → la dirección / el codirector, 28/09/2026

Nota corta; el detalle completo está en `05_calendario/bitacora/2026-09-28-revision.md`.

## 1 · Para la dirección: C51.1 («el Engranaje habla») sin el muestrario del viernes 25

`PLAN_DE_CAMBIOS.md` (versión 13, sección C51.1) dice que la boca del personaje se movería con el
volumen real de la voz en las tarjetas de marca, con «muestrario el viernes 25». Comprobado en
`03_produccion/pipeline/escena.html`: no está hecho — el comentario del SVG del personaje sigue
diciendo «No habla. Reacciona.» — y no hay ningún `07_pruebas/` con ese muestrario. No es un
encargo de mi cola (`revision-diaria.md` no lo menciona) y es una decisión de presentación, así
que no lo he tocado. Lo dejo dicho porque es justo lo que responde a la pregunta de
`novedades.md` sobre el vídeo de `@Maestro_Seductor`, y el viernes pasó sin el muestrario.

## 2 · Para quien mantenga `00_estrategia/tareas/revision-diaria.md`

Repetido de la sesión del 25/09, y confirmado hoy con grep y lectura directa del código: los
encargos 1, 2, 5, 6, 11 y 12 de la cola del paso 4 **ya están hechos**, y también la caché de voz
y `voz_adelantada.yml` (C27). El fichero de la tarea los sigue listando como pendientes. Detalle
punto por punto en la bitácora de hoy. Sugiero limpiar esa cola antes de que alguien vuelva a
gastar una sesión reproduciendo el mismo hallazgo.

Además, el encargo 9/10 (P9, créditos de sonidos) está **a medias**:
`03_produccion/sonidos/creditos.json` ya está indexado y correcto, pero `montaje.py` no usa
ningún sonido todavía (cero menciones a «sonido» en el fichero). Falta la mezcla de verdad.

## 3 · Para la bibliografía / quien pueda verificar DOIs con alguien delante

`K03` (Hessel et al., 2023) sigue marcado «⚠️ por verificar» en `BIBLIOGRAFIA_CURADA.md` y es
fuente central de `MDS-029` esta semana. He intentado verificar su DOI con `WebFetch`
(`https://doi.org/10.18653/v1/2023.acl-long.41` y `https://aclanthology.org/2023.acl-long.41/`)
y las dos veces la herramienta ha devuelto `PROVENANCE_REQUIRED`: pide una aprobación de acceso
que, en una sesión programada sin nadie delante, se queda sin contestar. No es un fallo de red
ni del proxy de egreso (eso ya se sabía bloqueado para `api.crossref.org`): es un permiso nuevo
que necesita a alguien mirando. Si alguien con una sesión interactiva puede comprobar el DOI, el
título que debería devolver es el que trae la ficha; si no coincide, es exactamente el patrón de
`F04`/`F05`/`C05`/`G03`.

## 4 · Hoja de contactos (C50): dos planos corregidos hoy

`MDS-027` escena 5.2 y `MDS-028` escena 2.1 tenían planos de archivo que no contaban lo que
decía la frase de debajo (una fiesta de fin de año en vez de alguien que no pilla un chiste; una
pareja mayor con un termómetro digital en vez de una clase de humor). Corregidos en
`05_calendario/visuales/ajustes.json`. No he podido ver la hoja nueva porque no hago `push`;
que la revisión de mañana la mire antes de dar los dos planos por buenos.

## 5 · La incidencia de hoy está en `05_calendario/estado/2026-09-28.md`

Cara tapada por el texto en la escena 1 de `MDS-026`, el vídeo de hoy. Publica a las 19:00
España. Detalle y opciones ahí.
