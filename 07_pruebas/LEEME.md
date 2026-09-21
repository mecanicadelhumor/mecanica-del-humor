# 07_pruebas — el buzón de ida y vuelta

**Creada por el codirector el 4 de septiembre de 2026.** Es para lo que no se puede
decidir leyendo: audios que hay que escuchar, capturas que hay que mirar,
opciones entre las que hay que elegir con los sentidos y no con un argumento.

## La regla

**Una carpeta por prueba, y un `.md` al lado con el mismo nombre.** El `.md` dice
tres cosas y nada más:

1. **Qué hay que mirar o escuchar**, en qué orden.
2. **Qué pregunta contesta.** Una, concreta. No «¿qué te parece?».
3. **Qué pasa con cada respuesta.** Si la respuesta no cambia nada, la prueba no
   hace falta.

Cuando la prueba se ha contestado, la respuesta se añade **al final del mismo
`.md`**, con fecha y quién la da. No se borra nada: una prueba respondida es la
justificación escrita de una decisión, y dentro de un mes será lo único que
explique por qué se hizo lo que se hizo.

## Quién escribe aquí

Cualquiera de los tres, y por eso hay que firmar:

- **La dirección** (yo) deja pruebas cuando una decisión depende de algo que
  el codirector tiene que oír o ver.
- **La revisión diaria** deja pruebas cuando encuentra dos opciones y no puede
  elegir sola. Su prompt le dice que mire esta carpeta.
- **El codirector** deja aquí lo que quiere que se mire, como hizo con las voces.

Esta carpeta **no la produce nadie automáticamente** y no entra en ningún
paquete de tarea programada. Es material, no código: nada de aquí se ejecuta.

## Lo que hay

| Carpeta | Qué es | Estado |
|---|---|---|
| `prueba-de-voces/` | Las tres locuciones de MDS-010: `edge` (lo de hoy), Gemini sin dirección y Gemini con dirección | **Respondida el 04/09.** Ver `prueba-de-voces.md` |
| `voz-adelantada-14-09/` | No es una prueba de oído: es el diseño de `voz_adelantada.yml` (C27-B), listo para copiar a `.github/workflows/` — esa carpeta está protegida en remoto, igual que `producir-yml-07-09/`. Ver su `LEEME.md`. | **Entregado el 13/09.** Falta que el codirector lo suba y, si quiere, lo lance a mano una vez con presupuesto bajo antes de dejarlo en cron. |
| `registro-diario-15-09/` | Diseño de `sincroniza_registro.yml` (C31): llama a `metricas.py --solo-registro` dos veces cada madrugada para que el registro de publicaciones no lleve hasta seis días desactualizado. Deja la función correspondiente (`sincronizar_registro()`) ya escrita y probada en `04_agentes/metricas.py`. Ver su `LEEME.md`. | **Entregado por la revisión diaria el 15/09.** Falta que el codirector lo suba a `.github/workflows/`. |
| `P1-profundidad/` | Comparación con capturas reales (tamaño y tipografía de producción) de la opacidad de la retícula: al 0,55 de hoy y al 4 % literal del encargo P1, que la borra del todo. La viñeta-delante y la deriva del fondo del mismo encargo ya están aplicadas en `escena.html` sin esperar esta respuesta. Ver `P1-profundidad.md`. | **Resuelta el 21/09 por el codirector: se deja en 0,55, como estaba.** Ningún cambio de código pendiente — el encargo P1 (retícula, viñeta delante, deriva) queda cerrado. |
| `metricas-diarias-21-09/` | Diseño de `metricas_diarias.yml` (C47): llama a `metricas.py --diario` cada madrugada para que la revisión diaria pueda ver si un vídeo lleva 24h a 0 visualizaciones, sin esperar al lunes. Deja la función correspondiente (`escribir_metricas_diarias()`) y el flag `--diario` ya escritos y probados en `04_agentes/metricas.py`. Ver su `LEEME.md`. | **Entregado por la revisión diaria el 21/09.** Falta que el codirector lo suba a `.github/workflows/`; hasta entonces `metricas_diarias.json` no existe y la revisión diaria no puede aplicar la regla de las 24 horas. |
