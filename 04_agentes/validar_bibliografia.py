#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validar_bibliografia.py — que el .md y su JSON no se separen.

C39 (18/09/2026).

## Por qué existe

`01_bibliografia/BIBLIOGRAFIA_CURADA.md` lo **genera** `scripts/generar_md.py` a
partir de `data/semillas.json`, y su propia cabecera lo dice: «No edites este
archivo a mano: edita el JSON y vuelve a ejecutar generar_md.py».

Nadie lo ha hecho nunca. Medido el 18/09/2026, cinco fichas estaban corregidas en
el `.md` y sin corregir en el JSON:

| Ficha | Corregido en el .md | Qué seguía diciendo el JSON |
|---|---|---|
| `C05` | título y DOI (revisión diaria, 18/09) | el título y el DOI de otro artículo |
| `F03` | DOI (el codirector, 18/09)           | — |
| `F04` | título y autores (el codirector, 18/09) | otro título |
| `F05` | DOI (el codirector, 18/09)           | el DOI viejo |
| `G03` | autores y año (revisión diaria, 18/09) | «varios», 2015 |

**Es decir: la próxima vez que alguien regenere el `.md`, se pierden las cinco.**
Nada avisaría. El trabajo de dos personas de un día entero desaparecería en un
commit que parece rutina, y la única señal sería que una ficha vuelve a estar mal
semanas después.

Es la trampa 4 del proyecto con otra cara: un fichero derivado que se edita a mano
miente sobre su origen hasta el día en que se vuelve a derivar.

## Qué comprueba, y qué NO

Comprueba **lo único que se puede comprobar sin red y sin equivocarse nunca**: que
cada ficha diga lo mismo en los dos sitios. Título, autores, año, fuente y DOI.

**19/09/2026 · añadido «fuente».** El primer regenerado tras C39 (revisión diaria,
19/09) demostró que la lista de arriba se quedaba corta: comparando título, autores,
año y DOI, este script decía «los dos ficheros dicen lo mismo» y sin embargo
regenerar borraba el volumen y las páginas de `C05`, `E06`, `G05` y `G06` (estaban
en el `.md`, hechas a mano, y `semillas.json` solo tenía el nombre de la revista) y
el párrafo largo de verificación de `E02`, `E06`, `G05` y `G06` (que no tenía —y
sigue sin tener— ningún campo correspondiente antes de que `generar_md.py` ganara
`nota_ampliada` ese mismo día). Lo de la fuente sí se puede comprobar sin red, así
que se comprueba desde hoy. Lo del párrafo largo no tiene un campo estructurado que
comparar carácter a carácter con algo del `.md` sin re-implementar aquí el propio
`generar_md.py` — así que, por ahora, sigue siendo un punto ciego: si alguien
escribe un `nota_ampliada` nuevo a mano en el `.md` en vez de en el JSON, este
script no lo va a ver. Queda dicho para quien lea esto de aquí en adelante.

**No comprueba que el DOI exista ni que apunte al artículo que la ficha nombra.**
Eso hace falta —es lo que estaba roto en F04, F05, C05 y G03— pero necesita salir a
internet, y ni el contenedor de la revisión diaria ni este tienen permitido llegar
a `api.crossref.org` (comprobado el 18/09: el proxy de egreso lo rechaza). Quien sí
puede es la revisión diaria con `WebFetch`, que es como verificó C05 hoy, y por eso
esa comprobación vive en su prompt y no aquí. Una comprobación que no se puede
ejecutar no es una comprobación: es una intención.

    python3 04_agentes/validar_bibliografia.py
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MD = RAIZ / "01_bibliografia" / "BIBLIOGRAFIA_CURADA.md"
JSON = RAIZ / "01_bibliografia" / "data" / "semillas.json"

# ### `C05` ★★ Título del artículo
CABECERA = re.compile(r"^### `([A-Z]\d{2})` ([★]*)\s*(.+?)\s*$")
# **Autores** (2012) · *Revista*, 6(1), 74-82  ó  **Autores** (2012) · *Revista, 6(1), 74-82*
AUTORES = re.compile(r"^\*\*(.+?)\*\*\s*\((\d{4})\)\s*·\s*\*(.*?)\*")
DOI = re.compile(r"^DOI: \[`([^`]+)`\]")


