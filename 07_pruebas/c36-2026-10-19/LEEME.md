# C36 en vivo · el Short entero en una sola toma (19/10/2026)

Guion: `MDS-045` (cinco escenas). Workflow «Prueba de voces», `gemini-3.1-flash-tts-preview`, dos
llamadas: `gemini_plano.mp3` (sin dirección de actor, 37,6 s) y `gemini_dirigido.mp3` (con dirección,
50,2 s). Las dos contestaron en un minuto.

Antes, con `gemini-2.5-pro-preview-tts` (15/10 y hoy a las 13:17 UTC): ninguna respuesta en 20 minutos,
las dos veces. **Ese modelo no sirve para nosotros**; los largos irán con `3.1`.

## Prueba 1 · ¿se puede partir la toma por escenas? Sí

`03_produccion/pipeline/corte_palabras.py` sobre las dos tomas:

| Toma | Corte 1-2 | 2-3 | 3-4 | 4-5 | Hueco entre escenas |
|---|---|---|---|---|---|
| plano | 3,81 s | 13,41 s | 19,93 s | 28,45 s | 0,94-1,00 s |
| dirigido | 4,01 s | 21,17 s | 30,46 s | 40,29 s | 1,48-2,06 s |

Los ocho cortes caen entre la última palabra de una escena y la primera de la siguiente («…tu dinero |
cena de…», «…se parte | diez minutos…», «…los cubiertos | unos psicólogos…», «…ganaban | el chiste…»), en
silencio de verdad (RMS 1-3 sobre 32.767). Whisper casa entre el 88 y el 100 % de las palabras de cada escena.

## Lo que falta

- **Que el codirector lo oiga** (regla 11.2): ¿suena como un vídeo, mejor que seis tomas pegadas? La
  dirigida mete pausas de casi dos segundos entre escenas: el render las respetaría, y el Short duraría
  50 s en vez de ~41. Si gusta la plana, el ritmo es el de ahora.
- Pruebas 3 y 4 del diseño del 15/09 (una tanda de seis Shorts sin deriva; desfase de sincronía < 0,5 s):
  piden meter el corte en `voz.py`, que es el trabajo de la dirección del jueves 22.
