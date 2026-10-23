# Personaje 2D · muestrario (C61, camino 2D) · 23/10/2026

Debía estar el 12/10 y no se hizo. Este es el muestrario del **personaje 2D propio**: un presentador
vectorial (SVG) dibujado para la marca, animado sin nadie delante a partir del guion y de la voz.

## Qué hay

| Fichero | Qué es |
|---|---|
| `hoja_expresiones.png` | Las seis caras: neutra, entiende, piensa, sorpresa, serio (la del remate) y duda |
| `personaje_completo.mp4` | 12,8 s, 1080×1920, con la voz de `MDS-045` (toma C36 de `07_pruebas/c36-2026-10-22/c36.mp3`, escenas 1 y 2): el personaje como plano principal |
| `personaje_esquina.mp4` | La variante «momento puntual»: el plano de fondo (foto del banco, `apreton_manos_hombres_reunion.jpg`, Pixabay Content License, en `banco.json`) y el personaje en un círculo en la esquina **solo en la apertura y en el remate** |
| `personaje.html` | El personaje y toda su animación, en una función del tiempo `setT(t)` |
| `preparar.py` · `pista.json` | La pista de interpretación: palabras con su tiempo (faster-whisper `tiny`) y energía del audio a 30 fps |
| `render.py` | Fotograma a fotograma en Chromium (como `render.py` de producción) y ffmpeg |

## El personaje

Adulto, gafas redondas en **ámbar** (el único detalle ámbar), chaqueta en el azul de la marca, camisa
blanco hueso e insignia del Engranaje en **cian**. Silueta reconocible de lejos: el remolino alto del
pelo. No copia a ningún personaje conocido (dibujo propio desde cero; regla 7.1.1 adaptada).

## Cómo se mueve

- **La boca**: visemas del español sacados de la palabra que dice Whisper (A, E, I, O, U, cierre m/b/p,
  f/v, consonante), repartidos en el tiempo de cada palabra; cuánto abre lo decide la energía del audio.
- **Los ojos**: parpadeo con un calendario fijo (cada 2,4-3,7 s), nada al azar (regla 11.5).
- **Los gestos, por papel de escena**: apertura cómplice (entiende), planteamiento (neutra), la pregunta
  del chiste (piensa, cabeza ladeada, mirada arriba), **el remate serio y quieto** (sin cabeceo: regla
  13.1), la reacción (sorpresa → entiende). Transiciones de 0,28 s. Cabeceo leve con la voz.
- Sin red, sin GPU, sin cuota: un SVG en el mismo Chromium del render.

## Tiempo de render (contenedor, sin GPU)

- Completo: 384 fotogramas en 42,5 s (**111 ms/fotograma**).
- Esquina: 384 fotogramas en 193 s (502 ms/fotograma; lo caro es la foto de fondo a pantalla completa,
  no el personaje).

## Para repetirlo

    python preparar.py ../../c36-2026-10-22/c36.mp3 0 12.8
    CHROMIUM_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell \
      python render.py hoja
    python render.py completo ../../c36-2026-10-22/c36.mp3 0 12.8
    python render.py esquina  ../../c36-2026-10-22/c36.mp3 0 12.8

(`playwright` y `faster-whisper` instalados; `CHROMIUM_PATH` solo si la versión de playwright no casa
con el Chromium instalado.)

## Lo que falla o falta (dicho sin adornos)

- **La boca va por letras, no por fonemas**: Whisper oye a veces otra palabra («Terriers» por «Te ríes»)
  y los visemas salen de lo que oye. Se nota poco porque suena parecido; en producción se tomarían las
  palabras del guion alineadas con Whisper, como ya hace `corte_palabras.py`.
- **Es plano**: no gira la cabeza en tres cuartos ni mueve las manos. Tiene el carisma de un buen
  pictograma, no el de un VTuber. Es exactamente el riesgo que el plan apuntaba para el Engranaje.
- El cuello y las orejas se separan un poco del cuerpo en los ladeos grandes (piensa, duda).
- No está integrado en el pipeline: es una prueba aparte. Integrarlo sería una capa más en
  `escena.html`, como la animación de C55.2.

## Los vídeos en el repositorio

`.gitignore` deja fuera los `.mp4` de `07_pruebas/` por tamaño. Para que el codirector pueda verlo desde GitHub van, como excepción (añadidos con `git add -f`), las copias ligeras `*_540.mp4` (540×960, el mismo contenido con su audio). Los originales a 1080×1920 se regeneran con los scripts de esta carpeta.
