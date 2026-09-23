# Dirección → las tres tareas programadas · miércoles 23 de septiembre de 2026

Sesión extraordinaria: el codirector la ha pedido porque **tres Shorts seguidos (21, 22 y 23)
han salido con guiones sin hilo**, y porque la presentación necesita un giro grande. El
razonamiento completo va en la **versión 12 de `00_estrategia/PLAN_DE_CAMBIOS.md`**, que manda
desde hoy (C48, C49 y C50). Esta nota llega en el primer `push` del día, el de los guiones; la
versión 12 puede llegar en un segundo `push` por la tarde. Lo que necesitáis para trabajar hoy
está entero aquí y en los tres prompts, que ya van actualizados.

`novedades.md` es del codirector. Ni la dirección ni vosotros lo tocáis.

---

## 1 · SE ANULA el punto 5 de la nota del 21/09 («esta semana no se toca guion»)

Esa congelación era para medir C38 limpio. **Medir con guiones que no se entienden no mide nada**,
y el codirector lo ha visto tres días seguidos. Queda anulada entera: desde hoy los guiones
pendientes se corrigen en cuanto se ve el defecto. Voz y presentación siguen como estaban
(C44 entra el lunes 28), salvo el arreglo de una línea en `escena.html` que se cuenta abajo.

## 2 · MDS-023, MDS-024 y MDS-025 los ha reescrito la dirección hoy. No los toquéis

- **MDS-023** se vuelve a producir **hoy**: la subida de madrugada (`X1GAp3OUgKg`) la borra el
  codirector en Studio, y la emisión del 23/09 lleva `rehacer_video_id`. El siguiente intento de
  cron de hoy (el de las 04:47 o el de las 08:23 UTC, que llegan con retraso) lo produce solo.
  **Hay una segunda emisión de MDS-023 el sábado 26 como red de seguridad**: si hoy sale bien,
  el sábado `cola.py` dice «nada que producir» y es lo esperado. No es un error de parrilla.
- **MDS-024** (jueves) y **MDS-025** (viernes) salen en su día, con el guion nuevo.
- **Revisión diaria:** si encuentras algo en estos tres, **no los edites**, ni con la excepción
  de las 48 horas. Escríbelo en `revisiones/<ID>.md` y en la primera línea de tu fichero de
  `estado/`. Los ha escrito la dirección esta mañana con el codirector delante.

## 3 · Lo que ha cambiado en `validar_guion.py` (C48)

- **La duración de la serie ±12 % deja de ser ERROR** y pasa a AVISO. El techo de 55 s sigue
  siendo ERROR. Motivo: para caber en la serie, los guiones de esta semana perdieron justo las
  frases que cosían una escena con la siguiente.
- **El remate antes del segundo 10 deja de ser ERROR** y pasa a AVISO.
- **Nuevo ERROR desde MDS-026:** todo Short lleva dos campos, `historia` (pregunta, respuesta,
  puente) y `lectura_en_frio` (lo que contestó un lector que solo vio las narraciones y los
  textos de pantalla, con `veredicto: "pasa"`). Sin ellos no se produce. Cómo se hace, en
  `04_agentes/prompts/guionista_corto.md`, sección «La lectura en frío».

## 4 · Para la planificación del jueves 24: lee el guionista entero, ha cambiado lo primero

`04_agentes/prompts/guionista_corto.md` tiene una sección nueva al principio, **«La historia»**,
que manda sobre todo lo demás. Resumen para que no se te pase: un Short es **una pregunta, una
respuesta y un puente**; el chiste de la apertura **es** el fenómeno que explica el estudio, no
una anécdota aparte; cada escena se une a la anterior con «pero» o «por eso», nunca con «y
además»; ningún cierre con una frase que haya que descifrar; y **ningún Short se entrega sin
lectura en frío**. Tu prompt (`planificacion-jueves.md`) está actualizado en el paso 2.

## 5 · Para la revisión diaria, desde HOY: la lectura en frío del Short de mañana

Antes que cualquier otra cosa del paso 1, **cada día**: coge el Short que se produce en la
próxima madrugada, pásale **solo** sus `narracion` y sus textos de pantalla, en orden, a un
subagente sin más contexto (herramienta Agent), y pídele que conteste las cinco preguntas de
`guionista_corto.md` («La lectura en frío»). Si no entiende una frase, o si lo que cuenta que
dice el vídeo no se parece a la `tesis`, **es INCIDENCIA** en tu fichero de `estado/`, con la
frase exacta. Desde MDS-026, además, lo arreglas con la excepción de las 48 horas y vuelves a
pasar la lectura con un lector nuevo. (Hoy y mañana no: los tres de esta semana son de la
dirección, punto 2.)

## 6 · `sincroniza_registro.yml` funciona. No era una avería

La nota del 22/09 decía que podía no estar corrigiendo el registro. **Sí lo corrige**: el commit
`77d6c7a` del 22/09 a las 13:41 UTC pasó `MDS-021` de `private` a `public`. Lo que pasa es que el
cron de las 08:50 UTC llega con cuatro o cinco horas de retraso, y la revisión lee a las 09:30:
**lee siempre antes de que haya corrido la sincronización de ese día**. Es la trampa 14 (quien lee
tiene que contar desde el último reintento de quien escribe). Un vídeo que se publicó ayer a las
19:00 aparecerá como `private` en tu lectura de hoy y se corregirá por la tarde: **eso no es
incidencia**. Sí lo es si pasan **dos días** sin un commit «registro: sincronizado» habiendo
algo que corregir.

## 7 · Un arreglo pequeño en `escena.html`, visto al comprobar MDS-025

`contar()` pintaba los decimales con punto («43.6») porque `toFixed()` siempre pone punto. Ahora
respeta la coma del guion. Solo afecta a cifras con decimales; la barrera de C21 pasa en las 18
escenas de la semana, medida con las tipografías de marca instaladas.

## 8 · Lo que viene: la presentación cambia de verdad (C50)

El codirector pide un giro de 180° en la imagen: fotos y vídeo reales, o generados, en lugar de
texto sobre fondo azul. La dirección lo está preparando hoy y el plan está en la versión 12.
**Nadie toca la presentación por su cuenta** mientras tanto: se diseña, se prueba en
`07_pruebas/` y entra cuando el codirector lo haya visto.
