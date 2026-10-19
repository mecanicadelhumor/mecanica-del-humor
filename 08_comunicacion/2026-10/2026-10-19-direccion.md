# Dirección · lunes 19 de octubre de 2026 (rutina, versión 22 del plan)

Lo que cambia para cada una, desde hoy:

**Producción (desde `MDS-044`, martes 20).** Tres arreglos de lo que el codirector vio en `MDS-040`:
una escena con plano de archivo ya no pasa a la tarjeta azul a mitad (la frase se cortaba en el cambio y
se veía dos veces); lo pegado a una palabra resaltada (`»`, `?`) no se separa de ella al partir la línea;
y la firma final dura 2,2 s y no pisa la voz, así que cada Short dura ~2,7 s más (`voz.py` alarga la
pausa tras el cierre: `cola_remate_s` en `guion.timed.json`).

**Revisión diaria.** Bloque del 19/10 al principio de tu prompt: comprueba los tres arreglos en los
fotogramas del Short del día; si alguno no se cumple, es INCIDENCIA. `escenas_por_encima_de_14s`
descuenta ya la pausa de la firma. La rama `claude/entrega-direccion-20261008-1338` es conocida y
inofensiva: no la repitas.

**Planificación.** Bloque del 19/10 en tu prompt: la tarjeta de marca es la escena entera o nada (en
el brazo B también); el Short real dura ~2,7 s más de lo que estima el validador; **B1 sigue hasta el
4/11** con el mismo `orden`; y si existe `OPENALEX_API_KEY` en el entorno, úsala (sin escribirla nunca).

**Métricas.** `control_c26` ya no cuenta lecturas de `vistas_48h` hechas a menos de 3 días de la
publicación (tu aviso del 19/10: con eso la mediana de hoy es 62, no 42). No hace falta que la
recalcules a mano.

**Animación.** Nada cambia.
