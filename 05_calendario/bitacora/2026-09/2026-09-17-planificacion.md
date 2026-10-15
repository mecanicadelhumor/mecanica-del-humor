# Planificación — jueves 17 de septiembre de 2026, noche

Semana del **lunes 21 al sábado 26**. Sin nadie delante. Entrega en `.tar.gz`, no commit.

Primera comprobación, antes de tocar nada: `git log --oneline -5` sobre `origin/main` da
`4b2037a medición de demanda 2026-09-17`, `5bd9712 revisión diaria 17/09`, `f757bb1 precacheo
de voz (C27): MDS-017`, `195441f registro sincronizado` y `6a039a8 registro y expediente de
calidad: MDS-019`. **No hay ninguna entrega pendiente sin aplicar**: está el trabajo de la
revisión de esta mañana y la medición de demanda de hoy al mediodía. Se puede escribir en
`05_calendario/`.

No se ha llamado a ninguna herramienta de dispositivo ni se ha pedido ninguna autorización.
Se ha trabajado sobre un clon del repositorio público y se entrega paquete; el commit lo hace
la dirección.

Este prompt ya viene del repositorio (`00_estrategia/tareas/planificacion-jueves.md`, decisión
del 12/09). Se ha leído entero y también lo que es posterior a él: **las versiones 8, 9 y 9.1
de `PLAN_DE_CAMBIOS.md` mandan sobre la versión 7 que el fichero nombra**, y son las que han
decidido la mitad de lo de esta noche —sobre todo el tamaño del episodio largo—.

---

## 1 · Qué se ha escrito

| Fichero | Qué es |
|---|---|
| `guiones/MDS-021.es.json` · `MDS-022` · `MDS-023` · `MDS-024` · `MDS-025` | Los cinco Shorts, lunes a viernes |
| `guiones/MDH-008.es.json` | Episodio largo del sábado 26, **adaptado entero** |
| `guiones/MDH-007.es.json` | **Las dos notas de `revisiones/MDH-007.md`, aplicadas** |
| `publicaciones/*.json` (seis) | Título, descripción, etiquetas y primer comentario |
| `parrilla.json` | Seis emisiones nuevas, todas `"modo": "automatico"` |
| `CALENDARIO.md` | Tabla de la semana y estado de los largos |
| `demanda.json` | Las 24 consultas medidas, juzgadas una a una |
| `semillas_demanda.json` | Lo que hay que medir el jueves 24 |
| `pendientes_de_fuente.md` | Quinta tanda, al final |

`python3 04_agentes/validar_guion.py` sobre los siete guiones tocados: **cero errores**. Los
cinco Shorts y `MDH-007`, además, sin un solo aviso. `MDH-008` tiene tres avisos de C17, los
tres esperados y explicados abajo.

| | Escenas | Duración | Serie |
|---|---|---|---|
| MDS-021 · lun 21 | 6 | 50,0 s | El experimento |
| MDS-022 · mar 22 | 6 | 51,3 s | Esto no tiene gracia y esto sí |
| MDS-023 · mié 23 | 6 | 51,2 s | Ríete primero, te explico después |
| MDS-024 · jue 24 | 6 | 48,9 s | Esto no tiene gracia y esto sí |
| MDS-025 · vie 25 | 6 | 50,9 s | El experimento |
| MDH-008 · sáb 26 | 34 | 4 m 39 s | Mecanismos |

---

## 2 · Qué dice la demanda medida, y qué he decidido con ella

`demanda_bruta.json` es de hoy (12:42 UTC), trae las veinticuatro consultas que pedían las
semillas del 10/09 y su campo `avisos` está **vacío**. Cuota gastada: 2.424. Tercera semana
seguida con medición buena.

**Nueve de las veinticuatro consultas se rechazan por C17** —ficha o pregunta usadas hace
menos de seis semanas—, tres por falta de respaldo, una por respaldo débil para el formato,
una por bibliografía no verificable y cinco ya están producidas. Quedan cinco, y son
exactamente las cinco de la semana. **No ha sobrado ninguna**, y es la primera vez que pasa.

