#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
explorador_de_demanda.py — mide qué pregunta la gente de verdad.

POR QUÉ EXISTE ESTE FICHERO
---------------------------
La tarea de planificación de los jueves corre en modo desatendido, y en ese modo
las herramientas web están bloqueadas: no puede consultar nada por su cuenta. La
primera ejecución, el 20 de agosto, lo dijo con todas las letras y entregó una
medición coja — `vistas_top10: null` en todos los candidatos.

La salida no es pedirle permiso a Silvestre cada jueves (eso devuelve el proyecto
a depender de que él esté delante), sino separar las dos mitades del trabajo:

    ESTE SCRIPT (GitHub Actions, con internet)  ->  MIDE
    La tarea de planificación (sin internet)    ->  JUZGA

Actions no tiene ninguna restricción de red, corre solo, y es gratis en un
repositorio público. Deja los números en 05_calendario/demanda_bruta.json y el
agente los lee del repositorio, que sí puede clonar.

QUÉ MIDE, Y CON QUÉ FIABILIDAD
------------------------------
1. YouTube Data API (`search.list` + `videos.list`) — la señal buena. Busca la
   pregunta y suma las visualizaciones de los diez primeros resultados. Si suman
   medio millón, hay demanda; si suman dos mil, no la hay. Es una medición
   directa, no una estimación.
   Cuota: search.list cuesta 100 unidades, videos.list 1. Con 25 preguntas son
   ~2.525 de las 10.000 diarias, y una subida cuesta 1.600. Por eso el workflow
   corre a mediodía, cuando la producción de la madrugada ya terminó.

2. Autocompletar de YouTube — qué escribe la gente literalmente. Sin clave.
   Endpoint no documentado: si deja de responder, se anota y se sigue.

3. Páginas vistas de Wikipedia — API oficial, sin clave. Sirve de proxy de
   interés y sobre todo de ESTACIONALIDAD.

Lo que NO hace: decidir. No sabe si la bibliografía respalda una pregunta ni si
el enfoque es aceptable. Eso es criterio, y el criterio es del agente.

    python3 04_agentes/explorador_de_demanda.py
    python3 04_agentes/explorador_de_demanda.py --sin-youtube   # solo gratis
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "05_calendario" / "demanda_bruta.json"

AGENTE = "MecanicaDelHumor/1.0 (canal de divulgacion; contacto: mecanicadelhumor@gmail.com)"

# Las semillas del autocompletar. No son temas: son principios de frase, que es
# como escribe la gente en un buscador.
SEMILLAS = [
    "cómo ser gracioso", "cómo ser más divertido", "por qué nos reímos",
    "sentido del humor", "hacer reír", "chistes que", "humor negro",
    "me da vergüenza", "caer bien", "por qué no le hago gracia",
    "hablar en público", "conversación interesante", "risa nerviosa",
]

# Las preguntas que se miden con la API. Salen de las semillas de la semana
# anterior; esta lista es solo el arranque y el agente la reescribe cada jueves
# en 05_calendario/semillas_demanda.json si ese fichero existe.
PREGUNTAS = [
    "cómo ser más gracioso", "por qué nos reímos", "cómo tener sentido del humor",
    "por qué no le hago gracia a nadie", "cómo hacer reír a la gente",
    "psicología del humor", "por qué me río cuando estoy nervioso",
    "humor negro por qué nos hace gracia", "cómo caer bien a la gente",
    "miedo al ridículo", "cómo contar un chiste bien", "por qué se contagia la risa",
]

ARTICULOS_WIKI = ["Humor", "Risa", "Comedia", "Chiste", "Ironía", "Sátira"]


def _get(url, cabeceras=None, intentos=3):
    for i in range(intentos):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": AGENTE, **(cabeceras or {})})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if i == intentos - 1:
                return None
            time.sleep(1.5 * (i + 1))
    return None


