# Registro de mejoras

Historial de lo observado en los vídeos ya producidos y de lo que se ha hecho al
respecto. Se **añade al final**, nunca se reescribe: sirve para no repetir
errores y para no volver a discutir decisiones ya tomadas.

Lo alimenta la revisión diaria de las 07:00 y cualquier sesión que mire un vídeo.

---

## 18 de agosto · MDH-002.es (producción de prueba, sin subir)

Primera revisión con fotogramas reales, a partir de `05_calendario/qa/MDH-002.es/`.

### Lo que está bien

- Audio correcto: −14,25 LUFS (objetivo −14), pico −1,22 dBTP (límite −1,0),
  rango 3,1 LU. La normalización de `montaje.py` funciona.
- Colchón de entrada: el silencio inicial acaba en 0,629 s, justo donde debe.
  **El falso arranque de la voz no aparece** — al menos en español.
- La rotación de música eligió `cama_02_dusk_next_route.mp3`, la que le tocaba
  al episodio 02.
- Las escenas de tipo `comparacion` y `lista` se leen bien y con jerarquía clara.

### Fallos encontrados

1. **No hay subtítulos quemados.** Seis fotogramas repartidos por todo el vídeo,
   ninguno con subtítulo en pantalla. Es grave por partida doble: se pierde la
   accesibilidad y, sobre todo, los subtítulos palabra a palabra son *lo único
   que se mueve* durante el tramo central de cada escena, que es estático por
   diseño. Sin ellos el vídeo se percibe como un pase de diapositivas — que es
   exactamente el diagnóstico que dio Silvestre sobre los dos primeros vídeos.

   Causa probable: `voz.py` construye los subtítulos con las marcas de tiempo por
   palabra que devuelve el sintetizador (`WordBoundary`), y si esa lista viene
   vacía escribe un `.ass` con cabecera y sin una sola línea. `montaje.py` lo
   quema sin error y sin efecto. Nadie avisaba.

   *Hecho:* `voz.py` avisa y cuenta las marcas; `montaje.py` avisa si monta sin
   subtítulos y dice por qué; `qa.py` registra en la ficha `subtitulos.quemados`
   y el número de líneas, que es lo que distingue si el fallo está en la voz o en
   el montaje. El `.ass` se guarda ya entre los artefactos. **Pendiente de
   confirmar con la producción del 19.**

2. **Los titulares nunca se han visto como estaban diseñados.** `escena.html`
   pide Archivo Black; el runner solo instalaba `fonts-inter` y
   `fonts-jetbrains-mono`, y Archivo Black no está en los repositorios de Ubuntu.
   Los titulares caían a Inter en peso 700 mientras los enunciados piden 800: la
   jerarquía visual estaba invertida.

   *Hecho:* se descarga la fuente en el propio job, con aviso si falla.

3. **El ámbar ha perdido su función.** La regla es un resaltado por pantalla. En
   la escena 9 había dos (*quién* y *dónde*) y en la 18, tres. Cuando todo está
   resaltado, nada lo está.

   *Hecho:* corregido en MDH-002.es. Los guiones siguientes lo respetan.

4. **Escena 18 de 20,4 s reales**, por encima del máximo de 20 que impone el
   validador. La estimación a 150 palabras por minuto se queda corta frente a la
   voz real, que va a −4 %.

   *Hecho:* recortada. **Pendiente:** calibrar `PPM` en `validar_guion.py` con
   las duraciones reales de varios episodios, en vez de dejarlo en 150.

5. **Los fotogramas de QA se tomaban a ciegas.** El primero cayó en mitad de un
   fundido entre escenas y salió al 20 % de opacidad: inservible.

   *Hecho:* `qa.py` calcula los instantes a partir de `guion.timed.json` y apunta
   al 60 % de cada escena, cuando la entrada ya terminó y la salida no ha
   empezado.

### Error editorial, detectado por Silvestre y no por el sistema

El arranque de MDH-002.es era **un calco del chiste inglés**: «un hombre entra en
un bar… y se agacha, porque el bar es de hierro». En inglés *bar* significa a la
vez local y barra, y el chiste existe; en español no hay doble sentido y la
escena no era un chiste, era una frase rara. El cierre remataba con el mismo
calco.

*Hecho:* sustituido por un chiste nativo en español cuya gracia no depende de
ninguna palabra concreta, sino de que rompe una norma social sin que pase nada
—es decir, el propio gancho **es ya** una violación benigna, que es lo que el
vídeo explica después. El cierre lo desmonta con las dos condiciones.

*Lección de sistema:* `validar_guion.py` comprueba estructura, no si un chiste
funciona. Ningún agente estaba leyendo el guion antes de producirlo. La revisión
de las 07:00 pasa a revisar **también el episodio del día siguiente**, que
todavía no se ha producido y da veinte horas de margen. Un calco del inglés al
español, o al revés, es motivo de bloqueo.