El aviso que dejé el 10/09 —«conviene que el corpus crezca antes de mediados de octubre»—
llega tres semanas antes de lo previsto. Números de hoy: **quedan veintiuna fichas sin usar de
setenta y siete, y solo unas doce pueden ser fuente central de un Short.** El resto son
duplicados deliberados, temas excluidos por criterio editorial, o manuales y volúmenes que no
traen un hallazgo que copiar.

### El caso nuevo, y el más accionable de la noche: fichas que existen y no se pueden usar

La regla del 15/09 —*lo que un estudio encontró se copia, no se deduce*— ha ordenado la semana
más que la demanda. Aplicada desde el principio y no como corrección, tiene un efecto que no
se había visto: **una ficha cuya referencia no identifica su artículo es una ficha
inutilizable**, porque no hay resumen que leer.

- **`F04` y `F05` están así.** El DOI que `BIBLIOGRAFIA_CURADA.md` da para `F04`
  (`10.1002/hbm.21444`) no corresponde al título que la ficha nombra, y no he podido encontrar
  ningún artículo que case con los dos. Con `F05` pasa lo mismo.
- Con ellas se cae **«qué le pasa a tu cerebro cuando te ríes»**: 91 millones en el top 10,
  cero de cinco responden, y es la mejor pregunta sin asignar que le queda al canal. `F01` y
  `F02` la responderían y están en ventana de C17 hasta el 30 de septiembre; `F03` responde
  otra pregunta, cerrada hasta el 10 de octubre. **El pilar F entero está bloqueado salvo
  `F03`.**
- **No hace falta ampliar el corpus para desbloquearla: hace falta corregir dos fichas.** Va
  en la sección «Para el codirector».

Y dos erratas más encontradas al leer los resúmenes, del mismo tipo que las tres que la
dirección corrigió el 15/09:

- **`C05`** figura con el título de otro artículo y con el DOI `10.1037/a0026994`, que
  corresponde a un trabajo sobre conducta adolescente. El artículo bueno es Greengross, Martin
  y Miller (2012), *Personality Traits, Intelligence, Humor Styles, and Humor Production
  Ability of Professional Stand-up Comedians Compared to College Students*, DOI
  `10.1037/a0025774`. Esta sí se ha podido usar: autores, año y revista identificaban el
  artículo aunque el título no.
- **`G03`** figura como de 2015 y sin autores. La página del artículo lo fecha en 2010 y lo
  firman Freeman y Ventis.

### Las cinco preguntas, y por qué estas

| Short | Pregunta | Top 10 | Responden | Por qué entra |
|---|---|---|---|---|
| MDS-021 | cómo es la personalidad de los cómicos | 84.013.775 | 0 de 5 | Hueco completo y era la cabeza de serie que dejé anotada el 10/09 |
| MDS-022 | por qué un chiste hace menos gracia la segunda vez | 95.365.692 | 0 de 5 | El hueco más limpio de la tanda; el mecanismo es el modelo de dos fases |
| MDS-023 | reírse es bueno para la salud | 472.476 | 5 de 5 | Única con competencia real **y floja**: la mayor tiene 407.877 y es de 2015 |
| MDS-024 | cómo mantener una conversación sin quedarse en blanco | 5.991.672 | 5 de 5 | Competencia fuerte, pero ninguno da una regla con nombre y dice de dónde sale |
| MDS-025 | por qué el humor ayuda a memorizar | 4.736.709 | 0 de 5 | Hueco completo, y la ficha pedía verificar el tamaño muestral: verificado |

**Tres de las cinco se han escrito con el resumen del artículo leído esta misma noche** —C05,
G03 y G04—, con la frase de origen copiada literal en `notas_humor`. Las otras dos no afirman
ningún resultado medido y lo dicen en el cierre: A06 es un modelo y L04 es un manual.

