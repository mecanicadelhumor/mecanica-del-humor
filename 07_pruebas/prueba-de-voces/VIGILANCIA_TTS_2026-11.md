# Vigilancia de modelos de voz (TTS) — noviembre de 2026

Fecha de la revisión: 2 de noviembre de 2026.
Criterio: coste cero absoluto, uso comercial (canal de YouTube), español de España, entonación natural y expresiva con humor; ejecución en GitHub Actions (CPU) o, como mucho, en una T4 de Kaggle.

> Nota de método: todo lo que aparece como «verificado» se ha comprobado en la ficha oficial (Google AI for Developers, Hugging Face o GitHub del autor) el 2 de noviembre de 2026. Lo que viene de blogs, foros o agregadores se marca como **no verificado**. No he escuchado ninguna muestra: ninguna valoración de calidad en español peninsular de esta nota es una escucha propia.

---

## 0. Aviso urgente: los dos modelos que usamos se apagan el 17 de noviembre

La página oficial de retiradas de la API de Gemini indica para **los dos modelos que usamos**:

| Modelo actual | Uso en el canal | Fecha de apagado | Sustituto oficial |
|---|---|---|---|
| `gemini-3.1-flash-tts-preview` | Shorts | **17 de noviembre de 2026** | `gemini-3.8-flash-tts` o `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-flash-preview-tts` | Vídeo largo | **17 de noviembre de 2026** | `gemini-3.8-flash-tts` o `gemini-3.8-flash-lite-tts` |

Fuente: <https://ai.google.dev/gemini-api/docs/deprecations>. Google aclara que las fechas indicadas son «las más tempranas posibles» y que avisará antes de la retirada exacta, pero no conviene contar con una prórroga. Además, el registro de cambios del 18 de septiembre de 2026 dice que se está «limitando el acceso a los modelos 2.5 a usuarios que los hayan usado activamente», sin nombrar el TTS (<https://ai.google.dev/gemini-api/docs/changelog>).

**Consecuencia:** no se trata de mejorar por gusto: hay que migrar. Faltan 15 días.

---

## 1. Novedades de Gemini TTS en 2026

### Cronología (registro de cambios oficial)

- **15 de abril de 2026**: sale `gemini-3.1-flash-tts-preview` («cost-efficient, expressive, and steerable»). *Ojo:* la página de retiradas da como fecha de lanzamiento el 26 de febrero de 2026. Las dos páginas oficiales no coinciden. No afecta a nada práctico.
- **17 de junio de 2026**: streaming para `gemini-3.1-flash-tts-preview`.
- **26 de agosto de 2026**: salen `gemini-3.5-transcribe` y `gemini-3.5-transcribe-live` (voz a texto). Puede servir para alinear los subtítulos, pero no he comprobado que devuelva marcas de tiempo por palabra.
- **22 de septiembre de 2026**: **pasan a GA `gemini-3.8-flash-tts` y `gemini-3.8-flash-lite-tts`**, junto con el endpoint de voces (*Voices*). Flash-Lite se presenta como sustituto de la 3.1 preview «para producción de alto volumen».

### Los dos modelos nuevos

| | `gemini-3.8-flash-tts` | `gemini-3.8-flash-lite-tts` |
|---|---|---|
| Posicionamiento oficial | «Maximum voice fidelity, acting nuance, and dialect coverage»: gama creativa insignia, pensada para audiolibros, diálogo y actuación con vocalizaciones | «High throughput, low latency, and cost efficiency»: voz de un solo hablante en producción |
| Idiomas | más de 130 (incluye «Spanish», sin desglose por variante) | más de 100 (la tabla tiene 101) |
| Límite de tokens | 8.192 de entrada y 16.384 de salida | 8.192 de entrada y 16.384 de salida |
| Nivel gratuito | **Sí, gratis** (tabla de precios) | **Sí, gratis** |
| Precio de pago (por si acaso) | 0,50 $ por millón de tokens de entrada y 9 $ por millón de salida hasta el 31/12/2026; luego 1 $ y 18 $ | 0,50 $ y 6 $ hasta el 31/12/2026; luego 1 $ y 12 $ |
| Datos del nivel gratuito usados por Google | Sí | Sí |

