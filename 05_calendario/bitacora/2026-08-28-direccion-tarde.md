# Dirección — 28 de agosto de 2026, segunda sesión

Continuación de `2026-08-28-direccion.md`, con lo que salió al aplicar aquello.

---

## 1. `metricas.py` tenía dos fallos, y el segundo era peor que el que se vio

**El que reventó** (`IndexError`, línea 104): cuando un vídeo todavía no tiene datos,
la API de analítica **no omite la clave `rows`: la devuelve vacía**. Y
`r.get("rows", <por defecto>)` solo usa el valor por defecto si la clave *falta*. Así
que devolvía `[]` y el `[0]` de la línea siguiente se salía de rango. Un lector de
métricas que se cae cuando aún no hay métricas es inútil exactamente el día que hace
falta. Arreglado con `r.get("rows") or [[0] * len(cab)]`, y además cada vídeo va en su
propio `try`: uno que falle ya no tumba la lectura de los demás.

**El que no se vio, y es el que importa.** El script elegía qué vídeos medir así:

```python
if p.get("estado") != "public" or not p.get("video_id"):
    continue
```

Y `registro_publicaciones.json` guarda el estado del **momento de la subida**, que en
modo `revision` es siempre `private`. Nadie lo actualiza cuando Silvestre le da a
publicar. De los seis vídeos del canal, el único con `public` escrito es `MDH-001`, del
uno de agosto. **Los cinco Shorts estaban excluidos y lo iban a seguir estando para
siempre.** Aunque no se hubiera caído, la primera lectura habría salido vacía y
`metricas.json` seguiría hoy sin una sola cifra — que es justo el cuello de botella que
llevamos tres semanas señalando.

Arreglado en la raíz: **el estado se le pregunta a YouTube**, no al registro.
`videos.list` ya se llamaba para sacar la duración; añadir `status` a `part` cuesta las
mismas unidades de cuota (1 por cada 50 vídeos). Y de paso `metricas.py` **corrige el
registro**: escribe el estado real de cada vídeo, con `_estado_leido_utc`. Los dos
ficheros son de GitHub Actions, así que no pisa a nadie.

Efecto secundario que vale la pena: la revisión diaria dejará de confundirse con vídeos
«en privado» que llevan días publicados.

`metricas.yml` cambia **una línea**: el `git add` incluye ahora también
`registro_publicaciones.json`.

---

## 2. La cuota de la API: vamos sobrados, pero había un derroche

La cuota de la YouTube Data API son **10.000 unidades al día** y se renueva a
medianoche del Pacífico, o sea **a las 09:00 de España** todo el año. La API de
*analítica* tiene cuota aparte, así que `metricas.yml` no compite.

Lo que cuesta cada cosa:

| Trabajo | Unidades | Cuándo |
|---|---|---|
| Subir un vídeo (`videos.insert`) | 1.600 | a diario |
| Miniatura, primer comentario, lista | ~150 | a diario |
| Medir la demanda | **101 × pregunta** (hoy 20 → 2.020) | los jueves |

Día normal: ~1.750 de 10.000. Jueves: ~3.800. **Sobra sitio para unas sesenta preguntas
más** antes de acercarse al techo. No hay problema, y Silvestre no tiene que volver a
lanzarlo a mano.

**Pero había un derroche que yo mismo acababa de introducir.** Al poner dos horas de
cron en `demanda.yml` (porque el `schedule` de Actions se pierde), la segunda pasada
repetía la medición entera y gastaba otras ~2.000 unidades para escribir exactamente lo
mismo. Arreglado igual que en `cola.py`: `explorador_de_demanda.py` sale en un segundo
si `demanda_bruta.json` ya tiene medición de hoy. `--rehacer` lo fuerza.

**Y un tope de gasto, que no existía.** La lista de preguntas la reescribe la
planificación cada semana y puede crecer sola. Sesenta preguntas serían 6.060 unidades
y, en un mal orden, dejarían al canal **sin cuota para subir el vídeo de esa noche**,
que cuesta 1.600. Ahora el explorador para en 3.500 unidades, avisa de cuántas preguntas
quedaron sin medir y sigue. La medición importa; publicar importa más.

**Detalle afortunado de las horas:** la cuota se renueva a las 07:00 UTC y el tercer
intento de producción es a las 08:23 UTC. Es decir, la última oportunidad del día cae
siempre **después** del reinicio: un día no puede quedarse sin vídeo por lo que se gastó
el día anterior.

---

## 3. El cron de la demanda está bien programado

