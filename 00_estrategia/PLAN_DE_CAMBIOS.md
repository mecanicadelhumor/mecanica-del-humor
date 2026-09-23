# Plan de cambios — Mecánica del Humor

**Versión 3 · 21 de agosto de 2026** — con las decisiones tomadas y la fase 1 y
media de la fase 2 ya escritas en el repositorio.

> ⚠️ **La versión que manda es la 12, al final de este documento (23 de
> septiembre).** Las anteriores siguen vigentes en todo lo que la 12 no corrija.
> *(Hasta el 23/09 este aviso decía «la 10»: se quedó sin actualizar el 21/09, cuando
> ya mandaba la 11. Trampa 32: una corrección escrita en un sitio y no en los demás.)*
> En corto: la **4** partió la escalera de métricas en dos (Shorts y largo); la
> **5** puso la primera barrera antes de publicar y cambió el rumbo de C7; la
> **6** abrió C25 (la presentación) y fijó en C26 la fecha en la que se decide si
> el canal sigue; la **7** reescribió los dos guionistas y arregló las
> comprobaciones que miraban donde no tocaba; la **8** dirige la voz escena a
> escena (C33) y **revierte el descarte de las imágenes** que había hecho C25
> (C34); la **9** puso una sola voz por vídeo (C33.1 y C33.2); y la **10** le pone
> reloj al Short —la duración de su serie y el remate en el segundo doce (C38)— y
> contesta a TikTok, Reels y marketing (C40 y C41); la **11** suspende el episodio largo
> (C42), pone el estado del canal en un fichero por día (C45) y hace que el canal se lea a sí
> mismo (C46 y C47); y la **12** pone **la historia antes que el reloj** —la lectura en frío
> obligatoria (C48)— y decide el **giro de la imagen**, de diapositiva a vídeo (C50).
> **Si vas a decidir algo con este plan, lee la versión 12 antes.**

Este documento es **ejecutable**. Cada cambio trae qué archivos toca, qué tiene que ser
cierto para darlo por hecho, y qué no hay que hacer. El razonamiento está en
`DIAGNOSTICO.md`; las restricciones que nadie puede saltarse, en `REGLAS.md`.

**Antes de empezar cualquier cambio de este documento, lee `REGLAS.md`.**

---

## Cómo se usa

- Los cambios están **ordenados por dependencia**, no por importancia. Un cambio con
  bloqueantes sin resolver no se empieza.
- **Un cambio por producción.** Si entran dos a la vez y el resultado empeora, no se sabe
  cuál fue. (Regla 1 de `MEJORA_VISUAL.md`, que sigue vigente.)
- Cada cambio se anota al terminar en `05_calendario/MEJORAS.md`, con lo medido antes y
  después. Ese archivo **se añade al final, nunca se reescribe**.
- Los archivos marcados como **protegidos** no se tocan sin permiso explícito. **Desde el
  07/09/2026 esto ya no aplica a la dirección**, que puede editar cualquier fichero del
  repositorio; para los demás agentes no cambia nada. `.github/workflows/` sigue protegida
  para todos, sin excepción. Las autorizaciones vigentes, una por una, están en
  `PROMPT_DE_ARRANQUE.md`.

### Estado a 20 de agosto, tarde

| Fase | Cambios | Estado |
|---|---|---|
| **0 · Desbloquear** | P0.1 · P0.2 | **hecho.** Actions falló por el cambio de figuras del 19 y se resolvió esa mañana. MDH-003.es producido y en privado. Los subtítulos quemados llegaron a funcionar (`lineas_ass: 793`) y **se retiraron a propósito** — ver C6.1 |
| **1 · Distribución** | C1 · C2 · C3 | **código escrito.** Falta ejecutar la primera producción vertical |
| **2 · Empaquetado** | C4 · C5 · C9 | **código escrito.** Falta verlo con las tipografías reales |
| **3 · Producto** | C6 · C7 · C8 | C8 hecho (parrilla). C6 y C7 pendientes |
| **4 · Compuesto** | C10 · C11 · C12 · C13 | C11 y C12 escritos en `publicar.py`. C10 y C13 pendientes |
| **Permanente** | C14 | **hecho.** Las tres tareas programadas reescritas |

### Lo que ya está en el repositorio

| Fichero | Qué trae |
|---|---|
| `02_marca/personaje.svg` | **El Engranaje**, el personaje. Seis expresiones por clase CSS, cero peticiones, cero coste de render |
| `03_produccion/pipeline/escena.html` | Formato vertical 1080×1920 con sus zonas seguras, el personaje enganchado al escalonado, `etiqueta` en `enunciado`, viñeta corregida para el lienzo alto |
| `03_produccion/pipeline/render.py` | Lienzo según `formato`; el viewport y la página ya no se pueden desincronizar |
| `03_produccion/pipeline/miniatura.py` | **Reescrito.** Cuatro temas con contraste verificado por código, el personaje al 28 % del encuadre, cuatro palabras o menos, ajuste automático del titular, tres variantes, versión vertical |
| `03_produccion/pipeline/cola.py` | Resuelve trabajos `corto`, hora de publicación por emisión, `formato` en el plan |
| `03_produccion/pipeline/publicar.py` | Listas de reproducción por serie, la pregunta como primer comentario, sin capítulos en los Shorts |
| `04_agentes/esquema_guion.json` | `formato`, `serie`, `personaje`, `voz`, ids `MDS-###` |
| `04_agentes/validar_guion.py` | Límites por formato, **fórmulas de apertura prohibidas**, reglas del Short (remate, personaje, escena 1 sin rótulo) |
| `04_agentes/prompts/guionista_corto.md` | **Nuevo.** El oficio del Short y las cinco series |
| `04_agentes/prompts/guionista.md` | El gancho, el personaje, las dos voces, 4 a 6 minutos |
| `05_calendario/parrilla.json` | **Reescrita.** Cinco Shorts (L–V 19:00) y un largo (sábado 12:00), solo español |
| `05_calendario/guiones/MDS-001.es.json` | El primer Short, validado: 6 escenas, 41,6 s, «Desmonta el chiste» |

Todo compila, todo valida contra el esquema, y los guiones largos que ya existían siguen
pasando el validador sin errores nuevos.

---

## Hoja de ruta: en qué orden, en qué fechas, y si se aplican todos

**¿Se aplican los catorce? No necesariamente, y es a propósito.** Esto no es una
lista de tareas: es una **cola ordenada por la escalera de métricas de C14**. Cada
cambio ataca un peldaño concreto, y un cambio que arregla el peldaño 3 no sirve de
nada mientras el problema esté en el 2. Los tres últimos de la tabla están
condicionados a que el canal llegue a tener el problema que resuelven.

| # | Cambio | Peldaño que ataca | Estado | Cuándo |
|---|---|---|---|---|
| **C1** | Un canal + doblaje automático | 1 · distribución | ✅ hecho | 20 ago |
| **C8** | Cinco Shorts + un largo | 1 | ✅ hecho | 20 ago |
| **C2** | Shorts como puerta de entrada | 1 | ✅ código hecho | **en la calle el 24 ago** |
| **C4** | El personaje | 2 · empaquetado | ✅ hecho | 20 ago |
| **C5** | Miniaturas con contraste medido | 2 | ✅ hecho | 20 ago |
| **C9** | Los primeros quince segundos | 3 · gancho | ✅ validador y prompt | 20 ago |
| **C14** | La escalera de métricas | — | ✅ hecho | primera lectura **24 ago** |
| **C12** | Series y listas automáticas | 5 · retorno | ✅ código hecho | primera lista **24 ago** |
| **C11** | La pregunta como primer comentario | 5 | ✅ código hecho | actúa cuando haya público |
| **C3** | Temas por demanda | 1 y 2 | ⚙️ **completado el 21 ago** con `demanda.yml` | primera medición real **27 ago** |
| **C6** | Movimiento en pantalla | 4 · ritmo | ✅ **entregado por C15** el 28 ago | ver C15 al final |
| **C7** | Dos voces | 4 | ⏳ pendiente | escalón 1 (`edge-tts`) la semana del 1 sep; escalón 2 (Gemini TTS) cuando el 1 esté probado. **Sin tarjeta: el nivel gratuito de `gemini-3.1-flash-tts-preview` incluye la salida de audio** (28 ago) |
| **C13** | Fuera de YouTube | 1 | ⚙️ parcial | Bluesky **ya**; TikTok e Instagram **solo si se pasa el peldaño 1** |
| **C10** | Una página web por episodio | 1 · tráfico externo | ⏸️ aplazado | **solo si se pasa el peldaño 2**. Antes es tráfico llevado a una puerta por la que nadie entra |

**Cómo se lee esta tabla:** de arriba abajo hasta la línea de C6, todo lo que
podía hacerse sin datos ya está hecho. De C6 en adelante manda la medición del
lunes. Si el lunes 24 el CTR sigue por debajo del 4 %, se vuelve a C5 —más
variantes de miniatura— antes de tocar C6, por muy tentador que sea el ritmo.

**Lo que no está en la lista y podría entrar:** si a las cuatro semanas la señal
dice que una serie de Shorts funciona muy por encima de las demás, entra un C15
—reconstruir la parrilla entera alrededor de esa serie— y desplaza a lo que quede
por debajo. La cola se reordena con los datos; no es un compromiso.

---

## Las decisiones que faltaban, tomadas

### Alcance: mano libre

El codirector autoriza cambiarlo todo salvo las reglas fijas de `REGLAS.md`.

### El canal inglés: consolidar ahora, reabrir con datos

`@humormechanics` queda en pausa y sus vídeos ocultos. El doblaje automático de YouTube
está **activado y sin revisión manual** desde el 20 de agosto.

El motivo es aritmético: dos canales desde cero pagan dos arranques en frío, y el inglés
compite contra Charisma on Command, The School of Life y Psych2Go mientras el español no
compite prácticamente contra nadie. El doblaje prueba la demanda inglesa gratis.

**Condición de reapertura:** si a las ocho semanas las pistas dobladas acumulan más del
25 % del tiempo de visionado total, se reabre con readaptación de verdad, no traducción,
por lo del «hombre entra en un bar» del 19 de agosto.

### La voz: Gemini TTS con dos hablantes. La clonación queda en reserva

El codirector acepta grabar su voz para clonarla **con la condición de que el modelo y la
muestra no salgan de un entorno local o muy seguro**. Esa condición y la infraestructura
del canal son incompatibles hoy, y conviene decirlo claro en vez de estirarla:

- La producción corre en **GitHub Actions sobre un repositorio público**. La muestra de
  referencia tendría que vivir donde el runner la lea, y un secreto de repositorio no
  llega: el límite está muy por debajo de lo que ocupan veinte segundos de audio.
- Los modelos libres que clonan bien, Chatterbox y Qwen3-TTS, **piden GPU**. Los runners
  gratuitos de Actions son solo CPU.
- Hacer el repositorio privado costaría los minutos ilimitados de Actions, que es lo que
  sostiene el coste cero de todo el sistema.

Así que **no se clona la voz por ahora**, y no porque no merezca la pena: porque hacerlo
hoy exigiría relajar la condición que el codirector puso.

**Lo que sí se hace, y resuelve el mismo problema:** el escalón 2 de C7, Gemini TTS con
dos hablantes y control de expresión por prompt, con la `GEMINI_API_KEY` que ya está en
los secretos. Rompe la cadencia fija, da al canal una voz reconocible y mete al escéptico,
que es donde vive el humor. Sin datos personales de nadie y sin GPU.

**Cuándo se reabre la clonación:** si a las ocho semanas la voz sigue siendo lo que peor
funciona, hay dos caminos limpios — renderizar el audio en el ordenador del codirector y
subir solo el resultado, o pagar minutos privados de Actions — y entonces sí se le pide la
grabación. No antes.

---

# FASE 0 · Desbloquear

Nada de lo demás sirve si la producción no corre.

## P0.1 · Averiguar por qué Actions lleva dos días callado

**Solo lo puede hacer el codirector.** Abrir la pestaña *Actions* del repositorio
`mecanica-del-humor`.

| Lo que ve | Lo que significa | Qué hacer |
|---|---|---|
| No hay ejecución del 20 de agosto | Cuota agotada, workflows deshabilitados o repo en pausa | Reactivar; si es cuota, comprobar que el repo es **público** (minutos ilimitados) |
| Hay ejecución y falla | Fallo de código o de entorno | Copiar el log del paso «Recuperar el plan» y del paso que falla, y pegarlo en la conversación |
| Hay ejecución y termina sin subir nada | El plan venía vacío | El paso «Recuperar el plan» dice si traía uno o dos trabajos |

**Criterio de aceptación:** hay una ejecución que termina con un `final.mp4` subido y una
entrada nueva en `05_calendario/registro_publicaciones.json`.

## P0.2 · Confirmar los subtítulos quemados

El arreglo está en el repositorio desde el 19 de agosto (`voz.py` pide
`boundary="WordBoundary"` explícito; `requirements.txt` fija `edge-tts>=7,<8`) y **nunca se
ha ejecutado**.

**Criterio de aceptación:** en `05_calendario/qa/<ID>/ficha.json` de la primera producción
nueva:

```json
"subtitulos": { "ass_existe": true, "lineas_ass": <mayor que 0>, "quemados": true }
```

y al menos cuatro de los seis fotogramas de QA muestran subtítulo en pantalla.

**Si sigue en 0:** el fallo está en la síntesis, no en el montaje. No tocar `montaje.py`.
Volcar en `MEJORAS.md` la versión exacta de `edge-tts` instalada en el runner.

---

# FASE 1 · Distribución

El canal no tiene un problema de calidad. Tiene un problema de que nadie lo ve.
Esta fase es la que más visualizaciones mueve y la que menos código toca.

## C1 · Un solo canal, con doblaje automático

**Problema:** dos canales desde cero pagan dos arranques en frío y dividen una señal que ya
era nula. Desde febrero de 2026 YouTube da doblaje automático gratis a todos los creadores,
en 27 idiomas, con voz expresiva en español.

### Lo que hace el codirector (una vez, 15 minutos)

1. En `@mecanicadelhumor`: *Studio → Configuración → Valores predeterminados de subida →
   Configuración avanzada* → activar **doblaje automático**. Dejar marcado «revisar antes
   de publicar» las dos primeras semanas.
2. En `@humormechanics`: poner los vídeos en **no listado** (no borrar), y en la descripción
   del canal: *«Este canal está en pausa. El contenido está ahora en
   youtube.com/@mecanicadelhumor con audio en inglés.»*
3. Verificar el teléfono en `youtube.com/verify` si no está hecho — sin eso no hay
   miniaturas personalizadas y `publicar.py` ya avisa de ese 403.

### Lo que hace el sistema

- `05_calendario/parrilla.json`: los trabajos pasan a `["es"]`. **No** borrar los guiones
  ingleses ya escritos; se archivan tal cual para cuando se reabra el canal.
- `03_produccion/pipeline/cola.py`: dejar de resolver trabajos `en`.
- `05_calendario/CALENDARIO.md`: reflejar el cambio con fecha y motivo.

### Criterio de aceptación

Una producción completa que sube **un** vídeo, en español, y que a las 24 h tiene una pista
de audio en inglés generada por YouTube.

### Cuándo se revierte

Si a las ocho semanas las pistas dobladas en inglés acumulan **más del 25 % del tiempo de
visionado total**, hay demanda inglesa real: se reabre `@humormechanics` con readaptación
de verdad (no traducción — ver el incidente del «hombre entra en un bar» en `MEJORAS.md`,
18 de agosto).

---

## C2 · Shorts como puerta de entrada

**Problema:** el vídeo largo saca 1–9 visualizaciones. Un canal de menos de 1.000
suscriptores saca **50–500 por Short** en las primeras 48 horas. El feed de Shorts es la
única superficie de YouTube que no exige audiencia previa.

**Buena noticia:** no hace falta infraestructura nueva. Los requisitos son ≤180 s y 9:16, y
**la clasificación como Short es automática al subir por la API** — no hay casilla ni hace
falta `#shorts`.

### Cadencia nueva

| Qué | Cuánto | Cuándo |
|---|---|---|
| Short | 5 por semana | lunes a viernes, 18:00 CEST |
| Vídeo largo | 1 por semana | sábado, 12:00 CEST |

### Archivos

| Archivo | Cambio |
|---|---|
| `03_produccion/pipeline/escena.html` | Aceptar `?formato=vertical`: viewport 1080×1920, tipografías escaladas, seguros arriba (título del Short) y abajo (barra de UI de YouTube: dejar 300 px libres) |
| `03_produccion/pipeline/render.py` | Pasar el formato al navegador sin interfaz |
| `04_agentes/esquema_guion.json` | Añadir `formato: "corto" \| "largo"`; en `corto`, máximo 8 escenas y `duracion_total_s ≤ 55` |
| `04_agentes/validar_guion.py` | Reglas nuevas de arriba, y **error** si un `corto` pasa de 55 s |
| `03_produccion/pipeline/miniatura.py` | Variante 1080×1920 |
| `05_calendario/parrilla.json` | Entradas de tipo `corto` |
| `03_produccion/pipeline/publicar.py` | **Sin cambios.** Ya sube bien. |

### Los cinco formatos de Short

Todos duran entre 30 y 50 segundos y **rematan**. Ninguno es un recorte del vídeo largo.

**S1 · Desmonta el chiste**
`chiste (0-8 s) → silencio de 2 s → despiece (10-35 s) → remate (35-40 s)`
El despiece nombra las tres piezas: qué expectativa se rompió, por qué fue inofensiva,
dónde estaba la bisagra. Es la marca del canal en cuarenta segundos.

**S2 · Ríete primero, te explico después**
El chiste va en el segundo cero, sin preámbulo de ninguna clase. La explicación es el
premio, no el peaje.

**S3 · El experimento**
Un estudio real con resultado contraintuitivo, contado como historia. Termina con la cifra
grande en pantalla y el DOI en la descripción. Obligatorio: `fuente` en la escena.

**S4 · Esto no tiene gracia y esto sí**
Dos chistes casi idénticos; uno funciona y otro no. Se cuentan los dos antes de explicar
nada. Motor de comentarios: la gente discute cuál es cuál.

**S5 · Diagnóstico en 30 segundos**
«Si haces esto, tu humor es de este tipo». Contenido de identidad, el que más comentarios
genera. **Siempre atado a la taxonomía real de estilos de humor del pilar B de la
bibliografía.** Un test inventado está prohibido (ver `REGLAS.md`).

### Reglas duras del Short

- Los **tres primeros segundos** deciden. Nada de logo, nada de «hola», nada de rótulo de
  serie antes del contenido.
- Texto en pantalla legible a 3 cm de alto: **cuerpo mínimo 64 px** en 1080×1920.
- Los subtítulos quemados van **entre el 15 % y el 70 % de la altura**. Por debajo los tapa
  la interfaz de YouTube.
- **Un remate.** Un Short sin remate es un recorte, y se rechaza en validación.

### Criterio de aceptación

Cinco Shorts producidos y subidos en una semana. Los cinco pasan `validar_guion.py`. La
ficha de QA confirma 1080×1920 y duración ≤55 s. A las 48 h, **al menos uno supera las 50
visualizaciones**; si ninguno lo hace, el problema está en los tres primeros segundos y se
va a C9 antes de producir más.

---

## C3 · Elegir los temas por demanda, filtrarlos por bibliografía

**Problema:** los temas salen de las 77 obras. «¿Qué puedo demostrar?» no es «¿qué quiere
saber alguien?».

### Archivo nuevo: `04_agentes/explorador_de_demanda.py`

Corre **los lunes a las 06:00** en Actions. Sin claves nuevas, sin coste.

**Fuentes, en orden de fiabilidad:**

1. **La propia API de YouTube — la señal más fiable y la más fácil de interpretar.**
   `search.list` con `q=<pregunta>`, `regionCode=ES`, `relevanceLanguage=es`,
   `order=viewCount`; luego `videos.list` sobre esos IDs para leer `viewCount` y fecha.
   *Si los diez primeros resultados de «cómo ser gracioso» suman medio millón de vistas,
   hay demanda; si suman dos mil, no la hay.* Es una medición directa y oficial, no una
   estimación.
   **Cuota:** `search.list` cuesta 100 unidades, `videos.list` cuesta 1. Veinte consultas
   semanales son ~2.020 de las 10.000 diarias, y una subida cuesta 1.600 — así que este
   agente corre **en un día sin producción**, o se parte en dos. Registrar el gasto.
2. **Autocompletar de YouTube** — `https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=<semilla>`
   Devuelve JSON con las búsquedas reales que empiezan por la semilla. Sin API key.
   Semillas de partida: `cómo ser gracioso`, `por qué nos reímos`, `sentido del humor`,
   `hacer reír`, `chistes que`, `humor negro`, `me da vergüenza`, `caer bien`,
   `conversación`. Expandir a dos niveles (semilla + cada letra del abecedario).
   **Aviso:** endpoint no documentado. Comprobado el 20/08/2026: responde y devuelve JSON
   válido. Si algún día deja de responder, el explorador **degrada a la fuente 1 y avisa**;
   no se rompe.
3. **Páginas vistas de Wikipedia** — oficial, gratuita, sin clave, estable desde 2015:
   `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/es.wikipedia/all-access/all-agents/<artículo>/daily/<inicio>/<fin>`
   Proxy de interés y sobre todo de **estacionalidad** para conceptos (`Humor`, `Risa`,
   `Comedia`, `Teoría_de_la_incongruencia`).
4. **Comentarios propios y de la competencia** — `commentThreads.list`, 1 unidad de cuota.
   Se buscan preguntas literales. Es la demanda de mayor calidad, porque viene de gente que
   ya te ve.
5. **JSON público de Reddit** — `https://www.reddit.com/r/<sub>/search.json?q=<término>` en
   `r/AskReddit`, `r/standup`, `r/socialskills`, `r/askspain`. Sirve para saber **con qué
   palabras** formula la gente la pregunta. **Solo lectura. Jamás escribir.**

> **No usar `pytrends`.** La librería se archivó en abril de 2025 y ya no funciona de forma
> fiable; la API oficial de Google Trends sigue en alfa de acceso limitado en 2026. Raspar
> los endpoints internos de Trends exige rotación de sesiones y mantenimiento continuo, que
> es justo lo que este proyecto no puede permitirse. Las fuentes 1 y 3 cubren lo mismo y
> son oficiales.

**Salida:** `05_calendario/demanda.json`

```json
{
  "generado_utc": "2026-08-24T06:00:00Z",
  "candidatos": [
    {
      "pregunta": "por qué no le hago gracia a nadie",
      "fuentes_demanda": ["youtube_search", "autocompletar", "reddit"],
      "vistas_top10": 512400,
      "video_top_mas_reciente": "2024-03-11",
      "competencia": "baja",
      "respaldo_bibliografico": ["B01", "J02", "H05"],
      "apto": true
    }
  ]
}
```

### La regla que impide que esto degenere en clickbait

> **La demanda elige la pregunta. La bibliografía decide si podemos responderla
> honestamente.**
>
> Si `respaldo_bibliografico` sale vacío, `apto` es `false` y **no se hace el vídeo**. Se
> anota en `05_calendario/pendientes_de_fuente.md` para que la próxima ronda de
> bibliografía lo mire. Nunca al revés: nunca se busca una fuente para justificar un tema
> que ya se ha decidido hacer.

### Cambio en `04_agentes/prompts/guionista.md`

El guionista recibe la pregunta en las palabras del usuario y **el título del vídeo debe
contener esa pregunta o su formulación más natural**. Un título de ensayo es motivo de
rechazo.

### Criterio de aceptación

`demanda.json` con al menos 30 candidatos, de los cuales ≥10 con `apto: true`. Los ocho
episodios de la tanda 2 salen de ahí, no de la bibliografía.

---

# FASE 2 · Empaquetado

Con impresiones ya existiendo, esta fase decide si alguien hace clic.

## C4 · El personaje

**Problema:** el 69 % de los vídeos que rompen llevan una cara en la miniatura (80 % entre
los que más rompen). Un canal sin cara no puede tenerla — salvo que se la dibuje.

### Qué es

Una **cabeza mecánica** en SVG, dibujada en el mismo lenguaje que el engranaje de marca:
trazo de 3 px, ámbar sobre azul marino, engranajes visibles. La boca es una línea
articulada; las cejas, dos bielas. Sin nombre propio de momento.

**No habla. Reacciona.** Es el escéptico, el que no lo pilla, el que lo pilla tarde.

### Expresiones mínimas (seis)

`neutra` · `duda` (una ceja) · `entiende` (las dos cejas arriba) · `no_le_hace_gracia`
(boca recta) · `se_ríe` · `piensa` (engranajes girados).

Un solo SVG con las piezas separadas; la expresión es una combinación de transformaciones
CSS. Nada de seis archivos.

### Archivos

| Archivo | Cambio |
|---|---|
| `02_marca/personaje.svg` | Nuevo. El SVG con las piezas identificadas por `id` |
| `02_marca/NOMBRE_Y_MARCA.md` | Sección nueva: qué es, cuándo aparece, cuándo no |
| `03_produccion/pipeline/escena.html` | Atributo `personaje: "<expresión>"` en cualquier escena; se pinta abajo a la derecha en horizontal, abajo centrado en vertical |
| `03_produccion/pipeline/miniatura.py` | El personaje entra en la miniatura ocupando entre ¼ y ⅓ del encuadre |
| `04_agentes/esquema_guion.json` | Campo `personaje` opcional por escena |
| `04_agentes/prompts/guionista.md` | Cuándo pedirlo: en el gancho, en el remate, y en la escena donde el espectador está pensando la objeción |

### Coste de render

**Cero.** El cambio de expresión ocurre en la entrada de escena, que `render.py` ya captura.
**No animar el personaje durante el tramo central** — eso multiplicaría las capturas. Si se
quiere movimiento continuo, va por C6.2 (capa compuesta en FFmpeg), no por aquí.

### Criterio de aceptación

El muestrario de `vista.py` pinta las seis expresiones y se distinguen a 320 px de ancho
(el tamaño real de una miniatura en móvil). `vista.py` informa del **mismo número de
unidades animables** que antes en las escenas sin personaje.

---

## C5 · Miniaturas que se vean

**Problema:** azul marino muy oscuro, sin cara y sin contraste alto. El 89 % de los vídeos
que rompen llevan una de las dos cosas. Estas no llevan ninguna.

### Reglas nuevas en `03_produccion/pipeline/miniatura.py`

1. **Fondo claro o saturado.** El `#0B1220` deja de usarse en miniatura. Paleta de fondos:
   ámbar saturado, cian saturado, coral, o blanco roto. El azul marino queda como color del
   vídeo, no de la portada.
2. **El personaje** ocupando entre ¼ y ⅓ del encuadre.
3. **Cuatro palabras o menos**, Archivo Black, con caja sólida detrás.
4. **Nada en la esquina inferior derecha** (ahí YouTube pinta la duración).
5. **Contraste verificado por código.** `miniatura.py` ya mide luminancia; añadir el
   cálculo del ratio de contraste WCAG entre el texto y su fondo inmediato y **salir con
   código distinto de cero si baja de 7:1**. El criterio deja de depender del gusto de
   nadie.
6. **Tres variantes por vídeo**: `miniatura_a.png`, `_b.png`, `_c.png`. Cambia **un solo
   elemento** entre variantes.

### El A/B pobre pero gratis

La prueba A/B de Studio no está en la API. `thumbnails.set` sí. El analista semanal:

1. Al publicar, sube la variante `a`.
2. A los 7 días anota el CTR y sube la `b`.
3. A los 14, anota y sube la `c`.
4. Se queda con la mejor y lo registra en `MEJORAS.md`.

No es un A/B limpio (el vídeo envejece entre medias) pero con tres semanas y varios vídeos
la señal aparece, y no cuesta nada.

### Criterio de aceptación

Las tres variantes generadas, todas pasando el umbral de 7:1, y la comparativa del
muestrario mostrando las miniaturas nuevas junto a las viejas a 320 px.

---

## C9 · Los primeros quince segundos

**Problema:** más del 55 % de los espectadores se pierden en los primeros treinta segundos
cuando la entrada es floja. En un canal de humor, además, el gancho es la demostración de
que el canal sabe de lo que habla.

### Cambio en `04_agentes/prompts/guionista.md`

**Prohibido abrir con:**
- la promesa del contenido («en este vídeo vamos a ver…», «hoy te explico…»)
- una cifra de autoridad sin escena («cincuenta años de investigación…»)
- «todo el mundo cree que…»
- cualquier presentación del canal antes del segundo 3

**Obligatorio abrir con una de estas tres:**
- **un chiste** que sea, él mismo, un ejemplo de lo que el vídeo explica
- **una escena concreta** con gente haciendo algo («son las tres de la tarde y tu jefe
  acaba de contar un chiste que no tiene gracia»)
- **una pregunta que el espectador conteste mentalmente** antes de que acabe la frase

**Y la regla que manda:** **la primera risa antes del segundo quince.** No una sonrisa
educada: algo construido para provocar risa.

### Cambio en `04_agentes/validar_guion.py`

- **Error** si la primera escena es de tipo `titulo` con narración de más de 8 s.
- **Error** si las primeras 40 palabras contienen cualquiera de las fórmulas prohibidas
  (lista literal en el propio validador, ampliable).
- **Aviso** si `notas_humor` no marca ningún remate en los primeros 15 segundos.

### Criterio de aceptación

Los ocho guiones de la tanda 2 pasan sin errores. La retención a los 30 s de los tres
vídeos siguientes sube respecto a la media de los cuatro publicados.

---

# FASE 3 · Producto

Con gente entrando y haciendo clic, esta fase decide si se quedan.

## C6 · Movimiento en pantalla sin coste de render

**Problema (el más importante del análisis técnico):** `render.py` captura una sola imagen
del tramo central de cada escena y la estira. Durante la mayor parte del vídeo la pantalla
está congelada, y la regla de retención pide cambio cada 3–5 segundos.

**La solución no es capturar más. Es que el vídeo compuesto se mueva.**

### C6.1 · Los subtítulos quemados: llegaron a funcionar y se retiraron

**Actualización del 20 de agosto, y cambia el plan.** El arreglo funcionó — MDH-003 salió
con `lineas_ass: 793` — y el codirector decidió **retirarlos**: palabra a palabra, en la banda
baja y sobre un diseño que ya es tipográfico, competían con el texto de la escena en vez
de acompañarlo. `montaje.py` los deja en `quemar_subs=False`, con el interruptor
`--con-subs` por si acaso.

Es la decisión correcta y la accesibilidad no se pierde: `publicar.py` sube el `.srt` a
YouTube desde el principio, y unos subtítulos activables se pueden traducir, buscar y leer
al tamaño de cada uno.

**Pero deja el problema entero encima de la mesa.** Eran lo único que se movía durante el
tramo central. Ahora ese tramo está completamente quieto, y C6.2, C6.3 y C6.4 pasan de ser
mejoras opcionales a ser **el trabajo pendiente más importante del canal**.

### C6.4 · Escenas más cortas y más numerosas — la vía que no se había visto

La más barata de todas, y no toca ni una línea de `montaje.py`.

`render.py` captura la **entrada** y la **salida** de cada escena fotograma a fotograma, y
del centro captura una sola imagen. Es decir: **cada escena nueva es movimiento que ya se
está pagando.** Un episodio de treinta escenas de 12 s y uno de sesenta escenas de 6 s
duran lo mismo, pero el segundo tiene el doble de entradas animadas y ningún tramo quieto
de más de cinco segundos.

Coste: el número de capturas sube más o menos en proporción al número de escenas. Con
2.043 capturas actuales sobre un máximo teórico de 13.350, hay margen de sobra dentro de
los minutos gratuitos.

**Hay que medirlo** antes de adoptarlo, regla 6 de `MEJORA_VISUAL.md`, pero es la única
vía que mejora el ritmo *narrativo* además del visual, porque obliga a que cada escena
tenga una sola idea.

### C6.2 · Una capa viva compuesta por FFmpeg

Un elemento pequeño en bucle superpuesto con `overlay` sobre el vídeo **ya renderizado**:
un engranaje que gira lento en una esquina, o una línea de barrido muy tenue.

- Asset: un único WebM/PNG en bucle de 2 s, en `03_produccion/assets/vivo/`.
- Filtro: `overlay` con `shortest=0` y bucle sobre el asset.
- **Cero capturas añadidas.** El coste es de FFmpeg, no del navegador.
- Opacidad máxima 12 %: tiene que notarse sin competir con el texto.

Archivo: `montaje.py` — **protegido**, pedir permiso.

### C6.3 · Movimiento de cámara, bien hecho esta vez

`zoompan` se descartó porque trunca el recorte a entero y la imagen salta un píxel. La
salida conocida es **escalar antes**: renderizar/escalar a 2× y hacer el recorte animado
sobre esa rejilla, de modo que el truncamiento caiga por debajo del píxel de salida.

- Probar con `scale=3840:2160` seguido de `crop` con desplazamiento animado, o `zoompan`
  con `s=3840x2160` y `d=1`.
- **Medir antes de adoptar** (regla 6 de `MEJORA_VISUAL.md`): tiempo del job antes y
  después, y comparar tres fotogramas consecutivos buscando el salto.
- Si el salto persiste, **se descarta y no se reintenta**. Con C6.1 y C6.2 ya hay
  movimiento.

### Criterio de aceptación

Analizando el vídeo terminado, **no hay ningún tramo de más de 5 segundos en el que la
diferencia entre fotogramas consecutivos sea nula.** Añadir esa comprobación a `qa.py`:
`tramos_congelados_s: [ ... ]` en la ficha.

---

## C7 · Dos voces

**Problema:** una voz sintética con cadencia fija durante siete minutos drena retención. Y
un canal sobre humor narrado por una sola voz neutra desperdicia el recurso cómico más
barato que existe: que alguien conteste.

### Los dos papeles

- **Narrador** — explica. La voz actual.
- **Escéptico** — interrumpe con la objeción que el espectador está pensando. Entre una y
  tres intervenciones por vídeo, siempre cortas (menos de 12 palabras), siempre antes de
  que el narrador la resuelva.

El escéptico **es** el personaje de C4. Misma identidad, dos canales de expresión.

### Implementación, en dos escalones

**Escalón 1 — hoy, gratis y sin riesgo:** dos voces distintas de `edge-tts` asignadas por
`escena.voz`. Cambio pequeño en `voz.py` (**protegido**: pedir permiso). El escéptico va
con una voz claramente distinta en timbre, no solo en tono.

