# Reglas de producción · lo que sabemos que hace un Short que funciona

**Creado el 08/10/2026 por la dirección** (punto 2 del cuaderno del codirector, 06/10). Es un
fichero **vivo**: las reglas entran, se prueban y salen. Lo escribe la dirección y nadie más
(`entregar.py` lo deja de la dirección, como `bucle/`). Las demás tareas **lo leen** y lo cumplen.

> **Cómo se usa.** Cada Short sigue **todas** las reglas vigentes de este fichero a rajatabla, **más
> una sola modificación**: añadir algo, quitar o saltarse una regla, o cambiar una por otra. Esa
> modificación es el brazo del ciclo del bucle (`05_calendario/bucle/ciclos.json`). El brazo
> `control` es el Short con **cero** modificaciones: es la medida de lo que valen las reglas tal
> cual. Así se construye una estrategia ganadora poco a poco, como se aprende una apertura de
> ajedrez: una variación cada vez, contra la línea principal.

## Cómo se mueve una regla

```
IDEA ──► EN COLA ──► EN PRUEBA ──► VIGENTE
 (cualquier agente   (hipotesis.json,   (un brazo del ciclo   (el bucle dijo GANA o
  la sugiere)         la dirección       en curso)             el codirector la fijó)
                      decide el orden)                          │
                                          PIERDE / SIN EFECTO ──► RETIRADA (con el motivo)
```

1. **Cualquier agente puede sugerir una hipótesis** (en su bitácora o en `08_comunicacion/`); **solo
   la dirección** decide cuál se prueba y en qué orden. La decisión y la responsabilidad son suyas
   (el codirector, en su defecto).
2. **Una hipótesis cambia una cosa**, y dice qué regla toca (`regla_afectada` en `hipotesis.json`),
   qué métrica la decide y qué resultado la confirma o la descarta **antes** de ver ningún dato.
3. **Una prueba es un brazo del ciclo**, medida con «Se quedaron viendo» a 48 horas y decidida por la
   regla escrita en `04_agentes/bucle.py` (+8 puntos con 6 Shorts por brazo, +15 con 4; sin efecto con
   10). **Nunca se cambia una regla de decisión con los datos delante**: se cambia para el ciclo
   siguiente y se dice.
4. **Si gana**, la modificación pasa a ser una regla vigente (o sustituye a la que cambió) y el ciclo
   siguiente la tiene en el control. **Si pierde o no tiene efecto**, se retira y queda aquí, en
   «Reglas retiradas», con el motivo: lo que no funcionó también es conocimiento.
5. **Una excepción solo vale si la anota un brazo**: nadie salta una regla «porque este Short lo pide»
   (eso es medir el criterio del que escribe, no el cambio).
6. **Las reglas de fondo no se juegan.** La ética, la verdad y la licencia (`REGLAS.md`, 1, 2, 7, 8, 9,
   13.3 y 14) **no son reglas de producción**: no se prueban, no se saltan en ningún brazo.

## Estado de hoy, 08/10/2026

Ciclo vigente: **B1** (12-25/10). Brazos: **control** (todo lo de abajo, sin tocar), **A**
(animación a medida en las escenas de mecanismo, regla R-IM-04 sustituida) y **B** (arranque con el
dato, regla R-GU-01 sustituida). Cola: ver `05_calendario/bucle/hipotesis.json`.

## Las reglas vigentes (la línea principal)

`Origen` = dónde se decidió. `Evidencia` = lo que la sostiene hoy: **medida** (un ciclo del bucle o
una comparación con datos), **editorial** (decisión de la dirección o del codirector, sin medir) o
**heredada** (venía del diagnóstico inicial). **Casi todo es editorial o heredado**: el bucle acaba de
empezar, y por eso este fichero existe.

### Guion

| ID | Regla | Origen | Evidencia |
|---|---|---|---|
| R-GU-01 | **La escena 1 abre con la situación o el chiste que el estudio explica**, en el segundo cero, nunca con una definición ni una presentación | Diagnóstico (08/2026); `planificacion-jueves.md` | Heredada. **A prueba en el brazo B** (abrir con el dato) |
| R-GU-02 | **El remate cae después del segundo 10** y se prepara con una pausa de 1,2-1,5 s justo antes (no después del planteamiento entero) | REGLAS.md 13.2 (18/09) | Editorial: la curva de retención dice que la mitad se va hacia el 13 |
| R-GU-03 | **3-8 escenas, 18-55 s, ninguna escena de más de 12 s** | `planificacion-jueves.md` | Heredada. **Ojo:** 19 de los 30 Shorts publicados pasan de los 45 s; `H-duracion` (≤ 40 s) está en la cola |
| R-GU-04 | **La historia primero**: pregunta, respuesta y puente en una frase cada una antes de escribir escenas; el chiste es el fenómeno | C48 (23/09) | Editorial |
| R-GU-05 | **Un «pero» o un «por eso» entre cada dos escenas seguidas**; frases enteras; el cierre se entiende solo | C48 | Editorial |
| R-GU-06 | **Lectura en frío con un subagente que no conoce el guion** (hasta tres vueltas; si no pasa, se cambia de tema) | C48 | Editorial: ha parado guiones rotos |
| R-GU-07 | **El cierre dice dónde falla el asunto** (no la bibliografía) y añade algo que el espectador no sabía | REGLAS.md 12; C48.1 (25/09) | Editorial |
| R-GU-08 | **El personaje reacciona después del remate**, no antes | `planificacion-jueves.md` | Heredada |
| R-GU-09 | **Una ficha de bibliografía no es la fuente central dos veces en seis semanas** | C17 (31/08) | Editorial |
| R-GU-10 | **La pregunta del título se contesta en el vídeo** y la tesis cabe en una frase | C48 (`historia`) | Editorial |

