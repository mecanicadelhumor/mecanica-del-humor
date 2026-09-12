# Plan de cambios — Mecánica del Humor

**Versión 3 · 21 de agosto de 2026** — con las decisiones tomadas y la fase 1 y
media de la fase 2 ya escritas en el repositorio.

> ⚠️ **La versión que manda es la 5, al final de este documento (4 de
> septiembre).** La 4 (31 de agosto) sustituyó la escalera de métricas de C14 por
> dos escaleras —una para Shorts y otra para el episodio largo— y añadió C17 a
> C20. La 5 resuelve la caducidad del token de YouTube, pone la primera barrera
> real antes de publicar, cambia el rumbo de C7 y añade C21 a C23. **Si vas a
> decidir algo con este plan, lee las dos secciones finales antes.**

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
  tocan sin permiso explícito del codirector en la conversación.

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
