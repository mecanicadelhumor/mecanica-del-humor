# C36 con el código de producción · el Short entero en una toma (22/10/2026)

Mismo guion que la muestra del 19/10 (`MDS-045`, el del miércoles 21), para que se pueda comparar.

| Fichero | Qué es | Dura |
|---|---|---|
| `ahora.mp3` | Lo que salió publicado: **una llamada por escena** (cinco tomas de la caché de producción), con las pausas del guion | 47,3 s |
| `c36.mp3` | **Lo nuevo**: el Short entero en **una** llamada, partido por escenas, cada trozo sin sus silencios y con las pausas del guion (las mismas que `ahora.mp3`) | 39,3 s |
| `toma_entera.mp3` | La toma tal como la devolvió Gemini, antes de partirla | 40,3 s |

Las dos versiones acaban con los ~3 s de cola de la firma final. Hecha por el workflow «Prueba de voces»
(run 39788533738, `gemini-3.1-flash-tts-preview`, una petición), con `voz.py` tal como iría a producción.
Whisper oye en cada trozo 10/11, 21/23, 15/15, 22/22 y 25/25 palabras, sin nada repetido.

**Lo que hay que oír:** ¿suena seguido, como una sola persona contando algo, y mejor que `ahora.mp3`?
Es lo que pediste el 19/10: el dirigido, con pausas pequeñas entre escenas.

**Lo que ya sé y tienes que saber:** la toma única es **más rápida** (8 s menos en total). La escena 1 sale
a 3,9 palabras por segundo, por encima del techo de 3,2 que vigila la revisión diaria (el 20/10 marcó como
incidencia `MDS-044` a 3,3). Si te suena bien así, ese techo se revisa para los Shorts de una toma; si te
suena atropellado, se le pide más calma en las notas y se repite la muestra.
