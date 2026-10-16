# Bitácora · Animación a medida (C55.2) · viernes 16 de octubre de 2026

Rutina «Animación». Clon en rama `claude/adoring-keller-354qph`, fichero de tarea leído entero.

## Qué Shorts
Brazo A (ciclo B1) con `"animar": true`, dentro de los próximos diez días y sin página (MDS-038, 039 y 042 ya la tenían):

| Short | Emisión | Escenas | Fondo | Vueltas | Resultado |
|---|---|---|---|---|---|
| `MDS-046` (aguantarse la risa) | jue 22 | 4 (comparación), 5 (dato) | **crema** `#FFF4E0` | 1 | página + hoja |
| `MDS-048` (WhatsApp / audio) | sáb 24 | 4 (comparación), 5 (dato) | **ámbar suave** `#FFE3A3` | 1 | página + hoja |

La escena 6 (cierre, remate de marca) no se ha pintado en ninguno. Los fondos rotan (crema, ámbar suave); el azul noche no ha tocado esta semana porque solo hay dos Shorts.

## Qué dibuja cada una
- **046/4**: 180 puntos (las 180 participantes) que entran en cascada; en «graciosas» saltan en ola; en «mitad» se parten en dos bloques de 90, cian y coral. Debajo, dos recuadros: la boca-sonrisa del grupo cian sigue; en «notara» una cremallera ámbar cierra la boca del grupo coral hasta dejarla plana. Sin caras (solo trazos de boca y objetos).
- **046/5**: dos vasos que se llenan; en «menos» el vaso coral (los que se aguantan) se vacía casi del todo; en «demás» el cian da un salto con destellos.
- **048/4**: un bocadillo con líneas grises (la frase escrita) y una onda de sonido; entre ambos el signo «=» en «mismas». Las líneas se dibujan en «leer»; las barras de la onda se animan y colorean en «escuchar».
- **048/5**: dos figuras sin cara. A la que oye le llegan arcos de sonido y en «sensato» se le enciende la cabeza (violeta, halo y rayos); la otra, en trazo gris discontinuo, recibe una hoja en «leyendo».

## Cosas que no se han hecho como decía la nota
- **048/5**: la nota pedía que en «más persona» le salieran ojos y boca. Eso es una cara (prohibida por la tarea) y además «más persona» ya no está en la narración tras la lectura en frío. Sustituido por la cabeza que se enciende.
- **046/4**: la nota pedía «dos caras de línea»; sustituidas por bocas sueltas y una cremallera, por la misma regla.
- **046/5**: la nota pedía medidores con aguja; hechos como vasos que se vacían (misma idea, sin números).
- Regla 14: los rótulos de pantalla son los del guion, sin añadir nada («la otra mitad» está en el guion aunque la voz dice «a la mitad»).

## Comprobaciones
Hojas en `05_calendario/animaciones/MDS-046/hoja.jpg` y `MDS-048/hoja.jpg` (6 instantes por escena, tiempos inventados a 2,6 palabras/s). `comprobarEscena` en 20 instantes por escena: **listas vacías en las cuatro escenas**. Consola sin errores. Mismo `t`, mismo píxel: comprobado. Sin red, sin `Math.random` ni `Date`, fuentes genéricas.

## Lo que queda flojo (para la revisión del día antes)
- En 046/4 la mitad de abajo está vacía hasta «graciosas»/«mitad»: lo llevan los puntos y los recuadros discontinuos.
- Los rótulos pequeños (`la mitad`, `las mismas palabras`) son de 38-40 px: se leen, pero son lo más justo de la pantalla.
- Las hojas se revisaron con tiempos inventados: no se ha visto con la voz real.
- Aprovechan la franja 330-1300 px; abajo queda aire (zona segura de YouTube).

## Gasto estimado
Una vuelta por Short; unos 25 minutos de cómputo y poco más de 100 000 tokens.
