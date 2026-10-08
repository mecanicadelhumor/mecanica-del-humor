# Por qué `MDS-016` hizo 1.203 visualizaciones · análisis y hipótesis

**Dirección en diferido, jueves 08/10/2026.** Encargo: punto 1 del cuaderno del codirector (06/10).
*«Si fue azar, quiero saberlo; si no, desgranar el vídeo en todas sus variables y sacar hipótesis
que se prueben en las iteraciones siguientes, con prioridad si alguna es especialmente fuerte.»*

Datos: `05_calendario/metricas.json` (lecturas del 21/09 al 06/10), `metricas_diarias.json`,
`demanda.json`, los 30 guiones de `05_calendario/guiones/` y `registro_publicaciones.json`. Todo lo
que sigue sale de ahí; lo que no se puede saber se dice.

## 1 · Qué dicen los números (y qué no)

| | `MDS-016` | El resto de los Shorts |
|---|---|---|
| Visualizaciones (total / a 48 h) | **1.203 / 1.115** | mediana 22; el siguiente, `MDS-022`, 267 |
| De dónde vinieron | **97,8 % feed de Shorts** | 82-98 % feed en los que pasan de 60 |
| «Se quedaron viendo» (`se_quedaron_total`) | **12,1 %** (146 de 1.203) | 15,6-37,8 % en los que pasan de 100; entre los que pasan de 60, solo `MDS-025` (4,5 %) queda por debajo |
| Retención | a 4 s: 1,12 · **a 8 s: 0,60** · a 12 s: 0,41 · a 20 s: 0,28; a 30 s: 17,8 % | `MDS-022`: 1,26 · 0,98 · 0,85 · 0,83; `MDS-021`: 1,41 · 0,95 · 0,78 · 0,68 |
| % visto medio | 30,3 % | 28-79 % |
| «Me gusta» por 100 | 1,16 | 0,0-1,37 entre los que pasan de 60 |
| Suscriptores / comentarios / compartidos | 0 / 0 / 0 | igual |
| Después de la primera semana | **1.203 desde el 21/09** (ni una vista nueva) | — |

Tres cosas que se desprenden y que no estaban dichas en el repositorio (donde el 25/09 aún
constaba «sin explicación»):

1. **No es la retención.** `MDS-016` tiene la **peor curva de los ocho Shorts que pasan de 60
   vistas**: pierde el 40 % de los que empiezan entre el segundo 4 y el 8, que es justo donde
   está el chiste. El feed no lo empujó porque se viera entero. Quien empuja a un vídeo con esa
   curva está mirando otra señal, o está repartiendo a ciegas.
2. **Es un estallido, no una cola.** 1.115 vistas en 48 h y ni una más en las tres semanas
   siguientes. No hubo búsqueda (1,1 %), ni suscriptores (0,3 %), ni boca a boca (0 compartidos).
3. **Es un valor extremo de verdad.** Los otros 29 Shorts, en escala logarítmica, tienen mediana
   22 y desviación 0,52 (en potencias de diez). `MDS-016` está a **3,2 desviaciones** por encima.
   Con una distribución normal en logaritmos eso ocurriría una vez entre mil; con las colas pesadas
   que tiene el reparto del feed, una vez entre treinta o cuarenta es plausible. **No se puede
   descartar el azar, y no se puede afirmar.**

## 2 · Todas las variables del vídeo, una por una

Veredicto: **DESCARTADA** = lo que tuvo `MDS-016` lo tienen vídeos que no despegaron;
**NO DISTINGUE** = no aparta a `MDS-016` de los demás; **ABIERTA** = podría ser y se puede probar.

