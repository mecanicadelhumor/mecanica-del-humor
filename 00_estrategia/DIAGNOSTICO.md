# Diagnóstico y estrategia — Mecánica del Humor

**Fecha:** 20 de agosto de 2026
**Estado del canal analizado:** 4 vídeos publicados (2 ES, 2 EN), ~20 visualizaciones totales, parte de ellas del propio autor.
**Ámbito:** por qué el canal no arranca, qué hacen los que sí lo consiguen, y qué cambiar.

> Este documento explica **por qué**. El **qué hacer**, en orden y con criterios de
> aceptación, está en `PLAN_DE_CAMBIOS.md`. Las restricciones que ningún agente puede
> saltarse están en `REGLAS.md`. Los tres se leen juntos.

---

## 0. La conclusión, antes de las 6.000 palabras

**El canal no tiene un problema de calidad. Tiene un problema de distribución, y la
arquitectura actual lo garantiza.**

Los vídeos están bien hechos. La bibliografía es real, el verificador tiene veto, el
audio está normalizado a −14 LUFS, la tipografía se corrigió, la viñeta se movió detrás
del texto y se midió el cambio de contraste al decimal. Ese nivel de cuidado es
inhabitual y no hay que tirarlo.

Pero para un canal con 0 suscriptores, YouTube solo tiene tres formas de enseñar un
vídeo a alguien:

1. **Búsqueda** — alguien escribe algo y tu vídeo responde.
2. **El feed de Shorts** — el único sitio donde no hace falta tener público previo.
3. **Enlaces desde fuera** — Google, otra red, una web.

El sistema actual no usa **ninguna de las tres**. Los títulos no responden a ninguna
búsqueda real, no hay un solo Short, y no existe ninguna entrada desde fuera de YouTube.
Los cuatro vídeos se publicaron en una superficie —el feed de recomendaciones— a la que
solo se accede teniendo ya audiencia.

Nueve visualizaciones no es un veredicto sobre los vídeos. Es la consecuencia aritmética
de publicar donde nadie puede verte.

Y hay un segundo problema, más incómodo: **la optimización que hace posible el coste cero
es exactamente la que destruye la retención.** `render.py` captura solo los fotogramas en
los que algo se mueve y estira el resto — por eso un vídeo de siete minutos cabe en los
minutos gratuitos de Actions. Pero el consenso técnico sobre retención en vídeo sin cara
es que **la pantalla tiene que cambiar cada 3–5 segundos**. El diseño del render y el
requisito de retención están en conflicto directo, y el sistema eligió el coste. El
propio control de calidad del 18 de agosto lo escribió: *«el vídeo se percibe como un
pase de diapositivas»*.

Los dos problemas tienen solución sin gastar un euro y sin poner a nadie a trabajar todas
las semanas. Eso es lo que viene a continuación.

---

## 1. Los canales de referencia

### 1.1 Cómo los he elegido

Un ranking de «canales de humor» no sirve de nada aquí: los grandes son cómicos con cara,
equipo y una década de ventaja. Para que la comparación enseñe algo, los candidatos tienen
que cumplir cuatro condiciones:

- **Materia adyacente** — psicología aplicada, habilidades sociales, o «cómo funciona algo»
  explicado con rigor. No comedia pura.
- **Sin cara, o casi** — para que el éxito sea replicable por un canal que no puede poner a
  una persona delante de una cámara.
- **Grandes de verdad** — millones de suscriptores, para que no sea casualidad.
- **En los dos idiomas** — porque el mercado español y el inglés no funcionan igual.

### 1.2 En inglés

| Canal | Suscriptores | Vídeos | Vistas totales | Formato | Por qué está aquí |
|---|---|---|---|---|---|
| **Psych2Go** | 13,1 M | 4.050 | 2.140 M | Animación 2D con personajes + narración | Psicología divulgada sin una sola cara real |
| **The School of Life** | 9,77 M | 1.230 | 999 M | Ilustración + narración culta | El tono más cercano al de Mecánica del Humor |
| **Charisma on Command** | 7,09 M | **442** | 832 M | Voz en off sobre clips de gente famosa; el presentador apenas sale | **El análogo exacto**: habilidades sociales desmontadas pieza a pieza |
| **Improvement Pill** | 3,77 M | 356 | 228 M | Muñecos de palo animados | Autoayuda con estructura, sin producción cara |

*(vidIQ, agosto de 2026.)*

**Charisma on Command merece un párrafo aparte.** Es el canal más parecido a lo que
Mecánica del Humor quiere ser: enseña una habilidad social explicando su mecanismo, sin
cara, con voz en off y montaje analítico. Y su fundador ha explicado públicamente cuál
fue la decisión que lo cambió todo: lo que él llama **«fame-jacking»** — dejar de hacer
vídeos sobre *el carisma* y empezar a hacerlos sobre *por qué cae bien esta persona
concreta que ya te interesa*. El vídeo de 2016 analizando a Trump «triplicó el negocio».

No inventaron demanda. Se engancharon a demanda que ya existía. Con **442 vídeos en doce
años** — unos tres al mes.

### 1.3 En español

| Canal | Suscriptores | Vídeos | Vistas totales | Formato | Por qué está aquí |
|---|---|---|---|---|---|
| **QuantumFracture** | 4,02 M | 620 | 713 M | Animación + voz en off; la cara es la excepción | Ciencia dura hecha entretenida en español |
| **Academia Play** | 3,76 M | 770 | 578 M | Ilustración + voz en off, sin cara | El faceless español de mayor recorrido |
| **VisualPolitik** | 3,78 M | 1.340 | 815 M | Voz en off + gráficos + metraje | Estructuralmente idéntico al pipeline de MDH |
| **Memorias de Pez** | 2,95 M | 1.140 | 599 M | Voz en off + ilustración | Divulgación de nicho, sin cara |
| **La Hiperactina** | 1,92 M | — | — | Cara + animación | Neurociencia en español |
| **Pero eso es otra historia** | 1,78 M | — | — | Voz en off + ilustración | Narrativa histórica sin cara |

