#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_produccion/pipeline/visual.py — C50 (versión 12 del plan, 23/09/2026).

EN PRUEBA: hoy solo lo llama el workflow «Prueba visual (C50)», que monta el
muestrario de 07_pruebas/visual-23-09/. No lo llama nada de la producción. Cuando
el codirector haya mirado el muestrario y decidido, producir.yml lo llamará antes
del render con la especificación que la planificación escriba en cada guion.

Convierte una especificación visual (qué se busca en cada escena) en ficheros de
imagen o vídeo:

    1. vídeo de archivo de Pexels (vertical),
    2. si no, vídeo de archivo de Pixabay (casi siempre horizontal: se recorta),
    3. si no, imagen generada con FLUX.1 [schnell] en Cloudflare Workers AI.

Deja en `<salida>/<ID>/<variante>/` los ficheros y un `manifiesto.json` con la
fuente, el autor, el enlace y la licencia de cada plano: lo que exige la regla
9 de REGLAS.md antes de usar una sola imagen.

    python3 visual.py --especificacion 07_pruebas/visual-23-09/visuales.json \
                      --salida 07_pruebas/visual-23-09/salida MDS-023 MDS-024
    python3 visual.py ... --solo-ia MDS-023        # variante C: todo generado

SOLO CORRE DONDE HAY RED Y CLAVES: en GitHub Actions, con los secretos
PEXELS_API_KEY, PIXABAY_API_KEY, CLOUDFLARE_ACCOUNT_ID y CLOUDFLARE_API_TOKEN.
Ni los contenedores de las tareas programadas ni el ordenador del codirector
llegan a estas APIs (comprobado el 23/09: el proxy de salida las rechaza). Si
falta una clave, esa fuente se salta y se dice en el log; nunca se inventa un
plano. Si un plano no se resuelve por ninguna vía, queda como «sin_imagen» y el
muestrario lo pinta con el fondo de siempre: exactamente lo que haría la
producción.

"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
GUIONES = RAIZ / "05_calendario" / "guiones"
SALIDA = RAIZ / "07_pruebas" / "visual-23-09" / "salida"   # lo cambia --salida
AGENTE = "MecanicaDelHumor-prueba-C50/1.0 (+https://github.com/mecanicadelhumor/mecanica-del-humor)"

LICENCIA_PEXELS = "Licencia de Pexels (uso gratuito, también comercial; https://www.pexels.com/license/)"
LICENCIA_PIXABAY = "Licencia de contenido de Pixabay (uso gratuito, también comercial; https://pixabay.com/service/license-summary/)"
LICENCIA_IA = ("Imagen generada con IA: FLUX.1 [schnell] (Black Forest Labs) en Cloudflare "
               "Workers AI. Pesos abiertos Apache 2.0; en Cloudflare rigen además los términos "
               "de BFL (https://bfl.ai/legal/terms-of-service), que se leen antes de publicar.")
MODELO_IA = "@cf/black-forest-labs/flux-1-schnell"


