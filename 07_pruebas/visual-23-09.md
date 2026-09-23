# visual-23-09 · C50: de diapositiva a vídeo

*Dejada por la dirección el 23/09/2026. Versión 12 de `00_estrategia/PLAN_DE_CAMBIOS.md`, C50.*

**Esta prueba necesita que antes esté hecha la tarea 2 de
`00_estrategia/tareas/tareas_codirector_2026-09-23.md`** (tres cuentas gratuitas, cuatro
secretos de GitHub y crear a mano el workflow `visual_prueba.yml` de esta carpeta). Sin eso no hay
nada que mirar: ni el ordenador del codirector ni los contenedores de las tareas programadas llegan
a Pexels, Pixabay o Cloudflare; GitHub Actions sí.

*Una excepción a la regla de esta carpeta («nada de aquí se ejecuta»), dicha para que no se lea como
un descuido: el workflow deja las hojas de contactos en `visual-23-09/hojas/` él solo. Es lo único
que escribe, y solo cuando se lanza a mano.*

## 1 · Qué hay que mirar, y en qué orden

Cuando la ejecución de **«Prueba visual (C50)»** termine en verde:

1. **Las hojas de contactos**, en `visual-23-09/hojas/` (o en GitHub, en esa misma carpeta). Nueve
   imágenes: tres Shorts (`MDS-023`, `024`, `025`) por tres variantes. Cada una tiene las seis
   escenas en fila y, debajo de cada escena, **la frase que dice la voz** y de dónde sale la imagen.
   - **A** · vídeo de archivo detrás y la frase corta de la escena encima.
   - **B** · lo mismo, pero con subtítulos grandes de la narración.
   - **C** · imágenes generadas con IA en todas las escenas.
2. **Las previas en vídeo** (sin sonido) de las variantes A y C: en la página de la ejecución, abajo
   del todo, **Artifacts → muestrario-c50**. Es un zip; dentro, en `salida/MDS-02X/`, los
   `previa_…mp4`. Míralas en el móvil si puedes: es donde se van a ver.

Mirando, ten delante estas tres cosas:

- **¿La imagen cuenta lo mismo que la frase?** Una imagen que no pega es peor que ninguna.
- **¿Se lee el texto?** Sobre cualquier fondo, a tamaño de móvil.
- **¿Parece un vídeo de verdad o un banco de imágenes?**

## 2 · Qué pregunta contesta

**¿Con qué variante pasamos de diapositiva a vídeo: A, B, C, o una mezcla?**

## 3 · Qué pasa con cada respuesta

| Respuesta | Qué hago |
|---|---|
| **A** | Entra así la semana del 28: archivo en las escenas de situación, tarjeta de marca sobre la imagen desenfocada en datos y comparaciones. La planificación escribe lo que se busca en cada escena |
| **B** | Como A, y además **vuelven los subtítulos quemados** (los apagaste el 20/08 porque competían con el texto de la escena; aquí no hay texto de escena con el que competir). Solo si lo dices tú |
| **C** | Imágenes generadas en todo, con movimiento de cámara. Antes de publicar hay que leer los términos de uso de Black Forest Labs en Cloudflare, y cada vídeo se marca como contenido sintético |
| **Una mezcla** (lo más probable) | Archivo cuando hay un plano que cuenta la frase; imagen generada cuando lo que se cuenta no existe en ningún banco («un hombre en pijama en una reunión») |
| **Ninguna** | C50 se replantea el viernes antes de tocar nada de producción |

Contesta debajo de esta línea, con fecha.

---

## Respuesta del codirector: 23/09/26

Me parece un buen camino a explorar. He creado las cuentas, subido los secretos y realizado la prueba con éxito. Te comento los resultados de tal prueba:

- A es nuestra mejor opción. Tiene varios pequeños problemas, nada que no se pueda pulir, creo:
   1. A veces el título cae justo encima de la cara de la persona que aparece en el vídeo. Sería cuestión de intentar detectar la cara y mover el título para que no cayera justo encima (solución más ambiciosa), o bien colocar los textos en la parte inferior y confiar en que la mayor parte de las veces las caras en un short van a aparecer en la parte superior.
   2. A veces la imagen no corresponde con el timing en el que aparece el título. En MDS-023 cuando se dice "aparecía roto de fábrica" aparece el vídeo del señor fregando los platos, cuando me imagino que tendría que aparecer el otro chico joven levantando el capó del coche. También hay algún caso extraño de coherencia no ideal como el de ver una familia asiática celebrando algo cuando el título habla de un viaje a Lisboa.
   3. Cuando aparecen los títulos que son porcentajes grandes o cuando son recuadros azules, entonces el vídeo de fondo se vuelve borroso y no se ve. Esto queda feo y habría que modificarlo para que se viera como el resto de vídeos. Esto pasa siempre en estos títulos. Por ejemplo, en el segundo 28 de MDS-23, bajo el título "265 jubilados".
   4. En MDS-025_A no sé si fue a propósito o no, pero la última escena, de "Eran 10 por grupo", es con una imagen fija de un sillón, no un vídeo. Como digo, desconozco si fue o no intencional, solo lo señalo.
- B no funciona. Los títulos no tienen sentido en muchas ocasiones. Se aprecian títulos como "PROBLEMAS, HACER CHISTES A" o "EL COCHE Y LA". Es decir, no es confiable en absoluto.
- C no sé que ha intentado, pero sea lo que sea que ha intentado no ha funcionado porque se ve todo exactamente como se veía hasta hoy, con el fondo azul y los títulos amarillos en todos los textos.

Notas adicionales:

1. Entre todos los vídeos generados se pueden intercalar pequeñas imágenes renderizadas como hasta ahora (con el fondo azul o cualquier otro) para mostrar los mensajes clave rápidamente antes de volver a los vídeos. Así se gana dinamismo sin mayor coste.
2. De igual forma, se puede explorar la generación gratuita de un personaje real que mueva los labios a la vez que se habla. Como sé que esto gastaría las cuotas gratuitas muy rápido en caso de que las hubiera, propongo que se utilizara solo para momentos puntuales en los shorts, dejando el resto del vídeo como se han propuesto.
3. Como alternativa al punto anterior, se podría explorar la creación de un avatar de dibujo animado que hiciera este trabajo si el punto 2 es inviable bajo las reglas del proyecto. En cualquier caso, tanto con una solución como con la otra, sería importante encontrar una manera de que hubiera consistencia entre los distintos vídeos, y no contar con un personaje (real o animado) muy distinto en cada vídeo, sobre todo si usan la misma voz después.
4. Dinamismo es la palabra. Tenemos que conseguir que el vídeo sea atractivo de principio a fin, y no aburrido, ni desde el guion ni desde la presentación.
Buen trabajo.
