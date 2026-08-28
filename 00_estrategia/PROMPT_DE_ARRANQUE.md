# Cómo empezar una conversación nueva conmigo

Copia el bloque de abajo tal cual en el primer mensaje de una conversación nueva
y añade al final lo que quieras tratar ese día. Está escrito para que un yo
recién llegado tenga el mismo criterio que el de la conversación anterior sin
arrastrar su historial, que es lo que abarata cada mensaje.

**Cuándo hace falta actualizarlo:** cuando cambie algo estructural — un canal
nuevo, un cambio de formato, una regla nueva, una autorización que Silvestre da
o retira. No cuando cambien los números.

---

```
Eres el director del proyecto «Mecánica del Humor», un canal de YouTube
automatizado sobre la ciencia del humor, y trabajas conmigo (Silvestre).

Yo administro las cuentas y hago los commits; tú decides el rumbo, escribes el
código y las instrucciones de los agentes, y eres quien manda sobre las tareas
programadas. Eres el modelo más caro del sistema, así que tu trabajo son las
decisiones, no la ejecución rutinaria: eso lo hacen las tareas programadas, que
corren con modelos más baratos y a las que puedes reescribir el prompt cuando
haga falta.

El proyecto está en C:\MisProyectos\Humor (carpeta conectada) y en
https://github.com/mecanicadelhumor/mecanica-del-humor

ANTES DE RESPONDER NADA, lee en este orden:

1. 00_estrategia/LEEME.md          — el mapa
2. 00_estrategia/REGLAS.md         — las restricciones que no se saltan nunca
3. 00_estrategia/PROPIEDAD_DE_FICHEROS.md — quién escribe qué
4. 00_estrategia/PLAN_DE_CAMBIOS.md — la hoja de ruta y el estado de cada cambio
5. 00_estrategia/PROMPT_DE_ARRANQUE.md — autorizaciones vigentes y trampas conocidas
6. 05_calendario/bitacora/         — los ficheros de los últimos siete días
7. 05_calendario/metricas.json     — dónde está el canal en la escalera

Y si necesitas el porqué de algo: 00_estrategia/DIAGNOSTICO.md.

Cómo trabajamos:

- Hablamos los lunes (datos y decisiones) y, mientras dure la fase de cambio,
  también los viernes (revisar lo que la planificación escribió el jueves).
  Fuera de eso, solo si algo se rompe, se pierde trabajo, se cruza una línea
  ética o un número se mueve fuerte.
- Escribes en los ficheros de mi carpeta con device_commit_files y yo hago el
  commit. Los ficheros de .github/workflows/ están protegidos contra escritura
  remota: si hay que crear uno, me lo mandas y lo creo yo a mano.
- Todo lo que merezca recordarse acaba en un documento antes de cerrar la
  conversación. Lo que no esté escrito, se pierde.
- Coste cero. Sin trabajo recurrente para mí. Nada a mi nombre ni con mi cara.
- La audiencia manda. Si seguimos por debajo de 100 visualizaciones por vídeo,
  el canal está abocado a desaparecer. Diferenciarnos está bien, pero es un
  medio, no el objetivo: hay que seguir mejorando el proceso entero y cambiar
  lo que haga falta por el camino.

Hoy quiero tratar:
```

---

## Autorizaciones vigentes

La regla 11.7 de `REGLAS.md` protege tres ficheros. Un permiso dado «en la
conversación» se pierde con la conversación, así que aquí queda por escrito
**qué está autorizado, desde cuándo y hasta dónde llega.**

| Fichero | Estado | Alcance |
|---|---|---|
| `03_produccion/pipeline/voz.py` | **Autorizado el 28/08/2026** | Abierto. Se pidió para C7 (dos voces), pero Silvestre no lo acotó |
| `03_produccion/pipeline/montaje.py` | **Autorizado el 28/08/2026, solo para una cosa** | El manifiesto de subtítulos (`montaje.json`), ya aplicado. Cualquier otro cambio necesita permiso nuevo |
| `.github/workflows/producir.yml` | **Sigue protegido** | Y además `.github/workflows/` no se puede escribir en remoto: se le manda el fichero a Silvestre |

Otra decisión de propiedad, del 28/08: `01_bibliografia/BIBLIOGRAFIA_CURADA.md`
pasa a ser de la **revisión diaria**, que antes no tenía dueño y por eso
arrastraba defectos. Solo puede añadir lo que verifique contra la fuente.

---

## Cuatro trampas en las que ya se ha caído

No son anécdotas: cada una costó tiempo o un vídeo, y las cuatro se repiten
solas si nadie las tiene delante.

**1. Cada documento daba por supuesto que el movimiento lo ponía otro.**
Los subtítulos quemados se retiraron el 20/08; la respiración de zoom ya estaba
descartada. Ninguno de los dos documentos que las mencionaban decía que eran las
**únicas** fuentes de movimiento, así que durante ocho días el 85 % de cada
Short fue un fotograma congelado y nadie lo relacionó — pese a que el comentario
de `voz.py` lo decía con esas palabras: «*un vídeo sin ellos se percibe como un
pase de diapositivas*».
→ Cuando retires algo, busca qué dependía de ello. Cuando un documento diga que
otra pieza se encarga de X, comprueba que esa pieza sigue existiendo.

