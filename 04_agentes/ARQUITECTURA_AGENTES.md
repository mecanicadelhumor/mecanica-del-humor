# Arquitectura de agentes

## Principio de diseño

Un agente = **un archivo de entrada, un archivo de salida y un criterio de rechazo**. Nada de agentes
que «colaboran» en abstracto: cada uno lee un JSON, escribe otro JSON y puede decir «esto no pasa».
Así se puede pulir uno sin tocar los demás, que es exactamente lo que pediste.

El repositorio es la memoria compartida. No hay estado oculto en ningún sitio.

```
corpus.json  ──►  fichas/*.json  ──►  calendario.json  ──►  guiones/*.json
                                                                  │
                        ┌─────────────────────────────────────────┤
                        ▼                                         ▼
                 verificacion/*.json                        build/<id>/
                 (bloquea o aprueba)                    mudo · voz · final
                                                                  │
                                                                  ▼
                                                          publicaciones/*.json
                                                                  │
                                                                  ▼
                                                            metricas/*.json
                                                          (realimenta calendario)
```

## Reparto de inteligencia

La regla es sencilla: **Claude solo donde el criterio importa y equivocarse sale caro.** Todo lo demás
va a Gemini gratuito o es determinista.

| Agente | Motor | Por qué ahí |
|---|---|---|
| Bibliotecario | Gemini Flash | Resumir papers es volumen, no criterio. Consume mucho y arriesga poco |
| Editor jefe | **Claude** | Decide qué se publica. Un mal calendario cuesta semanas |
| Guionista | **Claude** | Es el producto. Aquí no se ahorra |
| Chistólogo | **Claude** | Un canal de humor sin gracia está muerto. Requiere el mejor modelo |
| Verificador | **Claude** | Un dato falso destruye la credibilidad del canal entero |
| Adaptador EN | **Claude** (revisión) + Gemini (primer pase) | El humor no se traduce, se readapta |
| Empaquetador | Gemini Flash | Generar 20 variantes de título es fuerza bruta |
| Realizador / Locutor / Montador | Python determinista | Sin modelo. Mismo guion, mismo vídeo, siempre |
| Publicador | Python determinista | API de YouTube |
| Analista | Gemini Flash | Leer números y resumir tendencias |
| Mantenimiento del código | OpenCode | Refactors y arreglos del pipeline, no del contenido |

---

## Los agentes, uno a uno

### 1. Bibliotecario · `agente_bibliotecario`
**Entrada** `01_bibliografia/data/semillas.json` → **Salida** `corpus.json` + `fichas/<id>.json`
**Motor** Python (metadatos) + Gemini Flash (fichas) · **Cadencia** semanal

Enriquece el corpus vía OpenAlex/Unpaywall/EuropePMC, descarga lo que sea acceso abierto y convierte
cada paper en una **ficha de hallazgo**: qué se preguntó, qué se hizo, qué salió, con qué número, y
con qué límites. La ficha —no el paper— es lo que lee el guionista.

**Rechaza si:** no encuentra el efecto principal con su tamaño, o la muestra es menor de 30 sin que
sea un estudio cualitativo declarado. Marca la ficha como `frágil` y el guionista no puede usarla como
dato central, solo como apoyo.

### 2. Editor jefe · `agente_editor`
**Entrada** `fichas/` + `metricas/` → **Salida** `05_calendario/calendario.json`
**Motor** Claude · **Cadencia** semanal (lunes)

Decide qué se publica, en qué orden y por qué. Equilibra los pilares para que el canal no se convierta
en «doce vídeos sobre neurociencia», protege la promesa (*enseñar a ser gracioso*) y reordena según lo
que digan las métricas.

**Rechaza si:** el tema no tiene al menos una ficha de prioridad 1 detrás, o si repite el ángulo de un
vídeo publicado en las últimas 6 semanas.

### 3. Guionista · `agente_guionista`
**Entrada** ficha(s) + entrada del calendario → **Salida** `guiones/<id>.es.json`
**Motor** Claude · **Cadencia** por vídeo

Escribe el guion escena a escena en el esquema que consume el pipeline. Cada afirmación numérica lleva
su `fuente` con el `id` de la bibliografía. Ver `prompts/guionista.md`.

**Rechaza si:** no puede sostener la tesis con las fichas disponibles. Devuelve «me falta evidencia
para X» en vez de inventarla.

### 4. Chistólogo · `agente_chistologo`
**Entrada** `guiones/<id>.es.json` → **Salida** el mismo guion, con gracia
**Motor** Claude · **Cadencia** por vídeo, después del guionista

El agente más importante y el que casi todos los canales de este tipo se saltan. Un canal que enseña
humor **tiene que tener humor**, y no como adorno: cada técnica explicada debe demostrarse en el propio
vídeo en el momento de explicarla. Aplica violación benigna y la teoría general del humor verbal como
herramientas de escritura, no como decoración.

