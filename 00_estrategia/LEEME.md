# 00_estrategia — Léeme primero

Análisis del 20 de agosto de 2026 sobre por qué el canal no arranca y qué cambiar.
Escrito para que **cualquier conversación del proyecto** pueda aplicarlo sin rehacer el
análisis.

## Los archivos, en orden de lectura

| Archivo | Qué es | Cuándo se lee |
|---|---|---|
| **`REGLAS.md`** | Las restricciones que nadie puede saltarse: ética, rigor, coste cero, cómo se cambian las cosas | **Siempre, antes de tocar nada.** Es corto |
| **`PROPIEDAD_DE_FICHEROS.md`** | Quién escribe qué. De obligado cumplimiento para toda tarea programada | Antes de escribir en cualquier sitio |
| **`PLAN_DE_CAMBIOS.md`** | La cola de cambios con sus criterios de aceptación. **La versión 19, al final, manda sobre lo anterior** (la 18 trae el bucle; la 19, las reglas de producción, el análisis de `MDS-016` y la animación en el render): **el bucle de aprendizaje (C60)** —siete Shorts a la semana desde el 12/10 y catorce desde el 19/10 solo si la voz de una toma (C36) pasa sus pruebas, cada uno de un brazo de un experimento, medido con «Se quedaron viendo»—, el personaje animado (C61) y la dirección en diferido (C62). La 17 tiene el envoltorio del Short (C56-C59); la 16, las rutinas de Code y la animación a medida | Al ir a hacer algo, y al decidir qué se hace antes |
| **`REGLAS_DE_PRODUCCION.md`** | **Las reglas de un Short que funciona** (08/10/2026): la línea principal que cumple cada vídeo, con origen y evidencia, más una sola modificación por vídeo (la de su brazo del bucle). Mutable; lo escribe solo la dirección | Antes de escribir o producir un Short, y al decidir qué se prueba |
| **`ANALISIS_MDS-016.md`** | Por qué el único Short que pasó de 1.000 visualizaciones lo hizo: cada variable, qué se descarta y las hipótesis (08/10/2026) | Al elegir temas y al ordenar la cola de hipótesis |
| **`REFERENTES_2026-10-08.md`** | PsychToons y Kurzgesagt: dos canales sin cara que funcionan, y qué se aprende de ellos | Cuando se hable de imagen, personaje o formato largo |
| **`MERCADO_2026-10.md`** | El estudio del mercado de la divulgación en YouTube del 02/10/2026: cómo reparte el feed, qué funciona pieza a pieza, los canales automatizados y la IA, el dinero, y dónde estamos. Con fuentes | Cuando haga falta saber **qué hace el mercado**, al lado de `DIAGNOSTICO.md`, que dice por qué el canal se diseñó así |
| **`PROMPT_DE_ARRANQUE.md`** | Cómo empezar una conversación nueva, autorizaciones vigentes, trampas conocidas y dónde está el proyecto hoy | Al abrir una conversación, y al cerrarla |
| **`PROMPT_DIRECCIÓN.md`** | El cuaderno del codirector entre sesiones: lo que quiere comentar de un día para otro. **Suyo y solo suyo: se lee, no se edita ni se borra** | Al abrir una conversación de dirección |
| **`TOKEN_DE_YOUTUBE.md`** | Cómo se saca el token de YouTube y por qué caducaba. Quince minutos, una vez | Si el canal deja de publicar, o al tocar los secretos |
| **`DIAGNOSTICO.md`** | El análisis completo: canales de referencia, por qué triunfan, y las 8 causas del problema | Cuando haga falta entender **por qué** |
| **`tareas/`** | Los prompts de las tres tareas programadas. Desde el 12/09 **el fichero es el prompt**: el almacén solo lleva un arranque que lo lee. Y los `tareas_codirector_FECHA.md`, que son lo que la dirección le pide al codirector (fuera de git) | Al cambiar lo que hace un agente |
| **`REDES.md`** | Las cuentas fuera de YouTube | Cuando toque C13 |
| **`panel.html`** | El resumen visual de una página | Cuando quieras la foto entera sin leer |

Y fuera de esta carpeta, tres sitios que dicen dónde está el canal hoy:

- **`05_calendario/estado/`** — cinco líneas al día, lo escribe la revisión diaria. **Un
  fichero nuevo por día: el de hoy es el de nombre más alto.** Desde el 21/09/2026; antes era
  `ESTADO.md`, que está **congelado** (C45, y `estado/LEEME.md` cuenta por qué).
