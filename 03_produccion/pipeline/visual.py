#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_produccion/pipeline/visual.py — C50 · de dónde sale la imagen de cada plano.
Versión 13 del plan (23/09/2026): entra en producción.

Tres órdenes:

  resolver     Lee el campo «visual» de los guiones que aún no se han
               publicado, busca en Pexels y en Pixabay, genera con Cloudflare
               Workers AI lo que el archivo no tiene, elige y deja en
               05_calendario/visuales/:
                 <ID>.json  el manifiesto: qué plano va en cada escena, de
                            dónde sale, su autor, su enlace y su licencia
                            (regla 9), y dónde va el texto para no tapar caras;
                 <ID>.jpg   la hoja de contactos, que mira la revisión diaria;
                 <ID>/      las imágenes generadas (no se pueden volver a
                            descargar, así que se guardan).
               La lanza el workflow «Visuales (C50)». Necesita red y las
               claves PEXELS_API_KEY, PIXABAY_API_KEY, CLOUDFLARE_ACCOUNT_ID y
               CLOUDFLARE_API_TOKEN (la que falte, esa fuente se salta).

  traer        En producir.yml, ANTES del render: baja los planos del
               manifiesto a build/<ID>/visual/ y deja visual/local.json, que es
               lo único que lee render.py (el render no usa la red, regla
               11.6). No necesita claves: los enlaces del archivo son
               públicos. NUNCA falla la producción: lo que no baja sale como
               tarjeta de marca, y sin manifiesto el Short sale como siempre.

  diagnostico  Prueba las tres claves y deja lo que contesta cada servicio en
               05_calendario/visuales/diagnostico.json (y en el resumen del
               workflow). Existe porque el 23/09 la variante C de la prueba no
               sacó ni una imagen y nadie pudo saber por qué: el error se
               tragaba.

Lo que se pidió al ver la prueba del 23/09 (07_pruebas/visual-23-09.md) y
dónde está:
  · planos que no pegan con la frase → puntuación de relevancia contra el
    título del clip (`relevancia`), varias búsquedas por plano, y la hoja de
    contactos con la frase exacta que suena durante cada plano;
  · planos quietos (el sillón de MDS-025) → se mide el movimiento de cada
    candidato y se descarta el que no se mueve (`MOV_MIN`);
  · el título encima de una cara → OpenCV busca caras en cada plano y el
    texto se va a la banda donde no las hay (`texto_pos`), y el encuadre se
    centra en ellas;
  · nada de repetir un clip ya usado en otro Short.

Uso:
    python3 visual.py resolver                    # todo lo pendiente
    python3 visual.py resolver MDS-024 --forzar   # uno, aunque no haya cambiado
    python3 visual.py traer build/MDS-024.es/guion.timed.json
    python3 visual.py diagnostico
"""
import argparse
import base64
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(AQUI))
import fondo_visual  # noqa: E402

GUIONES = RAIZ / "05_calendario" / "guiones"
VISUALES = RAIZ / "05_calendario" / "visuales"
REGISTRO = RAIZ / "05_calendario" / "registro_publicaciones.json"
AJUSTES = VISUALES / "ajustes.json"
APAGADO = VISUALES / "APAGADO"
CACHE = RAIZ / "03_produccion" / "cache_visual"     # en .gitignore: solo copias ligeras para analizar

VERSION = 1           # subirla obliga a volver a resolver todo lo pendiente
AGENTE = "MecanicaDelHumor-C50/1.0 (+https://github.com/mecanicadelhumor/mecanica-del-humor)"
FPS = 30
PALABRAS_MIN = 130    # la misma estimación de ritmo que validar_guion.py

MOV_MIN = 0.5         # por debajo, el plano se ve quieto (medido sobre 96x96 a 5 fps; ver movimiento())
RELEVANCIA_MIN = 0.34 # al menos un tercio de las palabras de la búsqueda en el título del clip
RELEVANCIA_FLOJA = 0.2  # por debajo, el clip no tiene nada que ver: antes la tarjeta de marca
CANDIDATOS_A_MIRAR = 4
DIAS_DE_HOJAS = 14    # las hojas y las imágenes generadas de lo ya publicado se borran pasado esto
TRAER_MAX_S = 480     # lo más que puede tardar `traer` en producción, con la red como esté

LICENCIA_PEXELS = "Licencia de Pexels (uso gratuito, también comercial; https://www.pexels.com/license/)"
LICENCIA_PIXABAY = ("Licencia de contenido de Pixabay (uso gratuito, también comercial; "
                    "https://pixabay.com/service/license-summary/)")
MODELO_IA = "@cf/black-forest-labs/flux-2-klein-4b"      # admite ancho y alto (256-1920): sale vertical
MODELO_IA_RESPALDO = "@cf/black-forest-labs/flux-1-schnell"  # solo cuadrado: se recorta
LICENCIA_IA = ("Imagen generada con IA ({modelo}, Black Forest Labs) en Cloudflare Workers AI. "
               "Se declara en la descripción y como contenido sintético.")
ESTILO_IA = (", vertical 9:16 photo, realistic, natural light, candid, "
             "no text, no captions, no watermark, no logos")
ANCHO_IA, ALTO_IA = 768, 1360   # múltiplos de 16; ~104-156 neuronas por imagen (de 10.000 al día)

# Bandas donde va el texto en modo archivo, en fracción del alto (escena.html).
BANDAS = {"abajo": (960 / 1920, 1490 / 1920), "arriba": (250 / 1920, 920 / 1920)}
RELACION = 1080 / 1920


# ---------------------------------------------------------------------------
# Red
# ---------------------------------------------------------------------------
class ErrorHTTP(Exception):
    def __init__(self, url, codigo, cuerpo):
        self.url, self.codigo, self.cuerpo = url, codigo, cuerpo or ""
        super().__init__(f"HTTP {codigo} en {urllib.parse.urlparse(url).netloc}: "
                         f"{self.cuerpo.strip()[:400]}")


class ErrorIA(RuntimeError):
    """Ningún modelo de imagen ha dado imagen. `pasajero` dice si merece la
    pena volver a intentarlo más tarde (cuota, 5xx, red) o no (clave, permiso)."""
    def __init__(self, mensaje, pasajero):
        super().__init__(mensaje)
        self.pasajero = pasajero


def pasajero(ex):
    """¿Es un fallo que se arregla solo esperando? 429, 5xx y cortes de red sí;
    una clave mala, un permiso o un 404, no. Solo los primeros hacen que un
    manifiesto quede «incompleto» y se rehaga en la siguiente pasada: si no, un
    error permanente lo rehace todos los días y cambia planos ya revisados."""
    if isinstance(ex, ErrorHTTP):
        return ex.codigo == 429 or ex.codigo >= 500
    if isinstance(ex, ErrorIA):
        return ex.pasajero
    return isinstance(ex, (urllib.error.URLError, TimeoutError, ConnectionError, OSError))


def pedir(url, cabeceras=None, cuerpo=None, tipo=None, intentos=3, espera=4, timeout=120):
    """GET (o POST si hay `cuerpo`) que devuelve bytes. Reintenta los 429, los
    5xx y los cortes de red; un 4xx distinto es definitivo y se devuelve CON
    su cuerpo, que es donde el servicio dice qué le pasa."""
    cab = {"User-Agent": AGENTE}
    cab.update(cabeceras or {})
    if tipo:
        cab["Content-Type"] = tipo
    ultimo = None
    for i in range(intentos):
        req = urllib.request.Request(url, data=cuerpo, headers=cab)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            try:
                texto = e.read().decode("utf-8", "replace")
            except Exception:
                texto = ""
            ultimo = ErrorHTTP(url, e.code, texto)
            if e.code == 429 or e.code >= 500:
                time.sleep(espera * (i + 1))
                continue
            raise ultimo
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            ultimo = e
            time.sleep(espera * (i + 1))
    raise ultimo


def pedir_json(url, cabeceras=None, datos=None):
    cuerpo = json.dumps(datos).encode("utf-8") if datos is not None else None
    return json.loads(pedir(url, cabeceras, cuerpo, "application/json" if cuerpo else None))


def descargar(url, ruta, intentos=3, timeout=300):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    tmp = ruta.with_suffix(ruta.suffix + ".part")
    tmp.write_bytes(pedir(url, intentos=intentos, timeout=timeout))
    tmp.replace(ruta)
    return ruta


def _multipart(campos):
    limite = "mdh" + hashlib.sha1(json.dumps(campos, sort_keys=True).encode()).hexdigest()[:20]
    partes = [f"--{limite}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n"
              for k, v in campos.items()]
    partes.append(f"--{limite}--\r\n")
    return "".join(partes).encode("utf-8"), f"multipart/form-data; boundary={limite}"


# ---------------------------------------------------------------------------
# Relevancia: cuántas palabras de la búsqueda están en el título del clip
# ---------------------------------------------------------------------------
_VACIAS = set("""a an the of on in at with and or to for from by is are his her their its into
over under near while one two some very as up down out off this that these those who
someone something person's""".split())
_SINONIMOS = {"women": "woman", "men": "man", "people": "person", "persons": "person",
              "guy": "man", "lady": "woman", "kids": "child", "kid": "child", "children": "child",
              "elderly": "old", "senior": "old", "seniors": "old", "aged": "old", "older": "old",
              "grandmother": "old", "grandfather": "old", "retiree": "old", "retired": "old",
              "phone": "phone", "smartphone": "phone", "cellphone": "phone", "mobile": "phone",
              "laughter": "laugh", "laughs": "laugh", "smiles": "smile", "smiling": "smile"}


