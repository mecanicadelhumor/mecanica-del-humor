# `voz_adelantada.yml` — diseño de C27-B, 13/09/2026

> **Actualizado el 15/09/2026 (C33.2):** el workflow ya está creado (14/09). La copia de esta
> carpeta pasa a correr **todos los días** (el codirector cambia la misma línea en la de
> `.github/`), y `voz_precache.py` precachea siempre el largo pendiente más cercano de la
> parrilla, no «el del próximo sábado». Lo de abajo es el diseño original.

**Qué hay aquí:** el `.yml` completo de un workflow nuevo. Cópialo a
`.github/workflows/voz_adelantada.yml` y súbelo cuando quieras encenderlo — esa
carpeta está protegida contra escritura remota (regla 11.7), por eso se deja
aquí en vez de escribirse directamente.

**No hace falta nada más para que funcione.** El código del que depende
(`03_produccion/pipeline/voz_precache.py`) ya está en el repositorio, escrito y
verificado hoy con Gemini y `edge-tts` simulados (`google-genai` y `edge-tts` no
tienen red desde este contenedor, así que la llamada real a la API no se ha
podido probar — sí toda la lógica alrededor). El secreto `GEMINI_API_KEY` que
necesita también está ya en el sitio correcto desde el 12/09 (paso «Sintetizar
narración» de `producir.yml`); este workflow es un job aparte y lo vuelve a
pedir en su propio paso, como es normal en Actions.

## Qué hace, en una frase

De martes a viernes, coge el guion del sábado que viene y sintetiza contra
Gemini las escenas de narración que todavía no estén en
`03_produccion/cache_voz/` — hasta agotar un presupuesto diario de llamadas
(9 por defecto, por debajo del límite real de 10/día para no arriesgar la
décima). El sábado, cuando `voz.py` aprenda a construir el episodio largo con
Gemini (paso siguiente, todavía sin escribir — ver «Lo que esto NO hace» más
abajo), se encuentra casi todo el audio ya hecho.

## Por qué de martes a viernes, y no de viernes a viernes

La instrucción original decía «de viernes a viernes». La corregí al escribir
esto: el guion del sábado que viene **no existe en el repositorio** hasta que
la planificación del jueves lo escribe y tú le haces `push` — normalmente el
viernes por la mañana (es la misma razón por la que la revisión diaria corre a
las 11:30 y no de madrugada, ver `00_estrategia/tareas/revision-diaria.md`).
Un disparo en lunes o martes de una semana cualquiera sí encuentra guion —el
que la planificación de la semana ANTERIOR ya escribió para el sábado que
viene—, así que el rango correcto es **martes a viernes**, que son los cuatro
días en los que, semana tras semana, el guion del sábado siguiente ya está en
el repo y aún queda margen antes de necesitarlo.

## Por qué el modelo 2.5 y no el 3.1 de los Shorts

`gemini-2.5-flash-preview-tts` (`MODELO_GEMINI_LARGO` en `voz_precache.py`) y
`gemini-3.1-flash-tts-preview` (el de los Shorts, C7) tienen cuotas diarias
**independientes**. Si el largo compitiera por el modelo de los Shorts, un
episodio de ~40 escenas se comería en un día la cuota que necesitan los cinco
Shorts de la semana completa.

## El detalle que más importa si algún día se toca esto: la clave de caché

`voz.py` cachea los Shorts con `_cache_voz_ruta(texto, "gemini", voz)` — el
literal `"gemini"` a secas, porque hasta ahora solo existía un modelo de
Gemini en juego. `voz_precache.py` cachea el largo con
`_cache_voz_ruta(texto, MODELO_GEMINI_LARGO, voz)` — el modelo exacto, no el
literal. Con eso, las dos cachés nunca chocan aunque compartan carpeta y
compartan voces (`Charon` para narrador, `Puck` para escéptico, en los dos
casos).

