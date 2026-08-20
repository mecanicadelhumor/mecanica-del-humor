# Redes sociales — qué hacer y qué no

**20 de agosto de 2026.** Instrucciones para dejar operativas las cuentas de marca.
Léelo entero antes de tocar nada: la mitad de este documento dice **que no hagas cosas**,
y eso también es trabajo hecho.

Cuentas creadas por Silvestre el 20 de agosto:

| Red | Cuenta | Estado |
|---|---|---|
| TikTok | `@mecanicadelhumor` | creada |
| Bluesky | `mecanicadelhumor.bsky.social` | creada |
| Instagram | — | suspendida al registrar, en revisión |

---

## 0. Lo primero: la foto de perfil

**Cámbiala en las tres cuentas por `02_marca/avatar.png`.**

La foto actual es un retrato generado de un hombre joven que no existe. Hay que
cambiarla por dos motivos, y el segundo importa más que el primero:

1. **De marca.** Nadie recuerda una cara de archivo. Todo el mundo recuerda una cabeza
   mecánica ámbar. El Engranaje ya es el personaje del canal, sale en los vídeos y en
   las miniaturas, y como avatar hace que las cuatro superficies —YouTube, TikTok,
   Bluesky, Instagram— se reconozcan como la misma cosa de un vistazo, en un icono de
   treinta píxeles.
2. **De criterio.** La regla 7 de `REGLAS.md` dice que este canal no finge que hay una
   persona detrás. Un retrato inventado como cara pública del proyecto es exactamente
   eso. El canal no necesita una cara humana: necesita una cara, y ya la tiene.

Tres versiones en `02_marca/`:

| Fichero | Cuándo |
|---|---|
| `avatar.png` | **el bueno.** Fondo ámbar, expresión de duda. Es el que más contrasta en un icono pequeño y el que mejor cuenta de qué va el canal |
| `avatar_alt_neutra.png` | si la duda resulta demasiado escéptica |
| `avatar_alt_oscuro.png` | fondo azul marino, por si alguna red recorta mal el ámbar |

Son PNG de 1080×1080. Todas las redes los recortan en círculo y la cara está centrada
con margen de sobra para eso.

**Sobre la fecha de nacimiento.** El campo de fecha de nacimiento es del titular de la
cuenta, no del personaje: la cuenta es tuya, lo que es de marca es lo que se publica. Meta
y TikTok cruzan ese dato con el teléfono y con cuentas anteriores, y una discrepancia es
una de las causas típicas de la suspensión automática que te ha saltado en Instagram.
Cuando puedas, pon tu fecha real en las tres. Es un campo privado y te evita perder las
cuentas más adelante, cuando duela.

---

## 1. Bluesky — operativa hoy, cinco minutos

Es la única de las tres que se puede automatizar hoy sin pedirle permiso a nadie, porque
su API es abierta y no hay revisión de aplicaciones.

**Lo que tienes que hacer:**

1. Entra en `bsky.app` con la cuenta de marca.
2. **Ajustes → Privacidad y seguridad → Contraseñas de aplicación → Añadir**.
3. Nómbrala `mecanica-actions`. Copia la contraseña que sale — tiene la forma
   `xxxx-xxxx-xxxx-xxxx` y **solo se ve una vez**.
4. En GitHub: repositorio → **Settings → Secrets and variables → Actions → New repository
   secret**, y crea estos dos:

   | Secreto | Valor |
   |---|---|
   | `BSKY_HANDLE` | `mecanicadelhumor.bsky.social` |
   | `BSKY_APP_PASSWORD` | la contraseña de aplicación |

Ya está. Una contraseña de aplicación **no puede cambiar la contraseña de la cuenta ni
borrarla**: para eso existen. Si algún día quieres cortar el acceso, la revocas desde esa
misma pantalla y no rompes nada más.

**Qué publicará:** un apunte al día con el hallazgo del vídeo, el enlace al estudio y el
enlace al Short. Texto útil por sí mismo, no un cebo. Nunca hilos automáticos, nunca
respuestas a nadie, nunca menciones a terceros.

