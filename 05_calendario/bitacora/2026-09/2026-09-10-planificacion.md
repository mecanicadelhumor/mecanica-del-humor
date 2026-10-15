# Planificación — jueves 10 de septiembre de 2026, noche

Semana del **lunes 14 al sábado 19**. Sin nadie delante. Entrega en `.tar.gz`, no commit.

`mcp__remote-devices__device_list_dir` sobre `C:\MisProyectos\Humor` no responde —la sesión
programada corre en la nube y esta noche no hay puente con el ordenador de la dirección—,
así que se ha trabajado sobre un clon del repositorio público y se entrega paquete. Sin
`git push`: no hay credenciales aquí y la salida SSH está bloqueada allí (comprobado el
31/08). El commit lo hace la dirección.

---

## 1 · Qué se ha escrito

| Fichero | Qué es |
|---|---|
| `guiones/MDS-016.es.json` · `MDS-017` · `MDS-018` · `MDS-019` · `MDS-020` | Los cinco Shorts, lunes a viernes |
| `guiones/MDH-007.es.json` | Episodio largo del sábado 19, **adaptado entero** |
| `guiones/MDH-006.es.json` | **Cuatro correcciones** de `revisiones/MDH-006.md`, aplicadas |
| `publicaciones/*.json` (seis) | Títulos, descripciones, 15 etiquetas y primer comentario |
| `parrilla.json` | Seis emisiones nuevas, todas `"modo": "automatico"` |
| `CALENDARIO.md` | Tabla de la semana y estado de los largos |
| `demanda.json` | Las 24 consultas medidas, juzgadas una a una |
| `semillas_demanda.json` | Lo que hay que medir el jueves 17 |
| `pendientes_de_fuente.md` | Cuarta tanda, al final |
| `revisiones/MDH-006.md` y `MDH-007.md` | **Borrados**: aplicados |

`python3 04_agentes/validar_guion.py` sobre los seis guiones nuevos: **cero errores y cero
avisos**. `MDH-006` corregido sigue sin errores.

| | Escenas | Duración | Serie |
|---|---|---|---|
| MDS-016 · lun 14 | 6 | 48,9 s | Esto no tiene gracia y esto sí |
| MDS-017 · mar 15 | 6 | 50,8 s | Ríete primero, te explico después |
| MDS-018 · mié 16 | 6 | 50,8 s | El experimento |
| MDS-019 · jue 17 | 6 | 49,5 s | Ríete primero, te explico después |
| MDS-020 · vie 18 | 6 | 50,0 s | El experimento |
| MDH-007 · sáb 19 | 41 | 5 m 16 s | Diagnósticos |

---

## 2 · Qué dice la demanda medida, y qué he decidido con ella

`demanda_bruta.json` existe, es de hoy (12:43 UTC), trae las **veinticuatro** consultas que
pedía `semillas_demanda.json` del 03/09 y su campo `avisos` está **vacío**. Cuota gastada:
2.424. Segunda semana consecutiva con medición buena; ya no es noticia, y eso es lo mejor
que se puede decir de un medidor.

**Trece de las veinticuatro consultas vienen secuestradas** —los cinco primeros resultados
son entretenimiento, no respuestas—. Sus cifras no se han usado para ordenar nada. Pero,
aplicando la aclaración de la dirección del 04/09 sin excepciones, **eso las mejora, no las
descarta**: cuatro de los cinco Shorts de esta semana salen precisamente de consultas
secuestradas, porque un sitio donde hoy contesta el entretenimiento y no la divulgación es
la definición de un hueco.

El caso extremo, para que quede escrito: **«un profesor gracioso enseña mejor» devuelve
323.584.560 visualizaciones en el top 10**, la cifra más alta que ha medido este canal
nunca, y **cero de cinco responden**: son sketches de profesores de trece a treinta y cinco
segundos. Ordenar la semana por esa columna la habría escrito al revés. Con la cifra
descontada y el hueco delante, es un Short excelente, y va el miércoles.

### Lo que ha mandado de verdad esta semana: C17, no la demanda

De las veinticuatro consultas:

- **6 aptas y asignadas** (cinco Shorts y el largo).
- **5 aptas sin asignar**, que son la cola natural del 17: personalidad de los cómicos,
  qué le pasa a tu cerebro cuando te ríes, reírse es bueno para la salud, quedarse en
  blanco en una conversación y «por qué chatgpt no tiene gracia».
