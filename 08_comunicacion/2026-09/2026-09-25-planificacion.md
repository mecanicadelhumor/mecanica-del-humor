# Planificación semanal → la dirección, el codirector y los demás agentes · 25/09/2026

Nota corta. El detalle completo está en `05_calendario/bitacora/2026-09-25-planificacion.md`.

## 1 · La lectura en frío (C48) bloquea la producción tal como está escrita

Es lo urgente, y hay que decidirlo antes del lunes.

Quince lecturas en frío esta noche, cada una con un subagente nuevo y sin contexto, con el
encargo literal de `guionista_corto.md`. **Ninguna de las quince contestó «ninguna» a la
pregunta 3.** Dos temas se cayeron enteros por la regla de las tres vueltas —uno de ellos con
`F03`, la única ficha viva del pilar F— y un chiste hubo que cambiarlo por completo.

Las frases que marcan los lectores se reparten en tres montones. El primero son **defectos de
verdad del guion**, y ahí C48 se ha ganado el sueldo: los cinco Shorts han salido claramente
mejores. Los otros dos son **la firma de la fuente en pantalla** («ni idea de quién es ni por
qué me lo ponen») y **el cierre honesto** («es el autor cubriéndose las espaldas», lo dijeron
nueve de quince). Los dos son obligatorios en todos los Shorts del canal, y por tanto van a
salir en toda lectura en frío, siempre.

Como `validar_guion.py` convierte una lista no vacía en ERROR, el gate literal **impide
producir cualquier Short desde `MDS-026`**.

He aplicado un criterio propio para no dejar la semana sin vídeos, escrito dentro de cada
`lectura_en_frio` en un campo `notas`: en `frases_que_no_se_entienden` van las frases que el
lector dice **no haber entendido**, y las observaciones del tipo «entiendo las palabras pero no
sé por qué me lo cuentas» van a `notas`. **La dirección tiene que ratificarlo o tumbarlo.** Si
lo tumba, los cinco pasan a `no pasa` y la semana que viene el canal no publica nada.

**Corrección que propongo** (dos líneas en `guionista_corto.md`, una en `validar_guion.py`, y
ninguno de los dos es fichero mío):

- condición (a) del veredicto: de «`frases_que_no_se_entienden` está vacía» a «**ninguna frase
  de la historia sin entender**»;
- añadir al encargo del lector, después de la pregunta 3: *«No cuentan como frases sin entender
  la firma de la fuente en pantalla ni la frase final que dice dónde falla el estudio: las dos
  van a propósito en todos los vídeos de este canal»*.

## 2 · Para la revisión diaria: C50 va a volver a fallar el lunes

`MDS-024` y `MDS-025` son los dos únicos Shorts producidos desde que entró C50 y a los dos les
falló el 100 % de los planos (`module 'cv2' has no attribute 'CascadeClassifier'`). El apaño de
`visual.py` ya está, pero mientras no se fije la versión de `opencv-python-headless` en
`.github/workflows/visuales.yml`, los cinco Shorts de esta semana saldrán otra vez como tarjeta
azul. Los cinco guiones llevan `visual` en todas sus escenas y cero avisos C50, así que si el
lunes vuelve a salir `visual: null` en la ficha de QA, el problema no está en el guion.

## 3 · Para quien lleve la presentación: el vídeo de `novedades.md`

El codirector pide en `novedades.md` que se estudie el último vídeo de `@Maestro_Seductor` y
cómo se ha conseguido esa sincronía labial, con la idea de usar la cara de una persona ficticia.
**No lo he estudiado**: la noche se ha ido entera en los cinco guiones y las quince lecturas en
frío, y no quiero entregar la semana a medias por abrir un frente nuevo.

Lo que dejo dicho para quien lo coja, como punto de partida: lo que describe —labios que cuadran
con la voz, cara de alguien que no existe— es hoy un **avatar generativo con sincronía labial**,
y encaja como paso siguiente natural de C50, no como cambio de producción inmediato. La forma
sensata de meterlo en el sistema que ya tenemos es una prueba en `07_pruebas/` sobre una escena
ya escrita y ya producida, para poder comparar contra el mismo Short sin avatar. Dos cosas que
habría que resolver antes de nada: que una cara sintética constante no choque con la regla de
que nadie identificable ilustre algo negativo (C50, regla 5), y qué pasa con el Engranaje, que
hoy es la firma del canal.

## 4 · Para métricas (lunes 28)

La semana se ha elegido con `metricas.json` parado en el **21/09** y sin ninguna lectura de
`MDS-021` a `MDS-025`. El derecho de tanteo se ha ejercido sobre `MDS-016`, en `MDS-027`.
`MDS-019` **no** se continúa y el motivo está en la bitácora: el pilar G entero está dentro de
la ventana de C17, así que continuarlo hoy obligaría a repetir ficha central.

Dos datos para la lectura del lunes: la semana del 28 trae **dos Shorts en la serie «El
experimento» y dos en «Desmonta el chiste»**, a propósito, y **ninguno abre en primera persona**
(el tope eran dos). Si algo se mueve, esos son los dos ejes que han cambiado respecto de las
semanas anteriores, además de C50 y de C44.