- **`05_calendario/metricas.json`** — los números, cada lunes.
- **`08_comunicacion/`** — `novedades.md` es del codirector, para hablarles a las tareas
  programadas; se lee y no se toca. Lo demás es el buzón entre agentes, un fichero nuevo por
  mensaje. La dirección deja ahí lo decidido después de cada sesión (C43, desde el 21/09).

## El resumen en cuatro líneas

1. El canal **no tenía un problema de calidad, tenía un problema de
   distribución.** Eso sigue siendo cierto, y en agosto se atacó por donde decía
   el diagnóstico: Shorts a diario, un solo canal, personaje y miniaturas.
2. **No ha funcionado todavía.** A 31 de agosto, cinco Shorts en su primera
   semana suman 44 visualizaciones entre los cinco, cero suscriptores y cero
   comentarios. El criterio de aceptación de C2 falló por un factor de diez.
3. **~~La única superficie que responde es la búsqueda~~ — CORREGIDO el 18/09/2026.**
   Fue cierto en agosto (`MDS-002` y `MDS-006` sacaban de `YT_SEARCH` el 63,6 % y el
   81,2 %) y dejó de serlo a partir de `MDS-007`. Ponderado por visualizaciones sobre
   los quince Shorts con datos de tráfico: **feed de Shorts 54,6 %, búsqueda 27,7 %,
   suscriptores 6,9 % y todo lo externo junto 5,4 %.** `MDS-015` sacó del feed el
   96,8 % de las suyas. **Manda el feed**, y al feed se le convence con la proporción
   de vídeo vista, no con distribución — que es lo que hace de C38 la decisión de la
   semana y lo que deja el marketing externo en ruido (C40).
4. **La apuesta hasta el 27 de septiembre** es que lo que mata al vídeo es el
   primer segundo —una tarjeta de texto con voz sintética— y que arreglarlo
   (C19 + C16, y luego C7) mueve el número. Si el 27 ningún Short ha pasado de
   100 visualizaciones y la mediana sigue por debajo de 20, el problema no es la
   ejecución sino el tema, y toca ampliarlo.
5. **Y desde el 4 de septiembre hay una quinta línea:** dos vídeos salieron rotos
   en una semana (texto cortado, y una escena que decía en pantalla algo que la
   voz no menciona). El proyecto no tenía **ninguna** comprobación capaz de
   impedir una publicación. Ahora sí — ver C21 y la regla 14.
6. **Y desde el 7 de septiembre, una sexta:** el problema ya no es solo que un
   vídeo salga roto, es que **todos salen iguales**. La presentación es lo que
   más lejos está de los canales de referencia, y por eso existe C25.

7. **Y desde el 12 de septiembre, una séptima:** los guiones que fallan **cumplen el prompt
   entero**. Tres avisos en cuatro días sobre guiones sin un solo incumplimiento: el problema
   no es que los agentes se salten las reglas, es que las reglas dicen qué tiene que
   *contener* un guion y no qué tiene que *sostenerlo*. Ver la versión 7 y los dos prompts de
   guionista, reescritos.

8. **Y desde el 14 de septiembre, una octava, que es la que manda hoy:** por primera vez
   hay medianas limpias a 48 horas, y dicen que **la mediana de los quince Shorts es 10
   visualizaciones, con cero por encima de 50 y cero suscriptores en todo el canal.** No es
   que los números no se muevan: esta semana han bajado. Y la curva de retención, que
   también es nueva, enseña **fuga continua** —la mitad de la audiencia se va en el segundo
   13— en vez de un desplome inicial: el problema ya no es solo que no entren, es que una
   vez dentro no hay nada que mirar. De ahí salen C33 (la voz se dirige escena a escena) y
   C34 (**se revierte el descarte de las imágenes**: el banco propio entra).

9. **Y desde el 15 de septiembre, una novena:** **un vídeo, una voz.** `MDS-017` salió con dos
   voces alternándose porque el respaldo a `edge-tts` era escena a escena; ahora es por vídeo
   entero y en escalera (C33.1). Y el mismo día, **el primer Short por encima de 1.000
   visualizaciones**, `MDS-016`, todavía sin explicación.

