#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vista.py — el espejo del sistema visual.

Renderiza a PNG un muestrario con los nueve tipos de escena, o las escenas que
le pidas de un guion real, sin montar vídeo. Tarda segundos en vez de minutos.

    python3 vista.py -o 03_produccion/vista_previa            # muestrario
    python3 vista.py --guion 05_calendario/guiones/MDH-002.es.json --escenas 1,4,13 -o /tmp/v

Existe porque tocar el diseño a ciegas es la forma más rápida de romper un
canal que ya funciona. Cualquiera —persona o agente— que cambie escena.html
debería poder ver el antes y el después antes de que eso llegue a un vídeo.

Importante: las tipografías mandan. Este script solo dice la verdad si se
ejecuta donde están instaladas Archivo Black, Inter y JetBrains Mono, es decir
en GitHub Actions (véase .github/workflows/vista.yml). En un entorno sin ellas
las medidas de línea cambian y los desbordamientos que veas pueden ser falsos.
"""
import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent
ESCENA_HTML = AQUI / "escena.html"
RAIZ = AQUI.parents[1]

ESCALONADO, ENTRADA, SALIDA = 0.16, 0.55, 0.45

# Muestrario: un ejemplo de cada tipo, con textos de longitud realista —
# los de verdad, sacados de guiones ya producidos. Un muestrario con «Lorem
# ipsum» miente justo en lo que importa, que es si el texto cabe.
MUESTRARIO = [
    {"tipo": "titulo", "etiqueta": "Episodio 02", "titulo": "Por qué te *ríes*",
     "subtitulo": "El mecanismo, pieza a pieza", "narracion": "x"},
    {"tipo": "enunciado",
     "texto": "Explicar un chiste no lo estropea por educación. Lo estropea *mecánicamente*.",
     "narracion": "x"},
    {"tipo": "dato", "cifra": "50 años",
     "pie": "de investigación midiendo _exactamente lo contrario_ de lo que crees sobre tu propio humor",
     "narracion": "x"},
    {"tipo": "lista", "titulo": "Tres formas de hacer algo benigno",
     "puntos": ["Que la víctima seas *tú*",
                "Señalar la idea, no a la persona",
                "Marcar que es juego: tono, cara, ritmo"], "narracion": "x"},
    {"tipo": "cita", "texto": "Comedia es tragedia más tiempo.",
     "autor": "Atribuido a Steve Allen. Ahora con una gráfica detrás", "narracion": "x"},
    {"tipo": "comparacion", "titulo": "La misma queja, dos versiones",
     "et_a": "Genérico", "a": "«Los aviones son incómodos.»",
     "et_b": "Específico",
     "b": "«El brazo del asiento del medio pertenece a *quien lo tome primero* y esa es toda la ley que hay ahí arriba.»",
     "narracion": "x"},
    {"tipo": "diagrama", "titulo": "Las dos fases",
     "pasos": [{"titulo": "Detección", "pie": "esto no cuadra"},
               {"titulo": "Resolución", "pie": "ah, era eso"},
               {"titulo": "Recompensa", "pie": "y llega el premio"}], "narracion": "x"},
    {"tipo": "cierre", "titulo": "Violación *más* algo benigno. Nada más.",
     "subtitulo": "En el próximo episodio: por qué «todavía es pronto para reírse de eso» tiene fecha de caducidad.",
     "narracion": "x"},
    # Los dos enunciados de más van AL FINAL a propósito. «enunciado» tiene
    # desde el 19/08 tres variantes de composición que dependen del número de
    # escena, y con un solo ejemplo en el muestrario solo se vería una. Puestos
    # aquí, el ejemplo de arriba cae en n=2 y estos en n=9 y n=10, así que la
    # vista previa enseña las tres. Al final y no intercalados para no correr
    # la numeración de los ocho muestrarios que ya existen: renumerarlos
    # dejaría PNG huérfanos con el nombre viejo en el repositorio.
    {"tipo": "enunciado",
     "texto": "Nadie se ríe de un chiste que ya ha entendido. Se ríe *mientras* lo entiende.",
     "narracion": "x"},
    {"tipo": "enunciado",
     "texto": "Demasiado cerca duele. Demasiado lejos *aburre*.",
     "narracion": "x"},
]


def instante_pleno(n_uds, dur):
    """El momento en el que todas las unidades ya han entrado y ninguna se va."""
    t = max(n_uds - 1, 0) * ESCALONADO + ENTRADA + 0.05
    return min(t, max(dur - SALIDA - 0.05, 0.1))


def escenas_de(guion_path, cuales):
    g = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    idioma = g.get("idioma", "es")
    fuera = []
    for i, e in enumerate(g["escenas"], 1):
        if cuales and i not in cuales:
            continue
        d = dict(e)
        d["n"], d["idioma"] = i, idioma
        d["marca"] = "Humor Mechanics" if idioma == "en" else "Mecánica del Humor"
        d["ref"] = e.get("fuente", "") or ""
        d.setdefault("duracion_s", 8.0)
        fuera.append(d)
    return fuera


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--salida", required=True)
    ap.add_argument("--guion", default=None, help="si se omite, se pinta el muestrario")
    ap.add_argument("--escenas", default=None, help="números separados por comas")
    ap.add_argument("--escala", type=float, default=0.5,
                    help="0.5 = 960x540, suficiente para juzgar y ligero para el repositorio")
    a = ap.parse_args()

    if a.guion:
        cuales = {int(x) for x in a.escenas.split(",")} if a.escenas else None
        escenas = escenas_de(a.guion, cuales)
        prefijo = Path(a.guion).name.split(".")[0]
    else:
        escenas = [dict(e, n=i, idioma="es", marca="Mecánica del Humor", ref="A01",
                        duracion_s=8.0) for i, e in enumerate(MUESTRARIO, 1)]
        prefijo = "muestrario"

    salida = Path(a.salida)
    salida.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none",
                                      "--disable-lcd-text", "--hide-scrollbars"])
        pag = nav.new_page(viewport={"width": 1920, "height": 1080},
                           device_scale_factor=a.escala)
        pag.goto(ESCENA_HTML.as_uri())
        for e in escenas:
            n_uds = pag.evaluate("d => cargar(d)", e)
            pag.evaluate("t => pintar(t)", instante_pleno(n_uds, e["duracion_s"]))
            destino = salida / f"{prefijo}_{e['n']:02d}_{e['tipo']}.png"
            pag.screenshot(path=str(destino))
            print(f"  {destino.name}  ({n_uds} unidades)")
        nav.close()

    # Deja constancia de con qué tipografías se pintó: una vista previa hecha
    # sin Archivo Black no dice lo mismo que la de producción, y conviene que
    # quien la mire lo sepa sin tener que preguntar.
    try:
        import subprocess
        fam = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True).stdout
        presentes = sorted({f for f in ("Archivo Black", "Inter", "JetBrains Mono", "DejaVu Sans")
                            if f.lower() in fam.lower()})
    except Exception:
        presentes = []
    (salida / "_entorno.json").write_text(json.dumps(
        {"tipografias_presentes": presentes, "escala": a.escala,
         "_nota": "Si falta «Archivo Black», los títulos NO son los de producción."},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(escenas)} escenas en {salida} · tipografías: {', '.join(presentes) or 'ninguna de las de marca'}")


if __name__ == "__main__":
    main()