### Imagen

| ID | Regla | Origen | Evidencia |
|---|---|---|---|
| R-IM-01 | **Vídeo de archivo detrás del texto** en las escenas de situación; tarjeta de marca solo donde no hay plano | C50 (23/09) | Editorial (petición del codirector del 14/09: «mucha más densidad de estímulos»). Sin medir |
| R-IM-02 | **Nunca pantalla negra**; la firma de marca al final | C58 (02/10) | Editorial |
| R-IM-03 | **Lo que se ve está sostenido por lo que se oye** y al revés (se ve mudo, se oye a ciegas) | REGLAS.md 14 | Editorial; no se juega |
| R-IM-04 | **Las escenas de mecanismo salen como el resto** (archivo o tarjeta con texto) | C50 | **A prueba en el brazo A** (animación a medida) |
| R-IM-05 | **El Engranaje (personaje) con la cara que concuerda con la frase**: `duda` y `no` solo donde algo falla | REGLAS.md 14.3 | Editorial |
| R-IM-06 | **La barrera de texto (C21)**: nada que no quepa en su caja ni en la zona segura de la interfaz | C21 | Mecánica: ha impedido publicaciones rotas |

### Voz y sonido

| ID | Regla | Origen | Evidencia |
|---|---|---|---|
| R-VO-01 | **Una sola voz por vídeo** (Gemini 3.1, escalera a 2.5 y al final `edge`) | C33.1 (15/09) | Editorial: `MDS-017` salió con dos voces |
| R-VO-02 | **Sin silencio de entrada** (0,10 s de colchón; el silencio de la toma se recorta) | C58, C58.1 | Editorial |
| R-VO-03 | **Música de la rueda, y el vídeo normalizado a −14 LUFS** | `montaje.py` | Heredada |
| R-VO-04 | **La voz dice lo que pone el guion**, palabra por palabra | `qa.py` | Mecánica |

### Envoltorio (lo que ve el feed antes y después del vídeo)

| ID | Regla | Origen | Evidencia |
|---|---|---|---|
| R-EN-01 | **El título es la pregunta**, corto (C56) | C56 (02/10) | Editorial. Ojo: `MDS-016`, el mejor, no era una pregunta (ver `ANALISIS_MDS-016.md`) |
| R-EN-02 | **Pregunta al espectador como primer comentario**, fijada | C57 | Editorial. Aún sin respuestas: 0 comentarios en los 30 Shorts medidos |
| R-EN-03 | **Remate de marca «Síguenos»**, fijo y sin voz | C59 | Editorial |
| R-EN-04 | **Un Short por día a las 19:00 (hora de España)**; siete a la semana desde el 12/10 | C60 | Editorial |

### Tema (qué se elige)

| ID | Regla | Origen | Evidencia |
|---|---|---|---|
| R-TE-01 | **La demanda elige la pregunta; la bibliografía decide si se puede responder** | REGLAS.md 3 | Heredada. **Ojo:** la demanda y las vistas correlacionan 0,17 en los 12 Shorts de los que hay dato (08/10) |
| R-TE-02 | **Los dos mejores temas de las últimas cuatro semanas tienen derecho de tanteo** | C46 (21/09) | Editorial |
| R-TE-03 | **Dos de los siete Shorts de la semana son de la familia `mensajes`** (mientras haya fuente real) | `ANALISIS_MDS-016.md` (08/10) | **Exploración**, no regla: se mide con `familia_tema`. Caduca el 22/11 si no hay efecto |

## Lo que se sabe y no es una regla: los hallazgos

Cosas medidas que condicionan las reglas pero que no se «cumplen» en cada Short.

- **El feed manda** (54,6 % del tráfico; 97,8 % en `MDS-016`) y se le convence con la proporción que
  no desliza, no con distribución (C38, C40).
- **La retención no explica el alcance de `MDS-016`** (la peor curva de los Shorts con más de 60
  vistas): el feed no lo premió por verse entero (`ANALISIS_MDS-016.md`).
- **Ni la miniatura, ni la hora, ni la música, ni la voz, ni la duración** distinguen a `MDS-016`
  (ver `ANALISIS_MDS-016.md`, §2). **Sí lo hace el tema (mensajes) y, compartido con `MDS-022`, el chiste de
  literalismo.**
- **«Sin cara» no es el techo; «sin identidad», sí.** Kurzgesagt (25,7 M) no tiene cara pero tiene la
  misma voz desde 2013, un estilo que se reconoce en un fotograma y mascotas; PsychToons (163 K) crece
  con ilustración IA en un solo estilo como mero acompañante de la voz (`REFERENTES_2026-10-08.md`).
- **Los números semanales se mueven solos**: la mediana semanal fue 113 → 66 → 62 sin cambios
  nuestros. Por eso el control va dentro del mismo ciclo.

## Reglas retiradas

*(Ninguna todavía. Aquí van con la fecha, el ciclo que las midió, el resultado y la razón.)*

## Registro de cambios (solo se añade al final)

| Fecha | Cambio | Quién | Por qué |
|---|---|---|---|
| 08/10/2026 | Fichero creado con las reglas de hoy; R-TE-03 como exploración | Dirección (diferido) | Cuaderno del 06/10, punto 2 |
| 08/10/2026 | Hallazgo «sin cara no es el techo» y `H-ilustracion-ia` en cola | Dirección (diferido) | Cuaderno del 08/10, punto 3 |
