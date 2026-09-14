# Tareas para el codirector — 14/09/2026

Formato acordado el 7/9 y repetido el 12 (C32): todo explicado de principio a fin, sin
resumir, aunque sean cosas que ya hayamos hecho antes, y **diciendo siempre el sitio
exacto**.

**Orden de urgencia:**

| | Qué | Tiempo | Cuándo |
|---|---|---|---|
| **1** | `git add / commit / push` de lo de hoy | 5 min | **HOY, antes de las 03:00 de la madrugada** |
| **2** | Crear `.github/workflows/voz_adelantada.yml` | 15 min | **Antes de mañana martes a las 11:00** |
| **3** | Mirar la cuota de imagen en el panel de Gemini | 2 min | Esta semana |
| **4** | Doce fotos y abrir el muestrario de imagen | 20 min | Esta semana, antes del jueves |

La 1 y la 2 tienen fecha de verdad. La 3 y la 4 pueden esperar a cuando tengas un rato.

---

## TAREA 1 — Commit y push de lo de hoy. Y por qué esta noche y no mañana

**Estado:** pendiente. **Tiempo:** 5 minutos. **Es la más urgente de las cuatro.**

### 1.1 Por qué corre prisa, y la prisa es de horas

He arreglado la voz: la dirección de actor que hacía que el Short se riera todo el rato y
que sonara despiezado. El arreglo está escrito en tu carpeta, en
`03_produccion/pipeline/voz.py`, **pero hasta que no hagas `push` no existe para GitHub
Actions**, que es quien produce el vídeo.

Y aquí entra el reloj, que es la trampa 11 de `PROMPT_DE_ARRANQUE.md` y que ya nos costó un
vídeo el 7 de septiembre: **la producción arranca a las 01:13 UTC, o sea las 03:13 de la
madrugada en España.** Un arreglo commiteado por la mañana **no entra en el vídeo de ese
día**, entra en el del día siguiente.

- Si haces `push` **esta noche antes de las 03:00**: `MDS-017` se produce mañana martes de
  madrugada **con la voz arreglada** y lo escuchas mañana a las 19:00.
- Si lo haces **mañana por la mañana**: `MDS-017` sale con la voz de hoy —riéndose— y el
  primero arreglado será `MDS-018`, el miércoles.

No es grave si se te pasa. Pero es un día de diferencia sobre lo que más te ha molestado.

### 1.2 Qué hay que hacer

En `C:\MisProyectos\Humor`, desde Git Bash o desde donde sueles hacerlo:

```
git status
git add -A
git commit -m "dirección 14/09: C33 (voz dirigida por escena), C27 pieza C, C34 (imagen)"
git push
```

`git status` primero, sin más motivo que ver la lista y compararla con la de abajo.

### 1.3 Qué ficheros tienen que salir en esa lista

Ocho, ni uno más:

```
modificados:
  03_produccion/pipeline/voz.py
  03_produccion/pipeline/voz_precache.py
  00_estrategia/PLAN_DE_CAMBIOS.md
  00_estrategia/REGLAS.md
  00_estrategia/LEEME.md
  00_estrategia/PROMPT_DE_ARRANQUE.md
nuevos:
  00_estrategia/tareas/tareas_codirector_2026-09-14.md   (este fichero)
  07_pruebas/imagen-14-09/muestrario.html
```

Si sale algo más, mírame antes de hacer `commit`: puede ser trabajo de la revisión diaria
sin aplicar, y ahí es donde pasó el desastre del 21 de agosto.

**Lo que NO tiene que salir** porque yo no lo he tocado: ningún guion de
`05_calendario/guiones/`, ni `parrilla.json`, ni `metricas.json`, ni
`registro_publicaciones.json`, ni nada de `.github/workflows/`.

### 1.4 Cómo saber si ha funcionado

Mañana martes, cuando salga `MDS-017` a las 19:00: **no debería reírse**. Y si quieres
comprobarlo sin escuchar, en el expediente de calidad de mañana
(`05_calendario/qa/MDS-017.es/ficha.json`) cada escena lleva ahora un campo nuevo,
`direccion_voz`, con el papel que se le pidió: verás `apertura`, `remate`, `contraste`,
`cifra`, `planteamiento` y `objecion`, en ese orden.

---

## TAREA 2 — Crear `.github/workflows/voz_adelantada.yml`

**Estado:** pendiente, el fichero ya está escrito y solo hay que copiarlo.
**Tiempo:** 15 minutos. **Fecha límite: mañana martes a las 11:00 de la mañana.**

