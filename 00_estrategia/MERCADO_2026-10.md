# El mercado de la divulgación en YouTube, y dónde estamos — octubre de 2026

**Encargo del codirector** (`PROMPT_DIRECCIÓN.md`, semana del 28/09): investigar a fondo el mercado de
YouTube de divulgación y entretenimiento basado en conocimiento —el marketing, cómo están hechos los
vídeos, qué funciona y qué no en cada pieza, y con más atención los canales automatizados— para
encontrar las diferencias con este canal y mejorar los números, no solo los procesos.

Escrito por la dirección el viernes 2 de octubre de 2026. Complementa a `DIAGNOSTICO.md` (agosto),
que comparaba con los grandes del formato largo; este mira sobre todo **el Short**, que es lo que
publicamos, y lo que ha cambiado en el mercado desde entonces. Las fuentes están al final.

---

## 0 · La conclusión, en diez líneas

1. **El guion ya está por encima del mercado; el envoltorio, por debajo.** La historia cosida, la
   lectura en frío y el cierre honesto no los tiene casi nadie en el nicho. Lo que nos separa de los
   que crecen son piezas baratas que rodean al guion: el primer segundo, el título, el final y la
   pregunta al espectador.
2. **Nuestros Shorts empiezan con 0,6 s de imagen congelada y un fundido desde negro**, y la voz entra
   a los 0,6 s. El mercado entero dice lo contrario: se empieza en movimiento y sin aire muerto.
3. **Las miniaturas no cumplen su función, y no por cómo son**: YouTube no las enseña donde importa.
   Lo que se ve de cada Short fuera del feed es **un fotograma del vídeo**: negro en el buscador,
   casi todo azul oscuro en la pestaña del canal.
4. **Nuestros títulos miden 74-98 caracteres; los Shorts en tendencia, 20-40.** El mejor título del
   canal, el de `MDS-016`, es también el más corto (45).
5. **El primer comentario lleva escrito desde agosto en cada Short y no se ha publicado nunca** (C20).
   Con cero comentarios en todo el canal y S3 como bloqueo, es la pieza más barata que tenemos parada.
6. **Los canales sin cara en español, con 400-700 vídeos, sacan 1.000-3.000 visualizaciones por
   Short.** Ese es el techo realista de nuestro formato a medio plazo, y queda muy por encima de los
   150 que pide C26. Por encima de eso ganan las caras (personas o personajes).
7. **El dinero no va a venir de los Shorts**: desde el 1/02/2027 hacen falta 10 millones de
   visualizaciones de Shorts cada 90 días para cobrar de ellos. «Sostenible» aquí significa coste
   cero, trabajo cero y una audiencia que justifique seguir; los ingresos, si llegan, vendrán del
   formato largo.
8. **El riesgo de ser «contenido no auténtico» es real para un canal como este**: YouTube cerró en
   enero 16 canales automatizados por publicar plantillas en serie. Lo que nos protege es lo mismo que
   nos diferencia, y conviene que se note también en la forma: variar formatos.
9. **Lo que se decide hoy** está en el apartado 5: títulos cortos y la pregunta al espectador, ya; el
   primer segundo y una llamada a seguir el canal, con el sí del codirector.
10. **Lo que no se toca antes del 15/11**: la cadencia (5 a la semana) y el formato largo. Los dos
    tienen argumentos para cambiar, pero cambiar ahora rompería la ventana de la decisión.

---

## 1 · Las dos preguntas del cuaderno

### 1.1 · La música de los días 1 y 2: no es azar ni un fallo, es el final de la vuelta

`cola.py` elige la pista por el número del Short: `pistas[(n - 1) % 14]`, con las 14 pistas en
orden alfabético (`cama.mp3` se descarta por ser copia de otra). Desde que el 18/09 entraron las
once nuevas, la rueda iba por ellas: `MDS-025` → `cama_11`, `026` → `cama_12`, `027` → `cama_13`,
`028` → `cama_14`. **`MDS-029` era el 29.º y la rueda volvió a empezar**: `cama_01` el día 1 y
`cama_02` el día 2, las dos primeras de las tres de siempre. Comprobado en la ficha de producción
de cada uno (`05_calendario/qa/MDS-0XX.es/ficha.json`, campo `musica.archivo`).

Lo que viene: **`MDS-031` (lunes 5) lleva `cama_03`, la tercera de las de siempre, y `MDS-032`
(martes 6) ya `cama_04`.** Cada pista vuelve cada 14 Shorts, casi tres semanas.