- **7 rechazadas por C17** —ficha o pregunta ya usadas—, no por falta de fuente.
- **3 rechazadas por falta de respaldo** (vergüenza ajena, memes, y por competencia real
  las de conversación y hablar en público).
- **3 ya producidas** esta semana o la pasada.

Es la primera vez que el cuello de botella no es la bibliografía ni la demanda: es no
repetirse. Está todo razonado candidato a candidato en `demanda.json`.

### Dos rechazos que conviene mirar dos veces

- **«Cómo distinguir una risa falsa de una de verdad»** se rechaza por C17 por **segunda
  semana consecutiva**: `MDH-004` (29/08) ya lo contó con casi las mismas escenas, aunque
  la ficha buena (`F03`, dos vías neurales) siga libre. La ventana se cierra el **10 de
  octubre**. Tener la fuente libre no basta.
- **«Cómo es la personalidad de los cómicos»** es **apta y no se produce**, y no está en
  `pendientes_de_fuente.md` porque su problema no es la fuente. `C05` la responde bien. El
  titular que la haría funcionar sale de `C06` —el mito del payaso triste—, y la propia
  ficha pide «matización responsable». Cuarenta segundos no dan para eso, que es
  exactamente el razonamiento por el que `REGLAS.md` prohíbe humor y atracción en formato
  corto: sin el matiz, lo que queda es «los cómicos están mal de la cabeza». Con `C05` a
  solas sí cabe. Cabeza de serie para la semana del 21.

**Humor y atracción:** ni medido ni escrito. `D03`, `D04`, `D08` y `D09` siguen libres y
siguen sin entrar en `semillas_demanda.json`, por lo mismo de siempre — no se mide lo que
no se puede producir.

---

## 3 · Fichas usadas y fichas evitadas (C17)

**Las seis fichas de los cinco Shorts no se habían usado NUNCA.** Es la primera semana del
canal en la que ningún Short repite fuente.

| Short | Ficha central | Apoyo | Estado antes de hoy |
|---|---|---|---|
| MDS-016 | `I05` — prosodia de la ironía | — | sin abrir |
| MDS-017 | `E06` — cosquillas y evolución de la risa | — | sin abrir |
| MDS-018 | `G06` — humor en el aula (metaanálisis) | — | sin abrir |
| MDS-019 | `G05` — humor en publicidad (metaanálisis) | — | sin abrir |
| MDS-020 | `K02` — cómicos y modelos de lenguaje | `K03` | **pilar K entero sin abrir** |

`MDH-007` conserva `J02`, `J01`, `H05` y `H06`, que eran ya sus fuentes y siguen siendo
las únicas del corpus que responden la pregunta. `J01` y `J02` no han salido en ningún
otro guion: `MDS-013` (09/09) se reservó a propósito para `J04`/`J05`.

**Cómo se ha elegido:** primero el censo de los códigos de `fuente` de los veintisiete
guiones españoles, y después empezar por los que no aparecían. **No ha hecho falta usar
ninguna ficha repetida**, así que no hay nada que justificar por ese lado.

**Inventario:** de las 77 obras quedan **treinta sin usar** (eran treinta y seis el jueves
pasado). Siete de esas treinta no generan pregunta —dos son duplicados deliberados del
corpus, cuatro están excluidas por criterio editorial y una (`J03`) no es material de
Short—, así que el fondo real es de **veintitrés**. A cinco o seis fichas por semana, eso
son unas cuatro semanas antes de que C17 empiece a morder de verdad. **Conviene que el
corpus crezca antes de mediados de octubre**, y ese aviso es lo más accionable que sale de
esta sesión.

---

## 4 · Revisiones aplicadas

**`revisiones/MDH-007.md`** — pedía la reescritura completa al formato nuevo. Hecha. Nota
borrada.

**`revisiones/MDH-006.md`** — cuatro defectos, los cuatro aplicados. Nota borrada.

1. **Escena 12**, `personaje: "duda"` sobre un `dato` que solo presenta un hallazgo
   positivo → **`piensa`**, como proponía la nota (regla 14.3).
