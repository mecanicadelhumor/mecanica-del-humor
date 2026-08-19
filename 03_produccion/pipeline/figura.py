#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
figura.py — Agente Ilustrador.

Convierte las escenas de tipo «figura» de un guion en imágenes PNG con la
paleta del canal, y escribe en el propio guion la ruta de cada imagen para que
render.py la encuentre.

    python3 figura.py build/MDH-003.es/guion.timed.json

Por qué existe: el esquema y escena.html contemplan escenas de tipo «figura»
desde el principio, pero no había quien las generara, así que ningún guion las
usaba y los vídeos no tienen ni una gráfica. Es el ítem V1 de MEJORA_VISUAL.md.

Dónde encaja en el pipeline: DESPUÉS de voz.py y ANTES de render.py. voz.py
deja guion.timed.json con las duraciones reales; figura.py le añade las rutas
de las imágenes; render.py lo pinta. Si se ejecuta sobre un guion sin escenas
de tipo «figura» no hace nada y sale con código 0: así el paso del workflow
puede ser incondicional.

Reglas que cumple, de MEJORA_VISUAL.md:
  - Determinista. Mismos datos, mismo PNG. Nada de azar.
  - Nada de internet en tiempo de render: matplotlib dibuja en local.
  - Coste de render CERO. La figura es una imagen estática: entra con el
    escalonado que ya captura render.py y no anima nada en el tramo central.

El fondo va TRANSPARENTE a propósito: la escena ya tiene su fondo y su
retícula de plano técnico, y un PNG opaco los taparía dejando un rectángulo
plano en medio de la pantalla.
"""
import argparse
import json
from pathlib import Path

import logging

import matplotlib
matplotlib.use("Agg")                      # sin pantalla: esto corre en un runner
# En el runner de Actions Inter está instalada y esto no salta. En un contenedor
# sin ella, matplotlib avisa una vez por cada texto de la figura y llena el log
# de ruido que tapa los avisos de verdad. La sustitución por DejaVu ocurre igual.
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Paleta de marca (02_marca). Deben coincidir con las variables CSS de
# escena.html: si algún día cambian allí, cambian aquí.
FONDO   = "#0B1220"
TINTA   = "#F2F4F8"
TENUE   = "#8A97AE"
AMBAR   = "#FFB020"
CIAN    = "#4CC9F0"
CORAL   = "#EF476F"

# 1500x660 px: el ancho útil de .caja y el max-height que le da escena.html.
ANCHO_PULG, ALTO_PULG, PPP = 7.5, 3.3, 200

# Inter para todo, con los respaldos habituales. En el runner de Actions está
# instalada (fonts-inter); en un contenedor sin ella matplotlib cae a DejaVu y
# la figura sigue saliendo, solo que con otra letra. Igual que el resto del
# sistema visual: la vista previa de verdad es la de Actions.
TIPOS = ["Inter", "DejaVu Sans", "sans-serif"]


def _lienzo():
    fig, ax = plt.subplots(figsize=(ANCHO_PULG, ALTO_PULG), dpi=PPP)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color(TENUE)
        ax.spines[lado].set_linewidth(1.4)
    ax.tick_params(colors=TENUE, labelsize=13, length=5, width=1.2)
    for etiqueta in ax.get_xticklabels() + ax.get_yticklabels():
        etiqueta.set_fontfamily(TIPOS)
    ax.grid(axis="y", color=TENUE, alpha=0.16, linewidth=1.0)
    ax.set_axisbelow(True)
    return fig, ax


def _ejes(ax, spec):
    for eje, clave in ((ax.set_xlabel, "etiqueta_x"), (ax.set_ylabel, "etiqueta_y")):
        if spec.get(clave):
            eje(spec[clave], color=TENUE, fontsize=14, fontfamily=TIPOS, labelpad=10)


def _marca(ax, spec, x, y):
    """Anotación opcional sobre un punto concreto: «aquí está el máximo»."""
    m = spec.get("marca")
    if not m or "x" not in m:
        return
    try:
        i = list(x).index(m["x"])
    except ValueError:
        return
    ax.plot([x[i]], [y[i]], "o", color=AMBAR, markersize=11,
            markeredgecolor=FONDO, markeredgewidth=2.5, zorder=5)
    if m.get("texto"):
        ax.annotate(m["texto"], (x[i], y[i]), textcoords="offset points",
                    xytext=(0, 18), ha="center", color=AMBAR, fontsize=15,
                    fontfamily=TIPOS, fontweight="bold", zorder=6)


def dibujar(spec, destino):
    """spec -> PNG. Devuelve la ruta. Determinista."""
    clase = spec.get("clase", "linea")
    fig, ax = _lienzo()

    if clase == "barras":
        x = [str(e) for e in spec["x"]]
        y = list(spec["y"])
        # El ámbar marca la barra destacada; el resto en cian apagado, para que
        # el color signifique algo en vez de decorar.
        destacada = spec.get("destacar")
        colores = [AMBAR if (destacada is not None and str(destacada) == e) else CIAN
                   for e in x]
        ax.bar(x, y, color=colores, width=0.62, zorder=3)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=4, integer=False))
    else:                                            # linea
        x, y = list(spec["x"]), list(spec["y"])
        ax.plot(x, y, color=AMBAR, linewidth=3.2, solid_capstyle="round", zorder=4)
        ax.fill_between(x, y, min(y), color=AMBAR, alpha=0.12, zorder=2)
        ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=4))
        _marca(ax, spec, x, y)

    _ejes(ax, spec)
    fig.tight_layout(pad=0.6)
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, transparent=True, dpi=PPP)
    plt.close(fig)
    return destino


def procesar(guion_path, salida=None):
    guion_path = Path(guion_path)
    guion = json.loads(guion_path.read_text(encoding="utf-8"))
    carpeta = Path(salida) if salida else guion_path.parent / "figuras"

    hechas = 0
    for i, e in enumerate(guion.get("escenas", []), 1):
        if e.get("tipo") != "figura":
            continue
        spec = e.get("figura")
        if not spec:
            # Escena de tipo figura con una imagen ya puesta a mano: se respeta.
            if e.get("imagen"):
                continue
            print(f"::warning::Escena {i} es de tipo «figura» y no trae ni «figura» ni «imagen». Se deja vacía.")
            continue
        destino = carpeta / f"escena_{i:03d}.png"
        dibujar(spec, destino)
        # Ruta ABSOLUTA: escena.html se carga con file:// desde el directorio
        # del pipeline, así que una ruta relativa se resolvería contra ese
        # directorio y no contra build/. Con la absoluta no hay ambigüedad.
        e["imagen"] = destino.resolve().as_uri()
        hechas += 1
        print(f"  escena {i:>2}  {spec.get('clase','linea'):<7}  {destino}")

    if hechas:
        guion_path.write_text(json.dumps(guion, ensure_ascii=False, indent=2),
                              encoding="utf-8")
    print(f"{hechas} figura(s) generada(s) para {guion_path.name}.")
    return hechas


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Genera las figuras de un guion.")
    ap.add_argument("guion", help="normalmente build/<ID>/guion.timed.json")
    ap.add_argument("-o", "--salida", default=None, help="carpeta de las imágenes")
    a = ap.parse_args()
    procesar(a.guion, a.salida)