Si las tres originales no te gustan, se pueden sacar de la rueda (quedarían 11) sin tocar código:
basta con quitarlas de `creditos.json`. Te lo pregunto en la sesión.

### 1.2 · Las miniaturas: no cumplen su función, y el motivo no es el diseño

**Lo que hacemos.** `miniatura.py` dibuja para cada Short una portada vertical de color (ámbar,
cian, granate o hueso, por turnos) con el Engranaje y cuatro palabras, y `publicar.py` la sube con
`thumbnails.set()`. YouTube la acepta sin error.

**Lo que YouTube enseña de verdad** (medido hoy, píxel a píxel, sobre las imágenes que sirve
`i.ytimg.com` para doce Shorts del canal):

| Dónde se ve el Short | Qué imagen usa YouTube | Qué sale en la nuestra |
|---|---|---|
| **El feed de Shorts** (93-98 % de nuestras visualizaciones) | **Ninguna**: el vídeo arranca solo | — |
| La pestaña Shorts del canal, la estantería de Shorts de la portada | `oar2.jpg`, **un fotograma elegido por YouTube** | **90-95 % azul marino casi vacío** en los Shorts de plantilla (`MDS-016`, `022`, `025`…); un plano de archivo en los de C50 |
| La estantería de Shorts del buscador | `frame0.jpg`, **el primer fotograma** | **Negro al 100 %** en todos: el vídeo empieza con un fundido desde negro |
| Superficies horizontales (algunas listas, insertados, enlaces compartidos) | `hqdefault.jpg` | **La nuestra**, con bandas difuminadas a los lados |

Es decir: la portada que dibujamos solo aparece donde casi nadie mira, y donde sí se mira (el canal,
el buscador) sale un rectángulo oscuro. Para quien llega al canal después de un buen Short —los
cinco suscriptores nuevos, por ejemplo—, la pared de Shorts es una pared de rectángulos oscuros.

**Por qué.** Las miniaturas personalizadas de Shorts existen desde el **25 de julio de 2026**, pero
**primero solo para canales del Programa de Partners**, se suben desde Studio en el escritorio, no se
ven nunca en el feed y se recortan a una franja central de proporción 3:2. Nosotros no estamos en el
programa, así que YouTube guarda la nuestra y en las superficies verticales pone un fotograma.

**Qué se hace** (detalle en el apartado 5):

- **`miniatura.py` no se toca.** No cuesta nada, sirve en las superficies horizontales y el día que
  el canal entre en el programa habrá que adaptarla a la franja 3:2. Hasta entonces, pulirla no
  mueve nada.
- **La portada de verdad es el primer fotograma.** Quitar el fundido desde negro hace que el
  buscador enseñe la primera imagen del Short en vez de un rectángulo negro, y es, además, el
  arreglo del primer segundo (C58, abajo).

---

## 2 · Cómo funciona hoy el mercado (lo que ha cambiado desde agosto)

### 2.1 · El feed de Shorts reparte probando

- **Cada Short nuevo recibe una prueba**: unos cientos o un millar de visionados en el feed para ver
  si encuentra a su público. Si quien lo ve no se queda, la prueba se corta (Todd Sherman, jefe de
  producto de Shorts). Es lo que vemos: o 60-250, o 2-10.
- **La métrica que decide la prueba es «visto frente a deslizado»**: qué parte de quienes lo tienen
  delante no pasan al siguiente. Está en Studio y **la API no la da**: no la tenemos.
- **Desde el 31/03/2025 cualquier reproducción cuenta como visualización**, aunque sea medio
  segundo; las «visualizaciones con interacción» son aparte. Por eso el primer segundo pesa tanto:
  decide si la prueba sigue.
- **No hay duración ideal ni frecuencia que premie** (Sherman): «el público es el algoritmo». Lo que
  sí se mide es si se quedan, si lo repiten y si siguen viendo cosas después (el valor de la sesión).

### 2.2 · El Short medio, en cifras de 2026

Metricool, sobre 799.718 vídeos (julio de 2026): las visualizaciones de Shorts **subieron un 127 %**
y la duración media de visionado **bajó a unos 16 segundos**; el feed trae más del 61 % de las
visualizaciones orgánicas; **el rendimiento por vídeo es máximo publicando 2-4 a la semana**, y pasar
a 4-7 añade solo un 6 % de visualizaciones totales. Las cuentas pequeñas son las que más crecieron.

### 2.3 · El dinero

- **RPM de un Short: 0,01-0,07 $ por mil visualizaciones**; el formato largo, 2-10 $ (50-100 veces
  más).