*(vidIQ agosto 2026 para los cuatro primeros; 2btube, enero de 2024, para los dos
últimos — cifras algo desactualizadas, probablemente por lo bajo.)*

**VisualPolitik es la prueba de concepto más directa.** Es literalmente lo que hace
Mecánica del Humor —voz en off sobre gráficos y texto en pantalla, sin cara, producción
industrializada— y tiene 3,78 millones de suscriptores y 7,45 millones de vistas en los
últimos treinta días. El formato **no** es el problema. Lo que VisualPolitik tiene y
Mecánica del Humor no es que cada vídeo suyo responde a algo que la gente ya se está
preguntando esa semana.

### 1.4 Lo que NO existe, y qué significa

Buscando en español «ciencia del humor», «psicología del humor», «por qué nos reímos»,
lo que aparece son episodios sueltos de podcasts, charlas de psicólogos y Shorts de
divulgadores generalistas. **No hay un canal español que sea el sitio al que vas cuando
te interesa esto.** El hueco es real.

Pero conviene entender bien qué clase de hueco es, porque aquí está la trampa que se ha
comido al canal:

> **Un nicho de oferta no es lo mismo que un nicho de demanda.**
>
> «La ciencia del humor» es un nicho de oferta: está definido por lo que el creador quiere
> hacer. Nadie escribe «ciencia del humor» en el buscador de YouTube.
>
> «Cómo ser más gracioso», «por qué nos reímos», «cómo tener sentido del humor», «por qué
> no le hago gracia a nadie» sí se escriben. Ahí sí hay vídeos, y son en su mayoría
> mediocres: charlas grabadas, coaching sin fuentes, consejos recalentados.

Eso deja al canal en la mejor posición posible **si cambia de qué lado lo mira**: hay
demanda real, la competencia es floja, y la única ventaja que Mecánica del Humor tiene
sobre esos vídeos —77 obras curadas y un verificador con veto— es exactamente la que esa
audiencia no está recibiendo de nadie.

---

## 2. Qué tienen en común los que triunfan

Siete factores. Cada uno viene con la evidencia y con qué implica para este canal.

### F1 · No compiten por el tema. Se enganchan a una pregunta que la gente ya se hace

Charisma on Command no hace «la ciencia del carisma». Hace «por qué todo el mundo quiere
caerle bien a esta persona». QuantumFracture no hace «relatividad general», hace «qué
pasaría si cayeras en un agujero negro». La materia es la misma; el punto de entrada, no.

La demanda es un recurso que ya existe y que no se fabrica. Los canales que crecen la
localizan y se enganchan a ella. Los que no crecen esperan a que la demanda venga a
buscar su tema.

### F2 · El empaquetado es la mitad del trabajo, y obedece reglas medibles

Según el análisis de vidIQ sobre vídeos que rompen (*breakout*):

- **69 %** de los vídeos que rompen llevan una **cara humana** en la miniatura. Entre los
  que más rompen, **80 %**.
- **89 %** llevan **cara o color de altísimo contraste**. Una de las dos, siempre.
- La mediana de texto en miniatura es de **cinco palabras o menos**.
- Solo un **5 %** usan expresiones exageradas. No es cuestión de gritar; es cuestión de
  que se vea.

Ese 89 % es la cifra importante para un canal sin cara: **si renuncias a la cara, el
contraste deja de ser opcional.**

### F3 · La pantalla cambia cada 3–5 segundos

La regla estándar de montaje de retención para vídeo sin cara: algo tiene que cambiar en
pantalla cada 3–5 segundos. No cortes frenéticos —un texto que entra, una gráfica que se
construye, un empuje lento sobre una imagen quieta cuentan como cambio—. El ojo necesita
algo que hacer.

Referencias de retención de 2026: la media de un canal educativo está en el **42 %**; en
vídeos de 5 a 10 minutos, el rango «bueno» es **50–70 %**. Un pase de diapositivas con voz
sintética no llega a la media, y por debajo de la media YouTube no reparte impresiones.

### F4 · Sin cara no significa sin personaje

Kurzgesagt tiene sus pájaros. Psych2Go tiene sus personajes. Improvement Pill tiene sus
muñecos de palo. Ninguno enseña una cara real y **todos tienen una cara**.

Esta es la línea que separa «canal sin cara» de «basura generada»: un personaje recurrente
demuestra que detrás hay una decisión creativa sostenida en el tiempo. Una plantilla
demuestra lo contrario.

### F5 · El formato demuestra lo que enseña

QuantumFracture explica física con visuales que se comportan como la física. Charisma on
Command es, él mismo, carismático. Kurzgesagt explica la escala del universo con
animaciones cuya escala te marea.

**Un canal sobre humor que no hace gracia es una contradicción que el espectador nota en
el segundo doce, aunque no sepa nombrarla.** Es el problema editorial más grave de
Mecánica del Humor y ninguna mejora técnica lo arregla.

### F6 · Publican mucho menos de lo que parece

| Canal | Vídeos | Años | Vídeos/mes |
|---|---|---|---|
| Charisma on Command | 442 | 12 | ~3 |
| Improvement Pill | 356 | 11 | ~2,7 |
| Academia Play | 770 | 11 | ~6 |
| QuantumFracture | 620 | 14 | ~3,7 |
| Psych2Go | 4.050 | 12 | ~28 |