10. **Y desde el 23 de septiembre, una décima:** **un guion puede cumplirlo todo y no entenderse.**
   Tres Shorts seguidos pasaron todas las comprobaciones y no tenían hilo. Desde ese día, un guion
   no se produce sin que un lector que no lo ha escrito cuente de qué va (C48). Y la imagen pasa de
   diapositiva a vídeo (C50).

11. **Y desde el 2 de octubre, una undécima:** **el guion ya está por encima del mercado; el envoltorio,
   por debajo.** El estudio de mercado (`MERCADO_2026-10.md`) encontró que lo que nos separa de los
   canales que crecen son piezas baratas alrededor del guion —el primer segundo, el título, la
   pregunta al espectador, la llamada a seguir— y que ninguna de las cuatro estaba bien. Y que **lo que
   enseña YouTube no es lo que le mandamos**: la portada que veía el público era un fotograma negro.

## Estado a 5 de octubre

**El canal empieza a aprender solo** (versión **18** del plan). El codirector pidió iterar más rápido,
con las métricas como recompensa, y eso es C60:

- **Siete Shorts a la semana desde el 12/10** (también sábado y domingo) y **catorce desde el 19/10** si
  la voz de una sola toma (C36) pasa sus pruebas.
- **Cada Short es de un brazo de un experimento**: el control, la animación del mecanismo (A) y el
  arranque con el dato (B), asignados por un orden barajado y no por quien escribe. Lo cuenta el código
  (`04_agentes/bucle.py`) todos los días y lo decide una regla escrita antes del primer dato.
- **La cifra que manda en el bucle es «Se quedaron viendo»**: la parte de los que el feed puso delante
  que no deslizaron. El codirector la copió de Studio: entre el 2,7 % y el 40 %. Es donde perdemos.
- **El presentador, con fechas:** persona sintética (Kaggle) y personaje animado (2D propio y 3D VRM),
  muestrarios el 16/10 y A/B entre los dos desde el 26/10.
- **La dirección también corre como rutina** (C62), lunes y jueves, con el cuaderno del codirector en un
  repositorio privado. Lo que decide llega a `main` sin esperar a un `push`.
- **Las métricas ya no dependen del reloj de GitHub:** el workflow despierta a la rutina en cuanto
  escribe. Y la mediana C26 sigue subiendo: **35** (era 24).

## Estado a 2 de octubre

**El estudio de mercado, y cuatro arreglos baratos** (versión **17** del plan; el estudio, en
`MERCADO_2026-10.md`). La conclusión: el guion ya está por encima del nicho, y lo que nos separa de los
que crecen es lo que lo rodea. Desde `MDS-031` (lunes 5):

- **El título es la pregunta, sola**, 55 caracteres como mucho (eran 74-98; el mejor del canal tenía 45).
- **La pregunta al espectador se publica de verdad**, como comentario del canal, cuando el Short ya es
  público. Desde el 31/08 no se había publicado ninguna.
- **El primer segundo, sin negro**: los Shorts empezaban con 0,6 s de imagen congelada y un fundido desde
  negro, y ese fotograma negro era además su portada en el buscador.
- **La firma final pide que sigan el canal**, con una frase fija.

Y dos respuestas: **las miniaturas** no se tocan, porque YouTube solo enseña la nuestra en las
superficies horizontales (la portada que se ve es el primer fotograma); y **la música** de los días 1 y 2
no fue un fallo: la rueda de 14 pistas dio la vuelta.

## Estado a 30 de septiembre

**El canal vuela solo por primera vez** (versión **16** del plan). Nada de lo que sale en los vídeos
ha cambiado: es la segunda semana de la imagen real (C50) y se mide.

- **Las rutinas de Code funcionan (C53.1).** La de métricas entregó sola a `main` a la primera; las
  tres tareas de agosto están apagadas. Desde mañana la revisión diaria tampoco necesita paquetes.
- **C53.2:** `entregar.py` mide contra `main` (ya no se le escapa un trabajo commiteado antes de
  tiempo) y el workflow borra las ramas de sesión que ya están en `main`. **El botón «Crear PR» de una
  ejecución de rutina no se pulsa nunca.**
- **La animación a medida, vista (C55.1):** `MDS-027` entero, con su voz y su música, en
  `07_pruebas/animacion-2026-10/`. Enseña el mecanismo mejor que el vídeo de archivo y tiene menos
  estímulo visual. Decide el codirector; hay una propuesta nueva: animar solo las escenas que explican.
