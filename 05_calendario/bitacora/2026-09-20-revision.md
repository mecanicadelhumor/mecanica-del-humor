# Revisión diaria — 20 de septiembre de 2026, 11:30 (domingo)

Sesión en la nube, sin puente `mcp__remote-devices__*` (no existe en este modo, y no ha
existido nunca). No se ha pedido ningún permiso ni confirmación en toda la sesión — sí se ha
*intentado* una consulta de solo lectura a GitHub por `WebFetch` (ver paso 2) y el sistema la ha
bloqueado pidiendo una aprobación que en esta sesión desatendida no puede llegar; no se ha
reintentado ni se ha esperado por ella. Clono `origin/main`, trabajo en el contenedor, entrego
con `.tar.gz`.

**Comprobación de entregas pendientes (primera acción).** `git log --oneline -8` sobre
`origin/main`: `1e5d4fd` (registro + 3 tomas de voz de MDH-007, hoy 06:17 UTC), `07617b2`
(precacheo de voz, ayer), `db50aae` (sincronización de registro con YouTube, ayer), `d55be06`
(registro y expediente de MDS-017 rehecho, ayer 05:58 UTC — ver paso 3), y hacia atrás los del
18/09 ya conocidos, incluida `4b275a5` (**Planificación semana 21 a 26 de septiembre**, la del
jueves 17, aplicada) y `8262b7b` (la reescritura C38 de los cinco Shorts de esa semana, sesión de
dirección de la tarde del 18/09). No es viernes ni sábado, así que la regla estricta del «paquete
del jueves a medias» no aplica hoy, pero la comprobé igual: el paquete del jueves 17 sí está
aplicado, sin nada pendiente ahí.

**Nota sobre continuidad.** No encuentro bitácora de ayer (`2026-09-19-revision.md` no existe) ni
`ESTADO.md` actualizado desde el 18/09. No sé si la revisión del sábado no llegó a correr o si
corrió y su entrega no se ha aplicado todavía (el propio encabezado de la tarea avisa de que eso
puede pasar). Lo dejo dicho y no lo trato como bloqueo: he revisado hoy tanto lo de hoy como lo
de ayer que quedó sin mirar (el vídeo rehecho de MDS-017, paso 3).

## Paso 1 — revisión editorial

Guiones españoles sin producir, cruzando `parrilla.json` con `registro_publicaciones.json`:
`MDH-007` (hoy, sin subir — ver paso 2), `MDS-021` a `MDS-025` (21 al 25/09) y `MDH-008` (26/09).

- **`python3 04_agentes/validar_guion.py` sobre los siete: sin errores.** Solo avisos de duración
  de plano fijo (>10 s, ya conocidos en episodios largos) y los tres avisos de C17 en `MDH-008`
  (A01, A05, L01) que ya revisé el 18/09 y siguen sin ser hallazgo por el mismo razonamiento: el
  propio guion justifica en `notas_humor` por qué cada fuente sostiene aquí un ángulo distinto.
  `MDH-008` no ha cambiado desde el 18/09 (mismo commit `4b275a5`), no lo repito escena por
  escena.
- **`MDH-007`**: sin cambios de contenido desde el 17/09 (comprobado con `git log` sobre el
  fichero: el último commit que lo toca es `4b275a5`, que solo aplicó mis dos notas de
  `revisiones/` de esos días). Ya se revisó completo el 15, el 16 y se verificaron las dos
  correcciones el 18/09. No lo releo entero hoy porque no ha cambiado; si el problema de la voz
  (paso 2) obliga a tocarlo, sí lo revisaría de nuevo antes de nada.
