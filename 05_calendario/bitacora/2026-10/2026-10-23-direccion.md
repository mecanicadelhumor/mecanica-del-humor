# Dirección · viernes 23 de octubre de 2026 (extraordinaria)

Rutina «Dirección» lanzada fuera de su día, con el codirector delante y contestando. Sin otra sesión de
dirección hoy (último commit de dirección en `main`: el mío del 22/10). Cuaderno procesado hasta `4986b5a`.
Versión **24** del plan.

## Lo roto, primero

- **El muestrario VRoid del 16/10 no se hizo, y nadie lo dijo hasta el 22/10.** Rastreado: el avatar
  entró el 13/10 (`4f95779`); la fila del calendario de la versión 21 no tenía dueño; la dirección del
  15/10 no lo hizo ni lo apuntó en «Sin mirar»; la del 19/10 no lo nombró; la revisión diaria no mira el
  plan. Con él, el muestrario 2D (12/10) y la prueba de Kaggle (13-15/10). Culpa de la dirección.
  Arreglo: C70, `05_calendario/compromisos.json` + paso 0 de la revisión diaria. Trampa 62.
- El canal publica: `MDS-047` hoy (estado del 22/10: OK). B1 sin cambios desde ayer.

## Hecho

1. **C70**: `compromisos.json` (14 filas), bloque del 23/10 y línea «Plazos vencidos» en
   `tareas/revision-diaria.md`, bloque en `tareas/planificacion-jueves.md`, fila en
   `PROPIEDAD_DE_FICHEROS.md`.
2. **Muestrario 2D** (`07_pruebas/personaje-2026-10/muestrario-2d-2026-10-23/`) y **VRoid**
   (`…/muestrario-2026-10-23/`), hechos hoy por subagentes y mirados (hoja de caras y fotogramas). Vídeos
   ligeros a 540×960 añadidos con `git add -f` (`.gitignore` excluye los `.mp4` de `07_pruebas/`).
3. **C51.3**: prueba de Kaggle preparada (`07_pruebas/presentador-2026-10/PRUEBA.md`); workflow en
   `00_estrategia/tareas/workflows_2026-10-23/`. Sin ejecutar: no hay claves aquí.
4. **C36 encendido** (`voz.py`), **C36.1** rótulo de situación (0,7 s antes y después; Whisper parte el
   trozo; probado con la toma real de `MDS-045` con Gemini simulado: una petición, «rótulo con 0.70s
   detrás»; y el caso que falla: frontera no encontrada → la escena se queda como estaba). Calibrado en las
   612 escenas: 5 rótulos. **C36.2** techo de ritmo 4,2 en la toma única (`voz.py`, `qa.py`).
   `VERSION_UNA_TOMA = 2` (la caché de tomas únicas anteriores no se reutiliza; no hay ninguna en
   producción). Muestra: `07_pruebas/c36-2026-10-23/c36_rotulo.mp3`.
5. **Planificación**: C17 no aplica a los largos; temas en reserva (`temas_en_reserva.md`, suyo; añadido a
   `entregar.py`).

## No hecho

- **La cola final** (≈3 s): pendiente de que el codirector elija (a/b/c). Compromiso `C36-cola`, lunes 26.
- Imagen horizontal y voz por tandas del largo: lunes 26, como estaba.
- Propuestas de iteración y calidad: escritas (plan v24 y sus tareas); nada cambia hasta que conteste.


---

# Segunda ejecución · 23/10, ~08:30 UTC (en diferido, «Run now» del codirector)

## Leído

- Cuaderno (`29d23d1`): «Revisión extraordinaria. Urgente el workflow de la Tarea 3, que no funciona.»
  Y sus respuestas en el fichero de tareas del 23/10.
- Ninguna sesión interactiva nueva hoy (el commit de dirección de las 07:52 es de la propia dirección).
  El canal publica; B1 sin datos nuevos desde ayer; la revisión diaria de hoy aún no ha corrido (09:28).

## Hecho

1. **Lo roto — el workflow de la tarea 3.** Las ocho caras: HTTP 400, `'/seed' not allowed`. FLUX.1
   [schnell] ya no admite semilla. `caras.py` pasa a FLUX.2 [klein] 4B (el de producción, con semilla,
   multipart, 1024×1024), con schnell sin semilla de respaldo. Probado con un Cloudflare simulado que
   rechaza `seed` en schnell: 8 caras con klein y sus semillas; 8 con schnell (`null`) si klein cae; el
   código viejo, el mismo 400. El workflow no cambia. `PRUEBA.md` lo cuenta.
2. **El mismo fallo en producción, latente**: el respaldo de `visual.generar` mandaba `seed` a schnell.
   Quitado. Solo corre si klein falla: no cambia lo que se ve. Trampa 63.
3. **Respuestas del codirector** a `compromisos.json` (hechas, nuevas con dueño y fecha) y versión 25 del
   plan: cola (b) el lunes 26; los dos personajes en un brazo; esquina libre (2/11); 14 por semana,
   factorial, bayesiano y filtro; patrón de calidad.

## No hecho

- **No he lanzado el workflow**: no puedo (ni Actions ni claves desde aquí). Lo relanza el codirector.
- La cola (b): el lunes 26, con su muestra, como estaba prometido.
- La viñeta de compromisos en `tareas/direccion.md` (privado): sigue pedida al codirector.

## Tercera ejecución · 23/10, ~09:00 UTC (con el codirector delante)

- El codirector relanzó `caras`: run verde, ocho caras con klein, **pero ningún commit**. Causa: `git add -A
  caras salida` falla entero si `salida/` no existe, y el `|| true` lo calla. Las caras, copiadas del
  artefacto a `07_pruebas/presentador-2026-10/caras/`. Arreglo sin tocar el workflow:
  `salida/.gitignore` con `!*.mp4` (también deja subir los vídeos de `kaggle`, que el `.gitignore` de la
  raíz excluía). Probado en una copia del repositorio. Hoja mirada: ocho adultos ficticios, fondo azul
  marino, sin texto.

## Cuarta ejecución · 23/10, ~09:20 UTC (con el codirector delante)

- **Caras elegidas**: la 2 (principal), la 6 (alternativa, brazo 2 frente a 6 más adelante) y la 4
  (reservada para vídeos muy serios). `caras/eleccion.md` y `compromisos.json`.
- **Primer «kaggle» (cara 2)**: dos minutos, sin vídeo. Kaggle sin GPU, sin internet y sin encontrar la
  entrada. La metadata y la CLI piden bien GPU e internet; lo más probable es que la cuenta no tenga el
  teléfono verificado (se le pide al codirector). Lo nuestro, arreglado: la entrada se busca en todo
  `/kaggle/input`, el cuaderno para y lo explica si falta GPU o internet, el run sale en rojo sin vídeo, y
  `salida/.gitignore` ya no se borra. Probado en el contenedor (PRUEBA.md).

- **Segundo «kaggle» (~09:33 UTC, con GPU)**: dos T4, internet y entrada bien; sale el vaivén
  (`a_movimiento_afin.mp4`), pero Wan y MuseTalk caen porque el diffusers de git main subió
  `huggingface_hub` a 2.3.0 y el transformers de Kaggle pide <2.0. Arreglo: diffusers de PyPI y
  `huggingface_hub>=1.5,<2` en los dos `pip install`. Relanza el codirector.
