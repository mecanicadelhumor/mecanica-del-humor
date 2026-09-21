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

# Valor por defecto de «doi_confianza» en una ficha nueva: significa «nadie lo
# ha comprobado todavía contra la fuente», no «lo comprobé y no me fío». Ver el
# bucle de más abajo (19/09/2026, tras C39).
SIN_VERIFICAR = "por verificar automaticamente"

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
        # «doi_confianza» hace dos papeles: si sigue en el valor por defecto
        # (SIN_VERIFICAR, «por verificar automaticamente»), todavía no se ha
        # comprobado el DOI contra la fuente y se avisa. Si trae cualquier otro
        # texto, es la nota de quien SÍ lo comprobó (fecha, contra qué y quién) y
        # se imprime tal cual — antes se pisaba siempre con «⚠️ por verificar»,
        # así que una ficha ya verificada (p.ej. E06, G05, G06) salía marcada
        # como si no lo estuviera. Sin DOI, la misma nota va detrás de «Tipo»
        # (caso G03): no hay línea de DOI donde colgarla.
        confianza = o.get("doi_confianza")
        nota = "" if not confianza else (
            " ⚠️ por verificar" if confianza == SIN_VERIFICAR else f" · {confianza}")
        if o.get("doi"):
            A(f"DOI: [`{o['doi']}`](https://doi.org/{o['doi']}){nota}  ")
            nota = ""  # ya colocada; no se repite en la línea de Tipo
        A(f"Tipo: {o.get('tipo','')}{nota}\n")
        A(f"{o['por_que']}\n")
        # Nota ampliada (opcional): el párrafo largo de verificación que antes
        # solo existía escrito a mano en el .md —el «qué dice el artículo y qué
        # no», la corrección con lo que decía antes— y que la regeneración
        # borraba sin dejar rastro (C39, 18/09/2026).
        if o.get("nota_ampliada"):
            A(f"{o['nota_ampliada']}\n")

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
