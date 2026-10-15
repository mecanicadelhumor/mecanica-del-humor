# Revisión diaria → la dirección / el codirector, 22/09/2026

Nota corta; el detalle completo está en `05_calendario/bitacora/2026-09-22-revision.md`
(paso 2 y paso 4).

**`sincroniza_registro.yml` (C31) puede no estar corrigiendo el registro desde el 20/09.**
Es el workflow que se subió el 15/09 precisamente para que no se repitiera el caso
`MDS-011` (seis días de incidencia falsa por leer un registro caducado). Lo que he visto
hoy:

- El último commit que corrige de verdad `registro_publicaciones.json` contra YouTube es
  `421ba35`, del sábado 20/09 a las 13:14 UTC.
- Desde entonces, `MDS-021` pasó de subido a público (17:00 UTC del 21/09) — un cambio de
  estado que el workflow debería haber detectado en alguna de sus dos pasadas diarias
  (`50 8 * * *` y `10 9 * * *`; su propia cabecera dice «tres pasadas», el `on.schedule`
  solo trae dos — inconsistencia menor aparte). Ninguna ha dejado commit.
- No sé si el workflow corre y no encuentra nada que corregir por algún motivo que se me
  escapa, o si está fallando en silencio (token, permisos). No tengo credenciales de
  YouTube ni acceso al historial de Actions desde este contenedor — lo intenté por
  `WebFetch` y pidió una aprobación que nadie iba a dar, así que no he insistido.
- **No es incidencia de canal**: los vídeos se siguen publicando bien (`MDS-021` y `MDS-022`
  traen `publicar_en` correcto), solo el fichero que describe su estado puede estar
  desactualizado. Pero es exactamente el tipo de cosa que un vistazo al historial de
  Actions resuelve en un minuto y que yo no puedo mirar en absoluto.
- De paso, he corregido `07_pruebas/LEEME.md`: la fila de `registro-diario-15-09/` seguía
  diciendo «falta que el codirector lo suba», y el workflow lleva subido desde el 15/09.

**Sin resolver desde el 19/09, y no es mío decidirlo (repetido para que no se pierda):**
`escena.html` sigue sin ninguna sintaxis de guion para el resaltado «coral» que
`00_estrategia/tareas/revision-diaria.md` describe. No lo toco esta semana porque sería un
cambio de presentación (bloqueados hasta el 28 por la nota de dirección del 21/09).

**Seguimiento, no incidencia nueva:** la incidencia del 21/09 sobre `MDS-021` (fragmento de
audio de 0,41s en el 0:32,3) no tuvo ninguna respuesta escrita antes de que el vídeo pasara
su hora de publicación. Salió con el defecto. Lo dejo dicho por si en algún momento se
pregunta por qué.

# Respuesta del codirector: 22/09/26
El Action "Sincroniza el registro con YouTube" se está ejecutando correctamente (últimas ejecuciones en verde en GitHub Actions el 21/09 a las 17:52 GMT+2 y a las 17:21 GMT+2). Por lo tanto, cualquier error si lo hay debe ser de otro tipo.