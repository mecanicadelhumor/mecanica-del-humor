# Bitácora · dirección · viernes 02/10/2026

Sesión de viernes, de tarde. Versión **17** del plan. El estudio de mercado, en
`00_estrategia/MERCADO_2026-10.md`.

## 1 · Lo que se leyó

El arranque entero en su orden: `LEEME.md`, `REGLAS.md`, `PROPIEDAD_DE_FICHEROS.md`, las versiones 14 a
16 de `PLAN_DE_CAMBIOS.md`, `PROMPT_DE_ARRANQUE.md`, el cuaderno del codirector (dos preguntas y una
tarea especial), `estado/2026-09-30` a `2026-10-02`, `08_comunicacion/` (novedades y las notas del 1 y
el 2), las bitácoras de métricas del 30/09 y de la revisión de hoy, `metricas.json` (del 29/09) y la
respuesta del codirector en `tareas_codirector_2026-09-30.md`: tareas 1 y 2 hechas (la 2 con un cron
de tres días), **C55.2: mezclado** (archivo en las escenas de situación, animación en las de mecanismo,
y que no siempre sea el azul de marca), Kaggle ok.

## 2 · El estado del canal

- `MDS-030` subido (07:08 UTC), sale a las 17:00 UTC. La revisión de hoy entregó sola (`37dc2a2`), sin
  incidencias. La planificación del jueves entregó sola (`bd02c5c`): `MDS-031` a `035`.
- **Contadores públicos a las 15:15 (España):** 5 suscriptores (eran 0 el 28/09). `MDS-026` 67 · `027`
  66 · `028` **6** · `029` 10 · `025` 67 · `022` 268 · `021` 147 · `016` 1.200.
- **Las rutinas, comprobadas** con la herramienta de tareas programadas: planificación
  `7 22 * * THU,FRI,SAT` en **UTC** (00:07 de España del día siguiente) con `claude-opus-5-5`; revisión
  `28 9 * * *`; métricas `3 10 * * 1`. Por el desfase de zona, el reintento del sábado arrancaba en
  domingo y su paso 0 lo cerraba: corregido en `planificacion-jueves.md` (antes de las 03:00 cuenta
  como el día anterior).

## 3 · Las dos preguntas del cuaderno

- **Música:** `cola.py`, `pistas[(n − 1) % 14]`. `MDS-028` → `cama_14`, `029` → `cama_01`, `030` →
  `cama_02`: comprobado en `05_calendario/qa/MDS-0XX.es/ficha.json`. Fin de la vuelta, no fallo. El
  codirector decidió que las 14 pistas se quedan.
- **Miniaturas:** medidas las imágenes de `i.ytimg.com` de doce Shorts desde el navegador integrado
  (cookies rechazadas, sin sesión iniciada): `oar2.jpg` (pestaña del canal) 90-95 % azul marino en los
  de plantilla; `frame0.jpg` (estantería del buscador) **negro al 100 %** en todos, por el fundido de
  entrada de `montaje.py`; `hqdefault.jpg` es la nuestra, y solo la usan las superficies horizontales.
  Las verticales personalizadas existen desde el 25/07/2026, primero solo para el Programa de Partners.

## 4 · El estudio de mercado

Búsquedas web (fuentes en el estudio) y medidas propias en YouTube: la búsqueda «por qué nos reímos»
con filtro de Shorts (lo que rompe tiene cara: 1,6 M y 376 K; lo sin cara, 2-11 K) y dos canales de
curiosidades sin cara (32,9 K suscriptores y 694 vídeos, ~1.400 por Short; 2,8 K y 443, ~1.000).

## 5 · Lo que se hizo

- **C56:** títulos de `MDS-031` a `035` (74-93 → 41-52 caracteres); aviso en `validar_guion.py` por
  encima de 55; `planificacion-jueves.md` (sección del 02/10 y paso 4).
- **C57:** `pregunta_al_espectador` en las cinco publicaciones; `publicar_preguntas()` en
  `metricas.py`, llamada desde `--solo-registro` (sin tocar workflows). Probada con un YouTube de
  mentira: cinco casos, idempotente. Aviso en `validar_guion.py` si falta.
- **C58** (sí del codirector): `montaje.py` (0,1 s y sin fundido de entrada en Shorts; `montaje.json`
  apunta el colchón) y `qa.py` (mide contra ese colchón; `silencio_inicial` y `arranque` corregidos para
  el colchón corto).
- **C59** (sí del codirector): `render.py` (remate «Síguenos» / «un mecanismo nuevo de lunes a
  viernes») y `escena.html` (dos renglones, apartado de la columna de botones).
- **Probado de punta a punta en el contenedor con `MDS-030`**: voz de la caché (0 llamadas a Gemini),
  render en modo tarjeta (Pexels no llega al contenedor ni al ordenador del codirector), montaje con
  `cama_02`, QA. 34,1 s; silencio inicial 0-0,129 s; sin sílaba suelta; desfase 0,24 s; LUFS −15,09
  (igual que el producido hoy: no es de este cambio). La primera versión de C59, en una sola línea,
  llegaba de borde a borde: rehecha en dos. Muestra y fotogramas enviados al codirector por el chat (no
  están en el repositorio).
- `revision-diaria.md`: qué mirar en la ficha desde C58 y la marca de C57.
- Documentos: versión 17 del plan, `PROMPT_DE_ARRANQUE.md` (tres filas de autorizaciones, trampas 49 a
  51, «dónde está a 2 de octubre»), `LEEME.md`, nota en `08_comunicacion/`, tareas del codirector.

## 6 · Lo que queda

- El `push` del codirector antes del lunes 5 a las 03:13 (tarea 1).
- «Visto frente a deslizado» de los diez últimos Shorts (tarea 3): la API no lo da.
- El bucle, para el lunes 5. La cadencia y el formato largo, para después del 15/11.