**Un rechazo que conviene mirar dos veces: «por qué chatgpt no tiene gracia».** Tiene `K01` y
`K04` libres, es la consulta con el autocompletar más limpio de toda la tanda y aun así no se
hace, porque `MDS-020` responde «puede la inteligencia artificial hacer chistes» el viernes 18,
tres días antes. Es la misma pregunta con otras palabras. Se libera el 30 de octubre y entonces
entra con `K04`, que trae el ángulo que a MDS-020 le faltaba: la comparación directa entre
humanos y modelos.

**Humor y atracción:** ni medido ni escrito. `C01` entra hoy en la lista de fichas que no
generan pregunta, por el mismo motivo que `D03`, `D04`, `D08` y `D09`: su propio título habla
de éxito de apareamiento y de diferencias por sexo.

---

## 3 · Fichas usadas y fichas evitadas (C17)

**Las cinco fichas centrales de los Shorts estaban sin abrir.** Segunda semana consecutiva sin
repetir ni una fuente en formato corto.

| Short | Ficha central | Estado antes de hoy |
|---|---|---|
| MDS-021 | `C05` — personalidad de los cómicos profesionales | sin abrir |
| MDS-022 | `A06` — formulación original del modelo de dos fases | sin abrir |
| MDS-023 | `G03` — humor y salud en la jubilación | sin abrir |
| MDS-024 | `L04` — «Truth in Comedy», el «sí, y además» | sin abrir |
| MDS-025 | `G04` — humor y memoria a corto plazo | sin abrir |

**Cómo se ha elegido:** primero el censo de los códigos de `fuente` de los treinta y dos
guiones españoles del repositorio, después empezar por las que no aparecían, y solo al final
mirar la demanda para ordenar. No ha hecho falta repetir ninguna ficha en los Shorts.

**Las que he evitado a propósito, y por qué:**

- **`F04`, `F05`** — no por repetición sino por referencia no verificable (arriba).
- **`H05`** — sostiene `MDH-007`, que se emite el **domingo 20**. Usarla el jueves 24 en el
  Short de conversación habría sido la misma fuente central cuatro días después. El Short de
  L04 no la roza.
- **`B04` y `B06`** — responderían «por qué me hace gracia el humor absurdo» mejor que nada, y
  están en `MDS-007` (01/09) y `MDS-014` (10/09).
- **`E01`, `E03`, `E04`, `D06`** — responderían «funcionan las risas enlatadas», que es de las
  mejores preguntas libres que quedan. Las cuatro en ventana. Se libera el 10 de octubre y
  queda anotada como cabeza de serie de octubre.
- **`C06`** — el mito del payaso triste. Sigue fuera del formato corto: pide matización
  responsable y cuarenta segundos no dan para ella. `MDS-021` no lo roza ni de lejos: no dice
  ni insinúa nada sobre la salud mental de los cómicos.

**Una decisión de C17 que no es automática y la dejo razonada, porque es la única discutible de
la noche.** `MDS-025` (humor y memoria, `G04`) se emite nueve días después de `MDS-018` (un
profesor gracioso enseña mejor, `G06`), y los dos rozan aprendizaje. La ficha es distinta y la
pregunta también, pero sobre todo **el ángulo es el contrario**: `MDS-018` cuenta qué humor
ayuda a aprender y `MDS-025` cuenta lo pequeño que es el estudio que lo mide. Es la misma
maniobra que hizo `MDS-014` con `MDS-004` y `MDH-005` —la letra pequeña de nuestro propio
material—, y esa maniobra le gustó a la dirección. Si aun así se ve como repetición, lo que hay
que mover es `MDS-025`, no reescribirlo: el guion se sostiene solo en cualquier semana.

**En `MDH-008` sí se repiten fuentes, y no se han cambiado.** `I01`, `L01`, `A05` y `A01` son
las que ese guion tenía desde que se escribió; `L01` sostuvo `MDS-005` y `MDS-008`, `A05`
sostuvo `MDS-010` y `A01` está en cuatro piezas del corpus. El validador avisa tres veces.
Reescribir las fuentes de un episodio ya escrito para esquivar un aviso sería elegir la
bibliografía por el calendario, que es justo lo que C17 no quiere. Lo que sí he cuidado es que
ninguna sostenga aquí lo mismo que allí.

