# Dirección en diferido · jueves 5/11/2026

- Arranque: sin sesión interactiva hoy (ningún commit «dirección» ajeno en `origin/main`). Cuaderno nuevo desde el 02/11 (commit `6a6bdbc`): «Carpeta tareas» e «Incoherencias». Respuesta del codirector al 02/11: tarea 1 hecha (`voz_prueba.yml`) y movido también `presentador_prueba.yml`.
- **Incoherencias (`MDS-057`)**: causa en `visual.py` (`relevancia()` contaba palabras sin distinguir el sujeto). 7 de 10 planos de `MDS-057` y 81 de 308 planos de archivo en todos los manifiestos. Arreglo: núcleo + animales + primer plano estricto (0,5, sin flojos). `VERSION = 2`. Probado con búsquedas simuladas (el elefante para «gorilla» queda fuera; el primer plano sin IA sale tarjeta) y con el resolver entero sobre una copia. Trampa 69.
- **`MDS-061`**: vueltas 4, 5, 6 con tres lectores cada una; no pasa (3/3 en la vuelta 6 no distinguen «a propósito» del lápiz). Viernes 6 sin Short; E18 a la reserva como tema de seis escenas.
- **Voz 3.8**: «Prueba de voces» sobre `MDS-060`. `gemini-3.8-flash-tts`: bien (run 42034577185; 30 s plano, 58 s dirigido; 24 kHz). `-lite`: primer intento, `APITimeoutError` del cliente a los 4 min (run 42034836337); relanzado. Referencia 3.1 detrás.
- **Largo**: imagen horizontal en `visual.py` (`poner_formato`), probada con simulación y con recortes reales de ffmpeg a 1920x1080. Voz por tandas aplazada al 12/11 (con 3.8: 2.5-flash caduca el 17/11). Ensayo al 12/11.
- **B1** cerrado en `ciclos.json`.
- **Limpieza** (cuaderno): workflows aplicados borrados en las dos carpetas; `c` y `Claude outputs/` fuera de la raíz; `LEEME.md` en las dos carpetas «tareas».
- `compromisos.json`: hechos `C51.3-workflow-apt`, `voz-3.8-mover` (03/11, codirector), `B1-cierre`, `largo-imagen-horizontal`, `MDS-061-jueves`; aplazados `largo-voz-tandas` y `largo-ensayo` al 12/11; nuevos `visual-relevancia-nucleo` (9/11) y `voz-3.8-oir` (codirector, 11/11).
- Plan: versión 29.
