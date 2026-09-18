#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
muestrear_geometria.py — el script de muestreo que pedía el encargo 8 de
la revisión diaria («escena.html: el caso que queda abierto — `lista` +
personaje»), y que hasta hoy (18/09/2026) no existía como herramienta
reutilizable.

La lección que lo motiva está escrita en `escena.html` junto a
`padding-bottom:790px` y en `00_estrategia/tareas/revision-diaria.md`: **medir
una escena quieta miente cuando la escena se mueve.** El 07/09 el hueco entre
el pie de una escena y la cara del personaje se midió en reposo (48px) y
pareció suficiente; en movimiento —el personaje entra, respira, y `#escena`
hace un zoom del 2,2 %— el hueco real caía a 7px, y así salió publicado
MDS-011 con la cara pegada al texto. Aquella calibración se hizo a mano,
mirando 21 instantes por escena uno a uno. Este script hace lo mismo, pero
como herramienta: se puede volver a correr cada vez que cambien los guiones
o `escena.html`, en vez de repetir el trabajo manual.

Qué mide: para cada escena vertical (`formato: corto`) con `personaje`, pinta
la escena en 21 instantes repartidos por su duración (mismo número que la
calibración del 07/09) y en cada uno mide el hueco vertical entre el borde
inferior de `.caja` (el bloque de texto) y el borde superior de `#personaje`
(la cara). Se queda con el PEOR caso — el hueco más pequeño — de los 21.

Uso:
    python3 muestrear_geometria.py                                   # todos los guiones
    python3 muestrear_geometria.py 05_calendario/guiones/MDS-020.es.json
    python3 muestrear_geometria.py --umbral 50 --json /tmp/informe.json