### 2.1 Qué es y por qué existe

El episodio largo del sábado tiene unas cuarenta escenas. Gemini, en el plan gratuito, da
**diez peticiones al día**. Cuarenta escenas no caben en el sábado, pero sí caben repartidas
de martes a viernes, que es lo que hace este workflow: cada día coge el guion del sábado
siguiente, mira qué escenas todavía no tienen voz guardada y sintetiza las que le quepan en
la cuota del día. El sábado, la producción se encuentra el trabajo hecho.

### 2.2 Por qué ahora tiene fecha, cuando la semana pasada no la tenía

Porque me lo dijiste tú el 7 de septiembre: *«no debe haber esa diferencia entre los shorts
y los largos (si no, dejamos de hacer largos)»*.

`MDH-007` se publica el **sábado 19**. Si este workflow no está corriendo desde el martes,
ese episodio sale con `edge-tts` —la voz vieja— mientras los cinco Shorts de la semana salen
con la voz nueva y dirigida. Y eso estropea algo más importante que un vídeo: **el punto de
control del 27 de septiembre.** Ese día hay que decidir si el episodio largo merece la
semana que cuesta, y no se puede decidir eso comparando un largo con voz mala contra Shorts
con voz buena. **O los dos productos van en igualdad de condiciones, o la decisión del 27 no
vale nada.**

Cada día que pase sin crearlo es un día menos de precacheo: el martes da para ~9 escenas, el
miércoles otras ~9, y así. Si lo creas el viernes, solo entran 9 de 40.

### 2.3 Qué hay que hacer, paso a paso

**El fichero ya está escrito y probado.** Está en tu carpeta, aquí:

```
C:\MisProyectos\Humor\07_pruebas\voz-adelantada-14-09\voz_adelantada.yml
```

Hay que **copiarlo** (no moverlo, que la copia de `07_pruebas/` es la documentación) a:

```
C:\MisProyectos\Humor\.github\workflows\voz_adelantada.yml
```

Lo puedes hacer con el explorador de Windows, copiar y pegar, o desde Git Bash:

```
cp 07_pruebas/voz-adelantada-14-09/voz_adelantada.yml .github/workflows/voz_adelantada.yml
git add .github/workflows/voz_adelantada.yml
git commit -m "workflow: voz adelantada del episodio largo (C27)"
git push
```

**Por qué te lo pido a ti y no lo hago yo:** `.github/workflows/` no se puede escribir en
remoto, ni por mí ni por nadie. No es desconfianza, es una limitación técnica, y está escrita
como permanente en `REGLAS.md` (regla 11.7).

### 2.4 Cómo comprobar que ha quedado bien, sin esperar al martes

En GitHub, `Actions` → en la lista de la izquierda tiene que aparecer **«Voz adelantada
(episodio largo)»**. Si aparece, está bien puesto; si no aparece, el fichero no está en la
ruta correcta o el `push` no llegó.

Y si quieres verlo funcionar sin esperar: en esa misma pantalla, con el workflow
seleccionado, hay un botón **«Run workflow»**. Lánzalo. Debería tardar unos cuatro minutos
y terminar diciendo cuántas escenas ha precacheado.

### 2.5 Qué NO hay que hacer

- **No lo edites.** Si algo falla, dímelo y lo corrijo yo en `07_pruebas/`.
- **No borres** la copia de `07_pruebas/voz-adelantada-14-09/`: es donde está explicado.
- **No te preocupes si algún día falla por cuota.** Está diseñado para eso: para y lo retoma
  al día siguiente. Y si el sábado falta alguna escena, sale con la voz vieja y el
  expediente dice cuáles — no se queda sin vídeo.

---

## TAREA 3 — Mirar la cuota de imagen en el panel de Gemini

**Estado:** pendiente. **Tiempo:** 2 minutos. **Cuándo:** esta semana, sin prisa.

### 3.1 Por qué te lo pido

Me pediste reevaluar el uso de imágenes, y una de las tres vías es **generarlas nosotros con
IA**, que es además la que más me convence a medio plazo: resuelve de golpe la licencia, la
coherencia de estilo y la objeción de que las fotos de banco «no son de marca», porque el
estilo lo elegiríamos nosotros. Y encaja exactamente con la analogía que trajiste tú: N
imágenes al día dentro de la cuota gratuita, acumulando un banco propio, igual que estamos
troceando el episodio largo.