Fuentes: <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts>, <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts>, <https://ai.google.dev/gemini-api/docs/pricing>, <https://ai.google.dev/gemini-api/docs/speech-generation>.

**Control de entonación** (según la guía oficial de generación de voz):
- `speech_metadata.style`, con indicaciones de estilo por turno («whispered urgently»…).
- Etiquetas en línea entre corchetes angulares: `<laugh>`, `<sigh>`, `<short pause>`, `<long pause>`. **Google recomienda escribirlas en inglés aunque el texto vaya en español.**
- «Backchannels» entre barras (`|oh really?|`), que funcionan mejor en Flash (no en Lite).
- Énfasis escribiendo la palabra en MAYÚSCULAS.
- El acento **no** se fija con `style` («avoid permanent accent changes»). Hay que elegir una voz regional de la *Extended Voice Library* (`GET /v1beta/voices`, filtrable por `language_code`, `region_code` y `accent`). **No he podido verificar si hay voces etiquetadas como español de España.** Es lo primero que hay que mirar.
- *Voice design* (crear una voz propia a partir de una descripción) y *voice replication* están disponibles en los dos modelos 3.8. **No consta si funcionan en el nivel gratuito.** Las voces guardadas caducan un año después de su último uso.
- Cambio técnico: las peticiones unarias de 3.8 devuelven **WAV** por defecto (24 kHz, mono, 16 bits), no PCM sin cabecera como los modelos anteriores. Hay que revisar el código que escribe el fichero. Requiere `google-genai >= 2.25.0` para listar voces.

**Marcas de tiempo por palabra:** la documentación no las menciona («TTS models accept text-only inputs and produce audio-only outputs»). Seguiremos alineando con Whisper.

