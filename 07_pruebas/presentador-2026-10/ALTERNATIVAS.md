# Alternativas a Wan 2.2 5B para la persona sintética (C51.3-alternativas)

**Empezado el 26/10/2026 por la dirección en diferido; el informe completo es del 2/11** (compromiso
`C51.3-alternativas`). Nace de la nota del codirector: *«antes de bajar la calidad busquemos soluciones
alternativas… queremos algo que sea de verdad creíble… hay que ser creativos y tener paciencia»*.

**Lo que ya sabemos hoy**: el montaje de dos piezas (movimiento + labios encima) tiene un techo. Lo que
hacen los modelos nuevos es generar la cabeza entera **a partir de la voz** (gestos, hombros y boca a la
vez), que es justo lo que le falta a nuestro vaivén.

## Candidatos a mirar (sin verificar todavía: notas de arranque, no conclusiones)

| Candidato | Idea | Qué hay que comprobar el 2/11 |
|---|---|---|
| **Wan 2.2 S2V 14B** | Voz → vídeo de la persona hablando | Memoria real (se le atribuyen ~80 GB en una sola GPU: fuera de la T4) y licencia de los pesos en su ficha |
| **InfiniteTalk** | Wan 2.1 afinado para hablar sin límite de duración; hay versiones comprimidas (fp8, GGUF) | Si una versión comprimida cabe en 16 GB y, sobre todo, **la licencia de los pesos** (las webs que lo venden como servicio no dicen nada de los pesos) |
| **MultiTalk** | El hermano pequeño; se le atribuye consumo de 12-16 GB | Lo mismo: memoria medida y licencia |
| **Kandinsky S2V 1.0 (variante «Lite», 2 B)** | De 2026, se compara con los anteriores | Memoria y licencia |
| **GPU prestada** | Si nada cabe en la T4 de Kaggle: servicios con créditos gratuitos mensuales en GPUs grandes | Cuáles siguen dando créditos, cuánto duran y si permiten uso comercial |

**Método del 2/11**: licencia primero (si los pesos no permiten uso comercial, se descarta sin probar,
como hicimos con InsightFace y BiSeNet); después memoria medida en la T4, no la de las fichas; después
calidad, con la misma cara 2 y la misma voz para poder comparar con lo de hoy. Y el coste por segundo de
vídeo: un Short necesita 2-3 s de presentador, no sesenta.

**Lo que no se hace**: pagar nada sin decírselo al codirector, ni meter un modelo cuya licencia no
permita uso comercial, ni dar por bueno un número de memoria que no hayamos medido nosotros.
