# Bitácora de la dirección · lunes 26/10/2026 (en diferido, 13:24 UTC)

Sin sesión interactiva hoy (último commit de dirección en `main`, el mío del 23/10). Cuaderno: un punto
nuevo (commit `c70f5e6`): **Wan volvió a fallar en Kaggle; que funcione, sin bajar calidad, y si no es
creíble, no se mete**. El codirector añadió además la viñeta de `compromisos.json` a mi prompt (la tarea
pendiente del 23/10: hecha).

## Lo vencido o que vencía hoy (dueño: dirección)

| Compromiso | Qué ha pasado |
|---|---|
| `C51.3-latentsync` | **Hecho**: en el cuaderno de Kaggle, probado en CPU de punta a punta |
| `C36-cola` | **Muestra hecha**, sin aplicar (regla 11.2) → 29/10 |
| `largo-imagen-horizontal`, `largo-voz-tandas` | **Aplazados al 29/10**: el día fue para Wan; el ensayo del 2/11 llega |

## Lo hecho

1. **Wan (C51.3)**. Causa real del fallo: la T4 no tiene bf16 de verdad y con bf16 PyTorch no puede usar
   la atención eficiente: guardaba la matriz de atención entera. Bajar a 384 y 320 no lo arreglaba (y el
   intento fallido retenía su memoria). Nuevo: fp16 (y bf16 con atención en fp32 si fp16 desborda, se
   detecta en el primer paso con NaN), **704×1280 vertical, 50 pasos, sin tamaños de respaldo**, cada
   intento en un proceso propio, informe de memoria y tiempos. Trampa 64.
2. **LatentSync 1.6** como labios (boca a 512, coherente), MediaPipe en lugar de InsightFace, entorno con
   uv y Python 3.10, fp16 forzado, respaldo 1.5. Probado en el contenedor: el recorte con la cara 2, el
   entorno con las versiones exactas y la 1.5 de punta a punta en CPU sobre el vaivén vertical.
3. **Lanzado el workflow** `kaggle`, cara 2 (run 8, 13:48 UTC), yo misma.
4. **Cola (b)**: muestra en vídeo, antes y después, con la voz real de MDS-045
   (`07_pruebas/cola-2026-10-26/`). El cambio, en `cola_b.diff`.
5. **B1 · B gana** (n = 4, +21,6 pp, sin reparo, prob 0,90). Control de B2 = B. B1 sigue para resolver A.
   Lo que no me gusta (cuatro Shorts con pocas vistas) va como regla para B2, no para B1.
6. Plan v26, `compromisos.json`, nota a las rutinas, tareas del codirector.

## El resultado de Kaggle

(Se completa abajo si llega antes de cerrar esta ejecución; si no, lo leo el jueves 29.)