**Escalón 2 — cuando el 1 esté probado:** Gemini TTS, que admite dos hablantes con control
de expresión por prompt. Ya hay `GEMINI_API_KEY` en los secretos. Está en *preview*, así que
`edge-tts` se queda como respaldo — la misma política de degradación que el proyecto ya
aplica en todo lo demás.

### Archivos

| Archivo | Cambio |
|---|---|
| `04_agentes/esquema_guion.json` | `voz: "narrador" \| "esceptico"` por escena, por defecto `narrador` |
| `03_produccion/pipeline/voz.py` | **protegido** — mapa de voces; los `WordBoundary` se concatenan respetando los desplazamientos de cada tramo |
| `04_agentes/prompts/guionista.md` | Cuándo entra el escéptico y cómo (nunca para hacer un chiste malo; siempre para decir en voz alta la duda real) |
| `04_agentes/prompts/chistologo.md` | El escéptico es material cómico: revisar sus intervenciones como se revisan los remates |

### Criterio de aceptación

Un episodio producido con las dos voces. Los subtítulos siguen cuadrando al fotograma
(comprobar con los seis fotogramas de QA). El nivel de audio sigue en −14 LUFS ±0,5 y el
pico por debajo de −1,0 dBTP.

---

## C8 · Menos vídeo largo, más corto

- **Un vídeo largo por semana**, de **4 a 6 minutos** (ahora 7:25). En 5–10 minutos, el
  rango bueno de retención es 50–70 %; es más fácil sostenerlo en cinco que en siete y
  medio.
- **Cinco Shorts por semana.**

Baja además la huella de «producción en masa» que preocupa por la política de contenido no
auténtico, y libera minutos de Actions para los Shorts.

**Archivos:** `05_calendario/parrilla.json`, `05_calendario/CALENDARIO.md`,
`04_agentes/validar_guion.py` (máximo de duración total para `formato: largo` = 380 s).

---

# FASE 4 · Compuesto

Cambios cuyo rendimiento llega en meses, no en semanas. Ninguno urge; todos suman.

## C10 · Una página web por episodio

**Archivo nuevo:** `03_produccion/pipeline/paginas.py` + `docs/` publicado en **GitHub
Pages** (gratis en repositorios públicos).

Genera una página por episodio con: el guion completo en texto, las figuras, las fuentes
con su DOI enlazado, y la nota de metodología. Índice por pilar temático.

**Por qué:** hay demanda en Google en español para «teoría de la ruptura benigna», «estilos
de humor de Martin», «por qué explicar un chiste lo mata», y casi nada bueno que la
responda. Trae tráfico externo, que es la tercera superficie que un canal sin audiencia
puede alcanzar.

Y es la parte del proyecto que más claramente **suma** algo a internet: divulgación seria,
en español, con fuentes enlazadas, gratis, que sigue siendo útil aunque el canal
desaparezca.

**Criterio de aceptación:** las páginas de los cuatro episodios ya publicados en línea, con
todos los DOI resolviendo, y `sitemap.xml` generado.

---

## C11 · El bucle de comentarios

1. **Al publicar**, `publicar.py` añade el primer comentario con la pregunta del episodio,
   vía `commentThreads.insert`. La pregunta ya la escribe el guionista desde el 19 de
   agosto.
   *(Fijar un comentario no está en la API v3. Se acepta sin fijar, o son diez segundos
   manuales. No forzarlo.)*
2. **Cada semana**, el analista lee los comentarios nuevos (`commentThreads.list`) y los
   pasa a `explorador_de_demanda.py` como fuente 3. Es la demanda de mayor calidad que
   existe: viene de gente que ya te ve.

**Prohibido:** responder comentarios con IA. Ver `REGLAS.md`.

### Y una función gratuita que conviene tener en el radar: **Hype**

YouTube permite a los espectadores «hypear» vídeos de canales de **menos de 500.000
suscriptores**, con tres hypes por semana y persona, y con **bonificación por canal
pequeño** —un hype sobre un canal de 10.000 suma más puntos que sobre uno de 100.000—. Los
puntos de los primeros siete días colocan el vídeo en una tabla regional semanal.

No sirve de nada con cero espectadores, pero **en cuanto haya unas decenas de personas
viendo los Shorts, pedirlo una vez en el cierre del vídeo largo es gratis y es
específicamente una palanca para canales pequeños.** Recordarlo cuando el nivel 1 de C14
esté superado; antes, no.

---

## C12 · Series con nombre y listas automáticas

Las listas de reproducción **sí** están en la API (`playlists`, `playlistItems`).
`publicar.py` asigna cada episodio a su serie al subirlo, creando la lista si no existe.

Series iniciales: **Desmonta el chiste**, **El experimento**, **Mecanismos**,
**Diagnósticos**.

**Por qué ahora:** desde febrero de 2026 YouTube redujo las notificaciones a los
espectadores poco activos. La campanita ya no es un canal fiable de retorno; las series con
nombre sí crean hábito.

---

## C13 · Salir de YouTube, sin ensuciar nada

| Canal | Qué se publica | Automatizable | Setup del codirector |
|---|---|---|---|
| **TikTok** | el mismo archivo vertical | sí, API de contenido | crear cuenta de marca |
| **Instagram Reels** | el mismo archivo vertical | sí, Graph API | crear cuenta de marca + vincular |
| **Bluesky / Mastodon** | un hallazgo al día + enlace al estudio | sí, API abierta | crear cuenta de marca |
| **Pódcast (Spotify)** | el audio que ya existe | sí, RSS generado por el workflow | dar de alta el RSS una vez |

**Todas las cuentas a nombre de Mecánica del Humor, ninguna a nombre del codirector.**

**Explícitamente NO:** publicación automática en Reddit o en foros. Es spam, va contra las
normas de esas comunidades y funciona en contra.

---

# PERMANENTE

## C14 · La métrica con la que se decide

Sustituye a la tabla de métricas de `05_calendario/CALENDARIO.md`. **Cada nivel no se mira
hasta haber pasado el anterior**; medir CTR sobre treinta impresiones es medir ruido.

| Nivel | Métrica | Umbral | Si no se pasa, el problema es |
|---|---|---|---|
| 1 | Impresiones por semana | ≥ 5.000 | **distribución** → C1, C2, C3 |
| 2 | CTR de miniatura | ≥ 4 % | **empaquetado** → C4, C5, títulos |
| 3 | Retención a los 30 s | ≥ 60 % | **el gancho** → C9 |
| 4 | Retención media | ≥ 45 % largo / ≥ 70 % Short | **el ritmo** → C6, C7, C8 |
| 5 | Suscriptores por mil vistas | ≥ 5 | **la promesa del canal** |

**Cadencia:** revisión **semanal**, los lunes. La tanda de cuatro semanas desaparece.

**Salida:** una entrada nueva en `05_calendario/MEJORAS.md` cada lunes, con el nivel en el
que está el canal, la métrica que lo bloquea y qué cambio se ha lanzado esa semana.

### El punto de parada honesto

Si a las **doce semanas** el nivel 1 sigue sin superarse, el problema no son los Shorts ni
las miniaturas: es que «la ciencia del humor» no es lo que la gente quiere ver. La
conversación entonces es sobre **ampliar el tema** —el humor dentro de habilidades sociales
y conversación, donde Charisma on Command demuestra que hay siete millones de personas— sin
renunciar ni al método ni a las fuentes.

Eso se decide con la tabla delante, no por agotamiento.

---

## Resumen para quien tenga prisa

1. **Hoy:** mirar Actions (P0.1). Sin eso no hay nada que hacer.
2. **Esta semana:** un solo canal (C1) y los primeros Shorts (C2).
3. **Semana que viene:** el personaje (C4), las miniaturas (C5), los ganchos (C9).
4. **Después:** movimiento (C6), dos voces (C7), menos largo (C8).
5. **En paralelo, sin prisa:** web (C10), comentarios (C11), series (C12), otras
   plataformas (C13).
6. **Siempre:** la tabla de C14, los lunes.

---

# C15 · El Short se mueve

**28 de agosto de 2026.** Sustituye a C6.2 y C6.3, que se cierran.

## El problema, medido

El tramo central de cada escena era **un fotograma estirado**, y ese tramo es el
85 % del vídeo. Renderizando MDS-005 (53 s) con el motor anterior salían **185
fotogramas en total**: para una escena de 9,1 s, 24 de entrada y **uno solo**
sobre los ocho segundos restantes. Tres capturas de la misma escena al 15 %, 50 %
y 85 % de su duración son idénticas píxel a píxel.

No es un despiste: estaba escrito en `voz.py` («*un vídeo sin subtítulos quemados
se percibe como un pase de diapositivas*»). Los subtítulos se retiraron el 20/08
(C6.1) y la respiración de zoom se había descartado antes. **Las dos únicas
fuentes de movimiento desaparecieron y no se puso nada en su lugar.**

## Por qué se puede arreglar ahora y antes no

Toda la arquitectura de captura se construyó sobre un presupuesto de render que
**no existe**: el repositorio es público y los minutos de Actions en runners
estándar sobre repositorios públicos son ilimitados. El único límite real es el
`timeout-minutes: 150` del job.

Medido: **259 ms por captura a 1080×1920**. Un Short de 60 s a 30 fps son 1.800
capturas, **7,8 minutos** de los 150 disponibles. Un largo de 5 min serían 38,8.

## Las cinco capas (solo formato vertical)

| | Qué | Dónde |
|---|---|---|
| C15.1 | Revelado palabra a palabra, 0,11–0,30 s/palabra según densidad; rebote en la palabra resaltada | `escena.html` · `pintar()` |
| C15.2 | Barra de avance del vídeo **entero** (no de la escena) | `escena.html` · `render.py` pasa `t_inicio`/`total_s` |
| C15.3 | Acercamiento lento del bloque, 2,2 % por escena | `escena.html` |
| C15.4 | Deriva de la retícula (2,2 px/s), personaje que respira y engranaje que gira; diagrama apilado; composición y cuerpo de letra por densidad | `escena.html` |
| C15.5 | Remate de marca en el último 1,25 s del cierre | `escena.html` · `render.py` |
|  | Captura continua en `formato: corto` | `render.py` · `vivo` |

**C15.3 es C6.3 resuelto en la capa correcta.** La bitácora del 24/08 midió que
`zoompan` de FFmpeg necesita preescalar a ×4 para no temblar, a un coste de 5,3×,
porque trunca a píxel entero. El navegador lo hace con precisión subpíxel y
gratis. La medición no se tira: es la que justifica no hacerlo en FFmpeg.

## Criterio de aceptación

- `05_calendario/qa/<ID>/ficha.json` de la primera producción nueva y los seis
  fotogramas mirados **antes** de publicar (regla 11.2).
- El episodio largo **no cambia**: `vivo` solo se enciende con `formato: corto`.
  Se decide con las métricas del Short delante (regla 11.1).
- Comprobado antes de entrar: 1.274 fotogramas frente a 185, y **cero de 59 pares
  de fotogramas consecutivos idénticos**.

## Lo que NO se hace

- No se vuelven a encender los subtítulos quemados. El motivo de C6.1 sigue en pie.
- No se toca la regla 12: el remate de marca va **después** de la crítica, no en
  su lugar.
- No se enciende `vivo` en el episodio largo todavía.

---

# Versión 4 · 31 de agosto de 2026 — la primera lectura con datos

Todo lo de arriba sigue vigente salvo lo que esta sección corrige expresamente:
**C14 se sustituye por dos escaleras** y entran **C17 a C20**. Lo escrito antes
del 31 de agosto no se reescribe: se lee con esta sección al lado.

## Lo que dijeron los números

Tres semanas de canal, dos de Shorts, y por primera vez `metricas.json` con
lecturas de verdad:

| | Vistas de por vida | Suscriptores | Comentarios | Me gusta |
|---|---|---|---|---|
| MDH-001 · 002 · 003 (largos, 18–20 ago) | 13 · 28 · 8 | 0 | 0 | 4 en total |
| MDS-001 a 005 (Shorts, 24–28 ago) | 6 · 11 · 13 · 3 · 11 | 0 | 0 | **0** |

**El criterio de aceptación de C2 —«a las 48 h, al menos uno supera las 50
visualizaciones»— falló por un factor de diez.** El plan decía qué hacer en ese
caso («el problema está en los tres primeros segundos y se va a C9 antes de
producir más») y no se hizo: se siguió produciendo. Queda dicho.

**Y el único indicio bueno del corpus: la búsqueda.** MDS-002 sacó el **63,6 %**
de sus visualizaciones de `YT_SEARCH` y MDS-003 el **46,2 %**. El feed de Shorts,
que es la superficie sobre la que se construyó toda la fase 1, aporta entre el
9 % y el 23 % en esos dos. Es decir: **la superficie que el diagnóstico daba por
inalcanzable está respondiendo, y la que se daba por segura no.** Los números son
minúsculos y no prueban nada por sí solos, pero es la única señal direccional que
hay, y sale gratis seguirla.

## C14 (bis) · Dos escaleras, porque son dos productos

**Por qué se cambia:** la escalera original medía impresiones y CTR de miniatura,
y **Studio no da ninguna de las dos para los Shorts** — ahí la decisión del
espectador es deslizar, no hacer clic. Cinco de cada seis vídeos del canal son
Shorts. La escalera que teníamos no podía medir el producto principal, y encima
dependía de que el codirector exportara un CSV a mano cada semana, que es trabajo
recurrente y por tanto contrario a la regla 5.

**Escalera de los Shorts — solo API, sin intervención de nadie:**

| Peldaño | Métrica | Umbral | Si falla, el problema es |
|---|---|---|---|
| S1 · el feed nos prueba | vistas desde `SHORTS` en 48 h | ≥ 50 | **el primer segundo** → C19, C16 |
| S2 · se quedan | `porcentaje_visto` | ≥ 70 % | **el ritmo y la voz** → C15, C7 |
| S3 · reaccionan | me gusta por 100 vistas | ≥ 3 | **el remate** |
| S4 · vuelven | suscriptores por mil vistas | ≥ 5 | **la promesa del canal** |

**Escalera del episodio largo — con CSV si lo hay, y si no se salta a L3:**

| Peldaño | Métrica | Umbral |
|---|---|---|
| L1 · impresiones/semana | ≥ 5.000 | solo con CSV |
| L2 · CTR de miniatura | ≥ 4 % | solo con CSV |
| L3 · retención a los 30 s | ≥ 60 % | API |
| L4 · porcentaje visto medio | ≥ 45 % | API |

**El canal está en S1**, a un factor diez del umbral. El CSV pasa a ser opcional:
si aparece uno en `05_calendario/exportes/` se lee, y nadie vuelve a pedirlo.

## El punto de control del 27 de septiembre

Entre medias entra un cambio por semana: **C19 + C16** la semana del 7, **C7** la
semana del 14. El 27, con la tabla delante, una sola pregunta:

> **¿Algún Short ha pasado de 100 visualizaciones en sus primeras 48 horas?**

- **Sí** → el formato funciona, toca escalarlo.
- **No, pero la mediana ha subido de 11 a 30 o más** → el camino es bueno y va
  lento. Se sigue.
- **No, y la mediana sigue por debajo de 20** → el problema no es la ejecución,
  es el tema. Se abre la conversación de ampliar el asunto al humor dentro de las
  habilidades sociales y la conversación, sin renunciar al método ni a las
  fuentes.

El punto de parada de las doce semanas sigue siendo el límite exterior. Este es
un control intermedio, no un indulto.

---

## C17 · No repetirse

**El hallazgo, del codirector:** «en el vídeo hay cosas que se repiten, como que te
ríes más junto a alguien que solo».

**Medido el 31/08 sobre los códigos de `fuente` de todos los guiones:**

- Se usan **30 fichas de las 77**. Cuarenta y siete no se han abierto nunca.
- **Doce salen en más de un guion; cuatro en tres o más.** `E02` —las 1.200 risas
  anotadas en la calle— sale en **MDS-002 (25 ago), MDH-004 (29 ago) y MDS-006
  (31 ago)**: tres vídeos en siete días. `A01` sale en cinco guiones.

No es escasez de bibliografía. Es la costumbre de coger la ficha que ya se conoce.

**Las dos reglas:**

1. **Una ficha que ha sido la fuente central de un vídeo no vuelve a serlo en seis
   semanas.** Como apoyo de pasada sí, y entonces se cuenta desde otro ángulo y
   con otras palabras, nunca con la misma frase.
2. **Se elige empezando por las fichas no usadas.** Si se acaba usando una
   repetida, se escribe en la bitácora por qué ninguna de las libres servía.

**Dónde vive:** criterio en el prompt de la planificación (paso 2) y en el de la
revisión diaria (paso 1); red de seguridad determinista como **aviso** de
`04_agentes/validar_guion.py`, encargado a la revisión diaria.

## C18 · La música cansa

Tres pistas reales para seis vídeos por semana —`cama.mp3` es copia byte a byte de
una de las otras— significa que cada pista suena una vez y media por semana. Lo
notó primero el codirector, que hoy por hoy es el espectador que más vídeos ve.

**Qué se hace:** ampliar a diez o doce pistas de licencia limpia y atribución
literal (Incompetech, CC BY 4.0, es la fuente más simple: una licencia, un formato
de atribución por pista, descarga directa), instrumentales y sin melodía que
compita con la voz. Cada una con su entrada en `creditos.json` indexada por
sha256, como ya está montado — `publicar.py` bloquea la subida si falta, y eso se
queda. Y en `musica_de()`: excluir duplicados por hash y no repetir una pista
hasta que hayan sonado todas.

Prioridad baja. Encargado a la revisión diaria, detrás de la verificación de C15.

## C19 · El primer segundo no puede ser una tarjeta de texto

**El razonamiento, y es el cambio más importante de esta versión.** Un Short nuevo
recibe una prueba del feed casi siempre. Seis a trece visualizaciones significa
que la prueba se hizo y se cortó enseguida: la gente desliza antes de leer. Y lo
que ve en esa décima de segundo es texto blanco centrado sobre fondo oscuro con
voz sintética — que en 2026 es la firma reconocible del vídeo automatizado, y el
espectador de Shorts ha aprendido a deslizarla sin pensar.

C15 hace que ese texto se mueva. **No hace que deje de ser texto.** De las 58
escenas de los diez primeros Shorts, 32 son `enunciado` y `figura` no se usa
ni una vez: el 72 % de lo que se ve es texto sobre fondo.

**La regla:** la escena 1 de un Short no puede ser una tarjeta de texto. Entra con
una ilustración del vocabulario dibujado (C16) en movimiento, con el Engranaje
haciendo algo, o con una comparación — y con cuatro palabras o menos en pantalla.
La voz sigue siendo la de siempre hasta C7; lo que cambia es lo que se ve mientras
habla.

**Cuándo:** semana del 7 de septiembre, junto con C16, y cuenta como **un solo
cambio** a efectos de la regla 11.1. Antes no: la semana del 31 es de MDS-006 y de
verificar C15 con los ojos.

**C16 se reordena en consecuencia:** el vocabulario dibujado ya no entra «una
ilustración por Short, donde encaje», sino **empezando por la escena 1**. Los
iconos ya están en `02_marca/iconos.svg`.

## C20 · El primer comentario ya no se publica (defecto conocido, aplazado a propósito)

`publicar.py` publica la pregunta del episodio como primer comentario solo si
`estado == "public"` en el momento de la subida. Desde el 31/08 el modo es
`automatico` y todo se sube en privado con `publishAt`, así que **la condición no
se cumple nunca y C11 ha dejado de funcionar de hecho**. El campo
`pregunta_pendiente` se escribe en `publicado.json` y no lo lee nadie.

**El arreglo, escrito para cuando toque:** un paso `--pendientes` en `publicar.py`
que recorra el registro buscando entradas con `publicar_en` ya pasado y
`pregunta_pendiente`, compruebe contra la API que el vídeo es público, publique el
comentario y marque la entrada. Se llamaría al principio de la producción del día
siguiente.

**No se hace ahora, y el motivo es honesto:** el canal tiene cero comentarios y una
decena de espectadores por vídeo. Un primer comentario no cambia nada hasta que
haya alguien a quien contestar. Entra cuando S3 se mueva.

## Lo que NO se cambia hoy, y por qué

- **La cadencia sigue en cinco Shorts y un largo.** Con este volumen de audiencia,
  más papeletas en el sorteo del feed vale más que menos vídeos mejores — pero es
  una creencia, no un dato, y se revisa el 27 de septiembre.
- **No se acelera C7 por delante de C19.** La voz importa para quien se queda; el
  deslizamiento ocurre antes de que la voz llegue a nada. Primero lo que se ve.
- **No entra C10 (una página por episodio)** aunque la búsqueda esté funcionando.
  Sigue detrás del peldaño S1: primero que el vídeo aguante, luego traerle gente
  de fuera.
- **Sigue sin haber barrera automática antes de publicar.** `qa.py` corre
  **después** de la subida en `producir.yml`: es un informe, no un control. Con la
  publicación automática, el único par de ojos previo es la revisión diaria de las
  11:30, que ve el vídeo dentro de la ventana de ~15 h entre subida y publicación.
  Decisión del codirector del 31/08, tomada con la audiencia actual delante: un mal
  vídeo hoy no cuesta nada, y él lo puede retirar. Se revisa cuando haya público.


---

# Versión 5 · 4 de septiembre de 2026 — dejar de publicar vídeos rotos

Todo lo anterior sigue vigente salvo lo que esta sección corrige expresamente.
Cinco decisiones, una de ellas de infraestructura y cuatro de producto.

## Dónde está el canal esta mañana

Tres Shorts seguidos por encima de 20 visualizaciones —**31, 21 y 21**— contra
una mediana de 11 en la primera tanda. Un «me gusta», el primero del canal. El
umbral de S1 sigue siendo 50 desde el feed en 48 horas y seguimos por debajo,
pero por primera vez el número se mueve en la dirección buena y **se mueve desde
que entró C15**, que es exactamente lo que el cambio prometía. La rama del punto
de control del 27 en la que estamos hoy es la segunda: «va lento, el camino es
bueno, se sigue».

Y en la misma semana, dos vídeos rotos: MDS-007 con la lista tapada (01/09) y
MDS-009 con «generosos» cortado y una escena que decía en pantalla algo que la
voz no menciona (03/09). Los dos se publicaron. **Ese es el problema de esta
versión.**

---

## C21 · La barrera: el render falla si el texto no cabe

**Lo que pasó.** El 3 de septiembre se publicó un Short en el que la escena 3
ponía «Más gener» — la palabra estaba cortada contra el borde del lienzo porque
`.cifra` tiene un tamaño fijo (300 px en vertical) sin ningún ajuste por
longitud. La revisión diaria lo encontró a las 11:30, siete horas y media antes
de publicarse, lo describió con precisión, y **decidió no marcarlo como
incidencia** razonando que no podía cancelar la publicación. Nadie lo vio hasta
que lo vio el codirector, ya publicado.

**El diagnóstico, que no es «hay que revisar mejor».** Un texto que no cabe en su
caja es una condición booleana. Pedirle a un agente que la vea mirando cinco
fotogramas es pedirle que haga a ojo lo que el navegador ya sabe con exactitud.
Llevamos dos semanas construyendo revisiones cada vez más finas sobre un pipeline
que no tiene **ni una sola comprobación que pueda decir que no**: `qa.py` corre
después de subir (trampa 6), y la revisión diaria no toca YouTube.

**La decisión.** `render.py` gana una barrera. Después de pintar cada escena y
antes de capturarla, comprueba en el navegador, para cada elemento de texto, si
`scrollWidth > clientWidth + 1`, si `scrollHeight > clientHeight + 1` o si su
rectángulo se sale del lienzo. Si algo se sale, **`SystemExit` con el número de
escena, el selector y el texto** — igual que ya se hace cuando falla FFmpeg.

**Por qué esto sí es una barrera y `qa.py` no lo era:** el render corre *antes*
que `publicar.py` en `producir.yml`. Un fallo aquí impide que se suba nada. Es la
primera vez que el proyecto tiene un control previo a la publicación, y se
consigue **sin tocar `producir.yml`**, que está protegido.

**El precio, aceptado a sabiendas:** un día sin vídeo si la barrera salta y nadie
lo arregla en el día. Con veinte espectadores, un hueco cuesta menos que una
palabra partida. Se revisa cuando haya público.

**Después, y solo después, el arreglo de fondo (C21.1):** extender a `.cifra`, a
`.pie` y a `ul.lista` la escalera `txt-xs`/`txt-s` que ya encoge `.enunciado`
según el número de palabras. Va segundo a propósito: **con la barrera puesta, el
umbral se puede elegir midiendo en vez de adivinando** — si te quedas corto, el
render falla y lo ves. Riesgo pendiente ya localizado: `MDH-005`, `cifra: "El
peor de los cuatro"`.

**Encargado a la revisión diaria**, prioridad 1, por delante de todo lo demás.

### C21.2 · Y el criterio de incidencia estaba al revés

«No puedo cancelarlo, luego no es una incidencia» es exactamente el razonamiento
que hay que prohibir. La revisión no puede retirar un vídeo; **el codirector sí**, y
`ESTADO.md` es el único sitio por el que se entera. Que el agente no pueda
arreglarlo es el motivo para avisar, no para callar.

Regla nueva, ya escrita en el prompt: **si el vídeo que se publica hoy tiene un
defecto que un espectador notaría, la primera línea de `ESTADO.md` dice
`INCIDENCIA`**, con el ID, la hora de publicación y qué puede hacer el codirector.
Lo que nadie ve todavía —un guion sin producir, un encargo sin hacer— sigue
siendo `OK` y va en la bitácora.

Y la revisión del vídeo pasa de «lunes y jueves» a **todos los días**. Con un
vídeo diario, mirarlo cuesta minutos.

---

## C22 · Los dos canales — es regla, no criterio

Sube a `REGLAS.md` como **regla 14**, con su caso. El resumen: lo que está en
pantalla tiene que estar sostenido por la narración de esa misma escena; lo
esencial de la narración tiene que tener correlato en pantalla; y la cara del
personaje concuerda con lo que se dice.

**Red de seguridad determinista**, encargo 3 de la revisión diaria: un **aviso**
en `validar_guion.py` que saque las palabras de contenido de `texto`, `cifra` y
`pie` y señale las que no aparecen en la `narracion` de su escena, comparando por
raíz. Sobre MDS-009 tiene que avisar de «dinero» y «mesa». Es tosco a propósito:
no decide, señala dónde mirar — como el aviso de C17, que el 3 de septiembre hizo
que la planificación tirara un guion entero antes de publicarlo. **Ese es el
patrón que funciona en este proyecto: comprobaciones tontas y deterministas que
le dicen a un agente listo dónde poner los ojos.**

---

## C23 · El token de YouTube deja de caducar

**El problema.** El 1 de septiembre el canal no publicó porque `YT_REFRESH_TOKEN`
había caducado. La causa es que la aplicación de OAuth está en modo **«Prueba»**,
y Google documenta que en ese modo el token de actualización caduca a los **siete
días**. Renovarlo a mano cada semana es trabajo recurrente y por tanto contrario a
la **regla 5**: no es una molestia, es un cambio mal diseñado.

**La salida, y no exige inventarse nada.** Publicar la aplicación —«Público» /
«En producción»— **sin pedir la verificación**. Son cosas distintas y se
confunden siempre:

- **Publicar** es un botón. Cambia el estado a producción y con eso **el token
  deja de caducar a los siete días**.
- **Verificar** es un formulario, y es lo que pide página web, política de
  privacidad, términos de servicio y un vídeo de demostración. **No hace falta
  para publicar.** Solo hace falta para pasar de 100 usuarios o para quitar la
  pantalla de aviso.

Lo que se paga por no verificar, con la lista delante:

| | |
|---|---|
| Pantalla de «Google no ha verificado esta aplicación» al dar el consentimiento | Una vez, y se pasa con *Configuración avanzada → Ir a…* |
| Tope de **100 usuarios** durante toda la vida de la aplicación | Necesitamos **uno**. Irrelevante |
| Los ámbitos siguen siendo restringidos y sin verificar | Ya lo son hoy, y funcionan |

**El riesgo que sí hay que mirar, y se dice sin adornar.** La documentación de la
API de YouTube afirma que «*todos los vídeos subidos por el endpoint
`videos.insert` desde proyectos de API sin verificar creados después del 28 de
julio de 2020 quedarán restringidos a modo privado*». Empíricamente **eso no nos
está pasando**: los nueve vídeos del canal se han subido en privado con
`publishAt` y YouTube los ha hecho públicos solos. La auditoría de YouTube es un
eje **distinto** del estado de publicación de la pantalla de consentimiento, así
que publicar no debería cambiar nada ahí — pero eso es un razonamiento, no una
medición, y conviene comprobarlo con el primer vídeo que salga después del
cambio, no dentro de una semana.

**Cómo se comprueba, sin gastar un vídeo:** el Short del lunes 7 se sube de
madrugada y se publica a las 19:00. La revisión diaria de las 11:30 ya mira
`registro_publicaciones.json`; si el vídeo aparece `private` con `publicar_en`
como siempre, no ha cambiado nada. Si apareciera bloqueado como privado, se
revierte el estado a «Prueba» y volvemos al token de siete días mientras se
piensa otra cosa. Reversible en un clic.

**Lo que NO se hace, y por qué:**

- **Cuenta de servicio**: no sirve. YouTube no acepta cuentas de servicio para
  subir a un canal.
- **Renovar el token con un workflow**: no se puede. Google no emite un token de
  actualización nuevo al usar el existente, así que no hay nada que rotar sin
  volver a pasar por el navegador.
- **Tipo «Interno»**: exige Google Workspace. La cuenta es de Gmail.
- **Dejarlo como está con un aviso**: es la regla 5 otra vez. Un canal que se
  para cada siete días si nadie se acuerda no vuela solo.

**Lo que hace el codirector, una vez, ~10 minutos:** en la consola de Google Cloud,
*APIs y servicios → Pantalla de consentimiento de OAuth → Audiencia →* botón
**Publicar aplicación**, aceptar el aviso de que la verificación queda pendiente,
volver a generar el `YT_REFRESH_TOKEN` con el flujo de siempre y actualizar el
secreto del repositorio. Y ya no se vuelve a tocar.

---

## C7 · Cambia el rumbo: se salta el escalón 1

**El escalón 1 —dos voces distintas de `edge-tts` asignadas por
`escena.voz`— se descarta.** No se aplaza: se descarta.

**El motivo.** Lo que está roto no es que haya una sola voz: es que la voz que
hay no tiene ritmo, ni pausa, ni entonación. Lee palabras. Dos voces de
`edge-tts` entregan **dos lectores planos en vez de uno**, y consumen la semana
del 14 sin tocar el problema. El plan encadenó los escalones cuando el escalón 2
parecía caro y arriesgado; hoy sabemos que el nivel gratuito de
`gemini-3.1-flash-tts-preview` incluye la salida de audio, que admite **dos
hablantes en una sola llamada** y que **el estilo, el acento, el ritmo y el tono
se dirigen en lenguaje natural**, con etiquetas dentro del propio texto. Eso es
literalmente lo que falta.

**Lo que entra en su lugar, esta semana y a coste cero:**
`04_agentes/prueba_voz.py` (escrito hoy) genera tres audios del mismo guion —
`edge-tts` como referencia, Gemini escena a escena con las pausas de hoy, y
Gemini en **una sola llamada con dirección de actor** para que el ritmo lo decida
el modelo y no nuestro empalme. Corre por `workflow_dispatch` con
`voz_prueba.yml`. El codirector escucha tres ficheros y decide. **Si el modelo o el
nivel gratuito han cambiado, el script falla con el error a la vista — y ese
fallo también es un resultado.**

**Una dependencia que hay que decir antes y no descubrir a mitad de semana**
(trampa 1: cuando quites algo, mira qué dependía de ello). `voz.py` construye los
subtítulos con las marcas de tiempo por palabra que devuelve `edge-tts`, y Gemini
no las da. Comprobado hoy en el código: **el `.srt` que se sube a YouTube se
escribe por bloques de escena** (`bloques`, `voz.py` línea 302), no por palabra,
así que **sobrevive intacto al cambio de motor**. Lo que muere es el `.ass`
—que no se quema desde el 20/08— y con él el canario `lineas_ass > 0` de `qa.py`,
que habrá que sustituir por otra comprobación (que la duración del audio cuadre
con la suma de las escenas sirve). No es un bloqueante; es una tarea que ya está
identificada.

**Calendario nuevo:** prueba y decisión la semana del 7 (no ocupa la ranura de
cambio, porque no toca la producción); **C7 escalón 2 en producción la semana del
14**, que era la fecha que ya tenía. `edge-tts` se queda como respaldo, con la
misma política de degradación que el resto del proyecto.

### C7.1 · La cuota decide la arquitectura, y ya está decidida (misma tarde)

La primera versión de `prueba_voz.py` pedía **una llamada por escena** y murió
con `RESOURCE_EXHAUSTED` en el primer intento real. Los números del nivel
gratuito, **por modelo**:

| | Límite | Lo que gastábamos |
|---|---|---|
| Peticiones por minuto | **3** | 7 seguidas |
| Peticiones por día | **10** | 7 por ejecución |
| Tokens de entrada por minuto | 10.000 | 62 |

**El cuello de botella no es el tamaño: es el número de peticiones.** Un Short
entero son ~300 tokens de entrada, el 3 % del límite por minuto.

Y eso no es un problema de la prueba, **es el que decide cómo se implementa C7**:
con diez peticiones al día, un episodio largo de cuarenta escenas troceado por
escena es imposible. Una llamada por vídeo son **seis peticiones a la semana**,
y además es la única forma de que el ritmo lo decida el modelo en vez de nuestro
empalme — que era el objetivo. **Así que si Gemini entra, entra con el guion
entero en una sola llamada.** No hay que volver a discutirlo.

**El problema que eso abre, y que la prueba ya contesta sin gastar una petición
más:** si el audio viene de una sola pieza, `render.py` no sabe cuánto dura cada
escena, y sin eso no puede sincronizar el vídeo. La salida es medir los
silencios: la dirección pide una pausa clara entre líneas, y el script analiza la
onda devuelta, cuenta los tramos de voz y los compara con el número de escenas
del guion. **Si cuadran, C7 escalón 2 es viable tal cual. Si no cuadran**, el
plan B es partir el guion en dos o tres llamadas —sigue cabiendo de sobra en diez
al día— y cerrar el corte donde nos convenga.