def _raiz(palabra):
    w = _SINONIMOS.get(palabra, palabra)
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    return w[:4]


def _palabras(texto):
    return [w for w in re.findall(r"[a-z]+", (texto or "").lower())
            if w not in _VACIAS and len(w) > 1]


def relevancia(consulta, titulo):
    q = {_raiz(w) for w in _palabras(consulta)}
    if not q:
        return 0.0
    t = {_raiz(w) for w in _palabras(titulo)}
    return round(len(q & t) / len(q), 3)


# ---------------------------------------------------------------------------
# Las fuentes. Cada búsqueda devuelve candidatos homogéneos, sin descargar.
# ---------------------------------------------------------------------------
_CACHE_BUSQUEDAS = {}


def _slug(url):
    ultimo = [p for p in urllib.parse.urlparse(url or "").path.split("/") if p]
    s = ultimo[-1] if ultimo else ""
    s = re.sub(r"-?\d+$", "", s)
    return s.replace("-", " ")


def _pexels_candidato(v):
    ficheros = [f for f in v.get("video_files", []) if (f.get("file_type") or "").endswith("mp4")
                and f.get("link") and f.get("width") and f.get("height")]
    if not ficheros:
        return None
    vertical = [f for f in ficheros if f["height"] > f["width"]]
    grupo = vertical or ficheros
    # Para el render: el más pequeño que llegue a 1920 de alto (o a 1080 de
    # ancho si es horizontal); si no hay, el mayor.
    # Un horizontal se recorta a 9:16 y se amplía: para que no quede blando,
    # también se le pide que llegue a 1920 de alto (en la práctica, el 4K).
    buenos = sorted((f for f in grupo if f["height"] >= 1920), key=lambda f: f["width"] * f["height"])
    hd = buenos[0] if buenos else max(grupo, key=lambda f: f["width"] * f["height"])
    # Para analizar: el más pequeño que tenga al menos 360 px en el lado corto.
    ligeros = sorted((f for f in ficheros if min(f["width"], f["height"]) >= 360),
                     key=lambda f: f["width"] * f["height"])
    ligero = ligeros[0] if ligeros else hd
    usuario = v.get("user") or {}
    return {"fuente": "pexels", "id": v["id"], "pagina": v.get("url"), "titulo": _slug(v.get("url")),
            "autor": usuario.get("name"), "autor_url": usuario.get("url"),
            "licencia": LICENCIA_PEXELS, "duracion_s": float(v.get("duration") or 0),
            "ancho": hd["width"], "alto": hd["height"], "url": hd["link"], "url_ligero": ligero["link"],
            "tipo": "video"}


def buscar_pexels(consulta):
    clave = os.environ.get("PEXELS_API_KEY")
    if not clave:
        return []
    k = ("pexels", consulta)
    if k not in _CACHE_BUSQUEDAS:
        url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
            {"query": consulta, "orientation": "portrait", "size": "medium", "per_page": 20})
        datos = pedir_json(url, {"Authorization": clave})
        _CACHE_BUSQUEDAS[k] = [c for c in (_pexels_candidato(v) for v in datos.get("videos", [])) if c]
    return [dict(c) for c in _CACHE_BUSQUEDAS[k]]


def _pixabay_candidato(h):
    tam = h.get("videos") or {}
    hd = next((tam[k] for k in ("large", "medium", "small") if (tam.get(k) or {}).get("url")), None)
    ligero = next((tam[k] for k in ("tiny", "small", "medium") if (tam.get(k) or {}).get("url")), hd)
    if not hd:
        return None
    usuario = h.get("user") or ""
    return {"fuente": "pixabay", "id": h["id"], "pagina": h.get("pageURL"),
            "titulo": f"{h.get('tags', '')} {_slug(h.get('pageURL'))}",
            "autor": usuario, "autor_url": f"https://pixabay.com/users/{usuario}-{h.get('user_id')}/",
            "licencia": LICENCIA_PIXABAY, "duracion_s": float(h.get("duration") or 0),
            "ancho": hd.get("width"), "alto": hd.get("height"), "url": hd["url"],
            "url_ligero": ligero["url"], "tipo": "video"}


def buscar_pixabay(consulta):
    clave = os.environ.get("PIXABAY_API_KEY")
    if not clave:
        return []
    k = ("pixabay", consulta)
    if k not in _CACHE_BUSQUEDAS:
        url = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
            {"key": clave, "q": consulta[:100], "per_page": 20, "safesearch": "true"})
        datos = pedir_json(url)
        _CACHE_BUSQUEDAS[k] = [c for c in (_pixabay_candidato(h) for h in datos.get("hits", [])) if c]
    return [dict(c) for c in _CACHE_BUSQUEDAS[k]]


def clip_fijado(ref):
    """«pexels:123» o «pixabay:456»: ese clip y ningún otro."""
    fuente, _, ident = (ref or "").partition(":")
    if fuente == "pexels" and os.environ.get("PEXELS_API_KEY"):
        v = pedir_json(f"https://api.pexels.com/videos/videos/{int(ident)}",
                       {"Authorization": os.environ["PEXELS_API_KEY"]})
        return _pexels_candidato(v)
    if fuente == "pixabay" and os.environ.get("PIXABAY_API_KEY"):
        datos = pedir_json("https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
            {"key": os.environ["PIXABAY_API_KEY"], "id": int(ident)}))
        hits = datos.get("hits") or []
        return _pixabay_candidato(hits[0]) if hits else None
    return None