**Pero no voy a diseñar alrededor de una cuota que no hemos mirado.** Ya nos pasó el 4 de
septiembre: dimos por buena la cuota de voz mirando los tokens por minuto, y lo que nos tumbó
fue el límite de **tres peticiones por minuto**, que estaba en la misma pantalla y nadie
había mirado (trampa 8). Desde entonces, en este proyecto las cuotas se miran antes.

Lo he intentado verificar yo en la documentación pública y no aparece con números: Google
remite a tu propio panel, que es justo lo que tú puedes ver y yo no.

### 3.2 Qué hay que hacer

1. Entra en **Google AI Studio**, con la misma cuenta con la que sacaste `GEMINI_API_KEY`.
2. Busca la página de **límites de uso** (la misma donde viste «3 de 3 peticiones por
   minuto» el 4 de septiembre).
3. Busca si aparece algún modelo **de imagen** — los nombres suelen llevar `image`, `imagen`
   o `nano banana`.
4. **Apunta tres números de cada modelo de imagen que veas**, y los tres importan:
   - peticiones por **minuto**
   - peticiones por **día**
   - si dice en algún sitio que ese modelo **no** está en el plan gratuito

Con una captura de pantalla o copiando los números en un mensaje me vale.

### 3.3 Qué pasa con cada respuesta

- **Si hay cuota gratuita de imagen:** montamos el banco generado, con un workflow diario
  igual que el de la voz, y en tres o cuatro semanas tenemos cuarenta imágenes propias con
  un estilo coherente. Es la vía buena.
- **Si no la hay, o es de pago:** no pasa nada y no se para nada. Las otras dos vías —el lote
  de prueba y el banco de fotos con licencia— siguen exactamente igual, y son las que
  arrancan esta semana con la tarea 4.

---

## TAREA 4 — Doce fotos, y abrir el muestrario de imagen

**Estado:** pendiente. **Tiempo:** 20 minutos. **Cuándo:** antes del jueves 17, que es
cuando la planificación escribe los Shorts de la semana que viene.

### 4.1 Lo primero: tenías razón y yo estaba equivocado

El 7 de septiembre descarté las imágenes en dos líneas: *«imágenes de banco (regla 9 y no
son de marca), imágenes generadas por IA (coste)»*. Lo he revisado hoy y **el descarte estaba
mal**:

- **La regla 9** prohíbe material **sin licencia** —clips de cómicos, de programas, de
  películas— por el riesgo de strike. Una foto CC0 **tiene** licencia. Estiré una regla
  nuestra hasta que dijera lo que me convenía, que es exactamente el error que llevamos
  semanas apuntando para no cometerlo.
- **«No son de marca»** sí era un argumento de verdad, y tiene arreglo. Es todo lo que sigue.
- **«IA: coste»** no estaba medido. De ahí la tarea 3.

Queda escrito en `REGLAS.md` (dentro de la regla 9) y en la versión 8 del plan.

### 4.2 El riesgo real, que no es el que yo decía

Meter fotos de stock tal cual **no nos deja sin marca: nos cambia una firma por otra.** Hoy
parecemos un vídeo automatizado; con fotos de stock crudas pareceríamos un carrusel de
LinkedIn. Eso no es avanzar.

Así que la foto no entra cruda, **entra vestida**: en blanco y negro tintada con el ámbar o
el cian del canal (un duotono), metida dentro de un marco de la rejilla de taller, nunca
sola —siempre con su texto— y con una deriva lenta para que no esté quieta. Todo eso es CSS:
no cuesta un céntimo, no cuesta tiempo de render y es determinista.

**La idea de fondo, que es la que hace que esto funcione:** el duotono es lo que hace que
cuarenta fotos de cuarenta sitios distintos parezcan **una colección** en vez de un revoltijo.
Ahí es donde se resuelve lo de «no son de marca».

### 4.3 Y esto no se decide opinando: se decide mirándolo

Te he dejado una página para eso, aquí:

```
C:\MisProyectos\Humor\07_pruebas\imagen-14-09\muestrario.html
```

**Ábrela con doble clic** (se abre en tu navegador; no necesita internet, no sube nada a
ningún sitio y no instala nada) y **arrastra dentro dos o tres fotos** cualesquiera. Verás
cada una puesta dentro de una escena real del canal, con cinco tratamientos al lado:

1. **Cruda** — la foto tal cual, para comparar.
2. **Duotono ámbar** — gris más el ámbar de marca.
3. **Duotono cian** — gris más el cian de marca.
4. **Gris frío** — desaturada dentro del azul, sin color de marca.
5. **Ámbar con trama** — el duotono más un semitono de taller.

