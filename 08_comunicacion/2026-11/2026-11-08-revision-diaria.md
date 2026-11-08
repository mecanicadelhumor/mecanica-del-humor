# Revisión → dirección y producción · 08/11/2026

**Producción parada por el 404 de los modelos de voz.** Google devuelve «model not found» para `gemini-3.1-flash-tts-preview` y `gemini-2.5-flash-preview-tts` (run 42458171312, 08/11). Sin voz no se sube nada: MDS-062 (07/11) y MDS-063 (08/11) no salieron. He cambiado `voz.py` a `gemini-3.8-flash-tts` (+ `-lite` de respaldo), sin probar en vivo y sin que el codirector haya oído la muestra. Falta: que «Producir vídeo» se relance a mano tras aplicar la entrega. Si el 3.8 falla también, la causa estará en el log del paso «Sintetizar narración».
