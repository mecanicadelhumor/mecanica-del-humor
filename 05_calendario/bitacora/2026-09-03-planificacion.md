# Planificación — jueves 3 de septiembre de 2026, noche

Semana del **7 al 12 de septiembre**. Primera tanda de la historia del canal elegida
con **demanda medida de verdad**.

Comprobación 3 de `PROPIEDAD_DE_FICHEROS.md` antes de tocar nada: `git log --oneline -5`
sobre `origin/main` trae `cb591f6 medición de demanda 2026-09-03`, `bfed822 revisión diaria
3/9` y el expediente de MDS-009. La bitácora de la planificación del 27/08 está en el
repositorio, o sea que **no hay ninguna entrega pendiente sin aplicar**. Se puede trabajar.

Sin acceso al ordenador de Silvestre: la tarea corre programada en la nube y el puente de
dispositivos no existe en este modo. Se ha clonado el repositorio público y se entrega
`.tar.gz`, como estaba previsto.

---

## Lo que he escrito

| Fichero | Qué es |
|---|---|
| `guiones/MDS-011.es.json` | lun 7 · «El experimento» · *cómo ser más gracioso* · C04, C03 |
| `guiones/MDS-012.es.json` | mar 8 · «Esto no tiene gracia y esto sí» · *cómo contar un chiste bien* · L02, L03 |
| `guiones/MDS-013.es.json` | mié 9 · «Desmonta el chiste» · *miedo a que se rían de ti* · J04, J05 |
| `guiones/MDS-014.es.json` | jue 10 · «Diagnósticos» · *estilos de humor test* · B05, B06 |
| `guiones/MDS-015.es.json` | vie 11 · «Ríete primero, te explico después» · *por qué se contagia la risa* · E03, D06 |
| `guiones/MDH-006.es.json` | sáb 12 · largo adaptado, 40 escenas, 4m47s |
| `guiones/MDH-005.es.json` | **corregido**: aplicadas las notas de `revisiones/` (produce el sábado 5) |
| `demanda.json` | 21 candidatos juzgados contra las 77 obras |
| `semillas_demanda.json` | 24 preguntas para la medición del jueves 10 |
| `pendientes_de_fuente.md` | tercera tanda, añadida al final |
| `publicaciones/*.json` | seis ficheros de metadatos |
| `parrilla.json` | seis emisiones nuevas, todas `automatico` |
| `CALENDARIO.md` | semana nueva, reserva actualizada, decisión del largo del 12 |

`python3 04_agentes/validar_guion.py` sobre los siete guiones: **cero errores**, código de
salida 0.

---

## Qué dice la demanda medida, y qué he decidido con ella

`demanda_bruta.json` existe, es de hoy (12:42 UTC), su campo `avisos` está **vacío** y trae
las veinte consultas con visualizaciones. Tres semanas pidiéndolo y a la tercera ha
llegado. Se acabaron los `vistas_top10: null`.

### El hallazgo de método, que es más importante que cualquier número suelto

**El volumen del top 10 no mide lo que parece que mide.** De las veinte consultas, **once
devuelven entretenimiento en vez de explicaciones**: «qué dice de mí mi sentido del humor»
saca 63 millones de visualizaciones y sus cinco primeros resultados son canciones de rimas
y sketches. Eso no es competencia y tampoco es demanda de respuesta: es que YouTube no
entiende la consulta como una pregunta.

Si esas cifras se hubieran usado tal cual para ordenar, la semana se habría escrito al
revés. Así que cada candidato de `demanda.json` lleva ahora un campo nuevo,
**`pertinencia_top5`**: cuántos de los cinco primeros resultados responden realmente la
pregunta, leído título a título. Es un juicio, no una medida, y por eso va con el
razonamiento al lado en `por_que_esa_competencia`.

Con ese filtro, el mapa queda así:

- **Dos consultas con demanda limpia y grande:** «cómo caer bien a la gente» (5 de 5,
  5.795.365) y «cómo ser más gracioso» (5 de 5, 2.025.194). La primera ya se hizo ayer
  (MDS-009). La segunda abre la semana.
