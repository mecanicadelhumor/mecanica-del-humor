# Dirección — lunes 31 de agosto de 2026

Primera conversación con métricas de verdad delante. Silvestre trae cinco cosas y
una pregunta de fondo: si el canal tiene arreglo o no.

---

## 1. El vídeo largo del sábado no se publicó, y ya no puede volver a pasar

**Qué pasó.** MDH-004 se produjo el 29 sin incidencias, se subió a la 01:29 UTC y
**se quedó en privado para siempre**. Su emisión en `parrilla.json` llevaba
`"modo": "revision"`, y en ese modo `cola.py` sube `private` **sin `publicar_en`**:
no hay nada que lo publique. Silvestre lo descubrió dos días después en Studio y lo
publicó a mano esta mañana.

**Lo que agrava el fallo:** la revisión diaria del 29 y la del 30 lo dieron por
publicado, con este razonamiento textual: «su hora de publicación ya pasó, así que
está publicado aunque el registro diga `private`». Es cierto en modo `automatico`
y falso en modo `revision`, y nadie tenía la distinción escrita.

**Respuesta, en tres capas:**

1. **Ya estaba resuelto para esta semana**, y conviene decirlo: la planificación del
   27 escribió MDS-006 a MDS-010 y MDH-005 con `"modo": "automatico"`. MDH-004 fue
   el último en modo revisión. Desde hoy `cola.py` sube en privado con `publishAt`
   y YouTube publica solo, con ~15 h entre la subida y la emisión.
2. **El defecto por defecto.** `modo = emision.get("modo", "revision")`: un olvido
   fallaba hacia el silencio. Encargado a la revisión diaria cambiar el defecto a
   `automatico`. Que el olvido falle hacia publicar.
3. **La regla en el prompt de la planificación:** `"modo": "automatico"` sin
   excepción, con el caso de MDH-004 escrito al lado para que se entienda por qué.

Y en el prompt de la revisión diaria, la distinción que faltaba: `private` **con**
`publicar_en` es correcto; `private` **sin** `publicar_en` en una emisión de la
parrilla es un fallo grave, porque ese vídeo no sale nunca.

**Lo que Silvestre acepta a cambio, y hay que dejarlo escrito:** nadie mira el
vídeo antes de que salga. `qa.py` corre **después** de la subida en `producir.yml`
—es un informe, no una barrera— y la revisión diaria de las 11:30, que sí cae
dentro de la ventana, no toca YouTube. Con una decena de espectadores por vídeo,
un mal vídeo no cuesta nada y él lo puede retirar. Se revisa cuando haya público.

## 2. Los números, y lo que de verdad dicen

| | Vistas de por vida | Suscriptores | Comentarios | Me gusta |
|---|---|---|---|---|
| MDH-001 · 002 · 003 | 13 · 28 · 8 | 0 | 0 | 4 en total |
| MDS-001 a 005 | 6 · 11 · 13 · 3 · 11 | 0 | 0 | **0** |

**Cinco Shorts, 44 visualizaciones entre los cinco.** El criterio de aceptación de
C2 —al menos uno por encima de 50 en 48 horas— falló por un factor de diez. El plan
decía qué hacer entonces («el problema está en los tres primeros segundos y se va a
C9 antes de producir más») y no se hizo: se siguió produciendo. Queda dicho.

**El diagnóstico honesto de ese número.** Un Short nuevo casi siempre recibe una
prueba del feed. Seis a trece visualizaciones significa que la prueba se hizo y se
cortó enseguida: la gente desliza antes de leer. Y lo que ve en esa décima de
segundo es texto blanco centrado sobre fondo oscuro con voz sintética, que es la
firma reconocible del vídeo automatizado. De las 58 escenas de los diez primeros
Shorts, 32 son `enunciado` y `figura` no aparece ni una vez: el 72 % de lo que se ve
es texto sobre fondo. C15 hace que ese texto se mueva; no hace que deje de ser
texto.

**El indicio bueno, y es el único: la búsqueda.** MDS-002 saca el **63,6 %** de sus
visualizaciones de `YT_SEARCH`; MDS-003, el **46,2 %**. El feed de Shorts aporta
entre el 9 % y el 23 % en esos dos. La superficie que el diagnóstico de agosto daba
por la más difícil de alcanzar está respondiendo, y la que se daba por segura no.
Números minúsculos, pero es la única señal direccional del corpus y seguirla es
gratis: **a partir del jueves la demanda medida elige el tema y la serie solo da la
forma**, en vez de repartir series y buscar la pregunta después.

## 3. Repetirse: medido, y no es escasez

Silvestre: «hay cosas que se repiten, como que te ríes más junto a alguien que
solo». Cruzados los códigos de `fuente` de todos los guiones:

- Se usan **30 fichas de las 77**. **Cuarenta y siete no se han abierto nunca.**
- **Doce salen en más de un guion; cuatro en tres o más.**
- `E02` —las 1.200 risas anotadas en la calle— sale en **MDS-002 (25 ago), MDH-004
  (29 ago) y MDS-006 (31 ago)**. Tres vídeos en siete días, exactamente lo que él
  notó. `A01` sale en cinco guiones.

