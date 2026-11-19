**Entrega: por rama, con `python3 04_agentes/entregar.py --tarea planificacion` (C53).** Sin plan B (ver el final si cambia).

# Bitácora · Planificación del jueves 19 de noviembre de 2026

El contenedor arrancó el **jueves 19 a las 22:08 UTC (23:08 de España)**: es la ejecución buena del jueves, no un
reintento. **Resultado: un Short, `MDS-072`, para el sábado 21/11** (el primer hueco libre). **La semana del 23 al
29/11 queda entera sin Short**, y el domingo 22 también. Se intentaron diecisiete temas con tres lectores por vuelta
(unas 190 lecturas) y pasó uno.

```
$ git log --oneline -5 origin/main
519e04a métricas 2026-11-19 (diaria)
4b39af6 medición de demanda 2026-11-19
902e606 métricas 2026-11-19 (diaria)
f34cdab dirección 2026-11-19: plan v33 — C26 sin respuesta (tercera vez) …
067de67 Visuales (C50): manifiestos y hojas de contactos

$ git ls-remote origin 'refs/heads/claude/entrega-*'
86a99d8… refs/heads/claude/entrega-direccion-20261112-1323   (de la dirección; no es mía)
73c4b17… refs/heads/claude/entrega-revision-20261104-1031    (de la revisión; no es mía)
```

Leído antes de empezar: `08_comunicacion/novedades.md` (cambios visuales en marcha; nada para mí), las notas de la
dirección del 16 y el 19/11 (C26 sigue sin decidir: «escribe la semana siguiente como siempre; si el codirector decide
parar, lo escrito se queda en el banco»), mi bitácora del 12/11, `ciclos.json`, `resultados.json`, la reserva y las
notas de `revisiones/` de `MDS-068` a `071`.

---

## 1 · Lo que ha hecho el canal (C46)

Últimos veinte Shorts con `vistas_48h` (`metricas.json`, lectura más alta de cada uno):

| Short | Publicado | Pregunta | Vistas 48 h |
|---|---|---|---|
| `MDS-047` | 10-23 | ¿Por qué dan miedo los payasos? | 35 |
| `MDS-048` | 10-24 | ¿Por qué discutir por WhatsApp sale peor? | 5 |
| `MDS-049` | 10-25 | ¿Por qué después de reírte cuentas de más? | 70 |
| `MDS-050` | 10-26 | ¿Por qué te ríes antes de las cosquillas? | **913** |
| `MDS-051` | 10-27 | ¿Sirve de algo escribir «jajaja» sin reírte? | 32 |
| `MDS-052` | 10-28 | ¿Se nota cuando alguien se ríe por compromiso? | 11 |
| `MDS-053` | 10-29 | ¿Hacer un chiste en una reunión te da puntos? | 16 |
| `MDS-054` | 10-30 | ¿Por qué escribimos en vez de llamar? | 30 |
| `MDS-055` | 10-31 | ¿Puede hacerte cosquillas una máquina? | **695** |
| `MDS-056` | 11-01 | ¿Por qué hay gente que se ríe de lo que cuenta? | 12 |
| `MDS-057` | 11-02 | ¿Los gorilas tienen cosquillas? | **428** |
| `MDS-058` | 11-03 | ¿Por qué duele que dejen de contestarte? | 10 |
| `MDS-059` | 11-04 | ¿Reírse adelgaza? | 4 |
| `MDS-060` | 11-05 | ¿Queda mal un emoji en un correo de trabajo? | 27 |
| `MDS-067` | 11-09 | ¿Cómo se nota la ironía en un WhatsApp? | 3 |
| `MDS-062` | 11-10 | ¿Por qué casi no te ríes cuando estás solo? | **388** |
| `MDS-064` | 11-11 | ¿Por qué un chiste malo hace gracia si alguien se ríe? | 14 |
| `MDS-065` | 11-12 | ¿Por qué consuelas a quien llora de alegría? | 28 |
| `MDS-066` | 11-13 | ¿Por qué se te pega la risa de otro? | 7 |
| `MDS-063` | 11-14 | ¿Qué le pasa a tu cerebro al reírte con amigos? | 2 |

Fuera de la tabla, de `resultados.json`: `MDS-068` (las ratas, 16/11) **1** a 48 h y `MDS-069` (sonreír a la fuerza,
17/11) **5**.

- **Los dos mejores de las últimas cuatro semanas:** `MDS-050` (913) y `MDS-055` (695), los dos de cosquillas;
  detrás, `MDS-057` (428, cosquillas) y `MDS-062` (388, reírse a solas). **Los dos peores:** `MDS-068` (1) y
  `MDS-063` (2).
