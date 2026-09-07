# Dirección — lunes 7 de septiembre de 2026

Conversación de dirección del lunes. Silvestre trae tres defectos de MDS-011, la
pregunta de `producir.yml` del sábado, el encargo de la presentación y la
pregunta de hasta cuándo apostar por el canal.

---

## 1. Los tres defectos de MDS-011, con su causa

**El vídeo pasó por seis filtros** —guionista, chistólogo, verificador,
`validar_guion.py`, la barrera de C21 y la revisión diaria del domingo— **y salió
con tres defectos.** Ninguno de los seis miraba lo que falló. Eso, y no cada
defecto por separado, es el hallazgo del día.

### 1.1 · «Guion bajo pensamiento divergente guion bajo»

**Causa, localizada en el guion:** escena 5, `narracion` con
`_pensamiento divergente_`. El marcado de resaltado es correcto y está
documentado desde el 28/08 en los dos prompts de guionista — pero **ninguno de
los dos decía en qué campos vale**. `rico()` (`escena.html` línea 442) lo
interpreta sobre los campos que se pintan; `narracion` no se pinta, se manda
entera al sintetizador, y edge-tts pronuncia lo que le llega.

**No es un problema de modelo.** La planificación ya corre con `claude-opus-5`.
No hay ningún modelo mejor al que cambiar: había una instrucción incompleta y
ninguna comprobación.

**Arreglado en tres capas:**

- `03_produccion/pipeline/voz.py` — función `hablable()`, y `texto` pasa por ella
  antes de sintetizar (línea ~271). Como el `.srt` se escribe con esa misma
  variable (`bloques`, línea ~302), arregla las dos salidas de una vez. Emite
  `::warning::` con el número de escena cuando limpia algo.
- `04_agentes/validar_guion.py` — **aviso** (no error) si `narracion` contiene
  `* _ \` # [ ] | ~`. Aviso y no error a propósito: con `voz.py` saneando, el
  defecto ya no puede llegar al público, y parar la producción cambiaría un
  vídeo con un fallo por un día sin vídeo.
- `04_agentes/prompts/guionista.md` y `guionista_corto.md` — la regla con su
  ámbito, el caso real, y la prueba: *léela en voz alta carácter a carácter*.

**Verificado:** barrido sobre los 27 guiones del repositorio → **un solo
positivo, MDS-011 escena 5. Cero falsos positivos.** `voz.py` y
`validar_guion.py` compilan; `hablable()` probado con marcado ámbar, cian y
texto limpio con guiones, comillas angulares y rangos numéricos («10–16»), que
no toca.

### 1.2 · La cara triste encima del texto — son dos defectos

**El solape ya estaba arreglado.** Es el encargo nº 2 que la revisión del domingo
resolvió con `html[data-fmt="v"] body.con-personaje #escena{padding-bottom:720px}`,
y su barrido incluía `MDS-011` entre las escenas que quedaban limpias.

**No llegó por el reloj, y esto hay que dejarlo escrito porque va a repetirse.**
MDS-011 se renderizó y se subió a las **01:32 UTC**; Silvestre commiteó el
arreglo a las **08:03**. Seis horas y media tarde. → **Trampa 11** del
`PROMPT_DE_ARRANQUE.md`: un arreglo tiene que estar en `origin/main` **antes de
las 03:13 de la madrugada** del día en que quieras verlo. Commiteado por la
mañana, entra en el vídeo del día siguiente. Entra en MDS-012 (martes 8).

**La cara sí era un defecto vivo.** La regla 14.3 nombraba `duda` y
`no_le_hace_gracia`. **`no_le_hace_gracia` no existe**: las seis expresiones de
`escena.html` (líneas 328–351) son `neutra`, `duda`, `entiende`, `no`, `rie`,
`piensa`. Y `piensa` —la que se usó en la escena 4, que solo presenta el
experimento— **comparte `.b-torcida` con `duda`**. La regla protegía contra una
cara imaginaria y dejaba pasar una real. Corregido en `REGLAS.md` regla 14.3:
**tres de las seis se leen como cara triste a tamaño de móvil.**