Psych2Go es la excepción, tiene un equipo detrás y se ganó el derecho al volumen después
de una década. Los demás sostienen millones de suscriptores publicando **dos o tres veces
al mes**.

Mecánica del Humor pasó el 19 de agosto a **publicar a diario en dos idiomas** —más que
cualquiera de estos canales— teniendo cero datos sobre si algo funciona. El razonamiento
escrito en `CALENDARIO.md` («la parrilla original solo servía para retrasar el momento de
saber si el canal funciona») es correcto en su intención y equivocado en su medio: publicar
más rápido no acelera el aprendizaje si ninguno de los vídeos llega a nadie. Solo acelera
el gasto.

### F7 · Tienen puerta de entrada desde fuera de YouTube

Charisma on Command tiene un curso y una lista de correo. The School of Life tiene libros
y una web enorme. VisualPolitik tiene web, pódcast y presencia en varias plataformas.
Ninguno depende solo de que el algoritmo se acuerde de ellos.

---

## 3. Diagnóstico del canal, causa por causa

Ordenadas por cuánto cuesta cada una en visualizaciones perdidas.

### D1 · Dos canales desde cero dividen una señal que ya era cero

Cada canal arranca su propio periodo de prueba con el algoritmo, por separado. Las 16
subidas previstas no son 16 señales: son dos veces ocho, en dos historiales distintos,
ninguno de los cuales llega al umbral en el que YouTube empieza a entender de qué va el
canal.

Y hay un dato que cambia la ecuación entera: **desde febrero de 2026 el doblaje automático
de YouTube está disponible para todos los creadores del mundo, gratis, en 27 idiomas**, con
mejora de «voz expresiva» —que imita tono, entonación y energía— disponible en español.
Se activa una vez en *Studio → Configuración → Valores predeterminados de subida →
Configuración avanzada*.

Es decir: hoy, mantener dos canales para servir a dos idiomas es estrictamente peor que
mantener uno con pistas de audio múltiples. Se paga el doble de arranque en frío a cambio
de algo que la plataforma regala.

Añádase que el canal inglés compite contra Charisma on Command, The School of Life y
Psych2Go, y el español no compite prácticamente contra nadie.

> **Matiz honesto:** el proyecto decidió *readaptar* al inglés en vez de traducir, y tiene
> razón — un chiste traducido literal deja de ser un chiste, y el propio incidente del
> «hombre entra en un bar» del 19 de agosto lo demuestra. El doblaje automático heredará
> ese problema. Por eso la propuesta no es «doblar y ya está», sino: consolidar ahora para
> sobrevivir, usar el doblaje como sonda barata para ver si hay demanda inglesa, y
> reabrir el canal inglés con readaptación real cuando el español funcione. Ver C1.

### D2 · Los temas los elige la bibliografía, no la demanda

El sistema funciona así: hay 77 obras curadas en doce pilares, y el calendario se construye
eligiendo de ahí. Es un método impecable para garantizar rigor y pésimo para conseguir
espectadores, porque **la pregunta «¿qué puedo demostrar?» no es la pregunta «¿qué quiere
saber alguien?»**.

El resultado se ve en los títulos:

| Título actual | Búsquedas que responde |
|---|---|
| «Nadie nace gracioso — lo que 50 años de investigación han medido de verdad» | ninguna |
| «Por qué te ríes: las dos condiciones que cumple cualquier chiste» | «por qué nos reímos», parcialmente |
| «Nobody Is Born Funny — What 50 Years of Research Actually Found» | ninguna |

Son títulos de ensayo. Están bien escritos. Nadie los escribe en un buscador.

La búsqueda es una de las dos únicas superficies que un canal de cero suscriptores puede
alcanzar, y además es la de mayor intención: quien busca tiene un problema concreto.
Renunciar a ella es renunciar a la mitad de lo poco que hay.

### D3 · Cero Shorts. Es la otra superficie, y es la más grande

Referencia de agosto de 2026: **un canal con menos de 1.000 suscriptores obtiene entre 50 y
500 visualizaciones por Short en las primeras 48 horas.**

Los vídeos largos de Mecánica del Humor están sacando entre 1 y 9.

El feed de Shorts es el único sitio de YouTube donde el reparto no depende de tu historial
ni de tus suscriptores: depende de si los tres primeros segundos retienen. Es la puerta
diseñada para gente que no tiene público.

Y lo mejor: **el pipeline actual ya puede producirlos sin infraestructura nueva.** Los
requisitos de 2026 son ≤180 segundos y 9:16, y la clasificación como Short es
**automática** al subir por la API — no hay casilla, no hace falta la etiqueta `#shorts`.
Es un cambio de viewport en `escena.html` y un esquema de guion más corto. Coste marginal:
cero.

### D4 · Las miniaturas incumplen las dos condiciones a la vez

He mirado las que hay. Fondo azul marino muy oscuro (`#0B1220` aproximadamente), texto
blanco y ámbar, retícula tenue, sin cara y sin ningún color de alto contraste. Son
elegantes. En una cuadrícula de YouTube, junto a doce miniaturas saturadas, desaparecen.

Recordando el dato: 89 % de los vídeos que rompen llevan **cara o contraste extremo**. Estas
no llevan ninguna de las dos. Es la única decisión de diseño del proyecto que está
objetivamente contra la evidencia.

### D5 · La arquitectura de render está optimizada contra la retención

