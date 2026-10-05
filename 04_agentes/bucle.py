#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bucle.py — el marcador del bucle de aprendizaje (C60, 05/10/2026).

Lo que hace, y nada más: junta en una tabla, para cada ciclo de
`05_calendario/bucle/ciclos.json`, qué Shorts salieron en cada brazo (control,
A, B…) y cómo les fue a las 48 horas, y aplica la regla de decisión que se
escribió ANTES de ver los datos. Escribe `05_calendario/bucle/resultados.json`.

    python3 04_agentes/bucle.py              # escribe resultados.json
    python3 04_agentes/bucle.py --imprimir   # además, la tabla en pantalla

Sin red, sin credenciales y sin modelo: lee ficheros del repositorio. Lo lanza
`metricas.yml` después de cada lectura (la diaria y la del lunes). Que lo
calcule el código y no un agente es a propósito: lo que se puede contar, se
cuenta igual todos los días, y nadie puede «interpretar» un empate como una
victoria.

DE DÓNDE SALE CADA COSA

- **Qué brazo es cada Short:** el campo `variante` del guion
  (`05_calendario/guiones/<ID>.es.json`), que escribe la planificación siguiendo
  el `orden` del ciclo. **Se mide lo que salió, no lo que se planificó**: si un
  brazo pide una comprobación en la ficha de producción (`comprobar_en_ficha`,
  por ejemplo que de verdad hubo escenas animadas) y la ficha no la cumple, ese
  Short se aparta con el motivo y no cuenta para nadie.
- **Cómo le fue:** `metricas_diarias.json` (lectura diaria) y `metricas.json`
  (la del lunes); de cada Short se coge la lectura más reciente que traiga
  `se_quedaron_48h`. Antes de 48 horas un Short no cuenta: su número todavía
  se mueve.
- **La cifra principal es «Se quedaron viendo»** (`se_quedaron_48h.pct` =
  engagedViews / views en las primeras 48 h): la parte de los que el feed puso
  delante que no deslizaron. Las demás se enseñan y sirven de freno.

LA REGLA (escrita el 05/10/2026, antes de tener un solo dato del ciclo 1)

Cada variante se compara con el control **del mismo ciclo** (no con el pasado:
el feed y el canal cambian de una semana a otra). Con la media por Short de
«se quedaron» (cada Short pesa uno, para que un viral no decida solo):

  - con 4 o más Shorts por brazo: diferencia ≥ +15 puntos → GANA; ≤ −15 → PIERDE;
  - con 6 o más: ≥ +8 → GANA; ≤ −8 → PIERDE;
  - con 10 o más y sin pasar de ±8 → SIN EFECTO (se queda el control);
  - en cualquier otro caso → SIGUE MIDIENDO.

Y dos frenos: si la variante gana pero su % visto medio queda más de 5 puntos
por debajo del control, es GANA CON REPARO (decide la dirección); y si la
variante tiene dos o más «ceros de feed» (menos de 10 vistas a 48 h) más que el
control, tampoco gana sola.