Comprobado en `origin/main`: `26 12 * * 4` y `52 15 * * 4`. El 4 es jueves (0 = domingo),
las horas son UTC y las dos caen antes de que la planificación despierte a las 20:00 UTC.
El orden es correcto.

Que no corriera el 27 encaja con lo mismo que le pasa a los otros dos workflows: el
`schedule` de Actions estaba en minuto 0 y se perdió. Con dos horas de intento la
probabilidad de perder las dos es mucho menor. **La prueba real es el jueves 3 de
septiembre.** Si vuelve a fallar con dos crons, entonces no es la hora y hay que mirar
otra cosa. La planificación de esa noche ya avisa en su primera línea si el fichero no
está.

---

## 4. El chiste de MDS-005 no tiene gracia, y es un fallo de método

Silvestre, sobre el Short de hoy: «el chiste no tiene gracia; a nivel de contenido van a
peor». Tiene razón en el diagnóstico y conviene ser preciso en la causa, porque no es
falta de talento del generador: **el guion se escribió al revés.**

Primero se eligió el mecanismo —«el conector cambia de sitio y el chiste funciona o
no»— y después se escribió un chiste **que pudiera demostrarlo**. Al chiste se le pidió
ser desmontable, no tener gracia, y salió exactamente lo que se pidió. Las dos versiones
del chiste del médico son malas, y un Short que abre con un chiste malo ya no se
recupera: el espectador decide en el segundo tres.

**Corregido en `04_agentes/prompts/guionista_corto.md`** con una sección nueva y un
orden que no se negocia: primero el chiste —uno que contarías en voz alta a un amigo sin
la explicación detrás—, después se mira qué mecanismo tiene dentro, y si el mecanismo
que se quería explicar no está en ningún chiste bueno, **se cambia de mecanismo, no de
chiste**. Con cinco criterios de descarte concretos, MDS-005 como ejemplo negativo, y la
prueba del algodón: si para que tenga gracia hay que explicar algo antes, no vale.

**Matiz importante, y es una buena noticia:** los cinco Shorts que escribió la
planificación del 27 son **claramente mejores** que los de la tanda anterior. «Mi abuelo
murió tranquilo mientras dormía; no como los cuatro que iban en el coche con él»
(MDS-007), «mi hijo dice que de mayor quiere ser como yo; le he dicho que no, que se
esfuerce» (MDS-008), «mi vecino toca el piano a las tres de la mañana, yo le acompaño
con la aspiradora a las siete» (MDS-010). Esos sí son chistes. La sensación de «van a
peor» viene de que MDS-005 es el peor de la primera tanda y es el que se ve hoy.

**Aviso sobre MDS-007 (martes 1):** el chiste del abuelo es humor negro sobre un
accidente. Está dentro de la regla 1 —es ficticio, no hay víctima real y es literalmente
el objeto de estudio del episodio, que va sobre si el humor negro dice algo de la
inteligencia— pero conviene que Silvestre lo sepa antes de que salga, no después.

**Lo que NO se ha tocado: la voz.** Silvestre dice «sobre todo por la narración», y ahí
hay un segundo problema que el prompt no arregla: `edge-tts` lee el chiste y la
explicación con **la misma voz, el mismo ritmo y la misma entonación**. Un chiste contado
con la cadencia de una nota a pie de página no es un chiste, es una cita. Eso es C7
escalón 1 —dos voces— y toca `voz.py`, que está protegido: va con permiso explícito, en
la conversación del lunes, con las métricas delante.

---

## 5. «Que no sean todo escenas de PowerPoint»

El dato, contado: de las **58 escenas** de los diez primeros Shorts, **32 son
`enunciado`** (texto centrado sobre el fondo). Con los `cierre`, **el 72 % de lo que se
ve es texto sobre fondo oscuro**. `figura` —el único tipo que muestra una imagen— se usa
**cero veces** en los diez. C15 hace que ese texto se mueva; no hace que deje de ser
texto.

**Dos cosas se han hecho ya**, y las dos son de prompt, no de código:

- **Máximo tres escenas `enunciado` por Short.** Las demás salen de los tipos que ya
  existen y casi no se usan: `comparacion`, `dato`, `lista`, `diagrama`, `cita`. Elegir
  el tipo de escena pasa a ser parte de escribir el guion: una comparación se entiende
  sola, un enunciado hay que leerlo.

### C16 · El vocabulario dibujado (propuesta, no aplicada)

**Sobre las imágenes reales libres de derechos: no.** Y no por licencias, que las hay
usables. Por tres razones, en orden de peso:

1. La regla 11.6 prohíbe depender de internet en tiempo de render, así que tendrían que
   vivir en el repositorio y engordarlo.