**Y hay un respaldo de cuota que no cuesta nada tener a mano:**
`gemini-2.5-flash-preview-tts` es otro modelo con **su propia cuota diaria**. Si
se agotan las diez de 3.1 probando, se relanza con ese en vez de esperar a
mañana. El workflow lo ofrece en un desplegable.

---

## C24 · Que no todos los vídeos parezcan el mismo vídeo

Hallazgo del codirector, del 2 y el 4 de septiembre: los contenidos están bien y
los guiones cierran mejor unas veces que otras, pero la presentación es idéntica
en todos — mismos fondos, mismo dinamismo, misma miniatura, misma voz. Cinco
Shorts a la semana con la misma cara son cinco veces el mismo vídeo para quien
pasa por el feed.

**Las cinco series ya existen y no se distinguen en pantalla.** «Desmonta el
chiste», «El experimento», «Esto no tiene gracia y esto sí», «Diagnósticos» y
«Ríete primero, te explico después» tienen forma narrativa propia y aspecto
común. Que cada una tenga su acento —un color de apoyo dentro de la paleta de
marca, una composición de partida, un tratamiento de fondo— es barato, es
determinista, no sube el coste de render y además construye lo que C12 buscaba:
que se reconozca la serie.

**Prioridad: detrás de C7.** No porque no importe, sino porque el orden de la
versión 4 sigue en pie —primero lo que se ve en el primer segundo (C19+C16, la
semana del 7), luego lo que se oye (C7, la semana del 14)— y meter variedad
visual encima de C19 rompería la regla de un cambio por producción justo en la
semana en que hay que medir si C19 funciona.

**La miniatura de un Short sí importa, y hasta hoy dábamos por hecho que no.**
En el feed no se ve; **en los resultados de búsqueda sí**, y la búsqueda es la
superficie que nos está dando el 46-64 % de las visualizaciones. C5 ya genera
tres variantes verticales con contraste medido. Queda pendiente comprobar que la
que se sube es la buena y que se lee a tamaño de resultado de búsqueda: se mira
en la revisión del lunes 7, con las miniaturas de los diez Shorts al lado.

---

## Lo que NO cambia hoy

- **La cadencia.** Cinco Shorts y un largo. Se revisa el 27 de septiembre, no antes.
- **El punto de control del 27 de septiembre**, con sus tres desenlaces escritos
  en la versión 4. Los datos de esta semana empujan hacia el segundo.
- **No se amplía el tema todavía.** La pregunta del codirector del 31/08 tiene
  respuesta: no es que el tema esté descartado, es que **con C19, C16 y C7 sin
  soltar todavía no se sabe qué está fallando**, y ampliar el tema ahora
  destruiría la única medición limpia que vamos a tener. Las dos sondas que la
  planificación metió en las semillas del 10 —«cómo mantener una conversación sin
  quedarse en blanco» y «cómo caer bien en una primera conversación»— están ahí
  precisamente para llegar al 27 con cifras en vez de opiniones.
- **C20 (el primer comentario) sigue aplazado.** Ahora hay un «me gusta», no una
  conversación. Entra cuando S3 se mueva.


---

# Versión 5.1 · 4 de septiembre, tarde — la prueba de voces, medida

## Lo que se oyó y lo que dicen los números

El codirector escuchó las tres pistas: **las dos de Gemini mejoran a `edge-tts`**, y
entre ellas no supo decidir — «parejas, quizá un poco mejor la dirigida», con una
diferencia de volumen a favor de la plana. Aprobó el cambio.

Medido después sobre las ondas (`07_pruebas/prueba-de-voces/`), el empate no lo
era:

| | Duración | Voz | Ritmo | RMS | RMS solo voz |
|---|---|---|---|---|---|
| Objetivo del guion (MDS-010) | **50,7 s** | — | — | — | — |
| `edge` (lo de hoy) | 41,4 s | 41,4 s | 2,63 pal/s | — | — |
| `gemini_plano` | 37,4 s | 23,0 s | **4,74 pal/s** | −18,4 dB | −16,3 dB |
| `gemini_dirigido` | **83,2 s** | 41,3 s | **2,64 pal/s** | −21,5 dB | −18,5 dB |

Tres conclusiones, y ninguna se podía oír:

1. **La dirigida no está leyendo las instrucciones en voz alta**, que era la
   sospecha razonable ante 83 segundos. Su tiempo de voz —41,3 s— coincide con el
   de `edge` —41,4 s— hasta la décima, y su ritmo (2,64 palabras por segundo) es
   el del español natural. **Los 42 segundos de más son silencio.** El modelo se
   tomó al pie de la letra la instrucción «deja una pausa clara entre líneas, y
   donde ponga [pausa] la pausa es larga».
2. **La plana corre.** 4,74 palabras por segundo de voz es casi el doble del
   habla natural: mete el guion entero en 23 segundos de voz. Suena «más clara y
   más fuerte» porque es más densa y no respira, no porque esté mejor dicha.
3. **La diferencia de volumen es irrelevante.** Con la voz sola son 2,2 dB, los
   picos de las dos están a menos de 1 dB del máximo, y `montaje.py` normaliza
   todo a −14 LUFS (`loudnorm=I=-14:TP=-1.5:LRA=11`). En producción esa
   diferencia desaparece.

**Y la instrucción que estropeó la dirigida la puse yo, para un experimento que
ya sabemos que falló.** Las pausas largas estaban ahí para poder cortar el audio
por los silencios y repartirlo entre escenas. El informe dice que no cuadra: 16
tramos para 6 escenas en la plana, 33 en la dirigida, y ningún umbral de silencio
da 6 —probado a 0,6 s, 0,8 s y 1,0 s: salen 8, 5 y 4—. **Cortar por silencios se
descarta.**

## C7.2 · Cómo entra Gemini: una llamada por escena, solo en los Shorts

Descartado el corte por silencios, la única forma de saber cuánto dura cada
escena es **pedir cada escena por separado**, que además es exactamente la
arquitectura de hoy — el cambio se reduce a cambiar el motor dentro de
`sintetizar()`.

| | Llamadas/día | ¿Cabe en 10? |
|---|---|---|
| Short de 5–8 escenas | 5–8 | **sí**, con margen para el respaldo |
| Episodio largo de 40 escenas | 40 | **no** |

**Decisión: los Shorts pasan a Gemini; el episodio largo del sábado se queda en
`edge-tts`.** Son cinco de cada seis vídeos y son el producto. El largo entra
cuando sepamos agrupar escenas sin perder el reparto de tiempos, o nunca.

Y la dirección se reescribe **sin la instrucción de las pausas**: las pausas
entre escenas ya las ponemos nosotros, deterministas, desde `pausa_despues_s`.
Lo que se le pide al modelo es lo único que `edge-tts` no sabe hacer — que
cuente en vez de leer, dentro de la escena.

### Las salvaguardas, que son la parte que no se puede improvisar

`voz.py` está autorizado desde el 28/08, pero es el fichero del que cuelga la
producción diaria. Encargado a la revisión diaria con estas condiciones:

1. **Interruptor con respaldo automático.** Parámetro `--motor {edge,gemini}`.
   **Cualquier** fallo de Gemini en una escena —cuota, red, respuesta vacía—
   sintetiza esa escena con `edge-tts` y sigue. Un vídeo con una voz peor es
   mejor que un día sin vídeo. Es la misma política de degradación que el resto
   del proyecto.
2. **Se escribe qué motor se usó**, escena a escena, en `ficha.json`. Si un día
   la mitad del vídeo sale con voz de respaldo, tiene que verse en el expediente
   y en `ESTADO.md`, no descubrirse escuchando.
3. **25 segundos entre llamadas.** El límite es de 3 por minuto. Dos minutos y
   medio de más en un job de veinte no es nada.
4. **Control de ritmo por escena.** Palabras dividido entre segundos de audio
   fuera de 1,6–3,2 es un aviso en `ficha.json`: es la firma de la pista plana,
   que corría al doble. No bloquea —el vídeo se sincroniza con la duración real,
   así que no se desincroniza nada— pero se ve.
5. **El `.srt` no cambia.** Se escribe por bloques de escena (`voz.py` línea
   302), no por palabra: sobrevive intacto. Lo que muere es el `.ass`, y con él
   el canario `lineas_ass > 0` de `qa.py`. **Hay que sustituirlo antes de
   encender Gemini**, no después: sirve que la suma de las duraciones de escena
   cuadre con la duración del audio final, que es lo que de verdad importa
   comprobar.
6. **Se enciende con un episodio, no con la semana.** Primer Short con Gemini el
   lunes 14. Si `ESTADO.md` de ese día no dice `OK`, se vuelve a `edge` cambiando
   un valor por defecto.

**Calendario:** el código se escribe la semana del 7 con `--motor edge` por
defecto —así no toca la producción y no gasta la ranura de cambio de esa semana,
que es de C19+C16—, y el valor por defecto cambia a `gemini` el lunes 14.

## C21.1 sube a urgente: dos vídeos de la semana que viene no renderizan

La barrera funcionó a la primera y encontró **dos defectos reales que nadie había
visto**: `MDS-013` (martes 9) y `MDS-015` (viernes 11). Con la barrera puesta,
esos dos días **no habría vídeo**.

Y hay un agujero de calendario que la barrera acaba de crear y que hay que
nombrar: **la nota va a `revisiones/`, que aplica la planificación del jueves 10
— después de que MDS-013 se produzca el martes.** El circuito normal de
propiedad de ficheros llega tarde cuando el defecto es de render y no de
contenido.

**Los dos son el mismo fallo de fondo, y no es «texto demasiado largo»:**

- `MDS-015`: `.cifra` con texto («10–16 millones de años»), 233 px de
  desbordamiento. Tercera vez que aparece este patrón.
- `MDS-013`: `.enunciado` con **dos palabras** («Ruta *panorámica*.»), 41 px de
  desbordamiento — porque con cinco palabras o menos la escalera sube la fuente a
  150 px. **La escalera actual mide número de palabras, y el que desborda es el
  ancho.** Una palabra larga a 150 px no cabe aunque sea la única.

**Así que C21.1 no es «añadir `.cifra` a la escalera»: es cambiar el criterio.**
En vez de elegir el tamaño por número de palabras, **se reduce el tamaño hasta
que quepa**: tras `cargar()`, mientras el elemento desborde y la fuente esté por
encima del suelo, se baja un 4 % y se vuelve a medir. Determinista, sin umbrales
que adivinar, y retira la familia entera de estos fallos de una vez.

- **Suelo: 64 px**, que es el mínimo legible de la regla de C2 para 1080×1920.
- Si al llegar al suelo sigue sin caber, **la barrera salta** — y entonces sí es
  un guion con demasiado texto, que es lo que la barrera debía cazar.
- El tamaño se fija una vez en `cargar()`, no por fotograma: mismo guion, mismo
  píxel.

**Y un segundo hallazgo que no arregla esto:** en MDS-015 el `pie` y el personaje
se solapan. Es de reparto vertical, no de tamaño de letra, y va aparte.

**Prioridad: es el encargo del lunes 7, por delante de todo.** Si por lo que sea
no está el lunes, la revisión diaria del lunes o del martes **aplica la excepción
de 48 horas sobre `MDS-013`** y corrige el guion, que es la red de seguridad.


---

# Versión 6 · 7 de septiembre de 2026 — la presentación, y la fecha en la que se decide

Todo lo anterior sigue vigente salvo lo que esta sección corrige expresamente.
Es la versión más larga porque contesta a las dos preguntas grandes que el codirector
puso hoy sobre la mesa: **qué hacemos con la presentación**, que es lo que él
señala como talón de Aquiles, y **hasta cuándo apostamos por el canal**.

## Los números con los que se escribe esto

MDH-005 (sábado 5) tiene **una visualización, la del codirector**. MDS-011 sale hoy
a las 19:00. Los tres Shorts con el motor C15 hicieron 31, 21 y 21 — la mejor
racha del canal— y siguen a menos de la mitad del umbral de S1.

La cifra de referencia del diagnóstico, y conviene tenerla delante todo el rato:
**un canal de menos de mil suscriptores saca entre 50 y 500 visualizaciones por
Short en las primeras 48 horas.** Nosotros sacamos entre 20 y 30. No estamos por
debajo de la excelencia: **estamos por debajo del suelo de lo normal.**

---

## Lo que se rompió hoy, y de dónde salía cada cosa

Tres defectos en MDS-011. Los tres son de arquitectura, ninguno es mala suerte.

### 1 · El guion bajo que se oye

La escena 5 traía `_pensamiento divergente_` dentro de **`narracion`**, y el
sintetizador dijo en voz alta «guion bajo pensamiento divergente guion bajo».

El marcado es real y es correcto: `*ámbar*` y `_cian_` los pinta `rico()` en
`escena.html`. **Lo que faltaba escrito en ninguna parte es dónde va.** Los dos
prompts de guionista explicaban qué pinta cada marca y no decían nunca que solo
valen en los campos que se ven; el guionista la aplicó al campo que no se ve, que
es el único que se oye.

**Y no es un problema de modelo.** La planificación ya corre con `claude-opus-5`,
que es el más caro del sistema: no hay ningún modelo mejor al que cambiar. Lo que
había era una instrucción incompleta y **ninguna comprobación**, que es el patrón
de siempre en este proyecto (trampa 7: no le pidas a un revisor que vea a ojo lo
que una condición booleana puede comprobar). Arreglado hoy en tres capas:

| Capa | Qué hace | Puede costar un vídeo |
|---|---|---|
| `voz.py` → `hablable()` | Quita el marcado justo antes de sintetizar. Arregla de paso el `.srt`, que sale del mismo texto | No |
| `validar_guion.py` | **Aviso**, con el nombre del campo y por qué | No |
| `guionista.md` y `guionista_corto.md` | La regla, con el caso y con la prueba: *léela en voz alta carácter a carácter* | — |

El aviso es aviso y no error **a propósito**: con `voz.py` saneando, el defecto ya
no puede llegar al público, y parar una producción por algo que el pipeline
arregla solo cambia un vídeo con un fallo por un día sin vídeo, que es peor.
Barrido sobre los 27 guiones del repositorio: **un solo positivo, MDS-011, y
ningún falso positivo.**

### 2 · La cara triste encima del texto — dos defectos, no uno

El **solape** ya estaba arreglado: es el encargo nº 2 que la revisión del domingo
resolvió con `padding-bottom:720px`. No llegó a este vídeo por una razón de reloj
que hay que dejar escrita, porque va a repetirse (ver la trampa 11, abajo).

Lo que **no** estaba arreglado es la cara. La regla 14.3 decía que `duda` y
`no_le_hace_gracia` se leen como cara triste. **`no_le_hace_gracia` no existe** —
las seis expresiones son `neutra`, `duda`, `entiende`, `no`, `rie`, `piensa`— y
la que se usó, `piensa`, **comparte la boca torcida con `duda`** (`.b-torcida` en
`escena.html`). La regla nombraba una cara inventada y dejaba fuera una real.

Corregido hoy en `REGLAS.md`: **tres de las seis expresiones se leen como cara
triste a tamaño de móvil**, y no van en escenas que solo presentan.

**Y la conclusión que importa no es normativa, es de dibujo.** Que la mitad del
vocabulario del personaje lea igual no se arregla vigilando qué guion usa cuál:
se arregla **redibujando `piensa`** para que sea pensativo y no cabizbajo. Va
como P8, abajo. Comprobado sobre los cinco guiones pendientes, un comprobador
automático de esto daría cuatro falsos positivos de cinco: **este no es un caso
para una comprobación determinista, y decirlo también es una decisión.**

### 3 · La voz sigue siendo la de siempre, y eso es culpa mía

El codirector esperaba oír Gemini hoy. **No tocaba hoy: C7.2 dice el lunes 14**, y el
código ni siquiera está escrito — se escribe esta semana con `--motor edge` por
defecto. Está en la versión 5.1 y en la tabla del prompt de arranque, pero
escrito para quien lee el plan entero, no para quien escucha el vídeo del lunes.

**Lo que se cambia:** cuando una decisión signifique *«esto que te molesta lo vas
a seguir viendo N días»*, se dice con esas palabras y con la fecha, en la línea de
`ESTADO.md` o en el resumen del lunes. No basta con que esté en el plan.

### Y el defecto de fondo que los tres comparten

MDS-011 pasó por el guionista, el chistólogo, el verificador, `validar_guion.py`,
la barrera de C21 y la revisión diaria del domingo. **Seis filtros y salió con
tres defectos.** Ninguno de los seis miraba lo que falló: el marcado en un campo
que no se pinta, una cara que la regla no nombraba, y una fecha que solo estaba
en un documento.

---

## C25 · La presentación

**El encargo del codirector, con sus palabras:** «hay mucha diferencia aún entre la
presentación de nuestros vídeos y la presentación de los vídeos de los canales
más exitosos; creo firmemente que nuestro talón de Aquiles es la presentación
ahora mismo, muy por debajo del contenido».

Estoy de acuerdo, y se puede decir con más precisión que «se ve peor».

### Las siete diferencias, nombradas

1. **Todo es texto.** 72 % de las escenas de los diez primeros Shorts es texto
   centrado sobre fondo, y **los ocho iconos de `02_marca/iconos.svg` no se han
   usado ni una sola vez en once Shorts.** Texto blanco sobre fondo oscuro con
   voz sintética es, en 2026, la firma reconocible del vídeo automatizado.
2. **La pantalla no tiene profundidad.** Un plano. Todo lo que se ve está a la
   misma distancia. Los canales de referencia tienen siempre dos o tres capas.
3. **Cada escena empieza de cero.** Se monta y se desmonta entera. No sobrevive
   nada al corte — y eso es exactamente lo que el codirector describió como «un corte
   despiezado del vídeo largo». Seis tarjetas seguidas no son una historia
   aunque el guion lo sea.
4. **La composición no cambia nunca.** Todo centrado, siempre. Cinco Shorts a la
   semana con el mismo encuadre son, para quien pasa por el feed, el mismo vídeo
   cinco veces.
5. **Nada se construye.** El texto aparece; no se dibuja, ni se cuenta, ni crece.
   La regla F3 del diagnóstico pide que algo cambie cada 3–5 s; nosotros solo
   cambiamos en los cortes de escena.
6. **El personaje no actúa.** Respira y cambia de cara. No entra, no señala, no
   se aparta. F4 dice que un personaje recurrente es lo que separa «canal sin
   cara» de «basura generada» — pero un personaje que no hace nada no lo es.
7. **No hay diseño de sonido.** Una cama de música y una voz. En formato corto,
   el acento sonoro en el corte es la mitad de la calidad percibida, y no
   tenemos ninguno.

### Las diez propuestas, y lo que cuesta cada una

Todas son deterministas, todas caben en el plan gratuito y ninguna necesita
material de terceros salvo P9, que necesita una descarga puntual.

| | Qué | Dónde | Coste de render | Qué compra |
|---|---|---|---|---|
| **P1** | **Profundidad.** Tres capas: plano de fondo con rejilla de taller al 4 %, plano de contenido, viñeta delante. El fondo deriva un 1,5 % **en contra** de la entrada del texto: paralaje | `escena.html` (CSS) | **Cero** | Que un fotograma deje de leerse como una diapositiva. Y la rejilla de taller *es* la marca: el canal se llama Mecánica |
| **P2** | **Continuidad.** El término en cian de cada escena no desaparece: encoge y se acopla a una pila en el borde superior, que crece con el vídeo. Al final, la pila **es** el resumen | `escena.html` + `render.py` | Cero | Convierte seis tarjetas en una pieza. Es el antídoto directo del «parece un recorte» |
| **P3** | **Los iconos existen (C16).** Los ocho de `iconos.svg`, y **dibujándose solos** con `stroke-dasharray` en ~0,6 s | campo `icono` + `escena.html` | Bajo | Una línea que se dibuja sola es la señal más barata de «esto lo ha hecho alguien» |
| **P4** | **La escena 1 no es una frase (C19).** Icono dibujándose + **cuatro palabras o menos** + el personaje entrando | guionista + `escena.html` | Bajo | El peldaño S1 entero depende del primer segundo |
| **P5** | **La cifra se construye.** El número cuenta desde cero en 0,5 s; el arco o la barra crecen hasta su valor | `escena.html` | Cero | F3 justo en la escena donde hoy hay una tarjeta quieta |
| **P6** | **Tres tamaños, no uno.** Antetítulo pequeño · palabra enorme · pie pequeño. Hoy hay un solo bloque centrado | `escena.html` (CSS) | Cero | Es lo que separa «maquetado» de «diseñado», y es gratis |
| **P7** | **Cada serie con su cara (C24).** Cinco composiciones de partida y un color de apoyo dentro de la paleta | `escena.html` | Cero | Que cinco Shorts a la semana no sean el mismo vídeo cinco veces |
| **P8** | **El personaje actúa,** y **se redibuja `piensa`.** Entra por el borde la primera vez, se inclina hacia la cifra, se aparta en el «dónde falla» | `personaje.svg` + `escena.html` | Cero | F4. Y quita de raíz el problema de las tres caras tristes |
| **P9** | **El corte suena.** Tres acentos CC0: clic en el corte, golpe grave en el remate, tic ascendente en la cifra | `montaje.py` | Cero | Lo que más sube la calidad percibida por byte en formato corto |
| **P10** | **El Short cuenta una historia.** `validar_guion.py` comprueba que la secuencia de tipos de escena **encaja con la estructura declarada de su serie** | `validar_guion.py` | — | MDS-011 es «El experimento» y no sigue la forma de «El experimento». Esto sí es determinista y fiable |

**Lo que se descarta, y por qué:** imágenes de banco (regla 9 y no son de marca),
imágenes generadas por IA (coste, y el canal declara IA en la voz, no en el
dibujo), vídeo de archivo (regla 9), y subir el número de capturas por segundo
(no es el problema: el problema es que no hay nada que capturar).

### El orden, y la regla que se relaja para poder hacerlo

**La regla 11.1 —un cambio por producción— se suspende hasta el punto de control
del 27 de septiembre, y solo para los cambios de presentación.**

El motivo no es la prisa, es aritmético: con veinte visualizaciones por vídeo,
**ningún cambio se puede atribuir midiendo.** La diferencia entre 21 y 31 son
diez personas. La regla se escribió para un canal con señal y la estamos pagando
—una mejora por semana— sin recibir a cambio lo único que compra, que es saber
cuál fue. Lo que **no** se relaja es lo que sí protege de verdad: la regla 11.2
(se mira el muestrario, no se imagina), la 11.5 (determinista) y la barrera de
C21. Y **los arreglos de defecto nunca han consumido la ranura**: eso queda
escrito, porque hoy se ha discutido.

**Vuelve a estar en vigor** el día que un Short pase de 100 visualizaciones en
48 horas. Ese día hay señal que atribuir y la disciplina empieza a pagar.

| Semana | Presentación | Voz | Lo demás |
|---|---|---|---|
| **7 sep** | **P3 + P4 + P6** (los iconos, la escena 1, la jerarquía) y **P10** | código de C7 con `--motor edge` | Los tres arreglos de hoy |
| **14 sep** | **P1 + P8** (profundidad, el personaje actúa y `piensa` redibujado) | **C7 se enciende**: Gemini en los Shorts | |
| **21 sep** | **P2 + P7 + P5** (continuidad, serie, la cifra que se construye) | | **P9** si el codirector ha dejado los sonidos |
| **27 sep** | **Punto de control.** Se mide un canal con la presentación entera puesta | | |

**Si algo se cae, se cae por este orden, empezando por el final:** P5, P2, P7,
P1. **P3, P4, P6 y P8 no se caen**: son los cuatro que atacan el primer segundo y
la sensación de plantilla, que es lo que estamos midiendo.

### Lo único que necesito del codirector, y es una vez

**Tres ficheros de sonido CC0** (`.wav` o `.mp3` cortos, menos de 1 s): un clic
seco de corte, un golpe grave, y un tic ascendente. En
`03_produccion/sonidos/`, con su atribución en `creditos.json` como la música.
Freesound con filtro CC0, o el paquete de interfaz de Kenney, valen. **Lo pido
porque los contenedores no llegan a esos sitios** — es el mismo bloqueo de red
que tiene parada la ampliación de música de C18. Sin prisa: hace falta para la
semana del 21.

---

## C26 · Hasta cuándo apostamos por el canal

**La pregunta del codirector:** «no quiero abandonar antes de tiempo; tampoco
mantener más tiempo del debido un proyecto fallido. Por eso busco un momento
clave en el que poder revisar y decidir juntos».

Es la pregunta correcta y hasta hoy solo estaba medio contestada: había un punto
de control intermedio (27 de septiembre) y una frase, «doce semanas», sin fecha
ni criterio. Esto lo cierra.

### La fecha: domingo 15 de noviembre de 2026

Doce semanas desde el primer Short (24 de agosto), trece desde el cambio de rumbo
(20 de agosto). Diez semanas desde hoy. Para entonces el canal habrá publicado
**unos noventa vídeos**, y **todo lo que está escrito en este plan estará puesto**:
C19, C16, C7, C21, C24 y las diez propuestas de C25. Es decir: se juzgará el
canal que queríamos hacer, no el que teníamos.

Antes está el **27 de septiembre**, que sigue siendo lo que era: un control
intermedio con tres desenlaces, no un indulto ni una sentencia.

### El criterio, escrito hoy y no aquel día

Se mira **la mediana de visualizaciones a las 48 horas de los últimos veinte
Shorts**. Veinte porque son cuatro semanas y aguanta un vídeo con suerte sin
mentir; la mediana y no la media por lo mismo.

| Si el 15 de noviembre… | Entonces |
|---|---|
| mediana **≥ 150**, o **≥ 100 suscriptores**, o algún Short por encima de **1.000** | **Se sigue.** El canal ha arrancado y la conversación pasa a ser de escala |
| mediana entre **50 y 150** | **La máquina funciona y el nicho es pequeño.** Se amplía el tema al humor dentro de las habilidades sociales y la conversación —donde Charisma on Command demuestra que hay siete millones de personas— sin renunciar al método ni a las fuentes. **Una prórroga de ocho semanas, hasta el 10 de enero, y solo una** |
| mediana **< 50** | **Se para.** |

**Por qué 50 es la línea de abajo, y no un número elegido para poder aprobar.**
50 es el **suelo** del rango que el diagnóstico documenta para un canal
desconocido de menos de mil suscriptores: entre 50 y 500 por Short en 48 horas.
Estar por debajo de 50 después de doce semanas, noventa vídeos y todos los
cambios aplicados no significa «vamos despacio»: significa que **YouTube no nos
está repartiendo ni lo que reparte por defecto**, y contra eso no queda ninguna
palanca de ejecución que no hayamos usado ya.

### Qué significa «se para», dicho sin eufemismos

No es borrar nada ni fingir que no ha pasado. Es: **se deja de publicar**, los
vídeos se quedan donde están, y **el pipeline se apunta a otra cosa**. Porque lo
que se ha construido aquí —cola, render determinista, barrera de calidad,
publicación automática, tres agentes con propiedad de ficheros, un token que ya
no caduca— **no es del tema del humor. Es de cualquier tema.** Parar el canal no
tira ese trabajo; lo libera.

### Las dos cláusulas que hacen que esto sea honesto

1. **Los umbrales se pueden cambiar, pero solo antes de que lleguen los datos.**
   Si el 15 de noviembre nos parece que la línea estaba mal puesta, eso no es una
   decisión: es una excusa. Cualquier cambio de esta tabla se discute y se
   escribe **antes** del 8 de noviembre.
2. **La prórroga es una y no se encadena.** Si el 10 de enero, con el tema ya
   ampliado, la mediana sigue por debajo de 150, se para. Sin tercera lectura.

### Lo que hace falta para poder decidir así

`04_agentes/metricas.py` **no calcula ninguna mediana hoy**. A partir del lunes
que viene tiene que escribir en `metricas.json`, cada lunes, tres cifras: la
mediana de los últimos veinte Shorts a las 48 horas, cuántos han pasado de 100 y
cuántos de 50. Encargo para la revisión diaria; sube de «prioridad baja» a
**«hace falta antes del 27 de septiembre»**, porque sin ese número el punto de
control se discute de memoria.

---

## Lo que NO cambia hoy

- **La cadencia.** Cinco Shorts y un largo. Se revisa el 27, como estaba escrito.
- **No se amplía el tema todavía.** Sigue valiendo el motivo del 4 de septiembre,
  y ahora con fecha: se amplía el 15 de noviembre si la mediana cae en la banda
  de en medio, no antes.
- **El episodio largo se queda en `edge-tts`.** Cuarenta escenas no caben en diez
  peticiones diarias. Sin novedad.
- **C10, C20 y C13 siguen detrás de S1.**


---

# Versión 6.1 · 7 de septiembre, mediodía — lo que salió al aplicar la versión 6

Cinco cosas, cuatro de ellas descubiertas al arreglar los defectos de MDS-011.
La versión 6 sigue vigente entera; esto la corrige donde hizo falta.

## Lo que se aprendió arreglando el solape: medir una escena quieta miente

El arreglo del domingo (`padding-bottom:720px`) se verificó **en el punto de
reposo** de la escena, donde el hueco entre el pie y la cara medía 48 px, y se
dio por cerrado. Con la escena **en movimiento** ese hueco baja a **7 px**, y
así se publicó.

Medido punto por punto, 21 instantes por escena, sobre las 49 escenas verticales
con personaje del repositorio. Los 41 px se los comen tres cosas que **no
existen en un fotograma quieto**:

| | Cuánto |
|---|---|
| El personaje entra 26 px por debajo de su sitio y sube | 26 px |
| Y respira, ±5 px, todo el rato | 5 px |
| `#escena` crece un 2,2 % durante la escena (el zoom de C15) y empuja el borde inferior de `.caja` | ~20 px |

**El número nuevo es 790 px** y no está elegido a ojo: 430 (`bottom` del
personaje) + 250 (su alto) + 5 (respiración) + 40 (el aire que ya se quería) +
65 (lo que empuja el zoom, medido). El peor caso del repositorio pasa de **−34 px
a +2 px**, y MDS-011 escena 4 de 7 px a **43 px**. Todos los guiones pendientes
quedan por encima de 108 px.

**Lo que queda abierto, dicho para que no se olvide:** ese peor caso de +2 px es
`MDS-007` escena 4 —una `lista` de tres puntos con personaje, ya publicada—.
**Subir más el `padding` no vale:** ahí el borde superior de `.caja` ya baja a
158 px y por encima de 150 px empieza la banda que tapa la interfaz de YouTube.
El arreglo bueno es el principio de C21.1 aplicado al alto —*encoge hasta que
quepa*, pero midiendo la banda reservada y no solo la caja— y está encargado.

→ **Trampa 15:** *cuando compruebes geometría en `escena.html`, llama a
`pintar(t)` en al menos veinte instantes de la escena y quédate con el peor caso.
Comprobar solo después de `cargar()` es comprobar un vídeo que no existe.*

## P8 se adelanta a medias: `piensa` ya no es una mueca

La cara `piensa` compartía la boca de `duda` —`b-torcida`, que a tamaño de móvil
se lee como una comisura caída—, y por eso MDS-011 presentó un experimento con
cara triste. Se ha redibujado hoy: **boca recta y las dos cejas levantadas**. El
«estoy pensando» lo cuentan ahora las cejas y el eje del engranaje girando 24°,
que además es lo de marca.

**Y con eso la regla 14.3 se encoge de tres caras a dos.** Esta mañana se amplió
para prohibir `duda`, `piensa` y `no` en escenas que solo presentan. Al mirar el
dibujo se vio la corrección de verdad, y queda escrita en `REGLAS.md`:

> **Cuando una regla tenga que prohibir la mitad de una paleta, sospecha de la
> paleta antes que de quien la usa.**

Lo que sigue pendiente de P8 es lo otro: que el personaje **haga** algo —entrar
por el borde, inclinarse hacia la cifra, apartarse en el «dónde falla»—. Baja
detrás de la caché de voz.

## C27 · El episodio largo también deja `edge-tts`

**La propuesta es del codirector, y es la buena.** Textualmente: «¿y si se
renderizan varias escenas al día y luego el último día se juntan en el vídeo
largo? El resultado de edge-tts no es bueno y no debe haber esa diferencia entre
los shorts y los largos (si no, dejamos de hacer largos)».

**De acuerdo con el diagnóstico y con la amenaza.** Un canal que publica cinco
piezas con una voz y una sexta con otra peor no tiene dos productos: tiene un
producto y un recordatorio semanal de que se puede hacer mejor. Y la conclusión
del 4 de septiembre —«el largo se queda en `edge-tts`, o nunca»— se tomó dando
por hecho que la cuota se gastaba el mismo día del render. **No tiene por qué.**

**La aritmética, que es lo que decide:**

| | |
|---|---|
| Escenas de un episodio largo | ~40 |
| Peticiones por día del nivel gratuito, **por modelo** | 10 |
| Modelos con cuota propia | `gemini-3.1-flash-tts-preview` y `gemini-2.5-flash-preview-tts` |
| Días entre que la planificación escribe el guion (jueves) y se produce (sábado) | 8 (de martes a sábado, dos semanas de margen real) |

Cuarenta escenas no caben en un día. **Sí caben en cuatro**, y sobra.

**Cómo se hace, y la pieza de la que depende todo es la caché:**

1. **`voz.py` gana una caché indexada por contenido**, en
   `03_produccion/cache_voz/<sha256 de narración + motor + voz>.mp3`. Antes de
   pedirle nada a Gemini, mira si ya está. Es la pieza central y entra **esta
   semana**, con C7. Beneficio inmediato y aparte: **repetir una producción deja
   de gastar cuota** — hoy hubo que rehacer MDS-011 a mano y se pagó dos veces.
   Y como la clave incluye el texto, un guion corregido se resintetiza solo en
   las escenas que cambiaron.
2. **Un workflow nuevo, `voz_adelantada.yml`**, de martes a viernes: coge el
   guion del sábado siguiente, mira qué escenas no están en caché y sintetiza
   **hasta agotar el margen del día**, con 25 s entre llamadas.
3. **Usa el modelo 2.5 y no el 3.1**, para no competir con la cuota que gastan
   los Shorts del día. Si el 2.5 se agota, para y lo retoma mañana; no hay prisa.
