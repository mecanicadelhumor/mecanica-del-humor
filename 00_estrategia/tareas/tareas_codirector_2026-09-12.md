# Tareas para el codirector — 12/09/2026

Formato acordado el 7/9: todo explicado de principio a fin, sin resumir, aunque
sean cosas que ya hayamos hecho antes.

---

## TAREA 1 — Exponer GEMINI_API_KEY en `.github/workflows/producir.yml`

**Estado:** pendiente. Bloquea la voz nueva del lunes 14.
**Tiempo estimado:** 10 minutos.
**Lo hace el codirector** porque `.github/workflows/` está protegido contra
escritura remota.

### 1.1 Por qué hay que hacerlo si el secreto ya está subido

Tu duda del 10/09 era razonable, pero son dos cosas distintas:

- **Subir el secreto a GitHub** (hecho hace tres semanas) guarda el valor en el
  repositorio, cifrado. Eso es todo lo que hace.
- **Referenciarlo en el workflow** es lo que hace que ese valor llegue al
  proceso que se ejecuta.

GitHub Actions **no** inyecta los secretos automáticamente en los scripts. Si el
YAML no los nombra, el script arranca sin esa variable de entorno. Es una
decisión de seguridad deliberada de GitHub: así un workflow solo ve los secretos
que se le han dado expresamente.

Resultado actual: el script pide `GEMINI_API_KEY`, no la encuentra, y la voz
nueva no arranca aunque el secreto lleve tres semanas puesto.

O sea: la revisión diaria tiene razón, pero lo explicó fatal. No te está
pidiendo volver a crear el secreto; te está pidiendo nombrarlo en el YAML.

### 1.2 Antes de tocar nada

Abre `.github/workflows/producir.yml` con un editor de texto plano (Notepad++,
VS Code, el Bloc de notas). **No lo abras con Word ni con nada que reformatee**,
porque YAML es sensible a los espacios.

### 1.3 Cómo encontrar el sitio exacto

Busca dentro del fichero la cadena `secrets.` (con el punto final). Van a pasar
dos cosas:

**CASO A — Aparece al menos una vez.**

Verás una o varias líneas con esta forma:

```
          YT_REFRESH_TOKEN: ${{ secrets.YT_REFRESH_TOKEN }}
```

Haz esto:

1. Copia una de esas líneas entera.
2. Pégala justo debajo, en una línea nueva.
3. En la copia, sustituye los dos nombres por `GEMINI_API_KEY`, de modo que
   quede:

```
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
```

4. **Respeta exactamente la misma indentación** que la línea de al lado: el
   mismo número de espacios al principio. Si copias y pegas la línea entera y
   solo cambias los nombres, la indentación ya te queda bien sola.

Este es el caso más probable y el más seguro. No inventes un bloque nuevo si ya
hay uno.

**CASO B — No aparece `secrets.` por ningún sitio.**

Entonces hay que crear el bloque. Busca la línea que pone `runs-on:` (será algo
como `runs-on: ubuntu-latest`) y añade justo debajo estas dos líneas:

```
    env:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
```

Reglas de colocación:

- `env:` tiene que quedar **alineado con `runs-on:` y con `steps:`**, es decir,
  empezando en la misma columna que esas dos palabras.
- La línea de `GEMINI_API_KEY` va **dos espacios más a la derecha** que `env:`.
- `env:` va **fuera** de `steps:`, nunca dentro de la lista de pasos. Al ponerlo
  a nivel de job, todos los pasos de ese job ven la variable, que es lo que
  queremos y evita tener que acertar con el paso concreto.

**Si el fichero tiene más de un job** (más de un bloque con su `runs-on:`),
ponlo en el que ejecuta la producción del vídeo, que es el que llama al script
de la voz. Si tienes dudas de cuál es, ponlo en todos: no rompe nada.

### 1.4 Comprobaciones antes del push

