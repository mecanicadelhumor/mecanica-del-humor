#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera BIBLIOGRAFIA_CURADA.md a partir de semillas.json (o corpus.json si existe)."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "data" / "corpus.json"
if not FUENTE.exists():
    FUENTE = RAIZ / "data" / "semillas.json"
SALIDA = RAIZ / "BIBLIOGRAFIA_CURADA.md"

d = json.loads(FUENTE.read_text(encoding="utf-8"))
obras = [o for o in d["obras"] if o.get("autores") != "control-negativo"]

L = []
A = L.append
A("# Bibliografía curada — la ciencia del humor\n")
A("> Base de conocimiento de **Mecánica del Humor / Humor Mechanics**.")
A("> Generado desde `data/semillas.json`. No edites este archivo a mano: edita el JSON y vuelve a ejecutar `scripts/generar_md.py`.\n")
A(f"**{len(obras)} obras** en 12 pilares temáticos. Cada pilar alimenta una serie de vídeos.\n")

A("## Cómo se ha curado\n")
A("El criterio no ha sido «lo más citado» sino **lo que da lugar a un vídeo enseñable**. Cada entrada")
A("responde a una pregunta que un espectador se hace de verdad, y trae consigo un dato, un experimento")
A("o una técnica que se puede mostrar en pantalla. Tres niveles:\n")
A("| Prioridad | Significado | Uso en el canal |")
A("|---|---|---|")
A("| **1** | Imprescindible | Define una teoría, una medida o un hallazgo que se repetirá en muchos vídeos. Leer entero. |")
A("| **2** | Importante | Aporta evidencia concreta a uno o dos vídeos. Leer resumen + resultados. |")
A("| **3** | Complementario | Contexto, réplicas y aplicaciones. Consultar cuando haga falta. |\n")
A("Se han incluido a propósito **una entrada de control** (un paper que no pertenece al tema) y **dos")
A("duplicados** con títulos distintos: sirven para comprobar que el agente bibliotecario descarta ruido")
A("y fusiona repetidos antes de que nadie los lea. Están marcados y excluidos del corpus final.\n")

A("## Índice de pilares\n")
for cod, nombre in d["pilares"].items():
    n = len([o for o in obras if o["pilar"] == cod])
    A(f"- **{cod}. {nombre}** — {n} obras")
A("")

for cod, nombre in d["pilares"].items():
    items = sorted([o for o in obras if o["pilar"] == cod],
                   key=lambda x: (x["prioridad"], x["id"]))
    if not items:
        continue
    A(f"\n---\n\n## {cod}. {nombre}\n")
    for o in items:
        estrellas = "★" * (4 - o["prioridad"])
        A(f"### `{o['id']}` {estrellas} {o['titulo']}\n")
        A(f"**{o['autores']}** ({o.get('anio','s.f.')}) · *{o.get('fuente','')}*  ")
        if o.get("doi"):
            marca = " ⚠️ por verificar" if o.get("doi_confianza") else ""
            A(f"DOI: [`{o['doi']}`](https://doi.org/{o['doi']}){marca}  ")
        A(f"Tipo: {o.get('tipo','')}\n")
        A(f"{o['por_que']}\n")

A("\n---\n\n## Fuentes abiertas y repositorios\n")
A("De aquí sale el material, y de aquí seguirá saliendo cuando el agente bibliotecario amplíe el corpus.\n")
A("| Fuente | Acceso | Para qué la usamos |")
A("|---|---|---|")
for f in d["fuentes_abiertas"]:
    A(f"| [{f['nombre']}]({f['url']}) | {f['acceso']} | {f['uso']} |")

A("\n## Clásicos en dominio público\n")
A("Gratis, legales y con un peso retórico enorme: citar a Kant sobre por qué nos reímos abre un vídeo solo.\n")
for c in d["clasicos_dominio_publico"]:
    A(f"- **{c['titulo']}** — {c['autor']} ({c['anio']}). {c['por_que']}")

A("\n---\n\n## Política de uso legal\n")
A("- Solo se descarga material en **acceso abierto**. Nunca repositorios pirata.")
A("- De lo cerrado se usan **resumen, datos publicados y cita**, que es lo que necesita un guion.")
A("- Los libros se compran o se piden en biblioteca; en el corpus figuran como referencia, no como archivo.")
A("- Todo dato que salga en pantalla lleva su `id` de esta bibliografía en el guion, para que el")
A("  agente verificador pueda comprobarlo antes de publicar.\n")

SALIDA.write_text("\n".join(L), encoding="utf-8")
print(f"Escrito: {SALIDA} ({len(obras)} obras)")
