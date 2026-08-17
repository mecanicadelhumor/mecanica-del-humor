# Mecánica del Humor / Humor Mechanics

Canal de YouTube automatizado sobre la ciencia del humor. Enseña a la gente a ser graciosa —y con
ello, a manejarse mejor socialmente— apoyándose en investigación real.

**Estado a 31 de julio de 2026:** los cinco objetivos del encargo están cumplidos. El sistema
produce vídeo real; falta conectarle internet.

---

## Qué hay aquí

```
Humor/
├── PROYECTO.md                     ← este archivo
├── SIGUIENTES_PASOS.md             ← lo que toca hacer, en orden
│
├── 01_bibliografia/
│   ├── BIBLIOGRAFIA_CURADA.md      77 obras en 12 pilares, con el porqué de cada una
│   ├── data/semillas.json          la misma lista, legible por máquina
│   └── scripts/                    fetch_biblio.py (descarga OA) · generar_md.py
│
├── 02_marca/
│   └── NOMBRE_Y_MARCA.md           nombre, handles verificados, identidad visual
│
├── 03_produccion/
│   ├── STACK_DE_PRODUCCION.md      qué herramientas y por qué
│   ├── pipeline/                   escena.html · render.py · voz.py · montaje.py
│   │                               miniatura.py · publicar.py
│   └── .github/workflows/          producir.yml (mover a la raíz del repo)
│
├── 04_agentes/
│   ├── ARQUITECTURA_AGENTES.md     los 12 agentes y sus contratos
│   ├── esquema_guion.json          el contrato que los une
│   ├── validar_guion.py            el portero automático
│   └── prompts/                    guionista · chistologo · verificador
│
└── 05_calendario/
    ├── CALENDARIO.md               8 vídeos, 4 semanas, 4 formatos a prueba
    └── guiones/                    MDH-001 … MDH-008, completos y validados
```

---

## Las cinco decisiones

### 1. Bibliografía

**77 obras curadas** en doce pilares temáticos, cada una con una frase explicando qué vídeo permite
hacer. No están elegidas por número de citas sino por si dan lugar a algo enseñable.

La descarga es legal por diseño: `fetch_biblio.py` resuelve cada obra en OpenAlex, busca la versión
en acceso abierto vía Unpaywall y Europe PMC, y descarga solo eso. Nunca toca repositorios pirata.
De lo cerrado se usan resumen, datos publicados y cita, que es lo que un guion necesita.

Lleva dentro tres trampas deliberadas —un paper que no pertenece al tema y dos duplicados con
títulos distintos— para comprobar que el filtro y la deduplicación funcionan antes de fiarse de
ellos.

### 2. Nombre

**Mecánica del Humor** (`@mecanicadelhumor`) y **Humor Mechanics** (`@humormechanics`). Los dos
handles estaban libres el 31 de julio; se comprobaron uno a uno, junto con otros catorce.

«Mecánica» promete algo que «ciencia» no promete: que puedes abrirlo, ver las piezas y volver a
montarlo. Y se dibuja solo —planos de despiece, engranajes, diagramas— lo cual resuelve la identidad
visual sin depender de generación de imagen.

### 3. Producción

**No se genera vídeo con IA. Se genera con código.** Los planes gratuitos de vídeo generativo dan
unos pocos segundos al día, no mantienen la coherencia entre planos y no permiten decidir qué hay en
pantalla en el segundo 42. Un canal didáctico necesita justo lo contrario.

En su lugar: escenas en HTML/CSS/SVG renderizadas fotograma a fotograma con un navegador sin
interfaz, montadas con FFmpeg sobre voz neuronal gratuita. Coste cero, sin GPU, y con una identidad
que será idéntica en el vídeo 200.

**Ya funciona.** Se ha renderizado el episodio 1 completo: 38 escenas, 7 minutos y 25 segundos de
vídeo 1080p, y el vídeo mudo está en esta entrega.

### 4. Calendario

**Ocho vídeos en cuatro semanas**, martes y viernes, en español e inglés: 16 subidas. Ocho es el
mínimo para que YouTube entienda de qué va el canal y el máximo que se puede producir a ciegas antes
de tener el primer dato de retención.

Prueban cuatro formatos por duplicado —tesis, mecanismo, autodiagnóstico y técnica— para que el
ganador no pueda ser casualidad. **Los ocho guiones están escritos, validados y en `05_calendario/`.**

### 5. Agentes

**Doce agentes**, cada uno con un archivo de entrada, uno de salida y un criterio de rechazo. Nada
de agentes que colaboran en abstracto: cada uno lee un JSON, escribe otro y puede parar la cadena.

El reparto de inteligencia sigue una regla: Claude solo donde equivocarse sale caro —guion, humor,
verificación, calendario—; Gemini gratuito para el volumen; Python determinista para render, voz,
montaje y subida.

El **verificador tiene poder de veto**: si una sola afirmación es falsa, o hay una cifra en pantalla
sin fuente, el vídeo no se produce.

---

## La restricción que lo condiciona todo

Mi contenedor en la nube **no tiene salida a internet** salvo a los repositorios de paquetes. Tu VM
local tampoco. Eso significa que no puedo llamar a la API de Gemini, ni sintetizar voz, ni subir
nada a YouTube desde aquí.

La solución no cambia lo que elegiste, solo reparte el trabajo:

| | Quién | Qué |
|---|---|---|
| **Cerebro** | Cowork (tareas programadas) | Investigar, guionizar, poner gracia, verificar, decidir |
| **Manos** | GitHub Actions | Voz, imágenes, render, montaje, subida |

GitHub Actions cumple tus dos condiciones: gratuito y completamente externo a tu ordenador. Tu Docker
con n8n queda como plan B, no como dependencia.

---

## Lo que ya está probado

- ✅ El motor de escenas renderiza los nueve tipos con la identidad de marca aplicada.
- ✅ Un guion de 38 escenas produce un mp4 de 7:25 a 1080p, con las duraciones exactas previstas.
- ✅ Optimización de render: 2.043 fotogramas capturados en vez de 13.350. Solo se captura lo que se
  mueve; FFmpeg estira el resto.
- ✅ El generador de miniaturas produce PNG 1280×720 con la fórmula de marca.
- ✅ El validador detecta escenas demasiado largas, cifras sin fuente, monotonía visual y texto en
  pantalla repetido de la narración. Los ocho guiones pasan sin errores.
- ✅ Handles de YouTube verificados uno a uno.

## Lo que falta por probar

- ⏳ La síntesis de voz (`voz.py`). El código está escrito; necesita una máquina con internet.
- ⏳ El montaje con voz y música (`montaje.py`). Igual.
- ⏳ La subida a YouTube (`publicar.py`). Necesita credenciales OAuth tuyas.
- ⏳ La adaptación al inglés. Se hace desde el guion español, no traduciendo: readaptando.

Todo eso se resuelve en la primera ejecución de GitHub Actions, y por eso es el primer punto de
`SIGUIENTES_PASOS.md`.