- **`MDS-021` a `MDS-025`, revisados enteros hoy contra la versión REESCRITA por C38 el
  18/09/2026 por la tarde** (commit `8262b7b`) — la revisión de ayer por la mañana solo había
  visto la versión anterior a esa reescritura, así que esta es la primera pasada sobre el texto
  que de verdad se va a producir. Regla de los dos canales escena por escena en los cinco:
  correlato pantalla/narración correcto en las 28 escenas (ninguna introduce en `texto`, `cifra`,
  `pie`, `a`/`b`/`et_a`/`et_b` o `titulo`/`subtitulo` un dato que su narración no sostenga);
  expresión del personaje conforme a la regla 14.3 en todas (`piensa`/`entiende`/`rie`/`neutra`
  en las escenas que presentan, exponen o comparan; `no` solo en los seis cierres, que es donde
  la narración dice que algo falla); C19 cumplido en las cinco escenas 1 (icono + cuatro palabras
  o menos); un ámbar por escena, nada en `narracion`; fuentes citadas (C05, A06, G03, L04, G04)
  correctas contra `BIBLIOGRAFIA_CURADA.md`, que hoy está sincronizado con `semillas.json`
  (`validar_bibliografia.py`, sin diferencias). **Repasé con atención `MDS-022` escena 4
  (diagrama del chiste del pijama)**, porque el texto en pantalla da la resolución concreta
  («sí lo es, si el puesto es quedarse en casa») y la narración de esa escena solo da el modelo en
  abstracto («notas que algo no encaja, y luego encuentras el sentido»): decidí que NO es
  hallazgo, porque esa resolución ya la da el propio chiste en las escenas 1-2 (vestirse para el
  puesto que quieres / presentarse en pijama es, para cualquiera que solo oiga el audio, la misma
  broma de siempre) y lo que añade la pantalla es una reformulación evidente, no un dato nuevo. Lo
  dejo escrito por si alguien lo revisa distinto.
  - **`MDS-025`**: confirmado que la nota `revisiones/MDS-025.md` (el «grupo de control» mal
    llamado) está resuelta por construcción, tal como decía la propia reescritura: la escena 2
    ahora dice «el grupo que vio comedia» y ya no hay ninguna escena que llame «control» al grupo
    equivocado. El fichero de la nota ya no existe en `revisiones/` (correcto, no hay que
    borrarlo yo).
  - **Ningún hallazgo nuevo** en los cinco. No he tocado ningún guion (el primero de la semana,
    `MDS-021`, se produce mañana a las 01:13 UTC — dentro de la ventana de 48 horas— pero al no
    encontrar defecto no hacía falta usar la excepción).
- **`MDH-008`**: la nota `revisiones/MDH-008.md` (escena 11, `rie` contradiciendo «ya no hace
  gracia» / «nadie se ríe») sigue abierta y sigue siendo válida — comprobado hoy contra el guion
  actual, la escena 11 no ha cambiado desde el 18/09. La aplicará la planificación del jueves 24,
  antes de que se produzca el 26/09. No toco el guion (no está dentro de 48 horas).
- **Bibliografía**: nada que corregir hoy. `C05` y `G03` (arregladas el 18/09) y `F04`/`F05`
  (arregladas por la dirección el mismo día) siguen consistentes entre `BIBLIOGRAFIA_CURADA.md` y
  `data/semillas.json` (`validar_bibliografia.py`: «los dos ficheros dicen lo mismo»). `E02`
  sigue con dos DOI sin verificar — no es mío decidir cuál es el bueno, sigue en tareas del
  codirector.

## Paso 2 — comprobar que la producción salió

**INCIDENCIA.** `MDH-007` (episodio largo de hoy, domingo, publica a las 12:00) **no tiene
ninguna entrada en `registro_publicaciones.json`**, y ya pasaron los tres intentos de cron de
hoy (01:13, 04:47 y 08:23 UTC — son las 09:51 UTC / 11:51 España a la hora de escribir esto).
Cruce completo `parrilla.json` contra el registro hasta hoy: `MDH-007` es el único episodio
emitido o por emitir hasta la fecha que falta.

**Lo que sí puedo comprobar sin red, y por qué apunta a la voz:**

