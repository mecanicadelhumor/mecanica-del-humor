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

## Estado a 4 de septiembre

Las fases 1 y 2 están hechas y la publicación es automática. **Y por primera vez
el número se mueve:** 31, 21 y 21 visualizaciones en los tres últimos Shorts,
contra una mediana de 11 en la primera tanda, y el primer «me gusta» del canal.
Llega justo después de C15, que es lo que ese cambio prometía. Seguimos en el
peldaño S1 y por debajo del umbral, pero en la rama buena de las tres que están
escritas para el 27 de septiembre.

Lo que queda por delante está en la **versión 5** de `PLAN_DE_CAMBIOS.md`, al
final, que es la que manda.

**Decisiones tomadas** (el razonamiento, en `PLAN_DE_CAMBIOS.md`):

- **Un solo canal, en español.** El inglés se sirve con el doblaje automático de
  YouTube. Se reabre `@humormechanics` solo si las pistas dobladas superan el
  25 % del tiempo de visionado a las ocho semanas.
- **No se clona la voz de Silvestre por ahora.** En su lugar, Gemini TTS con
  dirección de actor. **El escalón intermedio de dos voces de `edge-tts` se
  descartó el 4 de septiembre:** no arregla el ritmo, que es lo que está roto.
- **Los subtítulos quemados se retiraron** por decisión editorial. No los vuelvas
  a encender: el motivo está en `MEJORAS.md` del 20/08 y en C6.1.
- **Ni notificaciones ni CSV a mano.** Los agentes no avisan a Silvestre: dejan
  `05_calendario/ESTADO.md` escrito.
- **La aplicación de OAuth sale del modo de prueba** (C23), para que el token de
  YouTube deje de caducar cada siete días. Publicar no es verificar: no hace
  falta inventarse ni una web ni una política de privacidad.
- **Hay una barrera antes de publicar** (C21): `render.py` falla si un texto no
  cabe en su caja, y como corre antes que `publicar.py`, nada se sube roto.

## Relación con los documentos que ya existían

- `SIGUIENTES_PASOS.md` y `05_calendario/CALENDARIO.md` quedan **superados** en lo que
  toca a cadencia, idiomas y métricas de decisión. Ver C1, C8 y C14.
- `03_produccion/MEJORA_VISUAL.md` sigue **plenamente vigente**: sus siete reglas para
  tocar el diseño se mantienen, y su backlog (V1–V9) se integra en C4, C5 y C6.
- `05_calendario/MEJORAS.md` sigue siendo el registro histórico. Se añade al final, nunca
  se reescribe.
- El criterio editorial de `SIGUIENTES_PASOS.md` —cada vídeo termina diciendo dónde falla
  lo que acaba de explicar— **no se toca**. Está recogido como regla 11 en `REGLAS.md`.