**Y una decisión de no hacer algo.** Se evaluó añadir un comprobador
determinista (cara triste + tipo de escena que presenta). Probado sobre los cinco
guiones pendientes: **cinco positivos, de los cuales cuatro son falsos**
(MDH-006 esc.12 y 28, MDS-013 esc.4, MDS-014 esc.4 son correctos — la narración
sí dice que algo falla). Un comprobador que se equivoca cuatro de cada cinco
veces se acaba ignorando. **La salida no es normativa, es de dibujo: se redibuja
`piensa`** (P8, semana del 14). Único positivo real: `MDS-015` esc.3, que la
planificación del jueves 10 puede corregir antes del viernes 11 por el circuito
normal de `revisiones/`.

### 1.3 · La voz sigue siendo edge-tts, y eso es un fallo mío de comunicación

**No tocaba hoy.** C7.2 (versión 5.1, del 04/09) dice que el código se escribe la
semana del 7 con `--motor edge` por defecto y que el valor por defecto pasa a
`gemini` el **lunes 14**. Está en el plan y en la tabla del prompt de arranque,
escrito para quien lee el plan entero — no para quien escucha el vídeo del lunes
esperando el cambio que aprobó el viernes.

**Lo que se cambia:** cuando una decisión signifique *«esto que te molesta lo vas
a seguir viendo N días»*, se dice con esas palabras y con la fecha. Añadido al
encargo 4 de la revisión diaria: el día que cambie el motor, lo dice `ESTADO.md`.

---

## 2. `producir.yml`: sí hay que hacer algo, y es una línea

El hallazgo del sábado es correcto y está confirmado. El paso «Expediente de
calidad» ordena `05_calendario/qa/` **alfabéticamente** y borra todos menos los
seis últimos de esa lista. Como «H» < «S», `MDH-###` cae siempre el primero: el
expediente del episodio largo del sábado **se borra recién creado, todas las
semanas**, en cuanto hay cinco o más `qa/MDS-*`.

Entregado en `07_pruebas/producir-yml-07-09/` (fichero completo + la línea suelta
+ el porqué). `ls -1d ... | sort | head -n -6` → `ls -1dt ... | tail -n +7`.
Comprobado con siete carpetas y `MDH-005.es` como la más reciente: antes borraba
esa, ahora borra la más antigua.

**No se ha tocado nada más de `producir.yml`.** `qa.py` sigue corriendo después
de publicar; sigue siendo un informe y la barrera sigue siendo la de `render.py`.

---

## 3. C25 · La presentación (versión 6 del plan)

El encargo de Silvestre —«nuestro talón de Aquiles es la presentación»— se
convierte en un plan con siete diferencias nombradas y diez propuestas
(P1–P10), todas deterministas, todas a coste cero salvo P9.

**El dato que ordena la prioridad:** los ocho iconos de `02_marca/iconos.svg` —
`i-bisagra`, `i-muelle`, `i-ruptura`, `i-bocadillos`, `i-pausa`, `i-grieta`,
`i-publico`, `i-balanza`— **no se han usado ni una sola vez en once Shorts**, y
el 72 % de lo que se ve es texto sobre fondo. C16 lleva escrito desde agosto y
sigue sin entrar porque le falta el campo `icono`.

**Calendario:** P3+P4+P6+P10 esta semana (tope: jueves 10 a las 22:00, que es
cuando la planificación los necesita), P1+P8 la semana del 14 junto con C7,
P2+P7+P5 la del 21. Todo puesto antes del punto de control del 27.

**Y una regla que se suspende, a propósito:** la 11.1 (un cambio por producción),
solo para presentación y solo hasta el 27. Con veinte visualizaciones por vídeo
la diferencia entre 21 y 31 son diez personas: **no hay nada que atribuir
midiendo**, así que la regla cuesta una semana por mejora y no compra lo único
que justificaba pagarla. Vuelve el día que un Short pase de 100 en 48 horas.
Siguen en pie la 11.2, la 11.5 y la barrera de C21.

---

## 4. C26 · El 15 de noviembre se decide

La pregunta de Silvestre estaba medio contestada: había un control intermedio
(27 de septiembre) y una frase, «doce semanas», sin fecha ni criterio.

