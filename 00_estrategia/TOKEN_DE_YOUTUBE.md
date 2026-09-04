# El token de YouTube — por qué caducaba y cómo no volver a pasar por aquí

**4 de septiembre de 2026.** Escrito porque el 1 de septiembre el canal no
publicó, la causa tardó una mañana en encontrarse y no había nada escrito sobre
dónde se toca esto. Son quince minutos, una sola vez.

---

## Qué pasaba, en dos frases

El sistema sube los vídeos con un **token de actualización** (`YT_REFRESH_TOKEN`)
guardado como secreto del repositorio. Ese token permite pedir permisos nuevos
sin que nadie abra un navegador — es lo que hace que el canal vuele solo.

Una aplicación de OAuth cuya **pantalla de consentimiento está en modo
«Prueba»** recibe tokens que **caducan a los siete días**. No es un fallo: es lo
que Google documenta para ese modo. Con la aplicación en «Prueba», el canal se
para solo cada semana.

---

## Las dos cosas que se confunden siempre, y es lo único que hay que entender

|  | Qué es | ¿Nos hace falta? |
|---|---|---|
| **Publicar** la aplicación | Un botón. Pasa el estado de «Prueba» a «En producción». **Con eso el token deja de caducar.** | **Sí, y es todo lo que hay que hacer** |
| **Verificar** la aplicación | Un formulario que pide página web, política de privacidad, términos de servicio y un vídeo de demostración | **No.** Solo hace falta para pasar de 100 usuarios o para quitar la pantalla de aviso |

Es decir: **se puede publicar sin verificar.** Lo que se paga por no verificar:

- Una pantalla de «Google no ha verificado esta aplicación» al dar el
  consentimiento. Sale **una vez**, y se pasa por *Configuración avanzada → Ir a
  Mecánica del Humor (no seguro)*.
- Un tope de **100 usuarios** durante toda la vida de la aplicación. Nosotros
  necesitamos **uno**: la cuenta de marca del canal.

Nada de lo que hay que rellenar exige inventarse un dato.

---

## Parte A · Publicar la aplicación (una vez, 5 minutos)

1. Entra en **https://console.cloud.google.com/auth/audience** con la cuenta
   que creó el proyecto.
   *Si el enlace directo no te lleva:* menú ☰ → **APIs y servicios** →
   **Pantalla de consentimiento de OAuth**. Google la renombró a **Google Auth
   Platform**, y dentro está el apartado **Audiencia**.
2. Arriba a la izquierda, **comprueba que el proyecto seleccionado es el del
   canal** — el mismo que tiene habilitada *YouTube Data API v3*. Si tienes
   varios proyectos, este es el error fácil de cometer.
3. En **Estado de publicación** verás **«Prueba»** y, debajo, la lista de
   usuarios de prueba.
4. Pulsa **PUBLICAR APLICACIÓN**.
5. Sale un aviso diciendo que la aplicación estará disponible para cualquier
   usuario y que los ámbitos sensibles necesitan verificación. **Confirma.**
6. El estado pasa a **«En producción»**. Aparecerá algo como *«Verificación: no
   iniciada»* o un botón *«Preparar para la verificación»*: **no lo toques.**
   Ese es el formulario que pide la web y la política de privacidad, y no hace
   falta.

Con esto ya está resuelto lo que se rompió el día 1. **Pero el token que tienes
ahora sigue siendo de la época de «Prueba» y sigue caducando**, así que hay que
sacar uno nuevo.

---

## Parte B · Sacar un token nuevo (5 minutos)

Hay un script para esto en el repositorio desde hace semanas:
`04_agentes/obtener_token_youtube.py`. Pide los tres ámbitos correctos —subir,
miniaturas y subtítulos, y analítica— así que no hay que acordarse de nada.

Necesitas el **ID de cliente** y el **secreto de cliente**, que son los mismos
que ya están en los secretos del repositorio (`YT_CLIENT_ID` y
`YT_CLIENT_SECRET`). Si no los tienes a mano, están en
**https://console.cloud.google.com/apis/credentials**, en *ID de clientes de
OAuth 2.0*.

En una terminal, dentro de `C:\MisProyectos\Humor`:

```
pip install google-auth-oauthlib
python 04_agentes/obtener_token_youtube.py --client-id XXXX --client-secret YYYY
```

Lo que pasa entonces:

1. Se abre el navegador.
2. **Elige la cuenta de marca de Mecánica del Humor**, no tu cuenta personal.
   Este es el otro error fácil: un token de la cuenta equivocada falla al subir
   con un error que no dice eso.
3. Sale la pantalla de **«Google no ha verificado esta aplicación»**. Es la
   esperada. *Configuración avanzada* → *Ir a … (no seguro)*.
4. Acepta los tres permisos.
5. La terminal imprime el token entre dos líneas de `====`.

---

## Parte C · Guardarlo en GitHub (1 minuto)

En el repositorio: **Settings → Secrets and variables → Actions →
`YT_REFRESH_TOKEN` → Update**. Pega el token y guarda.

> **Ojo al orden.** Al reautorizar, Google invalida el token anterior de ese
> cliente y esa cuenta. Entre que sacas el nuevo y lo pegas en GitHub, el
> sistema no puede subir. Hazlo seguido, y mejor por la mañana: la producción
> corre de madrugada.

---

## Parte D · Comprobar que ha funcionado (al día siguiente)

Dos comprobaciones, y las dos las hace la revisión diaria sola a las 11:30:

1. **Que subió.** `05_calendario/registro_publicaciones.json` tiene la entrada
   del día. Si `ESTADO.md` dice `OK`, subió.
2. **Y una que solo hace falta esta vez.** Publicar la aplicación no debería
   cambiar nada en cómo se suben los vídeos, pero conviene mirarlo con el
   primero: la entrada del día tiene que seguir diciendo `"estado": "private"`
   con un `"publicar_en"`, igual que siempre, y el vídeo tiene que hacerse
   público solo a las 19:00.

   *Por qué se mira:* la documentación de YouTube dice que los vídeos subidos
   por `videos.insert` desde proyectos de API sin auditar quedan restringidos a
   privado. **Empíricamente no nos pasa** —los nueve vídeos del canal se
   publican solos— y la auditoría es un eje distinto del estado de la pantalla
   de consentimiento, así que no debería cambiar. Pero es razonamiento, no
   medición. Si el vídeo del lunes 7 se quedara bloqueado en privado, se vuelve
   a «Prueba» desde la misma página de la Parte A y estamos como antes.

---

## Si el canal vuelve a dejar de publicar

Con la aplicación ya en producción, el token **no caduca por tiempo**. Puede
dejar de valer por estas otras razones, y se distinguen por lo que dice el log
del paso «Subir a YouTube» del workflow `producir.yml`:

| Lo que dice el error | Qué ha pasado | Qué hacer |
|---|---|---|
| `invalid_grant` · *Token has been expired or revoked* | Alguien revocó el acceso en la cuenta, o se sacó otro token para el mismo cliente y cuenta | Repetir las partes B y C |
| `quotaExceeded` | Se agotaron las 10.000 unidades diarias de la API. Una subida cuesta 1.600 | Esperar al día siguiente. Si se repite, revisar cuánto gasta `explorador_de_demanda.py` |
| `forbidden` · miniatura | Falta verificar el teléfono del canal | `youtube.com/verify` |
| No hay error, no hay entrada | El cron no llegó a correr | Mirar la pestaña *Actions* |

Y si no está claro: **el token de actualización no se usa en ningún sitio más
que en los secretos del repositorio.** Rehacer las partes B y C nunca rompe
nada, así que ante la duda, se rehace.

---

## Lo que no funciona, para no volver a intentarlo

- **Cuenta de servicio.** YouTube no acepta cuentas de servicio para subir a un
  canal. No hay forma de quitar al humano del bucle por esa vía.
- **Renovar el token con un workflow automático.** Google no emite un token de
  actualización nuevo cuando usas el que tienes, así que no hay nada que rotar
  sin pasar otra vez por el navegador. Por eso la única solución de verdad era
  quitar la caducidad, no automatizar la renovación.
- **Cambiar el tipo de usuario a «Interno».** Requiere Google Workspace, y la
  cuenta es de Gmail.
