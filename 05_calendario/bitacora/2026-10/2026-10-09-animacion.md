# Bitácora · Animación a medida (C55.2) · viernes 9 de octubre de 2026

Rutina «Animación», 09:09 UTC. Clon en rama `claude/adoring-keller-h9as6z`, fichero de tarea leído entero.

## Qué Shorts
Los tres Shorts del brazo A (ciclo B1) con `"animar": true` caen dentro de los próximos diez días
y no tenían página:

| Short | Emisión | Escenas animadas | Vueltas | Resultado |
|---|---|---|---|---|
| `MDS-038` (cosquillas) | mié 14 | 4 (diagrama), 5 (comparación) | 1 | página + hoja |
| `MDS-039` (ascensor) | jue 15 | 4 (comparación), 5 (dato) | 1 | página + hoja |
| `MDS-042` (funeral) | dom 18 | 4 (comparación), 5 (dato) | 1 | página + hoja |

Ninguna escena animada es la última (la 6 lleva el remate de marca y no se ha pintado).

## Qué dibuja cada una
- **038/4**: escáner sobre un cerebro de línea; en «mueves» la mano echa a andar hacia el pie; en
  «predice» se dibuja en el cerebelo la huella prevista (ámbar, discontinua) y un rastro de puntos hasta el pie; al
  tocar, la huella real (cian) se superpone y lanza una onda.
- **038/5**: dos barras de volumen; en «flojita» baja la de «Tu mano»; en «otro» sube de golpe la de «Otra mano» (ámbar).
- **039/4**: dos parejas de figuras sin cara que entran desde los lados; en «reírse» la primera se
  acerca y salta un bocadillo con garabato; en «serias» la segunda queda separada y quieta.
- **039/5**: dos puntos en una regla; se iluminan en «mejor» y se tocan en «cerca». (El orden sigue
  el de la voz, que dice «mejor» antes que «cerca»; la nota del guion los ponía al revés.)
- **042/4**: dos ondas de sonido; en «arruga» la primera se ensancha y se vuelve ámbar; en «compromiso» la segunda se aplana y se pone gris.
- **042/5**: dos medidores; en «enfadado» baja la aguja del enfado, en «alivio» sube la del alivio; en
  «otra» (la otra risa) ambos vuelven a cero y se apagan. Sin la nube gris de la nota (se sustituyó por el medidor, sin añadir datos).

## Comprobaciones (hojas en `05_calendario/animaciones/MDS-XXX/hoja.jpg`)
Tiempos inventados a 2,6 palabras/s. `comprobarEscena` en 20 instantes por escena: **listas vacías
en las seis escenas**. Consola de la página: sin errores (tras corregir un radio negativo en 039/5 en la misma vuelta de pruebas).
Mismo `t`, mismo píxel: comprobado. Sin red, sin `Math.random` ni `Date`, fuentes genéricas.

## Lo que queda flojo (para la revisión del día antes)
- Las escenas aprovechan la franja y 250–1400 px; abajo queda aire (zona segura de YouTube).
- Hasta que la voz dice la primera palabra clave el texto no aparece (los marcos sí), así que el primer
  segundo lo llevan solo el fondo en movimiento y el dibujo.
- En 038/4 y 042/4 el texto «risa de verdad»/«lo que vas a sentir» entra con la voz, no antes.

## Gasto estimado
Una sola sesión, unas 20 llamadas de herramienta y tres páginas de ~250 líneas; del orden de 150k tokens.
No se ha tocado ningún guion ni nada fuera de lo permitido.
