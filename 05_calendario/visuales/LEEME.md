# 05_calendario/visuales/ — la imagen de cada Short (C50)

*Creado por la dirección el 23/09/2026. Versión 13 de `00_estrategia/PLAN_DE_CAMBIOS.md`, C50.*

Desde `MDS-024` cada escena de un Short lleva vídeo de archivo o una imagen generada detrás del
texto. Lo que se ve en cada momento lo escribe la planificación en el campo `visual` de cada
escena del guion; **esta carpeta es lo que sale de ahí**.

| Fichero | Qué es | Quién lo escribe |
|---|---|---|
| `<ID>.json` | **El manifiesto.** Cada plano de cada escena: de dónde sale (Pexels, Pixabay, imagen generada o tarjeta de marca), su autor, su enlace y su licencia (regla 9), en qué palabra entra (`desde`), cuánto se mueve, dónde tiene las caras y dónde va el texto (`texto_pos`). Y lo que se descartó y por qué (`descartes`) | El workflow «Visuales (C50)» (`visual.py resolver`). **Nadie lo edita a mano** |
| `<ID>.jpg` | **La hoja de contactos.** Un cuadro por plano con la banda del texto, las caras en rojo y, debajo, la frase que suena durante ese plano. Se borra a los 14 días de publicado el Short | El mismo workflow |
| `<ID>/` | Las imágenes generadas con IA de ese Short (no se pueden volver a descargar). Se borran a los 14 días de publicado | El mismo workflow |
| `diagnostico.json` | Qué contestó cada servicio (Pexels, Pixabay, Cloudflare) la última vez que cambió algo | El mismo workflow |
| `ajustes.json` | **Las correcciones de la revisión diaria**: excluir un clip, cambiar una búsqueda, pedir la imagen generada o una tarjeta de marca para un plano, o mover el texto. Al subirlo, el workflow vuelve a elegir | **La revisión diaria** (regla 10). Formato en `00_estrategia/tareas/revision-diaria.md` |
| `APAGADO` | **El interruptor.** Si existe (vacío basta), todos los Shorts salen como siempre, sin vídeo detrás. Para volver, se borra | El codirector o la dirección, nadie más |

**Cómo llega al vídeo:** en `producir.yml`, el paso «Traer el material visual (C50)» baja los planos
del manifiesto a `build/<ID>/visual/` antes del render (el render no usa la red, regla 11.6), y
`render.py` los compone con el texto encima. Si falta el manifiesto, si un plano no baja o si el
modo archivo falla, lo que falle sale como tarjeta de marca, o el Short entero como siempre: **una
imagen nunca cuesta un vídeo**. Lo que salió de verdad queda en `05_calendario/qa/<ID>/ficha.json`,
campo `visual`.