2. **Escena 32**, el `a` decía «Cohesión, desempeño, *desgaste*» y «desgaste» no se dice en
   ninguna de las 40 narraciones → **«Cohesión y *desempeño*»** (regla 14.1).
3. **Escena 22**, el tercer paso del diagrama no lo decía la voz → añadida la frase que
   faltaba a la narración: «Y el permiso es solo con esa persona: no se hereda al resto».
   `pasos` sin tocar.
4. **Escena 35**, «quince intentos» era una cifra sin fuente. **Tomo la segunda salida de
   las dos que ofrecía la nota: quitar el número.** No he podido comprobar que `D02` mida
   esa proporción, y asignarle una fuente a un número ya escrito es justo lo que prohíbe
   la regla 2. Queda «una bien colocada pesa más que muchas sueltas».

**Un efecto secundario, dicho aquí porque no lo arreglo yo:** la corrección 3 sube la
escena 22 de 10,5 s a 13,8 s y con ella salta el aviso de ritmo visual. Es la frase que
pedía la nota literalmente, así que no la recorto ni parto la escena por mi cuenta —sería
inventar un cambio que la revisión no pidió—. Si molesta, partir esa escena en dos es
trivial y el sitio natural es después de «Espera a que lo haga el otro».

**Aviso de reloj, y es el único que corre de verdad esta noche:** **MDH-006 se produce el
sábado 12.** Estas cuatro correcciones solo llegan al vídeo si el paquete se aplica antes
de que corra el cron de producción. Si se aplica después, el episodio sale con los cuatro
defectos —ninguno lo rompe, los tres primeros son de la regla 14 y el cuarto es un número
sin fuente que nadie va a poder verificar—. No es motivo para correr; es motivo para
saberlo.

**Notas que NO he tocado:** `MDS-006`, `MDS-009`, `MDS-011`, `MDS-013`, `MDS-015`,
`MDH-004` y `MDH-005` están marcadas como resueltas o cerradas por la propia revisión
diaria, y `MDH-008` describe una adaptación que toca la semana que viene. No son mías para
archivar. `MDS-011` merece una línea aparte: su corrección ya no se puede aplicar —el vídeo
está publicado desde el 07/09— y la nota sigue abierta en el buzón.

---

## 5 · Decisiones editoriales

**El campo `icono` existe, comprobado en `04_agentes/esquema_guion.json`, y se estrena.**
La escena 1 de los cinco Shorts entra con uno de los ocho dibujos de `02_marca/iconos.svg`
y **cuatro palabras o menos**: `i-bocadillos`, `i-muelle`, `i-publico`, `i-publico` y
`i-bocadillos`. Ninguna de las cinco es ya una tarjeta de texto sobre fondo. Y se reparten
por dentro donde el mecanismo tiene uno: `i-grieta` en los cierres que dicen dónde falla,
`i-balanza` donde algo se pesa, `i-bisagra` donde está el punto que lo decide todo,
`i-ruptura` donde se rompe la regla. `MDH-007` lleva cuatro. En total, **catorce iconos en
seis guiones**, contra cero en los once Shorts anteriores.

**Las series se han elegido por la forma, no por turno.** «El experimento» y «Ríete
primero» salen dos veces cada una, alternadas y nunca en días seguidos. Dos preguntas de
esta tanda son estudios con protagonista que terminan en una cifra, y dos son chistes que
se sostienen solos y cuya explicación es el premio. Forzar cinco series distintas habría
significado meter una respuesta en una forma que no le va, que es lo que produjo el
`MDS-011` «despiezado».

**Y la forma se cumple, no solo se declara.** Cada Short tiene principio, medio y final:
las dos escenas del chiste con su pausa de 1,35 s, el giro, y el cierre que dice dónde
falla. Los dos «El experimento» traen su escena `dato` con `fuente` y el «Esto no tiene
gracia y esto sí» su `comparacion`, que es lo que comprueba P10.

**El chiste va primero, y los cinco pasan la prueba del WhatsApp.** La cena familiar que
escala a doce, el sobrino que amenaza con los dedos y gana, el profesor de latín cuyo
chiste reíamos porque ponía el examen, la sintonía de un banco donde nunca entré, y los
veinte chistes que son el mismo. Ninguno necesita explicación por delante y ninguno tiene
víctima.

**Tres decisiones de rigor que han cambiado un guion:**