- **Once consultas secuestradas por el entretenimiento** (0 o 1 de 5). Su número no dice
  nada sobre nosotros, pero su vacío sí: nadie responde.
- **Un hueco limpio y diminuto:** «gelotofobia», 9.025 visualizaciones entre diez
  resultados, el mejor de 2010. Competencia nula y demanda casi nula.

### La pregunta que más demanda tiene, y por qué no es un largo

El calendario dejaba el largo del 12 a decidir entre `MDH-007` y **un largo nuevo sobre
«cómo ser más gracioso»**, «la pregunta con más demanda de todo el corpus». La medición le
da la razón: es la única consulta cuyos cinco primeros resultados responden la pregunta, y
ninguno de los cinco cita un estudio.

Y aun así ese largo **no se escribe, porque ya existe**. Es `MDH-001`, «Nadie nace
gracioso», publicado el 18 de agosto, construido sobre `H01` (cinco escenas), `H03`
(cuatro) y `C02` (tres) — exactamente las fichas que el candidato proponía. Escribirlo de
nuevo tres semanas después es un remake. C17 lo prohíbe y además sería tirar una semana.

Lo que sí hago es **llevarme esa demanda al Short**, por el único ángulo que MDH-001 no
ocupó: cómo se puntúa la gracia (`C04`, la tarea de pies de foto). No es una lista de
trucos, que es el motivo por el que la pregunta estaba reservada al formato largo.

### Y entonces, ¿por qué MDH-006 y no MDH-007?

La demanda **no desempata**: «humor en el trabajo» no se midió, y «miedo a que se rían de
ti» devolvió 74 millones de visualizaciones sin un solo resultado en tema. Con la demanda
callada, decide otra cosa:

- El cierre de **MDH-005**, que se produce el sábado 5 a las 03:00, promete literalmente
  «el próximo episodio va del sitio donde equivocarse sale más caro: el trabajo».
- El cierre de **MDH-006** promete a su vez la gelotofobia.

Poner MDH-007 el 12 obligaba a reescribir el cierre de un guion que entra en producción en
menos de treinta horas, y a romper dos promesas para no ganar nada. MDH-006 el 12,
MDH-007 el 19, y las dos promesas se cumplen solas.

**Nota para quien adapte MDH-007 el jueves 10:** hay que reescribir su título de
publicación a lenguaje natural. «Gelotofobia» suma 9.025 visualizaciones entre diez
resultados; «por qué se ríen de mí» y «miedo a que se rían de ti» sí se buscan. El
episodio es bueno; el título con el que está escrito no lo encontraría nadie.

---

## Fichas: cuáles he usado y cuáles he evitado

C17, paso 2: **empezar a elegir por las que no aparecen**.

**Estrenadas esta semana — nueve fichas que no se habían abierto nunca:**
`C03`, `L02`, `L03`, `J04`, `J05`, `B05`, `B06`, `E03`, `D06`.
Más `C04`, que existía solo como apoyo de pasada en MDH-001 y nunca había sido central.

El corpus pasa de **30 fichas usadas de 77 a 41**. Quedan 36 sin abrir (34 si se descuentan
`E05` y `J06`, que son los duplicados deliberados de control). Los pilares `K` (humor e
inteligencia artificial) y `G` (humor aplicado) siguen casi enteros sin tocar, y por eso
la lista de semillas de la semana que viene está construida a partir de ellos.

**Repeticiones que he evitado a propósito:**

- `E01` y `E02` (Provine) — la tentación obvia para «por qué se contagia la risa». `E02`
  ha sostenido MDH-004, MDS-002 y MDS-006; `E01` sostuvo MDS-002. Vetadas como fuente
  central hasta el 6 de octubre. MDS-015 se hace con `E03` y `D06` y **el cierre admite en
  voz alta que ninguna de las dos mide el contagio en sí**. Prefiero un hueco declarado a
  una cuarta vuelta de las 1.200 risas.
- `B01` y `B02` — MDS-014 va de tests de estilos de humor y no toca ninguna de las dos.
  Habría sido el tercer vídeo en tres semanas sobre los cuatro estilos de Martin.
