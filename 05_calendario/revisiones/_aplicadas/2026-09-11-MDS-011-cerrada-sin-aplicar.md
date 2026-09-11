# MDS-011 — regla 14 (los dos canales): la escena 4 añade «tus amigos» que la voz no dice

**Cerrada el 11/09/2026, sin aplicar.** El vídeo se publicó el 07/09 (sigue
además con el otro problema, sin relación con esto: `estado: "private"` sin
`publicar_en`, escalado en `ESTADO.md` desde el 08/09). Un guion ya producido
no se toca (`REGLAS.md`), así que esta corrección ya no tiene destino
posible: ni al guion (se aplicaría a un vídeo que no existe) ni al vídeo
(no se re-produce por un matiz de este tamaño). Se archiva para no seguir
ocupando el buzón; el razonamiento original queda íntegro debajo por si
vuelve a aparecer el mismo patrón («tus amigos», «martes», «dinero») en
otro guion.

Publica el lunes 07/09. Más de 48 h desde esta revisión (hoy 04/09), así que
sigue la regla general: nota para el jueves, no edición directa.
`validar_guion.py` sin errores; `comprobarDesbordes()` (la barrera de hoy) sin
hallazgos en este guion.

## El hallazgo

Escena 4, tipo `dato`:
```json
{
  "cifra": "Un pie de foto",
  "pie": "puntuado por jueces, no por tus amigos",
  "narracion": "Te dan una viñeta sin texto, escribes el pie, y unos jueces puntúan lo que has escrito. Esa es la prueba entera."
}
```
El `pie` en pantalla añade «no por tus amigos» — una comparación que la
`narracion` de esta escena no dice en ningún momento, y que tampoco aparece en
ninguna otra escena del Short. Aplicando el criterio de la regla 14 tal cual
está escrito («el texto puede decir menos que la voz; no puede introducir un
dato que la voz no dice»): quien escucha sin mirar nunca sabe que hay una
comparación con los amigos; quien mira sin oír lee una frase que no rompe el
sentido —se entiende sola— pero es información que solo existe en pantalla.

**Severidad, con la comparación con el caso que escribió la regla por
delante**: esto no es del tamaño de MDS-009 («dinero» sosteniendo un dato de
un estudio que no se menciona en ningún sitio y llevaba a una lectura confusa
en los dos canales). Aquí «amigos» es un contraste retórico, no un dato del
estudio, y ninguno de los dos canales queda confundido — solo desequilibrado:
uno de los dos recibe una idea de más. Lo anoto porque es exactamente el tipo
de caso que el aviso nuevo de C22 en `validar_guion.py` (encargo 3, todavía
sin hacer esta sesión) está pensado para señalar, y es un buen ejemplo real
para probarlo cuando se escriba.

ANTES:
```json
"pie": "puntuado por jueces, no por tus amigos",
```

DESPUÉS (más simple — quita la comparación que la voz no sostiene; no toca
`cifra`, `narracion` ni `fuente`):
```json
"pie": "puntuado por jueces",
```

O, si se prefiere conservar el contraste porque ayuda a entender la prueba,
la alternativa es sumarlo a la narración de esta escena («no por tus amigos»)
en vez de quitarlo del pie — lo dejo como opción, no como corrección elegida:
no soy quien decide el tono de la voz.
