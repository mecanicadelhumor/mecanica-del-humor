# Dirección — viernes 18 de septiembre de 2026

Sesión de viernes (revisar lo que la planificación escribió el jueves). Se convirtió en otra
cosa a los diez minutos: el codirector traía el mismo aviso dos días seguidos y, al ir a
medirlo, resultó estar medido en los veinticinco guiones del repositorio.

Detalle completo en la **versión 10** de `00_estrategia/PLAN_DE_CAMBIOS.md`, que es la que
manda.

## El punto de partida

`ESTADO.md` decía OK y lo estaba. La revisión diaria de esta mañana había hecho su trabajo y
además me dejó puesto el dato que decidía una de las preguntas abiertas de la versión 9: los
tres últimos Shorts salieron con **0 de 18 escenas en dirección mínima**, o sea que la dirección
de actor v2 de C33.2 no se está rechazando y se queda como está. Sin esa tabla habría gastado
media sesión en replantear C33.

Los números, que llevaban dos meses sin moverse, se han movido: `MDS-016` **1.280**, `MDS-019`
**182**, `MDS-018` por encima de 100. Mediana de los quince anteriores: 10. Suscriptores: cero.

## Lo que se ha medido, que es de donde sale todo lo demás

El codirector, 16/09: *«me sigue costando entender el hilo del short […] que el inicio, nudo y
desenlace estén mucho mejor hilvanados»*. 17/09: *«me sigue pareciendo un poco forzado el guion
entre el nudo y el desenlace»*. Los dos vídeos son de los cuatro que se reescribieron el 15/09
contra las tres pruebas de cosido. **Las pruebas se cumplieron y el problema sigue** — que es la
señal de que medían otra cosa.

Dos medidas, las dos sobre el repositorio entero:

1. **Los veinticinco Shorts tienen entre 88 y 120 palabras, media 108**, diga lo que diga la
   duración declarada de su serie (30, 35, 40 o 45 s). El exceso va del 8 % al 98 %, y es mayor
   cuanto más corta dice ser la serie. Lo constante no es la serie: son las 108 palabras, que es
   lo que cabe justo por debajo del techo del formato. **El techo se usaba como objetivo.**
2. **El remate cae en el segundo 6, 7 o 9** —se detecta solo: es la escena detrás de la pausa de
   1,2-1,5 s— y **la mitad de la audiencia se va en el segundo 13**. `MDS-016`, el único vídeo
   del canal por encima de mil, es el único que pone el remate en el 13.

De ahí sale C38, y de ahí sale que lo que el codirector llamaba «forzado entre el nudo y el
desenlace» es literalmente relleno para llegar al techo.

## Lo que se ha escrito

| Fichero | Qué |
|---|---|
| `04_agentes/validar_guion.py` | C38: duración contra la serie (ERROR, ±12 %), posición del remate (ERROR, ≥ s.10), reglas de `risa`. `PPM` 150 → **130**, medido. Racha de tipos a 3 en Shorts. Exención de `MDS-017` |
| `04_agentes/prompts/guionista_corto.md` | Prueba 4 (el reloj), la risa escrita, la tabla de duraciones por serie, lista final de 6 → 8 puntos |
| `04_agentes/esquema_guion.json` | Campo `risa` |
| `03_produccion/pipeline/voz.py` | C38.1: `NOTA_RISA`, y la firma de caché **solo** cambia si `risa` está encendida |
| `00_estrategia/REGLAS.md` | Regla **13.2** (el Short también mide distancias) y 13.1 ampliada |
| `00_estrategia/PLAN_DE_CAMBIOS.md` | **Versión 10**: C38, C38.1, C39, C40, C41 |
| `00_estrategia/LEEME.md` | Estado a 18/09 y **corregida** la frase de la búsqueda |
| `00_estrategia/PROMPT_DE_ARRANQUE.md` | Cuándo me escribe el codirector; trampas **31 a 34**; estado a 18/09; dos autorizaciones nuevas |
| `00_estrategia/tareas/planificacion-jueves.md` | Regla 13.2 y duración de serie en el criterio editorial; **apartado 7: el corpus** |
| `00_estrategia/tareas/revision-diaria.md` | La bibliografía tiene dos ficheros, y el DOI se abre con `WebFetch` |
| `04_agentes/validar_bibliografia.py` | **Nuevo.** El `.md` contra `semillas.json`, sin red |
| `01_bibliografia/data/semillas.json` | Sincronizadas `C05`, `F04`, `F05` y `G03`. `E02` NO |
| `05_calendario/guiones/MDS-021..025.es.json` | Los cinco, reescritos |
| `00_estrategia/tareas/tareas_codirector_2026-09-18.md` | Seis tareas |