- `A01` (ruptura benigna) — habría encajado en MDS-013 y no entra: es central en MDH-002 y
  aparece en cinco guiones. J04 sostiene el Short solo.
- `L01` — MDS-012 va de contar chistes y usa `L02` y `L03`. `L01` es central en MDS-008,
  de anteayer.

**La única repetición que queda, y por qué:** `C04` en MDS-011, que ya salía en MDH-001 en
dos escenas. No fue central allí —MDH-001 lo sostienen H01 y H03— y aquí se cuenta desde
otro sitio: allí era «se puede entrenar», aquí es «se puede puntuar, y así». Ninguna otra
ficha libre mide la producción de humor de forma mostrable en pantalla: `C02` es central en
MDS-007 (del martes pasado), `C01` lleva ⚠️ por su afirmación sobre diferencias entre sexos
y no se usa, y `C05` y `C06` describen la personalidad del cómico profesional pero sus
fichas no traen ni un hallazgo concreto que se pueda enseñar sin inventarlo.

### El Short que he tirado a la basura ya escrito

**«Cómo distinguir una risa falsa de una de verdad».** Tenía demanda medida (4.821.125),
tenía tres fuentes (`D07`, `E04`, `F03`), estaba redactado entero y pasaba el validador.

Y el aviso de C17 del validador me hizo abrir MDH-004, producido el 29 de agosto. Está
todo allí: la comparación «Las dos risas» con `E04` (escena 19), el dato «24 sociedades»
con `D07` (escena 20), «algo más que el azar» (escena 21) y el límite del laboratorio
(escena 27). **Cuatro escenas casi calcadas, ocho días después.** Es exactamente el
hallazgo de Silvestre del 31/08 —las 1.200 risas en tres vídeos en siete días— repitiéndose
con otras fichas.

Se retira. En su sitio entra MDS-013 con `J04` y `J05`, dos fichas vírgenes. La pregunta
vuelve a estar disponible a partir del 10 de octubre, y entonces mejor con `F03` de
columna, que es lo único de los tres que MDH-004 no gastó.

**Y esto vale como prueba de que la red de seguridad funciona.** El aviso automático de
`validar_guion.py` no dijo «esto es una repetición» —no puede saberlo—, dijo «mira aquí».
Miré, y había que tirar el guion. Sin ese aviso lo habría publicado.

---

## Revisiones aplicadas

**`revisiones/MDH-005.md`** → aplicada entera y movida a `revisiones/_aplicadas/2026-09-03-MDH-005.md`.

1. *Escena 9, el número que no se dice.* La narración pasa a «esas **cuatro** direcciones»,
   que es el número que ya estaba en pantalla. Quien escucha sin mirar lo recibe.
2. *Cian decorativo en tres escenas `dato`.* Retirado de «menos» (esc. 2), «2003» (esc. 9)
   y «peor bienestar» (esc. 28). Ninguna de las tres es un término del oficio.
3. *El hallazgo C17 que la nota dejaba a mi criterio (B01/B02 repiten de MDS-004).*
   **Decisión: el episodio no se rehace.** Un largo puede profundizar en la misma taxonomía
   que un Short de la semana anterior; eso no es repetirse, es la razón de que existan dos
   formatos. Lo que no puede es rematar igual. Y ahí sí había trabajo que hacer, así que:
4. *Hallazgo propio, del mismo tipo que el de la escena 9.* La escena 36 —la «letra
   pequeña», la firma del canal— tenía **tres puntos en pantalla y la narración solo decía
   el primero**. Los otros dos, que son el argumento fuerte de la crítica de B02, no
   existían para quien escucha sin mirar. Ahora la escena dice dos y el tercero pasa a
   escena propia (37). Efecto secundario buscado: la crítica de B02 se cuenta aquí con la
   circularidad de los ítems, que es distinto de como se contó en MDS-004 («mide más cosas
   que estilos de humor»). El episodio queda en 40 escenas y 4m57s.

**`revisiones/MDH-006.md`** → aplicada al adaptar el guion, movida a
`revisiones/_aplicadas/2026-09-03-MDH-006.md`.

