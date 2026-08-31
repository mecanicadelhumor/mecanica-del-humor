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

## La regla que hace falta para que esto no mienta

**La copia que se ejecuta es la del almacén.** Estos ficheros no corren. Quien
cambie un prompt tiene que hacerlo en los dos sitios: `update_trigger` con el
`trigger_id` que hay en la cabecera de cada fichero, y el fichero de aquí.

Si un día no coinciden, la del almacén es la buena — y este fichero está
desactualizado, no al revés.

## Quién los escribe

Solo Silvestre y yo (la dirección). `00_estrategia/` no lo toca ningún agente,
y estos prompts menos que nada: un agente que puede reescribir sus propias
instrucciones no tiene instrucciones.

| Fichero | Tarea | Cuándo corre |
|---|---|---|
| `revision-diaria.md` | Revisión de calidad | todos los días, 11:28 hora de España |
| `planificacion-jueves.md` | Equipo editorial | jueves, 22:00 |
| `metricas-lunes.md` | Analista | lunes, 09:00 |