4. **El sábado no cambia nada.** `voz.py` encuentra el 90 % hecho y lo que falte
   lo sintetiza con `edge-tts`, como siempre. **Un mal día no deja al canal sin
   vídeo: deja alguna escena con voz peor**, y `ficha.json` dice cuáles. Es la
   misma política de degradación que el resto del proyecto.

**Cuándo:** la caché, esta semana con C7. El workflow, la semana del 14 — el
diseño lo prepara la revisión diaria y lo deja en `07_pruebas/`, porque
`.github/workflows/` no se escribe en remoto y lo crea el codirector a mano.

**Y la parte incómoda de su frase, que no se esquiva:** «si no, dejamos de hacer
largos». Queda como opción viva para el 27 de septiembre. El episodio largo
cuesta cuarenta escenas de guion y de render para **una visualización**; si
C27 no lo iguala en calidad al Short, la pregunta no es cómo mejorarlo sino si
merece la semana. No se decide hoy: se decide con la tabla delante.

## C23 · La verificación de Google: hay que dejar de perseguirla

**El diagnóstico, con lo que se ve en la consola:**

- **«Verificación de la propiedad» → «Propietario verificado» con su marca
  verde. Eso está HECHO** y era lo único que necesitaba la web de `docs/`.
- **«No hemos encontrado ninguna página de Accelerated Mobile Pages en tu sitio
  web» es de Search Console, no de OAuth.** AMP es un formato de página móvil,
  no tener ninguna es lo normal y no bloquea nada. **No tiene nada que ver.**
- **«Estado de verificación» es la verificación de MARCA, y es un trámite
  distinto que no necesitamos** — y el botón «Corregí los problemas» **manda la
  aplicación a revisión**, que es exactamente lo que no queremos y lo que va a
  seguir fallando cada vez que se pulse.

**Lo que dice la versión 5 sigue siendo cierto palabra por palabra:** *publicar
no es verificar*. Publicar es **un botón** en *Audiencia* → **«Publicar
aplicación»**, y con eso el token deja de caducar a los siete días. Verificar es
un formulario con revisión humana, y solo hace falta para pasar de 100 usuarios
o para quitar la pantalla de aviso. Necesitamos un usuario.

**La acción, y es corta:** *Audiencia* → **Publicar aplicación** → aceptar que la
verificación queda pendiente. Nada más. Si el botón sale desactivado, lo que hay
que completar son **campos de la pantalla de consentimiento** (nombre de la
aplicación, correo de asistencia, datos de contacto del desarrollador), no pasar
ninguna revisión.

## Y el token, que resultó ser otro problema distinto del que creíamos

La lectura de métricas del lunes falló con **`invalid_scope: Bad Request`**, no
con un token caducado. Causa: **el token vigente se generó sin
`yt-analytics.readonly`**. En la pantalla de consentimiento cada permiso es una
casilla y es fácil dejarse una; el token resultante **sube vídeos perfectamente**
—`publicar.py` solo pide `youtube.upload` y `force-ssl`— y mata las métricas una
semana después, en otro sitio y con un error que no nombra el ámbito que falta.

Arreglado en las dos direcciones:

- **`obtener_token_youtube.py` ya no imprime un token incompleto: lo rechaza**,
  diciendo qué casilla faltó. Antes lo listaba y se quedaba tan ancho.
- **`metricas.py` ya no manda `scopes` al refrescar** —que es lo que provoca el
  `invalid_scope`— y comprueba los ámbitos por su cuenta. Si falta el de
  analítica, **hace igualmente la parte de Data API** (que es la que corrige
  `registro_publicaciones.json`) y lo dice en castellano.

→ **Trampa 16:** *un permiso que falta no rompe donde se concede: rompe donde se
usa, y eso puede ser una semana después. Cuando emitas una credencial, compara
lo concedido con lo pedido y falla ahí mismo.*

## El nombre del codirector sale del repositorio

Decisión suya, del 7 de septiembre. **Retirado de los 58 ficheros donde
aparecía** (271 menciones): documentos, comentarios de código, prompts de los
tres agentes y sus tres copias del almacén. En adelante se le llama **«el
codirector»** o **«la dirección»**, y es regla escrita en los tres prompts.

**Lo que esto NO hace, y conviene saberlo:** el nombre sigue en el **historial de
git**, en los commits anteriores a hoy. Quitarlo de ahí exige reescribir la
historia (`git filter-repo` y un `push --force`), que es una operación aparte y
con sus riesgos. **Queda a decisión del codirector**; mientras tanto, lo que ve
quien entra hoy al repositorio ya no lo lleva.

**Tres ficheros no se han tocado a propósito** —`revision-19-08.patch`,
`Claude outputs/voz_prueba.yml` y `Claude outputs/portada-web.png`—: son restos
de sesiones antiguas que no pinta nada que estén en el repositorio. **Lo suyo es
borrarlos, no reescribirlos.**

## P9 · Los sonidos ya están, y hacen falta dos cosas

Los tres acentos CC0 están en `03_produccion/sonidos/` con su
`attribution_texts.md`. Dos avisos:

1. **`montaje.py` sigue protegido.** La autorización del 28/08 cubría **solo** el
   manifiesto de subtítulos, y montar los sonidos es otra cosa. **Hace falta una
   autorización nueva y escrita** para que la revisión diaria pueda tocarlo. Sin
   ella, P9 no entra: la regla 11.7 no se salta «solo por esta vez».
2. **`attribution_texts.md` trae cuatro créditos y en la carpeta hay tres
   ficheros** (falta el de `alec_mackay`). Se acredita lo que exista.


---

# Versión 7 · 12 de septiembre de 2026 — el guion se cose, y las comprobaciones miran donde toca

Todo lo anterior sigue vigente salvo lo que esta sección corrige expresamente. Es la
sesión de dirección del sábado, desplazada desde el viernes 11 por cuota y por tiempo.

**Los números no se han movido y son el marco de todo lo que sigue.** Seguimos por debajo
de 100 visualizaciones por vídeo, que es el umbral que el codirector puso como condición de
supervivencia del canal. Nada de lo que hay aquí cambia eso por sí solo: son arreglos de
proceso, y el proceso es lo único sobre lo que podemos actuar de una semana para otra.

---

## Lo que une los cuatro fallos de esta semana

Cuatro cosas distintas llegaron al público entre el 9 y el 12 de septiembre: un Short sin
hilo, una referencia huérfana, un episodio largo sin gracia y un texto fuera de su caja. Y
una quinta se quedó a medias: la planificación del jueves.

**Los cinco tienen la misma forma.** En los cinco casos había una regla escrita, la regla se
cumplió, y el resultado falló igualmente:

| Lo que pasó | La regla que había | Por qué no sirvió |
|---|---|---|
| MDS-013 «parece un recorte de un recorte» | tener chiste, mecanismo y «dónde falla» | los tres estaban, y eran de cuatro asuntos distintos |
| MDS-014, el «martes» huérfano | la pantalla no introduce un dato que la voz no diga | el dato estaba en las dos, con dos palabras distintas |
| MDH-006, «el chiste no entra» | mínimo dos risas, una antes del segundo 15 | dos exactas, las dos en los primeros veinte segundos |
| MDH-006 2:34, texto fuera de su caja | la barrera de C21, con `svg text` en su lista | de un `<text>` de SVG solo medía el lienzo, nunca su caja |
| La planificación del 10/09, a medias | «trabaja sin nadie delante» | y el prompt le mandaba llamar a una herramienta que pide permiso |

**Una lista de ingredientes se puede cumplir entera y que el plato no ligue.** Eso es lo
que hay que corregir, y por eso esta versión no añade comprobaciones nuevas encima de las
que hay: **cambia qué miden las que ya existían.**

---

## El guionista · los dos prompts, reescritos

Es lo que el codirector puso como más urgente, con tres avisos en cuatro días. Aquí está lo
que cambia y por qué, que es lo que pidió entender.

### El diagnóstico, guion a guion

**MDS-013 (9/09) — «inconexo, cortado, difícil de seguir. Parece un recorte de un recorte,
sin hilo conductor, sin una historia narrada, sin un principio y un final.»**

Seis escenas y **cuatro asuntos**: «el navegador» (escenas 1-2), «las dos piezas» (3), «la
bisagra» (4), «el blanco es un grupo entero» (5) y la teoría de la norma prejuiciosa (6). El
ejemplo concreto entra en el segundo cero, desaparece durante cuatro escenas y reaparece en
las últimas seis palabras del vídeo. Y las dos ideas nuevas —el grupo, la teoría— entran en
los segundos 32 y 36 de un vídeo de 52.

No es que no tenga principio y final: es que **tiene cuatro principios**. El ejemplo no era
el hilo, era el marco, y desde dentro eso se ve como dos vídeos pegados.

**MDS-014 (10/09) — el «martes» que no se explica.**

Escena 2, voz: «lo repetí **el domingo**». Escena 4, pantalla: «lo jovial que estabas **el
martes**», voz: «lo jovial que estás **hoy**». Título de trabajo: «qué miden de tu
**martes**». Tres días para una idea, y ninguno explicado.

La regla 14.1 no lo cazaba porque el dato sí estaba en las dos mitades: lo que cambiaba era
**la palabra**. Y `validar_guion.py` no lo cazaba por un motivo peor, que conviene decir:
**la red determinista de C22 —el encargo 3, «señala las palabras de pantalla que no estén en
la narración de su escena»— nunca llegó a escribirse.** Está dada por entregada en la cola
desde el 10/09 y en el código no hay nada. Ver C28, abajo, donde se cierra con el motivo.

**MDH-006 (12/09) — «el contenido está bien, incluso mejor que otras veces, y se aprende
algo. Ese es el camino. Pero el chiste no entra.»**

Este es el más interesante porque la mitad del comentario es un elogio, y el elogio va sobre
lo que más cuesta. El problema es de reparto:

- Risa 1: «se rieron dos. Uno era yo» — segundo ~8.
- Risa 2: «la reunión de marzo. Que todavía se comenta» — segundo ~18.
- Y después, **hasta el minuto cinco, nada**.
- Callback final: «y los diez de mi reunión, por cierto, siguen calculando» — que remite a
  una premisa de hace cuatro minutos y medio **y además pide una resta**: doce menos dos.

`notas_humor` lo enseña a simple vista: cuatro entradas, tres de ellas en los primeros
veinte segundos. **El vídeo cumple la regla y deja de tener gracia en el segundo veinte.**

### Lo que cambia en `guionista_corto.md`

Tres pruebas nuevas, y van **delante de todo lo demás** en el documento porque son lo que
falló y porque se pasan **antes** de escribir la primera escena.

**Prueba 1 · El hilo: un solo sujeto, y vuelve.** Antes de nada, tres frases en
`notas_humor` —qué pasa, qué gira, cómo acaba— **nombrando el mismo sujeto concreto**. Si no
se pueden escribir sin cambiar de sujeto, el Short no está escrito todavía. Y en el guion: el
ejemplo de la escena 1 **vuelve por su nombre en una escena del medio**, no solo en el
cierre; y un Short nombra **dos cosas como mucho**, el ejemplo y el mecanismo.
*Cómo se comprueba:* poner las `narracion` en una columna y leer de una a la siguiente. Si
para entender la escena N hace falta una palabra que no está en la N-1, ahí no hay hilo.

**Prueba 2 · Nada nuevo después de la mitad.** Las dos últimas escenas **solo resuelven**.
Una idea que aparece por primera vez en la escena 5 o 6 no es un final: es otro Short. Si al
llegar al cierre hace falta introducir algo, el Short que se estaba escribiendo era otro.

**Prueba 3 · El detalle concreto se dice con la misma palabra.** Es C28, abajo, y sube
también a `REGLAS.md` como regla 14.4.

Y una lista de comprobación de seis líneas al final, para releer contra el guion terminado.

### Lo que cambia en `guionista.md`

**La regla de la risa deja de contar y pasa a medir distancias.** Es el cambio de fondo:

- **Nunca más de noventa segundos sin algo construido para hacer reír.** En un episodio de
  cinco minutos son cuatro o cinco, no dos. Y no hace falta que sean chistes con remate.
- **La primera sigue antes del segundo quince.**
- **Un callback a más de noventa segundos vuelve a decir su premisa en la misma frase.**
  Cuesta seis palabras y es la diferencia entre un remate y una referencia perdida. Es la
  regla de «el audio se basta solo» aplicada al eje del tiempo en vez de al eje
  pantalla/voz.
- **Un chiste no le pide aritmética al espectador.**
- Y el gancho **es también el sujeto del episodio**: si abre con una reunión de doce
  personas, esa reunión vuelve en el cuerpo, no solo al final.

**Por qué noventa segundos y no otro número.** La estructura ya reparte el cuerpo en dos o
tres bloques de *fenómeno → evidencia → técnica*; noventa segundos pone una risa en cada
bloque, que son las costuras que ya existen. Con el gancho y el cierre salen cinco. Y no se
confunde con el «giro cada 40 segundos» que ya estaba escrito: **un giro no es una risa**, y
tenerlos separados evita que el guionista cuente los giros y se quede tranquilo.

**Y un apartado nuevo sobre el `diagrama` horizontal**, que sale del fallo del 2:34: con tres
pasos cada caja mide 533 px y la letra va a 46 px, donde caben cinco o seis palabras cortas.
**Un paso de diagrama es una etiqueta, no una frase**; el matiz va en su `pie`, que va a 32 px
y aguanta más. Con cuatro pasos caben tres o cuatro palabras; con cinco, dos. *Si el paso no
cabe en cuatro palabras, el diagrama tiene un paso de más.*

### Lo que NO cambia, y es deliberado

Las cinco series, el chiste primero y la prueba del WhatsApp, el máximo de tres `enunciado`,
C19 y el campo `icono`, el ámbito del resaltado, el cierre que dice dónde falla, y la
prohibición de humor y atracción en Short. **Nada de eso ha fallado esta semana.** Lo que
falló fue que se podían cumplir todos y entregar un guion que no se sostiene.

---

## C28 · El detalle concreto, y el cierre honesto de C22

**Regla:** un día de la semana, un mes, un lugar o un nombre propio que aparezca en pantalla
se dice **con esa misma palabra** en la narración de esa misma escena, y no se adelanta en la
anterior. Sube a `REGLAS.md` como **regla 14.4**.

**Red determinista, en `validar_guion.py`, y es ERROR.** No aviso: a diferencia del marcado
en la narración —que `voz.py` sanea solo— aquí no hay nada aguas abajo que lo arregle. Si
llega al render, llega al público.

**Medido antes de escribirlo, contra los 302 guiones del repositorio:**

| Variante | Escenas señaladas | Veredicto |
|---|---|---|
| **C22 tal y como se especificó** — toda palabra de contenido de cuatro letras o más, comparada por raíz de 5 | **222 de 302 · 73,5 %** | Ruido. No es una comprobación |
| Días, meses **y cifras** | 44 de 302 · 14,6 % | Cinco falsos positivos de números («50 años» / «cincuenta años», «2003» / «dos mil tres») y ningún acierto en esa rama |
| **Días y meses solos** — lo que entra | **3 de 302 · 1,0 %** | Las tres reales. Cero falsos positivos |

Las tres que señala: **MDS-014 escena 4** («martes», el caso del codirector), **MDH-006
escena 3** («marzo» en pantalla una escena antes de que la voz lo diga) y **MDH-003 escena
19** («el lunes» como idiotismo que nadie pronuncia). Las tres están ya publicadas, así que
la regla no bloquea nada pendiente: **los seis guiones de la semana del 14 pasan limpios.**

**Y con esto se cierra C22, el encargo 3, que llevaba desde el 4 de septiembre sin escribirse
y dado por entregado en la cola desde el 10.** No se escribió porque **no se puede escribir
como estaba especificada**: señala tres de cada cuatro escenas. Decirlo es mejor que dejarlo
abierto para siempre. La versión estrecha hace el trabajo que importa.

→ **Y la lección, que es la de siempre aquí:** una comprobación tonta y estrecha que acierta
siempre vale más que una lista que señala tres de cada cuatro escenas. La segunda se acaba
ignorando, y entonces no protege de nada.

---

## C29 · La barrera no sabía mirar dentro del SVG

**El aviso del codirector:** *«en el vídeo largo publicado hoy, en el segundo 2:34, la frase
"Espera a que lo abra el otro" no cabe en su rectángulo y sobresale. Pasó todas las
revisiones y llegó hasta la publicación. No es grave, pero significa que no estamos siendo
pulcros.»*

Tiene razón en las dos mitades, y la segunda importa más que la primera.

### Por qué pasó, medido

`MDH-006` escena 22, `tipo: diagrama`, formato largo. La rama horizontal de `escena.html`
dibuja las cajas encadenadas dentro de un `<svg>` de 1920 px: con tres pasos, cada `<rect>`
mide **533 px** y el `<text>` del título va a **46 px**.

Medido con el motor real y la fuente real (Inter):

| Texto | Ancho | Caja | |
|---|---|---|---|
| «No lo abras tú» | 308 px | 533 px | holgura 225 px |
| **«Espera a que lo abra el otro»** | **604 px** | **533 px** | **se sale 70 px — 35 por cada lado** |
| «Y solo con esa persona» | 520 px | 533 px | holgura **13 px** |

El tercero es casi tan preocupante como el segundo: **13 px de margen es una palabra de
distancia del mismo fallo.**

### Y por qué la barrera de C21 dio el visto bueno

`comprobarDesbordes()` **llevaba `"svg text"` en su lista de selectores desde el 4 de
septiembre.** Parecía cubierto. No lo estaba:

```js
if (!soloLienzo && el instanceof HTMLElement){
    desbordaAncho = el.scrollWidth > el.clientWidth + TOL_ANCHO;
    ...
}
```

Un `<text>` de SVG **no es un `HTMLElement`** y no tiene `scrollWidth`: no desborda su caja,
la pinta encima. Así que de esos elementos solo se evaluaba el rectángulo **contra el
lienzo** — es decir, se detectaba que un texto se saliera de la *pantalla*, nunca que se
saliera de *su caja*. Y las cajas del diagrama están en el centro de la pantalla. **La única
situación que la barrera podía cazar ahí era la imposible.**

Comprobado: `comprobarDesbordes()` devuelve **0 problemas sobre las 40 escenas de MDH-006**.
La barrera no falló — nunca estuvo mirando.

Lo mismo pasaba con `ajustarTamano()` (C21.1, «encoge hasta que quepa»): su lista de
selectores no incluye `svg text` en absoluto, y aunque lo incluyera, `scrollWidth` no
existe ahí. **El diagrama horizontal del episodio largo era el único tipo de escena del
motor sin ninguna protección de anchura, en las dos capas.**

### Lo que entra, y está medido

**1 · `ajustarTextoSVG()`**, dentro de `cargar()`, una vez por escena (regla 11.5). Mide con
`getComputedTextLength()`, que sí existe en SVG, contra el ancho del `<rect>` de su mismo
`<g>` menos 18 px de aire a cada lado.

**Y encoge en bloque, no caja por caja.** Si el paso 2 baja a 40 px y los otros se quedan en
46, salen tres tamaños de letra distintos y eso se lee como un fallo de maquetación, no como
un ajuste: se aplica a todos el factor del peor. Los títulos entre sí y los pies entre sí.
Es lo que haría cualquiera a mano.

Suelo: **32 px** para el título del paso y **22 px** para su pie sobre un lienzo de 1920. Por
debajo no se lee en un móvil, y entonces el problema no es el tamaño: es que el guion ha
escrito una frase donde iba una etiqueta. Ahí salta la barrera y para el render, que es lo
que debe pasar.

**2 · `comprobarDesbordes()` gana una rama para el texto SVG**, midiendo cada `<text>` contra
su propio `<rect>` con 2 px de tolerancia.

**3 · `ricoSVG()` — y este es un defecto que nadie había visto.** La rama horizontal pintaba
los pasos con `esc()`, no con `rico()`, porque un `<span>` no existe dentro de un `<svg>`. **El
resaltado se quedaba a la vista, con los asteriscos.** Está publicado en MDH-004 escena 15
(«*ahí*, y casi nunca antes») y **estaba a punto de publicarse el 19/09 en MDH-007**, escena
10 («*Usarla*») y escena 20 («Buscas *tres*»). El equivalente de `<span>` en SVG es `<tspan>`,
que sí acepta `fill`. Es el mismo defecto que MDS-011 —una marca de pantalla en un sitio
donde nadie la interpreta— con la diferencia de que aquí sí se ve.

**4 · Aviso en `validar_guion.py`**: un paso de `diagrama` en formato largo con más palabras
de las que caben. Con tres pasos, seis; con cuatro, cuatro; con cinco, tres. Aviso y no error
porque el motor ya garantiza que quepa — pero encoger es el remedio, no el sitio donde se
arregla.

### Verificado contra el motor, no imaginado (regla 11.2)

- **Las 302 escenas de los 28 guiones, con el motor nuevo: 0 paran el render.** El encogido
  resuelve el único caso sin llegar al suelo.
- **MDH-006 escena 22 después:** los tres títulos a 37,89 px, el que se salía en **497 px
  dentro de 533**. Mirado en captura, no deducido.
- **Diferencia de píxeles contra el motor viejo, sobre las nueve escenas `diagrama` más dos
  escenas de control por guion:** cambian **cuatro**, y son exactamente las cuatro que tenían
  un defecto real (MDH-006 esc 22, 0,98 %; MDH-007 esc 10 y 20 y MDH-004 esc 15, entre 0,11 %
  y 0,20 %, que es el resaltado). **Todas las demás, idénticas al píxel.**
- **Determinista:** dos pasadas del motor nuevo sobre la misma muestra, diferencia 0,0000 %.

---

## C30 · Una tarea programada no puede pedir permiso, y no puede tener dos prompts

**El encargo del codirector:** *«La revisión semanal no se ejecutó por completo porque pidió
autorización manual. Esto no puede ocurrir, porque entonces se va al viernes y ya se
desaprovecha la cuota. Tiene que ejecutarse de forma automática y si algo no debe realizarse,
que quede constancia y lo hagamos manualmente en otro momento, pero que no bloquee.»*

### La causa, y estaba escrita en el prompt

`planificacion-jueves.md`, regla 1: *«Si `mcp__remote-devices__device_list_dir` sobre
`C:\MisProyectos\Humor` responde: trabaja ahí.»* Y lo mismo en `revision-diaria.md`: *«A las
11:30 el ordenador del codirector suele estar encendido. Prueba primero…»*

Una tarea programada corre en la nube. **El puente de dispositivos no existe en ese modo y no
ha existido nunca** — lo dicen todas las bitácoras que lo mencionan, incluida la del 3 de
septiembre con esas palabras exactas. Lo único que consigue esa llamada es **abrir una
petición de autorización** en el ordenador del codirector. A las diez de la noche de un
jueves, nadie la contesta. La sesión espera, la planificación se va al viernes y se pierde la
cuota del jueves, que es lo único para lo que esa tarea corre el jueves.

**La optimización compraba no tener que descomprimir un `.tar.gz`. Costó una semana de
planificación.**

### Lo que entra

**1 · Fuera la sonda, en los tres prompts.** No se llama a `mcp__remote-devices__*` nunca.
Se clona, se trabaja en el contenedor y se entrega `.tar.gz`. Siempre.

**2 · La regla general, que es la que pidió el codirector y va delante de todo:**

> **No pidas nunca una autorización, un permiso ni una confirmación a nadie.** No hay nadie
> delante: una pregunta no se queda sin contestar, se queda colgada. **Lo que no puedas hacer
> tú solo, no lo intentas: lo escribes** —en la bitácora, en la sección «Para el codirector»,
> con qué hay que hacer y por qué no lo has hecho tú— **y sigues.**
>
> **Entregar algo incompleto y dicho es siempre mejor que entregar nada esperando permiso.**

**3 · Y de paso, lo que hacía que esto fuera difícil de arreglar: se acaban las dos copias.**

Hasta hoy el prompt que corría vivía en el almacén de tareas programadas y
`00_estrategia/tareas/` era **un espejo**. El propio `LEEME.md` de esa carpeta avisaba: *«Si
un día no coinciden, la del almacén es la buena — y este fichero está desactualizado.»* Es
decir: el proyecto sabía que iban a divergir y lo había aceptado.

**Ahora el fichero del repositorio ES el prompt.** El del almacén se ha reducido a un arranque
de una página que dice: clona el repositorio, lee `00_estrategia/tareas/<tu fichero>.md` desde
el primer `---` hasta el final, y síguelo como si fuera este mensaje.

- Cambiar lo que hace un agente es **editar un fichero y commitearlo**.
- El prompt **se versiona con git** y se revisa en un diff, como el código. Es la instrucción
  más cara del proyecto y era lo único que no se podía revisar así.
- **Se acabó la divergencia.**

**El precio, dicho para que no sorprenda:** un cambio en esos ficheros **no surte efecto hasta
que está en `origin/main`**. Es la trampa 11 (el reloj) aplicada a los prompts.
Y por si el clon falla, el arranque lleva repetidas inline las seis o siete reglas cuyo
incumplimiento hace daño irreversible: no pedir permiso, no llamar al puente, no hacer `push`,
un fichero un dueño, y no escribir el nombre del codirector. Si no puede clonar, dice el error
y para; no improvisa.

**Aplicado hoy** a `trig_015qkb2sqbbJwJE1qgoNMK95` (planificación) y
`trig_019QjtovuzeUocmx1P8NJH3F` (revisión diaria), y verificado leyendo lo que quedó guardado.
**`trig_01GhNrF8nA2w2nXSfetcrHkQ` (métricas) sigue con el prompt entero en el almacén**: su
espejo `metricas-lunes.md` no se ha tocado hoy y pasarlo al mismo esquema queda pendiente.

---

## C31 · El registro no sabe lo que sabe YouTube

**El aviso del codirector:** *«la revisión diaria del 9/9 insistió en que MDS-011 no se había
publicado, hasta el punto de ponerlo como incidencia, cuando lo publiqué yo a mano. Tiene
permiso de YouTube concedido manualmente, así que no entiendo por qué no lo comprueba.»*

**Por qué no lo comprueba: porque no puede.** La revisión diaria corre en un contenedor en la
nube **sin red** —sus propias bitácoras lo dicen cada día— y su prompt le prohíbe expresamente
tocar YouTube. El permiso que el codirector concedió a mano es el del token de OAuth, y lo usan
`publicar.py` y `metricas.py` **desde GitHub Actions**, que sí tiene red. La revisión diaria no
lo ha tenido nunca.

Lo que ella lee es `registro_publicaciones.json`, y ahí está el defecto de fondo, que ya era la
**trampa 4**: *un campo que se escribe una vez y describe algo que cambia después, miente.* El
registro guarda el estado **del momento de la subida**, y lo único que lo corrige es
`metricas.py`… **los lunes**. Entre lunes y lunes el fichero puede llevar seis días desfasado.

MDS-011 se subió el 07/09 en `private` sin `publicar_en`, el codirector lo publicó a mano, y
nada escribió eso de vuelta. La revisión lo ha reportado como incidencia **seis días
seguidos**. No estaba leyendo mal el fichero: **estaba leyendo un fichero caduco como si fuera
el mundo.**

### Lo que entra

**1 · Ahora mismo, en el prompt: «no lo sé» no es «no publicado».** Sobre un vídeo cuyo
estado no cuadre, la primera vez es INCIDENCIA con todas las letras —puede ser el fallo de
MDH-004, y ese sí deja un vídeo escondido para siempre—. **A partir de la segunda**, y
mientras no cambie nada, baja a la bitácora redactado como *«sigue sin confirmar en el
registro desde el <fecha>; si lo publicaste a mano, está bien y se corregirá solo el lunes»*.
Y **si el codirector ha dicho en cualquier sitio que lo publicó él** —`ESTADO.md`,
`PROMPT_DIRECCIÓN.md`, una bitácora—, el asunto está cerrado.

**Por qué esto importa más de lo que parece:** una incidencia que se repite idéntica seis días
deja de ser un aviso y pasa a ser ruido. Y el ruido es lo que hace que el séptimo no se lea.
Un canal que publica una alarma falsa al día se queda sin alarmas.

**2 · El arreglo de raíz, encargado:** sacar a una función suelta de `metricas.py` la parte
que **ya sabe hacerlo** —preguntarle a YouTube el estado de los vídeos recientes y corregir el
registro, arreglada el 28/08— para poder llamarla sin tocar las métricas; y dejar en
`07_pruebas/` el diseño de un workflow que la llame **todos los días antes de las 11:28**.
Actions tiene red y tiene el token. Lo crea el codirector a mano, como todos los de
`.github/workflows/`.

---

## C27 · Corregido: el episodio largo sale con UNA voz

**El codirector, el 7 de septiembre:** *«he deducido que planteabas la opción de que algunas
escenas salieran con la voz de Flash y las otras con edge-tts para el vídeo largo si nos
quedábamos sin cuota. Eso es una chapuza. En ese caso prefiero que el vídeo se construya con
más tiempo.»* Y planteó tres opciones.

### La respuesta: ninguna de las tres, y el motivo es que la (a) ya está hecha

**Opción (a) — que la planificación vaya una semana por delante, para tener nueve días en vez
de dos.** Ya es así. La planificación del jueves 10 escribió `MDH-007`, que se produce el
**sábado 19**: nueve días. La del 3 escribió `MDH-006` para el 12. **El calendario ya da los
días que pedía.**

Lo que falta no son días: es **la máquina que los gasta**. Y está diseñada desde el 7 de
septiembre —la caché de `voz.py` más `voz_adelantada.yml`— y no ha entrado porque el workflow
tiene que crearlo el codirector a mano.

**Opción (b) — mover el día de la planificación.** El jueves es el día correcto por cuotas
(los límites se reinician el viernes por la mañana; se gasta lo que iba a caducar). Y no
compra nada que la caché no compre ya.

**Opción (c) — un agente nuevo que construya el largo día a día.** La **forma** es la
correcta: construir poco a poco a lo largo de la semana es exactamente lo que hace falta. El
**quién** no. Y esto merece quedar escrito como criterio general:

> **Construir el vídeo día a día no es un trabajo que necesite juicio, así que no debe ser un
> agente.** No hay nada que decidir: se mira qué escenas faltan en caché y se sintetizan
> hasta agotar el margen del día. Un agente es la forma más cara de ejecutar un bucle
> determinista, es la única que puede equivocarse de forma creativa, y añade un cuarto prompt
> que mantener, un cuarto dueño en la tabla de propiedad y una cuarta cuota que gastar.
> **Un workflow de Actions lo hace mejor: es gratis, tiene red, tiene los secretos, ya corre
> todos los días y no consume una sola llamada de modelo.**

### Las dos correcciones a C27

**1 · Un episodio largo sale con UNA sola voz, nunca mezclada.** La versión 6.1 decía: *«un
mal día no deja al canal sin vídeo: deja alguna escena con voz peor, y `ficha.json` dice
cuáles»*. **Eso es exactamente la chapuza que el codirector descartó.** Se cambia:

> La decisión se toma **una vez, el viernes por la noche**. Si la caché tiene las ~40
> escenas, el episodio entero va en Gemini. Si falta **una sola**, el episodio entero va en
> `edge-tts`, como siempre. Nada de «lo que falte cae al respaldo». Lo elegido se escribe en
> `ficha.json` y se dice en `ESTADO.md`.

Se pierde una semana de cuota cuando falla, y la cuota es gratuita y si no se usaba caducaba
igual. A cambio, nunca hay un vídeo con dos voces.

**2 · La ventana se abre el viernes, no el martes.** La versión 6.1 decía «de martes a
viernes»: cuatro días × 10 peticiones = **40 llamadas para ~40 escenas**, es decir, **cero
margen**. Pero el guion del sábado siguiente queda cerrado la noche del jueves anterior —la
planificación del 10 dejó `MDH-007` cerrado y dicho: *«no se va a tocar, que es lo que
`voz_adelantada.yml` necesita»—, así que la ventana real es **de viernes a viernes: ocho días
× 10 = 80 llamadas para 41 escenas.** El doble de lo que hace falta.

**Y lo que queda igual:** modelo 2.5 y no 3.1, para no competir con la cuota de los Shorts; 25 s
entre llamadas; y la caché indexada por sha256 del texto, que hace que corregir una escena
resintetice solo esa escena.

**La parte incómoda de su frase de entonces —«si no, dejamos de hacer largos»— sigue viva y
sin decidir**, para el 27 de septiembre. MDH-005 tuvo una visualización. Si C27 no iguala el
largo al Short en calidad, la pregunta no es cómo mejorarlo sino si merece la semana.

---

## C32 · El formato de las peticiones al codirector

**Textual, del 7 de septiembre y repetido el 12:** *«todo lo que necesites de mí va en un
fichero tareas_codirector_FECHA.md, explicado de principio a fin y sin resumir, aunque sea
algo que ya hayamos hecho antes (se me olvidan cosas, como me pasó con el token). Prefiero
leer rápido algo que ya me sé a acabar en una conversación paralela con Haiku intentando
entender qué me pides.»*

Queda como regla, en `PROMPT_DE_ARRANQUE.md` y aquí:

- **Todo lo que la dirección necesite del codirector va en
  `00_estrategia/tareas/tareas_codirector_AAAA-MM-DD.md`.** Nunca en un párrafo suelto dentro
  de un resumen, nunca solo en `ESTADO.md`, nunca solo en la conversación.
- **Explicado de principio a fin**: por qué hace falta, qué abre o desbloquea, los pasos
  exactos, cómo saber si ha funcionado, y qué NO hay que hacer. **Sin resumir aunque ya se
  haya hecho antes.**
- **Cada tarea lleva su tiempo estimado**, para que se pueda decidir qué entra en un rato
  suelto.
- **Y lleva su sitio exacto.** Esto es del 12/09 y sale de un fallo propio: la tarea del token
  estaba bien explicada y la de `GEMINI_API_KEY` decía «copia una de esas líneas y pégala
  justo debajo» **sin decir en qué paso del workflow**. El codirector la pegó en la primera
  aparición de `secrets.` que encontró, que es el paso de subir a YouTube, y la clave no llega
  a `voz.py`. Instrucción impecable, resultado inservible. → **Trampa 18.**

---

## Lo que NO cambia hoy

- **El calendario.** Cinco Shorts y un largo; la planificación sigue el jueves a las 22:00.
- **C25 y su orden.** P1 y P8 en la semana del 14, P2/P7/P5 en la del 21, P9 ahora sí en la
  del 21 porque la autorización de `montaje.py` está escrita. El punto de control sigue siendo
  el **27 de septiembre**.