Este es el hallazgo más importante del análisis técnico, y no es culpa de nadie: es una
consecuencia lógica de una restricción real.

`render.py` divide cada escena en entrada, centro y salida. Captura la entrada y la
salida fotograma a fotograma, y del centro captura **una sola imagen que FFmpeg estira**.
Por eso 2.043 capturas bastan donde harían falta 13.350, y por eso una producción entera
cabe en los minutos gratuitos de Actions. Es ingeniería excelente.

Y el centro es la mayor parte del vídeo. Es decir: **durante la mayor parte de los siete
minutos, la pantalla está literalmente congelada**, mientras la regla de retención pide
cambio cada 3–5 segundos.

El documento `MEJORA_VISUAL.md` ya identificó la única cosa que se mueve en el tramo
central —los subtítulos quemados palabra a palabra— y el registro del 19 de agosto
confirmó que **llevan sin funcionar desde el principio**: `lineas_ass: 0`, porque
`edge-tts` dejó de devolver eventos `WordBoundary`. O sea que los vídeos publicados no
tenían ni siquiera ese movimiento.

El arreglo está en el repositorio desde el 19 y **no se ha llegado a ejecutar nunca**,
porque la producción que debía estrenarlo no corrió.

### D6 · Una voz sintética sola durante siete minutos

`edge-tts` produce audio correcto. El problema no es el timbre, es la **cadencia fija**:
un ritmo idéntico durante siete minutos es uno de los factores que más drenan retención
en vídeo sin cara, junto con los silencios internos de más de medio segundo.

Y es una oportunidad desaprovechada: un canal sobre humor narrado por una sola voz neutra
está renunciando al recurso cómico más barato que existe, que es que alguien conteste.

### D7 · Hay un riesgo de política, no solo de crecimiento

Esto merece atención porque no aparece en ningún documento del proyecto.

El **16 de julio de 2026** YouTube aclaró su política de contenido no auténtico (renombrada
desde «contenido repetitivo» en julio de 2025). Queda fuera del Programa de Socios el
contenido **«genérico, repetitivo o basado en plantillas»** y, textualmente, el
**«contenido generado por IA hecho con plantillas genéricas o poco originales que dan la
impresión de producción en masa»**. En mayo de 2026 entró en vigor la **detección
automática de IA**: el contenido de IA sin etiquetar se marca solo.

Un canal que publica a diario vídeos renderizados desde una única plantilla HTML, con nueve
tipos de escena, la misma voz sintética y la misma retícula de fondo, encaja en esa
descripción **por su apariencia**, independientemente de lo bueno que sea el guion.

La buena noticia es que la política dice también qué se salva: se permite explícitamente
la IA usada para «ofrecer una narrativa única, bien documentada o creativa», y el contenido
de calidad hecho con ayuda de IA. Mecánica del Humor tiene ya lo difícil —tesis propia,
fuentes reales, un verificador con poder de veto—. Lo que le falta es **no parecer** lo que
no es. Los cambios C4, C6 y C7 atacan justamente eso.

### D8 · El canal habla de humor sin ser gracioso

Es el problema del que no se sale con ingeniería.

Los guiones son buenos como ensayo: tesis, mecanismo, matices, y un cierre honesto que
dice dónde falla lo que se acaba de explicar. Ese criterio editorial —recogido en
`SIGUIENTES_PASOS.md` y que recomiendo mantener íntegro— es la mejor decisión del
proyecto.

Pero un vídeo que *explica* la teoría de la ruptura benigna sin *provocar* una sola ruptura
benigna está pidiendo al espectador que se fíe de una promesa que el propio vídeo no
cumple. Los canales de F5 no explican su materia: la ejecutan mientras la explican.

Traducción operativa: **cada vídeo tiene que hacer reír al menos dos veces, y una de ellas
en los primeros quince segundos.** No como adorno. Como demostración.

### D0 · Además, y urgente: la producción lleva dos días sin correr

No es estrategia, pero bloquea todo lo demás. Según el registro del 20 de agosto: el 19
faltó el vídeo inglés, el 20 no salió nada, no hay commits nuevos, y el flujo de vista
previa tampoco se ha ejecutado pese a haber recibido *push* en sus rutas de disparo. Dos
workflows callados a la vez apunta a Actions parado —cuota, workflows deshabilitados o
repositorio en pausa—, no a un fallo de código.

**Comprobación de treinta segundos que solo puede hacer Silvestre:** abrir la pestaña
*Actions* del repositorio. Si no hay ejecución de hoy, el problema es de habilitación o
cuota. Si la hay y falla, el paso «Recuperar el plan» dice si el plan traía uno o dos
trabajos.

---

## 4. La estrategia

### 4.1 La idea en una frase

**Dejar de publicar ensayos donde nadie mira y empezar a demostrar el humor donde todo el
mundo mira, manteniendo intacto el rigor que hace que el canal merezca existir.**

### 4.2 Los tres cambios de los que depende todo

Si solo se hicieran tres cosas, estas:

1. **Un canal, no dos.** Consolidar en español y usar el doblaje automático gratuito
   para probar el inglés sin pagar un segundo arranque en frío.
2. **Shorts a diario, vídeo largo semanal.** Cambiar la puerta de entrada. Es donde
   pasa de 1–9 visualizaciones a 50–500 sin producir nada nuevo desde cero.
3. **Un personaje y unas miniaturas que se vean.** La cara que un canal sin cara necesita,
   dibujada en el mismo lenguaje de plano técnico que ya existe, y miniaturas que cumplan
   la regla del 89 %.

Los otros once cambios amplifican estos tres. Ninguno de los catorce cuesta dinero.

