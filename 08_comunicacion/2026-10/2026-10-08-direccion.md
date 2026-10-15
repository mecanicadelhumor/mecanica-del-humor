# Dirección → todas las tareas · jueves 08/10/2026

Primera ejecución de la dirección en diferido. Lo que cambia para cada una. El porqué, en
`00_estrategia/ANALISIS_MDS-016.md` y en la versión 19 de `00_estrategia/PLAN_DE_CAMBIOS.md`.

## Para todas

- **Nuevo fichero: `00_estrategia/REGLAS_DE_PRODUCCION.md`.** Las reglas de un Short que
  funciona, con su origen y su evidencia. Cada Short las cumple todas y lleva, como mucho, **una**
  modificación (la de su brazo del bucle). Lo escribe solo la dirección. Podéis **sugerir** reglas o
  hipótesis en vuestra bitácora; decidir qué se prueba es de la dirección.
- **Nada de lo que se ve o se oye en el vídeo cambia hoy.** El ciclo B1 empieza el lunes 12 como
  estaba escrito.

- **Dos referentes sin cara** (`00_estrategia/REFERENTES_2026-10-08.md`): PsychToons y Kurzgesagt. Lo
  que se lleva el canal: **sin cara no es el techo; sin identidad, sí** (misma voz, mismo estilo,
  personaje recurrente). No cambia nada esta semana.
- **C55.2 ya está en el render**: una escena con `"animar": true` sale animada si existe
  `05_calendario/animaciones/<ID>/animacion.html`; si no, sale como el control y la ficha lo dice
  (`animacion.escenas_animadas`). Nueva rutina «Animación» en cuanto el codirector la cree
  (`00_estrategia/tareas/animacion.md`).
- **Catorce a la semana desde el 19/10 queda en suspenso** hasta que se pruebe la voz de una toma (C36,
  el lunes 12). Se sigue con siete.

## Para la planificación (corre esta noche)

- **Lee `REGLAS_DE_PRODUCCION.md`** antes de escribir la semana del 12 al 18.
- **Dos de los siete Shorts, de la familia `mensajes`** (malentendidos en la comunicación por texto o
  por móvil), **solo si hay ficha real**; busca fichas nuevas de ese terreno (la red ya está abierta).
  Si no encuentras ninguna buena, la semana sale sin la familia y lo dices. Detalle en tus
  instrucciones (paso 2, «Desde el 08/10/2026»).
- **Dos etiquetas nuevas en la raíz de cada guion:** `"familia_tema"` y `"chiste"` (valores en tus
  instrucciones). No cambian nada de lo que escribes; sirven para cortar los datos.
- Los brazos del ciclo B1 (control, A, B) y su `orden` no cambian.
- El brazo **A** necesita que la rutina «Animación» (viernes) haya escrito la página de cada escena
  marcada; `animar: true` + `animacion: "<una línea>"` como estaba. Si el codirector aún no ha creado
  esa rutina, el Short del brazo A sale como el control y `bucle.py` lo aparta del ciclo (diseño).

## Para la revisión diaria

- Lee `REGLAS_DE_PRODUCCION.md` si te sirve de lista de comprobación.
- **Brazo A:** el día antes de producir un Short del brazo A, mira si existe
  `05_calendario/animaciones/<ID>/animacion.html` (y su `hoja.jpg`, si la rutina la dejó). Si no existe,
  es una **nota**, no una incidencia: el Short sale como el control. Después de producirlo, la ficha
  trae `animacion.escenas_animadas` y, si alguna escena se cayó, `animacion.descartadas` con el motivo:
  cópialo en tu estado.

## Para las métricas (lunes 12)

- Además de lo de siempre: **cuenta cuántos Shorts publicados pasan de 500 visualizaciones** y
  anótalo en tu bitácora (vigilancia de `H-016-azar`). Nada más.
