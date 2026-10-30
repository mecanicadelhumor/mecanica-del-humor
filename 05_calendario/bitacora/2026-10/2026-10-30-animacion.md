# Animación · viernes 30/10/2026

Shorts del brazo A de los próximos diez días (hasta el 9/11) con escenas `"animar": true`: 038, 039, 042, 046, 048, 051 y 055 ya tenían página; faltaba **MDS-059** (mié 4/11, posición 24, la última del ciclo B1). Hecho.

| Short | Emisión | Escenas | Fondo | Vueltas | Resultado |
|---|---|---|---|---|---|
| `MDS-059` (¿reírse adelgaza?) | mié 4/11 | 4 (comparación), 5 (dato) | **ámbar suave** `#FFE3A3` | 2 | página + hoja |

La escena 6 (cierre, remate de marca) no se ha pintado. El ámbar suave no había tocado aún en la semana pasada (051 azul noche, 055 crema).

## Qué dibuja
- **059/4**: dos salas de línea con dos figuras sin cara cada una y un contador de calorías en la pared. En «investigadores» entran las salas, en «parejas» las figuras, en «calorías» el contador; en «graciosos» la sala izquierda enciende la pantalla (sol con rayos), las figuras saltan y la aguja gira deprisa; en «sin» la derecha enciende una línea plana y la aguja casi se para.
- **059/5**: un medidor que sube poco en «gastaba» y un poco más en «más», con una línea de puntos en el nivel de «no reírse»; en «entre» se enciende la zona pequeña; aparece una balanza (gota de caloría / croqueta) que en «calorías» se inclina del todo hacia la croqueta.

## No se hizo como decía la nota
- Los rótulos `risas` / `sin reír` (`et_a`, `et_b`) no se pintan: la voz no los dice (regla 14). El texto de pantalla es `Vídeo *gracioso*`, `Sin gracia`, `2-10 *calorías*`, `con 10-15 minutos al día`.
- La nota pedía «una habitación con dos figuras» y un contador; hay dos habitaciones (una por tipo de vídeo) para que se vea la comparación.
- La croqueta de la balanza (escena 5) la nombra la voz en la 6, no en la 5; está dibujada, sin texto, como pedía la nota.

## Comprobaciones
Hoja en `05_calendario/animaciones/MDS-059/hoja.jpg` (6 instantes por escena, tiempos inventados a 2,6 palabras/s). `comprobarEscena` en 20 instantes por escena: listas vacías. Consola sin errores. Mismo `t`, mismo píxel. Sin red, sin `Math.random` ni `Date`, fuentes genéricas. Vuelta 1 → ajuste de los platos de la balanza → vuelta 2.

## Lo que queda flojo
- Mitad inferior vacía bajo el texto (se respeta la zona segura).
- En la escena 4 las salas ocupan solo el tercio superior; el texto va debajo.
- No se ha visto con la voz real.

## Gasto estimado
Dos vueltas; unos 25 minutos de cómputo y unos 90 000 tokens.
