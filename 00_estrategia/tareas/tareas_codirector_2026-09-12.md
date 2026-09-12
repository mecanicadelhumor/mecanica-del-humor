# Tareas para el codirector — 12/09/2026

Formato acordado el 7/9: todo explicado de principio a fin, sin resumir, aunque
sean cosas que ya hayamos hecho antes.

**Este fichero se reescribió por la tarde**, después de la sesión de dirección en modo
Cowork. Lo que había antes (las tareas 1 y 2 de la mañana) está corregido: la tarea 2
—reabrir la conversación en Cowork— **ya está hecha**, y la tarea 1 estaba **mal
explicada por mi parte**. Ver abajo.

**Orden de urgencia:**

| | Qué | Tiempo | Cuándo |
|---|---|---|---|
| **1** | `git add / commit / push` de lo de hoy | 5 min | **HOY, antes de las 11:28 de mañana** |
| **2** | Mover `GEMINI_API_KEY` de paso en `producir.yml` | 10 min | Antes del lunes 14 |
| **3** | Crear `voz_adelantada.yml` | 15 min | Cuando esté el diseño, no antes del viernes |
| **4** | Escuchar MDH-006 y decidir sobre `pico_dbtp` | 5 min | Opcional, ya está publicado |

---

## TAREA 1 — Commit y push de lo de hoy. Y por qué hoy y no mañana

**Estado:** pendiente. **Tiempo:** 5 minutos. **Es la más urgente de las cuatro.**

### 1.1 Por qué corre prisa

He cambiado cómo funcionan las tareas programadas, y el cambio tiene dos mitades:

- **La mitad que ya está hecha** (la hice yo esta tarde): el prompt que corre en el almacén
  de tareas programadas ya no contiene el texto entero. Ahora es un arranque corto que dice
  «clona el repositorio y lee `00_estrategia/tareas/<tu fichero>.md`».
- **La mitad que depende de ti**: ese fichero tiene que estar **en GitHub**. Lo he escrito en
  tu carpeta, pero hasta que no hagas `push` no existe para ellas.

**La revisión diaria corre mañana domingo a las 11:28.** Si a esa hora el commit no está,
va a clonar `origin/main`, leer la versión vieja del fichero, y comportarse como antes. No
rompe nada —el arranque lleva las reglas importantes repetidas dentro— pero se pierde el
arreglo de un día.

**Y la planificación corre el jueves 17 a las 22:00.** Esa sí es la que se bloqueó el 10, así
que esa es la que de verdad no puede leer la versión vieja.

### 1.2 Qué hay que hacer

En la carpeta `C:\MisProyectos\Humor`, desde Git Bash o desde donde sueles hacerlo:

```
git status
git add -A
git commit -m "dirección 12/09: guionista reescrito, C28, C29, C30, C31, C27 corregido"
git push
```

`git status` antes, sin más motivo que ver la lista de ficheros que salen y compararla con
la de abajo. Si aparece algo que no está en esa lista, dímelo antes de hacer push.

### 1.3 Los ficheros que he escrito en tu carpeta esta tarde

**Código y prompts de agentes:**

- `04_agentes/prompts/guionista_corto.md` — reescrito entero
- `04_agentes/prompts/guionista.md` — reescrito entero
- `04_agentes/validar_guion.py` — dos comprobaciones nuevas (C28 error, C29 aviso)
- `03_produccion/pipeline/escena.html` — tres funciones nuevas para el texto dentro de SVG

**Prompts de las tareas programadas** (son los que tienen prisa):

- `00_estrategia/tareas/revision-diaria.md`
- `00_estrategia/tareas/planificacion-jueves.md`
- `00_estrategia/tareas/LEEME.md`

**Documentos:**

- `00_estrategia/PLAN_DE_CAMBIOS.md` — versión 7 al final
- `00_estrategia/PROMPT_DE_ARRANQUE.md` — tus dos autorizaciones, tres trampas nuevas
- `00_estrategia/REGLAS.md` — regla 13 (cadencia de risa) y regla 14.4 (el detalle concreto)
- `00_estrategia/LEEME.md`
- `00_estrategia/tareas/tareas_codirector_2026-09-12.md` — este fichero
- `05_calendario/bitacora/2026-09-12-direccion.md` — la bitácora de la sesión

**Lo que NO he tocado, a propósito:**

- `00_estrategia/PROMPT_DIRECCIÓN.md` — es tuyo. Ni una letra.
- `.github/workflows/` — protegida siempre. Ver tarea 2.
- Ningún guion de `05_calendario/guiones/`, ni `parrilla.json`, ni `ESTADO.md`, ni nada
  que sea de la planificación o de la revisión diaria.

