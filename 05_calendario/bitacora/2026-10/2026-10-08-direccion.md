# Bitácora · dirección en diferido · 2026-10-08 (jueves)

Rutina «Dirección», 13:07 UTC. Primera ejecución. Detalle de lo decidido: versión 19 de
`00_estrategia/PLAN_DE_CAMBIOS.md`.

## 0 · Antes de nada
- `origin/main` del público: último commit `740cdd3` (bot, MDS-034, 11:48 UTC). Ningún commit de
  «dirección» de hoy ajeno a esta rutina: **no hubo sesión interactiva**, así que se trabaja.
  `refs/heads/claude/entrega-*`: ninguna rama pendiente.
- `direccion/leido.json` no existía (primera ejecución). Cuaderno leído entero: puntos 1 y 2 (06/10)
  y, añadido durante la ejecución (08/10 13:25 UTC), el punto 3. El codirector escribió además en la
  sesión: «hay una tarea 3, no la olvides», «es error mío, el canal es "psychtoons"» y la pregunta por
  Kurzgesagt.
- Tareas del 05/10: 1-5 hechas según su respuesta; la 6 (VRoid) pendiente, por su cuenta.

## 1 · Lo roto
- `MDS-034`: el run de producción de las 07:22 UTC murió en «Instalar dependencias» (avería del
  runner, revisión diaria). El reintento lo subió a las 11:48 UTC, `private` con `publicar_en`
  17:00 UTC: llega a su hora. Nada que hacer.

## 2 · El bucle
- `resultados.json`: B1 empieza el 12/10, sin datos. Nada que aplicar.
- Decidido antes de ningún dato: si el 25/10 algún brazo no tiene 6 Shorts medidos, B1 sigue hasta el
  01/11 como mucho (versión 19).

## 3 · Los puntos del cuaderno
1. **`MDS-016`** → `00_estrategia/ANALISIS_MDS-016.md`. Ninguna hipótesis adelanta a B1; la familia
   `mensajes` entra como exploración de tema (2 de 7 por semana, con ficha real), con etiquetas
   `familia_tema` y `chiste` en cada guion. Cola de hipótesis actualizada (`H-016-*`).
2. **Reglas de producción** → `00_estrategia/REGLAS_DE_PRODUCCION.md`, y `regla_afectada` en cada
   hipótesis.
3. **PsychToons (y Kurzgesagt)** → `00_estrategia/REFERENTES_2026-10-08.md`; `H-ilustracion-ia` en cola.
   Primero se buscó «Phsycomaths»: el canal grande con ese nombre (hoe_math, PsychoMath) dibuja a mano;
   el codirector aclaró el nombre en la sesión.

## 4 · Lo previsto (versión 18)
- **C55.2**: `03_produccion/pipeline/animacion.py` nuevo; `render.py` y `qa.py` tocados. Probado con
  `/usr/bin/python3` (Playwright 1.56, que casa con el Chromium del entorno): camino de siempre, camino
  C50 y siete casos de fallo; todos sacan el vídeo y la escena que falla sale como el control. Muestra:
  `07_pruebas/animacion-2026-10/c55-2_mezcla_MDS-027.jpg`. Prompt de la rutina «Animación»:
  `00_estrategia/tareas/animacion.md` (la crea el codirector).
- **C36**: no hecho (falta el código del corte por palabras). Lunes 12.
- Encontrado: el render no es determinista entre dos pasadas (trampa 55).

## 5 · Ficheros
Público: `00_estrategia/{ANALISIS_MDS-016,REGLAS_DE_PRODUCCION,REFERENTES_2026-10-08}.md` (nuevos),
`PLAN_DE_CAMBIOS.md`, `PROMPT_DE_ARRANQUE.md`, `LEEME.md`, `PROPIEDAD_DE_FICHEROS.md`,
`tareas/planificacion-jueves.md`, `tareas/animacion.md` (nuevo), `05_calendario/bucle/hipotesis.json`,
`03_produccion/pipeline/{animacion.py (nuevo),render.py,qa.py}`, `07_pruebas/animacion-2026-10/`,
esta bitácora y `08_comunicacion/2026-10-08-direccion.md`. Entregas: dos (`entregar.py`).
Privado: `tareas/tareas_codirector_2026-10-08.md`, `leido.json`.
