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

---

# Tarde · C50 entra en producción (versión 13 del plan)

## 6 · La respuesta del codirector a la prueba

Hizo la tarea 2 entera (cuentas, secretos, workflow, ejecución: `Prueba visual (C50)` en verde,
run 35837673091) y contestó en `07_pruebas/visual-23-09.md`: **A**, con cuatro problemas; B no; C
no hizo nada; y cuatro notas (tarjetas de marca intercaladas, un personaje que mueva los labios o
un avatar dibujado, coherencia entre vídeos, «dinamismo es la palabra»). Pidió empezar a producir
cuanto antes. Decidido: **C50 entra hoy** (versión 13).

## 7 · Lo que se ha visto en los manifiestos de la prueba

- Pexels encontró vertical para los 21 planos de la variante A (1080×1920 o 1080×2048). Pixabay no
  hizo falta ni una vez.
- El «sillón quieto» de `MDS-025` escena 6 era un **vídeo** de Pexels (id 6377183, «chair placed
  next to blank photo frame on wall»): de trípode, sin nada que se mueva. De ahí la medida de
  movimiento.
- La variante C: **21 de 21 planos «sin_imagen»**. `visual.py` capturaba la excepción y no guardaba
  el cuerpo de la respuesta. Sin registro de Actions (403 sin permisos de administrador), la causa
  no se puede saber desde aquí. De ahí el paso `diagnostico`.
- Documentación de Cloudflare leída hoy: FLUX.1 [schnell] **no admite ancho ni alto**; FLUX.2
  [klein] 4B sí (256-1920 px, por formulario multipart, 26,05 neuronas por tesela de salida). Y
  `status.containsSyntheticMedia` **existe en `videos.insert`** (comprobado en la referencia de la
  API de YouTube, no supuesto).

## 8 · Lo escrito y cómo se ha probado

- `visual.py` reescrito (resolvedor de producción: `resolver`, `traer`, `diagnostico`),
  `fondo_visual.py` nuevo (cortes, plan, pista de fondo), `render.py` (modo archivo con respaldo
  automático al render de siempre), `escena.html` (modo archivo: fondo transparente, velo, bandas
  abajo/arriba/centro, `encajarBanda()`), `publicar.py` (créditos y contenido sintético), `qa.py`
  (campo `visual` en la ficha) y `validar_guion.py` (avisos C50). `visual` escrito en `MDS-024` y
  `MDS-025`.
- **Prueba de punta a punta en el contenedor, sin red a las APIs:** clips sintéticos (con
  movimiento, quieto, con una cara abajo, con una cara arriba, horizontal con la cara a un lado) y
  las respuestas de Pexels, Pixabay y Cloudflare simuladas; voz falsa por escena (pitidos por
  palabra y silencios en la puntuación) de la que se sabe dónde empieza cada palabra.
  - El resolvedor descarta el clip quieto, pone el texto arriba cuando la cara cae abajo, se va a
    la IA cuando el archivo solo tiene un clip poco relevante, y no usa nunca un clip de relevancia
    cero (con Pexels caído y la IA fallando: tarjetas de marca y manifiesto «incompleto», que se
    rehace solo en la siguiente pasada).
  - Cortes contra la verdad de la voz falsa: **error medio 0,06 s, máximo 0,21 s** (antes de anclar
    en las pausas, hasta 0,58 s en los planos que empiezan frase).
  - Render de `MDS-024` (a media escala) y `MDS-025` (entero): duración idéntica a la voz; montaje y
    `qa.py` sin avisos (sincronía 0,04 s). **Tiempos: 3 min 19 s el render de siempre y 3 min 29 s
    el de archivo**, mismo Short, misma voz, 1.173 capturas los dos.
  - Un clip corrupto: ese plano sale como tarjeta de marca y el resto con vídeo. Un fallo del modo
    archivo entero: aviso y render de siempre.
  - **El render de siempre no cambia.** 72 capturas (24 escenas de cuatro guiones, tres instantes
    cada una) con el `escena.html` de antes y el de ahora: 4 difieren en una franja de un píxel
    (el borde del Engranaje o de un panel), y el motor de antes **contra sí mismo** da 2 de esas
    mismas diferencias: es el rasterizado de Chromium con la página ya usada, no el cambio.
    Repetidas en un navegador limpio, antes y ahora son idénticas.

## 8 bis · La revisión en frío del código, antes de entregar

Un subagente sin contexto revisó el cambio entero (diff, ejecución de pruebas propias con clips
raros: HEVC, 10 bits, girados, 60 fps, truncados). Encontró **dos críticos, un grave y nueve menores**;
corregidos todos antes de entregar:

- **Crítico · los manifiestos de mi prueba se habrían subido.** `05_calendario/visuales/` tenía los
  de la prueba simulada (enlaces `file://` e imágenes de relleno) con la misma firma que los guiones
  de verdad: el workflow los habría dado por buenos. No se entregan, y `traer` ya solo acepta enlaces
  `https://` (salvo `C50_PRUEBA_LOCAL=1`, solo en pruebas).
- **Crítico · `traer` sin tope de tiempo.** Con la red atascada podía comerse el job de 150 min. Ahora
  se limita a 8 min por Short, y el paso de `producir.yml` lleva `timeout-minutes: 15` y
  `continue-on-error: true`.
- **Grave · la longitud del vídeo no se comprobaba.** Un clip que pasa `ffprobe` pero no da
  fotogramas dejaba el mudo más corto que la voz y el montaje habría cortado el final. Ahora cada
  trozo de fondo se cuenta (y si falla, ese plano pasa a tarjeta de marca) y el vídeo compuesto tiene
  que tener exactamente los fotogramas de la voz, o el Short sale como siempre.
- **Menores:** capas de marca en RGBA (el cambio de formato de píxel movía un fotograma cada corte;
  medido y corregido), `plan()` dentro del respaldo, «incompleto» solo con fallos pasajeros (429,
  5xx, red), `excluir` como cadena, `podar()` con episodio vacío, `validar_guion.py` con búsquedas no
  textuales, respaldo de la IA con cualquier error, suelo de 64 px en `encajarBanda()` con aviso a la
  barrera, y los horizontales de Pexels pidiendo 1.920 px de alto.

## 9 · Lo que queda

- **Tarea 3 del codirector** (hoy): mover `visuales.yml` y `producir.yml` desde
  `00_estrategia/tareas/workflows_2026-09-23/` a `.github/workflows/`, borrar `visual_prueba.yml`, y
  `push`. Recomendado: una producción de prueba de `MDS-024` sin subir.
- Viernes 25: umbrales de movimiento y relevancia con los datos reales; muestrario del Engranaje
  que habla; respuesta del codirector sobre la regla 7 (presentador realista).
- `muestrario_visual.py` retirado (movido a `_to_delete/`): era de la prueba y ya no casa con
  `visual.py`.
