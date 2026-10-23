# C36 encendido, con el rótulo de situación (23/10/2026)

El mismo Short de siempre (`MDS-045`), con la **misma toma de Gemini** que oíste el 22/10
(`../c36-2026-10-22/toma_entera.mp3`; ninguna petición nueva) y el `voz.py` que entra en producción hoy.

| Fichero | Qué cambia frente a `../c36-2026-10-22/c36.mp3` |
|---|---|
| `c36_rotulo.mp3` (39,8 s) | **«Cena de empresa.»** lleva ahora 0,7 s de pausa delante (eran 0,41) y 0,7 s detrás (eran 0,57) |

**Lo que se ha visto al medirlo:** la pausa de detrás ya existía (0,57 s) y aun así se colaba. Whisper oye
«cenadempresa» como una sola palabra: Gemini lo dice deprisa y pegado. Por eso hay dos arreglos:

1. **Las pausas**, garantizadas por el código: el trozo de la escena se parte por Whisper entre el rótulo y
   el resto y se pegan con 0,7 s de silencio. Si Whisper no encuentra la frontera, la escena se queda como
   estaba (nunca se pierde la toma por esto; probado).
2. **La forma de decirlo**, que solo se oirá en la primera toma nueva: la dirección de esa línea le pide a
   Gemini «dilo como el título de la escena, con una pausa breve antes y otra después».

**Qué cuenta como rótulo:** en la escena 1 o 2, una frase de 2 a 4 palabras, sin comas, con «de», «del»,
«con» o «en» y seguida de más narración. Medido sobre las 612 escenas de todos los guiones: marca solo
cinco («Cena de empresa», «Videollamada de trabajo», «Grupo de la familia», «Cena con amigos», «Comida del
domingo») y ninguna frase con verbo.

**La cola del final (≈3 s sin voz) no ha cambiado todavía**: ver las tareas del codirector del 23/10.
