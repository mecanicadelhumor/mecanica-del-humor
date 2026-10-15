# Dirección → las tres tareas programadas · lunes 21 de septiembre de 2026

Primera nota que la dirección deja en esta carpeta. A partir de hoy hay una después de cada
sesión de dirección (lunes y, mientras dure la fase de cambio, viernes), para que lo decidido
os llegue **el mismo día** y no cuando alguien se acuerde de reescribir vuestro prompt. La
carpeta es idea del codirector, del 18/09.

`novedades.md` es suyo. Ni la dirección ni vosotros lo tocáis.

Razonamiento completo: **versión 11 de `00_estrategia/PLAN_DE_CAMBIOS.md`**, que es la que
manda desde hoy.

---

## 1 · No hay episodios largos (C42)

**El formato largo está suspendido.** `MDH-008` está fuera de `parrilla.json` (guardado con su
motivo en `_emisiones_suspendidas`) y **su guion sigue escrito y no se toca**. La semana son
**cinco Shorts, de lunes a viernes a las 19:00, y nada el sábado ni el domingo**.

Dos motivos, y el segundo es el que os afecta a todos:

- Siete episodios largos, treinta y cuatro días, **114 visualizaciones entre todos**. Los cinco
  Shorts de la última semana: **1.533 en sus primeras 48 horas**.
- El precacheo del largo gastaba cada día **9 de las 10 peticiones de
  `gemini-2.5-flash-preview-tts`**, que desde C33.1 (15/09) es el **peldaño (b) del respaldo de
  voz de los Shorts**. La cabecera de `voz_precache.py` sigue diciendo «cuota propia, nunca la
  de los Shorts»: era verdad el 14 de septiembre y es falsa desde el 15. **Mientras hubiera un
  largo pendiente, un Short que fallara con 3.1 no tenía red.**

**Vuelve cuando `control_c26.mediana_vistas_48h` de `metricas.json` llegue a 50.** Hoy vale 11,0.

## 2 · El estado del canal se escribe en `05_calendario/estado/` (C45)

`ESTADO.md` **está congelado**: se lee, no se escribe. La revisión diaria escribe
`05_calendario/estado/AAAA-MM-DD.md`, **un fichero nuevo cada día**. El estado de hoy es el
fichero de nombre más alto de esa carpeta.

Por qué: el 19 y el 20 chocaron dos entregas sin aplicar sobre el mismo fichero. Va a pasar
todos los fines de semana mientras la entrega sea manual. Un fichero nuevo no puede pisar nada
— es la regla del 21 de agosto, que a `ESTADO.md` nunca se le aplicó.

## 3 · Para la revisión diaria: releed el registro antes de decir que falta un vídeo

El 20/09 `ESTADO.md` dio por ausente a `MDH-007`. **Estaba subido desde las 09:37:31 UTC**, y la
revisión escribió a las 09:53 sobre un clon anterior a ese commit. El tercer intento de
producción (08:23 UTC, con los retrasos de Actions) cae justo encima de vuestra ventana.
`git fetch` y releer `registro_publicaciones.json` **inmediatamente antes** de escribir el
fichero del día, y decir a qué hora se releyó.

## 4 · Para la planificación del jueves: el canal se lee a sí mismo (C46)

`05_calendario/metricas.json` entra en vuestra lectura obligatoria **antes** de elegir tema.
Los dos mejores temas de las últimas cuatro semanas tienen **derecho de tanteo**: al menos uno
de los cinco Shorts continúa uno de ellos, o se escribe en la bitácora por qué no se puede.

El motivo, con nombre: `MDS-016` («por qué la ironía no se entiende por WhatsApp») hizo **1.210
visualizaciones a 48 horas** el 14/09, con los quince anteriores en mediana 10. Una semana
después no hay **ni un vídeo que lo continúe**, y nadie lo decidió: el número no llegaba a quien
elige los temas.

Y dos correcciones a vuestro prompt, que llevaba días con datos falsos: la sección «dónde está
el canal» estaba congelada en el 7 de septiembre, y decía que la búsqueda es la única superficie
que responde. **Manda el feed**: 54,6 % contra 27,7 % de búsqueda (C40, del 18/09).

## 5 · Esta semana la voz no se toca

Los cinco Shorts del 21 al 25 son la **primera medida limpia de C38**. No metáis encima ningún
cambio de voz, de guion ni de presentación. Lo que venga entra el **lunes 28**, después del
punto de control del 27. Regla 11.1.

## 6 · Encargo para la revisión diaria: las métricas, todos los días (C47)

`metricas.yml` corre **solo los lunes**, así que un Short puede hacer 0 visualizaciones durante
seis días sin que nadie se entere. Es exactamente lo que ha pasado con `MDS-017`.

Encargo de esta semana: lectura ligera diaria en `05_calendario/metricas_diarias.json` con
**solo** `id`, `publicado`, `visualizaciones` y `vistas_48h` de los vídeos publicados en los
últimos diez días. **Sin curvas de retención** — `metricas.json` ocupa 174 KB con cinco lecturas
porque guarda 100 puntos por vídeo, y a diario eso son megas de churn en git. La lectura
completa sigue siendo semanal y no se toca. El cron lo cambia el codirector.

Cuando esté: la revisión diaria marca `INCIDENCIA` si un Short pasa de 24 horas con 0
visualizaciones.
