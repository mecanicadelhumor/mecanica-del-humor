# Sesión de dirección — miércoles 23 de septiembre de 2026 (extraordinaria)

Sesión con el codirector delante, desde su ordenador (carpeta conectada), abierta a las 08:55 de
España. La pidió él con tres notas seguidas en `PROMPT_DIRECCIÓN.md` (21, 22 y 23) sobre guiones
sin hilo, y una cuarta en la del 23 sobre la presentación. Arranque con `PROMPT_DE_ARRANQUE.md` y
`PROMPT_DIRECCIÓN.md`, y lectura del orden de siempre: `LEEME.md`, `REGLAS.md`,
`PROPIEDAD_DE_FICHEROS.md`, `PLAN_DE_CAMBIOS.md` (versiones 10 y 11 enteras), `estado/` (el más
alto era el del 22: la revisión de hoy aún no había corrido), `08_comunicacion/` entera, las
bitácoras del 21 y el 22, y la parrilla y el registro de `origin/main` (clon aparte: la carpeta del
codirector iba dos commits por detrás).

Razonamiento completo en la **versión 12** del plan. Aquí, lo hecho y en qué orden.

---

## 1 · Los guiones (C48 y C48.1)

- **Leídos los ocho Shorts** del 16 al 25 contra lo que dijo el codirector. El patrón: el chiste y el
  estudio eran dos historias (o les faltaba la frase que las unía), las juntas se habían quitado
  para caber en la serie —el 18/09, en una reescritura mía—, y los cierres acababan en una frase
  que había que descifrar. Medido de paso: 23 de 25 Shorts abren con «mi X» y 25 de 25 cierran con
  «y aquí falla».
- **Fuentes releídas hoy:** `G03` entera (texto completo en ejop.psychopen.eu; DOI
  10.5964/ejop.v6i3.211, que la ficha no tiene), `G04` (PDF de Loma Linda: **el cortisol sí es
  resultado del estudio**, al contrario de lo que decía la nota del 17/09) y la ficha de `L04`.
- **`MDS-023`, `024` y `025` reescritos**, con el campo `historia`. Validador sin errores. **Barrera
  de C21 en las 18 escenas**, 21 instantes por escena, con las tipografías de marca instaladas: cero
  problemas. Visto el render de cada escena.
- **Defecto encontrado al mirar el render:** `contar()` de `escena.html` pintaba los decimales con
  punto. Arreglado; y la cifra de `MDS-025` va como «43,6%» (con espacio el «%» bajaba de línea; con
  espacio duro no cabía y la barrera paraba el render).
- **`validar_guion.py`:** C38 (serie ±12 %, remate en el segundo 10) de error a aviso; puerta nueva
  de C48 (`historia` y `lectura_en_frio`, error desde `MDS-026`); C48.1 (cierre que empieza igual
  que uno de los cuatro anteriores, aviso); y el saludo «qué tal» solo cuenta al principio de la
  frase (falso positivo que paró la primera versión de `MDS-023`). **Comprobado contra los 33
  guiones del repositorio: ninguno da más errores que antes y ninguno revienta.**
- **Prompts:** sección nueva «Lo primero de todo: la historia» en `guionista_corto.md` (con el
  encargo literal para el lector en frío y la séptima regla, la de las fórmulas);
  `planificacion-jueves.md` (orden de escritura nuevo en el paso 2); `revision-diaria.md` (lectura
  en frío del Short de mañana como primer paso, y los avisos del codirector en `novedades.md` como
  primer hallazgo). `REGLAS.md`: 13.2 corregida, 13.3 nueva, regla 12 precisada.
- **El codirector leyó las tres narraciones en la conversación** antes del push: *«se entienden
  mejor, pero ¿por qué todos tienen "y aquí falla"?»*. Los tres cierres, reescritos (C48.1).

## 2 · `MDS-023` se rehace hoy

- `parrilla.json`: `rehacer_video_id: X1GAp3OUgKg` en la emisión del 23, y **una segunda emisión
  de `MDS-023` el sábado 26 como red de seguridad**. Simulado con `cola.py` contra el registro de
  `origin/main`: el 23 produce; el 26 produce solo si el 23 no llegó a hacerlo.
- **El codirector borró `X1GAp3OUgKg` en Studio** e hizo dos push: `cc1f105` (09:41) y `8163e26`
  (09:45, los cierres nuevos). A las 09:46 los dos intentos de producción que quedaban del día (los
  de las 04:47 y las 08:23 UTC, que llegan con horas de retraso) no habían corrido todavía: el
  primero que corra produce el `MDS-023` nuevo.
- Voz: el 023 gasta hoy la cuota de 3.1 que usará el 024 esta noche; si no le llega, el 024 sale
  entero con 2.5 (C33.1). Dicho al codirector.

## 3 · La sincronización del registro (C49)

No estaba rota: el commit `77d6c7a` del 22/09 a las 13:41 UTC pasó `MDS-021` a `public`. Corre con
cuatro o cinco horas de retraso y la revisión lee antes. Comprobado con la API de Actions (las
ejecuciones del 21 fueron a las 15:21 y 15:52 UTC, antes de que `MDS-021` se publicara). De paso,
**`metricas.py` escribía el registro con sangría 1 y `registrar.py` con sangría 2**, y cada día el
fichero se reescribía entero en git. `metricas.py` pasa a sangría 2.

## 4 · La imagen (C50) y el presentador (C51)

- Investigado: Pexels (200 peticiones/hora, 20.000/mes), Pixabay (100/minuto), Cloudflare Workers AI
  (10.000 unidades diarias gratis, bloqueo y no cobro; FLUX.1 schnell, unas 58 por imagen cuadrada),
  la política de YouTube de contenido no auténtico (15/07/2025) y el campo
  `status.containsSyntheticMedia` de la API. Ni el contenedor ni el ordenador del codirector llegan
  a esas APIs (403 del proxy): **solo GitHub Actions**.
- Escrito y probado: `03_produccion/pipeline/visual.py` (busca y genera; probado con respuestas
  simuladas de las tres APIs) y `muestrario_visual.py` (monta hojas de contactos y previas; probado
  de punta a punta con vídeos e imágenes sintéticos: hojas A, B y C y dos previas de 46 s). El
  workflow `visual_prueba.yml` está en `07_pruebas/visual-23-09/`, para que el codirector lo cree.
- @Maestro_Seductor: **no he podido ver el vídeo** (YouTube devuelve 429 a la descarga automática).
  Su título, por oEmbed: «La Mentalidad para Atraer Sin Rogar». Respuesta en C51.

## 5 · Operativo, para la próxima sesión

- **Se me volvió a quedar un `.git/index.lock`** en la carpeta del codirector (un `git status` sin
  `--no-optional-locks`). Movido a `_to_delete/`. Trampa 40.
- Clon de trabajo de `origin/main` en el dispositivo: `~/remoto` (sin checkout, blobs a demanda).
- `validar_viejo.py` (el validador de antes de hoy, para comparar) se escapó a
  `04_agentes/_validar_viejo_tmp.py` y está movido a `_to_delete/`.

## Lo que queda

- Tarea 2 del codirector (cuentas, claves, workflow) → muestrario → decisión el viernes 25.
- Jueves 24, 22:00: primera planificación con C48. El viernes se miran sus cinco lecturas en frío.
- Push pendiente: este fichero, `LEEME.md`, el código de C50 y `07_pruebas/visual-23-09/` (van en
  el de la tarea 2.5).
