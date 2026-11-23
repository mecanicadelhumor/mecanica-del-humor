# Dirección en diferido · 2026-11-23 (lunes)

## Antes de nada
- `origin/main` 4ec7a9e (revisión diaria, 10:31 UTC). Sin sesión interactiva hoy (ningún commit de «dirección» que no sea mío desde el 19/11).
- Ramas `claude/entrega-*` vivas: `entrega-direccion-20261112-1323` y `entrega-revision-20261104-1031`, obsoletas; el codirector puede borrarlas.
- Cuaderno del codirector sin cambios desde 83c6c46 (10/11). Sin respuesta en el fichero de tareas del 19/11. `producir.yml` de `main` sigue con sus tres cron (no ha movido el de «se para»).
- Vencían hoy trece compromisos míos: `voz-3.8-vigilar` hecho; once que dependen de C26 al 30/11; `voz-sdk-3` al 07/12.

## Lo roto
- **La parrilla no tiene nada del 27 al 29/11.** El reintento de la planificación solo mira el lunes siguiente. Nota a la planificación: el jueves 26 llena primero esos tres días (`plan-27-29`).
- `MDS-075` salió sin animación (brazo A) y queda apartado.
- Nada más: se publica cada día, la revisión no ve defectos que paren nada.

## Bucle
`resultados.json` (22/11): «faltan datos» en todo. B2 acababa el 28/11 sin poder llegar a 6 por lado: **ampliado hasta el 22/12** (posiciones 25-48, `random.Random(20261123)`, comprobado que la semilla 20261102 reproduce las posiciones 1-24). Regla sin cambios. `bucle.py --imprimir` corre con el `ciclos.json` nuevo (el `resultados.json` de la prueba no se entrega).

## Voz 3.8
`MDS-071` bien (ficha del 20/11). Los tres primeros, bien. Se sale a veces el ritmo de una escena (071, 072, 075).

## C26
Mediana de los veinte últimos con dato: 21,5 (calculada hoy con `resultados.json` y `metricas_diarias.json`; igual que `control_c26`). `MDS-070` 65 y `MDS-071` 165. Recomendación: parar. Sin respuesta.

## Decisión (plan v34)
B2 ampliado; la planificación llena 27-29/11; mejoras al 30/11.

## Entrega
Público: `entregar.py --tarea direccion`. Privado: fichero de tareas del 23/11 y `leido.json`.
