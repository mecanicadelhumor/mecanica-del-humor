# Bitácora · Dirección en diferido · lunes 2 de noviembre de 2026

Rutina «Dirección» (13:33 UTC). Sin sesión interactiva hoy (en `origin/main` ningún commit de dirección
ajeno; en el privado, el codirector añadió dos notas al cuaderno y su respuesta a las tareas del 29/10).

```
05122de revisión diaria 2026-11-02
86f38a6 Registro y expediente de calidad: MDS-057
2c705fd registro: sincronizado con YouTube 2026-11-01
$ git ls-remote origin 'refs/heads/claude/entrega-*'   → (nada)
```

Leído: `tareas/direccion.md`, `REGLAS.md`, plan v26-v27, `PROMPT_DE_ARRANQUE.md` (trampas 64-66 y
«Dónde está» del 23 al 29/10), el cuaderno (nuevo desde `c5e34ab`: «Títulos» y «Vídeo del viernes») y la
respuesta del 29/10 («cara: sí, pero antes»), `compromisos.json`, estado del 02/11, revisión del 02/11,
`revisiones/MDS-058.md`, planificación del 29/10, `bucle/` entero.

## Lo vencido (todo con dueño dirección, vencía hoy)

| Compromiso | Qué ha pasado |
|---|---|
| `cara-final-aplicar` | **Hecho**, adelantado como pidió el codirector (abajo) |
| `iteracion-factorial`, `iteracion-bayes`, `B2-regla-pocas-vistas` | **Hechos**: B2 en `ciclos.json` y `bucle.py` |
| `tts-vigilancia` | **Hecho** (informe en `07_pruebas/prueba-de-voces/VIGILANCIA_TTS_2026-11.md`): **los dos modelos de voz se apagan el 17/11** |
| `C51.3-alternativas` | **Hecho** (informe en `07_pruebas/presentador-2026-10/ALTERNATIVAS_INFORME_2026-11-02.md`) |
| `lectura-frio-29-10` | **Hecho**: 6 de 14 temas pasaron |
| `iteracion-14` | **Aplazado al 16/11**, con su porqué |
| `MDH-008-guion` | Marcado hecho (lo pedía la revisión) |

## Lo roto

- **La voz** (lo más serio de hoy): Google retira `gemini-3.1-flash-tts-preview` y
  `gemini-2.5-flash-preview-tts` el **17/11/2026**. Lo comprobé yo en la página de retiradas, no me quedé con
  el informe del subagente. Sin cambiar, desde el 17/11 los Shorts salen con edge-tts o no salen. Hecho:
  `_solo_pcm` en `voz.py` y `prueba_voz.py` (si los 3.8 devuelven WAV, se le quita la cabecera; si no es
  mono 16 bits 24 kHz, para); probado con un PCM, un WAV de 24 kHz y uno de 48 kHz (para). Workflow de la
  prueba con los 3.8 para el codirector. Trampa 68.
- **`MDS-057`** (sale hoy 18:00Z, INCIDENCIA de la revisión): **se deja salir**. Retirarlo es tocar YouTube a
  mano (no lo hago sin el codirector) y es la posición 22 de B1.
- **`MDS-058`** (se produce esta noche, INCIDENCIA): apliqué la propuesta de la revisión y le pasé lectores
  nuevos. **Tres vueltas, tres «me iría en la 4»** (vuelta 1 además tropezó con «en el instituto»). Devuelto
  a la versión de la planificación, la que pasó su lectura oficial: mis versiones no eran mejores, y un
  Short que no sale es un dato que B1 no tiene. Lo que sí sale de aquí es la trampa 67.

## El bucle

- **B1, A**: «gana con reparo (más ceros de feed)». Lo decido: **no entra en el control de B2** y sigue
  como factor (porqué en `ciclos.json`, «decisiones»). B gana (26/10) → control de B2.
- **B2 escrito**: factorial 2×2 animación × corto, `orden` con semilla 20261102 (D, AD, A, control, …),
  posiciones por día, regla bayesiana, <10 vistas fuera. `bucle.py --imprimir` corre con B1 igual que antes
  y B2 en «faltan datos». La regla probada con datos inventados: GANA, PIERDE, SIN EFECTO, faltan datos y
  reparo por ceros de feed. `resultados.json` no lo subo (lo escribe `metricas.yml`).
- Ajustados a su brazo: `MDS-060` (D, sin la escena 3; lectura nueva: pasa), `MDS-062` (A, animar 4 y 5).

## El cuaderno

1. **Vídeo del viernes.** Escribí `MDS-061` (`E18`, sonrisa forzada; AD). Tres lectores: no pasa
   (la 3ª: «me quedo», pero tres frases tarde). Borrador en `07_pruebas/MDS-061-2026-11-02/`; el jueves
   5 la cuarta vuelta y la animación. **El arreglo de fondo**: tres lectores con mayoría y el banco
   (`guionista_corto.md`, `planificacion-jueves.md`, precisiones del 02/11).
2. **Títulos.** `H-titulo-afirmacion` a la cola (`hipotesis.json`), baja prioridad en Shorts.
3. **Cara del final.** Hecha (abajo).

## Código

- `escena.html`: la sonrisa del final empieza `A_RISA_ANTES_S` = 1,1 s antes de la tarjeta. Muestra
  renderizada en el contenedor (`07_pruebas/cara-final-2026-11-02/`): a 1,7 s del final ya sonríe; en la del
  29/10, no. Cero capturas más.
- `bucle.py`: `veredicto_bayes`, factores, pocas vistas.
- `voz.py`, `prueba_voz.py`: `_solo_pcm`.

## Para la próxima dirección (jueves 5)

`MDS-061` (vuelta 4 con tres lectores, animación, parrilla antes de las 01:13 UTC del viernes); la prueba
de voces 3.8 si el codirector movió el workflow; cerrar B1; imagen horizontal y voz por tandas del largo.