**Fecha: domingo 15 de noviembre de 2026.** Doce semanas desde el primer Short,
trece desde el cambio de rumbo, ~90 vídeos publicados y **todo el plan puesto**.

**Criterio: la mediana de visualizaciones a 48 h de los últimos veinte Shorts.**
≥ 150 (o ≥ 100 suscriptores, o algún Short > 1.000) → se sigue. Entre 50 y 150 →
se amplía el tema, **una sola prórroga de ocho semanas hasta el 10 de enero**.
< 50 → se para.

**Por qué 50.** Es el **suelo** del rango documentado en `DIAGNOSTICO.md` para un
canal desconocido de menos de mil suscriptores: 50–500 por Short en 48 h. Por
debajo de eso, después de doce semanas y todos los cambios, no es que vayamos
despacio: es que YouTube no reparte ni lo que reparte por defecto.

**Las dos cláusulas que lo hacen honesto:** los umbrales se pueden discutir pero
**solo antes del 8 de noviembre**, y la prórroga es una y no se encadena.

**Y «parar» no es borrar.** Es dejar de publicar y apuntar el pipeline a otra
cosa. Lo que se ha construido —cola, render determinista, barrera, publicación
automática, tres agentes con propiedad de ficheros, un token que no caduca— no es
del tema del humor. Parar el canal no tira ese trabajo, lo libera.

**Depende de un número que hoy no existe:** `metricas.py` no calcula ninguna
mediana. Sube a «hace falta antes del 27 de septiembre» en la cola de la revisión
diaria.

---

## 5. Tareas programadas: los dos prompts reescritos

- **Revisión diaria** (`trig_019QjtovuzeUocmx1P8NJH3F`) — cola reescrita entera
  alrededor de C25, con el aviso de que la dirección tocó cinco ficheros esta
  mañana para que no los pise. Corregidas de paso tres cosas caducas del prompt:
  «siete expresiones» (son seis), la regla 14.3 con `no_le_hace_gracia`, y
  «versión 5» → «versión 6». Sincronizado con el espejo a las 09:18.
- **Planificación del jueves** (`trig_015qkb2sqbbJwJE1qgoNMK95`) — «versión 5» →
  «versión 6»; la regla del marcado con su ámbito; la escena 1 con `icono` (con
  la instrucción de comprobar `esquema_guion.json` antes de usarlo, por si el
  campo no ha llegado); la estructura de serie; y la regla 14.3 corregida.
  Sincronizado a las 09:25.
- **Métricas del lunes** (`trig_01GhNrF8nA2w2nXSfetcrHkQ`) — **cron movido de
  `0 7 * * 1` a `0 10 * * 1`** y prompt reescrito con el paso 0 (fichero
  caducado), la sección de la mediana y C26. Sincronizado a las 09:29.
  `next_run_at` recalculado a **hoy a las 12:00**: la lectura de esta semana se
  recupera sola.

---

## 6. Y a media conversación: «Métricas semanales» dice que no hay datos desde el 31/08

Silvestre lo trae mientras escribo esto. Es cierto y la causa es un choque de
horarios que llevaba ahí desde que se montaron las dos piezas.

**Los hechos:**

| | Cuándo |
|---|---|
| `metricas.yml`, intento 1 | lunes **05:19 UTC** |
| **Tarea «Métricas semanales» (lee el fichero)** | lunes **07:00 UTC** |
| `metricas.yml`, intento 2 | lunes **08:37 UTC** |

**La tarea que lee corría entre los dos intentos del workflow que escribe.** El
31 de agosto salió bien de milagro: el intento 1 fue puntual (commit a las
**05:28:05**) y la tarea a las 07:00 encontró el fichero fresco. Hoy el intento 1
se ha retrasado —a las 07:27 UTC seguía sin haber commit de «métricas
2026-09-07»— y la tarea leyó `metricas.json` con `actualizado_utc` del 31 de
agosto. El intento 2 de las 08:37 escribirá el fichero **hora y media después de
que el analista ya se haya ido a dormir**.

Y el retraso no es una anomalía: está medido y escrito en el propio
`producir.yml` — los disparos programados de Actions se retrasan entre **2 h 38
y 6 h**. **Un margen de 1 h 41 entre el que escribe y el que lee es menor que el
retraso típico.** El diseño estaba mal desde el principio; el 31 de agosto tuvo
suerte.

