# `sincroniza_registro.yml` — diseño de C31, 15/09/2026

**Qué hay aquí:** el `.yml` completo de un workflow nuevo. Cópialo a
`.github/workflows/sincroniza_registro.yml` y súbelo cuando quieras encenderlo
— esa carpeta está protegida contra escritura remota (regla 11.7), por eso se
deja aquí en vez de escribirse directamente.

**No hace falta nada más para que funcione.** El código del que depende
(`sincronizar_registro()` y `corregir_registro()` en `04_agentes/metricas.py`,
y el flag `--solo-registro`) ya está en el repositorio, escrito hoy y probado
con un cliente de YouTube simulado (dos casos: corrige una entrada, no toca
nada cuando ya coincide — ver el propio `metricas.py`, función
`sincronizar_registro`, para el porqué). El secreto que necesita
(`YT_REFRESH_TOKEN` + `YT_CLIENT_ID` + `YT_CLIENT_SECRET`) ya está en el sitio
correcto: es el mismo que usa `metricas.yml`, y esta vía no necesita el ámbito
`yt-analytics.readonly` que a ese token a veces le ha faltado.

## Qué hace, en una frase

Dos veces cada madrugada (08:50 y 09:10 UTC, después del último cron de
`producir.yml`) le pregunta a la Data API de YouTube el estado real de cada
vídeo del registro y corrige `registro_publicaciones.json` si no coincide con
lo que dice. No toca `metricas.json`, no mide nada y no compite con
`metricas.yml`, que sigue siendo el único que calcula la mediana de C26 y solo
corre el lunes.

## Qué pregunta contesta

**¿Hace falta más para que la revisión diaria deje de necesitar la regla del
«no lo sé» del caso MDS-011, o con esto basta?**

La regla («la primera vez es incidencia, a partir de la segunda se anota y no
se repite como incidencia») seguirá haciendo falta siempre que el registro
pueda estar desactualizado — un vídeo publicado o retirado a mano entre la
última pasada de este workflow y las 11:30 sigue siendo posible, aunque la
ventana pase de seis días a unas pocas horas. Lo que este workflow cambia es
cuánto puede durar la mentira, no si puede existir.

## Qué pasa con cada respuesta

- **Si con esto basta** (la ventana de unas horas ya no produce falsos
  positivos en la práctica): se sube tal cual, y la regla del «no lo sé» se
  queda como red de seguridad para el caso raro, no como rutina diaria.
- **Si no basta** (sigue habiendo casos): hay dos vías, no excluyentes — subir
  la frecuencia (un tercer disparo más cerca de las 11:28, o que la propia
  revisión diaria llame `python3 04_agentes/metricas.py --solo-registro`
  como primer paso de su sesión, sin esperar a Actions) o investigar si el
  caso es en realidad la doble cara del token de `00_estrategia/TOKEN_DE_YOUTUBE.md`
  (un token sin el ámbito correcto tampoco corrige nada, y este workflow no
  lo distingue de «no había nada que corregir» — el log del paso «Corregir
  registro…» sí lo dice, si algo falla ahí es el primer sitio donde mirar).

## Dos cosas que se han dejado fuera a propósito

- **No reintenta con backoff.** Si la llamada a `videos.list` falla (token
  caducado, 5xx de Google), el paso falla y el workflow no hace commit; la
  siguiente pasada de las 09:10, o la del día siguiente, lo vuelve a
  intentar. No es una escalera como la de `voz.py` (C33.1) porque aquí no hay
  nada que perder por esperar: el registro se queda como estaba, que es
  exactamente lo que pasa hoy sin este workflow.
- **No añade `revisado`.** El campo que la nota de `registro_publicaciones.json`
  describe («lo marca el agente de revisión de calidad cuando ya ha sacado
  conclusiones») lo sigue sin tocar este workflow ni la revisión diaria: las
  instrucciones vigentes de la revisión diaria dicen explícitamente que ese
  fichero no entra en su paquete. Si se quiere que ese campo se use de
  verdad, es una decisión aparte.

---

*(Respuesta del codirector, cuando la haya, se añade aquí debajo con fecha y
firma — regla de `07_pruebas/LEEME.md`.)*

# Respuesta del codirector:
Hecho hoy 15/09 (subido el workflow también a su carpeta adecuada).