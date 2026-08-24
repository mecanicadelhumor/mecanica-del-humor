# Exportes de YouTube Studio

Aquí va **un solo CSV a la semana**, y es el único trabajo manual que queda en
todo el circuito de métricas.

## Por qué hace falta

La API de analítica de YouTube da casi todo —visualizaciones, duración media,
porcentaje visto, **la curva de retención completa**, suscriptores, me gusta,
comentarios y fuentes de tráfico— y `04_agentes/metricas.py` lo lee solo cada
lunes desde GitHub Actions.

Lo que la API **no** da son **impresiones y CTR**. No es un descuido nuestro:
esas dos métricas son exclusivas de Studio y no existen en la API (lo que la API
llama `impressions` son impresiones de *anuncios*, otra cosa distinta).

Y resulta que ahora mismo el CTR es justo la métrica que bloquea el canal, así
que no se puede prescindir de ella.

## Cómo se saca — treinta segundos, y no crece con el número de vídeos

1. YouTube Studio → **Estadísticas** → pestaña **Contenido**
2. Arriba a la derecha, **Modo avanzado**
3. Periodo: **últimos 28 días**
4. Botón de **exportar** (la flecha hacia abajo) → **Hojas de cálculo** o **CSV**
5. Deja el fichero en esta carpeta, con su nombre tal cual

Un único CSV trae **todas** las filas de **todos** los vídeos. Da igual que el
canal tenga tres vídeos o trescientos: es la misma descarga.

El script coge siempre el fichero más reciente de esta carpeta y busca las
columnas por palabra clave («impres», «clic»), así que da igual el idioma de la
interfaz o el orden de las columnas.

## Si algún lunes se te olvida

No pasa nada: `metricas.json` sale ese lunes con `impresiones` y `ctr` en
`null`, y todo lo demás igual de completo. La tarea del lunes lo dirá en su
resumen y seguirá adelante con los peldaños 3, 4 y 5 de la escalera.