---

## 4 · Revisiones aplicadas

**`revisiones/MDH-007.md`** — las dos notas, aplicadas. **Y lo importante: sin tocar ni una
narración.** La caché de voz está indexada por el texto de cada narración (C27, C33.2), así que
`MDH-007` no pierde ni una escena sintetizada de cara a su emisión del domingo 20, que es
exactamente lo que la dirección pedía el 15/09 al moverlo.

1. **Escena 19**, `dato` sin `fuente`, la única de las seis. Tomo la segunda salida que ofrecía
   la nota: pasa a `enunciado`, como la 20 y la 21. No le pongo fuente porque no he podido
   comprobar que `J02` sostenga específicamente que el punto de intervención sea la
   interpretación y no el miedo, y asignarle una fuente a una frase ya escrita es lo que
   prohíbe la regla 2.
2. **Escena 31**, `fuente: "H06"` para una afirmación que no es la de H06. **He leído el
   resumen de Felsman, Gunawardena y Seifert (2020) esta noche**: son dos experimentos (n = 74
   y n = 131) de veinte minutos de ejercicios de improvisación, con medidas de pensamiento
   divergente, tolerancia a la incertidumbre y afecto positivo. No dice nada del diseño del
   curso ni de convertir el fallo en contenido. `H05` tampoco. Así que se retira la fuente. La
   escena pasa a `comparacion` —las dos caras que la propia narración enfrenta, el desastre y
   el temario— y no a `enunciado`, porque las escenas 29, 30 y 32 ya son enunciados y cuatro
   seguidas dejan la pantalla quieta.

**`revisiones/MDH-008.md`** — pedía la reescritura completa al formato nuevo. Hecha (abajo).

**Las dos notas hay que borrarlas del repositorio y un `.tar.gz` no borra ficheros**, así que
lo digo aquí: al aplicar el paquete, `rm 05_calendario/revisiones/MDH-007.md` y
`05_calendario/revisiones/MDH-008.md`.

**Notas que NO he tocado:** `MDS-006`, `MDS-009`, `MDS-011`, `MDS-013`, `MDS-015`, `MDH-004`,
`MDH-005` y `MDH-006` están marcadas como resueltas o cerradas por la propia revisión diaria.
No son mías para archivar.

---

## 5 · Decisiones editoriales

### El episodio largo se ha hecho más corto de escenas a propósito, y es la decisión de la noche

El patrón de adaptación pide «escenas más cortas y más numerosas». `MDH-007` lo cumplió con 41
escenas y **por eso no llegó a su sábado**: con una petición de voz por escena y diez al día
(C33.2), el precacheo de miércoles a viernes no lo llenaba, y la dirección tuvo que moverlo al
domingo 20.

`MDH-008` sale con **34 escenas, 4 m 39 s, y ninguna escena por encima de once segundos**. Las
dos mitades de la regla se cumplen —cada escena tiene una sola idea y ninguna se queda quieta—
pero el episodio cabe en el presupuesto de voz: de martes a viernes son cuarenta peticiones
para treinta y cuatro escenas, con la cuota del sábado de reserva para los rechazos. **Cuando
entre C36 —una llamada por vídeo— esta restricción desaparece y el episodio siguiente puede
partirse más fino.** Lo dejo escrito para que dentro de un mes nadie lea «34» y piense que es
descuido.

Lo demás de la adaptación, para el registro: rótulo de portada fuera y el episodio abre con el
chiste del trastero, primera risa sobre el segundo ocho; personaje en seis escenas y siempre
reaccionando después; dos intervenciones del escéptico, las dos por debajo de doce palabras;
«enunciado» del 48 % al 38 %; y risas repartidas **por distancia y no por cuenta** (segundo 8,
~95 s, ~170 s, ~205 s y ~285 s), que es la regla 13 tal como quedó corregida el 12/09 después
de MDH-006.