### 4.3 Los catorce cambios

Cada uno está detallado, con archivos y criterios de aceptación, en `PLAN_DE_CAMBIOS.md`.
Aquí va el razonamiento.

---

#### C1 · Un solo canal, con doblaje automático

Pausar `@humormechanics` (no borrarlo: el handle se conserva y el canal se reabre cuando
haya con qué). Todo pasa a `@mecanicadelhumor`. Se activa el doblaje automático en Studio,
una sola vez, cinco minutos.

**Por qué:** deja de pagarse dos arranques en frío. El inglés se prueba gratis. Si las
pistas dobladas generan tiempo de visionado en inglés, hay demanda y se reabre el canal
con readaptación de verdad; si no, se ha ahorrado la mitad del trabajo.

**Aviso técnico:** las pistas de audio multilingües **no están en la API de datos v3**. El
doblaje automático es un ajuste de Studio que se aplica en la subida, y eso sí es
automatizable de facto: se configura una vez y actúa solo en todas las subidas siguientes.

---

#### C2 · Shorts como puerta de entrada, durante 90 días

Cinco Shorts por semana, un vídeo largo por semana. El Short **no es un recorte del vídeo
largo**: es una pieza nativa, completa en sí misma, con su propio remate.

**Cinco formatos repetibles**, diseñados para que un agente pueda escribirlos sin
supervisión y para que el propio formato demuestre la tesis del canal:

1. **«Desmonta el chiste»** — 40 s. Se cuenta un chiste. Dos segundos de silencio. Aparece
   el despiece: qué expectativa se rompió, por qué fue inofensiva, dónde estaba la bisagra.
   Es literalmente la marca del canal en cuarenta segundos.
2. **«Ríete primero, te explico después»** — 30 s. El chiste va en el segundo cero. La
   explicación es el premio. El vídeo *es* la demostración de que la teoría funciona.
3. **«El experimento»** — 45 s. Un estudio real con resultado contraintuitivo, contado
   como una historia, rematado con la cifra en pantalla y el DOI en la descripción.
4. **«Esto no tiene gracia y esto sí»** — 35 s. Dos chistes casi idénticos, uno funciona y
   otro no. El espectador nota la diferencia antes de que se la expliquen. Motor de
   comentarios: la gente discute cuál es cuál.
5. **«Diagnóstico en 30 segundos»** — «si haces esto, tu humor es de este tipo». Contenido
   de identidad, el que más comentarios genera, siempre atado a la taxonomía real de
   estilos de humor del pilar B de la bibliografía, no a un test inventado.

**Coste:** cero. `escena.html` con viewport 1080×1920, un esquema `guion_short.json`, y
`publicar.py` sin tocar (la clasificación como Short es automática).

**Por qué funciona aquí y no es una rendición:** el Short obliga a lo que al canal más le
falta —densidad, remate, gracia— y castiga lo que le sobra: el preámbulo.

---

#### C3 · Elegir los temas por demanda, filtrarlos por bibliografía

Un agente nuevo, `explorador_de_demanda.py`, que corre semanalmente en Actions y consulta,
todo gratis y sin claves:

- **Autocompletar de YouTube** — `suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=<semilla>`
  devuelve las búsquedas reales que empiezan por una semilla. Sin API key, sin coste.
- **Google Trends** vía `pytrends`, para interés relativo y estacionalidad.
- **Los comentarios** de los propios vídeos y de los vídeos competidores, vía la API de
  datos (barata en cuota).
- **Los JSON públicos de Reddit** (`r/AskReddit`, `r/standup`, subreddits en español) para
  detectar cómo formula la gente la pregunta con sus propias palabras.

Salida: una lista de preguntas reales ordenadas por demanda estimada y competencia.

**Y aquí va la salvaguarda ética, que es lo que separa esto del clickbait:**

> La demanda elige **la pregunta**. La bibliografía decide **si podemos responderla
> honestamente**. Si una pregunta con mucha demanda no tiene respaldo en las 77 obras, no
> se hace el vídeo: se anota como pendiente de fuente. Nunca al revés.

Eso convierte el problema en su contrario: en vez de un canal que busca a quién contarle
lo que ha leído, un canal que responde con evidencia lo que la gente ya se pregunta mal.

---

#### C4 · Un personaje: la cara que un canal sin cara necesita

**El cambio creativo central de este plan.**

Crear un personaje recurrente en SVG, dibujado en el mismo lenguaje de plano técnico que
ya define la marca: **una cabeza mecánica** —engranajes visibles, trazo ámbar de 3 px,
una boca que es una línea articulada y unas cejas que son dos bielas—. No habla. Reacciona.

Resuelve cuatro problemas a la vez:

- **La miniatura recupera su cara.** El dato del 69 %/80 % deja de ser inalcanzable.
- **Hay algo que se mueve.** Su expresión cambia, y eso cabe en la entrada de escena que
  `render.py` ya captura: coste de render cero.
- **Prueba que hay una decisión creativa detrás**, que es exactamente lo que la política de
  contenido no auténtico pide demostrar.
- **Y puede ser el chiste.** Un canal que enseña humor con un personaje que se ríe medio
  segundo tarde, o que no se ríe nunca, tiene gracia por construcción. El personaje es el
  contrapunto: el que no lo pilla, el que lo pilla demasiado, el escéptico.

Es SVG en línea. Cero peticiones, cero dependencias, cero coste, infinitamente consistente.
Y el vídeo 200 lo tendrá idéntico al vídeo 5, que era el argumento original a favor de
renderizar con código.

---

#### C5 · Miniaturas que se vean

