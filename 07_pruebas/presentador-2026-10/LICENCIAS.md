# Presentador sintético · primero, las licencias

**Dirección, 30/09/2026.** Versión 16 del plan, C51.3. Regla 7.1 de `REGLAS.md` (la persona
sintética, sí, con cinco condiciones). **Nada de esto ha corrido todavía**: es el estudio que va
antes de escribir una línea del cuaderno de Kaggle, porque la tarea 2 del 29/09 lo prometía así —
*«primero, comprobar la licencia de cada pieza (algunos modelos abiertos de sincronía labial
dependen de piezas que no permiten uso comercial)»*—, y resultó ser verdad en casi todos: de siete
modelos mirados, solo uno sirve, y con un cambio.

---

## 1 · Kaggle ya está listo, y lo que puso el codirector está bien

- Cuenta de la marca (`mecanicadelhumor@gmail.com`), teléfono verificado y un token creado. Kaggle
  ya no descarga `kaggle.json`: los tokens nuevos son **una sola cadena**, y la herramienta de Kaggle
  la lee de la variable `KAGGLE_API_TOKEN`. **Con esos tokens no hace falta el nombre de usuario.**
  El método viejo (`KAGGLE_USERNAME` + `KAGGLE_KEY`, el que describía la tarea) sigue existiendo solo
  para las claves antiguas. Fuentes: la documentación de `kaggle-api` y el PR #863 de ese repositorio.
- Los dos secretos de GitHub valen tal como están:
  - `KAGGLE_KEY` → el workflow de la prueba lo pasará como `KAGGLE_API_TOKEN: ${{ secrets.KAGGLE_KEY }}`.
    No hay que renombrar nada.
  - `KAGGLE_USERNAME` = `mecanicadelhumor` → **era la buena**. El nombre del token
    (`mecanica-token`) no sirve para nada fuera de la página de Kaggle. Hace falta el usuario igualmente,
    pero para otra cosa: el identificador de un cuaderno es `<usuario>/<nombre>`.
  - Una comprobación que conviene hacer una vez (diez segundos): que la dirección de tu perfil en
    Kaggle sea `kaggle.com/mecanicadelhumor`. Si fuera otra, ese secreto se cambia por lo que ponga ahí.

## 2 · Qué piezas hacen falta

Un presentador que habla dos o tres segundos son **tres cosas distintas**, y la licencia se mira en
cada una (y en cada pieza que cada una se descarga por dentro):

1. **La cara**, una vez y para siempre (regla 7.1.2: siempre la misma).
2. **El movimiento de la cabeza**: los modelos de sincronía labial solo mueven la boca **sobre un
   vídeo que ya existe**. Una foto quieta con la boca moviéndose se ve como una máscara.
3. **Los labios**, a partir de la voz del narrador (Gemini, la misma de siempre: regla 7.1.2, una sola
   voz).

## 3 · Las licencias, pieza a pieza

Comprobado el 30/09 en el código de cada repositorio (no solo en su portada) y en la ficha de cada
modelo. «Uso comercial» importa aunque hoy el canal no gane dinero: el día que entre en el programa de
socios de YouTube, todo lo que salga en él será uso comercial, y no se puede volver atrás de un vídeo
publicado.

| Pieza | Código | Pesos | Lo que se descarga por dentro | Veredicto |
|---|---|---|---|---|
| **FLUX.1 [schnell]** (la cara) | Apache 2.0 | Apache 2.0 | — (lo sirve Cloudflare, como en C50) | ✅ **Sirve.** Ya lo usamos |
| **Wav2Lip** | «solo uso personal, de investigación o no comercial» | ídem | — | ❌ No |
| **SadTalker** | Apache 2.0 | — | **Basel Face Model**: licencia **no comercial** | ❌ No |
| **Hallo / Hallo2**, **LivePortrait** | MIT | — | **InsightFace**: modelos «solo para investigación no comercial» | ❌ No |
| **LatentSync 1.5 / 1.6** (ByteDance) | Apache 2.0 | Apache 2.0 | **InsightFace** para detectar la cara **al generar**, no solo al entrenar (`latentsync/utils/face_detector.py`) | ⚠️ Solo cambiando el detector. Segunda opción |
| **EchoMimic v1 / v2** (Ant Group) | Apache 2.0 | **sin licencia declarada** en su ficha, y «pensado para investigación académica» | `sd-image-variations` (CreativeML OpenRAIL-M, «para investigación») | ❌ No, mientras los pesos no tengan licencia |
| **MuseTalk 1.5** (Tencent Music) | **MIT** | **MIT**: «disponibles para cualquier fin, también comercial» | whisper-tiny (MIT) · sd-vae-ft-mse (MIT) · DWPose y mmpose (Apache 2.0) · S3FD de `face_alignment` (BSD-3) · resnet18 de torchvision (BSD-3) · **BiSeNet `79999_iter.pth`** | ✅ **La primera opción**, con un cambio (abajo) |
| **Wan 2.2 TI2V-5B** (el movimiento) | Apache 2.0 | Apache 2.0 *(a confirmar en su ficha al descargarlo)* | — | ✅ Candidato. Lo que no sé es si cabe en la GPU de Kaggle a una velocidad razonable: es lo primero que mide la prueba |