def generar(prompt, semilla, destino, ancho=ANCHO_IA, alto=ALTO_IA):
    """Imagen generada con Cloudflare Workers AI. Primero FLUX.2 [klein] 4B en
    vertical; si ese falla, FLUX.1 [schnell] (cuadrada, se recorta). Lanza
    RuntimeError con TODO lo que contestó el servicio si ninguno sale."""
    cuenta = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    if not (cuenta and token):
        raise ErrorIA("faltan CLOUDFLARE_ACCOUNT_ID o CLOUDFLARE_API_TOKEN", False)
    texto = (prompt.strip().rstrip(".") + ESTILO_IA)[:2000]
    cab = {"Authorization": f"Bearer {token}"}
    errores, alguno_pasajero = [], False
    for modelo in (MODELO_IA, MODELO_IA_RESPALDO):
        url = f"https://api.cloudflare.com/client/v4/accounts/{cuenta}/ai/run/{modelo}"
        try:
            if modelo == MODELO_IA:
                cuerpo, tipo = _multipart({"prompt": texto, "width": ancho, "height": alto,
                                           "seed": semilla})
                datos = json.loads(pedir(url, cab, cuerpo, tipo, timeout=180))
            else:
                datos = pedir_json(url, cab, {"prompt": texto, "steps": 4, "seed": semilla})
        except Exception as ex:          # cualquier fallo de un modelo: se prueba el otro
            errores.append(f"{modelo}: {type(ex).__name__}: {ex}")
            alguno_pasajero = alguno_pasajero or pasajero(ex)
            continue
        imagen = (datos.get("result") or {}).get("image") if isinstance(datos, dict) else None
        if not imagen:
            errores.append(f"{modelo}: respuesta sin imagen: {json.dumps(datos)[:400]}")
            continue
        from PIL import Image
        try:
            im = Image.open(io.BytesIO(base64.b64decode(imagen))).convert("RGB")
        except Exception as ex:
            errores.append(f"{modelo}: imagen ilegible: {ex}")
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        im.save(destino, "JPEG", quality=88)
        return {"fuente": "ia", "modelo": modelo, "prompt": prompt, "semilla": semilla,
                "licencia": LICENCIA_IA.format(modelo=modelo.split("/")[-1]),
                "ancho": im.width, "alto": im.height, "tipo": "imagen",
                "fichero": str(destino.relative_to(RAIZ)).replace("\\", "/")}
    raise ErrorIA(" | ".join(errores) or "sin respuesta", alguno_pasajero)


# ---------------------------------------------------------------------------
# Mirar un candidato: movimiento, caras y un fotograma para la hoja
# ---------------------------------------------------------------------------
def _ffmpeg_bytes(*args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", *args],
                       capture_output=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[-400:])
    return r.stdout


def movimiento(fichero, inicio, ventana):
    """Media de la diferencia absoluta entre fotogramas consecutivos (5 por
    segundo, en gris y a 96x96). Un plano de trípode sin nada que se mueva da
    0-0,3; un paneo lento sobre una escena lisa, ~0,9 (medido el 23/09 con
    clips sintéticos); alguien gesticulando o una cámara en mano, bastante
    más. El sillón de MDS-025 (prueba del 23/09) es lo que se quiere cazar,
    sin tirar los paneos lentos. El umbral es una primera estimación: cada
    manifiesto guarda el movimiento de lo elegido y de lo descartado, y con
    una semana de datos reales se ajusta."""
    import numpy as np
    crudo = _ffmpeg_bytes("-ss", f"{inicio:.2f}", "-t", f"{max(1.0, ventana):.2f}", "-i", str(fichero),
                          "-vf", "fps=5,scale=96:96,format=gray", "-f", "rawvideo", "-")
    fot = np.frombuffer(crudo, dtype=np.uint8)
    n = fot.size // (96 * 96)
    if n < 2:
        return 0.0
    fot = fot[: n * 96 * 96].reshape(n, 96, 96).astype(np.float32)
    return round(float(np.abs(np.diff(fot, axis=0)).mean()), 2)


def fotograma(fichero, instante, destino):
    _ffmpeg_bytes("-ss", f"{instante:.2f}", "-i", str(fichero), "-frames:v", "1", "-y", str(destino))
    return destino


_DETECTORES = None