2. Una foto de banco de imágenes hace que el canal se parezca a **todos los demás
   canales automatizados**. Es la forma más rápida de perder lo único que este canal
   tiene ya construido: un aspecto propio.
3. El canal se llama Mecánica del Humor y su lenguaje es el plano técnico. Una foto de
   archivo de gente riéndose no dice nada que el plano no diga mejor.

**Lo que sí:** un **vocabulario dibujado propio**, en el mismo lenguaje que el Engranaje.
Ocho piezas de partida, SVG en línea, cero peticiones, cero licencias, deterministas:
la bisagra (el conector), el muelle (la tensión), la ruptura (la expectativa que se
desvía), los bocadillos (quién cuenta y quién recibe), la pausa, la grieta (dónde falla),
el público (quién se ríe y quién lleva la cuenta) y la balanza (el hallazgo discutido).
Están en `02_marca/iconos.svg` y la hoja de muestra en `02_marca/iconos_hoja.png`.

**No están enchufados a nada todavía**, a propósito: el lunes 31 sale MDS-006, que es el
primer Short con C15, y **hasta verlo no entra ningún cambio visual más** (regla 11.1).
Si C15 se ve bien, C16 entra la semana del 7 de septiembre con un tipo de escena nuevo
—`ilustracion`— y la regla de una ilustración por Short, nunca dos.

**Y una tercera pieza para más adelante: el Escéptico tiene voz pero no cara.** El
esquema de guion ya admite `voz: "esceptico"` y el largo lo usa. Darle una silueta propia
—otra cabeza del mismo taller, distinta— convierte la pantalla en una conversación en vez
de en una sucesión de rótulos. Se decide cuando C16 esté verificado.

---

## 6. Cierre de la sesión

**Silvestre autoriza tocar `voz.py`.** Sin acotar. Queda por escrito en
`00_estrategia/PROMPT_DE_ARRANQUE.md`, en la tabla de autorizaciones vigentes,
porque un permiso dado en una conversación se pierde con la conversación. Se
usará para C7 escalón 1 (dos voces) la semana del 7 de septiembre, después de
verificar C15 — no antes, o no sabremos cuál de los dos cambios movió el número.

**El chiste del abuelo (MDS-007, martes 1) queda aprobado.**

**El criterio que manda cuando haya duda**, con sus palabras: *«la audiencia va a
mandar. Si seguimos con menos de 100 visualizaciones por vídeo el canal estará
abocado a su desaparición»*. Es la corrección al riesgo de esta semana:
diferenciarse de los demás canales automatizados es un **medio**, no el
objetivo. Si dentro de tres semanas los números dicen que el vocabulario
dibujado no mueve nada y otra cosa sí, se cambia. Añadido al bloque copiable del
prompt de arranque para que ningún yo futuro lo pierda de vista.

Sobre los iconos: *«un pequeño paso adelante en la buena dirección»*. Ni más ni
menos: C16 no es la solución del problema de atractivo, es un ladrillo.

## 7. Una comprobación antes de cerrar, y lo que enseñó

Mañana se produce MDH-004, que es formato largo y **no** lleva C15. Antes de
irme comprobé que el cambio de ayer no le afecta: rendericé catorce fotogramas
de MDH-004 con la versión de antes y con la de ahora.

Salían **368 píxeles distintos de 254.016** por fotograma. Un susto — hasta que
rendericé **el fichero viejo contra sí mismo**: los mismos 368 píxeles.

| Comparación | Píxeles distintos (14 fotogramas) |
|---|---|
| viejo vs viejo | 2.578 |
| nuevo vs nuevo | 1.839 |
| viejo vs nuevo | 2.206 |

Mi cambio difiere **menos** que el ruido del propio navegador. El episodio largo
no cambia. Pero el hallazgo de fondo importa más que la comprobación:
**«mismo guion y mismo t, mismo píxel» (regla 11.5) nunca ha sido literalmente
cierto.** Chromium rasteriza distinto una línea de 1 px del marco según cuándo
promociona la capa; delta máximo 50 sobre 255, en fondo casi negro, invisible.
El suelo de ruido es ~0,06 % de los píxeles, y quien compare dos versiones
contra cero va a perseguir fantasmas. Anotado en `PROMPT_DE_ARRANQUE.md`.

**Cambio aplicado de todas formas:** `transform-origin` y `will-change` de
`#escena` pasan a estar dentro del bloque `html[data-fmt="v"]`. No era la causa,
pero el episodio largo no usa el acercamiento y no tiene por qué cargar con las
propiedades que lo hacen posible.