**Y esto es lo único frágil del diseño:** el día en que `voz.py` aprenda a
sintetizar el episodio largo con Gemini de verdad (el paso que viene después
de este), tiene que pedir la caché con este mismo modelo exacto
(`gemini-2.5-flash-preview-tts`), no con el literal `"gemini"` copiando sin
más el patrón de los Shorts. Si eso se copia mal, el precacheo de toda la
semana no sirve de nada: el sábado no encuentra nada en caché y sintetiza
todo de nuevo, de golpe, sin haber ganado los días. Está escrito con este
mismo aviso en la cabecera de `voz_precache.py` para que no se pierda.

## Lo que esto NO hace (a propósito)

- **No decide qué motor usa el episodio final.** La regla del codirector del
  12/09 es que un episodio largo sale con **una sola voz, nunca mezclada**:
  si la caché tiene las ~40 escenas el viernes por la noche, todo Gemini; si
  falta una sola, todo `edge-tts`, como hasta ahora. Esa decisión vive en el
  paso de producción del sábado (dentro de `voz.py` o de `producir.yml`),
  que todavía no existe — hoy `voz.py` sigue sin tocar para episodios
  `"largo"` (`usar_gemini` exige `formato == "corto"`, sin excepción). Este
  workflow solo rellena la caché; construir el episodio con ella es un paso
  posterior y deliberadamente separado.
- **No toca ningún guion, ni la parrilla, ni el registro de publicaciones.**
  Lo único que comitea es `03_produccion/cache_voz/`.
- **No compite con `producir.yml`** por runner ni por commit: grupo de
  concurrencia propio (`voz-adelantada`, no `produccion`), y el `git pull
  --rebase --autostash` antes del `push` es el mismo patrón que ya usa
  `producir.yml` en su paso «Registrar lo publicado», por si los dos
  workflows comitean cerca en el tiempo.

## Comprobado hoy (13/09/2026), en `/tmp`, fuera del repositorio

Con `edge-tts` y `google-genai` instalados en el contenedor (sí hay red hoy)
pero mockeando la llamada real a la API — no hay credenciales aquí —:

1. `escenas_pendientes()` ignora narraciones vacías y limpia el marcado de
   resaltado (`*`/`_`) con `hablable()` antes de calcular la clave — igual
   que hace `voz.py` para los Shorts.
2. La ruta de caché del largo es **distinta** de la que generaría el camino
   de Shorts para el mismo texto y la misma voz (verificado con el hash
   exacto, no solo "son distintos objetos").
3. `narrador`/`escéptico` se asignan a `Charon`/`Puck` según el campo `voz`
   de cada escena.
4. `formato: "corto"` no sintetiza nada (guarda temprano).
5. El presupuesto de llamadas se respeta: con 3 escenas pendientes y
   presupuesto 2, cachea 2 y dice que queda 1; una segunda pasada sin tocar
   nada más completa exactamente la que faltaba, sin repetir las dos ya
   hechas.
6. Una cuota diaria agotada (`RESOURCE_EXHAUSTED` / 429 «per day») se
   detecta, no lanza excepción, no cachea nada a medias, y dice cuántas
   escenas quedan para el día siguiente.
7. Escritura atómica: no queda ningún `.tmp.mp3` huérfano en la carpeta de
   caché tras una ejecución.

**Lo que no se ha podido probar:** la llamada real a la API de Gemini con el
modelo 2.5 (necesita `GEMINI_API_KEY` y red hacia Google, que este contenedor
no tiene hacia ese destino). Se verá la primera vez que el codirector suba
este `.yml` y lo lance a mano (`workflow_dispatch`) con `presupuesto: 1` para
confirmar sin gastar cuota de verdad.

## Cómo probarlo sin esperar a la semana que viene

Pestaña **Actions** → **Voz adelantada (episodio largo)** → **Run workflow**.
Con `presupuesto: 1` cachea una sola escena del guion del próximo sábado y
permite ver en el log si `GEMINI_API_KEY` llega bien al paso (mismo síntoma
que en `producir.yml`: `***` enmascarado es buena señal; `GEMINI_API_KEY`
ausente o un error de credenciales significa que no ha llegado). El campo
`fecha_sabado` del mismo formulario permite apuntar a cualquier sábado ya
escrito en `parrilla.json`, por si quieres probarlo sin esperar al próximo.