**Siguen abiertas:** `revisiones/MDH-007.md` y `revisiones/MDH-008.md` — los dos largos que
quedan sin adaptar. MDH-007 se adapta el jueves 10.

**Cerradas hace días pero todavía en la carpeta:** `MDH-004.md`, `MDS-006.md` y
`MDS-009.md`. Las tres dicen «RESUELTO» o «nota cerrada» en su primera línea y no tienen
acción pendiente. No las he movido porque las resolvió la revisión diaria y no yo; si
molestan al leer la carpeta, se archivan igual que las otras dos.

---

## La adaptación de MDH-006, con números

| | Antes | Después |
|---|---|---|
| Escenas | 26 | **40** |
| Duración | — | **4m47s** (rango 4-6 min) |
| `formato` | no lo tenía | `largo` |
| «enunciado» | 65 % | **42 %** |
| Primera risa | no había | **segundo 8** |
| Personaje | ninguno | 5 escenas (2, 12, 28, 39, 40) |
| Escéptico | ninguno | 2 (esc. 10 y 26, de 8 y 9 palabras) |

Gancho nuevo, que sustituye al rótulo de portada: *«En una reunión de doce personas se me
ocurrió algo gracioso. Y lo dije. — Se rieron dos. Uno era yo.»* Segunda risa en la escena
4 («la reunión de marzo», que además es la premisa del episodio) y tercera en la 28 («una
risa obligatoria no es información: es protocolo»). Callback en la 39: los diez de la
reunión siguen calculando.

**Ni un dato ni una fuente han cambiado.** Solo se han repartido, recortado y cambiado de
tipo visual, que es lo que dice el patrón de MDH-004.

---

## Decisiones editoriales de la semana

- **Dos series se repiten y una falta, y las dos cosas están bien.** «El experimento» sale
  el lunes; ninguna pregunta apta pedía la forma que falta. Es lo que autoriza el cambio
  del 31/08: la demanda elige el tema y la serie solo da la forma. No he forzado la
  rotación.
- **MDS-011 no es un manual de trucos.** «Cómo ser más gracioso» en cuarenta segundos se
  convierte justo en eso, y por ahí el canal no pasa. Entra por la medición.
- **MDS-013 no quema la gelotofobia.** La pregunta medida —«miedo a que se rían de ti»— se
  responde solo en la pieza que `J04` sostiene: dónde está la línea entre broma y burla.
  `J01` y `J02`, que son el episodio entero, no se tocan. El Short además alimenta al largo
  del 19.
- **MDS-014 corrige a nuestros propios vídeos.** MDS-004 y MDH-005 usan los cuatro estilos
  de B01; este Short cuenta que un test de estilos mezcla el rasgo con el estado. Poner la
  letra pequeña de tu propio material es lo más de marca que puede hacer este canal.
- **MDS-015 termina admitiendo que no lo sabemos.** El contagio de la risa no está medido en
  las 77 obras. Se dice en el cierre, con esas palabras.
- **Ni un chiste con víctima colectiva.** Los cinco de esta semana son de familia, de amigos
  y de uno mismo. MDS-013 habla *sobre* el humor a costa de un grupo, que es distinto, y lo
  hace para decir que no funciona.
- **Nada de humor y atracción**, ni en los guiones ni en las semillas de la semana que
  viene. `D03`, `D04`, `D08` y `D09` están sin abrir y siguen sin abrirse: que una ficha
  esté libre no la hace producible.

---

## Lo que falta, y lo que no es mío

### Para la revisión diaria (`03_produccion/` y `04_agentes/` son suyos)

1. **`explorador_de_demanda.py` devuelve el autocompletar inservible.** De las cuatro
   semillas medidas hoy, tres traen la codificación rota —`por qu?` en vez de `por qué`,
   `el sentido del humor a?o nuevo`— y el contenido son letras de canciones: «tendría que
   llorar por ti y me río como un loco», «el sentido del humor bananero». **No he usado ni
   una sugerencia para juzgar nada.** El resto del fichero (YouTube y Wikipedia) está
   impecable. Parece un problema de codificación al leer la respuesta del autocompletar,
   más que del diseño.