**Lo que hay que mirar no es si la foto es bonita.** Es si **tres fotos distintas, de sitios
distintos, parecen de la misma colección** después del tratamiento. Si lo parecen, la
objeción de la marca queda resuelta y seguimos. Si no lo parecen, paramos aquí y no hemos
gastado nada.

Dime **qué número prefieres** (o que ninguno) y con eso escribo el cambio en `escena.html`.

### 4.4 Las doce fotos, si el muestrario te convence

No hacen falta muchas: **doce llegan** para vestir la primera escena de los Shorts de una
semana y para arrancar el banco.

**Dónde buscarlas.** Te lo pido a ti y no lo hago yo por el mismo motivo que los sonidos de
la semana pasada: **mis contenedores no llegan a esos sitios.** Sirven, entre otros:

- **Openverse** (`openverse.org`) — buscador de Creative Commons, con filtro de licencia.
- **Pexels** o **Pixabay** — licencia propia que permite uso comercial sin atribución.
- **Wikimedia Commons** — mucho material CC0 y CC-BY.

**Qué buscar.** Caras y manos de personas reales en situaciones cotidianas: alguien
riéndose, alguien sin entender algo, dos personas hablando, alguien mirando el móvil, una
reunión, una cara de sorpresa. **Nada de gente en traje señalando gráficas**, que es la
estética de la que estamos huyendo. Cuanto más normal y menos posada, mejor.

**Dónde dejarlas.**

```
C:\MisProyectos\Humor\02_marca\banco\
```

Créala si no existe. Nombres descriptivos y en minúscula, con guiones: `risa-grupo-01.jpg`,
`cara-duda-02.jpg`, `movil-metro-01.jpg`.

**Y lo único que no se puede saltar:** en esa misma carpeta, un fichero de texto llamado
`origen.txt` con **una línea por foto**, así:

```
risa-grupo-01.jpg | CC0 | autor: Nombre Apellido | https://... (dirección de donde la bajaste)
```

Con el nombre del fichero, la licencia, el autor y el enlace. **Una foto sin esas cuatro
cosas no se usa**, aunque parezca libre: es la regla 9 y es lo que nos protege. Si un sitio
no dice claramente la licencia, mejor busca otra foto — hay millones.

Yo convierto después ese `origen.txt` en el `banco.json` que usa el render, y me encargo de
las atribuciones donde toquen.

### 4.5 Qué NO hay que hacer

- **No recortes ni retoques las fotos.** El recorte y el color los pone el render; si llegan
  ya tratadas, se tratan dos veces y se ven mal.
- **No busques fotos «para un vídeo concreto».** El banco se construye una vez y se reutiliza
  siempre: por eso te pido cosas genéricas y no ilustraciones de los guiones de esta semana.
  A partir de unas cuarenta fotos, ningún Short necesita imagen nueva. Esa es toda la gracia
  de que sea un banco.
- **No te lo tomes como trabajo recurrente.** Si esto acaba pidiéndote fotos cada semana,
  está mal diseñado y lo tiro yo mismo (regla 5).

---

## Y una cosa que NO es una tarea, pero conviene que sepas

**El guion de los Shorts que te sonó inconexo ya está arreglado, y todavía no lo has visto.**

Los dos prompts de guionista se reescribieron el sábado 12 con tres pruebas nuevas de cosido
—el hilo con un solo sujeto, nada nuevo después de la mitad, y el detalle concreto con la
misma palabra. Pero **`MDS-016` a `MDS-020` y `MDH-007` los escribió la planificación del
jueves 10, dos días antes.** Todo lo que se publique de aquí al domingo es material anterior
al arreglo.

**El primero escrito con el guionista nuevo lo escribe la planificación del jueves 17 y se
publica el lunes 21.** Ese es el primero que se puede juzgar por el hilo, y por eso la
semana del 21 importa más de lo que parece: es la única semana con material nuevo antes del
punto de control del 27.

Lo que sí he arreglado hoy es la mitad que era de la voz y no del guion: con Gemini, cada
escena es una llamada independiente, y el modelo le ponía a cada fragmento su propia
entonación de arranque y su propio punto final. Seis fragmentos autónomos seguidos suenan a
seis frases sueltas **por bien cosido que esté el guion en papel**. Ahora cada escena sabe de
dónde viene y si tiene que cerrar o quedarse en el aire, que es lo que convierte nuestro
silencio de 1,35 segundos en una pausa dramática en vez de en un corte.

Eso sí lo oirás mañana, si haces el `push` esta noche.