# ---------------------------------------------------------------------------
# 1. Autocompletar de YouTube
# ---------------------------------------------------------------------------
def autocompletar(semilla, nivel2=True):
    """Devuelve las búsquedas reales que empiezan por la semilla.

    Endpoint no documentado. Si un día deja de responder, esta función devuelve
    lista vacía y el resto del script sigue: nunca puede tumbar la medición.
    """
    salida, consultas = set(), [semilla]
    if nivel2:
        consultas += [f"{semilla} {c}" for c in "abcdeglmpqrstvy"]
    fallos = 0
    for q in consultas:
        url = ("https://suggestqueries.google.com/complete/search"
               f"?client=firefox&ds=yt&hl=es&gl=es&q={urllib.parse.quote(q)}")
        crudo = _get(url)
        if not crudo:
            fallos += 1
            if fallos >= 3 and not salida:
                break                      # el endpoint no responde: no insistas
            continue
        try:
            salida.update(s.strip() for s in json.loads(crudo)[1] if s.strip())
        except Exception:
            pass
        time.sleep(0.15)               # cortesía; el endpoint no está publicado
    return sorted(salida)


# ---------------------------------------------------------------------------
# 2. YouTube Data API — la señal buena
# ---------------------------------------------------------------------------
def cliente_youtube():
    faltan = [v for v in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")
              if not os.environ.get(v)]
    if faltan:
        print(f"  (sin YouTube API: faltan {', '.join(faltan)})", file=sys.stderr)
        return None
    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        print("  (sin YouTube API: falta google-api-python-client)", file=sys.stderr)
        return None
    cred = Credentials(None,
                       refresh_token=os.environ["YT_REFRESH_TOKEN"],
                       client_id=os.environ["YT_CLIENT_ID"],
                       client_secret=os.environ["YT_CLIENT_SECRET"],
                       token_uri="https://oauth2.googleapis.com/token",
                       scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    return build("youtube", "v3", credentials=cred, cache_discovery=False)


def medir_pregunta(yt, pregunta, gasto):
    """Vistas de los diez primeros resultados. Es la medición que decide."""
    try:
        r = yt.search().list(part="id", q=pregunta, type="video", maxResults=10,
                             regionCode="ES", relevanceLanguage="es",
                             order="relevance").execute()
        gasto["unidades"] += 100
    except Exception as e:
        return {"error": str(e)[:200]}
    ids = [i["id"]["videoId"] for i in r.get("items", []) if i.get("id", {}).get("videoId")]
    if not ids:
        return {"vistas_top10": 0, "resultados": 0}
    try:
        v = yt.videos().list(part="statistics,snippet,contentDetails",
                             id=",".join(ids)).execute()
        gasto["unidades"] += 1
    except Exception as e:
        return {"error": str(e)[:200]}

    vistas, detalle = [], []
    for it in v.get("items", []):
        n = int(it.get("statistics", {}).get("viewCount", 0) or 0)
        vistas.append(n)
        detalle.append({
            "titulo": it["snippet"]["title"][:110],
            "canal": it["snippet"]["channelTitle"],
            "publicado": it["snippet"]["publishedAt"][:10],
            "vistas": n,
            "duracion": it.get("contentDetails", {}).get("duration", ""),
        })
    detalle.sort(key=lambda d: -d["vistas"])
    total = sum(vistas)
    mediana = sorted(vistas)[len(vistas) // 2] if vistas else 0
    # Competencia: no es cuántas vistas hay, es si los que las tienen son buenos.
    # Un tema con mucha demanda y resultados viejos o flojos es exactamente
    # donde hay que estar.
    antiguedad = [d["publicado"] for d in detalle[:5]]
    return {
        "vistas_top10": total,
        "mediana_vistas": mediana,
        "resultados": len(vistas),
        "top5_publicados": antiguedad,
        "top5": detalle[:5],
    }


# ---------------------------------------------------------------------------
# 3. Wikipedia — estacionalidad
# ---------------------------------------------------------------------------
def wikipedia(articulo, dias=365):
    fin = date.today() - timedelta(days=1)
    ini = fin - timedelta(days=dias)
    url = ("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
           f"es.wikipedia/all-access/all-agents/{urllib.parse.quote(articulo)}/daily/"
           f"{ini:%Y%m%d}/{fin:%Y%m%d}")
    crudo = _get(url)
    if not crudo:
        return None
    try:
        items = json.loads(crudo)["items"]
    except Exception:
        return None
    por_mes = {}
    for it in items:
        por_mes.setdefault(it["timestamp"][:6], []).append(it["views"])
    return {
        "media_diaria": round(sum(i["views"] for i in items) / max(len(items), 1), 1),
        "por_mes": {m: sum(v) for m, v in sorted(por_mes.items())},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-youtube", action="store_true",
                    help="salta la API de YouTube (no gasta cuota)")
    ap.add_argument("--max-preguntas", type=int, default=25)
    a = ap.parse_args()

    # El agente puede reescribir la lista de preguntas de una semana para otra.
    propias = RAIZ / "05_calendario" / "semillas_demanda.json"
    preguntas, semillas = PREGUNTAS, SEMILLAS
    if propias.exists():
        try:
            d = json.loads(propias.read_text(encoding="utf-8"))
            preguntas = d.get("preguntas") or preguntas
            semillas = d.get("semillas") or semillas
            print(f"Semillas propias desde {propias.name}")
        except Exception as e:
            print(f"Aviso: {propias.name} no se pudo leer ({e}); se usan las de serie.")

    resultado = {
        "generado_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "_nota": ("Medición en bruto. NO decide nada: no sabe si la bibliografía "
                  "respalda una pregunta ni si el enfoque es aceptable. Eso lo "
                  "juzga la tarea de planificación de los jueves, que escribe "
                  "05_calendario/demanda.json a partir de este fichero."),
        "autocompletar": {}, "youtube": {}, "wikipedia": {}, "avisos": [],
    }

    print("1. Autocompletar de YouTube")
    # La expansión por letras multiplica por dieciséis las peticiones. Solo se
    # hace con las cinco primeras semillas, que son las que más rinden; el resto
    # se consulta a secas. Con esto el paso baja de ~15 min a ~2.
    for i, s in enumerate(semillas):
        sug = autocompletar(s, nivel2=(i < 5))
        resultado["autocompletar"][s] = sug
        print(f"   {s:32} {len(sug):3} sugerencias")
    if not any(resultado["autocompletar"].values()):
        resultado["avisos"].append(
            "El autocompletar no devolvió nada. Endpoint no documentado: puede "
            "haber cambiado. Comprobar suggestqueries.google.com a mano.")

    if not a.sin_youtube:
        print("2. YouTube Data API")
        yt = cliente_youtube()
        if yt is None:
            resultado["avisos"].append("Sin credenciales de YouTube: falta la señal principal.")
        else:
            gasto = {"unidades": 0}
            for q in preguntas[:a.max_preguntas]:
                m = medir_pregunta(yt, q, gasto)
                resultado["youtube"][q] = m
                if "error" in m:
                    print(f"   {q[:40]:42} ERROR {m['error'][:60]}")
                    if "quota" in m["error"].lower():
                        resultado["avisos"].append("Cuota de la API agotada a mitad de la medición.")
                        break
                else:
                    print(f"   {q[:40]:42} {m['vistas_top10']:>10,} vistas top10")
            resultado["cuota_gastada"] = gasto["unidades"]
            print(f"   cuota gastada: {gasto['unidades']} unidades de 10.000")

    print("3. Wikipedia")
    for art in ARTICULOS_WIKI:
        w = wikipedia(art)
        resultado["wikipedia"][art] = w
        print(f"   {art:12} {w['media_diaria'] if w else '—'} visitas/día de media")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(resultado, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"\nEscrito {SALIDA.relative_to(RAIZ)}")
    for av in resultado["avisos"]:
        print(f"AVISO: {av}")


if __name__ == "__main__":
    main()