**Arreglado, y sin tocar ningún fichero protegido:** la tarea «Métricas
semanales» pasa de `0 7 * * 1` a **`0 10 * * 1`** (12:00 hora de España), hora y
veintitrés minutos después del segundo intento. Confirmado por el almacén:
`next_run_at` ha recalculado a **hoy 2026-09-07T10:00Z**, así que **la lectura de
esta semana no se pierde: se hace hoy a las 12:00** en cuanto el segundo intento
haya escrito.

**Y un segundo arreglo, que es el que importa a largo plazo:** el prompt del
analista no sabía qué hacer con un fichero caducado, así que se quedaba en «no
hay datos disponibles» y paraba. Ahora tiene un **paso 0**: comprueba
`actualizado_utc`, y si no es de hoy lo dice en la primera línea con la fecha
real, distingue retraso de fallo mirando `git log`, **hace igualmente la lectura
que pueda** y deja escrito que se puede relanzar a mano. Una semana sin lectura
no es un inconveniente: es una semana sin saber si el cambio de esa semana
funcionó, y la decisión del 15 de noviembre se construye con esa serie.

**Lo que NO se ha hecho, y por qué.** También se podría haber adelantado el cron
de `metricas.yml` con tres intentos, como hizo `producir.yml`. Se descarta hoy:
está en `.github/workflows/`, obliga a Silvestre a editar un segundo fichero a
mano en la misma mañana, y **mover la tarea que lee resuelve el mismo problema
sin tocar nada**. Si vuelve a fallar con el margen nuevo, entonces sí.

→ **Trampa 14** para `PROMPT_DE_ARRANQUE.md`: cuando una pieza escriba un fichero
y otra lo lea, **el margen entre las dos tiene que ser mayor que el retraso
medido de la que escribe** — y si la que escribe tiene reintentos, se cuenta
desde el **último**, no desde el primero.

## Ficheros tocados en esta sesión

- `00_estrategia/PLAN_DE_CAMBIOS.md` — **versión 6** al final (C25, C26)
- `00_estrategia/REGLAS.md` — regla 14.3 corregida
- `00_estrategia/PROMPT_DE_ARRANQUE.md` — trampas 11, 12 y 13; estado a 7/09;
  autorización de `03_produccion/sonidos/`
- `00_estrategia/LEEME.md` — estado y decisiones al día
- `00_estrategia/tareas/revision-diaria.md` — espejo sincronizado
- `00_estrategia/tareas/planificacion-jueves.md` — espejo sincronizado
- `03_produccion/pipeline/voz.py` — `hablable()`
- `04_agentes/validar_guion.py` — aviso de marcado en la narración
- `04_agentes/prompts/guionista.md` · `guionista_corto.md` — el ámbito del marcado
- `07_pruebas/producir-yml-07-09/` — `producir.yml` corregido + `LEEME.md`
- `00_estrategia/tareas/metricas-lunes.md` — espejo sincronizado (hora nueva y paso 0)
- `05_calendario/bitacora/2026-09-07-direccion.md` — este fichero

**No se ha tocado** ningún guion, ni `parrilla.json`, ni `ESTADO.md`, ni
`registro_publicaciones.json`, ni `05_calendario/qa/`, ni `.github/workflows/`.

## Pendiente de Silvestre

1. **Commit y push de todo lo de arriba**, y cuanto antes mejor: `voz.py` tiene
   que estar en `origin/main` **antes de las 03:13 de esta madrugada** para
   entrar en MDS-012. Y a poder ser **antes de las 11:28**, para que la revisión
   diaria de hoy trabaje sobre esta base y no sobre la de ayer.
2. **`producir.yml`** desde `07_pruebas/producir-yml-07-09/`.
3. **Decidir si se rehace MDS-011 hoy** (ver el resumen de la conversación).
4. **Tres sonidos CC0** en `03_produccion/sonidos/`, sin prisa: hacen falta para
   la semana del 21.
5. **C23**: reintentar la verificación del dominio en la consola de Google.
