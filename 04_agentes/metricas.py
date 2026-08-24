#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metricas.py — lee la analítica del canal sola, sin que Silvestre copie nada.

POR QUÉ EXISTE
--------------
Hasta hoy las métricas se pedían a mano: la tarea del lunes le mandaba a
Silvestre una lista de vídeos y él copiaba los números de YouTube Studio uno a
uno. Con tres vídeos era llevadero; con seis piezas por semana deja de serlo, y
además se cometen errores al copiar.

QUÉ SE PUEDE AUTOMATIZAR Y QUÉ NO — el reparto no es opinable
-------------------------------------------------------------
La API de analítica de YouTube da mucho, pero NO da impresiones ni CTR: esas dos
son exclusivas de Studio y no existen como métrica de la API (lo que la API llama
«impressions» es `adImpressions`, que son impresiones de anuncios, otra cosa).

    POR API, automático            |  SOLO EN STUDIO
    -------------------------------|---------------------------
    visualizaciones                |  impresiones
    duración media                 |  CTR de las impresiones
    % medio visto                  |
    CURVA DE RETENCIÓN completa    |
    retención a los 30 s           |
    suscriptores, me gusta,        |
      comentarios, compartidos     |
    fuentes de tráfico             |

Para las dos que faltan hay una salida que **no crece con el número de vídeos**:
Studio → Analytics → Modo avanzado → Exportar → CSV. Un solo fichero con TODOS
los vídeos a la vez. Se deja en `05_calendario/exportes/` y este script lo lee.
Treinta segundos a la semana, tenga el canal tres vídeos o trescientos.

CREDENCIALES
------------
Necesita un refresh token con el ámbito `yt-analytics.readonly`, que el token
actual NO tiene. `04_agentes/obtener_token_youtube.py` ya lo pide: hay que
ejecutarlo una vez y actualizar el secreto `YT_REFRESH_TOKEN`.

    python3 04_agentes/metricas.py
    python3 04_agentes/metricas.py --desde 2026-08-18