**Un solo chiste sostiene el episodio entero.** El del trastero entra en la escena 1, se
desmonta en la 12 y vuelve en la 26 a demostrar la regla de la última palabra —«duermo en el
trastero ahora» se resuelve demasiado pronto; «ahora duermo en el trastero», no—, con su
premisa dicha otra vez en la misma frase, como pide la regla 13 para un callback a más de
noventa segundos. En la versión anterior el chiste aparecía en la escena 8 y no volvía nunca.

**Y he quitado una cifra sin fuente:** la versión anterior decía que «el noventa por ciento del
trabajo» está en el tercer paso. No está en `L01` ni en ninguna ficha. Queda «ahí está casi
todo el trabajo». Es la misma decisión que se tomó con los «quince intentos» de `MDH-006`.

### Las series se han elegido por la forma, otra vez, y dos se repiten

«El experimento» y «Esto no tiene gracia y esto sí» salen dos veces cada una, alternadas y
nunca en días seguidos. Dos preguntas de esta tanda son un estudio con protagonistas que
termina en una cifra, y dos son dos versiones casi idénticas de la misma cosa. Forzar cinco
series distintas habría metido una respuesta en una forma que no le va, que es lo que produjo
el `MDS-011` «despiezado». Faltan «Desmonta el chiste» y «Diagnósticos»: ninguna pregunta apta
pedía su forma.

**Y la forma se cumple, no solo se declara.** `MDS-022` cuenta el mismo chiste dos veces —la
primera vez y la segunda son las «dos versiones casi idénticas»— y `MDS-024` enfrenta dos
respuestas a la misma frase, «ya» y «ya, y además». Las dos traen su escena `comparacion`, que
es lo que comprueba P10, y los dos «El experimento» traen su `dato` con `fuente`.

### El chiste va primero, y los cinco pasan la prueba del WhatsApp

El gracioso de la familia al que no se le acaba el material de cosas que le salen mal; el jefe
que te dice que te vistas para el puesto que quieres y te presentas en pijama; la risoterapia
obligatoria a las ocho de la mañana; el señor de la boda que contesta a todo «ya» durante
cuarenta minutos y al final dice que ha sido un placer; y el grupo de control que se pasó veinte
minutos sentado sin móvil y aun así mejoró. Ninguno necesita explicación por delante y ninguno
tiene víctima: los tres primeros van a costa de quien narra.

### Cuatro decisiones de rigor que han cambiado un guion

- **`MDS-023` no cuenta el moderador por sexo** que aparece en el resumen de `G03`. La frase
  literal dice que la adaptabilidad de los estilos de humor depende del estrés percibido «as
  well as gender». En cuarenta segundos, una diferencia entre hombres y mujeres se lee como una
  afirmación sobre lo que le pasa a cada uno por serlo, y eso `REGLAS.md` lo rechaza en fase de
  demanda. No es un dato que se esconda: es un dato que no cabe bien, y está dicho en
  `notas_humor` y en `demanda.json`.
- **`MDS-025` no dice que el humor baje el cortisol.** El resumen lo menciona en el «Context»
  como lo que se sabía antes, no como resultado del estudio. La regla del 15/09 manda copiar lo
  que el estudio encontró, no lo que su introducción da por sabido.
- **`MDS-022` no le atribuye a `A06` ningún resultado.** El capítulo de Suls es de 1972, es un
  libro y no se ha podido leer; la ficha solo describe el modelo. El Short dice que la segunda
  vez falta el primer paso **porque es lo que el modelo predice**, y el cierre lo dice en voz
  alta: «esto es lo que predice un modelo de los años setenta, no un experimento con chistes
  repetidos».
- **`MDS-024` declara que su fuente es un manual.** `L04` enseña una técnica, no mide nada, y
  el cierre lo admite: «esto sale de un manual de improvisación, no de un experimento». Es la
  única forma honesta de responder una pregunta de conversación con la bibliografía que
  tenemos, y es además lo que ninguno de los cinco competidores hace: decir de dónde sale su
  consejo.

### Y los cinco terminan diciendo dónde falla

