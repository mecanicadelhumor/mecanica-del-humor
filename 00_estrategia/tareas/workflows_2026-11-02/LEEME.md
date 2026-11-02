# Workflow para mover (02/11/2026) · la prueba de voces con los modelos nuevos

**Qué es:** `voz_prueba.yml` con dos opciones más en el desplegable «modelo»: `gemini-3.8-flash-tts`
(queda como opción por defecto) y `gemini-3.8-flash-lite-tts`. Nada más cambia.

**Por qué:** Google apaga el **17/11/2026** los dos modelos de voz que usa el canal
(`gemini-3.1-flash-tts-preview` en los Shorts y `gemini-2.5-flash-preview-tts` en el largo). Lo dice su
página oficial de retiradas: <https://ai.google.dev/gemini-api/docs/deprecations>. Sin la prueba no se
puede escoger sustituto, y sin sustituto, desde el 17/11 los Shorts salen con edge-tts o no salen.

**Cómo moverlo (una vez):** en GitHub, abre `.github/workflows/voz_prueba.yml` → lápiz → borra todo →
pega el contenido de este `voz_prueba.yml` → «Commit changes» a `main`. Es el mismo fichero con las
líneas 33-40 cambiadas (el bloque `default:` / `options:` del input `modelo`).