- **C26 entera.** La decisión sigue siendo el **15 de noviembre**, con la mediana de los
  últimos veinte Shorts a 48 h, y los umbrales solo se pueden discutir **antes del 8 de
  noviembre**.
- **No se amplía el tema**, no se clona la voz, no vuelven los subtítulos quemados, y C10,
  C20 y C13 siguen detrás del peldaño S1.
- **La regla 11.1 sigue suspendida** para los cambios de presentación hasta el 27. Los cuatro
  arreglos de hoy son de defecto, y los arreglos de defecto nunca han consumido ranura.

---

# Versión 8 · 14 de septiembre de 2026 — la voz se dirige, y la imagen deja de ser texto

Todo lo anterior sigue vigente salvo lo que esta sección corrige expresamente. Es la
sesión de dirección del lunes, con la primera lectura de métricas que trae medianas
limpias a 48 horas y con el primer Short producido con Gemini ya escuchado.

**Lo primero, porque ordena todo lo demás: los números no están parados, están peor.**
La versión 7 decía «los números no se han movido». Con `vistas_48h` ya calculado por
`metricas.py`, la foto real es esta:

| | |
|---|---|
| Mediana de vistas a 48 h de los últimos 15 Shorts | **10** |
| Shorts por encima de 50 vistas a 48 h | **0 de 15** |
| Shorts por encima de 100 | **0 de 15** |
| Suscriptores ganados en 51 lecturas acumuladas | **0** |
| Me gusta en los cinco Shorts de la última semana | **0** |
| `MDH-006`, el episodio largo del sábado, a 2 días | **0 visualizaciones** |
| `MDS-014`, a 4 días | **1 visualización** |

La semana pasada la racha era 31 · 21 · 21. Esta semana es 26 · 13 · 8 · 1 · 31. Con
muestras de este tamaño nada de eso es estadística —la diferencia entre 8 y 31 son
veintitrés personas— pero **la dirección de la línea no es la que queríamos ver a trece
días del punto de control**, y decir «no se ha movido» sería más cómodo que exacto.

Y una cifra más, de la curva de retención, que es nueva y cambia dónde hay que apretar:
**`MDS-015` pierde la mitad de la audiencia en el segundo 13 y llega al segundo 26 con el
20 %.** No hay un desplome en el primer segundo: hay una fuga constante. No es un problema
de gancho. Es un problema de que, una vez dentro, no damos motivos para quedarse.

---

## Lo que se ha escuchado hoy, y de dónde salía cada cosa

La dirección escuchó el primer Short con voz de Gemini y lo resumió así: *«Está mejor, sin
duda, es un paso adelante»*, con tres reparos. Los tres tienen la misma raíz y la raíz
estaba en una sola constante de doce líneas.

### 1 · «Empezar con una risa y estar riéndose casi todo el short es excesivo»

**Los guiones no llevan risas escritas.** Comprobado sobre las 47 escenas de los ocho
Shorts con guion en el repositorio: cero. Las risas las pone el modelo, y las pone porque
**se las pedíamos en todas las escenas**. La dirección de actor era una constante:

> «Locuta esta frase de un vídeo corto de divulgación sobre humor […] cuéntala con la
> entonación de quien cuenta algo que le hace gracia.»

Esa frase iba pegada delante de las seis escenas por igual. Delante del planteamiento, del
dato, de la lista y del «y aquí falla: solo sabemos cómo suena». **Una instrucción de tono
aplicada a todas las escenas no es tono: es un tic**, y un modelo de voz que oye «algo que
le hace gracia» cuarenta segundos seguidos se ríe cuarenta segundos seguidos.

### 2 · «El guion se siente inconexo, resumido sin puntos en común»

Aquí hay dos cosas distintas y conviene no mezclarlas, porque una ya está arreglada y la
otra no lo estaba.

**La parte del guion ya se arregló el 12 de septiembre** con las tres pruebas de cosido de
`guionista_corto.md` (el hilo, nada nuevo después de la mitad, el detalle con la misma
palabra). Lo que pasa es que **todavía no se ha visto ni un solo Short escrito con ellas**:
`MDS-016` a `MDS-020` y `MDH-007` los escribió la planificación del **jueves 10**, dos días
antes de la reescritura. El primer Short con el guionista nuevo lo escribe la planificación
del **jueves 17** y se publica el **lunes 21**. Hasta entonces, todo lo que se publique es
material anterior al arreglo. Esto no es una excusa: es la fecha a partir de la cual el
arreglo se puede juzgar.

**Y la parte que no estaba arreglada, que es de la voz y no del guion.** Con Gemini, cada
escena es **una llamada independiente a la API**. El modelo no sabe que hay cinco escenas
más: le damos una frase suelta, y le pone a esa frase su propia entonación de arranque y su
propio punto final. Seis fragmentos autónomos seguidos suenan a seis frases sueltas **por
bien cosido que esté el guion en papel**. Y encima, entre una y otra, metemos nosotros un
silencio de hasta 1,35 s: un punto final, un silencio y otro principio no es una pausa
dramática, es un corte.

`MDS-016` es la demostración. Su guion tiene hilo de sobra —la madre, la cena del domingo,
los doce que ahora son vecinos— y aun así se oye despiezado. **El guion estaba cosido y la
voz lo descosía.**

### 3 · «Instrucciones mucho más claras y delimitadas para el actor»

Es la petición correcta y es la que resuelve las otras dos.

---

## C33 · La dirección de actor deja de ser una constante

**Hecho hoy, en `voz.py`. Entra en producción con `MDS-017` (martes 15).**

La dirección se construye **por escena**, y se construye sola: todo lo que hace falta para
dirigir una escena ya está en el guion, así que **no se toca el guionista y no hay nada que
el guionista pueda escribir mal.**

| De dónde sale | Qué decide |
|---|---|
| `tipo` de la escena | el papel: dato, comparación, lista, cita, cierre… |
| la posición | si abre el vídeo o lo cierra |
| `pausa_despues_s` **de la escena anterior** | **si esta escena es el remate** |
| `pausa_despues_s` **de esta escena** | si la frase se deja suspendida o se cierra |
| la narración de la escena anterior | el enlace, para que no arranque en frío |

**Los ocho papeles y qué se le pide a cada uno.** Esto es lo que la dirección pedía por
escrito —qué se lee del tirón, qué lleva pausa, qué va en serio:

- **apertura** — entra en frío, en mitad de una historia ya empezada. Tono de conversación.
- **planteamiento** — llano y sin subrayar: anunciar la gracia la estropea.
- **remate** — del tirón, sin pausas por dentro, **y completamente en serio**. Y una frase
  explícita: *no te rías tú*.
- **contraste** — dos mitades, con cambio claro de color de voz entre ellas.
- **cifra** — el resto del tirón, la cifra más despacio y clara, sin énfasis de anuncio.
- **enumeración** — marcar cada elemento, bajando el tono al pasar al siguiente.
- **cita** — otro color de voz mientras duran las palabras de otro.
- **objeción** (el cierre) — **baja el tono, en serio, sin ironía y sin gracia.**

**Cómo se detecta el remate, que es la pieza que parecía imposible.** No hace falta ningún
campo nuevo: `guionista_corto.md` ya manda 1,2–1,5 s de pausa entre planteamiento y remate
y 0,2–0,7 s en todo lo demás. Las dos poblaciones no se solapan. Medido sobre los ocho
Shorts del repositorio: **8 remates detectados en 47 escenas, uno por Short, los ocho
correctos, ningún falso positivo.**

**Y el arreglo del descosido, que es el menos obvio de los tres.** Cuando después de una
frase viene un silencio nuestro, ahora se le pide al modelo que **deje la frase suspendida,
sin cerrar la entonación**. Las pausas las seguimos poniendo nosotros —la versión 5.1 midió
que pedírselas al modelo da silencios de decenas de segundos— pero por fin le decimos qué
hacer con la frase que las precede. Un silencio después de una frase suspendida es una
pausa dramática; después de un punto final es un corte. Era literalmente lo mismo que la
regla del callback de la 13, aplicada al eje de la voz.

Y en todas las escenas, sin excepción: **no te rías, no añadas risas, risitas, resoplidos,
suspiros ni carraspeos.** Incluido el remate — sobre todo el remate: un chiste contado por
alguien que se ríe de su propio chiste deja de tener gracia.

### Lo que se probó y se retiró el mismo día

La primera versión intentaba además **deducir dónde va el retintín**, con dos señales: unas
comillas, o una palabra que nombrase el tono. Probada contra las 47 escenas reales, dispara
siete veces y **acierta una**:

| Escena | Lo que dispara | Lo que es de verdad |
|---|---|---|
| MDS-013 e1 | «el navegador» | un apodo |
| MDS-013 e3 | «no va en serio» | una cita |
| MDS-014 e2 | «sarcástico», «ingenioso» | resultados de un test |
| MDS-014 e3 | «Ironía, nonsense, sarcasmo» | nombres de categorías |
| **MDS-016 e1** | **«con retintín: qué ilusión»** | **ironía de verdad** |
| MDS-016 e4 | «al hablar irónicamente» | el tema del vídeo |

En español las comillas marcan citas y apodos mucho más que ironía, y en un canal **sobre
humor** la palabra «ironía» aparece por ser el asunto. Una señal que acierta una de siete
no es una señal: es ruido, y dirigir con ruido es exactamente lo que convirtió la dirección
vieja en un tic. **Retirada, y el motivo queda escrito en el código** para que a nadie le
parezca una buena idea dentro de tres semanas.

Es el mismo desenlace que la comprobación amplia de C22, que señalaba el 73,5 % de las
escenas, y la misma lección: **una comprobación estrecha que acierta siempre vale más que
una lista que señala tres de cada cuatro.**

**Entonces, ¿cómo se dirige la ironía?** Se declara, no se adivina. Encargo para la
planificación del jueves 17, abajo.

### Dos efectos secundarios que había que atender, y se han atendido

1. **La caché de voz ahora incluye la dirección en su clave.** Dos escenas con el mismo
   texto y distinto papel tienen que sonar distinto, y una caché que solo mirase el texto
   devolvería la toma vieja sin decir nada. Efecto buscado: **cambiar la dirección invalida
   la caché entera**, y la siguiente producción se sintetiza de cero.
2. **`voz_precache.py` se ha alineado con lo mismo.** Llamaba a `_gemini_pcm()` con el
   texto pelado, así que después de C33 habría precacheado el episodio largo **sin dirigir
   y con una clave que `voz.py` nunca habría encontrado**: una semana de cuota gastada para
   nada, en silencio. Es la trampa 1 del `PROMPT_DE_ARRANQUE.md` —cuando cambies algo, busca
   qué dependía de ello— y esta vez se buscó antes de entregar.

### Cómo se verá si ha funcionado

- `ficha.json` lleva ahora **`direccion_voz` por escena** con el papel que se le pidió. Se
  puede revisar el expediente sin escuchar el vídeo, igual que con `motor_voz`.
- **La prueba de verdad es escucharlo:** `MDS-017`, martes 15 a las 19:00.
- Si algo suena peor que hoy, se vuelve a `edge` con una línea —el respaldo automático
  sigue intacto— y esta sección se corrige.

---

## C34 · La imagen: se revierte el descarte del 7 de septiembre

**La petición de la dirección, textual:** *«hay que dar un cambio importante a la
presentación en imagen sí o sí o nos hundimos […] las miniaturas y los vídeos con fondo
azul y letras amarillas no pueden competir de ninguna manera con el atractivo de imágenes
reales».*

### Por qué lo descarté, y por qué estaba mal

C25 lo despachó en una línea: *«Lo que se descarta, y por qué: imágenes de banco (regla 9 y
no son de marca), imágenes generadas por IA (coste…)».* Los tres argumentos, uno a uno:

- **«Regla 9».** La regla 9 es *«nada de material ajeno **sin licencia**»* y su texto habla
  de clips de cómicos, programas y películas, por el riesgo de strike. **Una foto CC0 tiene
  licencia.** Estiré la regla hasta que dijera lo que me convenía. Es el error que la
  trampa 2 describe: diseñar alrededor de una restricción sin comprobar que dice eso.
- **«No son de marca».** Este sí era un argumento de verdad, y **tiene arreglo** — es todo
  el contenido del apartado siguiente.
- **«IA: coste».** No estaba medido. La trampa 8 del proyecto es exactamente esa: dar una
  cuota por conocida sin mirarla. Se mide antes de decidir.

**Se revierte el descarte.** Y no por deferencia: por el dato. CTR de miniatura **1,43 %**
contra un umbral de 4 %, **72 %** de las escenas es texto centrado sobre fondo, y una
retención que se desangra a lo largo del vídeo en vez de romperse al principio. Tres
señales distintas apuntando a lo mismo: **una vez que alguien entra, no hay nada que
mirar.**

### El diseño: la foto no entra cruda, entra vestida

**El riesgo real no es el que decía C25.** Meter fotos de stock crudas no nos deja «sin
marca»: nos cambia una firma reconocible por otra. Hoy parecemos un vídeo automatizado; con
fotos de stock crudas pareceríamos un carrusel de LinkedIn. Eso no es avanzar.

Así que la foto entra con **cuatro reglas de tratamiento**, todas en CSS, todas
deterministas y todas de coste cero de render:

1. **Duotono sobre la paleta del canal.** `grayscale(1)` más una capa del ámbar o el cian
   de marca en `mix-blend-mode: multiply`, sobre el azul `#0B1220`. Es lo que hace que
   **cuarenta fotos de cuarenta orígenes distintos parezcan una colección**, y es la
   respuesta técnica a «no son de marca».
2. **Enmarcada, nunca a sangre.** La foto vive dentro de una ventana de la rejilla de
   taller de P1, con su marco. El canal está *mirando* algo, no usando un fondo de
   escritorio.
3. **Nunca sola.** La foto acompaña; la jerarquía de tres tamaños de P6 sigue mandando. La
   dirección lo pidió así: *«me gusta el esquema de colores actual y las diapositivas que
   aparecen, pero deben ser intercaladas»*. De acuerdo, y por una razón de fondo: la
   diapositiva es lo que hace el vídeo **indexable**, y la búsqueda es hoy la única fuente
   de tráfico que crece.
4. **La foto se mueve.** Deriva lenta del 5 % durante la escena. Determinista, sin
   `Math.random()`, coste cero: es una `transform` de CSS.

### Cómo se decide esto, y se decide mirando

**`07_pruebas/imagen-14-09/muestrario.html`** — una página local donde se sueltan dos o tres
fotos y se ven dentro de una escena real del canal con los cinco tratamientos candidatos
(cruda, duotono ámbar, duotono cian, gris frío, ámbar con trama). No usa red, no sube nada
a ninguna parte y no necesita que exista todavía ningún banco.

**Lo que hay que mirar no es si la foto es bonita: es si tres fotos distintas, de fuentes
distintas, parecen de la misma colección después del tratamiento.** Si lo parecen, «no son
de marca» queda resuelto y C34 sigue. Si no lo parecen, **C34 se para ahí** y no se ha
gastado nada. Es la regla 11.2 —se mira el muestrario, no se imagina— aplicada antes de
escribir una línea de `escena.html`.

### De dónde salen las fotos: tres vías, por orden de lo que cuestan

**Vía 1 · el lote de prueba (esta semana).** Doce a veinte imágenes, nada más. Suficiente
para juzgar el tratamiento y para vestir la escena 1 de los cinco Shorts de una semana. Si
el muestrario convence, este lote es la primera tanda del banco; si no, no se ha perdido
nada.

**Vía 2 · el banco propio (es la idea de la dirección y es la buena).**
`02_marca/banco/` con un `banco.json` que lleva, por imagen: fichero, licencia, autor,
enlace de origen y **etiquetas**. Crece por tandas y **no se rehace nunca**: una imagen que
entra se queda para siempre y se reutiliza. Eso es lo que convierte esto en coste cero de
verdad y, sobre todo, en **cero trabajo recurrente** (regla 5): el esfuerzo es de arranque,
no de cada semana. A partir de unas cuarenta imágenes bien etiquetadas, ningún Short
necesita imagen nueva.

**Vía 3 · generarlas nosotros (la que más me convence a medio plazo, y la que hay que
medir antes).** Resuelve de golpe licencia, coherencia de estilo y la objeción de marca,
porque el estilo lo elegimos nosotros. Y es exactamente la analogía que trajo la dirección:
*«el ejemplo lo tenemos en casa, en cómo estamos trocear los vídeos largos para que se
produzcan en pequeñas dosis diarias manteniendo la cuota diaria»*. Es `voz_adelantada.yml`
aplicado a imágenes: N al día dentro de la cuota gratuita, acumulando un banco que después
se usa mil veces.

**Pero no se diseña alrededor de una cuota que no se ha mirado.** Va como sonda, no como
plan: la petición está en la tarea de hoy y son dos minutos en el mismo panel donde ya se
miró la de TTS. **Si la cuota de imagen no existe o no es gratuita, la vía 3 se cae y las
vías 1 y 2 siguen en pie sin cambios.**

Y si entra: **se declara en la descripción, como la voz.** La regla 7 dice que el uso de IA
se declara aunque no sea obligatorio. C25 argumentaba que «el canal declara IA en la voz,
no en el dibujo», lo cual es una razón para ampliar la declaración, no para no usarla.

### Dónde se pone la primera imagen, que es lo único que importa esta semana

**En la escena 1 del Short.** No en la miniatura, aunque el CTR de 1,43 % pida a gritos lo
contrario, y el motivo es que en el feed de Shorts **no hay miniatura que pulsar**: el
vídeo arranca solo. La miniatura decide en los episodios largos y en la página del canal, y
el largo es hoy el producto que menos tráfico mueve. El peldaño S1 se juega en el primer
segundo del Short, y ahí es donde una cara humana real, en duotono, detrás de cuatro
palabras, compra más que en ningún otro sitio del proyecto.

Segunda posición: **la miniatura del episodio largo**, si el largo sigue vivo después del
27 (ver abajo). Cinco imágenes, una por serie, y no hacen falta más.

---

## C35 · La densidad de estímulo — y por qué no hace falta trocear más

**La observación de la dirección:** *«en la publicidad el número de imágenes/estímulos que
aparecen es bastante alto […] es difícil dejar de mirar y deberíamos optar por algo así»*.

**La aritmética, que es lo que decide dónde apretar.** Un anuncio bueno cambia de plano cada
1–1,5 segundos. Un Short nuestro tiene seis escenas en cuarenta y ocho segundos: **un
cambio cada ocho**. Esa es la distancia real, y explica la fuga continua de la curva de
retención mejor que ninguna otra cosa que tengamos medida.

**La reacción natural sería partir el Short en más escenas. Es la vía cara y además no hace
falta.** Cara, porque cada escena es una llamada a Gemini y el nivel gratuito da diez al
día: un Short de doce escenas no cabe en su día de producción, y arreglarlo obliga a
precachear los cinco Shorts de la semana además del episodio largo. La cuenta semanal, para
tenerla escrita de una vez:

| | Llamadas/semana | De un presupuesto de |
|---|---|---|
| Hoy: 5 Shorts × 6 escenas (modelo 3.1) | 30 | 70 |
| Hoy: 1 episodio largo × ~40 escenas (modelo 2.5) | 40 | 70 |
| Si los Shorts pasaran a 12 escenas | 60 | 70 — **sin margen, y solo con precaché** |

**Y no hace falta, porque la densidad se construye dentro de la escena, no partiéndola.**
Una sola escena de ocho segundos con el icono dibujándose (P3), el texto apareciendo por
partes (P6), la cifra contando desde cero (P5), el personaje entrando (P8) y la foto
derivando (C34) son **cinco cambios en ocho segundos: uno cada 1,6 s.** Eso es densidad de
anuncio, sin un corte añadido, sin una llamada más de cuota y sin tocar el guion.

**Así que C35 no es un cambio nuevo: es la razón por la que P3, P5, P6 y P8 dejan de ser
mejoras de acabado y pasan a ser el asunto principal.** Estaban repartidas entre la semana
del 7 y la del 21 como si fueran acabado. No lo son: son el ritmo.

**Lo que sí queda anotado como límite conocido,** para que nadie lo redescubra a golpes:
mientras la voz de los Shorts vaya por Gemini, **un Short no puede pasar de nueve escenas
sin precaché.** No es un bloqueo hoy; es la pared con la que se choca el día que se intente.

---

## Lo que le toca a la planificación del jueves 17

Dos encargos, los dos escritos para que no haya que interpretarlos:

**1 · El campo `voz_tono`, opcional y con vocabulario cerrado.** Ya que la ironía no se
puede detectar, se declara. Un campo opcional por escena con **dos valores y ningún otro**:
`retintin` (la frase se dice significando lo contrario) y `serio` (esta escena no admite
guasa aunque su papel la permitiera). Sin valor, manda el papel que deduce C33, que cubre
las 47 escenas medidas. `validar_guion.py` da **error** si aparece un valor fuera de esos
dos — un campo de texto libre aquí acabaría en prosa que el modelo de voz leería en alto,
que es exactamente el fallo de MDS-011 con el resaltado.

**2 · Los Shorts del 21 al 25 son los primeros con el guionista nuevo.** Son la prueba de
las tres pruebas de cosido, y de ellos depende que se pueda decir algo del arreglo del 12
en el punto de control del 27. Que la escena 1 de los cinco esté escrita **contando con que
va a llevar imagen** (cuatro palabras o menos, C19/P4).

---

## El episodio largo: la pregunta se adelanta, la decisión no

`MDH-006` es, con palabras de la dirección, el mejor contenido del canal hasta ahora —*«el
contenido está bien, incluso mejor que otras veces, y se aprende algo. Ese es el camino»*—
y tiene **cero visualizaciones a las 48 horas**. `MDH-005` lleva cinco en nueve días.

Cuesta cuarenta escenas de guion, cuarenta de render, la revisión entera de la semana y
toda la maquinaria de C27 (la caché, el precaché, un workflow que la dirección tiene que
crear a mano). Y si se libera, esa capacidad no se pierde: se convierte en escenas de Short
con voz dirigida y en imágenes de banco.

**No se decide hoy y no se decide solo.** La fecha sigue siendo el **27 de septiembre**,
como estaba escrito, y esta entrada existe para que ese día la pregunta ya esté formulada y
no haya que improvisarla. Lo que sí decido hoy es **cómo llegamos a esa fecha**: `MDH-007`
(19/09) sale **con voz de Gemini**, lo que obliga a crear `voz_adelantada.yml` esta semana.
No por el vídeo en sí, sino porque **comparar un largo con voz mala contra Shorts con voz
buena no es comparar**: el 27 tienen que estar los dos productos en igualdad de condiciones
o la decisión no vale nada.

---

## Lo que NO cambia hoy

- **El punto de control sigue siendo el 27 de septiembre** y la decisión, el **15 de
  noviembre** (C26). Nada de lo de hoy mueve esas fechas, y los umbrales de C26 siguen sin
  poder tocarse después del 8 de noviembre.
- **La regla 11.1 sigue suspendida** para presentación hasta el 27, que es lo que permite
  meter C33 y C34 en la misma ventana. Siguen en pie la 11.2, la 11.5 y la barrera de C21.
- **No se clona la voz de la dirección**, no se encienden los subtítulos quemados, no entra
  C10, y `.github/workflows/` sigue sin escribirse en remoto.
- **Los guiones de esta semana no se tocan.** `MDS-017` a `MDS-020` y `MDH-007` están
  validados y sin hallazgos; reescribirlos ahora para «aprovechar» C33 sería meter mano a
  una semana entera de trabajo ajeno por una mejora que la voz ya aplica sola.

---

## Dos avisos de procedimiento sobre lo de hoy

**1 · `voz.py` lleva hoy dos cambios, y eso hay que justificarlo.** La regla 11.1 —un cambio
por producción— sigue en pie fuera de presentación. Los dos entran por motivos distintos y
ninguno se apoya en el otro:

- **C33 es un arreglo de defecto**, del defecto que la dirección reportó esta mañana. Los
  arreglos de defecto nunca han consumido ranura, y eso quedó escrito el 7 de septiembre.
- **La pieza C de C27 no toca el camino de los Shorts.** Es un `elif` para formato «largo»,
  y el único vídeo que se produce antes de que volvamos a hablar es un Short. Sobre el
  largo solo puede mejorar: coge de caché lo que haya y, si no hay nada, hace exactamente lo
  que hacía ayer. **No existe un resultado peor que el de hoy.**

Verificado antes de entregar, con dobles en lugar de la API y sin gastar cuota: un Short
hace seis llamadas en vivo con el modelo 3.1 y todas dirigidas; un largo sin precacheo hace
**cero** llamadas y cae entero a `edge`; y un largo precacheado por `voz_precache.py` hace
cero llamadas **y encuentra las seis escenas en la caché** — que era la pieza que faltaba
por comprobar, porque si la clave no casa el fallo es silencioso.

**2 · Cuidado mañana con `voz.py`, que es de la revisión diaria.** `03_produccion/` es suya
según `PROPIEDAD_DE_FICHEROS.md`, y hoy he escrito yo en su fichero — cosa que la
autorización general del 07/09 me permite, pero que abre exactamente la ventana del 21 de
agosto: si el codirector no ha hecho `push` antes de que la revisión diaria clone
`origin/main`, ella trabajará sobre un `voz.py` sin C33 y lo pisará entero al entregar.

**La red que lo impide ya existe y es la primera acción de su prompt:** `git log --oneline
-5` sobre `origin/main`, y si el último commit no incluye el trabajo que esperaba encontrar,
no se toca nada del calendario y se dice en el resumen. Aquí lo que tiene que encontrar es
un commit del 14/09 con `voz.py` dentro. **Si no lo encuentra, no toca `voz.py` ese día.**
Su ranura de mañana es C31, que no está en ese fichero, así que no pierde nada esperando.

---

# Versión 9 · 15 de septiembre de 2026 — un vídeo, una voz; y los guiones de la semana, cosidos

Todo lo anterior sigue vigente salvo lo que esta sección corrige expresamente. No es una
sesión de lunes ni de viernes: es la de «algo se ha roto», convocada por el codirector el
martes por la mañana con dos noticias.

**La buena: `MDS-016` es el primer Short del canal que pasa de 1.000 visualizaciones.** Lo
dice el codirector desde YouTube Studio; `metricas.json` no lo recoge todavía (la foto es del
lunes a las 08:48 UTC y el vídeo se publicó a las 19:00). La mediana de los quince anteriores
es 10 y ninguno había llegado a 50, así que esto es un cambio de escala. **No se sabe todavía
por qué**, y hay al menos cuatro candidatos que no se pueden separar con un solo vídeo: el
primer Short con voz de Gemini, una situación de casa con un remate que escala («ahora somos
doce»), una pregunta con mucha demanda medida (9 millones en el top 10) y el azar del feed.
**La lectura del lunes 21 tiene que abrir por aquí**: fuentes de tráfico de `MDS-016` y su
curva de retención comparada con la de `MDS-015`. Hasta entonces, lo único que se hace con
este dato es **no romper lo que tenía ese vídeo**, que es lo que motiva el resto de esta
versión.

**La mala: `MDS-017` se publicó con dos voces alternándose y con un guion que no se podía
seguir.** Palabras del codirector: *«mezcla las dos voces y resulta inconexo […] carente de
ritmo y sincronía, hasta el punto de que cuesta trabajo seguir el hilo»*, y *«no entiendo el
guion, mezcla lo de los dedos en el aire, lo de las cosquillas y lo del mando a distancia del
principio»*.

## Qué se anula, qué se mantiene y qué se amplía

| Documento o decisión | Estado desde hoy |
|---|---|
| C7 · salvaguarda 1: «respaldo automático e inmediato a `edge-tts` ante cualquier fallo de Gemini **en una escena**» | **ANULADA.** Sustituida por C33.1 |
| C27 · pieza C: «el largo coge de la caché lo que haya y lo que falte sale con `edge-tts`, escena a escena» | **ANULADA.** Sustituida por C33.1 (el largo tampoco se mezcla nunca) |
| Versión 8, «Los guiones de esta semana no se tocan» | **ANULADA** para `MDS-017` a `MDS-020`, reescritos hoy. Se mantiene para `MDH-007` |
| C33 · la dirección de actor por escena | **SE MANTIENE**, con una corrección: un `titulo` que no es la escena 1 ya no se dirige como «apertura» |
| C27 · `voz_adelantada.yml` y `voz_precache.py` | **SE MANTIENEN**, con tope de tres fallos por ejecución y la clasificación de errores de C33.1 |
| C34 y C35 (imagen y densidad) | **SE MANTIENEN** sin cambios; ver abajo lo que ha contestado el codirector |
| C7 · una llamada por escena | **SE MANTIENE por ahora.** C36 propone sustituirla, con prueba antes |
| `guionista_corto.md` (las tres pruebas de cosido) | **SE MANTIENE**. Se amplía el prompt de la planificación con dos reglas (abajo) |

---

## C33.1 · Un vídeo, una voz. Nunca mezclada

**Hecho hoy en `03_produccion/pipeline/voz.py`. Probado con dobles de la API, sin gastar cuota.**

### Lo que pasó, medido

`05_calendario/qa/MDS-017.es/ficha.json`: `"motores_por_escena": {"edge (respaldo)": 3,
"gemini": 3}`. Nadie lo decidió. El código de C7 mandaba **cada escena por separado** a
`edge-tts` en cuanto su llamada a Gemini fallaba, por el motivo que fuera, y seguía con la
siguiente. Es exactamente lo que el codirector había descartado para el largo el 7 de
septiembre («una chapuza»), y la regla se había escrito solo para el largo. **Tenía que haber
valido para los dos formatos desde el principio: fue un error mío.**

No hay forma de saber desde aquí cuál fue el fallo de cada escena: los registros de Actions
piden credenciales. Lo que sí se sabe es que el código tenía **tres defectos**, y los tres
explican el resultado solos o juntos:

1. **Ni un reintento.** La documentación de Google lo dice sin rodeos: los modelos TTS
   devuelven a veces texto en lugar de audio y el servidor responde con un 500, «de forma
   aleatoria en un pequeño porcentaje de peticiones», y hay que reintentar. Aquí un 500 era
   respaldo inmediato.
2. **La cuota diaria no se reconocía nunca.** Google la escribe «`per_model_per_day`» o
   «`PerDay`», y el código buscaba «per day» o «perday» quitando solo los espacios. Con la
   cuota agotada se seguía llamando escena tras escena, con 25 s de espera cada vez.
3. **El respaldo era por escena.** Con eso, cualquier fallo suelto producía un vídeo mezclado.

Y un cuarto, que no pasó pero habría pasado el sábado: **`MDH-007` tiene 41 escenas** y el
precacheo de martes a viernes da como mucho 36. Con el código de ayer, el episodio habría
salido con cinco escenas en `edge-tts` y treinta y seis en Gemini.

### El arreglo

**Una escalera por vídeo, no por escena:**

| Escalón | Qué hace |
|---|---|
| a | El vídeo **entero** con `gemini-3.1-flash-tts-preview`. Primero mira la caché. Cada escena tiene **tres intentos**: un 429 por minuto espera 65 s, un 500 o una respuesta sin audio espera lo normal, y el tercer intento va con una dirección mínima, por si lo que falla es el clasificador de Google que decide si el texto es una petición de voz |
| b | Si una sola escena no sale, el vídeo **entero** otra vez con `gemini-2.5-flash-preview-tts`, que tiene su propia cuota de 10 al día (el panel del codirector del 14/09 lo confirma: `Gemini 2.5 Flash TTS · 0/3 · 0/10`). Lo hecho con 3.1 queda en la caché para otro día |
| c | Si tampoco sale y **todavía no se ha reiniciado la cuota** (un cron de antes de las 08:00 UTC), el paso **falla sin subir nada**. La cuota de Google se reinicia a medianoche de California (07:00 UTC en verano, 08:00 en invierno), así que el cron de las 08:23 UTC vuelve a intentarlo con la cuota llena y solo pide lo que falta |
| d | Solo en ese último intento, el vídeo **entero** con `edge-tts`. En una ejecución manual este escalón no existe: el paso falla y decide el codirector |

**El largo sigue la misma escalera con un único modelo**, el 2.5 de su caché: lo precacheado
se recoge y lo que falte se pide en vivo. Para `MDH-007` eso significa que el sábado a las
01:13 UTC faltarán unas cinco escenas y la cuota del viernes estará casi gastada; el paso
fallará, y a las 08:23 UTC pedirá las cinco con la cuota nueva. El episodio se publica a las
12:00: hay margen, pero poco, y por eso la tarea 2 de hoy le pide al codirector una línea en
`producir.yml`.

**Una comprobación nueva que cubre la otra limitación documentada.** Google avisa de que, con
un prompt ambiguo, el modelo puede **leer en voz alta las instrucciones de dirección**. Nada
lo detectaba. `_audio_plausible()` rechaza una toma cuya duración no puede corresponder al
texto (más de 5 palabras por segundo, o menos de 1,1 con 1,5 s de margen): las instrucciones
son diez veces más largas que la narración, así que no pasa.

**Y lo que ve el expediente.** `ficha.json` lleva ahora `modelo_voz` (quién puso la voz del
vídeo), **`voz_mezclada` (tiene que ser `false` siempre)**, `origen_voz` por escena (caché,
llamada o dirección mínima) y `direccion_voz` por escena (el papel de C33). Lo último estaba
prometido el 14/09 y no estaba: `qa.py` no lo copiaba.

### Las pruebas, con dobles de la API

Doce casos en `/tmp` (no quedan en el repositorio), los doce en verde:

1. Todo bien: seis llamadas, un modelo.
2. Un 500, una respuesta vacía y un 429 por minuto: nueve llamadas, un modelo, ninguna escena
   en `edge-tts`.
3. La cuota de 3.1 se acaba en la escena 4: el vídeo entero sale con 2.5.
4. Las dos cuotas agotadas en el cron de las 01:13: código 3, nada subido.
5. Las dos agotadas en el último intento: el vídeo entero en `edge-tts`.
6. Las dos agotadas en una ejecución manual: código 3, nunca `edge-tts`.
7. El modelo lee las instrucciones dos veces: el tercer intento sale con la dirección mínima.
8. Una escena imposible con 3.1: el vídeo entero con 2.5.
9. **El reintento del cron con caché**: la primera pasada deja cuatro escenas y falla; la
   segunda solo hace **dos** llamadas.
