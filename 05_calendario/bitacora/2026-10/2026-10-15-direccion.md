# Dirección en diferido · jueves 15/10/2026

Rutina «Dirección», 13:07 UTC. Sin sesión interactiva hoy (último commit con «dirección» en `main`: el
mío del 12/10). Cuaderno procesado hasta `99755c9` (14/10). Versión 21 del plan.

## Lo roto, primero

- **C66 no comprobaba nada.** Las fichas de `MDS-037`, `038` y `039` traen `voz_fiel` «sin comprobar» en
  las seis escenas. Log del paso de voz del 15/10 (job 116271259739): `Whisper falló con escena_00N.tmp.mp3
  ("open() got an unexpected keyword argument 'metadata_errors'")`. Reproducido en el contenedor con
  PyAV 19.0.1 + faster-whisper 1.2.1; con PyAV 18.1.0 funciona (es con lo que se calibró el 12/10).
  **Arreglo**: `voz.py` `_audio_16k` (ffmpeg → float32 16 kHz) y `corte_palabras.py` igual; `av<19` en
  `requirements.txt`. **Prueba con PyAV 19**: toma buena «20/20 palabras, 0 trozos repetidos»; la misma
  pegada dos veces «40/20, 17 trozos repetidos» → rechazada; `palabras_oidas` da 40.
- El canal publica: `MDS-038` público, `MDS-039` `private` con `publicar_en` 17:00 UTC.

## Cuaderno

1. **Remate descentrado** (12, 13, 14/10). Causa: `escena.html`, `#remate` en vertical con
   `padding-left:40px; padding-right:150px` desde C59 (02/10). Centro del bloque medido en el render: 482-485
   px; con 150/150: 537-540. Muestra en `07_pruebas/remate-2026-10-15/`. Entra con la firma.
2. **Carpetas por mes**: hecho en el público (bitácora y comunicación), `entregar.py` acepta las dos rutas
   (probado: la del mes correcto sí, la de otro mes no, la de un subnivel no). Privado: se le pide al
   codirector cambiar `tareas/direccion.md`.

## Respuestas del 12/10

- Tarea 1 (arranque de la rutina): hecha, esta ejecución leyó del privado.
- Firma: sí → `REMATES` en `render.py`, «un mecanismo nuevo cada día». Desde `MDS-040`.
- Largos: `LARGOS_2026-10.md` §8. Uno a la semana desde el 8/11; sin rama «se para».
- VRoid: hecho (`avatar.vrm`, VRM 1.0, uso comercial individual, sin redistribución ni alteraciones).

## C36 en vivo

`voz_prueba.yml` lanzado a mano (run 38741425047) con `MDS-041` y `gemini-2.5-pro-preview-tts`: la llamada
«sin dirección» no contestó entre 13:17:50 y 13:37:41 UTC; cancelado por el tope de 20 min. No relanzo con
3.1 (misma cuota diaria que `MDS-040`) ni con 2.5 flash (respaldo de producción). `prueba_voz.py`: tope de
240 s por llamada. Al lunes.

## Métricas

`control_c26` 64 (12/10). `MDS-036` 321 a 48 h, «se quedaron» 15,6 %. `MDS-037`-`039` a 0 en la diaria de
las 12:07 UTC (retraso de Analytics). B1: «faltan datos» en los dos brazos.

## Sin mirar

Trampa 55. La caja punteada vacía que la revisión vio en `MDS-039`/4: el fotograma de la ficha (27,19 s)
es de mitad de la animación; la segunda caja se llena después. No es defecto.

## Ficheros

`03_produccion/pipeline/{voz.py,corte_palabras.py,render.py,escena.html,voz_precache.py}`,
`04_agentes/{entregar.py,prueba_voz.py,validar_guion.py}`, `requirements.txt`, `00_estrategia/{PLAN_DE_CAMBIOS,
PROMPT_DE_ARRANQUE,LEEME,PROPIEDAD_DE_FICHEROS,LARGOS_2026-10}.md`, los cuatro prompts de `tareas/`,
`05_calendario/bitacora/` y `08_comunicacion/` (movidas por meses), `07_pruebas/remate-2026-10-15/`.