| Variable | `MDS-016` | Comparación | Veredicto |
|---|---|---|---|
| **Miniatura** | La que elige YouTube (fotograma casi vacío, 90-95 % azul marino; `MERCADO_2026-10.md`) | En el feed de Shorts no se ve la miniatura; 97,8 % vino de ahí | **DESCARTADA** |
| **Hora y día** | Lunes 14/09, 17:00 UTC | Todos los Shorts salen a las 17:00 UTC | **NO DISTINGUE** |
| **Voz** | La última toma con `edge-tts` (Gemini entra con `MDS-017`) | Los quince anteriores, también `edge`, mediana 16 | **DESCARTADA** como causa; ojo, ver §3 |
| **Música** | `cama_01` | La usan otros 8 Shorts (de 4 a 141 vistas) | **DESCARTADA** |
| **Serie** | «Esto no tiene gracia y esto sí» | La misma serie: `MDS-003` 16, `008` 28, `012` 16, `022` **267**, `024` 4, `029` 22 | **NO DISTINGUE** |
| **Duración** | 59 s (el guion apuntaba a 48,9; la diferencia no está explicada en los ficheros) | Entre 35 y 61 s los demás | **NO DISTINGUE** |
| **Escenas / palabras** | 6 escenas, 106 palabras | 4-6 escenas, 72-120 palabras | **NO DISTINGUE** |
| **Gancho: anécdota en primera persona** («Le dije a mi madre, con retintín…») | Sí, 13 palabras | 20 de los 30 guiones abren así (recuento por palabras clave); 12 de ellos no pasan de 30 vistas | **NO DISTINGUE** |
| **Frase citada en pantalla** («Qué *ilusión*.») | Escena 1: tres palabras entre comillas | Otros ocho guiones abren con una frase entre comillas: `004` 26, `013` 7, `022` **267**, `026` 69, `028` 8, `031`, `034`… | **NO DISTINGUE** (la comparte, eso sí, con `MDS-022`, el segundo mejor) |
| **Mecanismo del chiste: «tomarlo al pie de la letra»** y releer la misma frase | La ironía dicha → se ríe; **la misma frase escrita → «somos doce»**. El chiste es una escena doméstica que escala sola | `MDS-022` (267, el segundo mejor) es el mismo mecanismo: «vístete para el puesto» → pijama → «ahora vuelve a leerlo, mismo jefe, mismo pijama». Sus propias notas dicen que *«pasa la prueba del WhatsApp: se cuenta solo, no necesita la explicación de detrás y no tiene víctima»*. `MDS-030` (156, el tercero) también pone el chiste primero y autocontenido | **ABIERTA**, y es lo único que comparten los dos primeros (H-016-literalismo) |
| **Estructura «mismo estímulo, dos versiones»** | Sí | `MDS-003` (misma caída, dos finales) 16, `005` (mismo chiste, mal y bien) 12, `012` (mismo chiste dos veces) 16, `018` 115 | **NO DISTINGUE** por sí sola: la tienen cuatro Shorts que no despegaron |
| **Remate** | Hipérbole absurda y concreta: «ahora somos doce y ha invitado a los vecinos», con pausa de 1,35 s antes | Otros remates son explicaciones, no exageraciones | **ABIERTA** (H-016-remate) |
| **Cierre honesto** | «Si hace falta el emoji, ya no era ironía: era un aviso» | Todos los Shorts tienen cierre honesto | **NO DISTINGUE** |
| **Título** | «Por qué la ironía no se entiende por WhatsApp» (45 caracteres, sin interrogación, sin dos puntos) | Los otros «Por qué…» sin interrogación: `015` 39, `017` 15, `022` 267. Es de los más cortos (`MERCADO`: «el de `MDS-016` es también el más corto»). En el feed el título solo se superpone al vídeo | **ABIERTA**, floja |
| **Demanda de búsqueda** | La pregunta tenía mediana 5.634 en los diez primeros resultados (`demanda.json`): de las más bajas de las que hemos hecho | La demanda y las vistas correlacionan 0,17 entre los 12 Shorts de los que hay dato | **DESCARTADA**: no es que se buscara mucho |
| **Tema** | Un malentendido en **mensajes de texto** (WhatsApp, el móvil del espectador), una experiencia que todos han tenido esta semana | De los 30 Shorts, ninguno trata de los mensajes o el móvil del espectador; el resto es ciencia del chiste, la risa, los cómicos o la IA. Con `MDS-022` (malentendido con el jefe) forma la pareja de «comunicación cotidiana mal entendida» | **ABIERTA**, y la más fuerte (H-016-tema) |
| **Fuente (I05, Attardo)** | Una ficha de prosodia de la ironía, citada pero no explicada | — | **NO DISTINGUE**: el espectador no la ve |
| **Descripción, etiquetas, primer comentario** | Cuidadas | Igual que los demás | **NO DISTINGUE** (y en el feed casi no pesan) |

## 3 · Lo que no se puede separar

- **El canal cambió justo después.** Mediana de visualizaciones de los quince Shorts anteriores
  (`MDS-001` a `015`): **16**. De los catorce siguientes (`MDS-017` a `030`): **68**. Pudo ser que el
  feed *aprendió* a qué público mandarnos con el estallido de `MDS-016`; pudo ser la voz de Gemini
  (desde `MDS-017`), el vídeo de archivo (C50, desde el 23/09), el cierre más claro o simple deriva
  del feed (la mediana semanal ha ido 113 → 66 → 62 sin que cambiáramos nada). **Cuatro cambios a la
  vez: no se puede atribuir** y por eso este análisis no lo usa como prueba de nada.
- **Una sola observación.** `MDS-016` es un caso; cualquier explicación basada solo en él es una
  historia que se ajusta a los datos, no una conclusión. Lo que sí se puede hacer con un caso es
  **descartar** lo que no lo distingue (la columna de arriba) y **apostar** por lo que queda, pero
  apostando donde mirar y midiendo, no dando nada por bueno.
- **La curva sugiere que el feed no premió la retención de ese vídeo, sino otra cosa.** Qué cosa,
  los ficheros no lo dicen. Las candidatas razonables son una prueba inicial a un público
  especialmente receptivo (gente de mensajería/ironía) o el propio azar del reparto. Para eso no hay
  dato; hay que fabricarlo.

## 4 · Las hipótesis, ordenadas

Cada una cambia **una** cosa respecto al control vigente y dice cómo se confirma o se descarta.
Pasan a `05_calendario/bucle/hipotesis.json`.