# ---------------------------------------------------------------------------
# Red
# ---------------------------------------------------------------------------
def pedir(url, cabeceras=None, datos=None, intentos=3, espera=4):
    """GET (o POST si hay `datos`) que devuelve bytes. Reintenta los 429 y los
    5xx; un 4xx distinto es definitivo (no se paga dos veces por el mismo no:
    trampa 30)."""
    cab = {"User-Agent": AGENTE}
    cab.update(cabeceras or {})
    cuerpo = json.dumps(datos).encode("utf-8") if datos is not None else None
    if cuerpo is not None:
        cab.setdefault("Content-Type", "application/json")
    ultimo = None
    for i in range(intentos):
        req = urllib.request.Request(url, data=cuerpo, headers=cab)
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            ultimo = e
            if e.code == 429 or e.code >= 500:
                time.sleep(espera * (i + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            ultimo = e
            time.sleep(espera * (i + 1))
    raise ultimo


def pedir_json(url, cabeceras=None, datos=None):
    return json.loads(pedir(url, cabeceras, datos).decode("utf-8"))


def descargar(url, ruta):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(pedir(url))
    return ruta


# ---------------------------------------------------------------------------
# Las tres fuentes. Cada una devuelve un dict con el plano ya descargado, o None.
# ---------------------------------------------------------------------------
def elegir_fichero_pexels(ficheros):
    """El fichero de vídeo vertical más pequeño que llegue a 1920 de alto, o si
    no hay ninguno, el más alto que haya. Solo mp4."""
    verticales = [f for f in ficheros
                  if (f.get("file_type") or "").endswith("mp4")
                  and (f.get("height") or 0) > (f.get("width") or 0)]
    if not verticales:
        return None
    buenos = sorted((f for f in verticales if (f.get("height") or 0) >= 1920),
                    key=lambda f: f["height"])
    return buenos[0] if buenos else max(verticales, key=lambda f: f.get("height") or 0)


def pexels(consulta, dur_min, destino, usados):
    clave = os.environ.get("PEXELS_API_KEY")
    if not clave:
        print("  · Pexels: sin PEXELS_API_KEY, me la salto")
        return None
    url = ("https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": consulta, "orientation": "portrait", "size": "medium", "per_page": 15}))
    datos = pedir_json(url, {"Authorization": clave})
    videos = [v for v in datos.get("videos", []) if ("pexels", v.get("id")) not in usados]
    if not videos:
        return None
    largos = [v for v in videos if (v.get("duration") or 0) >= dur_min]
    v = (largos or sorted(videos, key=lambda v: -(v.get("duration") or 0)))[0]
    f = elegir_fichero_pexels(v.get("video_files", []))
    if not f:
        return None
    ruta = descargar(f["link"], destino.with_suffix(".mp4"))
    return {"fuente": "pexels", "id": v["id"], "pagina": v.get("url"),
            "autor": (v.get("user") or {}).get("name"),
            "autor_url": (v.get("user") or {}).get("url"),
            "licencia": LICENCIA_PEXELS, "fichero": str(ruta.relative_to(SALIDA)),
            "ancho": f.get("width"), "alto": f.get("height"),
            "duracion_s": v.get("duration"), "consulta": consulta, "tipo": "video"}


def pixabay(consulta, dur_min, destino, usados):
    clave = os.environ.get("PIXABAY_API_KEY")
    if not clave:
        print("  · Pixabay: sin PIXABAY_API_KEY, me la salto")
        return None
    url = ("https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
        {"key": clave, "q": consulta, "per_page": 20, "safesearch": "true"}))
    datos = pedir_json(url)
    hits = [h for h in datos.get("hits", []) if ("pixabay", h.get("id")) not in usados]
    if not hits:
        return None
    largos = [h for h in hits if (h.get("duration") or 0) >= dur_min]
    h = (largos or sorted(hits, key=lambda h: -(h.get("duration") or 0)))[0]
    tamanos = h.get("videos") or {}
    f = next((tamanos[k] for k in ("large", "medium", "small")
              if (tamanos.get(k) or {}).get("url")), None)
    if not f:
        return None
    ruta = descargar(f["url"], destino.with_suffix(".mp4"))
    usuario = h.get("user") or ""
    return {"fuente": "pixabay", "id": h["id"], "pagina": h.get("pageURL"),
            "autor": usuario,
            "autor_url": f"https://pixabay.com/users/{usuario}-{h.get('user_id')}/",
            "licencia": LICENCIA_PIXABAY, "fichero": str(ruta.relative_to(SALIDA)),
            "ancho": f.get("width"), "alto": f.get("height"),
            "duracion_s": h.get("duration"), "consulta": consulta, "tipo": "video"}


def generada(prompt, semilla, destino):
    cuenta = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    if not (cuenta and token):
        print("  · Cloudflare: sin CLOUDFLARE_ACCOUNT_ID o CLOUDFLARE_API_TOKEN, me la salto")
        return None
    url = f"https://api.cloudflare.com/client/v4/accounts/{cuenta}/ai/run/{MODELO_IA}"
    datos = pedir_json(url, {"Authorization": f"Bearer {token}"},
                       {"prompt": prompt, "steps": 4, "seed": semilla})
    if not datos.get("success", True) or not (datos.get("result") or {}).get("image"):
        print(f"  · Cloudflare: respuesta sin imagen: {str(datos)[:300]}")
        return None
    crudo = base64.b64decode(datos["result"]["image"])
    ext = ".png" if crudo[:8] == b"\x89PNG\r\n\x1a\n" else ".jpg"
    ruta = destino.with_suffix(ext)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(crudo)
    ancho = alto = None
    try:
        from PIL import Image
        with Image.open(ruta) as im:
            ancho, alto = im.size
    except Exception:
        pass
    return {"fuente": "ia", "modelo": MODELO_IA, "prompt": prompt, "semilla": semilla,
            "licencia": LICENCIA_IA, "fichero": str(ruta.relative_to(SALIDA)),
            "ancho": ancho, "alto": alto, "tipo": "imagen"}


