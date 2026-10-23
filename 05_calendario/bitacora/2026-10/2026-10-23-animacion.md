# Animación · viernes 23/10/2026

Shorts del brazo A de los próximos diez días (hasta el 2/11) con escenas `"animar": true`: 042, 046 y 048 ya tenían página; faltaban **MDS-051** (mar 27) y **MDS-055** (sáb 31). Los dos, hechos. (MDS-038/039 son anteriores a la ventana y ya tienen página.)

| Short | Emisión | Escenas | Fondo | Vueltas | Resultado |
|---|---|---|---|---|---|
| `MDS-051` (jajaja sin reírte) | mar 27 | 4 (comparación), 5 (dato) | **azul noche** `#16213A` | 1 | página + hoja |
| `MDS-055` (cosquillas y máquina) | sáb 31 | 4 (comparación), 5 (dato) | **crema** `#FFF4E0` | 1 | página + hoja |

La escena 6 (cierre, remate de marca) no se ha pintado en ninguno. Los fondos rotan respecto a los de la semana pasada (crema, ámbar suave): hoy azul noche y crema; el ámbar suave no ha tocado.

## Qué dibuja cada una
- **051/4**: una hoja de diario con anillas; en «cara a cara», «teléfono» y «chat» se van sumando filas (dos bocadillos, móvil, bocadillo con puntos) con su línea escrita; en «risa» a cada fila le salta al lado una carcajada (círculo ámbar con rayos) o un bocadillo violeta con trazo en zigzag (sin letras).
- **051/5**: dos medidores de «felicidad» que suben a la vez (icono de risa con rayos / bocadillo de chat); en «casi» se frenan casi a la misma altura y se enciende un «≈» menta.
- **055/4**: dos figuras sin cara sentadas; en «veces» dan un salto con onda; en «investigador» baja una mano dibujada y en «máquina» un brazo mecánico con cepillo; después las dos tiemblan igual con las mismas líneas de movimiento.
- **055/5**: dos contadores de risa bajo mano y brazo; suben en «sonrisas», acaban exactamente a la misma altura en «mismo» y se enciende un «=» menta; sacudida a la vez en «fuertes».

## Cosas que no se han hecho como decía la nota
- **051/4**: la nota decía «carcajada dibujada o bocadillo con letras»; sin letras (regla 14: la pantalla no dice lo que la voz no dice) ni caras. Carcajada = círculo con rayos; el bocadillo lleva un zigzag. No se ha dibujado el icono del «sobre» porque la narración no lo dice.
- **051/5**: la nota decía «una boca riendo» en una barra; sustituida por círculo con rayos, por la regla de no caras. Las barras no llevan números.
- **055/4**: «siluetas de línea» hechas como figuras rellenas de color (cabeza + cuerpo, sin rasgos).
- La nota de 055/5 no pedía nada que no se pudiera dibujar.

## Comprobaciones
Hojas en `05_calendario/animaciones/MDS-051/hoja.jpg` y `MDS-055/hoja.jpg` (6 instantes por escena, tiempos inventados a 2,6 palabras/s). `comprobarEscena` en 20 instantes por escena: **listas vacías en las cuatro escenas**. Consola sin errores. Mismo `t`, mismo píxel: comprobado. Sin red, sin `Math.random` ni `Date`, fuentes genéricas. El navegador se lanzó por ruta (`/opt/pw-browsers/chromium-1194`) porque `playwright install` no hacía falta.

## Lo que queda flojo (para la revisión del día antes)
- En 051/4 el diario está vacío hasta «cara a cara» (~3-4 s con la voz real): lo anclado a la palabra deja los primeros segundos con solo la hoja moviéndose y la deriva del fondo.
- Los rótulos pequeños (`en persona`, `en el chat`, `el investigador`, `o eso creían`) son de 40 px: se leen, pero son lo más justo.
- Mitad inferior (y > 1300 px) vacía en las cuatro escenas; se respeta la zona segura de YouTube.
- No se han visto con la voz real.

## Gasto estimado
Una vuelta por Short; unos 20 minutos de cómputo y unos 100 000 tokens.