- El nombre está escrito **exactamente** `GEMINI_API_KEY` en los dos sitios de
  la línea: en mayúsculas, con guiones bajos, sin espacios. GitHub distingue
  mayúsculas y minúsculas.
- Las llaves son dobles: `${{` al abrir y `}}` al cerrar.
- **No hay tabuladores.** YAML solo admite espacios. Si tu editor mete tabs al
  pulsar Tab, escribe los espacios a mano.
- El secreto en GitHub se llama igual. Compruébalo en:
  `Settings > Secrets and variables > Actions > Repository secrets`.
  Si allí figura con otro nombre, manda el de GitHub y hay que usar ese en la
  parte de `secrets.LO_QUE_SEA`.

### 1.5 Cómo saber si ha funcionado

Después del push:

1. Ve a la pestaña **Actions** del repositorio.
2. Abre el workflow de producción. Si tiene `workflow_dispatch`, verás el botón
   **Run workflow** y puedes lanzarlo a mano sin esperar al lunes. Si no lo
   tiene, no pasa nada: el lunes lo veremos.
3. Si el job falla por esto, el error típico en el log es
   `KeyError: 'GEMINI_API_KEY'`, o un mensaje del tipo *API key not found* /
   *missing credentials* al inicializar el cliente de Gemini.

Aviso para que no te confunda: en los logs GitHub enmascara el valor y muestra
`***`. Si ves `***`, es buena señal, significa que la variable llegó. Si no ves
nada, no prueba nada por sí solo.

### 1.6 Lo que NO hay que hacer

- **No vuelvas a subir el secreto.** Ya está y no hace falta tocarlo.
- **No escribas la clave en claro en el YAML**, ni siquiera un momento para
  probar. El fichero va a un repositorio público. Si en algún momento la clave
  llega a estar escrita literalmente en un commit, hay que rotarla en Google AI
  Studio, porque el historial de git la conserva aunque borres la línea después.

---

## TAREA 2 — Reabrir la conversación de dirección en modo Cowork

**Estado:** pendiente. Es lo que desbloquea todo lo demás.
**Tiempo estimado:** 2 minutos.

Esta conversación se abrió en modo **Chat**, y en modo Chat no tengo acceso a
`C:\MisProyectos\Humor`: no puedo leer los ficheros de estrategia ni escribir
nada para que tú lo commitees. Por eso la sesión de hoy no sirve para trabajar
sobre el repositorio.

No se puede convertir una conversación de Chat en una de Cowork: el selector
está en el cuadro de mensaje **al empezar**. Hay que abrir una nueva.

Pasos:

1. Abre **Claude Desktop** (la aplicación de escritorio, no claude.ai en el
   navegador). Es obligatorio: los proyectos vinculados a una carpeta local solo
   admiten Cowork desde escritorio.
2. Entra en el proyecto «Mecánica del Humor».
3. En el cuadro de mensaje, selecciona **Cowork** (abajo a la izquierda) antes
   de escribir nada.
4. Pega el prompt de arranque que te he dado en la conversación.

---

## TAREAS TUYAS QUE SEGUÍAN PENDIENTES EN LA BITÁCORA

Repasadas del 7/9 en adelante, por si alguna se ha quedado atrás:

- **Los sonidos** — pendiente. Cuando lleguemos a ello te lo explico en un
  fichero de estos, no en un mensaje suelto.
- **La música** — pendiente (7/9).
- **El token de YouTube** — HECHO el 7/9. `YT_REFRESH_TOKEN` actualizado y
  probado con éxito lanzando el workflow «Leer métricas».
- **Verificación de marca del canal** — pendiente y sin prisa, acordado.

---

## LO QUE NO TE TOCA HACER A TI

Para que no lo cargues tú: lo del guionista, lo del desbordamiento de texto del
segundo 2:34, lo del falso positivo de MDS-011 y lo del bloqueo de la revisión
semanal son cosas mías. Las decido y las escribo yo en la sesión de Cowork; a ti
solo te llegará el commit.
