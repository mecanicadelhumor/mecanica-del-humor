#!/usr/bin/env python3
"""
caras.py — C51.3, paso 1: ocho caras candidatas para la persona sintética.

Dirección, 23/10/2026 (la prueba debía correr el 13-15/10 y se cayó: ver
PRUEBA.md). Regla 7.1 de 00_estrategia/REGLAS.md: ficticia, que no se parezca
a nadie real, siempre la misma, declarada, nunca experta ni con biografía.

Qué hace: pide a Cloudflare Workers AI ocho retratos con FLUX.2 [klein] 4B
(Apache 2.0, el mismo modelo, servicio y claves que la imagen de los Shorts,
C50), con semillas fijas, y deja en caras/:
    cara_1.jpg … cara_8.jpg   los retratos (1024 x 1024)
    caras.json                modelo, prompt, semilla y licencia de cada uno
    hoja.jpg                  la hoja de contactos que mira el codirector

Las mismas semillas y el mismo prompt dan la misma cara: si el codirector
elige la 3, la 3 se puede regenerar idéntica cuando haga falta.

23/10/2026, mañana: la primera versión pedía FLUX.1 [schnell] con «seed» y
Cloudflare contestó 400 a las ocho («Additional or unevaluated properties
'/seed'»): ese modelo ya no admite semilla. Por eso klein, que sí la admite (por
formulario multipart, como en visual.generar). Si klein falla, schnell sin
semilla: sale la cara, pero no se podría regenerar idéntica (caras.json lo
dice con "semilla": null).

Claves: CLOUDFLARE_ACCOUNT_ID y CLOUDFLARE_API_TOKEN (secretos de GitHub).
Sin ellas, sale con código 2 y lo dice.

Uso:  python3 07_pruebas/presentador-2026-10/caras.py [--solo 3]
"""
import argparse
import base64
import io
import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(RAIZ / "03_produccion" / "pipeline"))
import visual  # noqa: E402  (pedir_json y los reintentos de C50)

MODELO = visual.MODELO_IA                      # FLUX.2 [klein] 4B: admite semilla
MODELO_RESPALDO = visual.MODELO_IA_RESPALDO    # FLUX.1 [schnell]: sin semilla
LADO = 1024
LICENCIA = ("Imagen generada con IA ({nombre}, Black Forest Labs, Apache 2.0) en "
            "Cloudflare Workers AI. Persona ficticia (regla 7.1).")
NOMBRES = {MODELO: "FLUX.2 [klein] 4B", MODELO_RESPALDO: "FLUX.1 [schnell]"}
SALIDA = AQUI / "caras"

# Lo común a las ocho: un presentador de divulgación, no un modelo de anuncio.
BASE = ("head and shoulders portrait photo of a fictional {quien}, friendly science "
        "communicator, looking straight at the camera, mouth closed, relaxed natural "
        "expression, plain dark navy blue studio background, soft even front light, "
        "sharp focus on the face, simple dark sweater, no text, no logo, no jewelry, "
        "realistic skin, 50mm photo")

# Ocho variantes: mitad hombres, mitad mujeres, edades y rasgos distintos, todas
# adultas (regla 7.1 y el encargo del 05/10: ni infantil ni sexualizado).
VARIANTES = [
    (1, 101, "woman in her thirties with short dark hair"),
    (2, 202, "man in his thirties with short brown hair and a trimmed beard"),
    (3, 303, "woman in her forties with shoulder-length curly hair"),
    (4, 404, "man in his forties with glasses and greying temples"),
    (5, 505, "woman in her late twenties with straight black hair in a low ponytail"),
    (6, 606, "man in his late twenties with wavy dark hair, clean shaven"),
    (7, 707, "woman in her fifties with short silver hair"),
    (8, 808, "man in his fifties with a short grey beard"),
]


