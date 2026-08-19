#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar_guion.py — portero automático del contrato de guion.

Se ejecuta antes de producir nada. Es barato, es determinista y detecta los
errores que un modelo comete cuando escribe treinta escenas seguidas.

    python3 validar_guion.py ../05_calendario/guiones/MDH-001.es.json

Devuelve código 1 si hay algún error grave: así GitHub Actions se para sola.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

PPM = 150            # palabras por minuto de la narración
MIN_ESCENA = 2.6
MAX_ESCENA = 20.0    # con la deriva lenta aguanta hasta aquí; más es narrativamente malo
MAX_IDEAL = 14.0
MAX_SEGUIDAS = 2     # escenas consecutivas del mismo tipo

CAMPOS = {
    "titulo": ["titulo"], "dato": ["cifra", "pie"], "enunciado": ["texto"],
    "lista": ["puntos"], "cita": ["texto", "autor"],
    "comparacion": ["a", "b"], "diagrama": ["pasos"],
    "figura": ["imagen"], "cierre": ["titulo"],
}
TEXTUALES = ["titulo", "subtitulo", "texto", "cifra", "pie", "a", "b", "et_a", "et_b", "etiqueta"]
# «Episodio 01» o «Parte 3» no son afirmaciones: no exigen fuente.
CON_DATOS = ["subtitulo", "texto", "cifra", "pie", "a", "b"]

# Firma de una narración que se quedó a medias: acaba en dos puntos y una sola
# palabra («…los aviones son incómodos: cero.»), o directamente en dos puntos,
# coma o punto y coma, o colgando de una conjunción. Ver el comentario largo
# de más abajo, donde se usa.
CORTADA = re.compile(r"(:\s*\S+\s*\.?|[:,;]|\b(y|o|pero|and|or|but)\s*\.?)\s*$", re.I)


def dur(e):
    n = len((e.get("narracion") or "").split())
    return max(MIN_ESCENA, n / PPM * 60 + 0.5) + e.get("pausa_despues_s", 0.45)


def texto_pantalla(e):
    partes = [str(e.get(c, "")) for c in TEXTUALES]
    partes += [str(p) for p in e.get("puntos", [])]
    partes += [f"{p.get('titulo','')} {p.get('pie','')}" for p in e.get("pasos", [])]
    return " ".join(partes)


def normal(s):
    return re.sub(r"[^a-záéíóúñ0-9 ]", " ", (s or "").lower())


