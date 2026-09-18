# Cómo terminar el trámite de la app de TikTok (Content Posting API)

**18 de septiembre de 2026.** Documento operativo, no forma parte de la cola versionada de
`PLAN_DE_CAMBIOS.md`: es el detalle de cómo completar el trámite que **C41** abrió hoy mismo.
Se lee junto a la Tarea 2 de `tareas/tareas_codirector_2026-09-18.md`, que este documento
corrige en un punto y amplía en el resto.

---

## Qué ha pasado hoy

El codirector ha empezado a rellenar la app en `developers.tiktok.com` y ha llegado a la
pantalla de **App Review**, que pide más de lo que la Tarea 2 tenía previsto. Dos cosas quedan
resueltas ya:

- **La organización/cuenta de desarrollador está creada.** Paso 1 de la Tarea 2, cumplido.
- **El icono de la app.** TikTok exige uno de 1024×1024. Se ha generado
  `02_marca/icono_app_tiktok_1024.png` a partir de `avatar.png` (que estaba en 1080×1080,
  reescalado con calidad). Listo para subir.

Lo que queda por resolver es lo que sigue.

---

## Lo que pide la pantalla de App Review, tal cual

1. Un texto (máx. 1000 caracteres) explicando cómo funciona cada producto y scope dentro de
   la app.
2. **Al menos un vídeo demo** (mp4/mov, máx. 50 MB, hasta 5 ficheros) que muestre el **flujo
   completo de principio a fin** de la integración: login, y el uso real de los productos y
   scopes pedidos. Tiene que enseñarse la interfaz y la interacción de usuario, no solo
   describirse.
3. **Como la app nunca ha sido aprobada antes, el vídeo tiene que grabarse contra el entorno
   sandbox** del Developer Portal, no contra producción.
4. Dos pestañas más, **Products** y **Scopes**, que fijan qué se pide exactamente.

## Por qué no se puede enviar todavía

El vídeo del punto 2 exige que la integración **ya funcione**, aunque sea en sandbox: no hay
nada que grabar sin un cliente que haga de verdad la llamada a `video.upload` y `video.publish`.
Eso choca con lo que la propia Tarea 2 decía en su punto final:

> *"no escribas nada de código, no configures ningún workflow y no me pidas que escriba el
> cliente de la API todavía"*

y con el paso 6 de esa misma tarea, que pedía mandar la app a auditoría sin haber escrito ese
cliente. Esa secuencia no es viable: **se escribió pensando que la auditoría se pedía sin
demostrar nada, y la pantalla de App Review demuestra que no es así.**

## Qué queda de la Tarea 2 y qué no

| De la Tarea 2 (`tareas_codirector_2026-09-18.md`) | Queda así |
|---|---|
| Paso 1 · crear cuenta de desarrollador | **Hecho.** No se repite. |
| Pasos 2-5 · crear la app, añadir Content Posting API, pedir `video.upload` + `video.publish`, verificar dominio | **Se mantienen tal cual.** Siguen siendo el camino correcto. |
| Paso 6 · mandar la app a auditoría, sin más | **Anulado tal como estaba escrito.** No se puede mandar sin el vídeo demo, y el vídeo demo exige el cliente mínimo que este documento añade a continuación. |
| «No escribas nada de código […] todavía» | **Se amplía, no se anula del todo.** Sigue sin tener sentido escribir el cliente completo de producción (`publicar_redes.py`, el paso en `producir.yml`) antes de saber si aprueban la app — ese trabajo se sigue tirando a la basura si rechazan. Lo que sí hace falta ya es un **script mínimo de sandbox**, que no es ese cliente: es solo lo justo para grabar el vídeo. |
| `PLAN_DE_CAMBIOS.md` **C41** | Sigue vigente sin tocarlo. Este documento es el desglose operativo de su último tramo, el que dice «cuando el trámite esté». |
| `REDES.md` | Sin cambios. |

---

## El orden correcto, de aquí al envío

1. ~~Crear la cuenta de desarrollador~~ — **hecho**.
2. Crear la app en el portal: nombre «Mecánica del Humor», descripción «publicación automática
   de los vídeos cortos propios del canal Mecánica del Humor».
3. Añadir el producto **Content Posting API**.
4. En **Scopes**, pedir `video.upload` **y** `video.publish` — los dos marcados. **No dejar esta
   pestaña ni la de Products en blanco**: si se dejan vacías no hay nada que TikTok revise.
5. Verificar el dominio con el mismo procedimiento que ya se usó para el OAuth de YouTube en
   septiembre (el de `docs/`).
6. Subir `02_marca/icono_app_tiktok_1024.png` como icono de la app.
7. Activar el **entorno sandbox** en el Developer Portal, con la propia cuenta de TikTok de la
   marca como usuario de prueba.
8. **Decisión pendiente de dirección** (ver más abajo): autorizar un script mínimo, solo de
   sandbox, que haga el login/OAuth y llame a `video.upload` y `video.publish` una vez, con
   algo de interfaz visible — no hace falta que sea bonito, pero TikTok pide ver «la interfaz y
   las interacciones», así que un terminal pelado puede no bastar; una página mínima local o un
   cliente de API con interfaz (Postman con su UI, por ejemplo) sí sirve.
9. Grabar el vídeo demo de ese flujo completo contra el sandbox.
10. Escribir el texto de hasta 1000 caracteres explicando el uso del Content Posting API y de
    los dos scopes.
11. Adjuntar vídeo + texto, revisar que Products y Scopes reflejan exactamente lo pedido en el
    punto 3-4, y enviar la app a auditoría.
12. Anotar la fecha de envío en `REDES.md` o en la bitácora del día. La espera (días a semanas)
    no bloquea nada más del proyecto: sigue corriendo sola mientras se trabaja en C38.

## Lo que la dirección tiene que decidir

**Autorizar ya el script mínimo de sandbox del punto 8**, adelantándolo respecto al plan
original que lo aplazaba todo hasta tener la app aprobada. La alternativa es dejar el trámite a
medias — app creada, producto y scopes pedidos, dominio verificado, pero sin enviar a
auditoría — hasta que C38 dé su primera medida el 27 de septiembre, tal y como decía el plan
inicial de C41.

**El riesgo de escribirlo ya:** si TikTok rechaza la app por otro motivo (redacción de la
pantalla de consentimiento, por ejemplo, que el propio `PLAN_DE_CAMBIOS.md` señala como el
motivo típico de rechazo), ese script mínimo sobrevive igual — es tan pequeño que no hay mucho
que tirar. El riesgo real no es escribirlo, es escribir de más: el cliente completo de
producción (`publicar_redes.py`, el paso en `producir.yml`) sigue esperando a que la
aprobación llegue, y ese sí se descarta si no llega.