`prob_mejor` es la probabilidad aproximada (normal, con la dispersión entre
Shorts) de que la variante esté de verdad por encima del control. Es una ayuda
para leer, no parte de la regla.
"""
import argparse
import json
import math
import statistics
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CAL = RAIZ / "05_calendario"
CICLOS = CAL / "bucle" / "ciclos.json"
SALIDA = CAL / "bucle" / "resultados.json"
GUIONES = CAL / "guiones"
QA = CAL / "qa"
DIARIAS = CAL / "metricas_diarias.json"
SEMANAL = CAL / "metricas.json"

REGLA = {
    "temprano": {"n": 4, "umbral_pp": 15.0},
    "normal": {"n": 6, "umbral_pp": 8.0},
    "cierre": {"n": 10},
    "reparo_visto_pp": 5.0,
    "cero_feed_vistas": 10,
}


def _json(ruta, defecto):
    try:
        return json.loads(Path(ruta).read_text(encoding="utf-8"))
    except Exception:
        return defecto


def lecturas_por_short():
    """{ 'MDS-036': {...la lectura más reciente con se_quedaron_48h...} }"""
    filas = []
    sem = _json(SEMANAL, {})
    for x in sem.get("lecturas", []):
        filas.append((x.get("leido") or "", x))
    dia = _json(DIARIAS, {})
    leido_dia = (dia.get("actualizado_utc") or "")[:10]
    for x in dia.get("videos", []):
        filas.append((leido_dia, x))
    mejor = {}
    for leido, x in sorted(filas, key=lambda t: t[0]):
        ident = (x.get("id") or "").replace(".es", "")
        if not ident:
            continue
        sq = x.get("se_quedaron_48h")
        if not isinstance(sq, dict) or sq.get("pct") is None:
            # sin la cifra principal no sustituye a una lectura que sí la traiga
            mejor.setdefault(ident, dict(x, leido=leido))
            continue
        mejor[ident] = dict(x, leido=leido)
    return mejor


def variante_de(ident):
    g = _json(GUIONES / f"{ident}.es.json", {})
    return g.get("variante"), g.get("ciclo")


def ficha_de(ident):
    return _json(QA / f"{ident}.es" / "ficha.json", {})


def cumple_ficha(brazo, ident):
    """None si cumple o no se pide nada; si no, el motivo para apartarlo."""
    req = brazo.get("comprobar_en_ficha")
    if not req:
        return None
    f = ficha_de(ident)
    if not f:
        return "sin ficha de producción todavía"
    valor = f
    for parte in req["campo"].split("."):
        valor = valor.get(parte) if isinstance(valor, dict) else None
    try:
        if valor is None or float(valor) < float(req.get("minimo", 1)):
            return f"no salió como se planificó: {req['campo']} = {valor!r}"
    except (TypeError, ValueError):
        return f"no salió como se planificó: {req['campo']} = {valor!r}"
    return None


def media(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.fmean(xs), 1) if xs else None


def mediana(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 1) if xs else None


def prob_mejor(a, b):
    """P(media real de a > media real de b), aproximación normal."""
    a = [x for x in a if x is not None]
    b = [x for x in b if x is not None]
    if len(a) < 2 or len(b) < 2:
        return None
    va, vb = statistics.variance(a), statistics.variance(b)
    se = math.sqrt(va / len(a) + vb / len(b))
    if se == 0:
        return 1.0 if statistics.fmean(a) > statistics.fmean(b) else 0.0
    z = (statistics.fmean(a) - statistics.fmean(b)) / se
    return round(0.5 * (1 + math.erf(z / math.sqrt(2))), 2)


def resumen_brazo(shorts):
    sq = [s["se_quedaron_pct"] for s in shorts]
    return {
        "n": len(shorts),
        "se_quedaron_media": media(sq),
        "porcentaje_visto_media": media([s.get("porcentaje_visto") for s in shorts]),
        "vistas_48h_mediana": mediana([s.get("vistas_48h") for s in shorts]),
        "me_gusta_por_100": (round(100 * sum(s.get("me_gusta") or 0 for s in shorts)
                                   / max(1, sum(s.get("visualizaciones") or 0 for s in shorts)), 2)
                             if shorts else None),
        "ceros_de_feed": sum(1 for s in shorts
                             if (s.get("vistas_48h") or 0) < REGLA["cero_feed_vistas"]),
    }


def veredicto(var, ctl, rv, rc):
    n = min(rv["n"], rc["n"])
    if n < REGLA["temprano"]["n"]:
        return "faltan datos", None
    d = round(rv["se_quedaron_media"] - rc["se_quedaron_media"], 1)
    if n >= REGLA["normal"]["n"]:
        umbral = REGLA["normal"]["umbral_pp"]
    else:
        umbral = REGLA["temprano"]["umbral_pp"]
    if d >= umbral:
        if (rv["porcentaje_visto_media"] is not None and rc["porcentaje_visto_media"] is not None
                and rv["porcentaje_visto_media"] < rc["porcentaje_visto_media"] - REGLA["reparo_visto_pp"]):
            return "gana con reparo (% visto más bajo): decide la dirección", d
        if rv["ceros_de_feed"] >= rc["ceros_de_feed"] + 2:
            return "gana con reparo (más ceros de feed): decide la dirección", d
        return "GANA", d
    if d <= -umbral:
        return "PIERDE", d
    if n >= REGLA["cierre"]["n"]:
        return "SIN EFECTO: se queda el control", d
    return "sigue midiendo", d


def calcular(hoy=None):
    hoy = hoy or datetime.now(timezone.utc).date()
    ciclos = _json(CICLOS, {}).get("ciclos", [])
    lect = lecturas_por_short()
    out = {"_nota": "Lo escribe 04_agentes/bucle.py desde metricas.yml (C60). No se edita a "
                    "mano: se corrige ciclos.json o el guion, y se vuelve a calcular.",
           "actualizado_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "regla": REGLA, "ciclos": []}
    for c in ciclos:
        brazos = c.get("brazos", {})
        por_brazo = {k: [] for k in brazos}
        apartados, pendientes = [], []
        for g in sorted(GUIONES.glob("MDS-*.es.json")):
            ident = g.name.replace(".es.json", "")
            var, ciclo = variante_de(ident)
            if ciclo != c.get("id") or var not in brazos:
                continue
            motivo = cumple_ficha(brazos[var], ident)
            x = lect.get(ident)
            if motivo and "todavía" not in motivo:
                apartados.append({"id": ident, "variante": var, "motivo": motivo})
                continue
            if motivo:                       # sin ficha todavía: aún no se ha producido
                pendientes.append({"id": ident, "variante": var, "motivo": motivo})
                continue
            if not x or not isinstance(x.get("se_quedaron_48h"), dict) \
                    or x["se_quedaron_48h"].get("pct") is None:
                pendientes.append({"id": ident, "variante": var,
                                   "motivo": "sin «se quedaron» a 48 h todavía"})
                continue
            try:
                pub = date.fromisoformat(x.get("publicado"))
            except (TypeError, ValueError):
                pub = None
            if pub and (hoy - pub).days < 2:
                pendientes.append({"id": ident, "variante": var, "motivo": "menos de 48 h"})
                continue
            por_brazo[var].append({
                "id": ident,
                "publicado": x.get("publicado"),
                "se_quedaron_pct": x["se_quedaron_48h"]["pct"],
                "vistas_48h": x.get("vistas_48h"),
                "porcentaje_visto": x.get("porcentaje_visto"),
                "me_gusta": x.get("me_gusta"),
                "visualizaciones": x.get("visualizaciones"),
                "leido": x.get("leido"),
            })
        res = {k: resumen_brazo(v) for k, v in por_brazo.items()}
        ctl = c.get("control", "control")
        comparaciones = {}
        for k in brazos:
            if k == ctl or ctl not in res:
                continue
            ver, dif = veredicto(k, ctl, res[k], res[ctl])
            comparaciones[k] = {
                "contra": ctl,
                "diferencia_pp": dif,
                "prob_mejor": prob_mejor([s["se_quedaron_pct"] for s in por_brazo[k]],
                                         [s["se_quedaron_pct"] for s in por_brazo[ctl]]),
                "veredicto": ver,
            }
        # Referencia, no regla: los Shorts de los 14 días anteriores al ciclo.
        referencia = []
        try:
            ini = date.fromisoformat(c.get("desde"))
        except (TypeError, ValueError):
            ini = None
        for ident, x in lect.items():
            try:
                pub = date.fromisoformat(x.get("publicado"))
            except (TypeError, ValueError):
                continue
            sq = x.get("se_quedaron_48h")
            if (ini and ident.startswith("MDS") and ini - timedelta(days=14) <= pub < ini
                    and isinstance(sq, dict) and sq.get("pct") is not None):
                referencia.append({"id": ident, "se_quedaron_pct": sq["pct"],
                                   "vistas_48h": x.get("vistas_48h"),
                                   "porcentaje_visto": x.get("porcentaje_visto"),
                                   "me_gusta": x.get("me_gusta"),
                                   "visualizaciones": x.get("visualizaciones")})
        out["ciclos"].append({
            "id": c.get("id"), "desde": c.get("desde"), "hasta": c.get("hasta"),
            "referencia_anterior": {**resumen_brazo(referencia),
                                    "ids": sorted(r["id"] for r in referencia)},
            "brazos": {k: {"nombre": brazos[k].get("nombre"), **res[k],
                           "shorts": por_brazo[k]} for k in brazos},
            "comparaciones": comparaciones,
            "apartados": apartados,
            "pendientes": pendientes,
        })
    return out


def imprimir(out):
    for c in out["ciclos"]:
        print(f"== Ciclo {c['id']} ({c['desde']} → {c['hasta']})")
        for k, b in c["brazos"].items():
            print(f"  {k:<8} n={b['n']:<2} se quedaron {b['se_quedaron_media']} % · "
                  f"visto {b['porcentaje_visto_media']} % · vistas48 mediana "
                  f"{b['vistas_48h_mediana']} · ceros {b['ceros_de_feed']}  ({b['nombre']})")
        for k, v in c["comparaciones"].items():
            print(f"  {k} contra {v['contra']}: {v['diferencia_pp']} pp · "
                  f"P(mejor) {v['prob_mejor']} → {v['veredicto']}")
        for a in c["apartados"]:
            print(f"  apartado {a['id']} ({a['variante']}): {a['motivo']}")
        if c["pendientes"]:
            print("  pendientes: " + ", ".join(f"{p['id']}({p['variante']})" for p in c["pendientes"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--imprimir", action="store_true")
    ap.add_argument("--hoy", default=None, help="YYYY-MM-DD, para probar con otra fecha")
    a = ap.parse_args()
    out = calcular(date.fromisoformat(a.hoy) if a.hoy else None)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if a.imprimir:
        imprimir(out)
    print(f"Escrito {SALIDA.relative_to(RAIZ)} — {len(out['ciclos'])} ciclo(s).")


if __name__ == "__main__":
    main()