- **El presentador (C51.3):** Kaggle listo; de siete modelos abiertos de sincronía labial, uno sirve
  (MuseTalk, con un cambio). Prueba, no antes del 12/10.

## Estado a 29 de septiembre

**Sesión de martes, sin cambios en producción** (versión **15** del plan). Esta semana se mide la
imagen real (C50) y no se toca nada de lo que sale en los vídeos.

- **Las tareas no podían entregar solas, y no era culpa del codirector:** se crearon desde Cowork y
  no tienen dónde poner un repositorio. Se crean otra vez como **rutinas de Code**, con el
  repositorio, y se apagan las viejas (C53.1, una vez, unos 25 minutos del codirector). Hasta
  entonces, el `.tar.gz` de siempre.
- **La animación a medida con Opus 5.5 (C55):** todos los Shorts con datos son ya animación en
  JavaScript de plantilla, incluidos los tres mejores; la imagen real no tiene datos todavía. Se
  propone un muestrario y, si convence, un Short de cada cinco durante cuatro semanas desde el 12/10,
  decidido por la retención a 30 s con una regla escrita de antemano.

## Estado a 28 de septiembre

**El punto de control del 27 está contestado con datos, y es un sí.** Versión **14** del plan.

- **Cinco Shorts por encima de 100 visualizaciones en 48 horas**, en dos semanas distintas. La
  mediana de C26 pasa de 11 a **24**; la de los últimos diez, a **90**. `MDS-021` y `MDS-022`
  retienen al 60 % en el segundo 30: lo mejor de la historia del canal.
- **Lo que bloquea ahora es S3**: cero suscriptores y casi cero «me gusta». La gente lo ve y no
  reacciona. Y uno de cada tres Shorts no llega a enseñarse; dos de esos tres son resubidas, y desde
  hoy **un Short subido no se vuelve a subir** (C54).
- **Viabilidad:** si el régimen se sostiene, el 15 de noviembre cae en «se amplía el tema», con la
  prórroga hasta el 10 de enero. Para llegar a «se sigue» el Short típico tiene que pasar de 100.
- **El canal empieza a volar solo (C53):** las tareas programadas suben su trabajo a una rama y el
  workflow «Entregas» lo pasa a `main` comprobando que cada una solo toca lo suyo. Falta un paso de
  unos diez minutos del codirector (añadir el repositorio a las tres tareas y mover cuatro workflows).
- **La actualidad como gancho (C52):** sí, pero para el primer segundo, no para la búsqueda (el feed
  trae el 93-98 % de las visitas). Un Short de cada cinco, como mucho, desde el jueves 1/10.
- **Y:** las caras vuelven a detectarse (C50.7), la regla 7 admite una persona sintética con cinco
  condiciones (7.1), y la voz (C44) espera a que el codirector pueda escuchar una muestra.

## Estado a 23 de septiembre, por la tarde

**C50 entra en producción el mismo día** (**versión 13** del plan). El codirector hizo las cuentas y
la prueba de imagen por la mañana, eligió la variante A —vídeo de archivo detrás y la frase corta
encima— con cuatro arreglos, y pidió empezar cuanto antes. Desde `MDS-024` (jueves 24):

- **Cada escena lleva vídeo de archivo o una imagen generada a pantalla completa**, un plano cada dos
  o tres segundos, y cada plano entra en la palabra de la narración que dice el guion (`desde`).
- **Lo elige un workflow nuevo, «Visuales (C50)»**, en cuanto cambia un guion, y deja un manifiesto
  y una hoja de contactos por Short en `05_calendario/visuales/`. La revisión diaria mira la hoja y
  corrige en `ajustes.json`.
- **Nada se desenfoca**, el texto no tapa caras (se detectan), no hay planos quietos (se mide el
  movimiento), y los mensajes clave pueden ir en **tarjeta de marca**, que es lo de siempre, como
  golpe. El final de cada Short es la firma de marca con el Engranaje.
- **Si algo falla, sale como tarjeta de marca o como siempre.** Y hay un interruptor:
  `05_calendario/visuales/APAGADO`.
- **C51.1**: el Engranaje hablará (muestrario el viernes 25); la persona realista depende de que el
  codirector diga sí a la regla 7.

## Estado a 23 de septiembre