Reglas nuevas para `miniatura.py`:

- Fondo **claro o saturado**, no `#0B1220`. El azul marino pasa a ser el color del vídeo,
  no el de la miniatura.
- La cara del personaje ocupando **entre un cuarto y un tercio del encuadre**.
- **Cuatro palabras o menos**, en Archivo Black, con caja sólida detrás.
- Nada en la esquina inferior derecha (ahí va la duración).
- **Contraste verificado por código**: `miniatura.py` ya mide luminancia; añadir el
  cálculo de ratio WCAG entre texto y fondo y **fallar la producción** si baja de 7:1.
  Así el criterio deja de depender del gusto de nadie.
- Generar **tres variantes** por vídeo. La prueba A/B de Studio no está en la API, pero
  `thumbnails.set` sí: el analista semanal rota la miniatura a los 7 días y compara CTR.
  Es un A/B pobre pero es gratis y es automático.

---

#### C6 · Romper la estática sin romper el presupuesto de render

El conflicto de D5 tiene salida, y es elegante: **no hace falta capturar más fotogramas.
Hace falta que el vídeo compuesto se mueva.** Tres vías, todas en el montaje, ninguna en
el render:

1. **Arreglar los subtítulos quemados y confirmarlo.** Ya está el código en el repositorio
   desde el 19 de agosto; solo falta que corra una producción. Es lo único que se mueve
   durante el tramo central y lleva roto desde el principio. **Prioridad máxima y coste
   cero.**
2. **Una capa viva compuesta por FFmpeg.** Un elemento pequeño en bucle —un engranaje que
   gira lentamente en una esquina, una línea de barrido tenue— superpuesto con `overlay`
   sobre el vídeo ya renderizado. Un solo asset de dos segundos en bucle, un filtro. No
   añade ni una captura.
3. **Movimiento de cámara, bien hecho esta vez.** Se descartó `zoompan` porque trunca el
   recorte a entero y la imagen salta un píxel. La solución conocida es escalar primero a
   un tamaño mayor (`s=` grande en `zoompan`, o `scale` a 2× seguido de `crop` con
   desplazamiento animado) para que el truncamiento ocurra en una rejilla más fina y el
   salto quede por debajo del píxel de salida. **Hay que medirlo antes de adoptarlo**, con
   la regla 6 de `MEJORA_VISUAL.md`.

Con la 1 y la 2 ya se pasa de «congelado» a «vivo». La 3 es opcional.

---

#### C7 · Dos voces

Convertir el monólogo en diálogo: **un narrador y un escéptico**. El narrador explica; el
escéptico interrumpe con la objeción que el espectador está pensando, y ahí es donde vive
el humor.

Dos implementaciones, ambas gratis:

- **La barata e inmediata:** dos voces distintas de `edge-tts` asignadas por rol de escena.
  Cambio pequeño en `voz.py`, funciona hoy.
- **La buena:** Gemini TTS, que admite hasta dos hablantes con control de expresión por
  prompt y ya hay `GEMINI_API_KEY` en los secretos. Está en *preview*, así que se mantiene
  `edge-tts` como respaldo, que es la política que el proyecto ya sigue.

**Por qué importa más de lo que parece:** rompe la cadencia fija (retención), da al canal
una voz reconocible (marca), demuestra decisión creativa sostenida (política de contenido)
y mete gracia en el propio formato en vez de solo hablar de ella (D8). Cuatro problemas,
un cambio.

---

#### C8 · Menos vídeo largo, más Shorts

Un vídeo largo por semana, cinco Shorts. De 4 a 6 minutos, no de 7 y medio: en 5–10
minutos el rango bueno de retención es 50–70 %, y es más fácil sostenerlo en cinco que en
siete y medio.

Baja también la huella de «producción en masa» que preocupa en D7, y libera minutos de
Actions para los Shorts.

---

#### C9 · Reescribir los primeros quince segundos

Regla nueva para el prompt del guionista, y motivo de bloqueo en `validar_guion.py`:

- **Prohibido** abrir con la promesa del contenido: «en este vídeo vamos a ver…»,
  «cincuenta años de investigación…», «todo el mundo cree que…».
- **Obligatorio** abrir con la cosa: un chiste, una escena concreta, o una pregunta que el
  espectador conteste mentalmente antes de que termine la frase.
- **La primera risa antes del segundo quince.**

Más del 55 % de los espectadores se pierden en los primeros treinta segundos cuando la
entrada es floja. Es el tramo más rentable del vídeo entero.

---

#### C10 · Cada episodio, también una página web

El repositorio ya es público y está en GitHub. Un script `paginas.py` genera una página
HTML por episodio —guion completo, figuras, y las fuentes con su DOI— y la publica en
**GitHub Pages**, gratis, en el mismo workflow.

**Por qué:** hay demanda en Google en español para «teoría de la ruptura benigna», «estilos
de humor Martin», «por qué explicar un chiste lo mata», y casi nada bueno que la responda.
Esas páginas traen tráfico externo al canal, que es la tercera superficie de D1.

Y hay una razón que va más allá del tráfico: **es la parte del proyecto que más claramente
suma algo a internet en vez de restarlo.** Divulgación seria, en español, con fuentes
enlazadas y gratis. Si el canal desapareciera mañana, eso seguiría siendo útil.

---

#### C11 · El bucle de comentarios

- **Al publicar**, `publicar.py` añade el primer comentario con la pregunta del episodio,
  vía `commentThreads.insert`. La pregunta ya la escribe el guionista desde el 19 de
  agosto; solo hay que publicarla.
  *(Fijar un comentario **no** está en la API v3. O se acepta sin fijar, o son diez
  segundos manuales; no vale la pena forzarlo.)*