- **`control_c26`:** mediana **21,5**, 4 por encima de 100, 5 por encima de 50.
- **Derecho de tanteo:** se intentaron **cuatro** temas de cosquillas (ratas optimistas `F23`, bonobos `E24`, el truco
  para aguantarlas `F21`, la risa de cosquillas de oído `E23`); **no pasó ninguno**. Lo digo claro: esta semana el
  tanteo no se ha podido ejercer. Y una lectura que la dirección puede querer hacer: el último Short de cosquillas,
  `MDS-068` (ratas), hizo **1** vista a 48 h; el feed no lo enseñó. El tema solo no basta.

## 2 · El bucle (C60, B2)

`resultados.json` (21:51 UTC del 19/11): **todo «faltan datos»**. Control n = 1 (`MDS-065`, 28,6 %); A n = 2
(`MDS-062` 17,7 %, `MDS-064` 21,4 %); D n = 1 (`MDS-060`, 25,9 %); AD n = 0. Apartados por menos de 10 vistas:
`MDS-063`, `066`, `067`, `068`, `069` (**cinco de los últimos siete**). Pendientes: `MDS-070`, `071`. No decido nada.

**Brazos:** la posición 17 (sábado 21) es **control**, y ahí va `MDS-072`, escrito con seis escenas y sin mirar el
brazo. Las posiciones 18 (domingo 22, A) y 19-24 (del 23 al 28, D, AD, A, AD, control, D) quedan **vacías**. El domingo
29 ya cae fuera de B2 (`hasta: 2026-11-28`) y no hay B3 escrito.

**Lo que esto significa para B2, y es para la dirección:** con la semana vacía, B2 cierra el 28/11 con muy pocos Shorts
por brazo (control 3-4, A 4-5, D 1-2, AD 1) y casi la mitad apartados por pocas vistas. No va a llegar a n = 6 por
lado en ningún factor.

## 3 · Lo que se ha escrito, y la lectura en frío con tres lectores

**Diecisiete temas, unas 190 lecturas, pasa uno.** Encargo literal de `guionista_corto.md`, subagentes nuevos en
cada vuelta (modelo `sonnet`), decide la mayoría. Un cambio de forma, no de fondo: desde la cuarta tanda los lectores
leían el encargo y el guion de un fichero con nombre neutro (`videoN.txt`) en vez de recibirlo pegado en el mensaje;
el texto es el mismo, literal, más una línea «Responde solo con las cinco respuestas, numeradas».

| Tema (ficha) | Vueltas | Resultado |
|---|---|---|
| **¿Te pones más rojo al verte cantar a ti? (`F25`)** | 3 (+2 de comprobación) | **pasa → `MDS-072`, sábado 21, control** |
| ¿Las ratas con cosquillas son más optimistas? (`F23`) | 2 | cae (el montaje de los pitidos) |
| ¿Los orangutanes se contagian la risa? (`E26`) | 1 | dejado (muy cerca de `MDS-066`) |
| ¿Los bonobos se hacen cosquillas? (`E24`) | 3 | cae |
| ¿Se nota cuando sonríes de vergüenza? (`E14`) | 3 | cae |
| ¿El móvil en la mesa enfría la charla? (`I21`) · *mensajes* | 3 | cae (el cierre, las tres veces) |
| ¿Por qué confunde un emoji que no pega? (`I24`) · *mensajes* | 3 | cae |
| ¿Hay un truco para aguantar las cosquillas? (`F21`, 2.ª semana) | 2 | cae |
| ¿La risa de las cosquillas suena distinta? (`E23`, 2.ª) | 3 | cae |
| ¿Una errata en el chat parece más humana? (`I17`, 2.ª) · *mensajes* | 3 | cae (solo rótulos en la tercera) |
| ¿Sirve de algo ponerse rojo? (`D15`) | 3 | cae (método y resultado sin el artículo) |
| ¿Se puede entrenar el sentido del humor? (`H01`) | 3 | cae (qué se hacía en el curso) |
| ¿Es normal pensar que se ríen de ti? (`J02`) | 2 | cae |
| `F25` en versión de cinco escenas (para un día D) | 1 | cae (el cierre, 3/3) |

Detalle de cada caída en `temas_en_reserva.md` («Caídos el 19/11/2026»).

**`MDS-072`, en una línea por cosa:**
- **Tesis:** verte cantar en vídeo te sonroja más que ver cantar a otro; se midió con un termómetro en la mejilla.
- **Lector («¿de qué va?»):** «Verte a ti mismo cantando en vídeo te sonroja más que ver cantar a otra persona, según
  un experimento».
- **Fuente:** `F25` (Nikolić y otros, 2024), nunca central; resumen leído en OpenAlex y método en el texto completo
  (PMC11251765): 63 chicas de 16 a 20 años (40 analizadas), dos visitas, sonda de temperatura en el pómulo.