**Rechaza si:** pasan más de 45 segundos sin un momento de gracia, o si algún chiste funciona a costa
de un grupo de personas en lugar de a costa de una idea.

### 5. Verificador · `agente_verificador`
**Entrada** guion + fichas → **Salida** `verificacion/<id>.json` con veredicto
**Motor** Claude · **Cadencia** por vídeo · **Poder de veto**

Recorre el guion afirmación por afirmación y clasifica cada una: `verificada` (coincide con la ficha),
`imprecisa` (la ficha dice algo parecido pero no eso), `sin fuente`, `falsa`. Propone la redacción
corregida.

**Bloquea la publicación si:** hay una sola afirmación `falsa`, o más de dos `imprecisas`, o cualquier
cifra en pantalla sin `id` de fuente. Este agente es el que hace que el canal se pueda defender.

### 6. Adaptador · `agente_adaptador`
**Entrada** `guiones/<id>.es.json` → **Salida** `guiones/<id>.en.json`
**Motor** Gemini Flash (borrador) + Claude (pase final) · **Cadencia** por vídeo

No traduce: **readapta**. Los ejemplos culturales cambian, los juegos de palabras se sustituyen por
otros equivalentes, y el ritmo se ajusta al inglés, que es más corto. Un chiste traducido literalmente
no es un chiste, es una frase rara.

### 7. Realizador · `render.py` · determinista
Guion → vídeo mudo. Playwright + FFmpeg. Sin modelo, sin aleatoriedad.

### 8. Locutor · `voz.py` · determinista
Guion → narración + subtítulos + duraciones reales. edge-tts.

### 9. Montador · `montaje.py` · determinista
Vídeo mudo + voz + música → `final.mp4` normalizado a −14 LUFS.

### 10. Empaquetador · `agente_empaquetador`
**Entrada** guion + vídeo → **Salida** `publicaciones/<id>.json`
**Motor** Gemini Flash · **Cadencia** por vídeo

Genera 15–20 títulos candidatos, elige 3, escribe la descripción con las fuentes citadas, las etiquetas,
los capítulos a partir de los tiempos reales de las escenas y el texto de la miniatura.

**Rechaza si:** el título promete algo que el vídeo no cumple. La retención castiga el clickbait mucho
más que el CTR lo premia.

### 11. Publicador · `publicar.py` · determinista
Sube a YouTube vía Data API v3 en estado **privado**. Un humano (tú) le da a publicar durante las
primeras semanas, como pediste. Después, un solo cambio de bandera lo automatiza.

### 12. Analista · `agente_analista`
**Entrada** YouTube Analytics → **Salida** `metricas/<semana>.json`
**Motor** Gemini Flash · **Cadencia** semanal

Retención por segundo, CTR, dónde se va la gente. Traduce eso a instrucciones concretas para el editor
jefe: «los vídeos que abren con una cifra retienen 12 puntos más a los 30 segundos».

---

## Cómo se orquesta

Tres tareas programadas de Cowork, que es lo que elegiste:

| Cuándo | Tarea | Qué hace |
|---|---|---|
| **Lunes 08:00** | `planificar` | Analista → Editor jefe → calendario actualizado y commit |
| **Martes y viernes 08:00** | `producir` | Guionista → Chistólogo → Verificador → commit → dispara GitHub Actions |
| **Diario 20:00** | `revisar` | Comprueba que las Actions terminaron y avisa de lo que espera aprobación |

GitHub Actions se encarga de las partes que necesitan internet (voz, render, subida). Yo me encargo de
las que necesitan criterio.

## Contrato del guion

Es el archivo que une a todos los agentes. Definido en `04_agentes/esquema_guion.json`.

```jsonc
{
  "id": "MDH-001",
  "idioma": "es",
  "titulo_trabajo": "...",
  "tesis": "La frase que el espectador debe poder repetir mañana",
  "pilares": ["A", "H"],
  "escenas": [
    {
      "tipo": "titulo|dato|enunciado|lista|cita|comparacion|diagrama|figura|cierre",
      "narracion": "Lo que se oye. Es lo único que define la duración.",
      "fuente": "A01",
      "...campos propios del tipo..."
    }
  ]
}
```

Reglas duras del contrato:

1. La **narración manda**. La duración de cada escena la fija la voz, nunca el diseño.
2. Toda escena con una cifra lleva `fuente`. Sin excepción.
3. En pantalla nunca aparece el texto de la narración: **el ojo y el oído reciben cosas distintas**,
   nunca lo mismo. Es la diferencia entre un vídeo y una presentación leída en alto.
4. Ninguna escena baja de 2,6 segundos ni pasa de 18. Si pasa de 18, hay que partirla.