| # | Hipótesis | Qué se haría | Se confirma si… | Se descarta si… |
|---|---|---|---|---|
| **H-016-tema** | El tema —un malentendido en los mensajes del móvil, algo que el espectador vive— llega a más gente que la ciencia del chiste, **aunque retenga igual o peor** | Desde la semana del 12/10, **2 de los 7 Shorts** de cada semana son de la familia `mensajes` (ver §5). Ortogonal a los brazos del ciclo B1 | Entre los Shorts de esa familia, mediana de visualizaciones a 48 h ≥ 3 veces la del resto del ciclo y al menos 2 por encima de 300 | Seis Shorts de la familia y ninguno pasa de 150 |
| **H-016-remate** | Un remate que **exagera hasta el absurdo y con un número concreto** («somos doce») engancha más que uno que explica | Ya está en la cola como `H-remate`; se le añade esta forma de remate como variante, y entra en un ciclo con tres brazos (B3) | «Me gusta» por 100 y «se quedaron» suben ≥ 8 puntos contra el control | Sin efecto en 10 Shorts |
| **H-016-literalismo** | El chiste que gusta es **un dicho tomado al pie de la letra que escala solo y se cuenta en cinco segundos sin explicación** (el de `MDS-016` y el de `MDS-022`), no el tema ni la ficha | Variante del control: el chiste de la escena 1-3 es un literalismo doméstico de ese tipo, frente a otro tipo de chiste, en el mismo tema. Se anota en cada guion `"chiste": "literalismo"` u otro, para cortar por ahí | Mediana de vistas a 48 h de los `literalismo` ≥ 3 veces la de los demás con 4 o más de cada | 6 de cada y sin diferencia |
| **H-016-azar** | Fue un valor extremo del reparto, sin causa en el vídeo | No se «prueba»: se vigila. Si en los próximos 30 Shorts (unas 4 semanas) alguno vuelve a pasar de 500 sin ser de la familia `mensajes`, el azar explica mejor que el tema | Otro Short fuera de la familia pasa de 500 | Los tres que pasen de 500 son de la familia `mensajes` |
| **H-016-misma-frase** | La estructura «mismo estímulo, dos versiones» es lo que funciona | Baja prioridad: cuatro Shorts la tienen y no despegaron | — | Ya prácticamente descartada |

Las hipótesis sobre miniatura, hora, voz, música, duración y el gancho de anécdota **quedan
descartadas** por la comparación (§2) y no entran en la cola.

## 5 · Qué se decide hoy, y qué no

**No se adelanta nada del ciclo B1.** La regla del bucle es no cambiar los brazos con el ciclo en
marcha (empieza el lunes 12) y la evidencia de `MDS-016` no es «especialmente fuerte»: es un caso
solo, con la peor retención del canal y con un tercio de probabilidad de ser azar en una cola larga.
Lo que el cuaderno pide para una hipótesis fuerte —adelantarla— no se cumple.

**Sí se hace hoy lo que no cuesta nada ni rompe el ciclo: H-016-tema como exploración de tema.** El
tema no es un brazo del bucle; lo elige la planificación. Los brazos (control, A, B) se reparten
con el `orden` barajado *después* de elegir los temas, así que dos de siete temas de la familia
`mensajes` caen en cualquier brazo y no sesgan la comparación (y si cayeran todos en uno, se ve en
la tabla y se anota). Queda escrito en las instrucciones de la planificación (paso 2), que corre
**esta noche**:

- **Familia `mensajes`** = un Short cuya pregunta es un malentendido o un comportamiento en la
  comunicación **por texto o por móvil** (ironía y emojis, el «vale», el visto, los audios, los
  grupos). Hay que tener **ficha de bibliografía real**: hoy solo existe `I05` (la ironía,
  libre desde el 26/10 por la regla de seis semanas). **La planificación busca ahora fichas
  nuevas** de ese terreno (con el entorno de red abierto), con la regla de siempre: título y DOI
  vistos juntos.
- En cada guion, dos campos en la raíz, para poder cortar después: `"familia_tema"`
  (`"mensajes"` o `"ciencia_del_chiste"`) y `"chiste"` (`"literalismo"` si el chiste de las primeras
  escenas es un dicho tomado al pie de la letra que escala solo, como el de `MDS-016` y `MDS-022`;
  `"otro"` en cualquier otro caso). Son etiquetas, no brazos: no cambian lo que se escribe. Mientras no haya fichas buenas, **no se inventa el Short**:
  se escribe en la bitácora que falta fuente y se hace la semana sin la familia.
- Lo lee el marcador: cuando haya datos, `bucle.py` no hace falta tocarlo; la dirección corta la tabla
  a mano desde `metricas_diarias.json` en la revisión de los lunes.

**Qué no se hace:** resubir `MDS-016` (regla 11.9) ni hacer «el 016 otra vez»: `MDS-027` ya fue la
continuación declarada del 016 y sacó 73. Una continuación del *tema*, sí; del *vídeo*, no.