10. **El largo con 36 escenas precacheadas**: a las 01:13 falla; a las 08:23 hace **cuatro**
    llamadas y sale entero en 2.5.
11. El precacheo con la API caída se para al tercer fallo (antes intentaba las 41).
12. La clasificación de los cinco mensajes de error reales.

**Lo que no se ha podido probar desde aquí**: una llamada real. La interfaz con la API
(`_gemini_pcm`) no se ha tocado, y es la misma con la que salió `MDS-016` con seis de seis.

### La corrección de C33 que ha salido al probar el largo

`_papel_escena()` convertía en «apertura» cualquier escena de tipo `titulo`, y la apertura le
dice al actor «es la primera frase del vídeo, entras en frío». `MDH-007` tiene **seis** escenas
así en mitad del episodio. Ahora son «sección»: *pasa página, con algo más de energía que la
frase anterior, sin anunciarlo como un locutor.* El precacheo de hoy (09:00 UTC) todavía usa la
dirección vieja, así que esas escenas se volverán a pedir; es una, como mucho dos, de las nueve
de hoy.

---

## Los guiones de esta semana: se reescriben los cuatro Shorts que quedan

**La versión 8 decía que no se tocaban.** Era una decisión razonable con lo que se sabía el
lunes —«están validados y sin hallazgos»— y hoy se sabe que **validados y sin hallazgos no
significa bien escritos**: son de la planificación del jueves 10, dos días antes de las tres
pruebas de cosido. El codirector ha tenido que ver uno publicado para decirlo. No tiene que ver
los otros tres.

Leídos los cuatro contra las tres pruebas, fallaban los cuatro, y uno tenía además **un error
de la regla 2**:

| Guion | Qué fallaba | Qué se ha hecho |
|---|---|---|
| `MDS-017` (hoy) | Tres sujetos: el sobrino y el mando, los dedos en el aire, las ratas. Y un cierre que decía que a la rata «no le hizo gracia» después de haber dicho que se reía | **Un solo sujeto: las ratas de Panksepp.** El científico que se pasa años haciéndoles cosquillas, las ratas que aprenden a apretar una palanca para que siga, el chillido de 50 kHz, y el cierre honesto de los propios autores: lo subjetivo no se mide, se infiere |
| `MDS-018` (mié) | El profesor de latín desaparecía en la escena 3; entraba «el error de Napoleón» y no se explicaba nunca | El profesor de latín de principio a fin. El chiste suyo no iba de latín: «me sé el chiste entero y ni una declinación». Serie cambiada a «Ríete primero»: `G06` es una revisión, no un experimento |
| `MDS-019` (jue) | Abría con la sintonía de un banco (una sintonía no es humor). Y **afirmaba que el humor «mejora cómo te cae quien lo usa»**, cuando el resumen de Eisend dice literalmente que no hay evidencia de eso y que **reduce** la credibilidad | Un anuncio que te hacía llorar de risa y no sabes qué vendía. El dato bueno: el humor le da **al anuncio el doble de efecto que a la marca**. El cierre: el propio Eisend avisa de que la investigación está algo sesgada |
| `MDS-020` (vie) | Tres cosas (los gatos, los veinte cómicos, el examen del New Yorker) y los cómicos sin veredicto | Los gatos y los veinte cómicos, con su veredicto literal: *«material de crucero de los años cincuenta, pero algo menos racista»*. El cierre de la versión del jueves se queda: este guion lo ha escrito una máquina |

**Todas las afirmaciones se han comprobado hoy contra el texto o el resumen de cada artículo**,
y la frase de origen está copiada en `notas_humor` de cada guion. Tres fichas de la
bibliografía estaban mal y se han corregido: `E06` (el título no era el del artículo), `G05`
(otro título, otra revista y otro DOI) y `G06` (es una revisión, no un metaanálisis).

Los cuatro pasan `validar_guion.py` sin errores ni avisos y la barrera de C21 con las fuentes
reales; `MDS-017` además se ha renderizado entero. Sus cuatro ficheros de
`05_calendario/publicaciones/` (título, descripción, etiquetas, primer comentario) se han
reescrito con ellos: la descripción de `MDS-017` seguía hablando del sobrino y del mando.

### Y la causa, para que el jueves 17 no se repita

Dos reglas nuevas en `00_estrategia/tareas/planificacion-jueves.md`, en «Criterio editorial»:

1. **Lo que un estudio encontró se copia, no se deduce.** Muchas fichas de la bibliografía son
   de una línea y no dicen el resultado. Un resultado en un guion tiene que estar en la ficha
   o en el resumen leído en esa ejecución, con la frase copiada en `notas_humor`.
2. **Una referencia que se nombra se explica en el mismo Short, o no se nombra.**

---

## Lo que ha contestado el codirector a las tareas del 14

- **Cuota de imagen: no hay.** Todos los modelos de imagen del panel (Nano Banana, Nano Banana
  Pro, Nano Banana 2 y 2 Lite, Veo) están a `0/0`. **La vía 3 de C34 (generar las imágenes
  nosotros) se cae**, como estaba previsto que pasara si la cuota no existía. Las vías 1 y 2
  (el lote y el banco con licencia) siguen igual.
- **Tratamiento elegido en el muestrario: el 1, duotono ámbar.** *«Por acercarse a los colores
  del canal. De todas formas, vamos probando así y vemos más adelante si encaja o no.»* Con eso
  C34 tiene lo que necesitaba para escribirse en `escena.html`. **No entra hoy**: hoy solo se
  arregla lo roto, y la imagen merece su propia sesión y su propio muestrario (regla 11.2). Va
  el viernes 18.
- **Las fotos del banco son de Pixabay, cuya licencia no exige atribución.** Está bien, y no hay
  que buscarlas otra vez. Lo que la regla 9 pide no es atribuir en el vídeo: es **poder
  demostrar de dónde salió cada imagen** si un día alguien reclama. Pixabay ha tenido casos de
  fotos subidas por quien no era su autor, y lo único que nos cubre ahí es el enlace. Por eso se
  le pide al codirector solo el enlace de cada foto (tarea 4 de hoy), sin buscar ninguna otra.
- **El panel, además, dice algo que no se había preguntado**: los modelos de la Live API
  (`Gemini 2.5 Flash Native Audio Dialog`, `Gemini 3 Flash Live`) tienen peticiones diarias
  **ilimitadas**. Es la base de la opción C de C37.

---

## C36 · Una llamada por vídeo, con el corte por palabras (propuesta; se prueba antes)

**El problema de fondo, que C33.1 no resuelve:** con una llamada por escena, un Short gasta
seis de las diez peticiones diarias, cualquier repetición se come la cuota de la noche
siguiente, un largo de 41 escenas no cabe ni en cuatro días, y cada escena es una toma
independiente — C33 le devuelve a mano el contexto, pero sigue siendo un montaje de seis
tomas.

**La idea:** el Short entero en **una sola llamada** (y el largo en tandas de cinco o seis
escenas), y cortar el audio por escenas después.

**Por qué no se hizo así el 4 de septiembre, y qué cambia ahora.** Se probó y se descartó
**el corte por silencios**: 16 y 33 tramos para 6 escenas, y ningún umbral daba 6. Esa
conclusión se mantiene. **C36 no corta por silencios: corta por palabras.** Un reconocedor de
voz local (`faster-whisper`, gratuito, en CPU, dentro de Actions) devuelve cada palabra con su
instante; como el texto de cada escena se conoce, la frontera entre la escena *k* y la *k+1*
es el hueco entre la última palabra de una y la primera de la otra, y se corta en el silencio
más profundo de ese hueco. De paso, se gana algo que hoy no existe: **una comprobación de que
la voz dice lo que pone el guion**, palabra por palabra.

**Lo que cambiaría:** un Short pasa de 6 peticiones a 1 o 2; un largo, de 41 a unas 8, **en un
solo día y sin precacheo**; y la voz sale de una sola toma, que es lo que de verdad cose.

**Lo que hay que probar antes de encender nada**, con `voz_prueba.yml` y sin tocar la
producción: que el corte por palabras acierta las seis fronteras en tres Shorts reales; que el
desfase de sincronía se queda por debajo de 0,5 s (el umbral de `qa.py`); que una tanda de seis
escenas no deriva (Google avisa de que la calidad cae en salidas de varios minutos); y cuánto
tarda el reconocedor en CPU. **Si falla cualquiera de las cuatro, C36 se descarta y se queda
C33.1**, que ya funciona.

**Cuándo:** se escribe en la sesión del viernes 18 y se prueba ese mismo día. No entra en
producción antes del lunes 21, y solo con las cuatro pruebas en verde.

---

## C37 · Un motor de voz sin cuota, por si Gemini falla (investigación, sin fecha)

El codirector preguntó hoy si otros modelos, de otras compañías, harían un trabajo decente
gratis. Lo mirado hoy:

| Opción | Veredicto |
|---|---|
| **Gemini 2.5 Flash TTS** | **Entra hoy**, como escalón b de C33.1. Cuota propia, mismas voces |
| Google Cloud Text-to-Speech, Azure Speech | **Descartadas**: exigen una cuenta de facturación con tarjeta. Aunque tengan tramo gratuito, la regla 4 no admite un servicio que puede cobrar |
| ElevenLabs (plan gratuito) | **Descartada**: uso no comercial, atribución obligatoria y unos diez minutos al mes; un mes de Shorts son veinticinco |
| XTTS-v2, Fish Audio S2, Higgs Audio | **Descartadas**: licencias no comerciales |
| **Qwen3-TTS** (Alibaba, Apache 2.0, español incluido) | **Candidata.** Pesos abiertos, se ejecuta en el runner de Actions sin cuota. Sus voces de serie no son hispanohablantes; la variante *VoiceDesign* crea una voz a partir de una descripción, sin clonar a nadie (regla 6). En CPU va lenta |
| **Chatterbox Multilingual** (MIT, 23 idiomas con español) | **Candidata**, mismo planteamiento |
| **VoxCPM2** (Apache 2.0, 30 idiomas, pesos GGUF para CPU) | **Candidata**, la más ligera de las tres |
| Kokoro (Apache 2.0) | Muy ligera, pero el español no es su fuerte |
| **Opción C · la Live API de Gemini** (peticiones diarias ilimitadas en el panel del codirector) | **Candidata, con reservas.** Es un modelo de conversación, no de lectura: hay que comprobar que dice el texto tal cual. La comprobación palabra por palabra de C36 es justo lo que haría falta para fiarse |

**La prueba, cuando toque:** un workflow manual que locute el mismo guion con las tres
candidatas locales y con la Live API, y deje los audios para que el codirector los escuche.
**No tiene fecha**: solo sube de prioridad si Gemini empieza a fallar más de lo que la escalera
de C33.1 aguanta, o si C36 se descarta.

---

## Lo que NO cambia hoy

- El punto de control sigue siendo el **27 de septiembre** y la decisión, el **15 de
  noviembre** (C26).
- **La regla 11.1 sigue suspendida** para presentación hasta el 27. C33.1 es un arreglo de
  defecto y no consume ranura; la reescritura de guiones no es un cambio de código.
- **`MDH-007` no se toca.** Tiene dos notas pendientes en `revisiones/` (escenas 19 y 31, las
  dos de la regla 2) que aplica la planificación del jueves 17, antes de su emisión.
- **C34 no entra hasta el viernes 18.**
- No se clona la voz de nadie, no se encienden los subtítulos quemados y
  `.github/workflows/` sigue sin escribirse en remoto.

---

# Versión 9.1 · 15 de septiembre, tarde — el primer intento, leído (C33.2)

La versión 9 se escribió por la mañana. A media mañana el codirector volvió a producir
`MDS-017` a mano con C33.1 ya subido, y el paso de voz falló. **Sin subir nada, que es lo que
tenía que pasar.** Pero el registro que copió en `PROMPT_DIRECCIÓN.md` enseña tres cosas que la
versión 9 no sabía, y las tres cambian el diseño.

## Qué dice el registro

| Modelo | Peticiones | Qué pasó |
|---|---|---|
| 3.1 | 11 | Escenas 1 y 2 bien. **Escenas 3, 4 y 5 rechazadas dos veces cada una con un 400** («Request contains an invalid argument»), siempre con la dirección completa. La 3 y la 4 salen al tercer intento, con la dirección mínima. La petición 11 da 429 |
| 2.5 | 10 | Escenas 1 a 4 bien, con **dos cortes de conexión** y un 429 por medio. La escena 5 da 429 tres veces, con un minuto de espera entre ellas |

**1 · La dirección de actor v1 se rechaza, y los rechazos gastan cuota.** Seis rechazos de
seis con la dirección larga y dos aceptaciones de dos con la mínima, sobre los mismos
textos. Y la petición 11 de 3.1 dio 429 justo cuando 4 aciertos y 6 rechazos sumaban las 10
del día: **un 400 cuenta como petición.**

**2 · La librería reintentaba por su cuenta, en silencio.** `google-genai` 2.x reintenta los
408, 409, 429, los 5xx y los cortes de conexión **hasta cuatro veces en unos tres segundos**
por cada llamada nuestra. Medido hoy con un transporte simulado: un 429 son 4 peticiones en
3,3 s. Con un límite de 3 por minuto y 10 al día, **eso explica los 429 «por minuto» del 14 y
del 15, el «4/3 RPM» del panel del codirector, y que 2.5 se agotara con solo cuatro escenas
hechas**: cada corte de conexión fueron probablemente cuatro peticiones.

**3 · El 429 de esta API no dice de qué límite es.** «You exceeded your current quota» y
nada más: ni «per day» ni «per minute». C33.1 lo tomaba siempre por el del minuto.

**Y la hipótesis del codirector** —que 2.5 falló por compartir cuota con 3.1— **no se
sostiene**: son cuotas separadas (su propio panel del 14 lo enseña). Lo que 2.5 sí compartía
era el daño de los reintentos ocultos.

## C33.2 · Lo que cambia

1. **Cliente sin reintentos propios** (`_gemini_cliente`): `attempts=0` más un cerrojo de
   códigos. Comprobado: un 429, un 500, un 503 y un corte de conexión son ahora **una**
   petición cada uno. Los reintentos los decide `_gemini_escena`.
2. **Dirección de actor v2**, con la estructura que recomienda Google y que ya había
   funcionado hoy: empieza pidiendo en claro que se lea en voz alta, luego las notas y luego
   `TEXTO:`. Es la mínima con las notas dentro.
3. **Un rechazo no se repite.** El siguiente intento va con la mínima. **Tras dos rechazos en
   un vídeo, el resto del vídeo va con la mínima desde el principio.** Con el caso de hoy eso
   son 8 peticiones para las seis escenas, no 11 para cuatro (probado con un doble que
   rechaza exactamente las escenas 3, 4 y 5).
4. **Un 429 sin apellido** espera un minuto y se reintenta. **Si vuelve a salir, es el límite
   diario** y el modelo se abandona.
5. **Tope de 10 peticiones por modelo en una producción.** La once no puede salir.
6. **31 s entre llamadas** en vez de 25.
7. **La clave de caché ya no depende de la redacción de la dirección**, sino de su firma:
   versión, papel, qué pasa al terminar y de dónde viene. Para invalidar a propósito, se sube
   `VERSION_DIRECCION`. **Las ocho tomas de hoy se siguen encontrando** con la clave vieja: la
   función v1 queda congelada solo para buscarlas.
8. **`edge-tts` no entra nunca solo.** Palabras del codirector, con `MDS-017` sin voz: *«Mejor
   eso que colocar el vídeo con la voz edge-tts»*. Se retira el escalón d de C33.1. Sin voz de
   Gemini para el vídeo entero no se sube nada, a ninguna hora. La única puerta es
   `VOZ_PERMITIR_EDGE=1`, a mano, y ningún workflow la pone.
9. **`voz_precache.py`** usa la misma lógica que `voz.py`, **cuenta peticiones y no escenas**,
   y precachea siempre **el largo pendiente más cercano de la parrilla**, sea el que le pasen
   o no (ver abajo por qué).

Veintiún casos con dobles de la API, todos en verde: los de la versión 9 adaptados (el de
«`edge-tts` en el último intento» ahora comprueba que NO entra) y ocho nuevos. Entre ellas el caso real de hoy, el 429 sin apellido suelto y repetido, la
caché con claves v1, el cliente sin reintentos y el precacheo con rechazos.

## El calendario de esta semana: se cambian el sábado y el domingo

**`MDS-017` no se publica hoy.** Lo decidió el codirector, y es lo correcto. Propuso publicarlo
el domingo; **va el sábado 19 a las 19:00**, y el episodio largo pasa al **domingo 20 a las
12:00**. El motivo es aritmético:

- `MDH-007` tiene 41 escenas. El precacheo de miércoles a viernes da como mucho 27 peticiones,
  y el sábado de madrugada queda 1 de la cuota del viernes. Con las 10 del sábado a las 08:23
  UTC se llega a 38. **Sin mezclar voces no llega al sábado.**
- El domingo, en cambio, tiene la cuota entera del sábado a las 01:13 UTC y la del domingo a
  las 08:23 UTC: 27 + 10 + 10 = 47 peticiones para 41 escenas, más las dos que cambiará la
  planificación el jueves al aplicar sus notas. El margen es corto: si la dirección v2 se
  rechaza a menudo, puede no llegar. En ese caso el largo no sale y se vuelve a mover.
- `MDS-017` necesita 2 peticiones (las escenas 1 a 4 ya están en la caché), y el sábado a las
  01:13 UTC tiene la cuota de 3.1 del viernes casi libre.

**Dos piezas nuevas para que el cambio funcione solo:**

- **`parrilla.json` · `rehacer_video_id`.** El registro sigue diciendo que `MDS-017` está
  subido (`9H2xEZnFeHA`, el vídeo de las dos voces, que el codirector ya ha borrado). Sin esto,
  los tres crons del sábado lo darían por hecho. `cola.py` ignora esa subida concreta. En cuanto
  llega la nueva, el registro cambia de identificador y la idempotencia vuelve a funcionar.
- **`voz_precache.py` · el largo más cercano.** `voz_adelantada.yml` le pasa el guion del
  próximo sábado, y el sábado 19 lleva un Short. Ahora precachea el largo pendiente más
  cercano de la parrilla (`MDH-007`) y, si le sobra presupuesto, el siguiente.

**Y un cambio de workflow recomendado, sin prisa (tarea del codirector):** que
`voz_adelantada.yml` corra **todos los días** y no solo de martes a viernes. Esta semana no
cambia nada: lo que precachea el sábado se lo quita a la producción del domingo de madrugada,
que usa la misma cuota. Pero desde la semana que viene el largo tendrá siete días en vez de
cuatro para llenarse, y dejará de ir justo.

## La cascada de madrugada, que va a pasar y no es una avería

Hoy se han gastado las dos cuotas del día de California. Esta noche, `MDS-018` fallará a las
03:13 y a las 06:47 sin subir nada, y **saldrá a las 10:23** con la cuota nueva. Esa
producción gasta parte de la cuota que usa la madrugada siguiente, así que durante unos días
es probable que alguna producción vuelva a salir a las 10:23 en vez de a las 03:13. Se corrige
sola en cuanto una producción de la mañana gasta poco. **La publicación de las 19:00 no está
en riesgo.**

## Lo que queda para el viernes 18, además de lo que ya estaba

- Leer las fichas de `MDS-018` a `MDS-020`: cuántas escenas salieron con la dirección v2 y
  cuántas con la mínima (`origen_voz`). **Si la v2 se rechaza tanto como la v1, se pasa a la
  mínima para todo** y la dirección por papel se replantea.
- Contar en `cache_voz/` cuántas escenas de `MDH-007` hay de verdad antes del domingo.
- C36 (una llamada por vídeo) gana urgencia: con rechazos que cuestan cuota, una llamada por
  vídeo es también un solo rechazo posible por vídeo.

---

# Versión 10 · 18 de septiembre de 2026 — el reloj del Short

Sesión de viernes: revisar lo que la planificación escribió el jueves. Se ha convertido en
otra cosa porque la dirección trajo el mismo aviso dos días seguidos, y al ir a mirarlo
aparece medido.

**Lo que dijo el codirector.** El 16/09: *«me sigue costando entender el hilo del short. No me
convence mucho la narrativa de cada short y tenemos que trabajar en ella para mejorarla, y que
el inicio, nudo y desenlace estén mucho mejor hilvanados.»* El 17/09: *«me sigue pareciendo un
poco forzado el guion entre el nudo y el desenlace.»* Los dos vídeos —`MDS-018` y `MDS-019`—
son de los cuatro que se reescribieron el 15/09 contra las tres pruebas de cosido. **Las
pruebas funcionaron y el problema sigue**, que es la señal de que estaban midiendo otra cosa.

**Y los números, que esta semana por fin se mueven:** `MDS-016` **1.280 visualizaciones**,
`MDS-019` **182** y `MDS-018` por encima de 100. Contra una mediana de 10 en los quince
anteriores y cero por encima de 50. Sigue sin haber suscriptores y sigue sin ser rentable,
pero por primera vez hay dos vídeos consecutivos por encima del umbral que el propio codirector
puso como condición de supervivencia.

---

## Lo que se anula, lo que se mantiene y lo que se amplía

| Documento o decisión | Estado desde hoy |
|---|---|
| Regla 13 · «En un Short, una [risa], y va primero» | **AMPLIADA** por la regla 13.2: el remate no cae antes del segundo 10, y el Short se escribe a la duración de su serie |
| `guionista_corto.md` · «entre 18 y 55 segundos» | **ANULADO como objetivo.** 55 s sigue siendo el techo del formato; el objetivo pasa a ser la duración de la serie ±12 % (prueba 4) |
| Duración de «Ríete primero, te explico después» (30 s) y de «Esto no tiene gracia y esto sí» (35 s) | **CORREGIDAS** a 35 s y 40 s. Razón abajo |
| `validar_guion.py` · `PPM = 150` | **ANULADO.** Pasa a 130, medido sobre los seis Shorts con expediente de calidad |
| Regla 13.1 · «una risa escrita en el guion sigue permitida» | **SE MANTIENE**, y desde hoy **se puede ejercer**: `voz.py` la vetaba en todas las escenas sin excepción (C38.1) |
| Versión 9 · los cuatro Shorts reescritos el 15/09 | **SE MANTIENEN** tal cual. `MDS-017` va exento de C38 (se publica mañana, ya renderizado) |
| C34 (imagen, duotono ámbar), señalado para hoy | **APLAZADO al lunes 21.** Sigue bloqueado por el enlace de origen de cada foto del banco, pedido el 15/09 y sin contestar. Y hoy la cola es otra |
| C36 (una llamada por vídeo), a probar hoy | **APLAZADO al lunes 21.** Sin diseño escrito, y la dirección v2 no se está rechazando (0 de 18 escenas con dirección mínima), así que la urgencia bajó |
| C13 · TikTok e Instagram, «solo si se pasa el peldaño 1» | **REABIERTO.** Se empieza el trámite hoy; ver C41 |
| C26 · la decisión del 15 de noviembre | **SE MANTIENE** sin cambios. Y el punto de control del **27 de septiembre**, también |

---

## C38 · El Short se escribe a un reloj, y el remate cae en el segundo doce

**Hecho hoy.** `04_agentes/validar_guion.py`, `04_agentes/prompts/guionista_corto.md`,
`04_agentes/esquema_guion.json`, `00_estrategia/REGLAS.md` (regla 13.2) y los cinco guiones de
la semana del 21.

### Lo medido, que es todo el argumento

Cada serie declara una duración desde agosto: 30, 35, 40 o 45 segundos. **Los veinticinco
Shorts del repositorio tienen entre 88 y 120 palabras, con una media de 108.** Las seis de
«Ríete primero, te explico después» —serie de 30 segundos— tienen 101, 103, 106, 111, 111 y
113 palabras. El exceso sobre lo declarado va del 8 % al 98 %, y el patrón es exacto: cuanto
más corta dice ser la serie, más se pasa.

**Lo constante no es la serie: son las 108 palabras**, que es lo que cabe justo por debajo del
techo del formato. Es decir, **el máximo se ha usado como objetivo**, y lo que rellena la
diferencia es explicación entre el remate y el cierre honesto. Eso es exactamente lo que se ve
desde fuera como «forzado entre el nudo y el desenlace»: entre los dos no hay historia, hay
metraje.

Es la **trampa 20** del proyecto —un mínimo escrito como suelo se usa como techo— vista por el
otro lado. Y es la **trampa 25** —una regla escrita para un formato no protege al otro—
cometida sobre la propia regla 13: el 12 de septiembre se corrigió su mitad del episodio largo,
que pasó de contar risas a medir distancias, y **la mitad del Short se quedó en «una, y va
primero»** seis días más.

### El segundo hallazgo, y es el que manda

La única curva de retención que tiene el canal dice que **la mitad de la audiencia se ha ido en
el segundo 13**, y goteando, no de golpe. Con eso delante, mira dónde cae el remate —la escena
que va detrás de la pausa de 1,2-1,5 s, que se detecta sola:

| | Remate en el segundo | Visualizaciones |
|---|---|---|
| **`MDS-016`** | **13** | **1.280** |
| `MDS-019` | 7 | 182 |
| `MDS-018` | 6 | >100 |
| `MDS-020` | 6 | — |

**`MDS-016` es el único vídeo del canal por encima de mil, y es el único que pone su mejor
momento donde la gente está decidiendo si se queda.** Los otros lo gastan en el segundo seis,
con todo el mundo todavía dentro, y a partir del trece no ofrecen nada. Es un cuarto candidato
para la pregunta abierta de la versión 9 —*por qué `MDS-016`*— y, a diferencia de los otros
tres, es el único sobre el que se puede actuar.

**Honestamente: esto es n = 1 para el éxito.** Lo que lo sostiene no es ese vídeo solo, sino
que apunta en la misma dirección que la curva de retención (fuga continua, no desplome
inicial) y que lo que se sabe del reparto de Shorts en 2026, donde la señal dominante es la
proporción vista y **un Short de 20 segundos visto entero vale más que uno de 60 visto a la
mitad**. Tres cosas distintas señalando al mismo sitio no son una prueba, pero son suficiente
para gastar una semana.

### Las dos reglas, las dos ERROR en `validar_guion.py`

1. **La duración de la serie, ±12 %.** Margen estrecho a propósito: con margen ancho se
   escribe al borde del margen, que es lo que ha pasado con el techo de 55 s durante
   veinticinco Shorts. Y el mensaje de error dice qué hacer, porque importa: *no recortes
   palabras aquí y allá; busca la escena que no hace avanzar nada entre el remate y el cierre
   y quítala entera.* Casi siempre la hay y casi siempre es la penúltima — la que repite con
   otras palabras lo que acaba de decir la anterior.
2. **El remate no cae antes del segundo 10.** Para eso el planteamiento ocupa **dos escenas y
   no una**, con la pausa detrás de la segunda. Que es, literalmente, la forma de `MDS-016`.

### Dos duraciones suben, y conviene decir por qué antes de que parezca que se mueve la portería

«Ríete primero» pasa de 30 a 35 s y «Esto no tiene gracia y esto sí» de 35 a 40. **Los números
de agosto se escribieron antes de que la regla 12 —cada vídeo termina diciendo dónde falla— se
extendiera a los Shorts.** Con el cierre honesto dentro, un Short de este canal tiene que meter
planteamiento (que ahora además llega al segundo 10), remate, el hallazgo con su fuente y el
«y aquí falla»: medido al escribir los cinco de la semana, eso no baja de unas 66 palabras ≈
35 s. **Un 30 aritméticamente imposible no es exigente: es un número que se ignora**, que es
justo lo que llevaba pasando. Un 35 que se cumple es más estricto.

### El estimador de duración, arreglado de paso

`PPM = 150` llevaba un mes escrito como pendiente. Medido hoy sobre los seis Shorts con
`duracion_final_s` en su expediente, descontando las pausas deterministas: 117, 126, 127, 141 y
141 ppm con Gemini (157 el de `edge-tts`). **Media 130.** Con 150, el validador daba 49 s para
un vídeo que salió de 58 (`MDS-016`): dejaba pasar por debajo del techo guiones que se
publicaban por encima. No acierta al segundo —la dispersión real es de ±10 %— pero deja de
mentir siempre en la misma dirección, que es lo único que le pide un techo.

### Una exención, escrita en el código y no en el guion

Las dos comprobaciones son ERROR y `producir.yml` para la producción con un error. De los
veinticuatro Shorts que las incumplen, **solo uno está pendiente de producirse: `MDS-017`,
mañana**. Reescribirlo la víspera cuesta sus peticiones de voz (perdería las cuatro escenas que
tiene en caché desde el 15/09), vuelve a meter mano a un guion ya revisado dos veces, y lo que
se gana dura un día. Va exento, y **la exención vive en `validar_guion.py`, no en el guion**:
conceder otra obliga a tocar el código, que es la fricción que le corresponde. Es la trampa 9
—una comprobación que puede parar algo tiene que mirar qué se lleva por delante— atendida antes
de que pasara y no después.

### Los cinco Shorts de la semana del 21, reescritos

Con una restricción autoimpuesta: **no entra ni una afirmación nueva.** Todo lo que dicen
estaba en la versión de la planificación del jueves 17, ya verificada contra el resumen de cada
artículo. Esta reescritura solo quita y recoloca.

| | Antes | Ahora | Remate |
|---|---|---|---|
| `MDS-021` · El experimento | 57 s · 109 pal. | **46 s · 85 pal.** | s. 9 → **s. 12** |
| `MDS-022` · Esto no tiene gracia y esto sí | 58 s · 112 pal. | **43 s · 79 pal.** | s. 6 → **s. 11** |
| `MDS-023` · Ríete primero | 58 s · 111 pal. | **39 s · 68 pal.** | s. 9 → **s. 11** |
| `MDS-024` · Esto no tiene gracia y esto sí | 55 s · 106 pal. | **45 s · 81 pal.** | s. 9 → **s. 12** |
| `MDS-025` · El experimento | 58 s · 111 pal. | **47 s · 89 pal.** | s. 10 → **s. 19** |

Los cinco pasan `validar_guion.py` sin errores ni avisos. Se ha corrido además **la barrera de
C21 escena por escena** (`comprobarDesbordes()` sobre las 29 escenas, con `pintar(t)` en el
estado asentado): cero problemas. Y el muestreo de geometría personaje/texto del 18/09: peor
hueco del lote 215 px, contra un umbral de 50. **Las dos comprobaciones llevan el mismo aviso
que puso la revisión diaria esta mañana: sin las tipografías de marca instaladas los píxeles no
son definitivos.** La revisión diaria de mañana y la del domingo las vuelven a pasar, y el
primero de los cinco no se produce hasta el lunes a las 01:13 UTC — el circuito llega a tiempo.

**`revisiones/MDS-025.md` queda aplicada** (la pantalla llamaba «grupo de control» al grupo que
veía los vídeos): la reescritura quita esa escena entera, así que el defecto desaparece por
construcción. **Hay que borrar la nota**, o la planificación del jueves 24 intentará aplicarla a
un guion que ya no la necesita. `revisiones/MDH-008.md` **no** se toca: es de un guion que no he
tocado y la aplica la planificación.

**Las descripciones de `publicaciones/` no se reescriben**, y esto es distinto del 15/09. Aquel
día describían otro vídeo; hoy describen el mismo, con algo más de detalle del que cabe en
cuarenta segundos, y todo lo que dicen está verificado. Una descripción más larga que el vídeo
no es un defecto: el `.srt` y la descripción son lo que hace encontrable la pieza.

---

## C38.1 · «Manda el guion»: la risa escrita deja de cercenarse

El codirector, el 16/09: *«me quiero asegurar de que si hay una risa en el guion no se cercene
de forma artificial. Lo que era artificial eran 3 o 4 risas en 40 segundos, pero si por guion
hay una o dos se pueden dejar (manda el guion).»*

Tenía razón y el código estaba mal. La regla 13.1 dice dos cosas —el narrador no se ríe, y
*una risa escrita en el guion es otra cosa y sigue permitida*— y `voz.py` solo obedecía la
primera: `NOTA_SIEMPRE` prohibía reírse en las seis escenas **sin excepción**. La segunda mitad
de la regla no tenía forma de ejercerse.

**Hoy no se estaba cercenando nada** —ningún guion del repositorio ha pedido una risa jamás,
comprobado sobre los veinticinco— pero un veto que no se puede levantar deja de ser dirección
de actor y pasa a ser una amputación. Y en cuanto el guionista empiece a escribir risas (que es
lo que C38 le pide para el centro del vídeo), se las habría comido en silencio.

- Se pide con `"risa": true` en la escena, y va **al final de esa narración**.
- **Una por Short como mucho**, y `validar_guion.py` da error si se pide en la escena 1, en el
  remate o en el cierre — los tres sitios que la propia regla 13.1 prohíbe. Es decir, solo cabe
  en el centro del vídeo: justo el tramo que C38 existe para llenar.

**Y una trampa cometida y corregida en la misma hora, que va al registro porque es útil.** La
primera versión metía `risa=0` en la firma de la caché de voz de todas las escenas. Eso cambia
la clave de las 49 tomas de `cache_voz/` — **entre ellas las 18 escenas de `MDH-007` que tienen
que llegar al domingo**. Es la trampa 24, literal. La firma solo cambia cuando `risa` está
encendida, y está comprobado corriendo la función real contra la caché real: **18 de 41, las
mismas que esta mañana.**

---

## C39 · La bibliografía: el fichero bueno es el que nadie estaba mirando

El codirector, hoy: *«Corregido F03, F04 y F05 en bibliografía»* y *«encárgate de que C05 y G03
solucionen sus erratas»*. C05 y G03 los había corregido ya la revisión diaria esta mañana. Al ir
a comprobarlo apareció algo peor.

**`BIBLIOGRAFIA_CURADA.md` es un fichero generado.** Su propia cabecera lo dice: *«No edites
este archivo a mano: edita el JSON y vuelve a ejecutar `scripts/generar_md.py`.»* Nadie lo ha
hecho nunca. Medido hoy, cinco fichas estaban corregidas en el `.md` y sin corregir en
`data/semillas.json`: `C05`, `E02`, `F04`, `F05` y `G03`.

**La próxima vez que alguien regenerara el `.md`, se perdían las cinco.** Sin un error, sin un
aviso, en un commit con pinta de rutina — y la única señal habría sido una ficha que vuelve a
estar mal semanas después. Es la trampa 4 con otra cara: **un fichero derivado que se edita a
mano miente sobre su origen hasta el día en que se vuelve a derivar.**

