# Dirección en diferido · 2026-11-19 (jueves)

## Antes de nada
- `origin/main` 067de67 (Visuales C50, 10:42 UTC). Sin sesión interactiva hoy (ningún commit de «dirección» que no sea mío desde el 16/11).
- Ramas `claude/entrega-*` vivas: `entrega-direccion-20261112-1323` y `entrega-revision-20261104-1031`, obsoletas (contenido ya en `main`); el codirector puede borrarlas.
- Cuaderno del codirector sin cambios desde 83c6c46 (10/11). Sin respuesta en el fichero de tareas del 16/11.
- Vencían hoy diez compromisos míos: nueve dependen de C26 y pasan al 23/11; `voz-3.8-vigilar`, dos de tres hechos, el resto al 23/11.

## Lo roto
Nada que no publique. `MDS-070`: fotograma negro en el plano 6.2 (revisión del 18/11); publicado, no se resube; anotado como `visual-negro-cierre`.
Las vistas: `MDS-063` 2, `066` 7, `067` 3, `068` 1 a 48 h. No es un fallo de producción, es el canal (C26).

## Bucle
`resultados.json` (18/11): B2 sin veredictos («faltan datos»). Nada que aplicar.

## Voz 3.8
`MDS-069` 36,6 s y `MDS-070` 37,2 s (antes 35-40 s), `gemini-3.8-flash-tts`, sin mezcla, `voz_fiel` sin palabras ajenas, lufs −14,3. Bien.

## Decisión (plan v33)
C26 sigue sin respuesta. Preparo el cambio de «se para» (`00_estrategia/tareas/workflows_2026-11-19/producir.yml`, sin el bloque `schedule:`; YAML comprobado: quedan `workflow_dispatch` y `push`). El canal sigue publicando mientras tanto; las mejoras, paradas al 23/11.

## Entrega
Público: `entregar.py --tarea direccion`. Privado: fichero de tareas del 19/11 y `leido.json`.