## Los cinco Shorts, y la restricción que me puse

**No entra ni una afirmación nueva.** Todo lo que dicen estaba en la versión de la planificación
del jueves 17, ya verificada contra el resumen de cada artículo. Esta reescritura solo quita y
recoloca. Es la única forma de tocar cinco guiones en una tarde sin reabrir la verificación de
la regla 2.

| | Antes | Ahora | Remate |
|---|---|---|---|
| `MDS-021` | 57 s · 109 pal. | 46 s · 85 pal. | s.9 → **s.12** |
| `MDS-022` | 58 s · 112 pal. | 43 s · 79 pal. | s.6 → **s.11** |
| `MDS-023` | 58 s · 111 pal. | 39 s · 68 pal. | s.9 → **s.11** |
| `MDS-024` | 55 s · 106 pal. | 45 s · 81 pal. | s.9 → **s.12** |
| `MDS-025` | 58 s · 111 pal. | 47 s · 89 pal. | s.10 → **s.19** |

**Comprobado, no supuesto:**

- `validar_guion.py` sobre los cinco: **sin errores y sin avisos**.
- **La barrera de C21, escena por escena**: `cargar()` + `pintar(t)` en el estado asentado +
  `comprobarDesbordes()` sobre las **29 escenas**. Cero problemas.
- **`muestrear_geometria.py`** (la herramienta que escribió la revisión diaria esta mañana) sobre
  los cinco: peor hueco personaje/texto del lote **215 px**, contra un umbral de 50.
- Las dos últimas llevan **el mismo aviso que puso la revisión esta mañana**: sin las tipografías
  de marca instaladas los píxeles no son definitivos. Las revisiones de mañana y del domingo las
  vuelven a pasar, y `MDS-021` no se produce hasta el lunes a las 01:13 UTC. El circuito llega.
- Sobre el repositorio entero, los únicos guiones que fallan C38 están **todos publicados**.
  Ninguno pendiente, salvo `MDS-017`, que va exento.

## Dos cosas que se cometieron y se corrigieron en la propia sesión

Las dejo escritas porque el valor está en que se cazaran, no en que no pasaran.

**1. La trampa 24, literal.** La primera versión de C38.1 metía `risa=0` en la firma de la caché
de voz de **todas** las escenas. Eso cambia la clave de las 49 tomas de `cache_voz/`, entre ellas
**las 18 escenas de `MDH-007` que tienen que llegar al domingo**. Habría dejado el episodio largo
sin voz y sin un solo error en el log. La firma solo cambia cuando `risa` está encendida, y está
comprobado ejecutando la función real contra la caché real: **18 de 41, las mismas que esta
mañana.**

**2. La trampa 9, atendida antes de que pasara.** Las dos comprobaciones de C38 son ERROR y
`producir.yml` para la producción con un error (paso «Validar guiones», línea 190). De los
veinticuatro Shorts que las incumplen, uno estaba pendiente: `MDS-017`, mañana. La exención vive
en `validar_guion.py` y no en el guion, para que conceder otra obligue a tocar código.

## Y una que no venía a cuento y era la más peligrosa del día

Al ir a comprobar que `C05` y `G03` estaban arregladas —lo pedía el codirector, y la revisión
diaria ya lo había hecho— apareció que `BIBLIOGRAFIA_CURADA.md` **es un fichero generado** desde
`01_bibliografia/data/semillas.json`. Lo dice su propia cabecera, en la línea cuatro. Nadie lo
había respetado nunca.