"""
import argparse
import csv
import glob
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "05_calendario" / "registro_publicaciones.json"
SALIDA = RAIZ / "05_calendario" / "metricas.json"
EXPORTES = RAIZ / "05_calendario" / "exportes"

AMBITOS = ["https://www.googleapis.com/auth/yt-analytics.readonly",
           "https://www.googleapis.com/auth/youtube.force-ssl"]

METRICAS = ("views,estimatedMinutesWatched,averageViewDuration,"
            "averageViewPercentage,subscribersGained,likes,comments,shares")

# Días mínimos publicado antes de mirar los números. Antes de 48 h la muestra es
# el propio autor recargando la página.
MINIMO_DIAS = 2


def credenciales():
    faltan = [v for v in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")
              if not os.environ.get(v)]
    if faltan:
        sys.exit(f"Faltan variables de entorno: {', '.join(faltan)}")
    from google.oauth2.credentials import Credentials
    return Credentials(None,
                       refresh_token=os.environ["YT_REFRESH_TOKEN"],
                       client_id=os.environ["YT_CLIENT_ID"],
                       client_secret=os.environ["YT_CLIENT_SECRET"],
                       token_uri="https://oauth2.googleapis.com/token",
                       scopes=AMBITOS)


def duraciones(yt, ids):
    """Duración real de cada vídeo, en segundos. Hace falta para convertir la
    curva de retención (que viene en fracción del vídeo) en «retención a los
    30 segundos», que es el umbral del peldaño 3."""
    fuera = {}
    for i in range(0, len(ids), 50):
        lote = ids[i:i + 50]
        r = yt.videos().list(part="contentDetails", id=",".join(lote)).execute()
        for it in r.get("items", []):
            m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:([\d.]+)S)?",
                         it["contentDetails"]["duration"])
            h, mi, s = (float(g or 0) for g in m.groups())
            fuera[it["id"]] = h * 3600 + mi * 60 + s
    return fuera


def fila(ya, vid, desde, hasta):
    r = ya.reports().query(ids="channel==MINE", startDate=desde, endDate=hasta,
                           metrics=METRICAS, filters=f"video=={vid}").execute()
    cab = [c["name"] for c in r.get("columnHeaders", [])]
    datos = r.get("rows", [[0] * len(cab)])[0]
    return dict(zip(cab, datos))


def retencion(ya, vid, desde, hasta, duracion_s):
    """Curva de retención absoluta y el valor a los 30 segundos.

    Es la métrica que Studio marca como «sin información suficiente» cuando hay
    pocas visualizaciones; la API la devuelve igual, y con ella se puede ver la
    forma de la caída aunque el número no sea significativo todavía."""
    try:
        r = ya.reports().query(ids="channel==MINE", startDate=desde, endDate=hasta,
                               metrics="audienceWatchRatio,relativeRetentionPerformance",
                               dimensions="elapsedVideoTimeRatio",
                               filters=f"video=={vid}").execute()
    except Exception as e:
        return {"error": str(e)[:160]}
    filas = r.get("rows", [])
    if not filas:
        return {"puntos": 0}
    curva = [{"t": round(f[0] * duracion_s, 1), "ratio": round(f[1], 4)} for f in filas]
    a30 = None
    if duracion_s and duracion_s > 30:
        objetivo = 30.0 / duracion_s
        cerca = min(filas, key=lambda f: abs(f[0] - objetivo))
        a30 = round(cerca[1] * 100, 1)
    return {"puntos": len(curva), "a_30s_pct": a30,
            "caida_primer_10_pct": round((curva[0]["ratio"] -
                                          curva[min(len(curva) - 1, len(curva) // 10)]["ratio"]) * 100, 1)
            if len(curva) > 2 else None,
            "curva": curva}


def trafico(ya, vid, desde, hasta):
    try:
        r = ya.reports().query(ids="channel==MINE", startDate=desde, endDate=hasta,
                               metrics="views", dimensions="insightTrafficSourceType",
                               filters=f"video=={vid}", sort="-views").execute()
    except Exception as e:
        return {"error": str(e)[:160]}
    total = sum(f[1] for f in r.get("rows", [])) or 1
    return {f[0]: round(f[1] * 100 / total, 1) for f in r.get("rows", [])}


def leer_export_studio():
    """Impresiones y CTR del CSV de Studio, si lo hay.

    Studio exporta un único CSV con todos los vídeos, así que el trabajo manual
    no crece con el número de vídeos. Se busca el más reciente de
    05_calendario/exportes/. Los nombres de columna cambian con el idioma de la
    interfaz, así que se buscan por palabra clave y no por posición.
    """
    ficheros = sorted(glob.glob(str(EXPORTES / "*.csv")))
    if not ficheros:
        return {}, None
    ruta = ficheros[-1]
    fuera = {}
    with open(ruta, encoding="utf-8-sig", newline="") as fh:
        lector = csv.DictReader(fh)
        for r in lector:
            claves = {k.lower(): k for k in r if k}
            def busca(*palabras):
                for baja, orig in claves.items():
                    if all(p in baja for p in palabras):
                        return r[orig]
                return None
            vid = busca("content") or busca("vídeo") or busca("video")
            if not vid or vid in ("Total", "TOTAL"):
                continue
            impr = busca("impres")
            ctr = busca("clic") or busca("click")
            def num(x):
                if not x:
                    return None
                x = str(x).replace(" ", "").replace(".", "").replace(",", ".")
                x = re.sub(r"[^\d.\-]", "", x)
                try:
                    return float(x)
                except ValueError:
                    return None
            fuera[vid.strip()] = {"impresiones": num(impr), "ctr": num(ctr)}
    return fuera, Path(ruta).name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default=None, help="YYYY-MM-DD; por defecto, la fecha de subida")
    a = ap.parse_args()

    from googleapiclient.discovery import build
    cred = credenciales()
    ya = build("youtubeAnalytics", "v2", credentials=cred, cache_discovery=False)
    yt = build("youtube", "v3", credentials=cred, cache_discovery=False)

    reg = json.loads(REGISTRO.read_text(encoding="utf-8"))["publicaciones"]
    hoy = date.today()
    hasta = (hoy - timedelta(days=1)).isoformat()   # ayer: hoy aún no está cerrado

    candidatos = []
    for p in reg:
        if p.get("estado") != "public" or not p.get("video_id"):
            continue
        subido = datetime.fromisoformat(p["subido_utc"].replace("Z", "+00:00")).date()
        if (hoy - subido).days < MINIMO_DIAS:
            continue
        candidatos.append((p, subido))

    if not candidatos:
        print("No hay vídeos públicos con al menos "
              f"{MINIMO_DIAS} días. Nada que medir.")
        return

    dur = duraciones(yt, [p["video_id"] for p, _ in candidatos])
    studio, nombre_csv = leer_export_studio()
    if nombre_csv:
        print(f"Export de Studio: {nombre_csv} ({len(studio)} filas)")
    else:
        print("Sin export de Studio: no habrá impresiones ni CTR "
              "(la API no las da; ver la cabecera de este fichero).")

    lecturas = []
    for p, subido in candidatos:
        vid = p["video_id"]
        desde = a.desde or subido.isoformat()
        base = fila(ya, vid, desde, hasta)
        d = dur.get(vid, 0)
        fila_out = {
            "leido": hoy.isoformat(),
            "id": p["id"],
            "video_id": vid,
            "titulo": p.get("titulo", ""),
            "formato": "corto" if p["id"].startswith("MDS") else "largo",
            "serie": p.get("serie", ""),
            "publicado": subido.isoformat(),
            "dias_publicado": (hoy - subido).days,
            "duracion_s": round(d, 1),
            "visualizaciones": int(base.get("views", 0)),
            "duracion_media_s": round(float(base.get("averageViewDuration", 0)), 1),
            "porcentaje_visto": round(float(base.get("averageViewPercentage", 0)), 1),
            "minutos_vistos": round(float(base.get("estimatedMinutesWatched", 0)), 1),
            "suscriptores": int(base.get("subscribersGained", 0)),
            "me_gusta": int(base.get("likes", 0)),
            "comentarios": int(base.get("comments", 0)),
            "compartidos": int(base.get("shares", 0)),
            "retencion": retencion(ya, vid, desde, hasta, d),
            "trafico_pct": trafico(ya, vid, desde, hasta),
        }
        fila_out.update(studio.get(vid) or studio.get(p.get("titulo", ""), {})
                        or {"impresiones": None, "ctr": None})
        lecturas.append(fila_out)
        print(f"  {p['id']:12} {fila_out['visualizaciones']:>5} vistas · "
              f"{fila_out['porcentaje_visto']:>5.1f}% visto · "
              f"ret30s {fila_out['retencion'].get('a_30s_pct')} · "
              f"CTR {fila_out.get('ctr')}")

    previo = {"lecturas": []}
    if SALIDA.exists():
        try:
            previo = json.loads(SALIDA.read_text(encoding="utf-8"))
        except Exception:
            pass
    # Se AÑADE, nunca se reescribe: la serie histórica es lo que permite ver si
    # un cambio funcionó. Una lectura del mismo día para el mismo vídeo se
    # sustituye, para que relanzar el script no duplique.
    clave = {(l.get("leido"), l.get("id")) for l in lecturas}
    previo["lecturas"] = [l for l in previo.get("lecturas", [])
                          if (l.get("leido"), l.get("id")) not in clave] + lecturas
    previo["_nota"] = ("Lo escribe 04_agentes/metricas.py desde GitHub Actions. "
                       "Impresiones y CTR solo aparecen si hay un CSV de Studio en "
                       "05_calendario/exportes/: la API de YouTube no las expone.")
    previo["actualizado_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    SALIDA.write_text(json.dumps(previo, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"\nEscrito {SALIDA.relative_to(RAIZ)} — {len(lecturas)} lecturas nuevas, "
          f"{len(previo['lecturas'])} en total.")


if __name__ == "__main__":
    main()
