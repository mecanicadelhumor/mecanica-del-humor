# Dirección → rutinas · lunes 9/11/2026 (versión 30 del plan)

**Para todas.** La producción estuvo parada del 06 al 09/11 y **no era Google**: el 06/11 salió `google-genai` 3.0.0, que llama a la API `v1`, donde los modelos TTS no existen (404 «model not found» con todos). Arreglado hoy: `voz.py` fija `api_version="v1beta"` y `requirements.txt` pide `google-genai>=2.34,<3`. **Los modelos vuelven a ser los de antes del 08/11** (`gemini-3.1-flash-tts-preview` y `gemini-2.5-flash-preview-tts`), por decisión del codirector, hasta el apagado del 17/11. «Producir vídeo» relanzado a mano: `MDS-067` ya está subido con `gemini-3.1-flash-tts-preview`, sale hoy a las 18:00 UTC. Trampa 70.

**Revisión diaria.** Si vuelve un 404 de voz: mira primero `pip` (qué versión de `google-genai` instaló el run) antes que el nombre del modelo. No toques `MODELO_GEMINI` ni el tope de `requirements.txt`: el cambio a 3.8 lo hace la dirección el 16/11 (`voz-3.8-cambio`). Mañana sale `MDS-062` (brazo A, animación ya hecha en `05_calendario/animaciones/MDS-062/`) y el sábado 14 `MDS-063`: son los dos que no salieron, recolocados en días vacíos de `parrilla.json`. Su hoja de contactos y la lectura en frío ya se miraron antes del 07/11; con una mirada a la hoja basta. La rama `claude/entrega-revision-20261104-1031` sigue anotada para el codirector, no es incidencia.

**Planificación (jueves 12).** El 10 y el 14 ya no están vacíos; **el domingo 15 sí** (era AD, posición 11). Si hay un guion aprobado, ahí. El banco sigue sin existir (1 aprobado de 7 el 07/11): cualquier guion que pase de más va a `_banco`.

**Métricas.** Nada nuevo. Los Shorts recolocados llevan su brazo en el guion: `bucle.py` los cuenta por guion, no por día.

**Animación.** Nada nuevo: `MDS-062` ya está animado; `MDS-064` (11/11) es el siguiente.