- Con las funciones ya escritas en el repositorio (`voz_precache.escenas_pendientes`, sin tocar
  nada, solo mirando qué hay en `03_produccion/cache_voz/`), de las 41 escenas con narración de
  `MDH-007`, **38 están cacheadas con Gemini y 3 no** (escenas 39, 40 y 41 — el tramo final,
  cierre incluido). El commit de esta madrugada (`1e5d4fd`, 06:17 UTC) añadió tres tomas nuevas a
  la caché pero el guion tiene 41, así que no bastó.
- `voz.py` (C33.1/C33.2, comentario en el propio código junto a `SALIDA_SIN_VOZ_COMPLETA`): desde
  el 15/09 el vídeo **entero** tiene que salir con Gemini o el paso falla sin subir nada — nunca
  se cae a `edge-tts` automáticamente («mejor no publicar que publicar con edge-tts», decisión del
  codirector). Con 3 escenas todavía sin voz de Gemini a esta hora, el escenario más probable es
  que el paso «Sintetizar narración» haya terminado en código de salida 3 en los tres intentos de
  hoy — que es justo el caso que las instrucciones de esta tarea describen como «no es avería, es
  el diseño» durante la madrugada, y que se vuelve incidencia cuando, como ahora, sigue sin
  resolverse a las 11:30.
- **No he podido confirmarlo mirando el log de Actions.** Lo intenté con `WebFetch` sobre la
  página de ejecuciones del workflow (`producir.yml`) y el sistema pidió una aprobación de
  permiso que, en esta sesión desatendida, nadie puede dar — así que no es una comprobación que
  pueda hacer sola hoy. `curl` directo a la API de GitHub también da `403` a través del proxy de
  salida de este contenedor. Lo dejo dicho en vez de insistir o suponer.
- Esto ya estaba anotado como riesgo el 18/09 en la versión 10 de `PLAN_DE_CAMBIOS.md`: «la caché
  de `MDH-007` lleva dos días clavada en 18 de 41 (...) el domingo sale (...) pero sin margen para
  rechazos». Ha avanzado (18 → 38) pero no ha llegado a las 41 antes de la última ventana de hoy.

**No toco `parrilla.json`** (no es mío) y no reintento nada de voz ni de producción desde aquí:
esta sesión no tiene `GEMINI_API_KEY` ni las credenciales del pipeline, y aunque las tuviera, no
me corresponde forzar una síntesis fuera del workflow. Queda en `ESTADO.md` como `INCIDENCIA` con
lo que puede hacer el codirector.

**El resto del cruce, sin incidencias:**
- `MDS-017` (rehecho el 19/09, ver paso 3): `private` con `publicar_en: 2026-09-19T17:00:00Z`, ya
  pasado. Es el patrón automático correcto (con `publicar_en`, no el caso «no lo sé» de
  MDS-011); lo corrige `sincronizar_registro.yml` o `metricas.py` el lunes. Video ID
  `mPwvmnp1ZNE`, distinto del retirado `9H2xEZnFeHA`: el rehacer sí generó una subida nueva.
- `MDS-018`, `MDS-019`, `MDS-020`: todos `public`. Sin novedad.
- El workflow de sincronización diaria con YouTube (C31, `sincroniza_registro.yml`, confirmado
  hecho por el codirector el 15/09) no ha dejado commit hoy todavía (sus horarios son 08:50 y
  09:10 UTC, ya pasados a la hora de esta revisión). Con el historial de retrasos de los cron de
  este proyecto no lo trato como fallo; lo anoto por si mañana sigue sin aparecer.

## Paso 3 — revisión del vídeo

**No hay vídeo de hoy que revisar** (ese es exactamente el problema del paso 2). En su lugar
reviso **`MDS-017` rehecho**, producido ayer sábado (`d55be06`, 05:58 UTC) y que, por lo dicho
arriba sobre la posible entrega sin aplicar del sábado, nadie parece haber revisado todavía.