- **Desde el 1 de febrero de 2027**: para entrar en el programa, 1.000 suscriptores y **8.000 horas**
  (antes 4.000) o **20 millones de visualizaciones de Shorts** en 90 días (antes 10). Y para cobrar
  publicidad de Shorts, **10 millones de visualizaciones de Shorts cada 90 días**, aunque ya estés
  dentro. El nivel bajo (500 suscriptores; 3.000 horas o 3 millones de Shorts) no cambia y solo da
  donaciones y tienda.
- **En ciencia, los canales que solo hacen formato largo tienen más suscriptores que los que mezclan
  Shorts** (AIR Media-Tech, 18.000 canales). En la audiencia hispana, el vídeo de 8-20 minutos es el
  que mejor equilibra retención y captación de suscriptores (2btube, 2026).

**Para nosotros:** el Short es la puerta, no la caja. A esta escala no paga nada y no va a pagar.
Si algún día hay ingresos, vendrán del formato largo, que hoy está suspendido (C42) con razón: el
que hicimos no funcionaba. Es una decisión para después del 15/11.

### 2.4 · La IA y los canales automatizados

- **Uno de cada cinco Shorts que ve una cuenta nueva es «AI slop»** (Kapwing, 500 Shorts de una
  cuenta recién creada). **España es el país con más suscriptores en canales de ese tipo**: ocho
  canales, 20,2 millones. Competimos en el mismo feed que ellos, y el espectador ya ha aprendido a
  deslizarlos al primer segundo.
- **La política de «contenido no auténtico»** (15/07/2025) castiga lo «producido en serie o
  repetitivo». En **enero de 2026 YouTube cerró 16 canales con unos 35 millones de suscriptores**
  por plantillas en serie; ninguno solo por usar IA. **Se permite** narrar con voz sintética un guion
  original, repetir una cabecera o un formato, y la animación con IA. **El patrón de alto riesgo**
  —canalización entera automatizada, guiones copiados, narración sintética, publicación diaria sin
  revisión— **se parece al nuestro en la forma** (automatizado, diario, la misma estructura en todos
  los vídeos), aunque no en el fondo: los guiones son originales, con fuente, y pasan una revisión.
- **Neal Mohan (carta anual de 2026):** YouTube va a reducir el alcance del contenido de baja calidad
  y repetitivo con los mismos sistemas que usa contra el spam.

**Para nosotros:** la regla 13.3 (nada de familia inventada, nada de fórmulas repetidas) ya va en
esa dirección. Falta llevarlo a la forma del canal: dos o tres formatos que se alternen, no uno solo
(lo que C55.2 empieza a hacer).

### 2.5 · La divulgación en español, hoy

Buscando «por qué nos reímos» en Shorts (2/10/2026):

| Short | Canal | Visualizaciones | Qué es |
|---|---|---|---|
| ¿Por qué nos reímos cuando alguien se cae? | Giuliana | **1,6 M** | Una persona, a cámara |
| ¿Por qué nos reímos ante situaciones incómodas? | La Hiperactina | **376 K** | Divulgadora conocida, cara y animación |
| ¿Por qué sonreímos y nos reímos los seres humanos? | AprendemosJuntos | 40 K | Una científica, a cámara |
| La ciencia detrás de una carcajada | Dentalk! | 11 K | — |
| ¿Por qué nos reímos con las cosquillas? | Aprende algo nuevo cada día | 4,3 K | Sin cara |
| El resto de los veinte primeros | varios | 2 – 3.300 | Sin cara en su mayoría |

Y dos canales sin cara de curiosidades, para medir el techo de nuestro formato:

| Canal | Suscriptores | Vídeos | Lo típico por Short |
|---|---|---|---|
| Aprende algo nuevo cada día | 32,9 K | 694 | **1.000 – 3.000** (mediana ~1.400) |
| El Qué, Cómo, Cuándo, Dónde y Por Qué | 2,8 K | 443 | **~1.000**, alguno por debajo de 100 |

Y en formato largo: **Psicología Animada**, psicología con animación y narración, 262.000
suscriptores con vídeos de unos cinco minutos, 1,5 a la semana.

Tres lecturas:

1. **Los temas que rompen son situaciones que todo el mundo reconoce en un segundo**: alguien que se
   cae, una situación incómoda, los nervios, las cosquillas. No el estudio: la escena.
2. **Por encima de unas miles de visualizaciones, ganan las caras**: personas o personajes. Es lo que
   ya decía `DIAGNOSTICO.md` (F4) y lo que persigue C51.