Importante, y es la razón por la que este script NO decide nada por sí solo
—solo informa—: las medidas de línea dependen de que Archivo Black, Inter y
JetBrains Mono estén instaladas (ver la misma advertencia en `vista.py`). Si
no lo están, el script lo dice en el informe y en la salida, y los números de
ESE informe concreto no sirven para decidir nada: hay que volver a correrlo
donde las tipografías de marca estén instaladas (GitHub Actions, o el
ordenador del codirector) antes de tocar `ajustarTamano()` con ellos.
"""
import argparse
import json
import subprocess
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent
ESCENA_HTML = AQUI / "escena.html"
RAIZ = AQUI.parents[1]
GUIONES_DIR = RAIZ / "05_calendario" / "guiones"

N_MUESTRAS = 21  # mismo número que la calibración manual del 07/09/2026
FUENTES_DE_MARCA = ("Archivo Black", "Inter", "JetBrains Mono")


def fuentes_instaladas():
    try:
        fam = subprocess.run(["fc-list", ":", "family"], capture_output=True,
                              text=True, timeout=10).stdout.lower()
    except Exception:
        return []
    return sorted(f for f in FUENTES_DE_MARCA if f.lower() in fam)


def escenas_con_personaje(guion_path):
    """Igual que escenas_de() en vista.py, pero solo lo que hace falta aquí:
    escenas verticales con personaje, con su número de escena y su id de
    guion, para poder señalar exactamente cuál falla."""
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    if g.get("formato") != "corto":
        return []
    idioma = g.get("idioma", "es")
    fuera = []
    for i, e in enumerate(g.get("escenas", []), 1):
        if not e.get("personaje"):
            continue
        d = dict(e)
        d["n"], d["idioma"], d["formato"] = i, idioma, "corto"
        d["marca"] = "Humor Mechanics" if idioma == "en" else "Mecánica del Humor"
        d["ref"] = e.get("fuente", "") or ""
        d.setdefault("duracion_s", 8.0)
        fuera.append(d)
    return fuera


def peor_hueco(pag, d):
    """Carga la escena, la pinta en N_MUESTRAS instantes y devuelve el peor
    (el menor) hueco vertical entre `.caja` y `#personaje`, con el instante
    en el que ocurre. None si alguno de los dos elementos no está en el
    árbol de render (por ejemplo una plantilla sin `.caja`)."""
    n_uds = pag.evaluate("d => cargar(d)", d)
    dur = d["duracion_s"]
    peor = None
    for i in range(N_MUESTRAS):
        t = dur * i / (N_MUESTRAS - 1)
        pag.evaluate("t => pintar(t)", t)
        r = pag.evaluate("""() => {
            const caja = document.querySelector('.caja');
            const cara = document.getElementById('personaje');
            if (!caja || !cara) return null;
            if (caja.getClientRects().length === 0 || cara.getClientRects().length === 0) return null;
            const rc = caja.getBoundingClientRect();
            const rp = cara.getBoundingClientRect();
            return { gap: rp.top - rc.bottom,
                     caja_bottom: rc.bottom, personaje_top: rp.top };
        }""")
        if r is None:
            continue
        if peor is None or r["gap"] < peor["gap"]:
            peor = dict(r, t=round(t, 3))
    return n_uds, peor


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guiones", nargs="*",
                     help="rutas a guiones .es.json / .en.json; si se omite, todos los de 05_calendario/guiones/")
    ap.add_argument("--umbral", type=float, default=50.0,
                     help="hueco en px por debajo del cual se marca como riesgo (por defecto 50, igual que TOL_ALTO)")
    ap.add_argument("--json", default=None, help="si se da, también escribe el informe completo aquí")
    a = ap.parse_args()

    rutas = [Path(g) for g in a.guiones] if a.guiones else sorted(GUIONES_DIR.glob("*.json"))
    fuentes = fuentes_instaladas()
    if len(fuentes) < len(FUENTES_DE_MARCA):
        faltan = sorted(set(FUENTES_DE_MARCA) - set(fuentes))
        print(f"AVISO: faltan tipografías de marca ({', '.join(faltan)}). "
              f"Los px de este informe NO son de fiar para decidir nada — "
              f"vuelve a correr esto donde estén instaladas.\n")

    informe = {"fuentes_de_marca_instaladas": fuentes, "umbral_px": a.umbral, "escenas": []}
    peor_global = None

    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none",
                                      "--disable-lcd-text", "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": 1080, "height": 1920})
        pag.goto(ESCENA_HTML.as_uri())

        for ruta in rutas:
            if not ruta.exists():
                print(f"  (no existe: {ruta})")
                continue
            for d in escenas_con_personaje(ruta):
                n_uds, peor = peor_hueco(pag, d)
                if peor is None:
                    continue
                fila = {"guion": ruta.stem, "escena": d["n"], "tipo": d.get("tipo"),
                        "personaje": d.get("personaje"), **peor}
                informe["escenas"].append(fila)
                marca = "RIESGO" if peor["gap"] < a.umbral else "ok"
                print(f"  {ruta.stem:14s} esc.{d['n']:<2d} [{d.get('tipo','?'):11s}] "
                      f"hueco peor = {peor['gap']:7.1f}px  en t={peor['t']:.2f}s  ({marca})")
                if peor_global is None or peor["gap"] < peor_global["gap"]:
                    peor_global = dict(fila)
        nav.close()

    informe["escenas"].sort(key=lambda f: f["gap"])
    print()
    if peor_global is None:
        print("Ninguna escena vertical con personaje encontrada en lo pedido.")
    else:
        print(f"Peor caso del lote: {peor_global['guion']} escena {peor_global['escena']} "
              f"— {peor_global['gap']:.1f}px en t={peor_global['t']:.2f}s")
        bajo_umbral = [f for f in informe["escenas"] if f["gap"] < a.umbral]
        if bajo_umbral:
            print(f"{len(bajo_umbral)} escena(s) por debajo del umbral de {a.umbral}px — revisar antes de producir.")

    if a.json:
        Path(a.json).write_text(json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nInforme completo: {a.json}")


if __name__ == "__main__":
    main()
