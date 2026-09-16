# P1 · Profundidad — la opacidad de la retícula, no se puede decidir leyendo

**Dejada por la revisión diaria del 16/09/2026.**

## Qué mirar, en este orden

1. `A_actual_opacidad-055.png` — cómo se ve hoy en producción (escena 5 de MDS-018, a tamaño real 1080×1920, tipografías de verdad).
2. `B_literal-4pct_invisible.png` — la misma escena con `#reticula{opacity}` bajado a **0,04** (el número literal del encargo, «rejilla de taller al 4 % de opacidad»), sin tocar nada más. **La retícula desaparece del todo**: a este contraste de color (`#16213A` sobre `#0B1220`, dos azules casi iguales) el 4 % no se lee como fondo, se lee como fondo plano. Eso choca con la razón que el propio encargo da para pedirlo: «la rejilla de taller es la marca». Una marca que no se ve no es la marca.
3. `C_implementado_vineta-delante_mismo-055.png` y `D_implementado_cierre_con-remate.png` — lo que sí he aplicado ya a `escena.html`, sin esperar esta respuesta porque no dependía de ella: la viñeta ahora pinta **delante** del contenido (antes pintaba detrás y no oscurecía nada; C29... perdón, P1 pedía «viñeta delante» y hoy cumple), y el fondo **deriva un 1,5 % de la altura, en el sentido contrario a como entra el texto** (el texto sube al entrar; el fondo baja despacio mientras la escena se asienta), function de `t` con la misma curva `suave()` de la entrada — determinista, regla 11.5. La opacidad de la retícula la he dejado **tal cual estaba (0,55)** a propósito: es la pieza que no podía decidir sola.

## Qué pregunta contesta

**¿Se baja la opacidad de la retícula, y a qué valor?** No es una pregunta que se conteste leyendo el número del encargo: al contraste de color real que tiene el sistema de diseño, «4 %» y «no se ve nada» son la misma cosa, y eso no puede ser lo que se quería. Necesito verlo decidido por alguien mirando la B, no infiriéndolo yo del texto del encargo.

## Qué pasa con cada respuesta

- **«Déjala en 0,55, como está» (o cualquier valor que la mantengas visible):** cierro el encargo tal cual lo dejé — viñeta delante y deriva ya aplicadas, opacidad sin tocar — y lo anoto como resuelto.
- **«Bájala, pero no al 4 %; prueba con X»:** dame el número (o un rango) y lo aplico y vuelvo a dejar una comparación aquí antes de darlo por cerrado — es un cambio de una línea, no hace falta repetir todo el resto.
- **«Sí, el 4 % literal, así de sutil»:** lo aplico tal cual, aunque a mí me parece que borra la marca en vez de sostenerla — dicho porque es mi trabajo decirlo, no para insistir después de que se decida.

## Nota técnica para quien retome esto

`03_produccion/pipeline/vista.py` llevaba desde su creación (04/09) sin poder previsualizar un Short de verdad: `escenas_de()` nunca copiaba el campo `formato` del guion a cada escena, así que `cargar()` nunca veía `"corto"` y toda vista con `--guion` salía en el lienzo horizontal (1920×1080) aunque el guion fuera vertical. Lo he corregido hoy (arreglo de defecto, no consume ranura de la regla 11.1): ahora `--guion <ruta-a-un-corto>` pinta en 1080×1920 de verdad. Las cuatro capturas de esta carpeta están hechas con la herramienta ya corregida — antes de hoy esto no se podía haber comprobado así.
