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

## El resultado de Kaggle (llegó hoy: cuatro ejecuciones del workflow)

| Hora | Qué pasó |
|---|---|
| 14:02 | **LatentSync 1.6 funciona** a la primera (4 min). Wan: sin memoria, pero con el dato que faltaba (`atencion_eficiente_fp16: true`): el modelo entero en fp16 son 10 de los 14,5 GB |
| 14:21 | Wan por grupos: se cayó en una línea mía (`enable_group_offload` no existe en los modelos de transformers). Corregido y probado aquí sobre los dos modelos en miniatura |
| 14:45 y 14:57 | Dos ejecuciones muertas en `apt-get update` del runner (10 min sin escribir nada). Workflow arreglado, preparado para que lo mueva el codirector (`workflows_2026-10-26/`) |
| **16:07** | **Wan funciona**: `fp16_bloques` a la primera, 704×1280, 77 fotogramas, **pico 13,5 GB**, 54,6 min. Y `b_latentsync_wan.mp4`: cabeza generada **y** labios |

**Mi lectura, sin adornos**: el camino está abierto (resolución completa, nada pixelado, licencias
limpias), pero **Wan tal como se lo pedí se mueve menos que el truco barato** (0,28 frente a 0,87 de
diferencia media entre fotogramas) y cuesta 18 minutos de GPU por segundo de vídeo. Le pedí quietud y me
la dio. El jueves 29: indicación con un gesto claro, 30-35 pasos en vez de 50, y entonces se decide
(`C51.3-wan-gesto`). Lo que el codirector tiene que mirar son los dos vídeos (`C51.3-ver-videos`).

**Trampa que me llevo**: no es solo «mira qué ocupa la memoria» (trampa 64). Es que **pedí quietud y
medí movimiento**: la indicación y lo que se quiere medir tienen que decir lo mismo, o el experimento
contesta otra pregunta.
