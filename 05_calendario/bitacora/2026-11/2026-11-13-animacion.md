# Animación · viernes 13/11/2026

Shorts de los próximos diez días (hasta el 23/11) con escenas `"animar": true` y sin página: **MDS-068** (lun 16/11), **MDS-069** (mar 17/11) y **MDS-071** (vie 20/11), todos del ciclo B2. El resto ya tenía página. Hecho.

| Short | Emisión | Escenas | Fondo | Vueltas | Resultado |
|---|---|---|---|---|---|
| `MDS-068` (¿las ratas se ríen con las cosquillas?) | lun 16/11 | 4 (lista), 5 (dato) | **ámbar suave** `#FFE3A3` | 2 | página + hoja |
| `MDS-069` (¿sonreír a la fuerza te pone contento?) | mar 17/11 | 3 (lista), 4 (dato) | **azul noche** `#16213A` | 2 | página + hoja |
| `MDS-071` (¿los perros se ríen?) | vie 20/11 | 4 (lista), 5 (dato) | **crema** `#FFF4E0` | 2 | página + hoja |

Fondos: la semana pasada fueron azul noche (062) y crema (064); esta se ven los tres, empezando por el ámbar suave. La última escena de cada guion (cierre, remate de marca) no se ha pintado. `MDH-008` tiene escenas marcadas pero no es un Short ni tiene fecha en estos diez días: no se toca.

## Qué dibuja
- **068/4**: una rata en línea y, en «cosquillas», una mano que le roza la barriga; al «jugar» entra una segunda rata y se mira con la primera. Abajo, un detector con una barra que barre desde el segundo 0 y marcas de chillido que corren: una tanda con las cosquillas, otra (violeta) que se suma al jugar.
- **068/5**: una onda de chillido (violeta, fina) se dibuja desde el principio y, en «risa», se transforma de izquierda a derecha en una onda ancha de risa (menta) con tres «ja»; en «alegría» saltan confetis y la rata de abajo, que ya chillaba, rebota.
- **069/3**: treinta figuras sin cara que entran en tandas (12 al principio, el resto en «casi cuatro mil»); la boca, plana, sube las comisuras poco a poco en «sonrieran»; en «cómo» sale una burbuja con un deslizador que busca.
- **069/4**: la sonrisa, ya completa, rebota con confeti en «contentas»; dos medidores: el primero parte de la mitad y sube «un poco»; el segundo llega en «incluso», parte de cero (figura gris) y sube también en «ninguna alegría» (la figura se colorea).
- **071/4**: perro y persona (sin cara) con micrófono cada uno en «micrófonos»; dieciséis puntos que se encienden en «dieciséis»; en «entrenaban», «jugaban» y «descansaban» caen tres tarjetas (cono, pelota, luna) con una onda de sonido igual de viva bajo cada una (no adelanta el resultado).
- **071/5**: tres barras: las de entrenar y descansar casi vacías, la de jugar se llena en «jugar»; el perro de abajo empieza a jadear en «jugar», una mano le hace cosquillas en «cosquillas» y salen corazones en «mimos».

## No se hizo como decía la nota
- **068/4 y 068/5**: las notas citan «al hacerles cosquillas», «cuando jugaban entre ellas», «parecida a la nuestra» y «una docena de razones»; esas frases ya no están en la narración (las quitó la lectura en frío). Se anclaron a «cosquillas», «jugar», «risa» y «alegría», y **no se dibujan los doce puntos** (sería un dato que la voz no dice).
- **069/3**: la nota pide una cara dibujada en línea. Como la regla es «sin caras humanas», solo se dibuja la **boca** (un arco grueso con las comisuras), sin cabeza, ojos ni nada más. Tampoco se dibuja el marco con la foto: la narración no la nombra. Se añadieron las treinta figuras sin cara para «casi cuatro mil personas».
- **069/4**: el medidor es una barra horizontal por persona-tipo (dos filas), en vez de uno junto a la cara.
- **071/4**: los carteles «entrenar / jugar / descansar» son iconos sin texto (la voz dice las palabras y el guion ya las pone en pantalla en la línea «Entrenar · jugar · descansar»).
- **071/5**: la nota habla de «tres barras, una por fase»; son verticales, con un icono arriba, y el perro de abajo muestra el jadeo y las cosquillas.

## Comprobaciones
Hojas en `05_calendario/animaciones/MDS-068/hoja.jpg`, `MDS-069/hoja.jpg` y `MDS-071/hoja.jpg` (6 instantes por escena, tiempos inventados a 2,6 palabras/s). `comprobarEscena` en 20 instantes por escena: listas vacías (tras la vuelta 2). Consola sin errores. Sin red, sin `Math.random` ni `Date`, fuentes genéricas. Mismo `t`, mismo píxel: comprobado con repintados intermedios; la primera captura tras cargar la página difiere en el texto (rasterizado de la primera pasada) y las siguientes son idénticas, como en las páginas anteriores.
Vuelta 1 → 2: 068 (mano que pisaba el texto, detector vacío los primeros segundos, ratas pequeñas), 069 (primer punto en dos líneas fuera de su caja, multitud tardía, figuras desalineadas con su medidor), 071 (micrófonos tapando el hocico, hueco sin tarjetas antes de su palabra, corazones sobre el texto).

## Lo que queda flojo
- Mitad inferior algo vacía en 068/4 y 071/4 bajo el panel o las tarjetas (se respeta la zona segura).
- No se ha visto con la voz real; si los tiempos reales son muy distintos, lo que se mueve puede llegar algo pronto en 069/3.
- La boca sola de 069/3 se lee como sonrisa pero es menos «cara» que la nota; la dirección dirá si quiere otra cosa.

## Gasto estimado
Dos vueltas por Short; unos 40 minutos de cómputo y unos 150 000 tokens.