2. **C19 no se puede cumplir del todo desde el guion, y esta es la semana en que entra.**
   `PLAN_DE_CAMBIOS.md` v4 dice que la escena 1 de un Short no puede ser una tarjeta de
   texto a partir de la semana del 7. He hecho la mitad que me toca: **los cinco Shorts
   tienen cuatro palabras o menos en pantalla en la escena 1** («El gracioso *oficial*»,
   «Versión *uno*», ««El *navegador*»», «Test de *humor*», «Como una *alarma*»). La otra
   mitad —que ahí haya un dibujo del vocabulario de `02_marca/iconos.svg` en vez de texto—
   **no tiene forma de expresarse en `esquema_guion.json`**: `figura` exige datos de
   gráfica o una ruta de imagen, y no hay ningún tipo ni campo para colocar un icono. Sin
   eso, C19 es inaplicable por mucho que lo intente el guionista. Propuesta concreta: un
   campo `icono` (nombre del símbolo en `iconos.svg`) admisible en cualquier escena, o un
   `tipo: "icono"` nuevo, más su soporte en `escena.html`. Es de la revisión diaria, no
   mío.
3. **El prompt del guionista sigue induciendo el cian mal puesto.** Cinco escenas `dato`
   con cian decorativo en dos semanas (MDS-006, MDS-009 y las tres de MDH-005) es un patrón,
   no un descuido. `04_agentes/prompts/guionista_corto.md` explica bien la regla en abstracto
   pero no dice lo único que hace falta: **en una escena `dato`, el `pie` no lleva cian salvo
   que la palabra marcada sea el nombre que la investigación le da a la cosa.** Una línea.

### Para el próximo jueves

- **Adaptar MDH-007** para el sábado 19, y reescribirle el título (ver arriba).
- **La lista de semillas se agotó y casi me deja sin semana.** De las veinte preguntas del
  27/08, quince estaban producidas o asignadas, cuatro excluidas por falta de fuente y una
  se ha caído esta noche por C17: quedaba **una** sin usar. He tenido que apurar hasta la
  última pregunta viable. La lista nueva tiene 24 preguntas y está construida al revés —
  partiendo de las fichas sin abrir y preguntando qué escribiría alguien para llegar a
  ellas—, pero conviene no volver a llegar tan justo.
- **Dos sondas nuevas** en las semillas para el punto de control del 27 de septiembre:
  «cómo mantener una conversación sin quedarse en blanco» y «cómo caer bien en una primera
  conversación». Si ese día toca abrir la conversación de ensanchar el tema al humor dentro
  de las habilidades sociales, mejor llegar con cifras que con opiniones. Medirlo cuesta
  cero.

### Sobre las métricas

`metricas.json` está actualizado a **31/08 08:41** y no tiene todavía ninguna lectura de
MDS-006 a MDS-010. O sea que esta semana se ha elegido **solo con demanda de búsqueda, sin
ninguna señal de rendimiento**. La primera lectura útil llegará con la tarea del lunes 7.

### Pendiente de Silvestre

**Nada**, más allá de aplicar el paquete y hacer el commit. No hay nada roto que solo él
pueda arreglar. (Esta línea la escribe la revisión diaria en `ESTADO.md`; se deja aquí
escrita porque ella lee esta bitácora.)

Dos detalles de la aplicación del `.tar.gz`, porque un tar no borra:

- `05_calendario/revisiones/MDH-005.md` y `MDH-006.md` **hay que borrarlos a mano**
  (`git rm`). Sus sustitutos van dentro del paquete, en `revisiones/_aplicadas/`.
- Nada de `03_produccion/`, `04_agentes/`, `metricas.json`, `demanda_bruta.json`,
  `registro_publicaciones.json`, `qa/` ni `ESTADO.md` va en el paquete. Solo ficheros de
  los que esta tarea es dueña.

### Y una cosa que no he hecho a propósito

**No he mandado ninguna notificación.** El canal tiene que volar solo; lo que hay que saber
está aquí escrito.
