# Stack de producción

## La conclusión primero

**No vamos a generar vídeo con IA. Vamos a generarlo con código.**

Es la decisión más importante del proyecto y conviene entender por qué, porque va contra el instinto.

### Por qué se descarta la generación de vídeo por IA

| | Realidad en 2026 |
|---|---|
| Veo, Sora, Kling, Runway, Luma | Los planes gratuitos dan del orden de **unos pocos clips de 5–10 segundos al día**. Un vídeo de 6 minutos necesita ~40–70 planos. |
| Coherencia | Cada clip se genera independiente: el estilo, los colores y los personajes bailan entre planos. Un canal necesita lo contrario. |
| Tu hardware | Una AMD 780M integrada no ejecuta modelos de difusión de vídeo. Descartado por definición. |
| Control | Un vídeo didáctico necesita que en el segundo 42 aparezca *exactamente* el eje Y con el valor 0,37. Los modelos generativos no hacen eso. |

Aunque fuese gratis e ilimitado, **seguiría siendo la herramienta equivocada** para este canal. Los
canales de divulgación que funcionan (Kurzgesagt, Veritasium, CGP Grey, 3Blue1Brown) no usan vídeo
generativo: usan **motion graphics**, es decir, gráficos animados y controlados al fotograma.

### Lo que sí vamos a hacer

Un **documental de pizarra animada generado por código**: escenas construidas en HTML/CSS/SVG,
renderizadas fotograma a fotograma con un navegador sin interfaz, montadas con FFmpeg sobre una
narración de voz neuronal. Gratis, ilimitado, reproducible al 100 % y con una identidad visual que se
mantiene idéntica en el vídeo 1 y en el vídeo 200.

Encaja además con la marca: **Mecánica del Humor** debe *parecer* un plano técnico. Lo es literalmente.

---

## Arquitectura de ejecución

Hay una restricción física que condiciona todo y conviene tenerla clara:

| Entorno | Internet | FFmpeg | Para qué sirve |
|---|---|---|---|
| **Cowork (yo, en la nube de Anthropic)** | ❌ solo repositorios de paquetes | ✅ | Pensar: investigar, guionizar, revisar, verificar, decidir |
| **Tu VM local** | ❌ | ✅ | Revisar y previsualizar. Nada más |
| **GitHub Actions** | ✅ completo | ✅ | Ejecutar: llamar a APIs, sintetizar voz, renderizar, publicar |

Es decir: **yo soy el cerebro y GitHub Actions son las manos.** No es un cambio respecto a lo que
elegiste —las tareas programadas de Cowork siguen orquestando todo—, es simplemente dónde vive el
músculo, porque desde mi contenedor no puedo llamar a la API de Gemini ni subir a YouTube.

GitHub Actions cumple además tus dos condiciones: es **gratuito** (ilimitado en repositorios públicos,
2.000 minutos/mes en privados) y es **completamente externo a tu ordenador**. Tu Docker con n8n queda
como plan B opcional, no como dependencia.

```
┌────────────────────────────────────────────────────────────┐
│  COWORK  (tarea programada — el cerebro)                   │
│  investigar · guionizar · verificar · decidir · commit     │
└───────────────────────────┬────────────────────────────────┘
                            │ git push (guion.json)
                            ▼
┌────────────────────────────────────────────────────────────┐
│  GITHUB  (repo = única fuente de verdad)                   │
│  guiones/ · marca/ · plantillas/ · .github/workflows/      │
└───────────────────────────┬────────────────────────────────┘
                            │ workflow_dispatch / cron
                            ▼
┌────────────────────────────────────────────────────────────┐
│  GITHUB ACTIONS  (las manos)                               │
│  1 voz (edge-tts)   2 subtítulos   3 escenas (Playwright)  │
│  4 montaje (FFmpeg) 5 miniatura    6 subida (YouTube API)  │
└────────────────────────────────────────────────────────────┘
```

---

## El stack, pieza a pieza

### 1. Voz — `edge-tts`

**Elegida.** Paquete de Python que usa las voces neuronales de Microsoft Edge. Gratis, sin clave API,
sin límite práctico, y con voces excelentes en español de España y en inglés.

Voces propuestas:

| Canal | Voz | Por qué |
|---|---|---|
| ES | `es-ES-AlvaroNeural` | Grave, tranquila, con autoridad sin sonar a locutor de documental de sobremesa |
| ES alt. | `es-ES-ElviraNeural` | Alternativa femenina, muy natural |
| EN | `en-US-AndrewMultilingualNeural` | Conversacional, moderna, aguanta 8 minutos sin cansar |
| EN alt. | `en-GB-RyanNeural` | Si se quiere un aire más «documental británico» |

