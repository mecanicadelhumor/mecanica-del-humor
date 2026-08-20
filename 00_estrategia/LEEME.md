# 00_estrategia — Léeme primero

Análisis del 20 de agosto de 2026 sobre por qué el canal no arranca y qué cambiar.
Escrito para que **cualquier conversación del proyecto** pueda aplicarlo sin rehacer el
análisis.

## Los tres archivos, en orden

| Archivo | Qué es | Cuándo se lee |
|---|---|---|
| **`REGLAS.md`** | Las restricciones que nadie puede saltarse: ética, rigor, coste cero, cómo se cambian las cosas | **Siempre, antes de tocar nada.** Es corto |
| **`PLAN_DE_CAMBIOS.md`** | Los 14 cambios, en orden de dependencia, con archivos afectados y criterios de aceptación | Al ir a hacer algo |
| **`DIAGNOSTICO.md`** | El análisis completo: canales de referencia, por qué triunfan, y las 8 causas del problema | Cuando haga falta entender **por qué**, o para discutir el rumbo |
| **`panel.html`** | El resumen visual de una página | Cuando quieras la foto entera sin leer |

## El resumen en cuatro líneas

1. El canal **no tiene un problema de calidad, tiene un problema de distribución.** Los
   vídeos están bien hechos y se publican en la única superficie de YouTube a la que un
   canal sin audiencia no puede llegar.
2. Las tres superficies que sí puede alcanzar —**búsqueda, feed de Shorts y enlaces desde
   fuera**— no se están usando en absoluto.
3. Los tres cambios de los que depende todo: **un solo canal** (C1), **Shorts a diario**
   (C2), **un personaje y miniaturas que se vean** (C4 y C5).
4. Antes que nada: **averiguar por qué GitHub Actions lleva sin ejecutarse desde el 19 de
   agosto** (P0.1). Sin producción no hay nada que arreglar.

## Estado a 20 de agosto, tarde

**Las fases 1 y 2 están escritas en el repositorio** y las tres tareas programadas
reescritas. La tabla completa, con qué fichero trae qué, está al principio de
`PLAN_DE_CAMBIOS.md`.

Lo que falta para que el canal nuevo respire: producir el primer Short (`MDS-001`) y
mirarlo con las tipografías reales.

**Decisiones tomadas** (el razonamiento, en `PLAN_DE_CAMBIOS.md`):

- **Un solo canal, en español.** El inglés se sirve con el doblaje automático de YouTube,
  ya activado. Se reabre `@humormechanics` solo si las pistas dobladas superan el 25 % del
  tiempo de visionado a las ocho semanas.
- **No se clona la voz de Silvestre por ahora.** Su condición —que no salga de un entorno
  local o muy seguro— es incompatible con un repositorio público y runners sin GPU. En su
  lugar, Gemini TTS con dos hablantes, que resuelve el mismo problema sin datos de nadie.
- **Los subtítulos quemados se retiraron** por decisión editorial. No los vuelvas a
  encender: el motivo está en `MEJORAS.md` del 20/08 y en C6.1.

## Relación con los documentos que ya existían

- `SIGUIENTES_PASOS.md` y `05_calendario/CALENDARIO.md` quedan **superados** en lo que
  toca a cadencia, idiomas y métricas de decisión. Ver C1, C8 y C14.
- `03_produccion/MEJORA_VISUAL.md` sigue **plenamente vigente**: sus siete reglas para
  tocar el diseño se mantienen, y su backlog (V1–V9) se integra en C4, C5 y C6.
- `05_calendario/MEJORAS.md` sigue siendo el registro histórico. Se añade al final, nunca
  se reescribe.
- El criterio editorial de `SIGUIENTES_PASOS.md` —cada vídeo termina diciendo dónde falla
  lo que acaba de explicar— **no se toca**. Está recogido como regla 11 en `REGLAS.md`.