**Cinco fichas estaban corregidas solo en el `.md`**: `C05`, `E02`, `F04`, `F05` y `G03` — dos de
ellas arregladas esa misma mañana y tres por el codirector. La próxima regeneración las borraba
las cinco, sin error y sin aviso, y la única señal habría sido una ficha mal tres semanas
después.

`04_agentes/validar_bibliografia.py` lo comprueba desde hoy. Sabe de la entrada de control `A09`
(que está en el JSON y no en el `.md` **a propósito**) y normaliza comillas tipográficas, porque
sin eso señalaba `E06` por un par de comillas curvas y una comprobación que señala ruido se deja
de leer. **Sincronizadas las cuatro verificadas; `E02` no**, porque tiene dos DOI y ninguno
comprobado: elegir a ojo es inventarse un dato.

**Y `F04`, ya corregida, resulta ser un artículo sobre entrenamiento de memoria de trabajo.** No
está rota: está bien identificada y fuera del tema. El pilar F sigue bloqueado, y con él «qué le
pasa a tu cerebro cuando te ríes» — 91 millones en el top 10, cero de cinco respondiendo.

## Las tres preguntas del codirector, contestadas

- **TikTok y Reels (C41).** Reabierto. Las dos APIs exigen auditoría o revisión de la app para
  publicar en abierto (TikTok deja los posts en privado hasta entonces; Meta tarda de dos a
  cuatro semanas). Coste cero, intervención puntual de setup, regla 8 lo autoriza expresamente.
  **Se empieza el trámite ya y no se publica hasta que C38 haya dado su primera medida**, porque
  la cola corre sola mientras arreglamos el guion. Y el premio de verdad no es la exposición:
  el mismo vídeo en dos feeds distintos **separa «el contenido no funciona» de «no nos están
  enseñando»**, que hoy no sabemos distinguir y que piden decisiones opuestas el 15 de noviembre.
- **Marketing gratuito (C40).** Medido sobre los quince Shorts con datos de tráfico, ponderado
  por visualizaciones: feed **54,6 %**, búsqueda **27,7 %**, suscriptores 6,9 %, **todo lo
  externo junto 5,4 %** — catorce visualizaciones en dos meses. Para un canal de Shorts sin
  audiencia el marketing externo no es una palanca pequeña: es ruido. **C38 es la campaña.** De
  paso, la frase de `LEEME.md` «la única superficie que responde es la búsqueda» era de agosto y
  dejó de ser cierta en `MDS-007`: queda corregida.
- **El corpus (C39).** No se crea un agente bibliotecario: se le encarga a la planificación del
  jueves, que ya lee la bibliografía y mide la demanda a la vez, y que no necesita un workflow
  nuevo del codirector. Disparador numérico —**menos de quince fichas sin usar, añade tres**—,
  orden por hueco y no por volumen, pilares bloqueados primero, y la regla que impide otro
  `F04`: *si el DOI y el título no se han visto juntos en la misma página, la ficha no se
  escribe.*

## Lo que no se ha hecho hoy, y por qué

- **C34 (imagen, duotono ámbar)** estaba señalado para hoy. **Al lunes 21**: sigue bloqueado por
  los enlaces de origen de las fotos, pedidos el 15/09 y sin contestar, y sin ellos `banco.json`
  no cumple la regla 9. No se ha caído.
- **C36 (una llamada por vídeo)** estaba para probarse hoy. **Al lunes 21**: no tiene diseño
  escrito y la urgencia bajó cuando la revisión enseñó que la dirección v2 no se rechaza (0 de
  18). Con la cuota estable, una llamada por escena aguanta.

## Lo que hay que mirar mañana

**La caché de voz de `MDH-007` lleva dos días en 18 de 41** y hoy no hay commit de precacheo,
aunque `voz_adelantada.yml` tiene cron a las 09:00 UTC. Con 23 escenas por sintetizar y el tope
de 10 peticiones por modelo y producción, el domingo sale —unas 20 en la pasada de las 01:13 y
el resto en la de las 08:23— **pero sin margen para rechazos**. Si mañana sigue en 18, mover el
episodio antes de que falle solo es mejor que descubrirlo el domingo a las 12:00.