- **`04_agentes/validar_bibliografia.py`** (nuevo): compara ficha a ficha el `.md` contra el
  JSON —título, autores, año, DOI— y falla si difieren. Sin red, determinista. Sabe de la
  entrada de control (`A09`, que está en el JSON y no en el `.md` **a propósito**) y normaliza
  comillas y guiones tipográficos, porque una comprobación que señala ruido se deja de leer.
- **Sincronizadas al JSON las cuatro verificadas hoy contra la fuente**: `C05` y `G03` (la
  revisión diaria, con `WebFetch`), `F04` y `F05` (el codirector). **`E02` no se toca**: nadie
  ha comprobado cuál de sus dos DOI es el bueno, y elegir uno a ojo es inventarse un dato.
  Va a las tareas del codirector.
- **Lo que este script NO hace, y hay que decirlo:** no comprueba que el DOI exista ni que
  apunte al artículo que la ficha nombra. Eso hace falta —es lo que estaba roto en las
  cuatro— pero necesita salir a internet, y el proxy de egreso de estos contenedores rechaza
  `api.crossref.org` (comprobado hoy). Quien sí puede es la revisión diaria con `WebFetch`,
  que es como verificó C05, así que esa comprobación vive en su prompt y no en un script. **Una
  comprobación que no se puede ejecutar no es una comprobación: es una intención.**

### Y `F04`, corregida, ya no es una fuente de este canal

El título nuevo de `F04` es *Functional Brain Connectivity at Rest Changes After Working Memory
Training* (Jolles et al., 2013). Es un artículo real y es el que corresponde a ese DOI — y **es
un trabajo sobre entrenamiento de memoria de trabajo, que no tiene nada que ver con el humor.**
La ficha ya no está rota: está bien identificada y fuera del tema. El pilar F sigue igual de
bloqueado que ayer, solo que ahora se sabe por qué.

Eso convierte la petición del codirector —*«el corpus tiene que crecer»*— en un encargo
concreto en vez de un deseo: hacen falta dos fuentes de neurociencia del humor que sustituyan a
`F04` y `F05`, y con ellas se desbloquea **«qué le pasa a tu cerebro cuando te ríes»**: 91
millones de visualizaciones en el top 10 y cero de cinco respondiendo. Es la mejor pregunta
libre que le queda al canal.

### Cómo crece el corpus, y por qué no hay una tarea programada nueva

Quedan **unas doce fichas** que puedan ser fuente central de un Short. A cinco por semana, eso
son dos semanas y media: la planificación del **8 de octubre** es la primera que se queda sin
material. No es urgente esta semana y sí lo es este mes.

**No se crea un agente bibliotecario.** La planificación del jueves ya lee la bibliografía, ya
lee resúmenes de artículos, ya mide la demanda y ya sabe qué preguntas están sin respuesta: es
la única pieza del sistema que tiene delante las dos cosas que el codirector dice que deben
mandar —las métricas de nuestros vídeos y las búsquedas de YouTube— en el mismo momento. Un
agente nuevo necesitaría un workflow nuevo, que solo puede crear el codirector a mano, y
duplicaría ese contexto. **Se le añade el encargo a la planificación**, en
`00_estrategia/tareas/planificacion-jueves.md`, con la regla que evita repetir F04:

> **Una ficha se escribe desde el registro del artículo, nunca de memoria.** Se localiza el
> artículo, se copia de ahí el título, los autores, el año, la revista y el DOI, y se pega en
> `notas_humor` la frase del resumen que sostiene lo que la ficha promete. Una ficha cuyo DOI y
> cuyo título no se hayan visto juntos en la misma página no se escribe.

Y el disparador es un número, no un criterio: **cuando queden menos de quince fichas sin usar,
la planificación añade tres**, elegidas por hueco de demanda medido y no por volumen —que es lo
que el codirector señala que está funcionando— y priorizando los pilares bloqueados, hoy el F.

---

## C40 · El marketing gratuito: lo que dicen nuestros propios números

El codirector preguntó por opciones de marketing gratuitas que no le expongan y que no sean
spam, y dijo que le interesa el aprendizaje. El aprendizaje está en `metricas.json` y es
incómodo, así que va primero.

**De dónde vienen las visualizaciones de los Shorts, ponderado por visualizaciones, sobre los
quince con datos de tráfico:**

| Superficie | Cuota |
|---|---|
| Feed de Shorts | **54,6 %** |
| Búsqueda de YouTube | 27,7 % |
| Suscriptores | 6,9 % |
| **Todo lo externo junto** (`NO_LINK_OTHER`) | **5,4 %** |
| Página de canal · notificaciones · otras | 5,4 % |

**Todo lo que no es YouTube son catorce visualizaciones en dos meses.** Una campaña de marketing
externa que doblara esa cifra añadiría catorce visualizaciones. `MDS-016` hizo 1.280 él solo, y
`MDS-015` sacó el 96,8 % de las suyas del feed.

**El aprendizaje, dicho sin adornos: para un canal de Shorts sin audiencia, el marketing externo
no es una palanca pequeña, es ruido.** La palanca es el feed, y al feed no se le convence
publicando en ningún sitio: se le convence con la proporción de vídeo vista, que es la señal que
más pesa en 2026. Es decir, **C38 es la campaña de marketing**, y no hay una segunda.

Hay una corrección importante que esto obliga a hacer en `LEEME.md`: *«la única superficie que
responde es la búsqueda»* fue cierto en agosto —`MDS-002` y `MDS-006` sacaban de ahí el 63 % y
el 81 %— **y ha dejado de serlo**. Desde `MDS-007` manda el feed. La frase lleva tres semanas
escrita como si siguiera valiendo, y tiene consecuencias: es la que sostiene «la búsqueda es
difícil pero es lo que tenemos» y la que justificaba C10 (una página por episodio).

**Lo que sí vale la pena, y es una consecuencia de lo anterior, no una lista de tácticas:**

1. **Más superficies de feed, que es C41.** No es marketing: es el mismo vídeo en otro sitio
   donde manda el mismo mecanismo.
2. **La búsqueda sigue valiendo el 27,7 %, y es gratis.** El `.srt`, el título y la descripción
   ya se escriben bien. No hace falta nada nuevo.
3. **Lo que se descarta y por qué.** Reddit, foros y comentarios de otros canales: la regla 8
   los prohíbe automatizados, y a mano son trabajo recurrente para el codirector, que prohíbe
   la regla 5. Las dos reglas dicen lo mismo desde lados distintos y no hay hueco entre ellas.
4. **C10 (una página por episodio) sigue aplazado, y ahora con un motivo mejor**: llevaría
   tráfico externo a un canal cuyo tráfico externo es el 5,4 %.

---

## C41 · TikTok y Reels: no es marketing, es un segundo feed

El codirector, el 16/09: *«si ya estamos haciendo el trabajo de producir los vídeos, ¿no
podríamos automatizar también la subida de estos shorts a Tiktok y como reels de Instagram
[…] manteniendo Youtube como el canal principal?»*

**La pregunta está mejor planteada de lo que parece**, y los números de arriba son el porqué: el
feed es la única superficie que reparte sin audiencia previa, y TikTok e Instagram son dos feeds
más con exactamente el mismo mecanismo. El coste marginal de producción es **cero**: el fichero
ya existe, es vertical, no lleva marca de agua y es nuestro. La regla 8 lo autoriza
expresamente —*«las publicaciones automáticas en TikTok, Instagram, Bluesky y el pódcast son
contenido propio en canales propios; eso no es spam»*— y la 6 se cumple porque las cuentas son
de la marca.

### Lo que cuesta de verdad, comprobado hoy y no recordado

Ni TikTok ni Instagram dejan publicar en abierto desde una aplicación sin revisar:

| | Qué hace falta | Plazo | Coste |
|---|---|---|---|
| **TikTok** · Content Posting API | Cuenta de desarrollador, la app con el producto «Content Posting», los permisos `video.upload` y `video.publish`, verificación de dominio y **auditoría de la app**. Sin auditoría, lo que sube la API queda en **privado / solo para ti**: no lo ve nadie | días a semanas, con rechazos por incumplir las guías de interfaz | 0 € |
| **Instagram** · publicación de Reels | Cuenta **de empresa** (las de creador no valen), `instagram_business_basic` e `instagram_business_content_publish`, **cada permiso con su revisión y su vídeo de demostración**. El vídeo tiene que estar en una URL pública para que Meta lo descargue | 2 a 4 semanas de revisión | 0 € |

Es decir: **coste cero y una intervención puntual de setup**, que es exactamente lo que la
regla 5 permite y lo que la regla 4 exige. Pero no es una tarde: es un trámite con cola.

### La decisión, que es de orden y no de sí o no

**Se empieza el trámite hoy y no se publica nada hasta que C38 haya dado su primera medida.**

El motivo es el de siempre en este proyecto: la cola de revisión son de dos a cuatro semanas de
**espera**, y la espera corre en paralelo a lo que estamos arreglando. Poner el trámite en
marcha hoy no cuesta nada más que el rato del codirector; publicar hoy sí costaría algo,
porque multiplicaría por tres la exposición de un vídeo con el medio flojo, que es lo que
estamos arreglando esta misma semana. **Cuando la aprobación llegue, los Shorts nuevos ya
llevarán el reloj de C38 puesto.** Si llega antes de lo previsto, se espera igual.

**Y hay un premio que no es la exposición.** Hoy no sabemos si nuestros Shorts son flojos o si
es el feed de YouTube el que no nos reparte. **El mismo vídeo en dos feeds distintos contesta
esa pregunta**, y la contesta antes del 15 de noviembre. Es la primera medida del proyecto que
puede separar «el contenido no funciona» de «no nos están enseñando», y las dos cosas piden
decisiones opuestas. Por eso C41 entra ahora y no en enero.

**Lo que hace falta de la dirección, cuando el trámite esté:** el paso de subida en
`producir.yml` (fichero del codirector), un `publicar_redes.py` que hable con las dos APIs, y
los dos identificadores en `REDES.md`. Nada de eso se escribe hoy: escribir el cliente de una
API antes de saber si la app está aprobada es trabajo que se tira si la aprobación no llega.

---

## Y la pregunta del codirector sobre cuándo escribirme

*«¿Es más interesante que te escriba antes de la revisión diaria para que si hay que cambiar el
prompt de la tarea puedas hacerlo, o después para que tengas los resultados?»*

**Después, siempre.** Y con un solo mensaje, que es lo que él prefiere por cuota.

El motivo es que la revisión diaria escribe `ESTADO.md` y su bitácora, y eso es la mitad de lo
que yo leo al arrancar. Si me escribe antes, arranco con la foto de ayer y le contesto con
información vieja. Hoy mismo es el ejemplo: la tabla de `origen_voz` de los tres últimos Shorts
—0 de 18 escenas con dirección mínima— la puso la revisión de esta mañana, y es lo que ha
decidido que la dirección de actor v2 se queda.

Y el miedo que hay detrás de la pregunta no se sostiene: **cambiar el prompt de la revisión
diaria no tiene prisa**, porque la tarea corre todos los días. Un cambio que escribo el viernes
entra en la del sábado. Lo único que sí tiene reloj es la **producción**, que arranca a las
01:13 UTC: un arreglo que tiene que salir en el vídeo de mañana está en `origin/main` antes de
esa hora, y esa es la hora que hay que tener delante, no la de la revisión.

**Queda escrito en `PROMPT_DE_ARRANQUE.md`** para que no haya que volver a preguntarlo.

---

## Lo que NO cambia hoy

- El punto de control sigue siendo el **27 de septiembre** y la decisión, el **15 de noviembre**
  (C26). Los umbrales se discuten antes del 8 de noviembre, no después de ver los datos.
- **La regla 11.1 sigue suspendida** para presentación hasta el 27. C38 no es presentación: es
  guion, y entra en cinco vídeos a la vez a propósito. Con n = 5 en una semana y la historia de
  quince Shorts como línea de base, la atribución sale de comparar contra el pasado, no dentro
  de la semana.
- No se clona la voz de nadie, no se encienden los subtítulos quemados, y `.github/workflows/`
  sigue sin escribirse en remoto.
- **`MDH-007` no se toca.** Se publica el domingo 20 a las 12:00.

## Lo que queda mirado y no resuelto

- **La caché de voz de `MDH-007` lleva dos días clavada en 18 de 41** y no hay commit de
  precacheo con fecha de hoy, aunque `voz_adelantada.yml` tiene cron a las 09:00 UTC. Con 23
  escenas por sintetizar y el tope de 10 peticiones por modelo y producción, el domingo sale
  —20 escenas en la pasada de las 01:13 y las 3 restantes en la de las 08:23— pero **sin margen
  para rechazos**. Hay que volver a contarlo mañana; si sigue en 18, el episodio se mueve otra
  vez antes de que falle solo.
- **`MDH-002` pasa del máximo del formato largo con el estimador nuevo** (6m44 contra 400 s).
  Está publicado desde agosto y no bloquea nada; se anota para que nadie se asuste al verlo.
- **E02** tiene dos DOI distintos en el `.md` y en el JSON y ninguno verificado.


---

# Versión 11 · 21 de septiembre de 2026 — el canal deja de arrastrar el formato que no funciona

**Esta es la versión que manda.** Todo lo anterior sigue vigente salvo donde aquí se diga lo
contrario, y lo que se anula se dice con su nombre.

La sesión sale de cinco cosas que el codirector trajo el lunes 21: un choque de ficheros entre
las revisiones del sábado y el domingo; las visitas cayendo en picado y el episodio largo a
cero; la sospecha de que la voz suena distinta en cada escena; la pregunta de si estas
conversaciones deberían ser una tarea programada; y la sensación de que no vamos bien de cara a
los hitos de decisión.

Cuatro de las cinco tienen respuesta medida. La quinta —los hitos— tiene una respuesta que no es
la que él esperaba.

---

## Lo primero, porque cambia el tono de todo lo demás: dónde estamos de verdad

**El punto de control del 27 de septiembre ya está contestado, y la respuesta es la buena.** Su
pregunta, escrita en la versión 4 y sin tocar desde entonces, es una sola:

> **¿Algún Short ha pasado de 100 visualizaciones en sus primeras 48 horas?**

Sí. **Tres**, todos en los últimos siete días, leídos por `metricas.py` el 21/09 a las 05:33 UTC:

| Short | Tema | Vistas a 48 h |
|---|---|---|
| `MDS-016` (14/09) | la ironía por WhatsApp | **1.210** |
| `MDS-019` (17/09) | los anuncios graciosos | **161** |
| `MDS-018` (16/09) | el profesor gracioso | **135** |

El desenlace escrito para ese «sí» es *«el formato funciona, toca escalarlo»*. Antes de esos
tres, quince Shorts con **mediana 10** y **ninguno por encima de 50**.

**Y una cosa que hay que decir en voz alta antes de que llegue noviembre, no después.** C26 da
tres puertas para «se sigue» el 15 de noviembre, y una de ellas es *«algún Short por encima de
1.000»*. **Esa puerta ya está abierta** desde el 14 de septiembre. Mi opinión, y la digo ahora
porque la cláusula 1 de C26 dice que los umbrales se discuten **antes del 8 de noviembre**:
**esa puerta está mal escrita.** Un vídeo por encima de mil que no sabemos explicar demuestra
que el techo existe; no demuestra que tengamos una máquina. Propuesta, para decidir entre los
dos antes del 8 de noviembre:

> sustituir *«algún Short por encima de 1.000»* por **«dos Shorts por encima de 1.000 en
> semanas distintas»**, y dejar las otras dos puertas —mediana ≥ 150, o ≥ 100 suscriptores—
> como están.

Si el codirector prefiere dejarla como está, se deja y se cumple: lo que no vale es llegar al
15 de noviembre con una puerta abierta que ninguno de los dos se cree.

### La previsión, que es la parte que de verdad contesta a «no vamos bien»

La cifra de C26 es **la mediana de los últimos veinte Shorts a 48 horas**. Hoy vale **11,0**.
Esa cifra no predice nada, y conviene entender por qué:

**El 15 de noviembre, ninguno de los veinte Shorts publicados hasta hoy estará en la
ventana.** Quedan 55 días y se publican cinco Shorts por semana: son unos **39 Shorts más**, así
que los veinte que se medirán serán los de, aproximadamente, el 18 de octubre en adelante.
**Todos ellos están sin escribir.** El 11,0 de hoy es historia de agosto, no un pronóstico.

Lo que sí pronostica algo es el régimen de la última semana. Las cinco últimas lecturas a 48 h
son **1.210 · 161 · 135 · 27 · 0**, mediana **135**. Quitando el outlier de 1.210: **81**.
Quitando también el 0: **148**.

| Si el régimen de la última semana se sostiene | La mediana del 15/11 cae en | Y eso es |
|---|---|---|
| tal cual, con sus ceros | 50–150 | **se amplía el tema**, prórroga única de ocho semanas hasta el 10 de enero |
| sin los ceros | rozando 150 | la frontera entre ampliar y seguir |
| si vuelve el nivel de agosto | < 50 | **se para** |

**Conclusión honesta: no estamos fracasando, estamos en la frontera.** Y el lado de la frontera
en el que caigamos **no lo decide el contenido bueno, lo deciden los ceros.** Subir un 161 a un
200 mueve la mediana bastante menos que evitar que un vídeo haga 0. Dos de los últimos cinco
Shorts salieron tocados —`MDS-017` con 0 y `MDS-020` con 27—, y en el primero la causa
documentada no es el guion: es la voz.

Por eso las decisiones de hoy van casi todas contra los ceros y no contra la calidad media.

### Y lo que hay que mirar en Studio antes de sacar conclusiones del cero

**`MDS-017` (19/09) tiene 0 visualizaciones a 48 horas y `MDH-007` (20/09) todavía no tiene
ninguna lectura.** Un 0 puede significar dos cosas **opuestas**, y la API de analítica no las
distingue:

- **0 visualizaciones con impresiones normales** → nos lo enseñaron y nadie lo abrió. Eso es
  contenido, miniatura o primer segundo.
- **0 visualizaciones con ~0 impresiones** → **no lo enseñaron.** Eso es distribución, y no lo
  arregla ningún guion.

Las impresiones solo están en Studio: la API de YouTube no las expone (lo dice la cabecera de
`metricas.json` y de `metricas.yml`). Es la **tarea 1** del codirector esta semana, y es la que
decide si lo siguiente que tocamos es el guion o la publicación. **Hasta tenerla, nadie
reescribe nada por culpa de ese cero.**

---

## C42 · El episodio largo se suspende

**Decisión tomada hoy y aplicada hoy.**

### Los números, que son la mitad del motivo

Siete episodios largos, el primero del 18 de agosto. Lectura del 21/09:

| | Publicado | Días | Vistas |
|---|---|---|---|
| `MDH-001` | 18/08 | 34 | 18 |
| `MDH-002` | 19/08 | 33 | **34** |
| `MDH-003` | 20/08 | 32 | 13 |
| `MDH-004` | 29/08 | 23 | 10 |
| `MDH-005` | 05/09 | 16 | 6 |
| `MDH-006` | 12/09 | 9 | 33 |
| `MDH-007` | 20/09 | 1 | 0 |

**114 visualizaciones entre los siete, en treinta y cuatro días**: dieciséis de media por
episodio, contando toda su vida. Los cinco Shorts de la última semana suman **1.533 en sus
primeras cuarenta y ocho horas**: trescientos seis de media por pieza. Y un largo cuesta siete
veces más de producir —41 escenas de voz contra 6—. No es que el formato largo vaya peor: es
que no compite.

Y no es una sorpresa que haya llegado esta semana. `MDH-004`, `MDH-005` y `MDH-006` tuvieron
**0 visualizaciones en su lectura a 48 horas**, los tres. **Que un episodio largo tenga 0 a las
48 horas no es una avería nueva: es el comportamiento normal del formato en este canal.** El
codirector lo ha visto hoy porque hoy lo ha mirado; llevaba pasando desde agosto.

### La otra mitad del motivo, que es la que nadie había visto

**El precacheo del episodio largo se estaba comiendo el respaldo de voz de los Shorts.**

La cabecera de `voz_precache.py` dice, con todas las letras: *«cuota propia, nunca la de los
Shorts (C7)»*. **Era verdad el 14 de septiembre y es falsa desde el 15.** Ese día C33.1 escribió
esto en `voz.py`:

```python
MODELOS_CORTO = (MODELO_GEMINI, MODELO_GEMINI_LARGO)   # 3.1, y si no, 2.5 entero
```

Es decir: **`gemini-2.5-flash-preview-tts` dejó de ser «el modelo del largo» y pasó a ser el
peldaño (b) del respaldo de voz de los Shorts.** Y `voz_adelantada.yml` corre **todos los días**
a las 09:00 UTC con `PRESUPUESTO_POR_DEFECTO = 9` sobre una cuota de 10 peticiones diarias.

**Nueve de cada diez peticiones de la red de seguridad de los Shorts se gastaban en el episodio
largo.** Un Short necesita seis. El peldaño (b) de C33.1 no podía ejercerse prácticamente nunca:
existía en el código y no existía en la práctica. `MDS-017` hizo 0 visualizaciones y su historia
es una historia de voz.

**Es la trampa 1 del proyecto, otra vez** —cuando cambies algo, busca qué dependía de ello— y la
24 —cuando cambies lo que entra en una clave o en una cuota, busca a todos los que la comparten.
Queda como **trampa 35**.

### Y la aritmética que hacía imposible a `MDH-007` desde el principio

41 escenas con narración ÷ 9 peticiones al día = **cinco días de precacheo perfecto**, sin un
solo rechazo, y los rechazos también gastan cuota (trampa 30). El domingo 20 llegó con 38 de 41.
`MDH-008` tiene 34 escenas: cuatro días perfectos. Es el mismo filo del cuchillo.

### Qué se hace, exactamente

| | Estado |
|---|---|
| `MDH-008` (sábado 26/09) | **No se emite.** Retirado de `05_calendario/parrilla.json`; queda con su motivo y su fecha en la clave `_emisiones_suspendidas` del mismo fichero |
| `05_calendario/guiones/MDH-008.es.json` | **Se queda escrito y sin tocar.** No se borra, no se edita |
| La semana | **Cinco Shorts, de lunes a viernes a las 19:00. Nada el sábado ni el domingo** |
| `voz_adelantada.yml` | **El codirector lo desactiva** (tarea 3). Sin largos pendientes en la parrilla, `voz_precache.py` ya no hace nada —imprime «No hay ningún largo pendiente» y no gasta—, pero un workflow que corre todos los días para no hacer nada es una trampa esperando a que alguien reponga un largo sin acordarse de esto |
| `00_estrategia/tareas/planificacion-jueves.md` | Paso 3 (**adaptar el largo**) **ANULADO** mientras dure la suspensión, con su texto conservado debajo para cuando vuelva. Paso 5 corregido: no se extiende el sábado |
| `00_estrategia/tareas/revision-diaria.md` | Avisada en la cabecera |

### Cuándo vuelve

**Cuando `control_c26.mediana_vistas_48h` de `metricas.json` llegue a 50**, que es el suelo del
rango normal para un canal desconocido. Es una condición medible y la escribe sola la tarea de
métricas cada lunes. Hoy vale 11,0.

No es «nunca». Es: **el formato largo es un lujo de canal con público, y no tenemos público
todavía.** Lo que se ha aprendido construyéndolo —41 escenas cosidas, la dirección de actor, el
precacheo— no se tira: está en el código y en los guiones, y el guion de `MDH-008` está
terminado esperando.

---

## C43 · La dirección no se automatiza. Su salida, sí

**La pregunta del codirector, del 21/09:** *«¿deberíamos convertir nuestras conversaciones de
dirección en tareas programadas o no? Evalúa la situación y dame tu opinión.»* Va en la misma
línea que su idea del 18/09 de `08_comunicacion/`.

**Mi respuesta es que no, y creo que la idea buena que hay detrás es otra.**

**Por qué no.** El propio proyecto tiene escrita la frontera, y es del codirector: *«las tareas
programadas tienen que ejecutarse enteras y solas: lo que no pueda hacerse sin una persona se
registra y se hace en otro momento, pero no bloquea»*. Una sesión de dirección es, por
definición, lo que no se puede hacer sin una persona. Esta misma sesión tiene tres puntos en los
que la respuesta correcta es *«en esto tienes razón y en esto otro no»* —el episodio largo sí,
el «no vamos bien» no, la puerta de los 1.000 hay que discutirla—, y eso no es una salida que se
pueda escribir en un fichero: es una conversación en la que alguien puede contestar.

Y hay una razón práctica: el trabajo de leer los nueve documentos del arranque **no es la parte
cara**. La parte cara es decidir, y no se delega a un modelo más barato sin dejar de ser lo que
se paga aquí. Automatizar la lectura y dejar la decisión a la tarea programada sería quedarnos
con el gasto y perder el criterio.

**Lo que sí se automatiza desde hoy, y es la idea suya del 18/09 llevada a su sitio: la salida.**

Hasta hoy, lo que se decide en una sesión de dirección llega a las tareas programadas **por
reescritura de sus prompts**, que es lenta, se olvida a medias (trampas 12, 18, 32) y no deja
rastro de cuándo se enteró cada agente. Desde hoy:

- **Después de cada sesión de dirección se escribe `08_comunicacion/AAAA-MM-DD-direccion.md`**
  con lo decidido, en la forma en que cada agente lo necesita. Los tres prompts ya dicen que
  esa carpeta se lee antes de trabajar.
- `08_comunicacion/novedades.md` **es del codirector y solo suyo**: se lee y no se toca. Eso ya
  estaba en su idea y se respeta tal cual.
- Los prompts se siguen reescribiendo cuando el cambio es permanente. La carpeta es para que el
  cambio llegue **el mismo día**, no para sustituir al prompt.

**Y lo que sí debería ser una tarea programada, aunque él no lo haya pedido, es lo de al lado:
mirar los números todos los días.** Ver C47.

---

## C44 · La voz deja de sonar a montaje

**La observación del codirector, del 21/09:** *«creo que el hecho de hacerlo por escenas provoca
que las voces en cada escena sean un poco distintas, y eso crea una sensación artificial.»*

**Tiene razón, y el mecanismo es peor de lo que él cree: no es solo que pase, es que se lo
estamos pidiendo.**

### Las tres causas, por orden de tamaño

1. **Cada escena es una llamada independiente a la API.** `voice_name: Charon` fija la
   identidad, no la toma: el registro, la velocidad, la energía y hasta la distancia aparente al
   micrófono los elige el modelo en cada generación. Seis llamadas en un Short son seis tomas;
   cuarenta y una en un largo son cuarenta y un narradores.
2. **La dirección de actor pide explícitamente que el timbre cambie.** Textual, hoy, en
   `DIRECCION_POR_PAPEL`: *«cambia claramente de color de voz en la segunda»* (contraste),
   *«cambia de color de voz mientras las dices»* (cita), *«baja el tono»* (enumeración, cierre).
   Esa dirección está bien pensada para una escena suelta y es exactamente lo que no se debe
   pedir cuando la continuidad entre tomas ya es frágil. **El tono se dirige con el fraseo —las
   pausas, el acento, la velocidad—, no con el timbre.**
3. **El volumen de cada toma no se iguala nunca.** `montaje.py` aplica `loudnorm=I=-14` **una
   sola vez, sobre la mezcla final**. Eso normaliza el programa entero contra el estándar de
   YouTube y **no hace absolutamente nada** para que la escena 4 suene igual de fuerte que la 3.
   Es, probablemente, la mitad de lo que se oye como «voz distinta».

Y encima, detrás de cada toma metemos hasta 1,35 s de silencio: un punto final, un silencio y
otro principio no es una pausa, es un corte. Eso ya estaba escrito como trampa 22 y C33 lo
atacó por el lado del contexto; el timbre se quedó sin atacar.

### Las tres capas del arreglo, y en qué orden entran

**Capa A · igualar el volumen de cada toma antes de la mezcla.** Determinista, sin red, sin
cuota, y **no toca la caché**: se aplica en el montaje sobre el mp3 que haya. `loudnorm` en dos
pasadas por escena a un objetivo fijo, y después la normalización de programa que ya existe.
Es la más barata y probablemente la que más se nota.

**Capa B · la dirección de actor deja de pedir cambios de timbre.** Dos cosas: una *ficha de
voz* fija, idéntica en todas las llamadas (registro, velocidad, distancia, energía), y reescribir
los papeles que piden «color de voz» para que pidan fraseo. **Cuesta invalidar la caché entera**
—`VERSION_DIRECCION` de 2 a 3—, y eso es asumible **precisamente porque el largo está
suspendido**: un Short entero son seis peticiones, media cuota diaria.

**Capa C · una sola toma por vídeo.** Es **C36**, propuesto el 15/09 y sin diseño escrito desde
entonces. Queda **reactivado y con dueño**. Un Short son ~110 palabras: caben de sobra en una
llamada. Una toma = una voz, y la prosodia fluye porque el modelo ve el guion entero. De regalo,
el gasto de voz de un Short baja de **seis peticiones a una**, con lo que la cuota deja de ser
el cuello de botella del canal. Lo que hay que resolver es el corte: partir el audio en escenas
con un alineador **local** (regla 11.6: nada de red en tiempo de render), tipo `faster-whisper`
con marcas de palabra, o alineación forzada contra el texto que ya conocemos.

### Cuándo entra cada cosa, y por qué no hoy

**Esta semana no se toca la voz.** La semana del 21 es la **primera medida limpia de C38** —los
cinco Shorts reescritos a la duración de su serie y con el remate a partir del segundo 10— y
meter la voz encima tira esa medición a la basura. Regla 11.1.

| Cuándo | Qué |
|---|---|
| Semana del 21 | **A y B se escriben y se prueban**, sin encender nada. C36 se diseña por escrito. Nada llega a un vídeo |
| **Lunes 28** | **A y B entran juntas**, después del punto de control del 27. Juntas y no por separado a propósito: son la misma cosa —«que el narrador suene a una persona»— y separarlas cuesta dos semanas de canal para una atribución que con este volumen no se va a poder hacer de todos modos. Queda dicho, que es lo que la regla 11.1 pide de verdad |
| Después de medir A+B | **C36**, si su diseño se sostiene |

**Y una cosa que el codirector debe oír tal cual:** el 20/09 se publicó un episodio de 41 tomas
distintas. Con el largo suspendido, el peor caso pasa a ser de **seis tomas**, no de cuarenta y
una. Parte del problema que describe se va solo con C42.

---

## C45 · `ESTADO.md` deja de ser un fichero que se reescribe

**El problema del codirector, del 21/09:** *«problema de conflicto de ficheros entre las
revisiones diarias del sábado y del domingo».*

**La causa es estructural y va a repetirse todos los fines de semana.** La revisión diaria corre
los siete días y entrega un `.tar.gz` que el codirector aplica a mano. El sábado no lo aplicó
—era sábado—, el domingo llegó el segundo paquete, y los dos traían **un `ESTADO.md` distinto
del mismo fichero**. Todo lo demás que entrega esa tarea es un fichero nuevo por ejecución y por
eso no chocó nada más.

**Y la lección es incómoda, porque la regla que faltaba ya existía.** El 21 de agosto, después
de que la revisión diaria borrara 188 líneas de bitácora de la planificación, se escribió la
regla que sostiene todo el reparto de ficheros de este proyecto: **un fichero nuevo no puede
pisar nada.** El 31 de agosto se le dio a ese mismo agente un fichero más, `ESTADO.md`, **que se
reescribe entero todos los días** — es decir, se volvió a crear justo la figura que la regla
existía para eliminar, diez días después de escribirla. Es la trampa 25 (una regla escrita para
un caso no protege al de al lado) cometida sobre la regla de la que salen las demás. **Trampa
36.**

**Lo que se hace, y ya está hecho:**

- Nace **`05_calendario/estado/`**, un fichero por día: `estado/AAAA-MM-DD.md`. **El estado de
  hoy es el fichero de nombre más alto.** Con su `LEEME.md` explicando el porqué.
- **`05_calendario/ESTADO.md` queda CONGELADO**, igual que `MEJORAS.md` lo está desde agosto: se
  lee, no se escribe. Su contenido es ahora un puntero.
- El `ESTADO_old.md` del sábado pasa a ser `estado/2026-09-19.md`, y el del domingo,
  `estado/2026-09-20.md`. No se pierde nada.
- El **paso 6** de `revision-diaria.md` está reescrito.

### Y de paso: la incidencia del domingo era falsa por dieciséis minutos

Al mirar el choque apareció otra cosa. `ESTADO.md` del 20/09 decía, como `INCIDENCIA`, que
`MDH-007` no estaba en `registro_publicaciones.json` tras los tres intentos de cron. **Sí
estaba.** Se subió el 20/09 a las **09:37:31 UTC** (`6sAuU_OHxwI`, `public`), y la revisión
escribió a las **09:53 UTC** sobre un clon anterior a ese commit.

El tercer intento de producción (08:23 UTC) arrastra los retrasos habituales de Actions —de dos
a seis horas— y cae **justo encima** de la ventana de la revisión de las 11:30 de España. No es
un descuido: es una carrera que estaba garantizada.

Consecuencia: el codirector se encontró el lunes con un pendiente que decía *«la dirección tiene
que mover MDH-007 de día en parrilla.json»* para un vídeo que llevaba veinticuatro horas
publicado. **Ese pendiente queda anulado.**

Arreglado en `revision-diaria.md`: antes de escribir una incidencia de «falta el vídeo del día»,
`git fetch` y releer `registro_publicaciones.json` de `origin/main`, y decir en la bitácora a
qué hora se releyó.

---

## C46 · El canal se lee a sí mismo

**Nadie había conectado nunca los resultados del canal con la elección de los temas.**

La planificación de los jueves elige la semana con `demanda.json` —lo que la gente busca en
YouTube— y **no lee `metricas.json`**. Está escrito en su propio prompt: *«NO eres dueño de (…)
`metricas.json`»*, y de ahí nadie dedujo que sí tenía que leerlo. La tarea de métricas de los
lunes lo lee y lo interpreta, pero su salida es una bitácora, no una entrada de la planificación
del jueves.