---

## TAREA 2 — `GEMINI_API_KEY` está en el paso equivocado de `producir.yml`

**Estado:** pendiente. Bloquea la voz nueva del lunes 14.
**Tiempo estimado:** 10 minutos.
**Lo haces tú** porque `.github/workflows/` está protegida contra escritura remota, siempre,
también para mí.

### 2.1 Lo que hiciste está bien hecho, y en el sitio equivocado. Y es culpa mía

Lo añadiste, y la línea es **correcta letra por letra**:

```
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
```

El problema es dónde está. Ahora mismo, en la **línea 294**, dentro del bloque `env:` del paso
**«Subir a YouTube»** — el que ejecuta `publicar.py`.

Y quien necesita esa clave es el paso **«Sintetizar narración»** (línea 194), que es el que
llama a `voz.py`, que es el que habla con Gemini. Ese paso **no tiene ningún bloque `env:`**.

**En GitHub Actions las variables de entorno de un paso solo existen en ese paso.** Así que
tal y como está, `publicar.py` recibe una clave de Gemini que no usa para nada, y `voz.py`
arranca sin ella y se cae al respaldo `edge-tts` sin decir nada.

**Y la culpa de esto es mía, no tuya.** Mis instrucciones de esta mañana decían: *«busca
`secrets.`, copia una de esas líneas entera, pégala justo debajo y cambia los dos nombres»*.
Todo correcto, y en ningún sitio decía **en qué paso**. La primera aparición de `secrets.`
en ese fichero está justamente en «Subir a YouTube», así que hiciste exactamente lo que
ponía. Es la misma clase de error que ya me había costado un vídeo en septiembre —documentar
una sintaxis sin documentar su ámbito— y está anotado como trampa 18 en
`PROMPT_DE_ARRANQUE.md` para que no vuelva a pasar.

### 2.2 El cambio, exacto

Abre `.github/workflows/producir.yml` con un editor de texto plano (VS Code, Notepad++, el
Bloc de notas). **No con Word ni con nada que reformatee**: YAML es sensible a los espacios.

**PASO A · Quitar la línea de donde está.**

Busca este bloque (está alrededor de la línea 289):

```yaml
      - name: Subir a YouTube
        if: ${{ github.event_name != 'workflow_dispatch' || inputs.subir }}
        env:
          YT_CLIENT_ID: ${{ secrets.YT_CLIENT_ID }}
          YT_CLIENT_SECRET: ${{ secrets.YT_CLIENT_SECRET }}
          TOKEN_ES: ${{ secrets.YT_REFRESH_TOKEN }}
          TOKEN_EN: ${{ secrets.YT_REFRESH_TOKEN_EN }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
```

**Borra la última línea**, la de `GEMINI_API_KEY`. Las otras cuatro se quedan como están.

**PASO B · Ponerla donde va.**

Busca ahora este otro bloque (está alrededor de la línea 194, bastante más arriba):

```yaml
      - name: Sintetizar narración
        run: |
          while IFS=$'\t' read -r ID G; do
```

Y déjalo así — es decir, **añade las dos líneas `env:` y `GEMINI_API_KEY` entre `- name:` y
`run:`**:

```yaml
      - name: Sintetizar narración
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: |
          while IFS=$'\t' read -r ID G; do
```

**La indentación, que es lo único delicado:**

- `env:` va **con los mismos espacios que `run:`** (ocho espacios). Lo más seguro es
  copiar la línea `run: |`, pegarla encima, y sustituir `run: |` por `env:`.
- La línea de `GEMINI_API_KEY` va **dos espacios más a la derecha** que `env:` (diez
  espacios en total).
- **Espacios, nunca tabuladores.** YAML no admite tabuladores. Si tu editor los mete al
  pulsar Tab, escríbelos a mano.

### 2.3 Comprobaciones antes del push

- El nombre está escrito **exactamente** `GEMINI_API_KEY` en los dos sitios de la línea:
  mayúsculas, guiones bajos, sin espacios. GitHub distingue mayúsculas.
- Las llaves son dobles: `${{` al abrir, `}}` al cerrar.
- El paso «Subir a YouTube» ha quedado con **cuatro** líneas dentro de su `env:`, no cinco.
- El paso «Sintetizar narración» ha quedado con `env:` **antes** de `run:`, nunca después.

### 2.4 Cómo saber si ha funcionado

No hace falta esperar al lunes:

1. Pestaña **Actions** del repositorio → workflow **«Producir vídeo»**.
2. Si tiene `workflow_dispatch` (lo tiene), sale el botón **Run workflow**. Lánzalo.
3. Abre el paso «Sintetizar narración» y despliega el log.

