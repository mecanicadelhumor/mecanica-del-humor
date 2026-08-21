# Quién escribe qué

**21 de agosto de 2026.** Regla estructural para que dos agentes no se pisen.
Es corta y es de obligado cumplimiento para cualquier tarea programada.

---

## Lo que pasó, y por qué va a volver a pasar si no se arregla

La noche del 20 de agosto la tarea de planificación escribió los seis Shorts de
la semana, adaptó MDH-004 al formato nuevo, generó `demanda.json` y dejó 190
líneas de bitácora en `MEJORAS.md`. A las 07:00 del 21, la revisión diaria
entregó su paquete. Silvestre los aplicó en orden.

**Resultado: la revisión diaria borró la entrada entera de la planificación en
`MEJORAS.md` (188 líneas, siete secciones) y revirtió MDH-004 a la versión
anterior a la adaptación** — de 30 escenas a 28, sin `formato`, sin personaje y
sin escéptico, con el gancho de ensayo otra vez en su sitio.

No fue un error de la revisión diaria. Fue el diseño:

1. La planificación corre a las 22:00 y **entrega un `.tar.gz`**, no un commit.
2. Ese paquete no llega a GitHub hasta que Silvestre lo aplica, a la mañana
   siguiente.
3. La revisión diaria arranca a las 07:00 y clona `origin/main` — donde el
   trabajo de la noche **todavía no está**.
4. Trabaja sobre esa base, empaqueta **ficheros enteros** y los entrega.
5. Al aplicarse encima, cada fichero entero pisa la versión buena.

Mientras la entrega sea manual habrá una ventana de horas en la que un agente
trabaja sobre una base caduca. No se puede cerrar esa ventana. **Lo que sí se
puede es hacer que dos agentes no escriban nunca el mismo fichero.**

---

## La regla

**Cada fichero tiene un dueño y solo uno. Los demás no lo escriben: informan.**

| Ruta | Dueño | Los demás |
|---|---|---|
| `05_calendario/guiones/` · `parrilla.json` · `publicaciones/` · `CALENDARIO.md` · `demanda.json` · `semillas_demanda.json` | **Planificación** (jueves 22:00) | escriben en `revisiones/`, no aquí |
| `05_calendario/demanda_bruta.json` | **Workflow `demanda.yml`** (jueves 14:00) | nadie más lo toca |
| `05_calendario/metricas.json` | **Métricas** (lunes 09:00) | nadie más lo toca |
| `03_produccion/` · `04_agentes/` (código, prompts, `MEJORA_VISUAL.md`) | **Revisión diaria** | proponen en el resumen |
| `05_calendario/registro_publicaciones.json` · `qa/` | **GitHub Actions** | nadie los mete en un paquete, nunca |
| `00_estrategia/` | **Silvestre y yo** | nadie más |

### Las dos carpetas nuevas que lo hacen posible

**`05_calendario/bitacora/`** — sustituye a escribir en `MEJORAS.md`.
Cada tarea crea **un fichero nuevo** por ejecución:

    bitacora/2026-08-21-revision.md
    bitacora/2026-08-21-planificacion.md
    bitacora/2026-08-24-metricas.md

Un fichero nuevo no puede pisar nada. `MEJORAS.md` queda **congelado** como
historia hasta el 21 de agosto: se lee, no se escribe.

**`05_calendario/revisiones/`** — el buzón de la revisión diaria.
Cuando encuentra un defecto editorial en un guion, **no edita el guion**. Escribe
`revisiones/<ID>.md` con el defecto y la corrección exacta, en formato
antes/después. La planificación las aplica el jueves siguiente, cuando vuelve a
escribir esos ficheros, y borra la nota al aplicarla.

### La única excepción, y es estrecha

La revisión diaria **sí puede editar un guion** cuando ese guion se produce en
menos de 48 horas. Entonces:

- toca **ese fichero y ninguno más** del calendario,
- lo dice en la primera línea de su resumen, en mayúsculas,
- y anota en su bitácora que lo ha hecho.

Fuera de esa ventana, un defecto puede esperar al jueves. Ninguno de los que se
han encontrado hasta ahora justificaba arriesgar una semana de trabajo ajeno.

---

## Además: cómo se entrega

1. **Un paquete contiene solo ficheros de los que la tarea es dueña.** Si un
   `.tar.gz` lleva algo de otra columna de la tabla, está mal hecho.
2. **Nunca `registro_publicaciones.json` ni `qa/`.** Los escribe el bot de
   Actions y provocan conflictos de merge.
3. **La primera comprobación de cualquier tarea** es `git log --oneline -5` sobre
   `origin/main`. Si el último commit no incluye el trabajo que esperaba
   encontrar —por ejemplo, la revisión del viernes no ve el commit de la
   planificación del jueves—, **hay una entrega pendiente sin aplicar**: en ese
   caso no se toca nada del calendario y se dice en el resumen.
4. **Al empaquetar, listar los ficheros por nombre en el resumen.** Silvestre
   aplica lo que ve; si no lo ve, no puede detectar que algo sobra.

---

## Cómo se recupera si vuelve a pasar

Nada se pierde de verdad: está todo en git. La receta, con el caso del 21 como
ejemplo:

```bash
git log --oneline -8                       # localizar el commit bueno
git show <bueno>:ruta/al/fichero > ruta/al/fichero
git diff <bueno> <malo> -- ruta/al/fichero # ver qué se llevó por delante
```

Para un fichero de bitácora, extraer el bloque borrado y volver a insertarlo:

```bash
git show <bueno>:05_calendario/MEJORAS.md | sed -n '<ini>,<fin>p' > /tmp/perdido.md
```

Lo que cuesta caro no es recuperar: es **no darse cuenta**. Por eso la
comprobación 3 de arriba es la primera acción de cada tarea.