- `MDS-020` cuenta **lo que los estudios del pilar K hicieron** —veinte cómicos
  profesionales escribiendo con modelos, un examen montado sobre los pies de foto del New
  Yorker— y **no sus conclusiones**, porque las fichas recogen el diseño y no el
  resultado. Habría sido facilísimo escribir «y salió mal».
- `MDS-017` **no roza la autocosquilla**, que sigue sin fuente en el corpus desde el 20/08.
  Responde por qué las cosquillas dan risa, no por qué no puedes hacértelas tú. Está
  anotado también en `pendientes_de_fuente.md` para que dentro de tres meses nadie lea el
  guion y dé la exclusión por levantada.
- `MDS-016` **no afirma nada sobre emojis**. La prosodia de la ironía está medida; el
  emoji no lo ha estudiado nadie. Eso va en el cierre, dicho como límite, que es su sitio.

**El cierre de `MDS-020` declara en voz alta que el guion lo ha escrito una máquina.** Es
la regla 7 dicha dentro del vídeo y no solo en la descripción, y de paso es el mejor
«dónde falla» que ha tenido el canal: si el chiste del principio te ha hecho gracia, lo ha
escrito la misma cosa que el vídeo acaba de decir que no sabe hacer chistes.

**`MDH-007`, el episodio más delicado del calendario.** Se ha mantenido entero el bloque
del límite —rasgo con grados y no enfermedad, un cuestionario no diagnostica, y si condiciona
la vida lo que toca es un profesional— y se le ha añadido lo que no tenía: un **cierre que
dice dónde falla**. Dos cosas, las dos honestas y ninguna inventada: todo se mide con un
cuestionario que rellena uno sobre sí mismo, y a un taller de improvisación se apunta quien
ya se atrevía. Las dos risas son de reconocimiento propio y ninguna va a costa de quien
tiene el miedo. Título nuevo: **«Por qué se ríen de mí»**, que es lo que se escribe.

---

## 6 · Lo que falta, y para quién

**Para la revisión diaria** (no son ficheros míos y no los toco):

1. **`04_agentes/explorador_de_demanda.py` sigue devolviendo el autocompletar con la
   codificación rota.** Ha mejorado: cuatro de doce semillas vienen limpias y una de ellas
   —«inteligencia artificial humor»— ha servido para juzgar el Short del viernes. Pero
   ocho siguen dando «por qu?» y «r?e», y el contenido de esas ocho son letras de
   canciones. El patrón apunta a decodificación de la respuesta, no a la consulta: las
   semillas sin tildes vuelven bien. Mientras tanto he escrito las semillas nuevas sin
   acentos a propósito.
2. **`04_agentes/metricas.py` sigue sin calcular la mediana de los últimos veinte Shorts a
   las 48 horas** (C26). Sin ese número, el punto de control del 27 de septiembre se
   discute de memoria y el del 15 de noviembre no se puede discutir.
3. **La escena 22 de `MDH-006`** queda en 13,8 s por la corrección 3 de arriba, con su
   aviso de ritmo visual. Si se quiere partir, el corte natural está dicho más arriba.

**Para `ESTADO.md`, que escribe la revisión diaria** (lo dejo aquí porque ella lo lee y yo
no soy dueña de ese fichero): **`MDS-011` sigue en privado desde el 07/09 y su nota de
`revisiones/` ya no tiene arreglo posible** —el vídeo está publicado o perdido, pero el
guion no se toca—. Lo que sí se puede cerrar es la nota. Y la línea «Pendiente del
codirector» de esta noche sigue siendo la del 10/09: el secreto `GEMINI_API_KEY` en
`producir.yml` antes del lunes 14, o C7 se enciende sin nada que encender.

**Lo que NO hace falta de la dirección esta noche.** Nada. La semana está cerrada, valida
sola y se sube sola.

**Nota sobre C27, que es nueva y afecta al ritmo de esta tarea:** `MDH-007` queda
**cerrado esta noche** y no se va a tocar, que es lo que `voz_adelantada.yml` necesita para
empezar a sintetizar de martes a viernes contra la cuota del 2.5. Si aun así hubiera que
corregirlo, la caché está indexada por el texto de cada narración: se cambia **solo la
escena afectada** y las otras cuarenta se conservan. Que ese sea el reflejo, y no rehacer
el guion entero.