# Comillas y guiones tipográficos frente a los de máquina de escribir. El .md los
# lleva rectos y el JSON curvos (o al revés) según quién escribiera cada ficha, y
# eso no es una diferencia: es una fuente. Sin esto, E06 salía señalada por un par
# de comillas — y una comprobación que señala ruido se acaba ignorando, que es la
# lección de la regla 14.4 de REGLAS.md.
TIPOGRAFICOS = str.maketrans({
    "\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'",
    "\u00ab": '"', "\u00bb": '"', "\u2013": "-", "\u2014": "-", "\u2212": "-",
})


def normal(s):
    """Para comparar: comillas y guiones normalizados, minúsculas, un solo espacio.

    No quita el resto de la puntuación: un título que cambia un dos puntos por un
    guion SÍ es una diferencia que conviene ver, aunque sea menor.
    """
    return re.sub(r"\s+", " ", (s or "").strip().translate(TIPOGRAFICOS)).lower()


def es_de_prueba(obra):
    """Las entradas que el corpus lleva a propósito y el .md excluye.

    La cabecera de BIBLIOGRAFIA_CURADA.md lo dice: hay «una entrada de control (un
    paper que no pertenece al tema) y dos duplicados», puestos para comprobar que
    el agente bibliotecario descarta ruido y fusiona repetidos. Están en el JSON y
    NO en el .md, y eso es correcto: 78 obras contra 77. Sin esta excepción, A09
    saldría señalada todas las veces por estar bien.
    """
    return (obra.get("fuente") == "descartar"
            or obra.get("autores") == "control-negativo"
            or "ENTRADA DE CONTROL" in (obra.get("por_que") or ""))


def leer_md():
    fichas, actual = {}, None
    for linea in MD.read_text(encoding="utf-8").splitlines():
        m = CABECERA.match(linea)
        if m:
            actual = {"id": m.group(1), "titulo": m.group(3),
                      "autores": None, "anio": None, "fuente": None, "doi": None}
            fichas[actual["id"]] = actual
            continue
        if actual is None:
            continue
        m = AUTORES.match(linea)
        if m and actual["autores"] is None:
            actual["autores"], actual["anio"], actual["fuente"] = (
                m.group(1), int(m.group(2)), m.group(3))
            continue
        m = DOI.match(linea)
        if m and actual["doi"] is None:
            actual["doi"] = m.group(1)
    return fichas


def leer_json():
    datos = json.loads(JSON.read_text(encoding="utf-8"))
    obras = datos if isinstance(datos, list) else (
        datos.get("obras") or datos.get("semillas") or [])
    return {o["id"]: o for o in obras if o.get("id")}


def main():
    md, js = leer_md(), leer_json()
    problemas = []

    for fid in sorted(set(md) | set(js)):
        if fid not in js:
            problemas.append(f"{fid}: está en el .md y NO en semillas.json. "
                             f"Al regenerar, la ficha desaparece.")
            continue
        if fid not in md:
            if es_de_prueba(js[fid]):
                continue  # entrada de control: tiene que estar solo en el JSON
            problemas.append(f"{fid}: está en semillas.json y NO en el .md. "
                             f"O se borró a mano del .md, o el .md está sin regenerar.")
            continue
        a, b = md[fid], js[fid]
        for campo, va, vb in (("título",  a["titulo"],  b.get("titulo")),
                              ("autores", a["autores"], b.get("autores")),
                              ("año",     a["anio"],    b.get("anio")),
                              ("fuente",  a["fuente"],  b.get("fuente")),
                              ("DOI",     a["doi"],     b.get("doi"))):
            if va is None and vb is None:
                continue
            if normal(str(va)) != normal(str(vb)):
                problemas.append(
                    f"{fid} · {campo} no coincide:\n"
                    f"        .md  : {va}\n"
                    f"        json : {vb}")

    print(f"{len(md)} fichas en el .md · {len(js)} en semillas.json")
    if not problemas:
        print("\nLos dos ficheros dicen lo mismo. Regenerar el .md es seguro.")
        return 0
    print(f"\nDESINCRONIZADAS ({len(problemas)}):\n")
    for p in problemas:
        print(f"  ✗ {p}")
    print("\nLa fuente de verdad es `data/semillas.json`: el .md se genera desde él.")
    print("Lleva la corrección al JSON *también*, o el próximo `generar_md.py` la borra.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