# ---------------------------------------------------------------------------
# Resolver un guion entero
# ---------------------------------------------------------------------------
def duracion_escena(e):
    # Misma estimación que validar_guion.py (130 palabras por minuto).
    n = len((e.get("narracion") or "").split())
    return max(2.6, n / 130 * 60 + 0.5) + float(e.get("pausa_despues_s") or 0.45)


def resolver(ident, specs, solo_ia=False):
    guion = json.loads((GUIONES / f"{ident}.es.json").read_text(encoding="utf-8"))
    variante = "C" if solo_ia else "A"
    carpeta = SALIDA / ident / variante
    carpeta.mkdir(parents=True, exist_ok=True)
    usados, manifiesto = set(), []
    print(f"\n{ident} · variante {variante}")
    for n, esc in enumerate(guion["escenas"], 1):
        planos = specs.get(str(n)) or []
        dur = duracion_escena(esc)
        # los planos de una escena se reparten su duración a partes iguales
        dur_plano = dur / max(1, len(planos))
        for k, plano in enumerate(planos, 1):
            destino = carpeta / f"e{n}_p{k}"
            semilla = int(plano.get("semilla") or (1000 + 10 * n + k))
            orden = ["ia"] if solo_ia else plano.get("orden", ["pexels", "pixabay", "ia"])
            hecho = None
            for fuente in orden:
                try:
                    if fuente == "pexels" and plano.get("busqueda"):
                        hecho = pexels(plano["busqueda"], dur_plano, destino, usados)
                    elif fuente == "pixabay" and plano.get("busqueda"):
                        hecho = pixabay(plano["busqueda"], dur_plano, destino, usados)
                    elif fuente == "ia" and plano.get("prompt"):
                        hecho = generada(plano["prompt"], semilla, destino)
                except Exception as ex:  # una fuente que falla no tumba la prueba
                    print(f"  · escena {n} plano {k}: {fuente} falló: {ex}")
                    hecho = None
                if hecho:
                    break
            if not hecho:
                hecho = {"fuente": "sin_imagen", "tipo": "ninguno"}
            elif hecho.get("id") is not None:
                usados.add((hecho["fuente"], hecho["id"]))
            hecho.update({"escena": n, "plano": k, "duracion_plano_s": round(dur_plano, 2),
                          "frase": esc.get("narracion", "")})
            manifiesto.append(hecho)
            print(f"  escena {n} plano {k}: {hecho['fuente']} "
                  f"{hecho.get('id') or hecho.get('fichero') or ''}")
    (carpeta / "manifiesto.json").write_text(
        json.dumps({"guion": ident, "variante": variante, "planos": manifiesto},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sin = sum(1 for m in manifiesto if m["fuente"] == "sin_imagen")
    print(f"  → {len(manifiesto)} planos, {sin} sin imagen · {carpeta / 'manifiesto.json'}")
    return manifiesto


def main():
    global SALIDA
    ap = argparse.ArgumentParser(description="C50 · resolver imágenes (prueba)")
    ap.add_argument("guiones", nargs="+")
    ap.add_argument("--especificacion", default=str(RAIZ / "07_pruebas" / "visual-23-09" / "visuales.json"))
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--solo-ia", action="store_true",
                    help="variante C: todos los planos, imagen generada")
    a = ap.parse_args()
    SALIDA = Path(a.salida).resolve()
    specs = json.loads(Path(a.especificacion).read_text(encoding="utf-8"))
    for ident in a.guiones:
        if ident not in specs:
            print(f"{ident}: no hay especificación en visuales.json, me lo salto")
            continue
        resolver(ident, specs[ident], a.solo_ia)


if __name__ == "__main__":
    sys.exit(main())
