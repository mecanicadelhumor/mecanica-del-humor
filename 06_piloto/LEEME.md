# Piloto — prueba de imagen del episodio 1

`MDH-001_prueba_de_imagen.mp4` es el episodio 1 completo renderizado de verdad: 38 escenas, 7 minutos
y 25 segundos, 1080p a 30 fps, generado por `render.py` desde
`05_calendario/guiones/MDH-001.es.json`.

**Va mudo, y es a propósito.** La síntesis de voz necesita salida a internet y mi contenedor no la
tiene: ese paso corre en GitHub Actions. Lo que este archivo demuestra es todo lo demás, que es lo
que no se podía dar por supuesto:

- que el sistema visual funciona y se sostiene siete minutos seguidos,
- que los nueve tipos de escena se ven bien con contenido real y no solo en una maqueta,
- que el ritmo de entradas y salidas acompaña al texto,
- y que las duraciones calculadas coinciden al segundo con el vídeo final.

Cuando se le añada la voz, las duraciones dejarán de ser estimadas y pasarán a ser las reales del
audio: el mismo `render.py` las lee de `guion.timed.json`, que produce `voz.py`. El resultado será
este vídeo con la narración encima y los subtítulos animados abajo, que es lo que aporta el
movimiento continuo durante los tramos en los que la escena se queda quieta.

Las dos imágenes son las miniaturas de los episodios 1 y 2, generadas con `miniatura.py` desde el
mismo sistema de diseño, para que nunca se desvíen de la identidad del canal.

## Cómo reproducirlo tú mismo

```bash
pip install playwright && playwright install chromium
python3 03_produccion/pipeline/render.py 05_calendario/guiones/MDH-001.es.json \
        -o 06_piloto/prueba.mp4 --fps 15 --escala 0.5
```

Con `--fps 15 --escala 0.5` tarda unos tres minutos y sirve para revisar el ritmo. A calidad
completa son unos veinte.