No falta bibliografía: sobra costumbre. **C17**, con dos reglas —una ficha central
no vuelve a serlo en seis semanas; se elige empezando por las no usadas— en los dos
prompts, más un aviso determinista en `validar_guion.py` encargado a la revisión
diaria.

## 4. El CSV de Studio, y por qué la solución no era arreglar el `glob`

El agente de métricas se quejó de no poder leer el CSV. Es cierto y tiene arreglo:
`glob.glob(EXPORTES / "*.csv")` no es recursivo y Studio deja siempre los ficheros
dentro de una subcarpeta. **Trampa del arreglo obvio:** Studio exporta *tres* CSV y
`sorted(...)[-1]` elegiría `Totales.csv`, que no tiene ni columna de vídeo ni
impresiones. Hay que quedarse con el que tenga las dos columnas. Encargado.

**Pero el problema de fondo era otro, y ese sí importa.** Pedirle un CSV cada
semana es trabajo recurrente, y la regla 5 lo prohíbe. Y hay algo peor: **Studio no
da impresiones ni CTR de miniatura para los Shorts** —ahí la decisión del
espectador es deslizar, no hacer clic—, así que la escalera de C14 **nunca iba a
poder medir el producto principal del canal**. Cinco de cada seis vídeos son Shorts.

**C14 se sustituye por dos escaleras.** La de los Shorts se mide entera con la API:
vistas desde `SHORTS` en 48 h ≥ 50 · `porcentaje_visto` ≥ 70 % · me gusta por 100
vistas ≥ 3 · suscriptores por mil ≥ 5. La del largo conserva impresiones y CTR
para cuando haya CSV, y si no lo hay se salta a la retención. **El canal está en el
peldaño S1.** Nadie vuelve a pedir el CSV; si aparece uno, se lee.

## 5. Los avisos que no llegan

Silvestre: los agentes dicen que le mandan avisos, él no recibe ninguno, y tampoco
quiere. Confirmado: los tres prompts usaban `PushNotification`. **Prohibida en los
tres.** En su lugar, la revisión diaria mantiene **`05_calendario/ESTADO.md`**, un
fichero de cinco líneas que sobrescribe cada día: estado OK o incidencia, último
vídeo, próxima emisión, una línea «Pendiente de Silvestre» —que casi siempre dirá
«nada»— y el enlace a la bitácora del día.

La regla que lo sostiene: si un agente necesita algo que se puede automatizar, lo
automatiza o lo deja como encargo; **no lo convierte en una petición**.

## 6. La música

Tres pistas reales para seis vídeos por semana (`cama.mp3` es copia byte a byte de
otra): cada pista suena una vez y media por semana. **C18**: ampliar a diez o doce
con licencia limpia y atribución literal, y que `musica_de()` excluya duplicados
por hash y no repita hasta agotar la lista. Prioridad baja, encargado a la revisión
diaria detrás de la verificación de C15.

Vale la pena decir por qué es prioridad baja aunque moleste: **hoy el espectador
que más vídeos ve del canal es Silvestre.** Que la música le canse es un síntoma
del problema de audiencia, no un problema aparte.

## 7. El orden de aquí al 27 de septiembre

| Semana | Qué entra | Por qué en ese orden |
|---|---|---|
| 31 ago | Nada nuevo. **Verificar C15 con los ojos** | Es el primer Short con el motor nuevo. Regla 11.1 |
| 7 sep | **C19 + C16** — el primer segundo deja de ser una tarjeta de texto | El deslizamiento ocurre antes de que la voz llegue a nada. Primero lo que se ve |
| 14 sep | **C7 escalón 1** — dos voces | La voz importa para quien se queda, no para quien desliza |
| **27 sep** | **Punto de control** | ¿Algún Short por encima de 100 visualizaciones en 48 h? |

Los tres desenlaces del 27 están escritos en `PLAN_DE_CAMBIOS.md` (versión 4) y en
el prompt de métricas, para que se decidan con la tabla delante y no por
agotamiento.

## 8. Ficheros tocados hoy

- `00_estrategia/PLAN_DE_CAMBIOS.md` — versión 4 al final (C14 bis, C17, C18, C19,
  C20, punto de control) y un aviso al principio que remite a ella
- `00_estrategia/PROMPT_DE_ARRANQUE.md` — estado a 31/08, trampas 5 y 6, bloque
  copiable con `ESTADO.md` en la lista de lectura
- `00_estrategia/LEEME.md` — mapa al día
- `00_estrategia/tareas/` — **nuevo**: `LEEME.md` y los tres prompts espejados
- `05_calendario/bitacora/2026-08-31-direccion.md` — este fichero

Y los prompts de las tres tareas programadas, reescritos en el almacén.

Nada de `05_calendario/guiones/`, `parrilla.json`, `03_produccion/` ni
`04_agentes/`: no son míos. Lo que hay que cambiar ahí va como encargo en el prompt
de la revisión diaria, que corre hoy a las 11:28.