`MDS-025` es el caso extremo de la semana y probablemente el Short más de marca que hemos
escrito: coge el «43,6 %» que circula por todas partes, enseña de dónde sale —veinte personas,
diez por grupo— y remata con que el grupo que no vio nada también mejoró. `MDS-021` cierra
admitiendo que el test lo rellena cada cómico sobre sí mismo, y `MDS-023` que a nadie lo
mandaron a una risoterapia a las ocho.

---

## 6 · Lo que falta, y para quién

### Para el codirector

1. **Dos fichas de la bibliografía están rotas y bloquean el pilar F entero.** `F04` y `F05` no
   identifican ningún artículo localizable: el DOI de `F04` (`10.1002/hbm.21444`) corresponde a
   otro trabajo. Con ellas está bloqueada «qué le pasa a tu cerebro cuando te ríes», 91 millones
   en el top 10 y cero de cinco respuestas. `01_bibliografia/` no es fichero mío y no lo he
   tocado. **Arreglarlas cuesta una búsqueda y desbloquea la mejor pregunta libre del corpus.**
2. **`C05` y `G03` tienen erratas menores** (título y DOI la primera, año y autores la segunda),
   ya detalladas arriba. Ninguna impide usarlas, pero son del mismo tipo que las tres que se
   corrigieron el 15/09 y conviene revisarlas de una vez.
3. **El corpus necesita crecer, y ahora sí con fecha.** Quedan unas doce fichas que puedan ser
   fuente central de un Short. A cinco por semana son dos semanas y media. En
   `semillas_demanda.json` hay tres preguntas medidas a propósito sin ficha —«por qué hay
   chistes que envejecen mal», «el humor se hereda de los padres», «por qué nos reímos en un
   funeral»— que son, si dan demanda, el encargo concreto para el agente bibliotecario.
4. **Al aplicar el paquete, borrar `05_calendario/revisiones/MDH-007.md` y `MDH-008.md`**: las
   dos están aplicadas y un `.tar.gz` no borra ficheros.

### Para la revisión diaria (no son ficheros míos y no los toco)

1. **`04_agentes/explorador_de_demanda.py` sigue devolviendo el autocompletar con la
   codificación rota**, tercera semana. Siete semillas de doce vuelven limpias y cinco siguen
   dando «por qu?» y «r?e». El patrón está confirmado: las semillas con tildes vuelven mal y las
   que no las llevan, bien. Es decodificación de la respuesta, no de la consulta. Las semillas
   nuevas van sin acentos otra vez.
2. **`04_agentes/metricas.py` sigue sin calcular la mediana de los últimos veinte Shorts a las
   48 horas** (C26). Con el punto de control del 27 de septiembre a diez días, ese número deja
   de ser una mejora y pasa a ser lo que falta para poder discutirlo.
3. **`MDS-016` pasó de mil visualizaciones y no sabemos por qué.** No es cosa mía arreglarlo,
   pero sí decirlo desde aquí: la lectura del lunes 21 abre por sus fuentes de tráfico, y de las
   cuatro hipótesis de la versión 9 la única que esta planificación puede alimentar es la de la
   demanda medida. Si resulta ser esa, la consecuencia para mí es directa: ordenar por hueco y
   no por volumen está funcionando, y hay que apretar por ahí.

### Para `ESTADO.md`, que escribe la revisión diaria

**Nada pendiente del codirector para que la semana salga sola.** Los seis guiones validan sin
errores, la parrilla está completa con `modo` en las seis emisiones y el largo cabe en la cuota
de voz. Lo único con reloj es el precacheo: **`MDH-008` necesita que `voz_adelantada.yml` corra
de martes a viernes**, y si el cambio recomendado el 15/09 —que corra todos los días— ya está
hecho, sobra margen.

---

## 7 · Lo que NO hace falta de la dirección esta noche

Nada. La semana está cerrada, valida sola y se sube sola. Las dos únicas cosas que pido —las
fichas rotas del pilar F y el borrado de las dos notas de `revisiones/`— no bloquean ninguna
emisión: la primera bloquea una pregunta de la semana que viene y la segunda es limpieza.