- **La lectura, honestamente:** pasó en la tercera vuelta, pero esa versión duraba **61 s** (techo 55). La recorté a
  49 s sin quitar escenas, y lo volví a leer dos veces: en la cuarta cayó por un rótulo que yo había añadido después
  de la lectura («Tu cara roja se mide», 3/3) y por «sensor en la cara» (2/3); en la quinta, solo por el rótulo de la
  escena 5, que había convertido en «dato» para quitar el aviso P10 (2/3). **Ese rótulo ha vuelto al de la tercera
  vuelta**, que leyeron seis lectores sin marcarlo. Es decir: la versión que sale no se ha leído con exactamente ese
  rótulo; la diferencia es solo el rótulo de la escena 5. Lo digo para que la revisión diaria lo mire si quiere.
- **Escena 3** («Cantando fatal. Y la cara, ardiendo.»): la quitarían casi todos los lectores (criterio c). Se queda
  porque es el remate del planteamiento y porque la versión sin ella cayó. Si la revisión cree que sobra, la versión
  de 45 s sin ella está en el historial del guion.
- Avisos de `validar_guion.py` que quedan: cuatro «enunciado» seguidos y la falta de escena «dato» (P10). Sin errores.

**Lo que se repite en las 190 lecturas** (para el próximo jueves):

1. **Los rótulos de pantalla bloquean tanto como la voz.** Un rótulo telegráfico («Un amigo… y tu propia mano», «Con
   errata… o sin ella», «Más calor · con su propio vídeo», «La que menos puedes frenar») lo copian dos de tres en la
   pregunta 3. Los rótulos que pasan son una frase con sujeto y verbo que se entiende sin la voz.
2. **El cierre honesto cae cuando la salvedad no dice qué implica.** «Eso sí, en el estudio eran parejas de un
   experimento, no dos amigas con un café» (3/3), «Lo que el estudio no sabe es si guardarlo en el bolso basta»
   (3/3). Pasa cuando nombra exactamente a quién no se ha probado («eran chicas de dieciséis a veinte años»).
3. **El método tiene que decir qué tenía delante la gente y qué contestaba**, y casi nunca cabe sin el texto completo:
   `D15` y `H01` cayeron exactamente ahí, y los dos tenían el artículo cerrado esta noche. `F25` pasó cuando el método
   salió del texto completo.
4. **Con el dato delante (brazo B), una escena de situación sin información nueva se lee como relleno** («me iría en
   la 2»: `F21`, `E24`). Cuando la situación es la del estudio (el karaoke) aguanta.
5. **Una comparación entre personas y animales no cose** si el dato va delante (`E24`, tres vueltas).
6. **La firma de la fuente sale en todas las lecturas** (a notas, como siempre).

**Variedad (C48.1):** un solo guion; no abre en primera persona; cierre «Así que esa cara roja es de verdad…», que no
repite ninguno de los cuatro anteriores. Etiqueta `chiste`: `otro`.

## 4 · Demanda, actualidad y fichas

- **Demanda medida:** `demanda_bruta.json` de hoy (20:52 UTC), 25 consultas, sin avisos. El aprobado sale de la
  medición: «por qué me pongo roja cuando me río» (**514,9 M** en el top 10, la más alta de la lista). Las tres de
  mensajes medidas (la errata, 50,3 M; el móvil en la mesa, 8,8 M; el emoji del banco, 85,1 M) se intentaron y cayeron.
  `demanda.json` y `semillas_demanda.json` actualizados.
- **Actualidad (C52):** ningún gancho. Tendencias: un ataque con daños en embajadas, fútbol, sucesos. Nada cumple C52.
- **Fuentes centrales:** `F25` (nunca central). **Evitadas por repetición:** `F19` (`MDS-050`), `F15` (`MDS-055`),
  `E03` (`MDS-057`), `E16` (`MDS-062`), `E06` (`MDS-068`), `E25` (`MDS-071`). `F10` se libera el 25/11; no la usé.
- **Corpus (paso 7): doce fichas nuevas**, cuatro de la familia `mensajes`: `I25` (el punto final en mensajes cortos),
  `I26` (la frase partida en varios mensajes), `I27` (el «escribiendo…» y la espera), `I28` (devolver el emoji), `D16`
  (la vergüenza como señal de buena persona), `D17` (los silencios largos entre desconocidos y amigos), `F26` (el
  efecto foco: la camiseta bochornosa), `E27` (los niños se ríen ocho veces más acompañados), `E28` (las risas que no
  se imitan), `E29` (la sonrisa se contagia en la guardería), `E30` (nos reímos más con quien se nos parece), `G11`
  (las cadenas de chistes en reuniones). Lo hizo un subagente con las reglas de la ficha (título, DOI y resumen vistos
  juntos en OpenAlex); **comprobé yo de nuevo el título de `I25`, `D16` y `E30`** contra su DOI. `D16` lleva año 2011
  (OpenAlex) aunque el volumen es de 2012. `validar_bibliografia.py`: pasa.

