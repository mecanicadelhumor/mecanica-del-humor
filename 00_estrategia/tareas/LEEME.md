# 00_estrategia/tareas/ — los prompts de las rutinas y los workflows por mover (público)

**Hay dos carpetas «tareas» en el proyecto y no son la misma cosa** (ordenado el 05/11/2026 por la
dirección, a petición del codirector):

| Carpeta | Repositorio | Qué guarda |
|---|---|---|
| **`00_estrategia/tareas/`** (esta) | público, `mecanica-del-humor` | **Los prompts de las rutinas** (`revision-diaria.md`, `planificacion-jueves.md`, `metricas-lunes.md`, `animacion.md`) y **los workflows que el codirector tiene que mover** a `.github/workflows/` (`workflows_<fecha>/`). Es la única carpeta con workflows |
| `direccion/tareas/` (en el ordenador del codirector, `00_estrategia/privado/tareas/`) | privado, `direccion` | El prompt de la dirección en diferido (`direccion.md`), los ficheros de tareas del codirector (`AAAA-MM/tareas_codirector_*.md`) y el espejo del arranque de la planificación. **Nunca workflows** |

No se renombran: las dos rutas están escritas en los arranques de las rutinas (trampa 58), y las rutinas
no las toca la dirección (trampa 47). Lo que confundía eran las carpetas `workflows_*` en los dos sitios:
desde hoy **solo hay workflows aquí**, y una carpeta `workflows_<fecha>/` se borra en cuanto el
codirector la ha movido y el fichero de `.github/workflows/` es idéntico.

Workflows pendientes de mover a 05/11/2026: `workflows_2026-10-23/` (el segundo Short diario,
`iteracion-14`, **aplazado al 16/11**: no lo muevas todavía).

---

## Los prompts de las rutinas (texto de 05/10/2026, devuelto aquí el 05/11/2026)

Las tres tareas que sostienen el canal —la revisión diaria, la planificación de
los jueves y las métricas de los lunes— corren con un prompt que vive en el
almacén de tareas programadas, no en el repositorio. Hasta el 31 de agosto de
2026 eso significaba que **no se podían leer sin arqueología**: `list_triggers`
no devuelve el texto, hay que sacarlo del `job_config` en crudo.

Esta carpeta es el espejo. Sirve para tres cosas:

1. **Leerlos.** Saber qué se le ha pedido exactamente a cada agente sin abrir
   nada más.
2. **Recuperarlos.** Si el almacén se pierde o una tarea se borra por error, el
   texto está aquí y se vuelve a crear.
3. **Discutirlos.** Un prompt es la instrucción más cara del proyecto: es lo
   único que decide qué hace un agente durante toda una semana. Merece revisarse
   como se revisa el código.

## Esto cambió el 12 de septiembre de 2026: ya no hay dos copias

**Hasta hoy la copia que se ejecutaba era la del almacén y estos ficheros eran un
espejo.** El párrafo que iba aquí avisaba de que un día no coincidirían — y la
manera de que no coincidieran era barata: cambiar el fichero y olvidarse del
`update_trigger`. Nadie se enteraría hasta que un agente hiciera algo que su
documentación decía que ya no hacía.

**Ahora el fichero de esta carpeta ES el prompt.** El del almacén se ha reducido
a un arranque de una página que dice: clona el repositorio, lee
`00_estrategia/tareas/<tu fichero>.md` desde el primer `---` hasta el final, y
síguelo como si fuera este mensaje.

Consecuencias, que son todas buenas:

- **Cambiar lo que hace un agente es editar un fichero y commitearlo.** Ya no
  hace falta `update_trigger` para nada salvo el cron, el nombre o el modelo.
- **El prompt se versiona con git** y se revisa en un diff, como el código. Es
  la instrucción más cara del proyecto y hasta hoy era lo único que no se podía
  revisar así.
- **Se acabó la divergencia.** No hay dos copias que comparar.

**Lo que hay que tener presente, y es el precio:** un cambio en estos ficheros
**no surte efecto hasta que está en `origin/main`**. Editarlo en local y no
commitear equivale a no haberlo cambiado, y la tarea de mañana leerá la versión
vieja. Es el mismo reloj de la trampa 11 (`PROMPT_DE_ARRANQUE.md`), aplicado a
los prompts.

**Y por si el repositorio no se puede clonar:** el arranque del almacén lleva
repetidas las seis o siete reglas cuyo incumplimiento hace daño irreversible
—no pedir autorización nunca, no llamar al puente de dispositivos, no hacer
`push`, un fichero un dueño, y no escribir el nombre del codirector—. Si el
clon falla, el agente dice el error y para; no improvisa.

## Quién los escribe

Solo el codirector y yo (la dirección). `00_estrategia/` no lo toca ningún agente,
y estos prompts menos que nada: un agente que puede reescribir sus propias
instrucciones no tiene instrucciones.

| Fichero | Tarea | Cuándo corre | `trigger_id` |
|---|---|---|---|
| `revision-diaria.md` | Revisión de calidad | todos los días, 11:28 hora de España | `trig_01K834hHyZ9ytxXXA3uP5y7Y` (rutina de Code desde el 30/09; la vieja, `trig_019Qjt…`, apagada) |
| `planificacion-jueves.md` | Equipo editorial | jueves 22:07 (+ viernes y sábado de reintento) | `trig_014hUCsYDz9mSVNKTFtQxZpR` (rutina de Code desde el 30/09; la vieja, `trig_015qkb…`, apagada) |
| `metricas-lunes.md` | Analista | lunes, 12:03 | `trig_01TmnPoPLXBx65x9Po4Y2PYh` (rutina de Code desde el 30/09; la vieja, `trig_01GhNr…`, apagada) — **sigue con el prompt entero en el almacén**, pendiente de pasar al mismo esquema |
| `animacion.md` | Animación a medida (C55.2) | viernes, 09:07 UTC | (rutina de Code; la crea el codirector) |