**El cambio en MuseTalk.** Todo es MIT, Apache o BSD salvo un fichero: `79999_iter.pth`, el modelo
que separa la boca del resto de la cara para pegar la boca nueva. Su código es MIT, pero está
entrenado sobre **CelebAMask-HQ**, un conjunto de fotos que solo se puede usar para investigación no
comercial. Que los pesos hereden esa restricción es discutible; **en este canal lo discutible no
entra** (regla 9, la misma prudencia que con la música CC BY-NC). Solo sirve para hacer una máscara,
así que se sustituye por la malla facial de **MediaPipe** (Apache 2.0) o, para una cara siempre
frontal, por una elipse fija. Es una función de unas decenas de líneas.

**Y lo que la regla 7.1 pide además de la licencia**, para que quede junto: la cara se genera una vez
y, si se parece a alguien conocido, se genera otra (7.1.1); se declara en la descripción y con
`containsSyntheticMedia`, que `publicar.py` ya sabe poner desde C50 (7.1.3); nunca habla en primera
persona de una vida que no tiene (7.1.4); y como mucho dos momentos de dos o tres segundos por Short
(7.1.5).

## 4 · La prueba, cuando toque (no esta semana)

En `07_pruebas/presentador-2026-10/`, con coste cero en euros y la cuota de GPU de Kaggle:

1. **La cara.** Ocho retratos con FLUX schnell (Cloudflare, las mismas claves de C50), todos
   ficticios, fondo neutro, mirando a cámara. **El codirector elige uno, o ninguno** (regla 11.2).
2. **Un cuaderno privado de Kaggle** que hace, con la cara elegida y una frase de la voz de un Short
   ya publicado (de la caché: cero peticiones a Gemini):
   (a) tres segundos de cabeza en reposo con Wan 2.2, a 480p; (b) MuseTalk 1.5 encima, con la
   máscara de MediaPipe en vez de BiSeNet; (c) el resultado y lo que tardó cada paso.
3. **Un workflow de prueba**, `presentador_prueba.yml`, solo a mano (`workflow_dispatch`), que sube el
   cuaderno con `KAGGLE_API_TOKEN`, espera y deja el vídeo en esta carpeta. Como todo lo de
   `.github/workflows/`, **lo crea el codirector a mano**.
4. **Lo mira el codirector, y nada entra en un vídeo sin eso** (C51.2).

**Cuándo:** no antes de la semana del 12/10. Esta semana se mide la imagen real (C50) y la siguiente
también; y la prueba de la animación a medida (C55) va antes porque ya está hecha. Se lo diré en su
fichero de tareas cuando haya algo que mirar.

## 5 · Lo que no está comprobado, dicho

- **Si Wan 2.2 cabe en la GPU gratuita de Kaggle** y cuánto tarda en tres segundos. Si no cabe, hay
  que buscar otra forma de mover la cabeza, y esa pieza vuelve a este documento con su licencia.
- **Las condiciones exactas de la GPU de Kaggle** (horas por semana, tipo de tarjeta): se leen en la
  primera ejecución, no las copio de memoria.
- **Cómo se ve.** Nada de lo anterior dice que el resultado sea bueno. Los presentadores sintéticos que
  circulan salen de servicios de pago; con piezas abiertas y gratuitas, lo razonable es esperar algo
  peor, y es posible que la conclusión de la prueba sea «no».

## Fuentes

- `kaggle-api`, documentación y PR #863 (tokens nuevos, `KAGGLE_API_TOKEN`):
  https://github.com/Kaggle/kaggle-api/pull/863/files · https://pypi.org/project/kagglehub
- LatentSync: https://github.com/bytedance/LatentSync (licencia en el repositorio; InsightFace en
  `latentsync/utils/face_detector.py`)
- MuseTalk: https://github.com/TMElyralab/MuseTalk · https://huggingface.co/TMElyralab/MuseTalk
  (licencia MIT de código y pesos; detector `sfd` por defecto en `musetalk/utils/face_detection/api.py`;
  `79999_iter.pth` en `musetalk/utils/face_parsing/__init__.py`)
- EchoMimic: https://github.com/antgroup/echomimic · https://huggingface.co/BadToBest/EchoMimic
  (ficha sin licencia) · https://huggingface.co/lambdalabs/sd-image-variations-diffusers
- Basel Face Model, licencia no comercial:
  https://faces.dmi.unibas.ch/bfm/content/basel_face_model/downloads/BFM_NonCommercial_License_Agreement.pdf
