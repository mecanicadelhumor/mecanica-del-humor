# Revisión diaria → otros agentes / la dirección, 19/09/2026

Nota corta, el detalle completo está en `05_calendario/bitacora/2026-09-19-revision.md`
(paso 1 y paso 4).

**Para quien toque `01_bibliografia/` (la planificación de los jueves, sobre todo):** el
sincronizado de C39 del 18/09 dejó cuatro fichas al día (`C05`, `F04`, `F05`, `G03`) pero
`validar_bibliografia.py` solo comparaba título/autores/año/DOI, así que no vio que otras
seis fichas (`E02`, `E06`, `G05`, `G06`, y el volumen/página de `C05`) tenían contenido
verificado que solo existía en `BIBLIOGRAFIA_CURADA.md` y que la próxima regeneración
habría borrado. Hoy queda cerrado: `semillas.json` sincronizado, `generar_md.py` ya sabe
imprimir la nota de verificación real (campo `doi_confianza`) y un párrafo largo opcional
(campo nuevo `nota_ampliada`), y `validar_bibliografia.py` compara también `fuente`. Si
alguien corrige una ficha directamente en el `.md` en vez de en `semillas.json`, el
validador lo sigue sin ver **si la diferencia está en `nota_ampliada`** (no en
título/autores/año/fuente/DOI) — queda escrito en la cabecera del propio script.

**Sin resolver, y no es mío decidirlo:** `escena.html` no tiene ninguna sintaxis de guion
para el resaltado «coral» que `00_estrategia/tareas/revision-diaria.md` describe («coral =
lo que falla, reservado al cierre»). Solo existen ámbar (`*así*`) y cian (`_así_`).
`guionista_corto.md`, reescrito el 12/09, tampoco menciona el coral. O se construye, o se
retira la mención de la tarea — cualquiera de las dos cierra la inconsistencia.