3. **El suelo es bajo para todos**: canales con 700 Shorts siguen sacando 1.000. Nadie en este nicho
   crece rápido sin cara; lo que distingue a los que crecen es la constancia y que cada Short pase su
   prueba en el feed.

---

## 3 · Anatomía de un Short que funciona, pieza a pieza, y dónde estamos

| Pieza | Lo que funciona en el mercado | Lo que hacemos | Distancia |
|---|---|---|---|
| **Primer fotograma y primer segundo** | Empezar en movimiento, sin aire muerto; el resultado antes que el cómo | 0,6 s de fotograma clonado + fundido desde negro de 0,4 s; la voz entra a los 0,6 s (`montaje.py`, decisión del 18/08 para que no «entrara en seco») | **Grande. Arreglo barato** |
| **Título** | 20-40 caracteres, 4-6 palabras, una curiosidad. En el reproductor de Shorts cabe, como mucho, una línea | 74-98 caracteres: la pregunta más un detalle del estudio («Ocho clases, dieciocho jubilados y una nota que se ponían ellos») | **Grande. Arreglo barato** |
| **Tema** | Una situación que se reconoce sin explicar | La ficha de la bibliografía primero; el gancho es el estudio | Media. Es C3 y C46 otra vez |
| **Historia** | Una pregunta, una respuesta | Cosido, lectura en frío, cierre honesto | **Ventaja nuestra.** Se mantiene |
| **Voz** | La voz sintética se acepta si el guion es original | Gemini, dirigida por escena | Bien |
| **Imagen y ritmo** | Cambio constante; personaje | Vídeo de archivo (C50) y, desde el 12/10, animación en las escenas de mecanismo (C55.2) | En marcha |
| **Cara o personaje** | Los que pasan de unas miles la tienen | El Engranaje solo en la firma; el presentador sintético, en estudio (C51.3) | Grande. En marcha |
| **Duración** | No hay óptima; el visionado medio son 16 s | 41-59 s. Los dos que mejor retienen duran 41-42; los de la semana que viene, 52-54 | Vigilar |
| **Final y bucle** | El final engancha con el principio y el vídeo se repite solo; las repeticiones cuentan | Fundido a negro de 0,6 s + 1 s de colchón + firma de marca: el bucle se nota | Grande. Para el lunes 5 |
| **Pregunta y llamada a la acción** | Una pregunta que el espectador puede contestar desde su vida; pedir que sigan el canal (en el experimento de Kapwing con un canal sin cara, «crítico») | El primer comentario se escribe y **no se publica nunca** (C20); no se pide nada | **Grande. Arreglo barato** |
| **Miniatura** | Solo cuenta fuera del feed | Ver 1.2: YouTube enseña un fotograma | Se arregla con el primer fotograma |
| **Cadencia** | 2-4 a la semana es lo mejor por vídeo; los grandes publican 2-6 al mes | 5 a la semana | Después del 15/11 |
| **Formato largo** | En ciencia, el que hace suscriptores e ingresos | Suspendido (C42) | Después del 15/11 |

---

## 4 · Nuestros números, con esto delante

Contadores públicos del canal, hoy a media tarde:

- **5 suscriptores** (eran 0 el 28/09). S4 empieza a moverse.
- **Semana de la imagen real (C50):** `MDS-026` 67 · `MDS-027` 66 · `MDS-028` **6** (a unas 46 h) ·
  `MDS-029` 10 (a unas 22 h). `MDS-030` sale hoy.
- **Semana anterior (plantilla):** `MDS-021` 147 · `022` 268 · `023` 2 · `024` 4 · `025` 67.
- `MDS-016`, 1.200.

**Lo que se puede decir y lo que no.** C50 no ha subido el número todavía: de momento, dos Shorts en
la banda de 60-70 y otro que el feed no probó. Con cuatro vídeos no se puede separar el efecto de la
imagen del de los temas. Lo que sí se ve es la forma: **o el feed nos prueba y sacamos 60-270, o no
nos prueba y sacamos 2-10.** Esa bifurcación se decide en el primer segundo y en la prueba del feed,
y es exactamente donde están los tres arreglos baratos del apartado 3.

---

## 5 · Lo que se decide

### Lo que decido hoy (versión 17 del plan)

- **C56 · Títulos: la pregunta, sola.** Como mucho 55 caracteres; el detalle del estudio pasa a la
  descripción. Los cinco Shorts de la semana del 5 (`MDS-031` a `035`) salen ya así. La planificación
  lo escribe así desde el jueves 8.
