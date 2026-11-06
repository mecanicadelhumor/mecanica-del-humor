# Animación · viernes 06/11/2026

Shorts del brazo A de los próximos diez días (hasta el 16/11) con escenas `"animar": true` y sin página: **MDS-062** (sáb 7/11) y **MDS-064** (mié 11/11), ambos del ciclo B2. El resto (038 a 059) ya tenía página. Hecho.

| Short | Emisión | Escenas | Fondo | Vueltas | Resultado |
|---|---|---|---|---|---|
| `MDS-062` (¿por qué casi no te ríes solo?) | sáb 7/11 | 4 (libreta), 5 (dato) | **azul noche** `#16213A` | 2 | página + hoja |
| `MDS-064` (¿por qué un chiste malo hace gracia si alguien se ríe?) | mié 11/11 | 4 (lista), 5 (dato) | **crema** `#FFF4E0` | 2 | página + hoja |

Fondos: la semana pasada fueron crema (055) y ámbar suave (059); esta semana toca azul noche y crema, y el ámbar suave queda para el siguiente. La escena 6 de cada uno (cierre, remate de marca) no se ha pintado.

## Qué dibuja
- **062/4**: una libreta de espiral que entra desde el principio; en «libreta» se abren tres páginas (dos con dos figuras sin cara charlando, una con una figura sola); en «semana» se encienden siete puntos (los días); en «cada vez que se reían» caen las rayitas (11 y 9 en las páginas con charla, 1 en la de la figura sola) y un lápiz sigue la última.
- **062/5**: dos figuras con bocadillos que alternan líneas de charla y «ja» (el «ja» sale dentro de la conversación, en «reírse» y en «mitad de una charla»); en «casi» aparece la figura sola con un bocadillo discontinuo vacío.
- **064/4**: seis marcos discontinuos desde el segundo 0; en «chistes», «eructos» y «caídas» caen las viñetas (bocadillo, burbujas de eructo, figura resbalando), en dos filas. En «risas» se encienden ondas y «ja» en la fila de arriba; en «sin» la de abajo queda con una línea plana gris.
- **064/5**: tres viñetas con su medidor. En «risas» suben el de risa fingida (rígida, encajonada, se sacude en «fingida») y el de risa de verdad; en «verdad» este último sube más y su «JA» crece y rebota. El primero, sin risa, casi no se mueve.

## No se hizo como decía la nota
- 062/4: los días van como siete puntos, sin las letras L-D (la voz no los dice, regla 14).
- 064/4: las etiquetas «Con risas» / «Sin risas» van debajo de cada fila (son las del guion, `puntos`); las ondas «ja ja» solo van en la fila de «con risas».
- 064/5: el medidor junto a tres viñetas (sin risa, fingida, verdadera) en vez de una por cada viñeta del 064/4: más legible a 1080 px.

## Comprobaciones
Hojas en `05_calendario/animaciones/MDS-062/hoja.jpg` y `MDS-064/hoja.jpg` (7 instantes por escena, tiempos inventados a 2,6 palabras/s). `comprobarEscena` en 20 instantes por escena: listas vacías. Consola sin errores. Mismo `t`, mismo píxel. Sin red, sin `Math.random` ni `Date`, fuentes genéricas. Vuelta 1 (primeros segundos vacíos en 062/4 y 064/4, rótulos pegados a las viñetas) → vuelta 2 (cuaderno y marcos desde el segundo 0, filas separadas).

## Lo que queda flojo
- Mitad inferior vacía bajo el texto (se respeta la zona segura).
- En 064/4 las etiquetas de fila quedan algo pegadas a las viñetas; el título va más abajo.
- No se ha visto con la voz real.

## Gasto estimado
Dos vueltas por Short; unos 30 minutos de cómputo y unos 110 000 tokens.