- **Cada semana**, el analista lee los comentarios nuevos y los pasa al explorador de
  demanda de C3. Los comentarios son la fuente de demanda de mayor calidad que existe,
  porque son de gente que ya te ve.

Eso cierra el círculo entre audiencia y contenido sin que nadie tenga que estar ahí todos
los días.

---

#### C12 · Series con nombre y listas de reproducción automáticas

Las listas **sí** están en la API. Cada episodio se asigna sola a su serie al publicarse.

Las series con nombre («Desmonta el chiste», «El experimento») crean hábito de vuelta, y
eso importa más desde febrero de 2026, cuando YouTube redujo las notificaciones a los
espectadores poco activos: la campanita ya no es un canal fiable de retorno.

---

#### C13 · Salir de YouTube, sin ensuciar nada

- **TikTok e Instagram Reels**, cuentas de marca. El mismo archivo vertical, subida
  automatizada. Gratis.
- **Una cuenta de texto** (Bluesky o Mastodon; X si se quiere) publicando **un hallazgo al
  día** con su enlace al estudio. Es contenido útil por sí mismo, no un cebo.
- **Pódcast**: el audio ya existe. Un RSS generado por el mismo workflow y distribuido en
  Spotify. Coste marginal cero.

**Y lo que NO se hace, explícitamente:** nada de publicar automáticamente en Reddit ni en
foros. Es spam, va contra las normas de esas comunidades, y funciona en contra. Si algún
día se participa en Reddit, se participa de verdad y a mano.

---

#### C14 · Cambiar la métrica con la que se decide

El plan actual espera al 5 de septiembre y mide retención, CTR, comentarios por mil vistas
y suscriptores por mil vistas. Con veinte visualizaciones totales, **esas métricas son
ruido**: un CTR calculado sobre treinta impresiones no significa nada.

El orden correcto es este, y cada escalón no se mira hasta haber pasado el anterior:

| Nivel | Métrica | Umbral para pasar al siguiente | Si no se pasa |
|---|---|---|---|
| **1. ¿Existe?** | Impresiones/semana | ≥ 5.000 (Shorts incluidos) | El problema es distribución: C1, C2, C3 |
| **2. ¿Se hace clic?** | CTR de miniatura | ≥ 4 % | El problema es empaquetado: C4, C5, títulos |
| **3. ¿Se quedan?** | Retención a los 30 s | ≥ 60 % | El problema es el gancho: C9 |
| **4. ¿Aguantan?** | Retención media | ≥ 45 % en largo, ≥ 70 % en Short | El problema es ritmo: C6, C7, C8 |
| **5. ¿Vuelven?** | Suscriptores por mil vistas | ≥ 5 | El problema es la promesa del canal |

Y la cadencia de decisión pasa de una tanda de cuatro semanas a **revisión semanal**, que
es lo que permite un pipeline automatizado.

---

## 5. Lo que no hay que hacer

Recogido también en `REGLAS.md`, que es el archivo que debe leer cualquier agente antes de
tocar nada.

- **No gastar dinero.** Todo lo anterior es gratis. Si una propuesta futura requiere pagar,
  se descarta o se pregunta.
- **No convertirlo en un canal de trucos.** «Cinco frases para caer bien» funcionaría un
  mes y mataría lo único defendible que tiene el canal. El criterio editorial de
  `SIGUIENTES_PASOS.md` —cada vídeo termina diciendo dónde falla lo que acaba de
  explicar— se mantiene íntegro, también en los Shorts.
- **No responder comentarios con IA.** Un comentario automático que finge ser una persona
  es exactamente la clase de basura que este canal no quiere añadir. La pregunta fijada
  del episodio no es eso: es contenido editorial, y se declara como tal.
- **No publicar automáticamente en Reddit ni en foros.**
- **No usar clips de cómicos sin licencia.** El «fame-jacking» de Charisma on Command
  funciona con material bajo cita, y aun así es zona gris para un canal automatizado con
  riesgo de strike. La alternativa es mejor y más de marca: **reconstruir** el chiste en el
  lenguaje visual del canal —despiece, diagrama, línea de tiempo— y nombrar la fuente. Un
  canal que se llama Mecánica del Humor debería dibujar el mecanismo, no reproducir el
  clip.
- **No inventar ni un dato.** El verificador conserva el veto. Si una gráfica necesita
  números que no están en el artículo, no se hace la gráfica.
- **No subir volumen antes de arreglar la distribución.** Más vídeos que nadie ve solo le
  enseñan al algoritmo que los vídeos de este canal no se ven.

---

## 6. Qué tiene que hacer Silvestre, y cuándo

Todo lo demás lo hace el sistema. Esto no puede.

| # | Qué | Cuánto | Cuándo |
|---|---|---|---|
| 1 | Abrir la pestaña *Actions* y comprobar por qué no hay ejecuciones desde el 19 | 2 min | **Hoy** — bloquea todo |
| 2 | *Studio → Configuración → Valores predeterminados de subida → Avanzada* → activar doblaje automático | 5 min | Esta semana |
| 3 | Verificar el teléfono en `youtube.com/verify` si no está hecho (desbloquea miniaturas personalizadas) | 3 min | Esta semana |
| 4 | Pausar `@humormechanics`: ocultar los vídeos, poner un aviso en la descripción. No borrarlo | 10 min | Esta semana |
| 5 | Aprobar los cuatro primeros Shorts antes de que el modo automático se active | 15 min | Semana 2 |
| 6 | Crear las cuentas de marca en TikTok e Instagram (a nombre de Mecánica del Humor) | 20 min | Semana 3, opcional |
| 7 | Decidir sobre C7 (dos voces) mirando y escuchando una muestra | 10 min | Semana 2 |