def validar(path):
    g = json.loads(Path(path).read_text(encoding="utf-8"))
    errores, avisos = [], []

    if g.get("bloqueos"):
        errores.append(f"El guion trae bloqueos sin resolver: {g['bloqueos']}")
    if not g.get("tesis"):
        errores.append("Falta la tesis: el guion no sabe qué quiere que el espectador se lleve.")

    escenas = g["escenas"]
    total = 0.0
    tipos = []

    for i, e in enumerate(escenas, 1):
        t = e.get("tipo")
        tipos.append(t)
        d = dur(e)
        total += d

        for campo in CAMPOS.get(t, []):
            if not e.get(campo):
                errores.append(f"Escena {i} ({t}): falta el campo obligatorio «{campo}».")

        if d > MAX_ESCENA:
            errores.append(f"Escena {i}: dura {d:.1f}s. Máximo {MAX_ESCENA}s — pártela en dos.")
        elif d > MAX_IDEAL:
            avisos.append(f"Escena {i}: {d:.1f}s. Por encima de {MAX_IDEAL}s la pantalla se queda quieta.")

        pantalla = texto_pantalla(e)
        afirmaciones = " ".join(str(e.get(c, "")) for c in CON_DATOS) + \
                       " " + " ".join(str(p) for p in e.get("puntos", []))
        # cifra en pantalla sin fuente
        if re.search(r"\d", afirmaciones) and not e.get("fuente"):
            errores.append(f"Escena {i}: hay una cifra en pantalla sin campo «fuente».")

        # resaltado ámbar: uno por escena
        n_amb = len(re.findall(r"\*[^*]+\*", pantalla))
        if n_amb > 1:
            avisos.append(f"Escena {i}: {n_amb} resaltados en ámbar. Debe haber uno como máximo.")
        if pantalla.count("*") % 2 or pantalla.count("_") % 2:
            avisos.append(f"Escena {i}: marca de resaltado sin cerrar.")

        # la pantalla no repite la narración
        pn, nn = normal(pantalla), normal(e.get("narracion", ""))
        if len(pn.split()) >= 5 and pn.strip() and pn.strip() in nn:
            avisos.append(f"Escena {i}: el texto en pantalla es literal de la narración. "
                          f"El ojo y el oído deben recibir cosas distintas.")

        # narración cortada a media frase
        #
        # De dónde sale esto: la escena 24 de MDH-002 se produjo con la
        # narración «La misma queja, dos versiones. "Los aviones son
        # incómodos": cero.» y ahí se acababa. El chiste —el remate entero de
        # la escena— estaba escrito en el panel de pantalla pero no en la
        # narración, así que la voz dijo «cero» y se calló. El guion inglés
        # traía el mismo corte. Nadie lo detectó hasta que Silvestre lo oyó.
        #
        # La regla que hay detrás es de Silvestre y vale para todo el canal:
        # **el audio tiene que ser autosuficiente**, porque mucha gente ve
        # YouTube sin mirar la pantalla. Lo que está en pantalla y no se dice,
        # para esa gente no existe.
        #
        # Esto NO comprueba esa regla —comprobarla de verdad exige entender el
        # guion, y por eso la revisión diaria lee los guiones enteros—. Lo que
        # detecta es la *firma* de una narración truncada: que acabe en dos
        # puntos y una palabra suelta, o colgando de una conjunción. Probado
        # contra los doce guiones del repositorio: cero falsos positivos y
        # pilla las dos escenas 24.
        #
        # Es error y no aviso a propósito: parar una producción se arregla
        # relanzándola; publicar un vídeo con un remate mudo, no. Si algún día
        # molesta, bajarlo a «avisos» es cambiar una palabra en la línea de
        # abajo.
        narr = (e.get("narracion") or "").strip()
        if narr and CORTADA.search(narr):
            errores.append(f"Escena {i}: la narración parece cortada a media frase "
                           f"(«…{narr[-40:]}»). Lo que no se dice, quien escucha sin "
                           f"mirar la pantalla no lo recibe.")

        if t == "lista" and len(e.get("puntos", [])) > 5:
            errores.append(f"Escena {i}: una lista de más de 5 puntos no se lee en pantalla.")
        if t == "diagrama" and len(e.get("pasos", [])) > 5:
            errores.append(f"Escena {i}: un diagrama de más de 5 pasos no se lee.")

    # tipos repetidos seguidos
    racha, anterior = 1, None
    for i, t in enumerate(tipos, 1):
        racha = racha + 1 if t == anterior else 1
        if racha > MAX_SEGUIDAS:
            avisos.append(f"Escena {i}: {racha} escenas «{t}» seguidas. Rompe el ritmo visual.")
        anterior = t

    # estructura
    if tipos and tipos[0] != "titulo":
        avisos.append("La primera escena no es de tipo «titulo».")
    if tipos and tipos[-1] != "cierre":
        errores.append("La última escena debe ser de tipo «cierre».")

    # duración total
    m, s = divmod(total, 60)
    if total < 240:
        avisos.append(f"El vídeo dura {int(m)}m{int(s)}s: corto para el formato (mínimo 4 min).")
    if total > 540:
        errores.append(f"El vídeo dura {int(m)}m{int(s)}s: pasa de los 9 minutos. Recorta.")

    # densidad de humor: el chistólogo debe haber dejado sus notas
    if not g.get("notas_humor"):
        avisos.append("No hay «notas_humor»: el chistólogo no ha pasado por aquí.")

    reparto = Counter(tipos)
    dominante, n_dom = reparto.most_common(1)[0]
    if n_dom / len(tipos) > 0.45:
        avisos.append(f"El {n_dom*100//len(tipos)}% de las escenas son «{dominante}». "
                      f"Demasiada monotonía visual.")

    print(f"\n{path}")
    print(f"  {len(escenas)} escenas · {int(m)}m {s:04.1f}s · reparto {dict(reparto)}")
    fuentes = sorted({e["fuente"] for e in escenas if e.get("fuente")})
    print(f"  fuentes citadas: {', '.join(fuentes) or 'ninguna'}")
    if avisos:
        print(f"\n  AVISOS ({len(avisos)})")
        for a in avisos:
            print(f"    · {a}")
    if errores:
        print(f"\n  ERRORES ({len(errores)})")
        for x in errores:
            print(f"    ✗ {x}")
    else:
        print("\n  Sin errores graves.")
    return len(errores)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guiones", nargs="+")
    a = ap.parse_args()
    fallos = sum(validar(p) for p in a.guiones)
    sys.exit(1 if fallos else 0)