**Cuota gratuita: sin confirmar.** La página oficial de límites solo dice que se consultan en AI Studio (<https://aistudio.google.com/rate-limit>) y que los modelos *preview* tienen límites más estrictos. Datos de terceros (**no verificados**):
- un agregador da para los dos 3.8 TTS gratuitos 3 peticiones por minuto y 10.000 tokens de entrada por minuto, sin cifra diaria;
- un hilo del foro oficial (7 de octubre de 2026) cuenta que la API cortaba `gemini-3.8-flash-tts` a 100 peticiones al día aunque AI Studio mostraba 10.000; no aclara si era nivel gratuito, y un empleado de Google respondió que estaba «resuelto» (<https://discuss.ai.google.dev/t/gemini-3-8-flash-tts-api-enforces-100-rpd-despite-ai-studio-showing-10k-rpd/187223>);
- otro hilo (8 de agosto de 2026) confirma el tope de **10 peticiones al día** que ya conocemos para la 3.1 (<https://discuss.ai.google.dev/t/gemini-lies-about-free-tier-quota-limits-sudden-resource-exhausted-blockers-on-tts-models/177531>).

→ **Hay que mirar la cuota real del proyecto en AI Studio** antes de rediseñar nada. Si es 10 al día por modelo como ahora, el reparto Flash para los Shorts y Lite para el largo (o al revés) sigue siendo viable.

**Calidad en español peninsular:** no hay evidencia específica. Una reseña en inglés (eesel.ai) lo sitúa n.º 1 en robustez de pronunciación en Artificial Analysis y n.º 2 en una «Voice Arena» a ciegas; otra (Unifically) lo pone 3.º por Elo. Son datos **no verificados**, contradictorios y no específicos del español.

---

## 2. Modelos abiertos: tabla comparativa

Leyenda: ✅ verificado en la ficha oficial · ⚠️ dato parcial o de terceros · ❓ no verificado.

| Modelo | Licencia de los pesos | ¿Uso comercial? | Español | CPU o GPU | Control de entonación o emoción | Marcas por palabra |
|---|---|---|---|---|---|---|
| **Chatterbox Multilingual V3** + ajuste **es-es** (Resemble AI) | MIT ✅ [ficha](https://huggingface.co/ResembleAI/chatterbox) · [es-es](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-es-es) | Sí | 23+ idiomas; **ajuste específico de español de España** (`ResembleAI/Chatterbox-Multilingual-es-es`) y otro de LatAm ✅. Sin evaluaciones publicadas ni horas de datos ❓ | Ejemplos solo con `cuda`; en CPU, fuentes contradictorias ⚠️ → **T4** | Control de «exageración» o intensidad y `cfg` ✅. Etiquetas `[laugh]`… solo en Turbo, que es solo inglés ✅ | No → Whisper |
| **Qwen3-TTS** (Alibaba, enero de 2026) | Apache-2.0 ✅ [ficha](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) | Sí | 10 idiomas, incluido el español ✅; variante peninsular sin especificar ❓. Un estudio en LinkedIn con español argentino lo pone 1.º en calidad (WER 1,2 %) ⚠️ | 1.7B: GPU. Pide FlashAttention 2, que **no funciona en T4** (Turing) y obliga a usar otra atención ❓. 0.6B: hay puertos a CPU, cerca del tiempo real en Apple M1 cuantizado; en un i5 x86, más lento que el tiempo real ⚠️ | **Instrucciones en lenguaje natural** (timbre, emoción, prosodia) ✅ | No consta |
| **Pocket TTS** (Kyutai) | Código MIT; pesos CC-BY-4.0 ✅ [ficha](https://huggingface.co/kyutai/pocket-tts) · [GitHub](https://github.com/kyutai-labs/pocket-tts) | Sí, con atribución. **La licencia de la voz española «lola» no aparece** en la página de voces ❓ (algunas voces de Kyutai son CC-BY-NC) | Español añadido (voz «lola»); acento sin especificar ❓. Variante de 24 capas de más calidad ✅ | **CPU**: unos 6× tiempo real en un MacBook Air M4 con 2 núcleos ✅ (no medido en Actions) | Clonación desde WAV; sin control de emoción documentado | Oficial no; existe un fork con marcas por palabra (`pocket-tts-timestamped`) ⚠️ |
| **Kokoro-82M** | Apache-2.0 ✅ [ficha](https://huggingface.co/hexgrad/Kokoro-82M) | Sí | Solo 3 voces (ef_dora, em_alex, em_santa), **sin nota de calidad**; fonemas con espeak-ng `es` ✅ | CPU, rápido (no hay cifra oficial) | Ninguno | No para el español ❓ |
| **Fun-CosyVoice3-0.5B** (diciembre de 2025) | Apache-2.0 ✅ [ficha](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512) | Sí | 9 idiomas, incluido el español ✅; dialectos solo del chino | GPU recomendable ❓ | Instrucciones de emoción, velocidad y volumen ✅ | No consta |
| **Voxtral-4B-TTS** (Mistral, marzo de 2026) | **CC-BY-NC-4.0** ✅ [ficha](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) | **No** | 9 idiomas, incluido el español | GPU de 16 GB o más (no cabe en una T4 de 16 GB con margen) | No documentado | No |
| **Fish Audio S2-Pro** (marzo de 2026) | Fish Audio Research License ✅ [blog oficial](https://fish.audio/es/blog/what-we-mean-by-open-source-for-s2/) | **No** (licencia comercial aparte) | Español en el «Tier 2» | GPU | Emoción en lenguaje natural | No |
| **F5-TTS / F5-Spanish** | **CC-BY-NC-4.0** ✅ [F5-Spanish](https://huggingface.co/jpgallegoar/F5-Spanish) (algunos sitios dicen CC0; manda la ficha del autor) | **No** | Ajuste en español | GPU (en CPU, lento) | Solo por la referencia | No |
| **XTTS-v2** (Coqui) | Coqui Public Model License ✅ [ficha](https://huggingface.co/coqui/XTTS-v2) | **No** (la CPML es no comercial y Coqui cerró en 2024, así que no hay a quién comprar licencia ⚠️) | 17 idiomas, incluido el español | GPU (en CPU, lento) | Solo por la referencia | No |
| **Orpheus multilingüe es/it** (Canopy) | Etiqueta Apache-2.0, pero es un ajuste de Llama 3.2 3B (podría arrastrar la licencia de Llama ❓) [ficha](https://huggingface.co/canopylabs/3b-es_it-ft-research_release) | ❓ Repo con acceso restringido, «research release», beta | Español e italiano; sin métricas | GPU (3B) | Etiquetas simples (sintaxis sin documentar en la ficha) | No |
| **Higgs Audio v2** (Boson AI) | Licencia «other» en HF; el LICENSE del repo de código es Apache-2.0 ⚠️ [ficha](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base) | ❓ No he podido confirmar los términos de los pesos | «4 languages» sin detallar ❓ | GPU (unos 6B en BF16) | Expresivo | No |
| **IndexTTS-2** (bilibili) | bilibili Model Use License ✅ [LICENSE](https://github.com/index-tts/index-tts/blob/main/LICENSE) | Sí, salvo empresas grandes (más de 100 M de usuarios activos al mes) | **Solo chino e inglés** | GPU | Emoción y duración | No |
| **Zonos v0.1** (Zyphra) | Apache-2.0 ✅ [ficha](https://huggingface.co/Zyphra/Zonos-v0.1-transformer) | Sí | **Sin español** (en, ja, zh, fr, de) | GPU NVIDIA serie 3000 o posterior (en T4, dudoso) | Emociones finas | No |
| **Supertonic 3** (Supertone, abril de 2026) | OpenRAIL-M ⚠️ | Sí, con restricciones de uso (obliga a declarar el contenido sintético) | 31 idiomas, incluido el español ⚠️ | CPU (ONNX) ⚠️ | ❓ | ❓. Según espejos de terceros, la empresa se disolvió y el repo se archiva ⚠️ |
| **Kani-TTS-2** | Probablemente Apache-2.0, con cláusula de restricciones ⚠️ | ❓ | `kani-tts-2-pt` lista el español ⚠️ | GPU de unos 3 GB ⚠️ | ❓ | ❓ |
| **Kyutai TTS 1.6B** | CC-BY-4.0 ✅ | Sí | **Solo inglés y francés** | GPU | — | — |
| **VibeVoice** (Microsoft) | MIT, pero «research only» y el modelo Large aparece como «Disabled» ✅ | No recomendado por Microsoft | **Solo inglés y chino** | GPU | — | — |
| **Dia-1.6B** (Nari) | Apache-2.0 ✅ | Sí | **Solo inglés** | GPU | Vocalizaciones | — |
| **Sesame CSM-1B** | Apache-2.0 ✅ | Sí | Inglés («some capacity» en otros idiomas, «likely won't perform well») | GPU | — | — |
| **Spark-TTS-0.5B** | **CC-BY-NC-SA-4.0** ✅ | **No** | Solo chino e inglés | — | — | — |
| **MaskGCT** (Amphion) | **CC-BY-NC-4.0** ✅ | **No** | Entrenado con inglés y chino | — | — | — |

### Lectura rápida

- **Descartados por licencia** (no comerciales): Voxtral TTS, Fish Audio S2, F5-TTS y F5-Spanish, XTTS-v2, Spark-TTS y MaskGCT.
- **Descartados por idioma**: IndexTTS-2, Zonos, Kyutai TTS 1.6B, VibeVoice, Dia y Sesame CSM.
- **Dudosos por licencia o estado**: Orpheus es/it, Higgs Audio v2, Kani-TTS-2 y Supertonic 3.
- **Viables en licencia y con español**: Chatterbox Multilingual (es-es), Qwen3-TTS, CosyVoice 3, Pocket TTS y Kokoro.
  - Solo **Chatterbox es-es** está ajustado expresamente para el español de España.
  - Solo **Pocket TTS** y **Kokoro** van con holgura en la CPU de GitHub Actions. Kokoro tiene pocas voces y sin calificar. Pocket TTS tiene una sola voz española, de licencia sin confirmar, y ningún control de emoción: como mucho sirve para reemplazar a Piper o edge-tts como respaldo, no a Gemini.
- **Ninguno** de los modelos abiertos revisados da marcas de tiempo por palabra de forma oficial (el fork de Pocket TTS es la excepción, no verificada). Hay que seguir alineando con Whisper. Edge-tts sí emite eventos `WordBoundary`.

---

## 3. ¿Hay algo que merezca una prueba ahora?

Sí. Dos candidatos:

1. **`gemini-3.8-flash-tts`** (con `gemini-3.8-flash-lite-tts` como variante barata dentro de la misma prueba). No es opcional: los dos modelos actuales se apagan el 17 de noviembre. Es gratuito, está en GA, tiene más control (etiquetas en línea, estilo por turno, voces regionales, diseño de voz) y no cambia la infraestructura.
2. **Chatterbox Multilingual, ajuste `es-es`**: licencia MIT, uso comercial libre, ajustado al español de España y con control de exageración, que viene bien para el humor. Corre en una T4 de Kaggle; en la CPU de Actions, probablemente no a un ritmo razonable (sin verificar). Sería la salida si la cuota gratuita de Gemini 3.8 resulta inservible. Lleva la marca de agua inaudible PerTh, lo que no impide el uso comercial.

(Qwen3-TTS queda como reserva: buena licencia y control por instrucciones, pero no hay evidencia de que suene peninsular, y el 1.7B choca con FlashAttention 2 en la T4).

### Plan de prueba ciega

**Frases** (del guion ya probado en esta carpeta, enteras y con tono distinto):
1. «Mi vecino toca el piano a las tres de la mañana.» (planteamiento)
2. «Vale. Ahora te lo explico y mira lo que le pasa.» (complicidad)
3. «Y falla aquí: es un modelo, no una cifra medida.» (remate seco)

**Contendientes** (5 audios por frase, 15 en total):
- A. Voz actual: `gemini-3.1-flash-tts-preview`, con la misma voz y la misma dirección de estilo que en producción. **Hay que generarla antes del 17 de noviembre.**
- B. `gemini-3.8-flash-tts`, misma voz prediseñada si existe; si no, la española con etiqueta de región de España en `GET /v1beta/voices`.
- C. `gemini-3.8-flash-lite-tts`, misma voz que B.
- D. Chatterbox `es-es` sin referencia (voz por defecto), con exageración 0,5.
- E. Chatterbox `es-es` con exageración 0,7–0,8 y `cfg` 0,3. Sin clonar ninguna voz real de terceros.

**Coste:** las tres frases van en una sola llamada por modelo de Gemini, así que A, B y C ocupan 3 peticiones, 1 por modelo, dentro de cualquier cuota. Si hay que cortar por frase, se aprovechan los silencios largos (`<long pause>`). D y E se generan en un cuaderno de Kaggle con T4 en pocos minutos, sin coste.

**Procedimiento:**
1. Antes de empezar, anotar en AI Studio la cuota real (peticiones al día) de los dos modelos 3.8 y consultar `GET /v1beta/voices` para ver si hay voces con región de España.
2. Normalizar todos los audios a la misma sonoridad (`ffmpeg -af loudnorm=I=-16`), a 24 kHz mono y recortando los silencios de los extremos.
3. Renombrarlos al azar (`x01.wav`…`x15.wav`) y guardar la clave en un fichero aparte que no vean los oyentes.
4. Que escuchen al menos el codirector y otra persona, sin saber qué es cada audio. Para cada uno, del 1 al 5: naturalidad, expresividad o gracia, acento peninsular (que no suene latino ni a doblaje) y errores (cortes, palabras comidas, ritmo raro). Al final de cada frase, cuál prefieren.
5. Pasar Whisper por los 15 audios: debe reconocer bien cada palabra y el alineado de los subtítulos debe salir limpio.
6. Decidir: si B o C empatan con A o la superan, se migra ya, con Flash para los Shorts y Lite para el largo (o según la cuota). Si D o E ganan con claridad, preparar el flujo en Kaggle como vía principal o de respaldo de calidad.

---

## 4. Lo que no he podido verificar

- La cuota gratuita real (peticiones al día) de los modelos 3.8 TTS.
- Si hay voces de Gemini etiquetadas como español de España y si el diseño de voz entra en el nivel gratuito.
- La calidad real de ningún modelo en español peninsular: no hay evaluaciones públicas fiables y no he escuchado muestras.
- La velocidad de Chatterbox y Qwen3-TTS en CPU de GitHub Actions o en una T4.
- La licencia de la voz española «lola» de Pocket TTS y los términos de los pesos de Higgs Audio v2 y Orpheus es/it.
- La disolución de Supertone (solo la mencionan espejos de terceros).