**El precio, con nombre y apellidos:** `MDS-016`, «por qué la ironía no se entiende por
WhatsApp», hizo **1.210 visualizaciones a 48 horas** el 14 de septiembre, cuando los quince
anteriores tenían mediana 10. Una semana después **no hay en el repositorio ni un solo vídeo que
lo continúe**, y nadie lo decidió: es que el número no llegaba a quien elige los temas. La mejor
señal que ha producido este canal en un mes se cayó por una rendija de la tabla de propiedad.

**Lo que se hace, y ya está hecho:** paso **1 bis** nuevo en `planificacion-jueves.md`.

1. `metricas.json` entra en su lectura obligatoria, **antes** de elegir tema.
2. **Los dos mejores temas de las últimas cuatro semanas tienen derecho de tanteo:** al menos
   uno de los cinco Shorts de la semana continúa, profundiza o mira desde otro ángulo uno de los
   dos. Si decide que ninguno se puede continuar, lo escribe con el motivo. Lo que no vale es no
   mirarlo.
3. **Un tema hundido no se repite en seis semanas**, salvo que el hundimiento tenga causa
   conocida ajena al tema (`MDS-017` hizo 0 por la voz, no por el asunto: no cuenta).
4. **`metricas.json` manda sobre `demanda.json`** cuando los dos hablen del mismo sitio. La
   demanda dice qué se busca ahí fuera; las métricas dicen qué nos funciona **a nosotros**, y
   eso es más pequeño, más caro y más valioso.

**Y de paso, dos correcciones al mismo prompt**, que llevaba días trabajando con datos falsos:

- Su sección «Dónde está el canal» estaba **congelada en el 7 de septiembre** y decía que
  sacamos «entre 20 y 30» visualizaciones por Short.
- Decía que *«el único indicio direccional sigue siendo la búsqueda»*. **Eso lo corrigió C40 el
  18 de septiembre** —feed 54,6 %, búsqueda 27,7 %— y la corrección se escribió en `LEEME.md` y
  no se propagó a los prompts. **Trampa 32 otra vez**: una corrección aplicada en un sitio y no
  en los demás.

---

## C47 · Las métricas se leen todos los días, no solo los lunes

**El agujero:** `metricas.yml` corre **solo los lunes** (`cron: "19 5 * * 1"` y `"37 8 * * 1"`).
La revisión diaria comprueba todos los días que el vídeo **se publicó**, y no mira nunca cuánta
gente lo vio. Resultado: **un Short puede hacer 0 visualizaciones durante seis días y no
enterarse nadie hasta el lunes.** Es literalmente lo que ha pasado con `MDS-017`.

Un cero es la señal más valiosa y más urgente que produce este canal —es la que mueve la mediana
de C26— y es la única que llega con seis días de retraso.

**Lo que se hace:**

1. **Un encargo para la revisión diaria esta semana:** una lectura ligera diaria en
   `05_calendario/metricas_diarias.json` con **solo** `id`, `publicado`, `visualizaciones` y
   `vistas_48h` de los vídeos publicados en los últimos diez días. **Sin curvas de retención**:
   `metricas.json` ocupa 174 KB con cinco lecturas porque guarda 100 puntos de retención por
   vídeo, y leer eso a diario lo pondría en varios megas de churn en git. La lectura completa
   sigue siendo semanal y no se toca.
2. **Una línea para el codirector** en `metricas.yml` (fichero protegido), tarea 4.
3. **La revisión diaria mira ese fichero** en su paso 2 y marca `INCIDENCIA` si un Short pasa de
   las 24 horas con 0 visualizaciones.

---

## Lo que NO cambia hoy

- **El punto de control sigue siendo el domingo 27 de septiembre** y la decisión, el **15 de
  noviembre**. Los umbrales se discuten **antes del 8 de noviembre** — y hoy queda abierta la
  única discusión pendiente: la puerta de «algún Short por encima de 1.000».
- **La semana del 21 no se toca.** Los cinco Shorts reescritos por C38 se producen como están:
  es la primera medida limpia de C38 y vale más que cualquier mejora que se nos ocurra meter
  encima. Regla 11.1.
- **C38, C38.1, C39, C40 y C41 siguen enteros.** El trámite de TikTok sigue donde lo dejó
  `PLAN_TIKTOK_APP_REVIEW.md`.
- **No se amplía el tema todavía.** Esa conversación es del 15 de noviembre, salvo que el 27
  diga otra cosa.
- No se clona la voz de nadie, no se encienden los subtítulos quemados, y `.github/workflows/`
  sigue sin poder escribirse en remoto.

## Lo que queda mirado y sin resolver

- **Por qué `MDS-016` hizo 1.210.** Sigue sin explicación desde el 15/09. Con C46 al menos
  dejará de ser un dato huérfano.
- **Las impresiones de `MDS-017` y `MDH-007`.** Tarea 1. Hasta tenerlas, el cero no se
  interpreta.
- **`E02`** sigue con dos DOI y ninguno verificado. Viene del 18/09.
- **`F04`** sigue sin sustituir (tarea 5 del 18/09).
- **P1 (profundidad)** sigue sin respuesta del codirector en `07_pruebas/P1-profundidad/` desde
  el 14/09. Es la más vieja de las preguntas abiertas.
- **C34 (banco de imágenes)** estaba bloqueado por los enlaces de origen. **Desbloqueado hoy**:
  el codirector dejó `02_marca/banco/creditos_pixabay.csv` el 18/09 y la dirección ha generado
  `02_marca/banco/banco.json` con los tres campos que exige la regla 9 —licencia, autor y
  enlace— para las quince imágenes. Entra en la cola de presentación.

---

# Versión 12 · 23 de septiembre de 2026 — la historia antes que el reloj, y la imagen deja de ser una diapositiva

**Esta es la versión que manda.** Todo lo anterior sigue vigente salvo donde aquí se diga lo
contrario, y lo que se anula se dice con su nombre, en la tabla de abajo.

Sesión **extraordinaria**, de miércoles. La pidió el codirector con tres notas seguidas en
`PROMPT_DIRECCIÓN.md`:

- **21/09**, sobre `MDS-021`: *«un poco un desastre en términos de guion. ¿Nadie revisa los guiones
  desde el punto de vista narrativo? Se sienten sin hilo, deslabazados.»*
- **22/09**, sobre `MDS-022`: *«sigue teniendo problemas de guion evidentes. Tenemos que mejorar la
  calidad de los guiones con máxima importancia.»*
- **23/09**, sobre `MDS-023`: *«¿Cómo puede ser que termine el vídeo de hoy con "¿y a nadie a las
  8?"? ¡El guion de los shorts no se sostiene por ningún sitio! Es una sucesión de mensajes
  inconexos, sin sentido, que huelen a AI Slop de lejos. […] Hay que cambiar los guiones hoy
  mismo.»* Y en la misma nota: *«Hay que repensar toda la estrategia de imágenes […] tenemos que
  darle un giro de 180º a la presentación de los vídeos.»*

Y dos asuntos que venían de antes: la nota de la revisión diaria del 22/09 sobre
`sincroniza_registro.yml`, y la petición del 21/09 en `08_comunicacion/novedades.md` de estudiar
el último vídeo de @Maestro_Seductor.

Salen cuatro cambios: **C48** (la historia), **C49** (la sincronización, que no estaba rota),
**C50** (la imagen) y **C51** (el presentador sintético, que no entra todavía).

---

## Lo que se anula, lo que se mantiene y lo que se amplía

| Documento o decisión | Estado desde hoy |
|---|---|
| Nota de dirección del 21/09, punto 5 · «esta semana no se toca voz, guion ni presentación» | **ANULADA en lo que toca al guion.** Medir C38 con guiones que no se entienden no mide nada. La voz sigue sin tocarse hasta el lunes 28 (C44) |
| C38 · «el Short se escribe a la duración de su serie ±12 %» (ERROR en `validar_guion.py`) | **ANULADA como error.** Pasa a referencia (AVISO). El techo de 55 s sigue siendo ERROR |
| C38 · «el remate no cae antes del segundo 10» (ERROR) | **Rebajada a AVISO.** La idea se queda como consejo |
| Regla 13.2 de `REGLAS.md` | **CORREGIDA** en sus dos primeras viñetas (referencia, no regla). La tercera se mantiene |
| Regla 13.3 de `REGLAS.md` | **NUEVA**: un Short cuenta una historia, y lo comprueba alguien que no la conoce |
| `guionista_corto.md` · las tres pruebas de cosido | **SE MANTIENEN**, detrás de la sección nueva «Lo primero de todo: la historia», que manda sobre ellas |
| `guionista_corto.md` · prueba 4 (el reloj) | **ANULADA como error**; se deja escrita por el razonamiento sobre la retención |
| Versión 10 · los cinco Shorts de la semana del 21 reescritos por la dirección el 18/09 | **SUSTITUIDOS** los tres que quedaban (`MDS-023`, `024` y `025`). `MDS-021` y `MDS-022` ya están publicados y se quedan como están |
| C44 · la voz (capas A y B el lunes 28) | **SE MANTIENE** tal cual |
| C26 · la decisión del 15 de noviembre, y el punto de control del 27 | **SE MANTIENEN** |
| C34 · el banco de imágenes (15 fotos de Pixabay en duotono, primera posición en la escena 1) | **SE AMPLÍA en C50**: el banco deja de ser quince fotos para la escena 1 y pasa a ser una fuente visual por escena |
| C6.1 · los subtítulos quemados, apagados por decisión del codirector del 20/08 | **SE MANTIENEN apagados.** Con imagen real detrás cambia el argumento que los apagó, así que el muestrario de C50 enseña una variante con ellos, **y decide el codirector** |
| Regla 11.1 (un cambio por producción), suspendida para la presentación hasta el 27/09 | **SE AMPLÍA la suspensión hasta que C50 esté entero.** Razón en C50 |
| Nota de la revisión diaria del 22/09 · «`sincroniza_registro.yml` puede no estar corrigiendo el registro» | **CERRADA**: no era una avería (C49) |
| Petición del 21/09 en `novedades.md` · el vídeo de @Maestro_Seductor | **CONTESTADA** en C51 |

---

## C48 · La historia antes que el reloj

**Hecho hoy.** `MDS-023`, `MDS-024` y `MDS-025` reescritos; `validar_guion.py`;
`04_agentes/prompts/guionista_corto.md`; `00_estrategia/tareas/planificacion-jueves.md` y
`revision-diaria.md`; `REGLAS.md` (13.2 corregida y 13.3 nueva); `esquema_guion.json`;
`08_comunicacion/2026-09-23-direccion.md`.

### Lo que se oyó, con las frases exactas

- `MDS-021` (21/09): *«Veinte años. No se me ha acabado.»* — un chiste que el espectador tiene que
  terminar él (el narrador tiene tantos defectos que el material no se le acaba). Y al cerrar,
  *«Yo saldría graciosísimo»*, que es la misma operación con otra premisa.
- `MDS-022` (22/09): *«Y ahora vuelve a leerlo.»* — en un vídeo que se escucha.
- `MDS-023` (23/09, retirado antes de publicarse): una risoterapia obligatoria a las ocho de la
  mañana, un estudio sobre estilos de humor y estrés en jubilados, *«les salió lo contrario»*
  (¿de qué?), y el cierre *«Y a nadie a las ocho»*.

### Por qué pasó, en orden de tamaño

1. **El chiste y el estudio eran dos historias pegadas, o les faltaba la frase que los unía.** La
   risoterapia de las ocho no es lo que mide un estudio sobre estilos de humor, y el señor de la
   boda que contestaba «ya» no era quien se quedaba en blanco. En `MDS-021` la anécdota sí era el
   fenómeno —el material a costa de uno mismo es el estilo autodestructivo que midió Greengross—,
   pero no había ninguna frase que lo dijera («o sea, que mis veinte años de material son justo el
   estilo que peor les va a los cómicos»). En los tres casos el espectador ve una anécdota, luego
   un estudio, y nadie le dice qué tienen que ver.
2. **Yo quité las frases que los cosían.** El 18/09 reescribí estos cinco Shorts para que cupieran
   en la duración de su serie, con una restricción que me pareció rigurosa: *«no entra ni una
   afirmación nueva; esta reescritura solo quita y recoloca»*. Lo que se quitó fueron los «por eso»
   y los «pero». `MDS-023` pasó de 111 palabras a 68. Las afirmaciones sobrevivieron todas; la
   historia, ninguna.
3. **Los cierres acababan en una frase que había que descifrar**, y eso lo fabricaba en parte una
   regla nuestra: la prueba 1 del guionista pide que el ejemplo de la escena 1 vuelva «por su
   nombre», y cumplida al pie de la letra produce callbacks de trámite («con el señor de la boda no
   lo probó nadie», «nadie ha medido el pijama»).
4. **Nadie comprobaba si se entendía.** `validar_guion.py` mide la forma. La revisión diaria mide
   los dos canales, las caras, el marcado y la ficha técnica — y dio los tres por limpios, porque
   lo eran. La planificación se revisa a sí misma. Y **quien escribe el guion es el único lector
   que nunca puede detectar un salto**: «y a nadie a las ocho» se entiende perfectamente si has
   escrito las cinco escenas de antes.
5. **Y yo había congelado los guiones de la semana** para medir C38 limpio (nota del 21/09, punto
   5). El codirector avisó el 21 y el 22 en su cuaderno; la revisión diaria no podía tocarlos; y
   yo no leo el cuaderno hasta que hay sesión. Tres días de avisos sin nadie autorizado a hacer
   caso.

### Lo que dice YouTube, que no es opinión nuestra

Desde el 15/07/2025, la política de monetización llama **contenido no auténtico** a, entre otras
cosas, *«image slideshows, templated storylines, or scrolling text with minimal or no narrative»*
y *«AI-generated content made with generic or unoriginal templates giving the impression of mass
production»* (YouTube Help, «YouTube channel monetization policies»). Eso afecta a la monetización,
no a la publicación, y el canal no monetiza todavía. Pero describe con precisión incómoda dos
rasgos nuestros: **23 de los 25 primeros Shorts abren con «mi madre», «mi jefe», «mi profesor»,
«en mi familia»…**, un narrador sintético con una familia inventada; y **el 72 % de lo que se ve
es texto sobre fondo** (medido el 07/09 en C25). La primera es C48; la segunda es C50.

### Los tres guiones, reescritos

Una pregunta, una respuesta y un puente cada uno, con el campo `historia` rellenado.

| | Antes (18/09) | Ahora | La historia en una línea |
|---|---|---|---|
| `MDS-023` · «¿Reírse es bueno para la salud?» | 68 pal. · ~39 s | **100 pal. · ~53 s** | Hacer chistes a tu costa tiene fama de dañino; en jubilados con muchos problemas iba con menos dolor; pero es una encuesta y puede ser al revés |
| `MDS-024` · «¿Cómo mantener una conversación sin quedarte en blanco?» | 81 · ~43 s | **100 · ~53 s** | La misma frase («vengo de Lisboa») con la respuesta que mata la conversación y la que la sigue; la regla del «sí, y además»; y es un manual, no un experimento |
| `MDS-025` · «¿Por qué el humor ayuda a memorizar?» | 89 · ~47 s | **87 · ~47 s** | Diez personas ven vídeos graciosos y diez se quedan sentadas sin móvil; las primeras mejoran la memoria un 43,6 % y les baja el cortisol; pero las otras mejoran casi la mitad |

- **Afirmaciones comprobadas hoy contra la fuente**, y en `MDS-023` contra el texto completo, no
  solo el resumen (`G03`, DOI 10.5964/ejop.v6i3.211, que la ficha no tenía). Las frases literales
  están en las notas de cada guion.
- **Una corrección de paso:** la nota de `MDS-025` del 17/09 decía que el resumen de Bains y otros
  solo menciona el cortisol como contexto. **No es así**: lo da como resultado (*«significant
  decreases in salivary cortisol were observed in the humor group»*). Por eso ahora el vídeo puede
  contestar al «por qué» de su título.
- **Los tres pasan `validar_guion.py`**, y **la barrera de C21 en las 18 escenas** con las
  tipografías de marca instaladas, midiendo en 21 instantes por escena (trampa 15).
- **Un defecto que salió al mirarlos:** `escena.html` pintaba los decimales con punto («43.6»)
  porque `toFixed()` siempre lo pone. Arreglado en `contar()`: respeta la coma del guion.
- **`MDS-023` se rehace hoy.** La subida de madrugada (`X1GAp3OUgKg`) la borra el codirector; la
  emisión del 23/09 lleva `rehacer_video_id`, y el siguiente intento de cron del día lo produce
  solo. Hay una **segunda emisión de `MDS-023` el sábado 26** como red de seguridad: si hoy sale
  bien, ese día `cola.py` dice «nada que producir» (comprobado simulándolo contra el registro de
  `origin/main`).

### La puerta nueva: la lectura en frío

Lo que se puede comprobar sin entender el vídeo se cumple sin entender el vídeo. Así que la
comprobación nueva no mide el guion: **le pregunta a alguien que no lo conoce qué ha entendido.**

1. Quien escribe rellena **`historia`**: pregunta, respuesta y puente, antes de la primera escena.
2. Un **subagente sin contexto** recibe solo las narraciones y los textos de pantalla y contesta
   cinco preguntas: de qué va, qué pregunta responde y qué responde, qué frase no ha entendido, qué
   frase sobra, y dónde se habría ido. Encargo literal en `guionista_corto.md`.
3. Sus respuestas van en **`lectura_en_frio`**. Pasa si no hay frases sin entender y si lo que
   cuenta es la misma idea que la `historia`.
4. **Desde `MDS-026`, `validar_guion.py` da ERROR sin las dos cosas**, y el Short no se produce.
5. **Y la revisión diaria repite la lectura cada día** sobre el Short de la madrugada siguiente,
   con otro subagente. Si no pasa, es INCIDENCIA; desde `MDS-026` lo arregla ella con la excepción
   de las 48 horas.

**Lo que esto no arregla, dicho antes de que pase:** el lector en frío es un modelo, no una
persona que desliza el dedo. Es una aproximación, mucho mejor que ninguna, pero el juez sigue
siendo el codirector. **Si un Short que pasó la lectura en frío le vuelve a parecer inconexo, el
defecto está en el encargo del lector**, y se corrige ahí (sería C48.1), no en el guion suelto.

**Y lo que se pierde, también dicho:** la semana del 21 era la primera medida limpia de C38. Ya no
lo es. Se pierde a propósito: medir el reloj con guiones que no se entienden no dice nada del
reloj.

### C48.1 · Y ninguna fórmula dos veces (añadido a las 09:45, a petición del codirector)

Al leer los tres guiones reescritos, el codirector: *«se entienden mejor, pero ¿por qué todos tienen
"y aquí falla"? ¿No hay más formas de terminar un Short que esa? Se agradecería más variedad entre
guiones.»*

**Tiene razón, y es la trampa 21 con otra cara:** los 25 Shorts publicados hasta el 22/09 cierran
con «y aquí falla» (y en pantalla, «Y falla aquí: …»), y los tres que acababa de reescribir yo,
también. La regla 12 obliga a decir dónde no llega lo que se ha contado; nunca dijo con qué frase.
Pero el propio guionista ponía de ejemplo «y esto se rompe cuando…», y de un ejemplo sale una
plantilla. Una frase que va en todos los vídeos no es rigor: es una coletilla que se oye venir.

- **Los tres cierres, reescritos**: `MDS-023` con una pregunta (*«¿y si es al revés?»*, que es la
  advertencia de los autores sobre la causalidad), `MDS-024` con *«es un truco de actores, no de
  científicos»* y `MDS-025` con *«lo malo es que eran diez por grupo»*, volviendo al grupo que se
  quedó sentado sin móvil, que es el chiste del principio.
- **La regla**: el cierre honesto sigue siendo obligatorio; la fórmula no. En los cinco Shorts de una
  semana no se repite ninguna, ni en el cierre, ni en su título de pantalla, ni en la apertura. En
  `guionista_corto.md` (la séptima regla de «La historia»), en `planificacion-jueves.md` y en la
  regla 12 de `REGLAS.md`.
- **`validar_guion.py` avisa (C48.1)** cuando el cierre de un Short empieza con las mismas tres
  palabras que el de cualquiera de los cuatro anteriores, en la narración o en el título. Probado:
  salta en `MDS-021` y `MDS-022` (publicados con «y aquí falla») y no en los tres nuevos.

| De la tabla del principio de esta versión | Añadido por C48.1 |
|---|---|
| Regla 12 de `REGLAS.md` · «un Short también puede terminar con "y esto falla cuando…"» | **PRECISADA**: la regla es el contenido, no la frase |
| `guionista_corto.md` · «"Y esto se rompe cuando…" cabe en cinco palabras» | **CORREGIDO**: era el ejemplo del que salió la plantilla |

---

## C49 · `sincroniza_registro.yml` funciona. Lo que falla es el reloj de quien lo lee

La revisión diaria del 22/09 escribió que el workflow podía no estar corrigiendo el registro
desde el 20/09, y el codirector contestó que corre en verde. **Tenían razón los dos**, y no hay
avería:

| Día | Corrió (UTC) | ¿Había algo que corregir? | Commit |
|---|---|---|---|
| 21/09 | 15:21 y 15:52 | No: `MDS-021` se publicaba a las 17:00 UTC, **después** | ninguno, y es lo correcto |
| 22/09 | 13:41 | Sí: `MDS-021` de `private` a `public` | **`77d6c7a`** |

El cron dice 08:50 y 09:10 UTC y llega con **cuatro o cinco horas de retraso**; la revisión diaria
lee a las 09:30 UTC. **Lee siempre antes de que haya corrido la sincronización de ese día.** Es la
trampa 14 otra vez: quien lee cuenta el margen desde la hora nominal del que escribe, no desde su
último reintento real. Escrito en `revision-diaria.md` (paso 2): un Short publicado la víspera que
aparece como `private` no es incidencia; sí lo son dos días sin sincronización habiendo algo que
corregir.

**Y un hallazgo de paso, arreglado:** `registrar.py` escribe `registro_publicaciones.json` con
sangría 2 y `metricas.py --solo-registro` con sangría 1. Cada producción y cada sincronización
reescribían **las ~950 líneas del fichero**: el commit `77d6c7a` cambiaba un solo campo y git
decía 470 inserciones y 470 borrados. Es ruido y es riesgo de conflicto. `metricas.py` escribe ya
con sangría 2.

(La cabecera del workflow dice «tres pasadas» y el `schedule` trae dos. Es un comentario en un
fichero protegido; no merece un encargo al codirector.)

---

## C50 · La imagen: de diapositiva a vídeo

**Decidido hoy. Se diseña y se prueba esta semana; entra cuando el codirector lo haya visto.**

### Por qué, y por qué ahora

El codirector: *«tenemos que darle un giro de 180º a la presentación de los vídeos. Estamos
estancados en ~100 visitas por vídeo, a pesar de que las nuevas voces hayan mejorado.»* Y el
14/09 ya lo había dicho: *«fondo azul con letras amarillas no compite con imágenes reales»*.

Lo que tenemos es, literalmente, lo que la política de YouTube pone como primer ejemplo de
contenido no auténtico: **texto sobre fondo, con la misma plantilla cada día**. C25 (los iconos,
la jerarquía tipográfica, el personaje) y C34 (quince fotos para la escena 1) lo han pulido; no lo
han cambiado. Un Short de un canal que funciona en este nicho es **imagen a pantalla completa que
cambia cada dos o tres segundos**, con el texto encima y no en lugar de la imagen.

### Qué se queda y qué cambia

**Se queda:** la paleta (azul noche, ámbar, cian), las tipografías, la cifra grande, los
diagramas y las comparaciones cuando son la explicación, el cierre honesto, y el Engranaje como
firma.

**Cambia:**

1. **Cada escena lleva una imagen o un vídeo a pantalla completa detrás.** Nada de fondo liso,
   salvo en el cierre.
2. **Un cambio de plano cada dos o tres segundos** —una escena de ocho segundos lleva dos o tres—,
   que es lo que pedía C35 y la regla del codirector de «mucha más densidad de estímulos».
3. **El texto pasa a ser una capa encima**: la frase corta de la escena (el `texto` de siempre),
   en blanco con la palabra clave en ámbar, sobre un degradado oscuro que garantiza que se lea. Las
   escenas de dato, comparación y diagrama siguen siendo tarjetas de marca, pero sobre la imagen
   desenfocada, no sobre azul.
4. **El Engranaje deja de reaccionar en cada escena** y se queda como firma: la apertura y el
   cierre.

### De dónde salen las imágenes, por orden

| Fuente | Para qué | Coste y licencia |
|---|---|---|
| **Vídeo de archivo: Pexels y Pixabay** (API) | Situaciones reales y genéricas: una boda, un móvil con WhatsApp, un aula, gente mayor riéndose, un coche averiado | Gratis. Pexels: 200 peticiones/hora y 20.000/mes; Pixabay: 100 por minuto. Las dos licencias permiten uso comercial sin atribución obligatoria, y **atribuimos igual** (regla 9: licencia, autor y enlace en `banco.json`) |
| **Imagen generada: FLUX.1 [schnell] en Cloudflare Workers AI** | Lo que el archivo no tiene: *un hombre en pijama en una reunión*, *una tostadora echando humo* | Gratis hasta 10.000 «neuronas» al día, y en el plan gratuito lo que pasa de ahí **se bloquea, no se cobra**. Según la tarifa publicada (4,8 por tesela de 512×512 y 9,6 por paso), una imagen de 1024×1024 a 4 pasos cuesta unas 58: **unas 170 al día**, y una semana necesita unas 30. **Dos cosas por comprobar en la prueba, no supuestas:** la documentación no da parámetros de ancho y alto, así que puede que solo saque imágenes cuadradas (entonces van enmarcadas, no a sangre, o se prueba otro de sus modelos); y los pesos abiertos de FLUX.1 [schnell] son Apache 2.0, pero en Cloudflare rigen además los términos de Black Forest Labs, que se leen antes de publicar nada |
| **Tarjeta de marca** (lo de ahora) | Datos, comparaciones y diagramas, cuando la explicación es el dibujo | — |

**Vídeo generado con IA: no, por ahora.** No hay ninguna vía gratuita que dé vídeo generado a
nuestro volumen, y los modelos abiertos necesitan una GPU que no tenemos. Una imagen generada con
movimiento de cámara (acercamiento y paneo lentos) da la mayor parte del efecto a coste cero. Se
reabre si C50 no mueve el número.

### Cómo funciona, sin que nadie tenga que hacer nada cada semana

1. **La planificación del jueves** escribe en cada escena un campo nuevo, `visual`: qué se busca
   en el archivo (en inglés, que es como están etiquetados) y, de respaldo, qué imagen generar.
2. **Un paso nuevo de `producir.yml`, antes del render**, lo resuelve: busca, descarga, guarda en
   caché, y apunta licencia, autor y enlace en `02_marca/banco/banco.json`. La red se usa **antes**
   del render, y el render sigue siendo determinista y sin red (regla 11.6).
3. **Si algo falla —la API no contesta, no hay resultado—, la escena sale como sale hoy.** Nunca se
   pierde un vídeo por una imagen.
4. **El render pinta el texto con fondo transparente** y `ffmpeg` lo compone encima del vídeo o la
   imagen de cada plano.
5. **`publicar.py` marca el vídeo como contenido sintético** (`status.containsSyntheticMedia`, que
   la API de YouTube admite) cuando lleva imágenes generadas, y la descripción dice de dónde sale
   cada cosa.
6. **La revisión diaria mira la hoja de contactos del Short de mañana**: que cada imagen cuente lo
   mismo que su frase, que nadie identificable salga en un contexto que le deje mal, y que no haya
   marcas ni texto dentro de la imagen.

### Lo que necesito del codirector, una sola vez

Tres cuentas gratuitas a nombre de la marca (Pexels, Pixabay y Cloudflare), sus claves como
secretos de GitHub, y crear a mano un workflow de prueba. Unos veinticinco minutos, explicados paso
a paso en `tareas_codirector_2026-09-23.md`. Es una intervención de puesta en marcha (regla 5), no
trabajo recurrente.

### El calendario

| Cuándo | Qué |
|---|---|
| Hoy, 23/09 | Decisión y diseño (esto). Código del resolvedor y de la prueba |
| En cuanto estén las claves | El workflow de prueba monta un **muestrario** con tres variantes sobre un guion real: **A** archivo + frase corta encima; **B** lo mismo con subtítulos palabra a palabra; **C** imágenes generadas con movimiento de cámara |
| Viernes 25 | **Lo mira el codirector y decide** (regla 11.2: se mira, no se imagina). También decide lo de los subtítulos |
| Semana del 28 | Entra en producción, en cuanto esté probado. Con suerte, el miércoles 30 |

**Sobre la regla 11.1.** El lunes 28 entra C44 (la voz), y C50 entra la misma semana. Son dos
cambios a la vez y no se podrá atribuir el resultado a uno de los dos. Lo digo y lo acepto: con
estos volúmenes la atribución fina no es posible de todos modos, y esperar una semana entre uno y
otro cuesta una semana de las ocho que quedan hasta el 15 de noviembre.

### Los riesgos, que son reales

- **El archivo huele a archivo.** Un plano de oficina de banco de imágenes es reconocible. Se mitiga
  eligiendo planos cortos y concretos (manos, objetos, caras en reacción) y mezclando con imágenes
  generadas. El muestrario lo dirá.
- **Una imagen que no cuenta lo que dice la frase es peor que ninguna.** Por eso la revisión mira
  la hoja de contactos cada día.
- **Personas reales en el archivo.** Las licencias prohíben usarlas de forma ofensiva o que las
  deje mal, y nosotros hablamos de defectos, fracasos y vergüenza. **Regla:** una persona
  identificable de archivo nunca ilustra una frase negativa sobre alguien («le dejó en ridículo»);
  para eso, objetos, manos, siluetas o imagen generada.

---

## C51 · El presentador de @Maestro_Seductor: cómo se hace, y por qué no ahora

**La petición, del 21/09 en `novedades.md`:** estudiar su último vídeo —un hombre «atractivo»
actuando el guion, con los labios perfectamente sincronizados con la voz—, saber cómo se ha
conseguido esa calidad y si podríamos replicarlo con la cara de una persona ficticia.

**Lo que he podido comprobar, y lo que no.** El vídeo es *«La Mentalidad para Atraer Sin Rogar»*,
de @Maestro_Seductor. **No he podido verlo**: YouTube rechaza la descarga automática de la página
y, aunque no lo hiciera, no tengo forma de analizar un vídeo fotograma a fotograma. Lo que sigue es
cómo se consigue hoy ese resultado, no una afirmación sobre qué herramienta usó él.

**Cómo se consigue.** El salto de calidad que notó el codirector es real y reciente. Las
herramientas de 2025-2026 (HeyGen Avatar IV, Hedra, OmniHuman, Kling Avatar, o los generadores de
vídeo con audio nativo como Veo 3) ya no pegan una boca sobre una cara grabada —que es lo que
producía la «disonancia» de sus vídeos anteriores—: generan **la cara entera, la cabeza y los
gestos a partir del audio**, así que la boca y todo lo demás van juntos. Y los Shorts con marca de
agua de OpusClip son el paso siguiente: un vídeo largo con el avatar, y OpusClip lo trocea solo en
Shorts; la marca de agua es la de su plan gratuito.

**Por qué no lo hacemos ahora. Son cuatro razones y cualquiera bastaría:**

1. **Coste.** Los planes gratuitos de esas herramientas dan del orden de **tres vídeos al mes con
   marca de agua**. Nosotros publicamos cinco a la semana. Regla 4.
2. **La vía gratuita existe, pero es la pieza más frágil que podríamos añadir.** Hay modelos
   abiertos que animan un retrato a partir del audio o cambian los labios de un vídeo (Hallo,
   EchoMimic, InfiniteTalk, LatentSync, MuseTalk), y todos necesitan una GPU. La única gratuita y
   automatizable es la de los cuadernos de Kaggle (unas 30 horas semanales), con una calidad por
   debajo de las comerciales.
3. **La regla 7: nada de fingir que hay una persona.** Una persona fotorrealista que no existe,
   presentando como si existiera, es exactamente eso, salvo que se diga con todas las letras; y
   YouTube exige declarar el contenido sintético realista. Se puede hacer bien, pero es una
   decisión tuya y no mía.
4. **Es el patrón que YouTube persigue**: presentador sintético, voz sintética, plantilla diaria.

Y una quinta que no es razón pero conviene decir: ese canal es de seducción, que es justo el tema
que la regla 1 nos prohíbe tratar como táctica. **De él copiaríamos la técnica, nunca el
contenido.**

**Lo que sí propongo, en este orden:**

1. **C50 primero.** Es el cambio grande y es gratis.
2. **Un paso intermedio, barato y nuestro: que el Engranaje hable.** Su boca movida por la voz real
   (por volumen o por fonemas), determinista, a coste cero y sin fingir nada: es un personaje
   dibujado y se ve que lo es. Da presencia de presentador sin la cara de nadie.
3. **Y si pasado el 15 de noviembre el canal sigue y quiere un presentador con cara humana**, una
   prueba con un modelo abierto en Kaggle, sobre un personaje ficticio y **declarado**. Esa
   decisión, la de la regla 7, es del codirector.

---

## Lo que NO cambia hoy

- **La voz no se toca hasta el lunes 28** (C44, capas A y B).
- **El punto de control del 27 y la decisión del 15 de noviembre** siguen igual, y la discusión de
  la puerta de los 1.000 sigue abierta hasta el 8 de noviembre.
- **El episodio largo sigue suspendido** (C42).
- **TikTok e Instagram** siguen donde los dejó C41.
- **`MDS-021` y `MDS-022` no se retiran.** Están publicados, se ven poco, y borrarlos no arregla
  nada: lo que se arregla es lo que viene. (Y retirarlos para que no cuenten en la mediana de C26
  sería hacerle trampas a nuestra propia regla.)

## Lo que queda mirado y sin resolver

- **La primera planificación con C48 es mañana, jueves 24.** El viernes 25 miro sus cinco
  lecturas en frío contra sus tesis, y el codirector lee los cinco guiones.
- **Por qué `MDS-016` hizo 1.210** sigue sin explicación. Hoy hay un indicio de contenido, no
  una explicación: en los tres Shorts que pasaron de 100 (`016`, `018` y `019`) la anécdota del
  principio **es** lo mismo que mide el estudio. Pero en `MDS-020` también lo era, y se quedó en
  27. No basta para explicar nada; basta para que C48 lo exija.
- `E02` (dos DOI), `F04` (sin sustituir) y P1 (sin respuesta desde el 14/09), como estaban.
