# Bitácora · Dirección en diferido · lunes 12 de octubre de 2026

Rutina «Dirección», 13:07 UTC. Sin sesión interactiva hoy (ningún commit de dirección ajeno en `main`).
Versión **20** del plan.

## Lo que encontré al llegar

- **El arranque de la rutina apunta a `00_estrategia/tareas/direccion.md`, que ya no existe** en el
  público: el codirector lo pasó al privado el 09/10. Lo encontré allí (idéntico al último del público) y
  lo seguí. Trampa 58; se le pide que cambie el arranque.
- Los prompts de revisión y métricas que el codirector devolvió al público el 09/10 son idénticos a los
  de antes; el de planificación del público es el bueno (trae el bloque del 08/10). Todo correcto.
- La rama `claude/entrega-direccion-20261008-1338` sigue viva; su contenido está en `main` (`991288b`,
  `fe3332b`). No la borro: no tengo con qué hacerlo sin `push --delete`, y el próximo `--aplicar` la
  limpia. Se queda dicho.
- La lectura completa del lunes de `metricas.yml` no ha llegado a las 13:10 UTC (el cron llega con 6-7 h
  de retraso toda la semana). La diaria del 11/10 sí.
- La rutina «Animación» corrió el viernes 9: páginas de `MDS-038`, `039` y `042`, barrera limpia.

## Lo decidido y hecho

1. **`MDS-035` (punto 1 del cuaderno).** El guion no repetía nada: la toma de Gemini del cierre dijo la
   frase dos veces (17,1 s para 20 palabras; Whisper oye 41). Lo marcaba la ficha
   (`escenas_ritmo_fuera_de_rango: [[6, 1.17]]`) como aviso y nadie lo leyó a tiempo. **C66** en
   `voz.py`: Whisper `tiny` comprueba cada toma; techo de duración más bajo. Calibrado sobre 129 tomas:
   solo `MDS-035`/6 y `MDS-020`/3 (dirección de actor leída en alto, en septiembre). Probado con Gemini
   simulado (caché mala borrada, reintento, tres fallos → la escalera de siempre, sin Whisper → solo
   duración). `requirements.txt` resuelto para Python 3.12.
2. **Revisión diaria**: bloque del 12/10 — la ficha del Short del día se lee antes de las 17:00 UTC; los
   campos de voz están en `guion`; toda cifra se copia de su fichero (el 11/10 dijo 0 para `MDS-034`, que
   tenía 97).
3. **C36**: `corte_palabras.py`, 70 de 70 fronteras sin conexión. Prueba en vivo el jueves 15.
4. **C55.4**: más color en la animación (respuesta del codirector), desde el viernes 16.
5. **C67**: `00_estrategia/LARGOS_2026-10.md`, la propuesta de los largos (tarea especial).
6. **Firma «de lunes a viernes»**: se le pregunta al codirector (hay Shorts en fin de semana desde hoy).

## Lo que no hice

- Trampa 55 (render no determinista): al jueves.
- C36 en vivo: necesita la clave de Gemini (solo en Actions).
- Nada en el bucle: B1 empieza hoy, sin marcador.