**Tres Shorts seguidos sin hilo, y la sesión de dirección fue de un miércoles.** El 21, el 22 y el
23 se publicaron (o se iban a publicar) guiones que el codirector describió como *«una sucesión de
mensajes inconexos, sin sentido, que huelen a AI slop de lejos»*. Los tres pasaban el validador. La
**versión 12** del plan, que manda desde hoy:

- **C48 · la historia antes que el reloj.** Un Short es una pregunta, una respuesta y un puente, y
  el chiste del principio **es** lo que explica el estudio. La duración de la serie deja de ser
  error. Y **ningún Short se produce sin una lectura en frío**: un lector que solo ve las
  narraciones cuenta de qué va el vídeo; si no lo entiende, no sale. Obligatoria desde `MDS-026`.
  Los tres Shorts que quedaban de la semana, reescritos; el de hoy, rehecho.
- **C48.1 · ninguna fórmula dos veces.** Los 25 Shorts publicados cerraban con «y aquí falla». El
  cierre honesto sigue; la coletilla, no.
- **C49 · la sincronización del registro no estaba rota**: corre con horas de retraso.
- **C50 · la imagen deja de ser una diapositiva.** Vídeo de archivo e imágenes generadas a pantalla
  completa, con el texto encima. Se decide mirando un muestrario, y entra la semana del 28.
- **C51 · el presentador sintético**, que pidió estudiar el codirector: todavía no, y por qué.

**Y una frase del plan que conviene tener delante:** *lo que se puede comprobar sin entender el
vídeo se cumple sin entender el vídeo.*

## Estado a 21 de septiembre

**El punto de control del 27 ya está contestado, y con un sí.** Su pregunta —*¿algún Short ha
pasado de 100 visualizaciones en 48 horas?*— tiene tres respuestas: `MDS-016` **1.210**,
`MDS-019` **161**, `MDS-018` **135**. Cero suscriptores todavía.

Y la previsión del 15 de noviembre, que es lo que preguntó el codirector: **la mediana de hoy
(11,0) no predice nada**, porque quedan 55 días y unos 39 Shorts más, así que ese día **ninguno
de los veinte Shorts publicados hoy estará ya en la ventana de veinte**. Lo que pronostica es el
régimen de la última semana —1.210 · 161 · 135 · 27 · **0**—, que cae en la banda de «se amplía
el tema». **No estamos fracasando: estamos en la frontera. Y la frontera la deciden los ceros,
no los vídeos buenos.**

La sesión del lunes 21 (**versión 11**, la que manda) cerró seis cosas:

- **C42 · se suspende el episodio largo.** Siete episodios largos en treinta y cuatro días
  suman **114 visualizaciones** entre todos —los cinco Shorts de la última semana, 1.533— y
  además su precacheo de voz se comía **9 de las 10 peticiones diarias** del modelo que **desde
  el 15/09 es el respaldo de voz de los Shorts**. Vuelve cuando la mediana llegue a 50.
- **C43 · la dirección no se convierte en tarea programada.** Lo que se automatiza es su
  salida: una nota en `08_comunicacion/` después de cada sesión.
- **C44 · la voz deja de sonar a montaje.** El codirector tenía razón, y además se lo
  pedíamos: la dirección de actor pide cambios de timbre escena a escena, y el volumen de cada
  toma no se iguala nunca. Entra el **lunes 28**, no antes: la semana del 21 es la primera
  medida limpia de C38.
- **C45 · `ESTADO.md` se congela** y nace `05_calendario/estado/`.
- **C46 · el canal se lee a sí mismo.** La planificación del jueves no leía `metricas.json`, y
  por eso `MDS-016` hizo 1.210 y nadie escribió nada que lo continuara.
- **C47 · las métricas se leen todos los días**, no solo los lunes.

## Estado a 18 de septiembre

**Por primera vez los números se mueven, y por primera vez se sabe por dónde.** `MDS-016` hizo
**1.280 visualizaciones**, `MDS-019` va por **182** y `MDS-018` pasa de 100 — contra una mediana
de 10 en los quince anteriores y cero por encima de 50. Sigue habiendo cero suscriptores.

La sesión del viernes 18 (**versión 10** del plan, que es la que manda) salió de que el
codirector trajo el mismo aviso dos días seguidos —«me cuesta seguir el hilo», «forzado entre el
nudo y el desenlace»— sobre dos guiones que **ya** se habían reescrito contra las tres pruebas
de cosido. Al medirlo apareció esto:

- **Los veinticinco Shorts del canal tienen entre 88 y 120 palabras**, dijera lo que dijera la
  duración de su serie (30, 35, 40 o 45 s). El techo del formato se usaba como objetivo, y lo
  que rellenaba la diferencia era explicación entre el remate y el cierre.
- **El remate cae en el segundo 6 o 7, y la mitad de la audiencia se va en el segundo 13.**
  `MDS-016` —el único por encima de mil— es el único que lo pone en el 13.
- De ahí **C38**: el Short se escribe a la duración de su serie y el remate no cae antes del
  segundo 10, las dos como error en `validar_guion.py`. Los cinco Shorts de la semana del 21
  reescritos, sin añadir ni una afirmación nueva.
- **C38.1**: `voz.py` prohibía reírse en las seis escenas sin excepción, así que la mitad de la
  regla 13.1 —«una risa escrita en el guion sigue permitida»— no se podía ejercer. Arreglado.
- **C39**: `BIBLIOGRAFIA_CURADA.md` es un fichero generado y llevaba cinco fichas corregidas
  solo ahí. La próxima regeneración las borraba todas.
- **C40 y C41**: el marketing externo es el 5,4 % del tráfico y no es una palanca; TikTok y
  Reels sí, porque son otro feed y el feed es lo que reparte. Se empieza el trámite ya y se
  publica cuando C38 haya dado su primera medida.

## Estado a 15 de septiembre

**Una buena y una mala.** La buena: `MDS-016` pasa de 1.000 visualizaciones, cuando ninguno de
los quince anteriores había llegado a 50. La mala: `MDS-017` se publicó con dos voces y un guion
que mezclaba tres historias. La sesión del martes 15 (versión 9 del plan) cerró:

- **C33.1 · un vídeo, una voz.** Reintentos, la cuota diaria bien reconocida, y una escalera
  por vídeo: Gemini 3.1 → Gemini 2.5 → esperar al cron de las 08:23 UTC → `edge-tts` entero solo
  como último recurso programado. Vale para Shorts y para largos.
- **Los cuatro Shorts que quedaban de la semana, reescritos** contra las tres pruebas de cosido y
  con las afirmaciones comprobadas en los artículos. Tres fichas de la bibliografía corregidas.
- **C36 y C37, propuestos:** una llamada por vídeo con corte por palabras (se prueba el viernes)
  y un motor de voz sin cuota (sin fecha).
- **Y por la tarde (versión 9.1, C33.2):** `MDS-017` no consiguió voz de Gemini al volver a
  producirlo, y no se subió nada. La causa: la dirección de actor se rechazaba, los rechazos
  gastan cuota y la librería reintentaba por su cuenta. Arreglado, y **`edge-tts` ya no entra
  nunca solo**. `MDS-017` pasa al **sábado 19** y `MDH-007` al **domingo 20**.

## Estado a 14 de septiembre

**La voz nueva es un paso adelante y el canal sigue donde estaba.** La sesión del lunes 14
cerró tres cosas:

- **C33 · la dirección de actor se construye por escena** y no como una constante. Era una
  sola frase pegada delante de las seis escenas —«cuéntala con la entonación de quien cuenta
  algo que le hace gracia»— y explicaba a la vez las risas de más y la sensación de
  despiece: seis llamadas independientes a la API, cada una con su entonación de arranque y
  su punto final. El guion estaba cosido desde el 12 y **la voz lo descosía**. Entra con
  `MDS-017` (martes 15).
- **C34 · se revierte el descarte de las imágenes de C25.** Lo descarté citando la regla 9,
  y la regla 9 no dice eso: prohíbe material **sin licencia**, no material con licencia. El
  banco propio entra, con un tratamiento de marca (duotono sobre la paleta) que se decide
  **mirándolo**, en `07_pruebas/imagen-14-09/muestrario.html`, antes de escribir una línea.
- **C35 · la densidad de estímulo se construye dentro de la escena**, no partiéndola en
  más. Con eso, P3, P5, P6 y P8 dejan de ser acabado y pasan a ser el asunto principal.

**Y una pregunta que ya está formulada para el 27:** `MDH-006`, el mejor contenido del canal
según la propia dirección, tiene **cero visualizaciones a las 48 horas**.

## Estado a 12 de septiembre