- **C57 · La pregunta al espectador, publicada de verdad.** Un comentario del canal con una pregunta
  que se pueda contestar desde la propia vida («¿cuál es la anécdota que ya no te hace gracia
  contar?»), no un resumen. Lo publica la sincronización diaria del registro cuando el Short ya es
  público: sin tocar workflows. Regla 7: es contenido editorial firmado por el canal y no responde a
  nadie.
- **Miniaturas:** no se tocan (1.2).
- **Lo que no cambia antes del 15/11:** cinco Shorts a la semana y el formato largo suspendido.
  Cambiar la cadencia ahora metería en la ventana de veinte de C26 los Shorts de estas semanas;
  volver al largo sin un formato nuevo es repetir lo que no funcionó.

### Lo que te pregunto (cambia cómo se ve o se oye el canal)

- **C58 · El primer segundo sin negro**: quitar el fundido de entrada y dejar el colchón inicial en
  una décima, solo en Shorts. Cambia una decisión tuya del 18/08.
- **C59 · Una llamada a seguir el canal**: una línea en pantalla en la firma final, sin voz.
- **La música**: sacar o no de la rueda las tres pistas de siempre.

### Para el lunes 5

- **El bucle**: que la última frase empalme con la primera y el vídeo no cierre a negro.
- **«Visto frente a deslizado»**: una sola consulta tuya en Studio de los últimos diez Shorts. Es el
  único dato que separa «el primer segundo espanta» de «el feed no nos prueba».
- **Después del 15/11, para pensarlo con tiempo**: menos Shorts y mejores, y un formato largo nuevo.

---

## 6 · Fuentes

- YouTube Shorts y miniaturas personalizadas (25/07/2026): [PPC Land](https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/) · [Relevant Audience](https://www.relevantaudience.com/social-media-marketing/youtube-shorts-custom-thumbnails-no-ab-testing/)
- Cómo reparte el feed (Todd Sherman): [Search Engine Journal](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/) · [Net Influencer](https://netinfluencer.com/?p=21933)
- Cambio del recuento de visualizaciones (31/03/2025) y RPM: [Gyre](https://gyre.pro/blog/youtube-shorts-view-count-update-impact-strategy-what-to-do-next)
- Estudio de 799.718 vídeos: [Metricool, YouTube Trends 2026](https://metricool.com/youtube-trends/)
- Programa de Partners desde el 1/02/2027: [NewscastStudio](https://www.newscaststudio.com/2026/08/10/youtube-partner-program-monetization-changes-2027/)
- Shorts y formato largo en 18.000 canales: [AIR Media-Tech](https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels)
- Audiencias hispanas 2026: [2btube](https://2btube.com/en/?p=16957)
- «AI slop» en el feed: [The Decoder, sobre el estudio de Kapwing](https://the-decoder.com/one-in-five-youtube-shorts-shown-to-new-users-is-ai-generated-slop-study-finds/)
- Contenido no auténtico y cierres de enero de 2026: [ytgrowth](https://ytgrowth.io/blog/youtube-ai-policy) · Carta de Neal Mohan: [Variety](https://au.variety.com/2026/digital/global/youtube-channels-using-ai-tools-reduce-slop-neal-mohan-letter-32190/)
- Experimento de canal sin cara hasta 1.000 suscriptores: [Kapwing](https://www.kapwing.com/resources/we-grew-a-faceless-youtube-channel-to-1000-subscribers/)
- Títulos de Shorts en tendencia: [TunePocket](https://www.tunepocket.com/youtube-shorts-video-titles/) · Bucles: [vidIQ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/) · Señales del feed: [Deeside](https://www.deeside.com/the-shorts-recommendation-loop-a-practical-map-of-signals-you-can-actually-influence/)
- Humor en la divulgación científica en YouTube: [Bernad-Mechó y Girón-García, 2023](https://europeanjournalofhumour.org/ejhr/article/view/760)
- Canales de referencia: [Psicología Animada (vidIQ)](https://vidiq.com/youtube-stats/channel/UCTjR-pXR-vZo3dgIjGcYLgQ) · [Psych2Go (OutlierKit)](https://outlierkit.com/channel/psych2go)
- Medido por la dirección el 2/10/2026: contadores públicos del canal y de los canales comparados, búsqueda de YouTube «por qué nos reímos» (filtro Shorts) e imágenes `oar2`, `frame0` y `hqdefault` de `i.ytimg.com`.

Las cifras de terceros (Metricool, AIR, 2btube, Kapwing) son de empresas que venden herramientas
para creadores: sirven como orden de magnitud, no como verdad exacta. Las de Sherman y las de la
política de YouTube son de primera mano.