def generar(n, semilla, quien):
    cuenta = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    prompt = BASE.format(quien=quien)
    cab = {"Authorization": f"Bearer {token}"}
    base = f"https://api.cloudflare.com/client/v4/accounts/{cuenta}/ai/run/"
    errores = []
    for modelo in (MODELO, MODELO_RESPALDO):
        try:
            if modelo == MODELO:
                cuerpo, tipo = visual._multipart({"prompt": prompt, "width": LADO,
                                                  "height": LADO, "seed": semilla})
                datos = json.loads(visual.pedir(base + modelo, cab, cuerpo, tipo, timeout=180))
                usada = semilla
            else:
                datos = visual.pedir_json(base + modelo, cab, {"prompt": prompt, "steps": 8})
                usada = None
        except Exception as ex:          # un modelo que falla: se prueba el otro
            errores.append(f"{modelo}: {type(ex).__name__}: {ex}")
            continue
        imagen = (datos.get("result") or {}).get("image") if isinstance(datos, dict) else None
        if not imagen:
            errores.append(f"{modelo}: respuesta sin imagen: {json.dumps(datos)[:400]}")
            continue
        from PIL import Image
        im = Image.open(io.BytesIO(base64.b64decode(imagen))).convert("RGB")
        destino = SALIDA / f"cara_{n}.jpg"
        im.save(destino, "JPEG", quality=92)
        return {"n": n, "fichero": destino.name, "modelo": modelo, "prompt": prompt,
                "semilla": usada, "ancho": im.width, "alto": im.height,
                "licencia": LICENCIA.format(nombre=NOMBRES[modelo])}
    raise RuntimeError(" | ".join(errores))


def hoja(fichas):
    """Cuatro por fila, con su número grande debajo: el codirector contesta «la 3»."""
    from PIL import Image, ImageDraw, ImageFont
    lado, pie, cols = 360, 70, 4
    filas = (len(fichas) + cols - 1) // cols
    lienzo = Image.new("RGB", (cols * lado, filas * (lado + pie)), (22, 33, 58))
    d = ImageDraw.Draw(lienzo)
    try:
        letra = ImageFont.truetype("DejaVuSans-Bold.ttf", 44)
    except OSError:
        letra = ImageFont.load_default(size=44)
    for i, f in enumerate(fichas):
        x, y = (i % cols) * lado, (i // cols) * (lado + pie)
        im = Image.open(SALIDA / f["fichero"]).resize((lado, lado))
        lienzo.paste(im, (x, y))
        d.text((x + lado // 2, y + lado + pie // 2), str(f["n"]), fill=(255, 176, 32),
               font=letra, anchor="mm")
    lienzo.save(SALIDA / "hoja.jpg", "JPEG", quality=90)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--solo", type=int, help="regenerar solo esta cara (1-8)")
    args = ap.parse_args()
    if not (os.environ.get("CLOUDFLARE_ACCOUNT_ID") and os.environ.get("CLOUDFLARE_API_TOKEN")):
        print("Faltan CLOUDFLARE_ACCOUNT_ID o CLOUDFLARE_API_TOKEN: no se genera nada.")
        return 2
    SALIDA.mkdir(parents=True, exist_ok=True)
    previas = {}
    if (SALIDA / "caras.json").exists():
        previas = {f["n"]: f for f in json.loads((SALIDA / "caras.json").read_text("utf-8"))}
    fichas, fallos = [], []
    for n, semilla, quien in VARIANTES:
        if args.solo and n != args.solo and n in previas:
            fichas.append(previas[n])
            continue
        try:
            fichas.append(generar(n, semilla, quien))
            print(f"cara {n}: hecha con {fichas[-1]['modelo']} (semilla {fichas[-1]['semilla']})")
        except Exception as ex:      # una cara que falla no tira las demás
            fallos.append(f"cara {n}: {type(ex).__name__}: {ex}")
            print(fallos[-1])
    (SALIDA / "caras.json").write_text(json.dumps(fichas, ensure_ascii=False, indent=1), "utf-8")
    if fichas:
        hoja(fichas)
        print(f"Hoja de contactos: {(SALIDA / 'hoja.jpg').relative_to(RAIZ)}")
    return 1 if not fichas else 0


if __name__ == "__main__":
    sys.exit(main())