def caras(ruta_imagen):
    """Caras en una imagen, como [x, y, ancho, alto] en fracción del cuadro.
    Haar de OpenCV, frontal y de perfil: es rápido, no necesita red ni
    modelos descargados, y aquí basta con saber DÓNDE hay una cara.

    Cualquier fallo de OpenCV se trata como «no hay caras», nunca como motivo
    para tirar el candidato. Antes solo se perdonaba `ImportError`, y el
    23/09/2026 `requirements.txt` no traía OpenCV: `cv2` se importaba desde
    otra cosa del entorno sin los bindings reales, así que cada candidato de
    cada plano de MDS-024 y MDS-025 moría con «no se pudo mirar:
    module 'cv2' has no attribute 'CascadeClassifier'» en `mirar()` (más
    abajo), y los dos Shorts siguientes se resolvieron enteros en tarjeta de
    marca el primer día de C50. Añadido `opencv-python-headless` a
    `requirements.txt`, y esta función ya no deja que un fallo de detección
    de caras cueste el plano entero: sin caras que perder, se sigue sin
    ellas."""
    global _DETECTORES
    try:
        import cv2
        if _DETECTORES is None:
            _DETECTORES = [cv2.CascadeClassifier(cv2.data.haarcascades + n)
                           for n in ("haarcascade_frontalface_default.xml", "haarcascade_profileface.xml")]
        img = cv2.imread(str(ruta_imagen))
        if img is None:
            return []
        alto, ancho = img.shape[:2]
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lado = max(20, min(ancho, alto) // 14)
        halladas = []
        # En gris tal cual y con el histograma ecualizado: cada versión encuentra
        # caras que la otra pierde (la ecualizada falla sobre fondos lisos y
        # oscuros; la otra, en contraluz). Se juntan y se quitan los duplicados.
        for imagen in (gris, cv2.equalizeHist(gris)):
            for det in _DETECTORES:
                for (x, y, w, h) in det.detectMultiScale(imagen, scaleFactor=1.1, minNeighbors=6,
                                                          minSize=(lado, lado)):
                    halladas.append((int(x), int(y), int(w), int(h)))
    except Exception:
        return []
    unicas = []
    for c in sorted(halladas, key=lambda c: -c[2] * c[3]):
        x, y, w, h = c
        if any(min(x + w, u[0] + u[2]) - max(x, u[0]) > 0.4 * min(w, u[2])
               and min(y + h, u[1] + u[3]) - max(y, u[1]) > 0.4 * min(h, u[3]) for u in unicas):
            continue
        unicas.append(c)
    return [[round(x / ancho, 4), round(y / alto, 4), round(w / ancho, 4), round(h / alto, 4)]
            for x, y, w, h in unicas]


def encuadre(ancho, alto, caras_):
    """Dónde cortar un plano que no es 9:16 para que las caras queden dentro.
    Devuelve {"x", "y"} en [0, 1] tal como lo usa fondo_visual (0,5 = centro)."""
    if not (ancho and alto):
        return {"x": 0.5, "y": 0.5}
    a = ancho / alto
    x = y = 0.5
    if caras_:
        peso = sum(w * h for _, _, w, h in caras_) or 1.0
        cx = sum((fx + w / 2) * w * h for fx, _, w, h in caras_) / peso
        cy = sum((fy + h / 2) * w * h for _, fy, w, h in caras_) / peso
        if a > RELACION + 0.01:                 # más ancho: se recorta a los lados
            visible = RELACION / a
            x = (cx - visible / 2) / max(1e-6, 1 - visible)
        elif a < RELACION - 0.01:               # más alto: se recorta arriba y abajo
            visible = a / RELACION
            y = (cy - visible * 0.42) / max(1e-6, 1 - visible)
    return {"x": round(min(1, max(0, x)), 3), "y": round(min(1, max(0, y)), 3)}


def caras_en_cuadro(ancho, alto, caras_, enc):
    """Las caras pasadas a coordenadas del cuadro final 1080x1920."""
    if not (ancho and alto):
        return []
    a = ancho / alto
    vx, vy, ox, oy = 1.0, 1.0, 0.0, 0.0
    if a > RELACION + 0.01:
        vx = RELACION / a
        ox = (1 - vx) * enc.get("x", 0.5)
    elif a < RELACION - 0.01:
        vy = a / RELACION
        oy = (1 - vy) * enc.get("y", 0.5)
    salida = []
    for fx, fy, w, h in caras_:
        x0, y0 = (fx - ox) / vx, (fy - oy) / vy
        salida.append([round(x0, 4), round(y0, 4), round(w / vx, 4), round(h / vy, 4)])
    return [c for c in salida if c[0] + c[2] > 0 and c[0] < 1 and c[1] + c[3] > 0 and c[1] < 1]


def mirar(cand, necesita_s, tmp):
    """Baja la copia ligera de un candidato y mide lo que hace falta para
    decidir. Devuelve el candidato con movimiento, caras, encuadre, inicio_s
    y la ruta de un fotograma para la hoja de contactos."""
    CACHE.mkdir(parents=True, exist_ok=True)
    ligero = CACHE / f"{cand['fuente']}_{cand['id']}_ligero.mp4"
    if not ligero.exists():
        descargar(cand["url_ligero"], ligero)
    dur = cand.get("duracion_s") or 0.0
    inicio = 0.4 if dur >= necesita_s + 0.8 else 0.0
    ventana = min(max(necesita_s, 1.5), 4.0, max(1.0, dur - inicio) if dur else 4.0)
    cand["inicio_s"] = inicio
    cand["movimiento"] = movimiento(ligero, inicio, ventana)
    todas = []
    for j, f in enumerate((0.2, 0.5, 0.85)):
        ruta = tmp / f"{cand['fuente']}_{cand['id']}_{j}.png"
        try:
            fotograma(ligero, inicio + f * ventana, ruta)
        except RuntimeError:
            continue
        todas += caras(ruta)
        if j == 1:
            cand["_fotograma"] = str(ruta)
    unicas = []
    for c in sorted(todas, key=lambda c: -c[2] * c[3]):
        if any(min(c[0] + c[2], u[0] + u[2]) - max(c[0], u[0]) > 0.4 * min(c[2], u[2])
               and min(c[1] + c[3], u[1] + u[3]) - max(c[1], u[1]) > 0.4 * min(c[3], u[3])
               for u in unicas):
            continue
        unicas.append(c)
    todas = unicas
    cand["caras_origen"] = todas
    cand["encuadre"] = encuadre(cand.get("ancho"), cand.get("alto"), todas)
    cand["caras"] = caras_en_cuadro(cand.get("ancho"), cand.get("alto"), todas, cand["encuadre"])
    return cand


# ---------------------------------------------------------------------------
# Especificación: el campo «visual» del guion, más los ajustes de la revisión
# ---------------------------------------------------------------------------
def _sha(texto):
    return hashlib.sha1((texto or "").encode("utf-8")).hexdigest()[:12]


def ajustes_de(ident):
    if not AJUSTES.exists():
        return {}
    try:
        datos = json.loads(AJUSTES.read_text(encoding="utf-8")).get(ident, {}) or {}
        return datos if isinstance(datos, dict) else {}
    except Exception as ex:
        print(f"::warning::{AJUSTES.name} no se puede leer ({ex}); se ignora")
        return {}


def especificacion(guion, ajustes):
    """Por escena: lista de planos normalizada. «marca» como escena entera se
    convierte en un plano de marca."""
    salida = {}
    for n, e in enumerate(guion["escenas"], 1):
        v = e.get("visual")
        if not v:
            continue
        if v == "marca":
            planos = [{"marca": True}]
        elif isinstance(v, dict):
            planos = [v]
        else:
            planos = [dict(p) for p in v if isinstance(p, dict)]
        for k, p in enumerate(planos, 1):
            if p.get("desde") is not None and not isinstance(p.get("desde"), str):
                p["desde"] = str(p["desde"])
            aj = ajustes.get(f"{n}.{k}") or {}
            if not isinstance(aj, dict):
                aj = {}
            if aj.get("excluir"):
                previo = p.get("excluir") or []
                nuevo = aj["excluir"]
                p["excluir"] = ([previo] if isinstance(previo, str) else list(previo)) + \
                               ([nuevo] if isinstance(nuevo, str) else list(nuevo))
            for campo in ("fijar", "busqueda", "prompt", "fuente", "marca", "desde"):
                if campo in aj:
                    p[campo] = aj[campo]
        aj_escena = ajustes.get(str(n)) if isinstance(ajustes.get(str(n)), dict) else {}
        pos = aj_escena.get("texto_pos") or e.get("texto_pos")
        if pos not in ("abajo", "arriba"):
            pos = None
        salida[n] = {"planos": planos, "texto_pos": pos}
    return salida


def firma(guion, espec):
    base = {"v": VERSION,
            "escenas": [{k: e.get(k) for k in ("tipo", "narracion", "texto", "cifra", "titulo",
                                                "a", "b", "pausa_despues_s")}
                        for e in guion["escenas"]],
            "espec": {str(n): s for n, s in espec.items()}}
    return hashlib.sha1(json.dumps(base, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def duracion_estimada(e):
    n = len((e.get("narracion") or "").split())
    pausa = e.get("pausa_despues_s")
    return max(2.6, n / PALABRAS_MIN * 60 + 0.5) + (0.45 if pausa is None else float(pausa))


def usados_en_otros(ident):
    """Clips ya usados en cualquier otro Short: no se repiten."""
    vistos = set()
    for m in VISUALES.glob("MD?-*.json"):
        if m.stem == ident:
            continue
        try:
            datos = json.loads(m.read_text(encoding="utf-8"))
        except Exception:
            continue
        for esc in (datos.get("escenas") or {}).values():
            for p in esc.get("planos", []):
                if p.get("id") is not None:
                    vistos.add(f"{p.get('fuente')}:{p.get('id')}")
    return vistos


def publicados():
    """Episodios ya subidos (con video_id en el registro): no se resuelven."""
    if not REGISTRO.exists():
        return set()
    try:
        datos = json.loads(REGISTRO.read_text(encoding="utf-8"))
    except Exception:
        return set()
    return {p.get("episodio") for p in datos.get("publicaciones", []) if p.get("video_id")}


# ---------------------------------------------------------------------------
# Resolver un guion
# ---------------------------------------------------------------------------
def _elegir_archivo(plano, necesita_s, prohibidos, tmp, descartes, n, k, fallos_api):
    """El mejor clip de archivo para un plano, o None.

    Las búsquedas se prueban EN ORDEN y solo se pasa a la siguiente si la
    anterior no ha dado un clip relevante y con movimiento: Pexels da 200
    peticiones por hora, y una semana entera de golpe (cinco Shorts, sesenta
    planos) no puede gastarlas en búsquedas de repuesto que no hacían falta.
    Si ninguna da un clip relevante, se devuelve el mejor de los flojos (y el
    que llama decide si antes prueba la imagen generada)."""
    consultas = plano.get("busqueda") or []
    if not isinstance(consultas, list):
        consultas = [consultas]
    consultas = [str(q).strip() for q in consultas if str(q).strip()]
    if plano.get("fijar"):
        try:
            c = clip_fijado(plano["fijar"])
        except Exception as ex:
            descartes.append({"escena": n, "plano": k, "id": plano["fijar"], "motivo": f"fijado: {ex}"})
            if pasajero(ex):
                fallos_api.append(str(ex))
            c = None
        if c:
            c["relevancia"] = 1.0
            c["consulta"] = f"fijado {plano['fijar']}"
            try:
                return mirar(c, necesita_s, tmp)
            except Exception as ex:
                descartes.append({"escena": n, "plano": k, "id": plano["fijar"],
                                  "motivo": f"fijado, no se pudo mirar: {ex}"})
    vistos, mejor_flojo = set(), None
    for orden_q, q in enumerate(consultas):
        candidatos = []
        for buscar in (buscar_pexels, buscar_pixabay):
            try:
                lista = buscar(q)
            except Exception as ex:
                if pasajero(ex):
                    fallos_api.append(str(ex))
                descartes.append({"escena": n, "plano": k, "consulta": q,
                                  "motivo": f"{buscar.__name__}: {ex}"[:500]})
                continue
            for rango, c in enumerate(lista):
                clave = f"{c['fuente']}:{c['id']}"
                if clave in vistos or clave in prohibidos:
                    continue
                vistos.add(clave)
                c["consulta"] = q
                c["relevancia"] = relevancia(q, c["titulo"])
                vertical = (c.get("alto") or 0) > (c.get("ancho") or 0)
                c["_nota"] = (c["relevancia"]
                              + (0.25 if vertical else 0.0)
                              + (0.10 if c["duracion_s"] >= necesita_s else 0.0)
                              + 0.15 * (1 - rango / max(1, len(lista)))
                              - 0.05 * orden_q)
                candidatos.append(c)
        candidatos.sort(key=lambda c: -c["_nota"])
        for c in candidatos[:CANDIDATOS_A_MIRAR]:
            if c["relevancia"] < RELEVANCIA_FLOJA or (
                    c["relevancia"] < RELEVANCIA_MIN and mejor_flojo is not None
                    and c["_nota"] <= mejor_flojo["_nota"]):
                continue                      # no se usaría: ni se descarga
            try:
                c = mirar(c, necesita_s, tmp)
            except Exception as ex:
                descartes.append({"escena": n, "plano": k, "id": f"{c['fuente']}:{c['id']}",
                                  "motivo": f"no se pudo mirar: {ex}"[:500]})
                continue
            if c["movimiento"] < MOV_MIN:
                descartes.append({"escena": n, "plano": k, "id": f"{c['fuente']}:{c['id']}",
                                  "titulo": c["titulo"], "motivo": f"quieto (movimiento {c['movimiento']})"})
                continue
            if c["relevancia"] >= RELEVANCIA_MIN:
                return c
            # «Una imagen que no pega es peor que ninguna»: un clip cuyo título
            # no comparte ni una palabra con la búsqueda no se usa nunca.
            if c["relevancia"] >= RELEVANCIA_FLOJA and (
                    mejor_flojo is None or c["_nota"] > mejor_flojo["_nota"]):
                mejor_flojo = c
    return mejor_flojo


def resolver_guion(ident, forzar=False):
    ruta = GUIONES / f"{ident}.es.json"
    guion = json.loads(ruta.read_text(encoding="utf-8"))
    espec = especificacion(guion, ajustes_de(ident))
    if not espec:
        print(f"{ident}: sin campo «visual»; sale como siempre")
        return None
    fir = firma(guion, espec)
    destino = VISUALES / f"{ident}.json"
    if destino.exists() and not forzar:
        try:
            previo = json.loads(destino.read_text(encoding="utf-8"))
            if previo.get("firma") == fir and not previo.get("incompleto"):
                print(f"{ident}: ya resuelto y sin cambios (firma {fir})")
                return None
        except Exception:
            pass
    print(f"\n{ident} · {guion.get('titulo_trabajo', '')}")
    tmp = CACHE / "_tmp" / ident
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True, exist_ok=True)
    carpeta_ia = VISUALES / ident
    shutil.rmtree(carpeta_ia, ignore_errors=True)
    prohibidos = usados_en_otros(ident)
    descartes, escenas_m, errores_ia, fallos_api = [], {}, [], []
    if not (os.environ.get("PEXELS_API_KEY") or os.environ.get("PIXABAY_API_KEY")):
        # Sin claves no se ha buscado nada: el manifiesto queda «incompleto»
        # para que se rehaga solo en cuanto las claves estén.
        fallos_api.append("sin PEXELS_API_KEY ni PIXABAY_API_KEY")
        print("::warning::C50 · sin claves de Pexels ni de Pixabay: no hay archivo que buscar")
    for n, e in enumerate(guion["escenas"], 1):
        s = espec.get(n)
        if not s:
            continue
        dur = duracion_estimada(e)
        est = dict(e, duracion_s=dur)
        usados, _ = fondo_visual.cortes(est, s["planos"], FPS)
        tiempos = [f / FPS for _, f in usados]
        frases = fondo_visual.palabras_del_plano(e.get("narracion") or "", s["planos"], usados, FPS,
                                                 dur - (0.45 if e.get("pausa_despues_s") is None
                                                        else float(e["pausa_despues_s"])))
        planos_m = []
        for j, (k0, f0) in enumerate(usados):
            k = k0 + 1
            p = s["planos"][k0]
            t1 = tiempos[j + 1] if j + 1 < len(tiempos) else dur
            necesita = (t1 - tiempos[j]) * 1.25 + 0.5
            base = {"k": k, "desde": p.get("desde"), "t_estimado": [round(tiempos[j], 2), round(t1, 2)],
                    "frase": frases[j] if j < len(frases) else ""}
            elegido = flojo = None
            excluir = p.get("excluir") or []
            excluir = {excluir} if isinstance(excluir, str) else set(excluir)
            if p.get("marca"):
                elegido = {"fuente": "marca", "tipo": "marca"}
            elif p.get("fuente") != "ia" and (p.get("busqueda") or p.get("fijar")):
                c = _elegir_archivo(p, necesita, prohibidos | excluir, tmp, descartes, n, k,
                                    fallos_api)
                if c and (c["relevancia"] >= RELEVANCIA_MIN or not p.get("prompt")
                          or p.get("fuente") == "archivo"):
                    elegido = c
                elif c:
                    # Hay clip, pero su título apenas se parece a lo que se
                    # busca: antes que un plano que no pega, la imagen
                    # generada. Si esa tampoco sale, se usa el clip igual.
                    descartes.append({"escena": n, "plano": k, "id": f"{c['fuente']}:{c['id']}",
                                      "titulo": c["titulo"],
                                      "motivo": f"poco relevante ({c['relevancia']}): se prueba la IA"})
                    flojo = c
            if not elegido and not p.get("marca") and p.get("prompt") and p.get("fuente") != "archivo":
                semilla = int(p.get("semilla") or int(hashlib.sha1(f"{ident}.{n}.{k}".encode()).hexdigest()[:6], 16))
                try:
                    ia = generar(p["prompt"], semilla, carpeta_ia / f"e{n}_p{k}.jpg")
                    ia["caras"] = caras(RAIZ / ia["fichero"])
                    ia["_fotograma"] = str(RAIZ / ia["fichero"])
                    elegido = ia
                except Exception as ex:
                    errores_ia.append(str(ex))
                    if pasajero(ex):
                        fallos_api.append(str(ex))
                    descartes.append({"escena": n, "plano": k, "motivo": f"IA: {ex}"[:600]})
            if not elegido and flojo:
                elegido = flojo
            if not elegido:
                elegido = {"fuente": "sin_imagen", "tipo": "ninguno",
                           "motivo": "ni archivo ni imagen generada: sale como tarjeta de marca"}
            if elegido.get("id") is not None:
                prohibidos.add(f"{elegido['fuente']}:{elegido['id']}")
            registro = dict(base)
            registro.update({kk: vv for kk, vv in elegido.items() if not kk.startswith("_")
                             and kk not in ("url_ligero", "caras_origen")})
            registro["_fotograma"] = elegido.get("_fotograma")
            planos_m.append(registro)
            print(f"  escena {n} plano {k}: {registro['fuente']:<10} "
                  f"{registro.get('id') or registro.get('fichero') or ''}  "
                  f"rel {registro.get('relevancia', '-')} mov {registro.get('movimiento', '-')} "
                  f"caras {len(registro.get('caras') or [])}  «{registro['frase'][:40]}»")
        escenas_m[str(n)] = {"narracion_sha": _sha(e.get("narracion")),
                             "texto_pos": s.get("texto_pos") or posicion_del_texto(planos_m, dur),
                             "planos": planos_m}
    manifiesto = {"guion": ident, "version": VERSION, "firma": fir,
                  "resuelto_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                  "escenas": escenas_m, "descartes": descartes,
                  "errores_ia": sorted(set(errores_ia))[:5],
                  # Si un servicio falló por algo pasajero (cuota, 5xx, red), el
                  # manifiesto se vuelve a hacer en la próxima pasada aunque el
                  # guion no cambie: un fallo pasajero no puede dejar un Short
                  # sin imagen para siempre. Los permanentes, no (ver pasajero()).
                  "incompleto": bool(fallos_api)}
    try:
        hoja_de_contactos(guion, manifiesto, VISUALES / f"{ident}.jpg")
    except Exception as ex:
        print(f"::warning::{ident}: no se pudo dibujar la hoja de contactos ({ex})")
    for esc in escenas_m.values():
        for p in esc["planos"]:
            p.pop("_fotograma", None)
    VISUALES.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    n_pl = sum(len(v["planos"]) for v in escenas_m.values())
    n_sin = sum(1 for v in escenas_m.values() for p in v["planos"] if p["fuente"] == "sin_imagen")
    print(f"  → {n_pl} planos ({n_sin} sin imagen) · {destino.relative_to(RAIZ)}")
    return manifiesto


def posicion_del_texto(planos, dur):
    """Abajo, salvo que las caras de los planos de la escena caigan más en la
    banda de abajo que en la de arriba. Cada cara pesa por su tamaño y por lo
    que dura su plano."""
    solape = {"abajo": 0.0, "arriba": 0.0}
    for p in planos:
        t0, t1 = (p.get("t_estimado") or [0, dur])[:2]
        peso_t = max(0.0, t1 - t0) / max(dur, 0.001)
        for x, y, w, h in p.get("caras") or []:
            for banda, (b0, b1) in BANDAS.items():
                comun = max(0.0, min(y + h, b1) - max(y, b0))
                solape[banda] += comun * w * peso_t
    return "arriba" if solape["abajo"] > solape["arriba"] * 1.2 and solape["abajo"] > 0.002 else "abajo"


# ---------------------------------------------------------------------------
# La hoja de contactos
# ---------------------------------------------------------------------------
def _fuente_pil(nombre, tam):
    from PIL import ImageFont
    try:
        ruta = subprocess.run(["fc-match", "-f", "%{file}", nombre], capture_output=True,
                              text=True, stdin=subprocess.DEVNULL).stdout.strip()
        return ImageFont.truetype(ruta, tam)
    except Exception:
        return ImageFont.load_default()


def _texto_de_pantalla(e):
    for campo in ("texto", "cifra", "titulo"):
        if e.get(campo):
            return re.sub(r"[*_]", "", e[campo])
    if e.get("a"):
        return re.sub(r"[*_]", "", f"{e.get('a')} / {e.get('b', '')}")
    if e.get("pasos"):
        return " → ".join(re.sub(r"[*_]", "", p.get("titulo", "")) for p in e["pasos"])
    return ""


def _envolver(d, texto, fuente, ancho, max_lineas):
    lineas, linea = [], ""
    for w in (texto or "").split():
        prueba = (linea + " " + w).strip()
        if d.textlength(prueba, font=fuente) > ancho and linea:
            lineas.append(linea)
            linea = w
            if len(lineas) >= max_lineas:
                break
        else:
            linea = prueba
    if linea and len(lineas) < max_lineas:
        lineas.append(linea)
    return lineas


def hoja_de_contactos(guion, manifiesto, destino):
    """Una miniatura por PLANO (no por escena), con la banda donde irá el texto
    y el texto encima, las caras recuadradas en rojo, y debajo la frase que
    suena durante ese plano y de dónde sale. Es lo que mira la revisión
    diaria: ¿la imagen cuenta lo mismo que la frase, justo cuando se dice?"""
    from PIL import Image, ImageDraw
    cw, ch, pie = 216, 384, 150
    planos = []
    for n, e in enumerate(guion["escenas"], 1):
        esc = manifiesto["escenas"].get(str(n))
        if not esc:
            planos.append((n, e, None, None))
            continue
        for p in esc["planos"]:
            planos.append((n, e, esc, p))
    cols = min(7, max(1, len(planos)))
    filas = (len(planos) + cols - 1) // cols
    hoja = Image.new("RGB", (cols * cw, 76 + filas * (ch + pie)), (245, 246, 248))
    d = ImageDraw.Draw(hoja)
    f_tit, f_pie, f_txt = _fuente_pil("Inter:weight=800", 26), _fuente_pil("Inter", 14), \
        _fuente_pil("Inter:weight=800", 20)
    resumen = {}
    for _, _, _, p in planos:
        clave = (p or {}).get("fuente", "sin visual")
        resumen[clave] = resumen.get(clave, 0) + 1
    d.text((14, 12), f"{guion['id']} · {guion.get('titulo_trabajo', '')}"[:110], font=f_tit, fill=(11, 18, 32))
    d.text((14, 46), f"C50 · hoja de contactos · {manifiesto.get('resuelto_utc', '')} · "
                     + ", ".join(f"{v} {k}" for k, v in sorted(resumen.items())), font=f_pie, fill=(70, 76, 90))
    for i, (n, e, esc, p) in enumerate(planos):
        x0, y0 = (i % cols) * cw, 76 + (i // cols) * (ch + pie)
        cuadro = None
        if p and p.get("_fotograma") and Path(p["_fotograma"]).exists():
            im = Image.open(p["_fotograma"]).convert("RGB")
            enc = p.get("encuadre") or {"x": 0.5, "y": 0.5}
            k = max(cw / im.width, ch / im.height)
            im = im.resize((max(cw, round(im.width * k)), max(ch, round(im.height * k))))
            ox = round((im.width - cw) * enc.get("x", 0.5))
            oy = round((im.height - ch) * enc.get("y", 0.5))
            cuadro = im.crop((ox, oy, ox + cw, oy + ch))
        else:
            color = (11, 18, 32) if (p or {}).get("fuente") == "marca" else (90, 94, 104)
            cuadro = Image.new("RGB", (cw, ch), color)
        capa = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        dc = ImageDraw.Draw(capa)
        pos = (esc or {}).get("texto_pos") or "abajo"
        if e.get("tipo") in fondo_visual.TIPOS_CENTRO:
            pos = "centro"
        if p and p.get("tipo") in ("video", "imagen"):
            b0, b1 = BANDAS.get(pos, (0.30, 0.76))
            dc.rectangle((0, int(b0 * ch), cw, int(b1 * ch)), fill=(0, 0, 0, 120))
            for (fx, fy, fw, fh) in p.get("caras") or []:
                dc.rectangle((int(fx * cw), int(fy * ch), int((fx + fw) * cw), int((fy + fh) * ch)),
                             outline=(239, 71, 111, 255), width=3)
            lineas = _envolver(dc, _texto_de_pantalla(e), f_txt, cw - 20, 4)
            ty = int(b0 * ch) + 8
            for ln in lineas:
                dc.text((10, ty), ln, font=f_txt, fill=(255, 255, 255, 255))
                ty += 24
        else:
            etiqueta = {"marca": "TARJETA DE MARCA", "sin_imagen": "SIN IMAGEN → marca"}.get(
                (p or {}).get("fuente"), "SIN VISUAL → como siempre")
            dc.text((10, 12), etiqueta, font=f_pie, fill=(255, 176, 32, 255))
            for j, ln in enumerate(_envolver(dc, _texto_de_pantalla(e), f_txt, cw - 20, 5)):
                dc.text((10, ch // 2 - 40 + j * 24), ln, font=f_txt, fill=(255, 255, 255, 255))
        cuadro = Image.alpha_composite(cuadro.convert("RGBA"), capa).convert("RGB")
        hoja.paste(cuadro, (x0, y0))
        # pie: escena.plano, tiempo, la frase de ese plano y la fuente
        if p:
            t0, t1 = (p.get("t_estimado") or [0, 0])[:2]
            cab = f"{n}.{p.get('k')} · {t0:.1f}–{t1:.1f}s · texto {pos}"
            if (n == len(guion["escenas"]) and e.get("tipo") == "cierre"
                    and p is esc["planos"][-1]):
                cab += " · y firma"     # los últimos 1,75 s del cierre son la tarjeta de marca
            frase = f"«{p.get('frase', '')}»"
            if p.get("fuente") in ("pexels", "pixabay"):
                origen = f"{p['fuente']} {p.get('id')} · {p.get('autor', '')}"
                medidas = f"rel {p.get('relevancia')} · mov {p.get('movimiento')} · caras {len(p.get('caras') or [])}"
            elif p.get("fuente") == "ia":
                origen, medidas = "imagen generada (IA)", f"caras {len(p.get('caras') or [])}"
            else:
                origen, medidas = p.get("fuente", ""), ""
        else:
            cab, frase, origen, medidas = f"{n} · sin «visual»", "", "", ""
        y = y0 + ch + 4
        d.text((x0 + 6, y), cab, font=f_pie, fill=(11, 18, 32))
        y += 18
        for ln in _envolver(d, frase, f_pie, cw - 12, 4):
            d.text((x0 + 6, y), ln, font=f_pie, fill=(40, 45, 55))
            y += 17
        d.text((x0 + 6, y0 + ch + pie - 40), origen[:40], font=f_pie, fill=(70, 76, 90))
        d.text((x0 + 6, y0 + ch + pie - 22), medidas[:44], font=f_pie, fill=(70, 76, 90))
    destino.parent.mkdir(parents=True, exist_ok=True)
    hoja.save(destino, "JPEG", quality=78, optimize=True)
    print(f"  hoja de contactos → {destino.relative_to(RAIZ)}")


# ---------------------------------------------------------------------------
# Órdenes
# ---------------------------------------------------------------------------
def pendientes():
    ya = publicados()
    salida = []
    for g in sorted(GUIONES.glob("MDS-*.es.json")):
        ident = g.name.split(".")[0]
        if ident in ya:
            continue
        try:
            guion = json.loads(g.read_text(encoding="utf-8"))
        except Exception:
            continue
        if any(e.get("visual") for e in guion.get("escenas", [])):
            salida.append(ident)
    return salida


def podar():
    """Las hojas y las imágenes generadas de lo ya publicado hace más de
    DIAS_DE_HOJAS días se borran (el manifiesto se queda: lleva los créditos).
    Sin esto el repositorio engorda ~1 MB por Short."""
    if not REGISTRO.exists():
        return
    limite = datetime.now(timezone.utc) - timedelta(days=DIAS_DE_HOJAS)
    datos = json.loads(REGISTRO.read_text(encoding="utf-8"))
    for p in datos.get("publicaciones", []):
        cuando = p.get("publicar_en") or p.get("subido_utc")
        try:
            t = datetime.strptime(cuando, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        ident = str(p.get("episodio") or "")
        if t < limite and re.fullmatch(r"MD[SH]-\d{3}", ident):
            (VISUALES / f"{ident}.jpg").unlink(missing_ok=True)
            shutil.rmtree(VISUALES / ident, ignore_errors=True)


def orden_resolver(ids, forzar):
    ids = ids or pendientes()
    if not ids:
        print("Nada pendiente con «visual».")
    for ident in ids:
        try:
            resolver_guion(ident, forzar)
        except Exception as ex:          # un guion que falla no tumba los demás
            print(f"::warning::{ident}: no se pudo resolver ({type(ex).__name__}: {ex})")
    podar()
    return 0


def orden_traer(timed):
    """Nunca devuelve error: lo peor que puede pasar es que el Short salga
    como siempre."""
    try:
        return _traer(timed)
    except Exception as ex:
        print(f"::warning::C50 · traer ha fallado ({type(ex).__name__}: {ex}); "
              f"el Short sale como siempre")
        try:
            (Path(timed).parent / "visual" / "local.json").unlink(missing_ok=True)
        except Exception:
            pass
        return 0


def _traer(timed):
    timed = Path(timed)
    carpeta = timed.parent
    try:
        guion = json.loads(timed.read_text(encoding="utf-8"))
    except Exception as ex:
        print(f"::warning::C50 · no puedo leer {timed} ({ex}): el Short sale como siempre")
        return 0
    ident = guion.get("id", "?")
    if APAGADO.exists():
        print(f"C50 apagado ({APAGADO.relative_to(RAIZ)} existe): {ident} sale como siempre")
        return 0
    ruta = VISUALES / f"{ident}.json"
    if not ruta.exists():
        print(f"{ident}: sin manifiesto visual; sale como siempre")
        return 0
    manifiesto = json.loads(ruta.read_text(encoding="utf-8"))
    destino = carpeta / "visual"
    destino.mkdir(parents=True, exist_ok=True)
    local = {"guion": ident, "firma": manifiesto.get("firma"), "escenas": {}}
    bajados = fallidos = 0
    # Presupuesto: si la red va mal, este paso no puede comerse el job (150
    # min). Pasado el límite, lo que quede sale como tarjeta de marca.
    limite = time.monotonic() + TRAER_MAX_S
    for n, e in enumerate(guion.get("escenas", []), 1):
        me = (manifiesto.get("escenas") or {}).get(str(n))
        if not me:
            continue
        if me.get("narracion_sha") != _sha(e.get("narracion")):
            print(f"::warning::{ident} escena {n}: la narración ha cambiado desde que se eligieron "
                  f"sus planos; va como tarjeta de marca hasta que se vuelva a resolver")
            continue
        planos = []
        for p in me.get("planos", []):
            q = dict(p)
            try:
                if p.get("tipo") == "video" and p.get("url"):
                    if not (str(p["url"]).startswith("https://")
                            or (os.environ.get("C50_PRUEBA_LOCAL") == "1"
                                and str(p["url"]).startswith("file://"))):
                        # Solo enlaces públicos de verdad. Un file:// en un
                        # manifiesto es de una prueba que se ha colado en el
                        # repositorio (C50_PRUEBA_LOCAL=1 solo en pruebas).
                        raise RuntimeError(f"enlace que no es https: {str(p['url'])[:80]}")
                    if time.monotonic() > limite:
                        raise RuntimeError(f"se acabó el tiempo de traer ({TRAER_MAX_S} s)")
                    f = destino / f"e{n}_p{p['k']}.mp4"
                    if not f.exists():
                        descargar(p["url"], f, intentos=2,
                                  timeout=max(20, min(120, int(limite - time.monotonic()))))
                    if fondo_visual_duracion(f) <= 0:
                        raise RuntimeError("el fichero no se puede leer")
                    q["local"] = f"visual/{f.name}"
                    bajados += 1
                elif p.get("tipo") == "imagen" and p.get("fichero"):
                    origen = RAIZ / p["fichero"]
                    f = destino / f"e{n}_p{p['k']}{origen.suffix}"
                    shutil.copyfile(origen, f)
                    q["local"] = f"visual/{f.name}"
                    bajados += 1
            except Exception as ex:
                fallidos += 1
                q["tipo"] = "ninguno"
                q["motivo"] = f"no se pudo traer: {ex}"[:300]
                print(f"::warning::{ident} escena {n} plano {p.get('k')}: {q['motivo']}")
            planos.append(q)
        local["escenas"][str(n)] = {"texto_pos": me.get("texto_pos") or "abajo", "planos": planos}
    (destino / "local.json").write_text(json.dumps(local, ensure_ascii=False, indent=2) + "\n",
                                        encoding="utf-8")
    print(f"{ident}: {bajados} planos listos para el render, {fallidos} sin traer "
          f"→ {destino / 'local.json'}")
    return 0


def fondo_visual_duracion(fichero):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(fichero)],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def orden_diagnostico():
    # Sin fecha ni recuentos a propósito: el fichero solo cambia (y solo se
    # sube al repositorio) cuando cambia el estado de algún servicio.
    res = {}
    if os.environ.get("PEXELS_API_KEY"):
        try:
            pedir_json("https://api.pexels.com/videos/search?query=people&per_page=1",
                       {"Authorization": os.environ["PEXELS_API_KEY"]})
            res["pexels"] = "ok"
        except Exception as ex:
            res["pexels"] = f"FALLA: {ex}"
    else:
        res["pexels"] = "sin clave (PEXELS_API_KEY)"
    if os.environ.get("PIXABAY_API_KEY"):
        try:
            pedir_json("https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
                {"key": os.environ["PIXABAY_API_KEY"], "q": "people", "per_page": 3}))
            res["pixabay"] = "ok"
        except Exception as ex:
            res["pixabay"] = f"FALLA: {ex}"
    else:
        res["pixabay"] = "sin clave (PIXABAY_API_KEY)"
    cuenta, token = os.environ.get("CLOUDFLARE_ACCOUNT_ID"), os.environ.get("CLOUDFLARE_API_TOKEN")
    if cuenta and token:
        cab = {"Authorization": f"Bearer {token}"}
        for nombre, url in (("token", "https://api.cloudflare.com/client/v4/user/tokens/verify"),
                            ("token_de_cuenta",
                             f"https://api.cloudflare.com/client/v4/accounts/{cuenta}/tokens/verify")):
            try:
                datos = pedir_json(url, cab)
                res[f"cloudflare_{nombre}"] = f"ok: {(datos.get('result') or {}).get('status', '?')}"
            except Exception as ex:
                res[f"cloudflare_{nombre}"] = f"FALLA: {ex}"
        prueba = CACHE / "_diagnostico.jpg"
        try:
            # 256x256: la prueba cuesta unas 26 neuronas de las 10.000 diarias.
            r = generar("a red apple on a wooden table", 7, prueba, 256, 256)
            res["cloudflare_imagen"] = f"ok con {r['modelo']} ({r['ancho']}x{r['alto']})"
            (RAIZ / r["fichero"]).unlink(missing_ok=True)
        except Exception as ex:
            res["cloudflare_imagen"] = f"FALLA: {ex}"
    else:
        res["cloudflare_imagen"] = "sin claves (CLOUDFLARE_ACCOUNT_ID / CLOUDFLARE_API_TOKEN)"
    VISUALES.mkdir(parents=True, exist_ok=True)
    (VISUALES / "diagnostico.json").write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n",
                                                encoding="utf-8")
    lineas = ["### C50 · diagnóstico de las fuentes de imagen", "",
              "| Servicio | Resultado |", "|---|---|"]
    lineas += [f"| {k} | {str(v).replace('|', '/')[:500]} |" for k, v in res.items()]
    print("\n".join(lineas))
    resumen = os.environ.get("GITHUB_STEP_SUMMARY")
    if resumen:
        with open(resumen, "a", encoding="utf-8") as fh:
            fh.write("\n".join(lineas) + "\n\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="C50 · la imagen de cada plano")
    sub = ap.add_subparsers(dest="orden", required=True)
    r = sub.add_parser("resolver", help="elegir los planos de los guiones pendientes")
    r.add_argument("guiones", nargs="*", help="MDS-024 … (vacío = todo lo pendiente con «visual»)")
    r.add_argument("--forzar", action="store_true", help="aunque no haya cambiado nada")
    t = sub.add_parser("traer", help="bajar los planos antes del render (producir.yml)")
    t.add_argument("timed", help="build/<ID>/guion.timed.json")
    sub.add_parser("diagnostico", help="probar las claves de Pexels, Pixabay y Cloudflare")
    a = ap.parse_args()
    if a.orden == "resolver":
        return orden_resolver(a.guiones, a.forzar)
    if a.orden == "traer":
        return orden_traer(a.timed)
    return orden_diagnostico()


if __name__ == "__main__":
    sys.exit(main())