Nada se ha movido en los números, y esa sigue siendo la única frase que importa: **por debajo
de 100 visualizaciones por vídeo, el canal está abocado a desaparecer.** Lo que sí ha
cambiado es el proceso. La sesión de dirección del sábado 12 cerró seis cosas —el guionista
reescrito, C28, C29, C30, C31 y la corrección de C27— y todas salen del mismo diagnóstico:
**cinco fallos distintos esta semana, y en los cinco había una regla, la regla se cumplió y
el resultado falló igual.**

## Estado a 7 de septiembre

Las fases 1 y 2 están hechas y la publicación es automática. **El número se movió
con C15** —31, 21 y 21 contra una mediana de 11— y ahí se quedó: el episodio
largo del sábado 5 tiene **una visualización, la del codirector**. Seguimos en el
peldaño S1 y por debajo del umbral.

**Y hay una cifra que ordena todo lo demás:** un canal desconocido de menos de
mil suscriptores saca **entre 50 y 500 visualizaciones por Short en 48 horas**.
Nosotros sacamos entre 20 y 30. No estamos por debajo de la excelencia; estamos
por debajo del suelo de lo normal.

Lo que queda por delante está en la **versión 7** de `PLAN_DE_CAMBIOS.md`, al
final, que es la que manda. Sus dos decisiones nuevas:

- **C25 · La presentación es el talón de Aquiles**, y ahora tiene plan: diez
  propuestas (P1–P10) repartidas en tres semanas, todas deterministas y a coste
  cero. La primera y la más importante: **los ocho iconos de `02_marca/iconos.svg`
  no se han usado ni una vez en once Shorts**, y el 72 % de lo que se ve es texto
  sobre fondo.
- **C26 · El 15 de noviembre se decide si el canal sigue**, con la mediana de los
  últimos veinte Shorts a las 48 horas: ≥ 150 se sigue, entre 50 y 150 se amplía
  el tema con una única prórroga, por debajo de 50 se para. **Los umbrales se
  discuten antes del 8 de noviembre, no después de ver los datos.**

**Decisiones tomadas** (el razonamiento, en `PLAN_DE_CAMBIOS.md`):

- **Un solo canal, en español.** El inglés se sirve con el doblaje automático de
  YouTube. Se reabre `@humormechanics` solo si las pistas dobladas superan el
  25 % del tiempo de visionado a las ocho semanas.
- **No se clona la voz del codirector por ahora.** En su lugar, Gemini TTS con
  dirección de actor, **una llamada por escena y solo en los Shorts, desde el
  lunes 14**. El escalón intermedio de dos voces de `edge-tts` se descartó.
- **Los subtítulos quemados se retiraron** por decisión editorial. No los vuelvas
  a encender: el motivo está en `MEJORAS.md` del 20/08 y en C6.1.
- **Ni notificaciones ni CSV a mano.** Los agentes no avisan al codirector: dejan
  `05_calendario/ESTADO.md` escrito.
- **Hay una barrera antes de publicar** (C21): `render.py` falla si un texto no
  cabe en su caja, y como corre antes que `publicar.py`, nada se sube roto.
- **La regla 11.1 —un cambio por producción— está suspendida** para los cambios
  de presentación hasta el 27 de septiembre. Con veinte visualizaciones no hay
  nada que atribuir midiendo.
- **El marcado de resaltado (`*ámbar*`, `_cian_`) va solo en los campos que se
  ven, nunca en `narracion`**: ahí el sintetizador lo lee en voz alta, y eso es
  lo que se publicó el 7 de septiembre.

## Relación con los documentos que ya existían

- `SIGUIENTES_PASOS.md` y `05_calendario/CALENDARIO.md` quedan **superados** en lo que
  toca a cadencia, idiomas y métricas de decisión. Ver C1, C8 y C14.
- `03_produccion/MEJORA_VISUAL.md` sigue **plenamente vigente**: sus siete reglas para
  tocar el diseño se mantienen, y su backlog (V1–V9) se integra en C4, C5 y C6.
- `05_calendario/MEJORAS.md` sigue siendo el registro histórico. Se añade al final, nunca
  se reescribe.
- El criterio editorial de `SIGUIENTES_PASOS.md` —cada vídeo termina diciendo dónde falla
  lo que acaba de explicar— **no se toca**. Está recogido como regla 11 en `REGLAS.md`.