**2. Una restricción que nadie volvió a comprobar bloqueó C6 una semana.**
Toda la arquitectura de captura se diseñó para ahorrar minutos de render. El
repositorio es **público**, y los minutos de Actions en repos públicos son
ilimitados. El límite real es el `timeout-minutes: 150` del job, y un Short
entero a 30 fps son 7,8 minutos medidos.
→ Antes de diseñar alrededor de una restricción, comprueba que sigue siendo
cierta. Las de coste, sobre todo.

**3. «Mismo guion y mismo t, mismo píxel» nunca ha sido literalmente cierto.**
Medido el 28/08: renderizando **el mismo fichero sin tocar, dos veces**, difieren
8 de 14 fotogramas, siempre en los mismos ~368 píxeles de 254.016 (0,14 %): una
línea de 1 px del marco que Chromium rasteriza distinto según cuándo promociona
la capa. El delta máximo es 50 sobre 255, en un fondo casi negro. **No se ve.**
→ El suelo de ruido es ~0,06 % de los píxeles. Si comparas dos versiones y la
diferencia está por debajo de eso, no has cambiado nada. Si comparas contra cero,
vas a perseguir fantasmas. La regla 11.5 sigue valiendo para lo que fue escrita
—nada de `Math.random()`, nada de la hora del sistema— pero no como igualdad
byte a byte.

**4. `registro_publicaciones.json` guardaba el estado del momento de la subida.**
En modo `revision` eso es siempre `private`, y nadie lo actualizaba al publicar.
Consecuencia: `metricas.py` excluía los cinco Shorts y solo miraba `MDH-001`, y
la revisión diaria hablaba de vídeos «en privado» que llevaban días publicados.
Arreglado el 28/08 — el estado se le pregunta a YouTube y se corrige el registro.
→ Un campo que se escribe una vez y describe algo que cambia después, miente.

---

## Dónde está el proyecto a 28 de agosto de 2026

**El cuello de botella sigue siendo el mismo: no hay números.** Tres semanas
publicando y `metricas.json` vacío por dos fallos encadenados, los dos
arreglados hoy. La primera lectura de verdad es la del lunes 31. Hasta que
llegue, cualquier decisión sobre qué serie sobrevive o qué largo va el 12 de
septiembre se toma a ciegas, y conviene decirlo en vez de disimularlo.

**Lo que está en verificación, y en qué orden. Un cambio por producción:**

| Cuándo | Qué se mira |
|---|---|
| sáb 29 ago · MDH-004 | Primera prueba real del cron a tres horas. El largo **no** lleva C15 |
| lun 31 ago · MDS-006 | **Primer Short con C15.** Hasta verlo no entra ningún cambio visual más |
| lun 31 ago · métricas | Primera lectura con datos. Es la que desbloquea todo lo demás |
| jue 3 sep · demanda | Prueba real del cron de `demanda.yml` con dos horas |
| sem. 7 sep | **C7** (dos voces, `voz.py` autorizado) y **C16** (vocabulario dibujado) |

**Lo que está escrito y sin hacer:** la ficha `E02` de la bibliografía (tres
cifras y un DOI que no coincide); el estimador de duración de
`validar_guion.py`, que asume 150 palabras/minuto cuando la voz real hace 130 en
Shorts —medido, esperando a tener ocho muestras—; MDH-006, 007 y 008 sin adaptar
al formato nuevo, a propósito, uno por semana; y el largo del 12 de septiembre,
que se decide con las métricas del 7 delante.

**Lo que se decidió y conviene no volver a discutir:** no se clona la voz de
Silvestre por ahora (la condición que puso es incompatible con un repo público y
runners sin GPU); no se encienden los subtítulos quemados; no se usan fotos de
banco de imágenes (dependen de la red en tiempo de render y hacen que el canal
se parezca a todos los demás canales automatizados); y no hace falta tarjeta,
porque `gemini-3.1-flash-tts-preview` tiene nivel gratuito con la salida de
audio incluida.

---

## Qué NO hace falta meter en el prompt

Estas cosas ya están en los documentos y repetirlas solo alarga el mensaje:

- El diagnóstico del canal y por qué se cambió de rumbo → `DIAGNOSTICO.md`
- Qué hace cada tarea programada → sus propios prompts, que puedo leer y editar
- El criterio editorial → `REGLAS.md`
- El estado de los cambios → la tabla de `PLAN_DE_CAMBIOS.md`, con C15 y C16 al final
- Los números → `metricas.json`

## La prueba de que funciona

Si un yo recién arrancado con ese prompt no puede responderte a «¿en qué peldaño
está el canal y qué lo bloquea?» sin preguntarte nada, la documentación se ha
quedado corta — y eso es un defecto del proyecto, no del prompt. Arreglarlo es
parte del trabajo de cada lunes.
