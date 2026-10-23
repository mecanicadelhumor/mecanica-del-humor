# Muestrario del personaje 3D (VRoid) · 23/10/2026

**C61, el camino 3D.** Es el avatar que hizo el codirector el 13/10 (`../avatar.vrm`, VRM 1.0), animado
sin nadie delante y con la voz de `MDS-045`: los primeros 14 s de `07_pruebas/c36-2026-10-22/c36.mp3`, la
toma única que ya oyó. **El modelo no se ha tocado** (sus condiciones: uso comercial individual, sin
redistribución ni alteración). Solo se le mueven los huesos y las expresiones que trae.

Este muestrario estaba previsto para el 16/10 y no se hizo. Fallo de la dirección, contado en el fichero
de tareas del codirector.

## Qué hay que mirar (2 minutos)

| Fichero | Qué es |
|---|---|
| **`retrato_1080x1920.mp4`** (14 s) | El personaje a pantalla completa, de pecho para arriba, hablando. Es el formato de un presentador que lleva una escena entera |
| **`puntual_1080x1920.mp4`** (14 s) | Un **momento puntual**: el titular arriba («Cena de empresa.») y el personaje en la mitad de abajo, como entraría dos o tres segundos dentro de un Short (regla 7.1.5, adaptada) |
| `retrato_fotograma.png` · `puntual_fotograma.png` | Un fotograma de cada uno (segundo 3,2) |

La pregunta para el codirector: **¿este personaje, así animado, merece ser un brazo del experimento (B3)?**
Sí, no, o sí con cambios (pelo, ropa, encuadre, cuánto se mueve).

## Cómo está hecho

- **Render**: `three.js` 0.169 y `@pixiv/three-vrm` 3.1.4 (MIT las dos), en el Chromium sin pantalla
  de siempre, con WebGL por software (SwiftShader). Sin GPU, sin cuota y sin internet durante el render.
- **La boca** (`boca.mjs`) sale **del audio**: la energía de cada fotograma decide cuánto se abre, y lo
  brillante del sonido (cruces por cero) decide la vocal VRM (`ou`/`oh` graves, `aa` medias, `ee`/`ih`
  agudas; las eses casi cierran la boca). Con ataque rápido y caída lenta, para que no tiemble.
  Determinista: el mismo audio da la misma boca (regla 11.5).
- **Los ojos**: parpadeos con un calendario fijo (cada 3-4 s). **La cabeza**: un balanceo lento y un
  asentimiento leve que sigue a la voz. Respiración en el pecho. Una sonrisa leve fija (`happy` 0,18).
- **La ropa** tiene huesos de muelle: se asientan 3 s antes del primer fotograma (si no, las mangas
  salían disparadas).
- **Fondo**: el azul de la marca `#16213A` con un halo más claro detrás de la cabeza (retrato) o una
  franja algo más clara (puntual), **porque la camiseta del avatar es del mismo azul que el fondo** y sin
  eso el cuerpo desaparece.

## Cuánto cuesta (el dato que importa para Actions)

Medido en este contenedor, sin GPU:

| Formato | Tiempo por fotograma | Por segundo de vídeo (25 fps) |
|---|---|---|
| 1080×1920 (retrato) | 1,44 s | **~36 s** |
| 540×960 (puntual, luego escalado) | 0,30 s | **~8 s** |

Un momento puntual de 3 s cuesta unos 25 s de render: nada. Un presentador que hablase el Short entero
(45 s) a resolución completa serían ~27 min, lo que es demasiado para cada producción. Para eso, mejor
renderizar a 540×960 y escalar (~6 min).

## Lo que falla o falta (dicho antes de que lo diga nadie)

- **La boca no es sincronía labial de verdad.** Sigue a la energía y al timbre, no a los fonemas: abre y
  cierra en su sitio, pero una «m» no siempre cierra los labios. Lo siguiente sería sacar las palabras
  con Whisper (ya lo usa `voz.py`) y los visemas del texto, que en español se escribe como se pronuncia.
  En este contenedor no está instalado faster-whisper, así que no se ha probado.
- **Los brazos están quietos**, colgando. Un presentador de verdad gesticula con las manos; eso necesita
  poses por papel de escena (el remate, quieto; la cifra, una mano).
- **El estilo es anime**, como avisaba el plan del 05/10. Es lo que da VRoid.
- **La camiseta se funde con el fondo** de la marca (arriba). Si el personaje entra, o se cambia el
  color de la camiseta en VRoid (eso sí lo puede hacer el autor), o se le pone siempre un fondo más claro.
- No está integrado en `render.py`: es una prueba aparte, como pide la regla 11.2.

## Cómo repetirlo

En una carpeta de trabajo **fuera del repositorio**:

    npm i three@0.169.0 @pixiv/three-vrm@3.1.4 playwright-core@1.48.2   # PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
    cp <esta carpeta>/{escena_vrm.html,render_vrm.mjs} . && ln -s <repo>/07_pruebas/personaje-2026-10/avatar.vrm .
    node <esta carpeta>/boca.mjs <repo>/07_pruebas/c36-2026-10-22/c36.mp3 14 25 > boca.json
    node render_vrm.mjs retrato 1080 1920 350 f_retrato
    node render_vrm.mjs puntual 540 960 350 f_puntual
    <esta carpeta>/montar.sh . <esta carpeta>

`render_vrm.mjs` usa `/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`, o el
binario de la variable `CHROMIUM`.

## Los vídeos en el repositorio

`.gitignore` deja fuera los `.mp4` de `07_pruebas/` por tamaño. Para que el codirector pueda verlo desde GitHub van, como excepción (añadidos con `git add -f`), las copias ligeras `*_540.mp4` (540×960, el mismo contenido con su audio). Los originales a 1080×1920 se regeneran con los scripts de esta carpeta.