---

## 2. TikTok — la dejamos parada. No hagas nada

Sé que suena raro habiendo creado la cuenta, pero publicar automáticamente en TikTok exige
darse de alta como desarrollador en `developers.tiktok.com`, crear una aplicación y pedir
la **Content Posting API** con permiso de publicación directa, que pasa por una **revisión
manual de TikTok**. Hasta que la aprueban, lo que sube una aplicación no auditada aterriza
como borrador privado en tu bandeja: tendrías que entrar cada día a darle a publicar, que
es justo el trabajo recurrente que este proyecto no quiere.

**La cuenta ya ha hecho lo importante**, que era reservar el nombre antes de que lo cogiera
otro. El resto puede esperar.

**Cuándo volvemos:** cuando los Shorts de YouTube pasen el peldaño 1 de la tabla de
métricas (5.000 impresiones por semana). Antes, montar la infraestructura de una segunda
plataforma es esfuerzo puesto en el sitio equivocado.

---

## 3. Instagram — resuelve la suspensión y luego espera

Lo mismo, y además está suspendida.

Publicar Reels por API pide una cuenta **profesional**, vinculada a una **página de
Facebook**, una aplicación en el panel de desarrolladores de Meta y el permiso
`instagram_content_publish`, que también pasa por **revisión de la aplicación**. Y el vídeo
tiene que estar colgado en una URL pública para que Meta lo descargue.

**Qué hacer ahora:**

1. Espera la revisión. Si la aprueban, cambia la foto de perfil por `avatar.png` y **no
   toques nada más**.
2. Si la rechazan, **no lo intentes con otro número de teléfono**. Registrar la misma
   cuenta con otro teléfono después de una suspensión es lo que convierte una suspensión
   temporal en una permanente, y además deja el número marcado. Usa el formulario de
   apelación de la propia suspensión, que suele resolverse en unos días.
3. Si al final no hay manera, no pasa nada. Instagram es la plataforma menos importante de
   las tres para este canal y la que más trabajo de infraestructura pide.

---

## 4. Reddit — no

Me preguntaste si te ocupabas. La respuesta es que no hay nada que ocupar, y prefiero
decirlo claro:

- **Publicar automáticamente en Reddit es spam.** Va contra las normas de prácticamente
  todos los subreddits relevantes, los moderadores lo detectan enseguida y el resultado no
  es «poco alcance»: es el dominio de tu canal baneado en los sitios donde estaría tu
  público. Es de las pocas jugadas que pueden dejarte peor que no hacer nada.
- **Participar de verdad sí funciona**, y por eso mismo no se puede automatizar: exige a
  una persona leyendo hilos y aportando algo. Es trabajo recurrente, que es lo que este
  proyecto ha decidido no tener.
- **Leer Reddit sí lo usamos, y ya está en marcha.** La tarea de planificación de los
  jueves lee `r/socialskills`, `r/standup` y `r/askspain` para saber **con qué palabras
  formula la gente sus preguntas** sobre humor. Solo lectura, sin cuenta, sin escribir
  nada. Ahí Reddit vale mucho.

Si algún día te apetece participar de verdad porque el tema te interesa, adelante — pero
como Silvestre, no como el canal, y sin que el sistema dependa de ello.

---

## Resumen

| Qué | Cuándo | Cuánto te cuesta |
|---|---|---|
| **Cambiar la foto de perfil por `avatar.png`** en TikTok y Bluesky | hoy | 2 min |
| **Crear la contraseña de aplicación de Bluesky** y meter los dos secretos en GitHub | hoy | 5 min |
| Poner tu fecha de nacimiento real en las cuentas | cuando puedas | 2 min |
| Apelar la suspensión de Instagram si la rechazan | cuando toque | 5 min |
| TikTok e Instagram automatizados | cuando los Shorts pasen el peldaño 1 | — |
| Reddit | nunca automatizado | — |

Todo lo demás lo hago yo.
