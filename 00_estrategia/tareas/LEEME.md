# Los prompts de las tareas programadas

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
| `revision-diaria.md` | Revisión de calidad | todos los días, 11:28 hora de España | `trig_019QjtovuzeUocmx1P8NJH3F` |
| `planificacion-jueves.md` | Equipo editorial | jueves, 22:00 | `trig_015qkb2sqbbJwJE1qgoNMK95` |
| `metricas-lunes.md` | Analista | lunes, 09:00 | `trig_01GhNrF8nA2w2nXSfetcrHkQ` — **sigue con el prompt entero en el almacén**, pendiente de pasar al mismo esquema |
