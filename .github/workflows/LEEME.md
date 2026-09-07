# `producir.yml` corregido — 7 de septiembre de 2026

**Qué hay aquí:** `producir.yml` entero, idéntico al que corre hoy salvo **una
línea**. Cópialo sobre `.github/workflows/producir.yml` y súbelo. El fichero está
protegido contra escritura remota (regla 11.7), por eso te lo dejo aquí en vez de
escribirlo yo.

## La línea, si prefieres editarla a mano

En el paso **«Expediente de calidad»**, la última línea era:

```bash
{ ls -1d 05_calendario/qa/*/ 2>/dev/null || true; } | sort | head -n -6 | xargs -r rm -rf
```

y pasa a ser:

```bash
{ ls -1dt 05_calendario/qa/*/ 2>/dev/null || true; } | tail -n +7 | xargs -r rm -rf
```

(`ls -1d` → `ls -1dt`, y `sort | head -n -6` → `tail -n +7`. En el fichero va con
seis líneas de comentario explicando el porqué, para que nadie lo revierta.)

## Qué arregla

La versión vieja ordenaba los directorios de `05_calendario/qa/`
**alfabéticamente** y borraba todos menos los seis últimos *de esa lista* — no
los seis más recientes en el tiempo. Como **«H» va antes que «S»**, `MDH-###`
ordena siempre delante de `MDS-###` sin importar la fecha. Con los cinco Shorts
de la semana ya guardados, el expediente del **episodio largo del sábado se
borraba recién creado, todas las semanas**, antes de que el paso «Registrar lo
publicado» pudiera comitearlo.

Por eso `05_calendario/qa/MDH-005.es/` no existe: no se perdió, se borró solo.

`ls -1dt` ordena por fecha de modificación, lo más reciente primero, y
`tail -n +7` se queda con todo lo que no está entre los seis primeros. Es decir:
borra los **más viejos**, que es lo que la línea quería decir desde el principio.

## Comprobado

Con siete carpetas y `MDH-005.es` como la más reciente:

- **Antes** (`sort | head -n -6`) → borraría `qa/MDH-005.es/`, la recién creada.
- **Ahora** (`ls -1dt | tail -n +7`) → borra la más antigua y `MDH-005.es` se queda.

## Efecto secundario, y es bueno

A partir del próximo sábado la revisión diaria vuelve a tener los seis fotogramas
y el `ficha.json` del episodio largo el mismo día en que se hace público. Hasta
ahora los sábados revisaba a ciegas.

## Lo que NO se ha tocado

Nada más. Ni el cron, ni el orden de los pasos, ni `qa.py` después de publicar
(sigue siendo un informe, no una barrera: la barrera es la de `render.py`). Un
solo cambio, para que se pueda verificar de un vistazo.
