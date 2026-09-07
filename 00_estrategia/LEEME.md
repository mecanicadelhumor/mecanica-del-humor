# 00_estrategia — Léeme primero

Análisis del 20 de agosto de 2026 sobre por qué el canal no arranca y qué cambiar.
Escrito para que **cualquier conversación del proyecto** pueda aplicarlo sin rehacer el
análisis.

## Los archivos, en orden de lectura

| Archivo | Qué es | Cuándo se lee |
|---|---|---|
| **`REGLAS.md`** | Las restricciones que nadie puede saltarse: ética, rigor, coste cero, cómo se cambian las cosas | **Siempre, antes de tocar nada.** Es corto |
| **`PROPIEDAD_DE_FICHEROS.md`** | Quién escribe qué. De obligado cumplimiento para toda tarea programada | Antes de escribir en cualquier sitio |
| **`PLAN_DE_CAMBIOS.md`** | La cola de cambios con sus criterios de aceptación. **La versión 4, al final, manda sobre lo anterior** | Al ir a hacer algo, y al decidir qué se hace antes |
| **`PROMPT_DE_ARRANQUE.md`** | Cómo empezar una conversación nueva, autorizaciones vigentes, trampas conocidas y dónde está el proyecto hoy | Al abrir una conversación, y al cerrarla |
| **`TOKEN_DE_YOUTUBE.md`** | Cómo se saca el token de YouTube y por qué caducaba. Quince minutos, una vez | Si el canal deja de publicar, o al tocar los secretos |
| **`DIAGNOSTICO.md`** | El análisis completo: canales de referencia, por qué triunfan, y las 8 causas del problema | Cuando haga falta entender **por qué** |
| **`tareas/`** | Los prompts de las tres tareas programadas, espejados. La copia que corre es la del almacén | Al cambiar lo que hace un agente |
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

## Estado a 7 de septiembre

Las fases 1 y 2 están hechas y la publicación es automática. **El número se movió
con C15** —31, 21 y 21 contra una mediana de 11— y ahí se quedó: el episodio
largo del sábado 5 tiene **una visualización, la de Silvestre**. Seguimos en el
peldaño S1 y por debajo del umbral.

**Y hay una cifra que ordena todo lo demás:** un canal desconocido de menos de
mil suscriptores saca **entre 50 y 500 visualizaciones por Short en 48 horas**.
Nosotros sacamos entre 20 y 30. No estamos por debajo de la excelencia; estamos
por debajo del suelo de lo normal.

Lo que queda por delante está en la **versión 6** de `PLAN_DE_CAMBIOS.md`, al
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
- **No se clona la voz de Silvestre por ahora.** En su lugar, Gemini TTS con
  dirección de actor, **una llamada por escena y solo en los Shorts, desde el
  lunes 14**. El escalón intermedio de dos voces de `edge-tts` se descartó.
- **Los subtítulos quemados se retiraron** por decisión editorial. No los vuelvas
  a encender: el motivo está en `MEJORAS.md` del 20/08 y en C6.1.
- **Ni notificaciones ni CSV a mano.** Los agentes no avisan a Silvestre: dejan
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