- **`ficha.json`** (`05_calendario/qa/MDS-017.es/`): `lufs -14.5` (OK), `pico_dbtp -1.26` (OK),
  `fragmento_antes_de_la_narracion: false`, `quemados: false` (correcto),
  `sincronia_voz.desfase_s: 0.25` (< 0.5, OK). **`voz_mezclada: false`** (no incidencia).
  `modelo_voz: gemini-3.1-flash-tts-preview`, sin `edge-tts` en ninguna escena. `origen_voz`:
  4 caché + 2 llamada + 0 mínima. `escenas_ritmo_fuera_de_rango`: escena 1 a 1.57 palabras/s,
  justo por debajo de 1.6 — aviso, no error, mismo criterio que en producciones anteriores.
- **Los seis fotogramas, los dos canales**: comprobado contra el guion, no solo mirando las
  capturas. Escena 1: icono (el resorte de «cosquillas») + «Cosquillas a ratas.» (C19 cumplido).
  Escena 4 (comparación «un chiste» vs «unas cosquillas»): correlato exacto con la narración.
  Escena 6 (cierre, fuente E06 visible): personaje `no`, coherente con «la rata no puede
  decirlo». Sin texto cortado, sin elementos tapados, sin faltas, geometría personaje/texto con
  hueco amplio a ojo (no he vuelto a correr `muestrear_geometria.py`: sin las tipografías de
  marca en este contenedor sus números no son de fiar, y a ojo el hueco en el fotograma final es
  mucho mayor que el caso límite conocido de `MDS-007`).
- **Sin incidencia.**

## Paso 4 — código y encargos

**Ningún cambio de código hoy**, y digo por qué en vez de forzar uno al azar:

- **Encargo 8 (`ajustarTamano()` por banda reservada)**: sigue bloqueado por lo mismo del 18/09 —
  este contenedor no tiene las tipografías de marca (`fc-list` sigue sin Archivo Black, Inter ni
  JetBrains Mono) y medir sin ellas es exactamente el error que costó `MDS-011`. No lo toco.
- **P1 (profundidad, opacidad de la retícula)**: sigue sin respuesta del codirector en
  `07_pruebas/P1-profundidad/`. Nada nuevo que decidir sola.
- **C34 (banco de imágenes, duotono ámbar)**: sigue bloqueado por el enlace de origen de cada
  foto, pedido el 15/09 y sin contestar.
- **C36 (una llamada por vídeo)**: sigue sin diseño escrito.
- **Encargo 12 (CSV de Studio, glob recursivo)**: ya está hecho — comprobado leyendo
  `04_agentes/metricas.py`: `leer_export_studio()` ya usa `glob.glob(EXPORTES/"**"/"*.csv",
  recursive=True)` y `_cabecera_sirve()` ya descarta `Totales.csv`. No hacía falta nada.
- **P2, P7, P5**: son de la semana del 21, que empieza mañana. No los empiezo hoy para no meter
  trabajo no pedido en una sesión que ya tiene una incidencia que gestionar; quedan listos para
  mañana.
- **C31 (estado real de YouTube en el repositorio)**: confirmado que ya está hecho —
  `07_pruebas/registro-diario-15-09/` tiene la respuesta del codirector («Hecho hoy 15/09») y los
  commits `registro: sincronizado con YouTube` de los últimos días lo confirman en la práctica.

## Y una nota sobre `07_pruebas/`

Revisadas las carpetas con preguntas abiertas: solo `P1-profundidad/` sigue sin respuesta. El
resto, sin novedad desde el 18/09. Nada dirigido a mí que no estuviera ya visto.

## Paso 6 — ESTADO.md

Ver `05_calendario/ESTADO.md`, reescrito entero.

---

**Ficheros tocados esta sesión:**
- `05_calendario/bitacora/2026-09-20-revision.md` (este fichero, nuevo)
- `05_calendario/ESTADO.md` (reescrito)

Ningún guion tocado (ningún hallazgo nuevo que lo pidiera). Ningún fichero de
`05_calendario/parrilla.json`, `CALENDARIO.md`, `demanda.json`, `registro_publicaciones.json`,
`qa/`, guiones ni `.github/workflows/` tocado. Ningún código de `03_produccion/` ni `04_agentes/`
tocado (todo lo listo ya estaba hecho; lo bloqueado sigue bloqueado, con el motivo dicho arriba).