Qué vas a ver, y qué significa cada cosa:

- **`***`** en lugar de un valor: buena señal. GitHub enmascara los secretos; que aparezca
  la máscara significa que la variable llegó.
- **`KeyError: 'GEMINI_API_KEY'`**, o un mensaje tipo *API key not found* / *missing
  credentials* al inicializar el cliente de Gemini: la variable **no** llegó. Repasa 2.3.
- **Nada de lo anterior, y el vídeo sale con voz**: también es normal por ahora. Hasta el
  lunes 14 `voz.py` corre con `--motor edge` por defecto, así que no pide la clave todavía.
  Lo que estás comprobando hoy es que la variable esté disponible, no que se use.

### 2.5 Lo que NO hay que hacer

- **No vuelvas a subir el secreto.** Está bien puesto desde hace tres semanas y no hay
  que tocarlo. Tu duda del 10/09 era razonable y la respuesta es la que ya te di: subir el
  secreto lo guarda cifrado en el repositorio; nombrarlo en el YAML es lo que hace que llegue
  al proceso. Son dos cosas distintas y hacen falta las dos.
- **No escribas la clave en claro en el YAML**, ni un momento para probar. El repositorio es
  público y el historial de git la conservaría aunque borres la línea después; habría que
  rotarla en Google AI Studio.
- **No muevas las otras cuatro líneas** del paso de subir a YouTube. Están bien.

---

## TAREA 3 — Crear `voz_adelantada.yml` (todavía no, pero para que sepas que viene)

**Estado:** el diseño no está escrito aún. **Tiempo cuando llegue:** unos 15 minutos.

Es la pieza que hace que el episodio largo del sábado deje de sonar peor que los Shorts. La
idea, en tres líneas: de viernes a viernes, un workflow coge el guion del sábado siguiente,
mira qué escenas de narración no están todavía en la caché de voz y sintetiza unas cuantas
cada día hasta agotar el margen diario de la API. El sábado, cuando se produce el vídeo, ya
está casi todo hecho.

**Lo que decidimos hoy y cambia lo que estaba escrito:** un episodio largo sale con **una
sola voz**, nunca mezclada. Si el viernes por la noche la caché no tiene las cuarenta
escenas, el episodio entero se hace con la voz de siempre. Nada de unas escenas con una voz y
otras con otra — que es la chapuza que descartaste el 7 y que el plan seguía dando por buena.

**Te lo pediré con un fichero como este cuando el diseño esté en `07_pruebas/`.** Lo escribe
la revisión diaria en la semana del 14. No hay nada que hagas tú ahora.

---

## TAREA 4 — MDH-006 y el `pico_dbtp` (opcional, y ya no corre prisa)

El episodio de hoy salió con `pico_dbtp` en −0,59 cuando el objetivo es ≤ −1,0. Ya está
publicado, así que esto es solo por si quieres escucharlo y decidir.

**Qué significa:** no es saturación —sigue por debajo de 0— así que es poco probable que se
oiga como distorsión. Lo que pasa es que el margen de seguridad es más estrecho de lo que
pide la especificación del canal, y ese margen está para absorber el pico que a veces
introduce la recodificación de YouTube. Es el primer episodio largo medido con este canario y
se aparta de los Shorts recientes con la misma música (−1,4).

**Qué puedes hacer:** escucharlo. Si no se nota nada raro, no hay nada que hacer y lo dejamos
pasar. Si se nota, dímelo y bajamos el nivel de la cama de música para los largos.

---

## LO QUE NO TE TOCA A TI, PARA QUE NO LO CARGUES

Todo lo de esta semana está hecho o encargado, y nada de ello necesita nada tuyo:

- **El guionista** — los dos prompts reescritos y ya en tu carpeta.
- **El texto del 2:34** — arreglado en `escena.html` y comprobado con el motor. De paso
  encontré que el resaltado del diagrama salía con los asteriscos a la vista: `*Usarla*` iba
  a publicarse así en MDH-007 el día 19. También arreglado.
- **El «martes» de MDS-014** — ahora es un error del validador, no algo que haya que ver a
  ojo.
- **El falso positivo de MDS-011** — arreglado en el prompt de la revisión diaria, y
  encargado el arreglo de fondo.
- **El bloqueo de la revisión semanal** — quitada la causa de los dos prompts, y ya
  aplicado en el almacén de tareas programadas.

Y una cosa que sí desbloquea tu autorización del 7: **`montaje.py` ya está autorizado sin
acotar**, así que P9 —los tres sonidos que descargaste— entra en la semana del 21 sin esperar
nada más.