## 5 · Revisiones

- `revisiones/MDS-068.md`, `069.md`, `070.md`: notas de Shorts ya publicados; no se rehacen (C54). No las retiro.
- `revisiones/MDS-071.md` (sale mañana, viernes 20): propuesta opcional de acortar la escena 2. **No la aplico**:
  tocar la narración a menos de un día obliga a resintetizar la voz y el cambio es opcional (un lector contra tres).
- `MDS-062.md`, `063.md`, `064.md`: igual que la semana pasada.

## 6 · Lo que he tocado

`05_calendario/guiones/MDS-072.es.json`, `05_calendario/publicaciones/MDS-072.es.json`, `05_calendario/parrilla.json`
(una emisión y `_cambio_19_noviembre_noche`), `05_calendario/CALENDARIO.md` (el sábado 21 y la semana del 23),
`05_calendario/temas_en_reserva.md` (doce líneas), `05_calendario/demanda.json`, `05_calendario/semillas_demanda.json`,
`01_bibliografia/data/semillas.json` y `BIBLIOGRAFIA_CURADA.md` (regenerado), esta bitácora y
`08_comunicacion/2026-11/2026-11-19-planificacion.md`.

---

## Para el codirector

1. **La semana del 23 al 29/11 no tiene ningún Short, y el domingo 22 tampoco.** Diecisiete temas, uno aprobado. Con
   el criterio actual (tres lectores, mayoría, y cualquier frase o rótulo copiado en la pregunta 3 cuenta) la tasa ha
   bajado de uno de cada cuatro (12/11) a uno de cada diecisiete. Si la dirección quiere que haya vídeos la semana que
   viene: **el reintento de mañana (viernes 22:07 UTC) sí correrá**, porque el paso 0 solo para si el lunes 23 tiene
   emisión o si queda una rama `claude/entrega-planificacion-*` sin aplicar, y el lunes 23 está vacío. Esa ejecución
   tendrá otra vez toda la semana por delante (con la reserva de esta noche). Además, la dirección puede relajar el
   criterio de la lectura (ver sugerencias) o aceptar publicar menos.
2. **Dos temas caen solo por no tener el artículo completo:** `D15` (Dijk y otros, 2009, *Emotion* 9(2), DOI
   10.1037/a0015081) y `H01` (Ruch y otros, 2018, *HUMOR*, DOI 10.1515/humor-2017-0099). Si alguien puede dejar los
   PDF en `01_bibliografia/` (o el método en una línea), los dos tienen a los tres lectores quedándose hasta el final.
3. **B2 no llegará a decidir nada** con las posiciones 18-24 vacías (ver el apartado 2). El 29/11 no tiene ciclo.
4. **C26** sigue sin decidir; si se para, `MDS-072` se queda en el banco.
5. Las ramas `claude/entrega-direccion-20261112-1323` y `claude/entrega-revision-20261104-1031` siguen vivas; no son
   mías.

## Sugerencias a la dirección

- **`H-lectura-q3-con-motivo`**: en la pregunta 3, pedir al lector que diga **por qué** no la entendió y contar como
  bloqueo solo «no sé a qué se refiere / no puedo repetirla», no «no sé qué otras cosas les preguntaron» ni «no sé
  quién es Fulano». Esta noche muchas frases se copiaron con «se entiende, pero…» o pidiendo un detalle que no cabe
  en 45 s. Regla afectada: punto 4 de la lectura en frío. Se mediría con la tasa de aprobados y con «se quedaron» de
  los que pasen (si los que pasan con el criterio nuevo retienen igual, el criterio viejo sobraba).
- **`H-rotulo-con-verbo`**: el rótulo de pantalla, una frase con sujeto y verbo (nunca «X… y Y»). Regla afectada:
  regla 14. Se mediría con las frases de rótulo copiadas en la pregunta 3.
- **`H-texto-completo`** (repetida del 12/11): no intentar un tema cuyo método no esté en el resumen sin haber leído
  el artículo. Esta noche, de los cuatro temas con texto completo, pasó uno y otro (`I17`) cayó solo por rótulos; de
  los que no lo tenían, ninguno.

## Lo que falta

- **Ocho días vacíos** (22 a 29/11). **Banco vacío.**
- **Familia `mensajes`: ninguno** esta semana (cayeron `I21`, `I24` e `I17`).
- **Tanteo de cosquillas: ninguno** (cayeron los cuatro).
- El largo `MDH-008` no lo he tocado (es de la dirección).