**Total: unas dos horas, repartidas en tres semanas, y ninguna se repite.**

---

## 7. Qué esperar, honestamente

No hay garantía. Lo que sí se puede decir con los datos de arriba:

- **Semanas 1–2.** Los Shorts deberían pasar de 1–9 visualizaciones a decenas o cientos.
  Eso no es éxito: es tener por fin una señal con la que trabajar. Es la diferencia entre
  estar midiendo y estar adivinando.
- **Semanas 3–6.** Con impresiones reales, CTR y retención empiezan a significar algo. Aquí
  es donde C4, C5 y C9 se ganan o se pierden, y donde el canal encuentra cuál de los cinco
  formatos de Short funciona.
- **Semanas 7–12.** Si algún formato despega, el vídeo largo semanal deja de ser un vídeo
  que nadie ve y pasa a ser el sitio al que va la gente que ya te conoce por los Shorts.
  Ese es el momento en que el trabajo de bibliografía y verificación empieza a rendir.

Y una advertencia que conviene tener escrita: **puede que no funcione.** El nicho es
pequeño y la ventaja competitiva del canal —rigor— es la que menos se nota en cuarenta
segundos. Si a las doce semanas el nivel 1 de la tabla de C14 sigue sin superarse, el
problema no son los Shorts ni las miniaturas: es que «la ciencia del humor» no es lo que
la gente quiere ver, y entonces la conversación es sobre ampliar el tema —humor dentro de
habilidades sociales y conversación, que es un mercado mucho mayor y donde Charisma on
Command demuestra que hay siete millones de personas— sin renunciar ni al método ni a las
fuentes.

Mejor saberlo en noviembre con datos que en marzo por agotamiento.

---

## Fuentes

**Datos de canales (agosto de 2026)**

- [Psych2Go — vidIQ](https://vidiq.com/youtube-stats/channel/UCkJEpR7JmS36tajD34Gp4VA/)
- [Charisma on Command — vidIQ](https://vidiq.com/youtube-stats/channel/@charismaoncommand/)
- [The School of Life — vidIQ](https://vidiq.com/youtube-stats/channel/@theschooloflifetv/)
- [Improvement Pill — vidIQ](https://vidiq.com/youtube-stats/channel/@ImprovementPill/)
- [QuantumFracture — vidIQ](https://vidiq.com/youtube-stats/channel/@quantumfracture/)
- [Academia Play — vidIQ](https://vidiq.com/youtube-stats/channel/@academiaplay/)
- [VisualPolitik — vidIQ](https://vidiq.com/youtube-stats/channel/@VisualPolitik/)
- [Memorias de Pez — vidIQ](https://vidiq.com/youtube-stats/channel/@memoriasdepez/)
- [Ranking 2btube de canales españoles de divulgación y educación](https://www.moncloa.com/2024/01/04/cuales-son-los-mejores-canales-espanoles-de-divulgacion-y-educacion-segun-un-analisis-de-2btube-2367585/)

**Estrategia y crecimiento**

- [Charlie Houpert (Charisma on Command) en el pódcast de Tim Ferriss — «fame-jacking» y las decisiones tempranas](https://tim.blog/2025/06/25/charlie-houpert-charisma-on-command/)
- [Cómo se descubre a los creadores nuevos en 2026 — TubeBuddy](https://www.tubebuddy.com/blog/how-to-get-discovered-on-youtube-why-new-creators-are-being-pushed-in-2026/)
- [Cambios del algoritmo de YouTube en 2026, mes a mes — AIR Media-Tech](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views)
- [Fuentes de tráfico de YouTube explicadas](https://humbleandbrag.com/blog/youtube-traffic-sources)
- [Fórmulas de título con datos](https://humbleandbrag.com/blog/best-youtube-titles)

**Métricas de referencia**

- [Benchmarks de retención 2026 — Lenos](https://www.lenostube.com/en/youtube-audience-retention-average-good-and-best-benchmarks/)
- [Benchmarks de Shorts 2026 — vistas por tamaño de canal](https://humbleandbrag.com/blog/youtube-shorts-benchmarks)
- [Diseño de miniaturas y datos de vídeos *breakout* — vidIQ](https://vidiq.com/blog/post/youtube-thumbnail-design-tips/)
- [Retención en vídeo sin cara: cadencia visual y errores de voz IA](https://framesail.com/blog/high-retention-faceless-youtube-videos)

**Políticas y funciones de plataforma**

- [Políticas de monetización de canales — Ayuda de YouTube (contenido no auténtico)](https://support.google.com/youtube/answer/1311392?hl=en)
- [YouTube aclara sus políticas sobre contenido de IA, 16 de julio de 2026 — TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
- [Doblaje automático y pistas de audio multilingües — Metricool](https://metricool.com/youtube-multi-language-audio-tracks-now-available-for-more-creators/)
- [Requisitos de subida de Shorts 2026](https://www.shortsync.app/resources/youtube-shorts-upload-requirements-2026)
- [Referencia de la API de datos de YouTube v3](https://developers.google.com/youtube/v3/docs)
- [YouTube Hype para canales pequeños — TubeBuddy](https://www.tubebuddy.com/blog/youtube-hype-the-new-feature-to-help-small-channels-shine/)
- [Modelos TTS de código abierto en 2026: Kokoro, Chatterbox y compañía](https://www.tryspeakeasy.io/blog/open-source-text-to-speech-2026)
