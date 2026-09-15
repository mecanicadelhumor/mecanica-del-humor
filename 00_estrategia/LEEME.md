# 00_estrategia — Léeme primero

Análisis del 20 de agosto de 2026 sobre por qué el canal no arranca y qué cambiar.
Escrito para que **cualquier conversación del proyecto** pueda aplicarlo sin rehacer el
análisis.

## Los archivos, en orden de lectura

| Archivo | Qué es | Cuándo se lee |
|---|---|---|
| **`REGLAS.md`** | Las restricciones que nadie puede saltarse: ética, rigor, coste cero, cómo se cambian las cosas | **Siempre, antes de tocar nada.** Es corto |
| **`PROPIEDAD_DE_FICHEROS.md`** | Quién escribe qué. De obligado cumplimiento para toda tarea programada | Antes de escribir en cualquier sitio |
| **`PLAN_DE_CAMBIOS.md`** | La cola de cambios con sus criterios de aceptación. **La versión 9, al final, manda sobre lo anterior** | Al ir a hacer algo, y al decidir qué se hace antes |
| **`PROMPT_DE_ARRANQUE.md`** | Cómo empezar una conversación nueva, autorizaciones vigentes, trampas conocidas y dónde está el proyecto hoy | Al abrir una conversación, y al cerrarla |
| **`PROMPT_DIRECCIÓN.md`** | El cuaderno del codirector entre sesiones: lo que quiere comentar de un día para otro. **Suyo y solo suyo: se lee, no se edita ni se borra** | Al abrir una conversación de dirección |
| **`TOKEN_DE_YOUTUBE.md`** | Cómo se saca el token de YouTube y por qué caducaba. Quince minutos, una vez | Si el canal deja de publicar, o al tocar los secretos |
| **`DIAGNOSTICO.md`** | El análisis completo: canales de referencia, por qué triunfan, y las 8 causas del problema | Cuando haga falta entender **por qué** |
| **`tareas/`** | Los prompts de las tres tareas programadas. Desde el 12/09 **el fichero es el prompt**: el almacén solo lleva un arranque que lo lee. Y los `tareas_codirector_FECHA.md`, que son lo que la dirección le pide al codirector (fuera de git) | Al cambiar lo que hace un agente |
| **`REDES.md`** | Las cuentas fuera de YouTube | Cuando toque C13 |
| **`panel.html`** | El resumen visual de una página | Cuando quieras la foto entera sin leer |

Y fuera de esta carpeta, dos ficheros que dicen dónde está el canal hoy:
**`05_calendario/ESTADO.md`** (cinco líneas, lo escribe la revisión diaria todos
los días) y **`05_calendario/metricas.json`** (los números).

## El resumen en cuatro líneas

1. El canal **no tenía un problema de calidad, tenía un problema de
   distribución.** Eso sigue siendo cierto, y en agosto se atacó por donde decía
   el diagnóstico: Shorts a diario, un solo canal, personaje y miniaturas.
2. **No ha funcionado todavía.** A 31 de agosto, cinco Shorts en su primera
   semana suman 44 visualizaciones entre los cinco, cero suscriptores y cero
   comentarios. El criterio de aceptación de C2 falló por un factor de diez.
3. **La única superficie que responde es la búsqueda**, que el diagnóstico daba
   por la más difícil: dos Shorts sacan de `YT_SEARCH` el 63,6 % y el 46,2 % de
   sus visualizaciones. El feed de Shorts apenas empuja.
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