**La ventaja decisiva:** `edge-tts` devuelve *word boundaries*, es decir, la marca de tiempo exacta de
cada palabra. Con eso los subtítulos salen perfectos **sin necesidad de Whisper ni de transcribir
nada**, y además nos da la duración real de cada frase, que es lo que sincroniza la animación con la
voz. Esto es lo que hace que todo el pipeline funcione sin GPU.

*Respaldos:* Gemini TTS (`gemini-2.5-flash-preview-tts`, gratis con tu clave de AI Studio, más
expresiva, con cuota diaria) y Piper TTS (100 % local y offline, por si Microsoft cierra el grifo).

### 2. Subtítulos — derivados de la propia voz

Sin coste, sin modelo, sin errores de transcripción: los tiempos vienen del sintetizador. Se generan
`.srt` (para subir a YouTube en los dos idiomas) y `.ass` (para quemar subtítulos animados palabra a
palabra en el vídeo, que es lo que sostiene la retención).

### 3. Visuales — Playwright + Chromium

Cada escena es un archivo HTML con el sistema de diseño de la marca. Un navegador sin interfaz lo
abre, avanza la animación fotograma a fotograma y guarda PNG. Resultado: animación real (tipografía
que entra, líneas que se dibujan, diagramas que se despiezan) con calidad de motion graphics, hecha
con CSS.

Complementos:

- **Gráficas de datos**: matplotlib con la paleta de marca. Cada estudio citado tiene su figura.
- **Imagen generativa puntual**: Gemini «Nano Banana» / Imagen en su capa gratuita, solo para
  metáforas visuales y miniaturas. Uno o dos por vídeo, no cuarenta.
- **B-roll de archivo**: APIs gratuitas de Pexels y Pixabay, más Wikimedia Commons para material
  histórico y de dominio público.

> Se ha evaluado **Remotion** (motion graphics en React, gratis para equipos de menos de 4 personas).
> Es superior en potencia, pero añade una base de código React y un tiempo de render mucho mayor. Se
> deja anotado como salto de calidad para la v2, cuando el pipeline básico ya esté publicando solo.

### 4. Montaje — FFmpeg

Concatenación de escenas, efecto Ken Burns, fundidos, quemado de subtítulos, mezcla de música con
*ducking* automático bajo la voz, normalización de sonoridad a −14 LUFS (el estándar de YouTube) y
exportación a 1080p H.264. Todo con un solo binario que ya está en todas partes.

### 5. Música y sonido

Biblioteca de audio de YouTube (libre y sin atribución), Free Music Archive y Kevin MacLeod (CC-BY,
con atribución en la descripción). Se fija una cama sonora por sección: intro, desarrollo, remate.

### 6. Publicación — YouTube Data API v3

Gratuita. La cuota diaria por defecto es de 10.000 unidades y una subida cuesta 1.600, es decir, hasta
**6 vídeos al día**: de sobra. Se sube en privado o como programado, y el paso de publicar queda con
verificación humana durante las primeras semanas, tal y como pediste.

### 7. Lo que NO usamos y por qué

| Descartado | Motivo |
|---|---|
| Vídeo generativo (Veo/Sora/Kling/Runway) | Cuota gratuita insuficiente y cero coherencia visual |
| Avatares tipo HeyGen / D-ID | Marca de agua en gratuito, límite de minutos, y el «avatar parlante» resta credibilidad científica |
| Whisper para subtítulos | Innecesario: los tiempos ya los da el TTS |
| Stable Diffusion local | Imposible en una 780M |
| n8n en tu Docker | Excelente herramienta, pero ata el proyecto a que tu equipo esté encendido. Queda como plan B |

---

## Coste total

**0 €.** Las únicas cuentas necesarias son gratuitas: Google AI Studio (ya la tienes), GitHub, y dos
canales de YouTube. El único recurso escaso real es tu suscripción de Claude, y por eso el reparto de
trabajo del documento de agentes envía a Gemini todo lo que no requiere criterio fino.

## Riesgos y planes B

| Riesgo | Probabilidad | Plan B |
|---|---|---|
| Microsoft rompe `edge-tts` | Media | Gemini TTS (ya integrado) → Piper local |
| Se agota la cuota gratuita de Gemini | Media | El guion es lo único crítico y lo hago yo; el resto degrada a plantillas |
| YouTube penaliza contenido «producido en masa» | Media-alta | Menos vídeos y mejores; guion original con tesis propia; declarar el uso de IA; no reciclar plantillas idénticas |
| Se agotan los minutos de GitHub Actions | Baja | Repositorio público = minutos ilimitados |
| Un dato citado resulta ser falso | **Alta si no se controla** | Agente verificador obligatorio antes de publicar (ver `04_agentes/`) |
