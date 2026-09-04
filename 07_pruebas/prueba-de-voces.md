# Prueba de voces — ¿merece la pena cambiar de motor de voz? (C7)

**Pedida por:** la dirección, 4 de septiembre de 2026.
**Material:** `07_pruebas/prueba-de-voces/`, generado por
`04_agentes/prueba_voz.py` sobre `MDS-010.es.json` con el workflow
`voz_prueba.yml`.

## Qué hay que escuchar, en este orden

1. `edge.mp3` — lo que sale hoy. La referencia.
2. `gemini_plano.wav` — el guion entero, sin dirección.
3. `gemini_dirigido.wav` — el guion entero, con dirección de actor.

## La pregunta

**¿Suena alguna de las dos de Gemini lo bastante mejor que `edge` como para
justificar cambiar el motor de voz de la producción diaria?**

- **Sí** → C7 escalón 2 entra la semana del 14, con salvaguardas.
- **No** → el escalón 1 vuelve a la mesa, o C7 se aparca y la ranura de esa
  semana se usa en otra cosa.

## La respuesta

**4 de septiembre, Silvestre:** «Gemini_dirigido mejora a edge. Gemini_plano está
parejo con gemini_dirigido, aunque creo que mejor ligeramente este último, pero
no estoy seguro. Lo que hay es una diferencia de volumen: gemini_plano se escucha
más fuerte y claro que gemini_dirigido.» **Cambio aprobado.**

**4 de septiembre, la dirección — lo que dicen las ondas, que el oído no podía
separar:**

| | Duración | Voz | Ritmo | RMS solo voz |
|---|---|---|---|---|
| Objetivo del guion | **50,7 s** | — | — | — |
| `edge` | 41,4 s | 41,4 s | 2,63 pal/s | — |
| `gemini_plano` | 37,4 s | 23,0 s | **4,74 pal/s** | −16,3 dB |
| `gemini_dirigido` | **83,2 s** | 41,3 s | **2,64 pal/s** | −18,5 dB |

1. **La dirigida no lee las instrucciones en voz alta**, que era la sospecha
   ante 83 segundos: su tiempo de voz coincide con el de `edge` hasta la décima.
   **Los 42 segundos de más son silencio**, porque se tomó al pie de la letra una
   instrucción mía de dejar pausas largas.
2. **La plana corre**: 4,74 palabras por segundo es casi el doble del habla
   natural. Suena «más clara y más fuerte» porque es más densa y no respira.
3. **La diferencia de volumen no importa**: 2,2 dB en la voz sola, y
   `montaje.py` normaliza todo a −14 LUFS. En producción desaparece.

**Decisión:** entra Gemini, pero con **una llamada por escena** y **sin pedir
pausas** —las ponemos nosotros desde `pausa_despues_s`—, y **solo en los Shorts**:
el nivel gratuito da 10 peticiones al día y un episodio largo son 40 escenas.
Desarrollo y salvaguardas en `00_estrategia/PLAN_DE_CAMBIOS.md`, versión 5.1.

**Lo que la prueba también descartó, y no era su pregunta:** cortar el audio por
los silencios para repartirlo entre escenas. 16 tramos para 6 escenas en la
plana, 33 en la dirigida, y ningún umbral da 6 (probado a 0,6 · 0,8 · 1,0 s:
salen 8, 5 y 4). Ver `informe.txt`.
