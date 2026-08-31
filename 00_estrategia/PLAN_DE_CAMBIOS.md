# Plan de cambios — Mecánica del Humor

**Versión 3 · 21 de agosto de 2026** — con las decisiones tomadas y la fase 1 y
media de la fase 2 ya escritas en el repositorio.

> ⚠️ **Hay una versión 4, al final de este documento (31 de agosto).** Sustituye
> la escalera de métricas de C14 por dos escaleras —una para Shorts y otra para el
> episodio largo— y añade C17 a C20. Si vas a decidir algo con este plan, léela
> antes: la primera lectura con datos cambió el orden de la cola.

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
- Los archivos marcados como **protegidos** (`voz.py`, `montaje.py`, `producir.yml`) no se
  tocan sin permiso explícito de Silvestre en la conversación.

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

Silvestre autoriza cambiarlo todo salvo las reglas fijas de `REGLAS.md`.

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

Silvestre acepta grabar su voz para clonarla **con la condición de que el modelo y la
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
hoy exigiría relajar la condición que Silvestre puso.

**Lo que sí se hace, y resuelve el mismo problema:** el escalón 2 de C7, Gemini TTS con
dos hablantes y control de expresión por prompt, con la `GEMINI_API_KEY` que ya está en
los secretos. Rompe la cadencia fija, da al canal una voz reconocible y mete al escéptico,
que es donde vive el humor. Sin datos personales de nadie y sin GPU.

**Cuándo se reabre la clonación:** si a las ocho semanas la voz sigue siendo lo que peor
funciona, hay dos caminos limpios — renderizar el audio en el ordenador de Silvestre y
subir solo el resultado, o pagar minutos privados de Actions — y entonces sí se le pide la
grabación. No antes.

---

# FASE 0 · Desbloquear

Nada de lo demás sirve si la producción no corre.

## P0.1 · Averiguar por qué Actions lleva dos días callado

**Solo lo puede hacer Silvestre.** Abrir la pestaña *Actions* del repositorio
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

### Lo que hace Silvestre (una vez, 15 minutos)

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
con `lineas_ass: 793` — y Silvestre decidió **retirarlos**: palabra a palabra, en la banda
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

| Canal | Qué se publica | Automatizable | Setup de Silvestre |
|---|---|---|---|
| **TikTok** | el mismo archivo vertical | sí, API de contenido | crear cuenta de marca |
| **Instagram Reels** | el mismo archivo vertical | sí, Graph API | crear cuenta de marca + vincular |
| **Bluesky / Mastodon** | un hallazgo al día + enlace al estudio | sí, API abierta | crear cuenta de marca |
| **Pódcast (Spotify)** | el audio que ya existe | sí, RSS generado por el workflow | dar de alta el RSS una vez |

**Todas las cuentas a nombre de Mecánica del Humor, ninguna a nombre de Silvestre.**

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
dependía de que Silvestre exportara un CSV a mano cada semana, que es trabajo
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

**El hallazgo, de Silvestre:** «en el vídeo hay cosas que se repiten, como que te
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
notó primero Silvestre, que hoy por hoy es el espectador que más vídeos ve.

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
  Decisión de Silvestre del 31/08, tomada con la audiencia actual delante: un mal
  vídeo hoy no cuesta nada, y él lo puede retirar. Se revisa cuando haya público.
