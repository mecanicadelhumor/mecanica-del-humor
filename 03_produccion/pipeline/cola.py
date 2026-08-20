#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cola.py — Agente Programador.

Decide qué hay que producir hoy y con qué reglas. Es la pieza que convierte el
workflow de «lánzalo tú a mano rellenando un formulario» en «se lanza solo».

Lee 05_calendario/parrilla.json y emite un plan: para cada guion del día, con
qué música se monta, en qué estado se sube y —si el episodio ya no pasa por
revisión— a qué hora exacta debe hacerse público.

    python3 cola.py                          # lo que toca hoy (hora española)
    python3 cola.py --fecha 2026-08-22       # simular otro día
    python3 cola.py --episodio MDH-004       # forzar un episodio concreto
    python3 cola.py --guion 05_calendario/guiones/MDH-002.es.json   # suelto

Sale por stdout un JSON compacto (una sola línea, para que quepa en un output
de GitHub Actions) con esta forma:

    {"hay_trabajo": true, "fecha": "...", "episodio": "MDH-002",
     "modo": "revision", "guiones": "ruta1 ruta2",
     "trabajos": [{"id": "MDH-002.es", "guion": "...", "idioma": "es",
                   "musica": "...", "estado": "private",
                   "publicar_en": null}, ...]}

Nunca falla por no tener trabajo: un día sin emisión devuelve hay_trabajo
false y código 0. Fallar sería llenar el buzón de correos de Actions en rojo
por algo que es normal.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PARRILLA = RAIZ / "05_calendario" / "parrilla.json"
GUIONES = RAIZ / "05_calendario" / "guiones"
MUSICA = RAIZ / "03_produccion" / "assets" / "musica"

# Margen mínimo entre «ahora» y la hora programada de publicación. YouTube
# rechaza un publishAt en el pasado, y una ejecución que se retrase o se
# relance a mano no debe tumbar la subida por eso: si ya no hay margen, se
# sube directamente en público.
MARGEN_MIN = 15


# ---------------------------------------------------------------------------
# Zona horaria
# ---------------------------------------------------------------------------
def _desfase_madrid(dt_naive):
    """Desfase de Europe/Madrid en un instante local dado, en horas.

    Se usa zoneinfo si está disponible. El respaldo implementa la regla de la
    UE (último domingo de marzo a las 01:00 UTC → último domingo de octubre)
    para no depender de que la imagen del runner traiga tzdata: este script
    decide la hora a la que se publica un vídeo y equivocarse en una hora es
    publicar a la hora equivocada todos los días.
    """
    try:
        from zoneinfo import ZoneInfo
        return dt_naive.replace(tzinfo=ZoneInfo("Europe/Madrid")).utcoffset().total_seconds() / 3600
    except Exception:
        pass

    def ultimo_domingo(anio, mes):
        d = datetime(anio + (mes == 12), (mes % 12) + 1, 1) - timedelta(days=1)
        return d - timedelta(days=(d.weekday() + 1) % 7)

    ini = ultimo_domingo(dt_naive.year, 3).replace(hour=2)     # 01:00 UTC = 02:00 local
    fin = ultimo_domingo(dt_naive.year, 10).replace(hour=3)    # 01:00 UTC = 03:00 local
    return 2.0 if ini <= dt_naive < fin else 1.0


def hoy_madrid():
    ahora_utc = datetime.now(timezone.utc)
    aprox = ahora_utc.replace(tzinfo=None) + timedelta(hours=2)
    return (ahora_utc.replace(tzinfo=None) + timedelta(hours=_desfase_madrid(aprox))).date()


def a_utc(fecha, hora_local):
    """'2026-08-22' + '18:00' (hora española) → datetime UTC con tz."""
    h, m = (int(x) for x in hora_local.split(":"))
    local = datetime.combine(fecha, datetime.min.time()).replace(hour=h, minute=m)
    return (local - timedelta(hours=_desfase_madrid(local))).replace(tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# Música
# ---------------------------------------------------------------------------
def pistas():
    """Las pistas disponibles, en orden estable y solo las que existen en disco.

    El orden lo fija el nombre del fichero (cama_01, cama_02, cama_03), no el
    orden del JSON, que es un diccionario indexado por hash y no significa
    nada. Se excluye cama.mp3 porque es una copia byte a byte de otra pista:
    entrarla en la rotación haría sonar la misma dos veces de cada tres.
    """
    indice = MUSICA / "creditos.json"
    if not indice.exists():
        return []
    nombres = sorted(p["archivo"] for p in json.loads(
        indice.read_text(encoding="utf-8"))["pistas"].values())
    return [MUSICA / n for n in nombres if (MUSICA / n).exists()]


def musica_de(episodio):
    """Rota entre las pistas según el número de episodio. Vacío si no hay."""
    disponibles = pistas()
    if not disponibles:
        return None
    try:
        n = int(str(episodio).split("-")[-1])
    except ValueError:
        n = 1
    return disponibles[(n - 1) % len(disponibles)]


# ---------------------------------------------------------------------------
# Plan
# ---------------------------------------------------------------------------
def rel(p):
    return str(Path(p).resolve().relative_to(RAIZ)).replace("\\", "/")


def trabajo(episodio, idioma, modo, fecha, horas, avisos, hora_fija=None):
    guion = GUIONES / f"{episodio}.{idioma}.json"
    if not guion.exists():
        avisos.append(f"No existe {rel(guion)}: se salta el canal «{idioma}» de {episodio}.")
        return None

    # El formato lo declara el propio guion. cola.py lo copia al plan para que
    # el workflow pueda ramificar sin volver a abrir el JSON, y para que quede
    # escrito en el log de qué se produjo cada día.
    try:
        formato = json.loads(guion.read_text(encoding="utf-8")).get("formato", "largo")
    except Exception:
        formato = "largo"

    estado, publicar_en = "private", None
    if modo == "automatico":
        # hora_fija: una emisión puede tener su propia hora. Los Shorts salen a
        # una hora distinta del episodio largo, y no tiene sentido meter eso en
        # horas_publicacion, que va por idioma.
        hora = hora_fija or horas.get(idioma, "18:00")
        instante = a_utc(fecha, hora)
        if instante > datetime.now(timezone.utc) + timedelta(minutes=MARGEN_MIN):
            publicar_en = instante.strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            # La hora ya pasó (ejecución tardía o relanzada a mano): programarla
            # sería un error de la API. Se publica ya, que es lo que se quería.
            estado = "public"
            avisos.append(f"{episodio}.{idioma}: las {hora} ya han pasado; se sube público directamente.")

    pista = musica_de(episodio)
    return {
        "id": f"{episodio}.{idioma}",
        "guion": rel(guion),
        "idioma": idioma,
        "formato": formato,
        "musica": rel(pista) if pista else "",
        "estado": estado,
        "publicar_en": publicar_en,
    }


def plan_del_dia(fecha=None, episodio=None, estado=None):
    datos = json.loads(PARRILLA.read_text(encoding="utf-8"))
    horas = datos.get("horas_publicacion", {"es": "18:00", "en": "17:00"})
    fecha = fecha or hoy_madrid()
    avisos = []

    emision = None
    if episodio:
        emision = next((e for e in datos["emisiones"] if e["episodio"] == episodio), None)
        if emision is None:                       # fuera de parrilla: se produce igual
            emision = {"episodio": episodio, "idiomas": ["es", "en"], "modo": "revision"}
    else:
        emision = next((e for e in datos["emisiones"] if e["fecha"] == str(fecha)), None)

    if emision is None:
        return {"hay_trabajo": False, "fecha": str(fecha), "trabajos": [], "guiones": "",
                "avisos": [f"No hay emisión programada para el {fecha}."]}

    modo = emision.get("modo", "revision")
    hora_fija = emision.get("hora")
    trabajos = [t for t in (trabajo(emision["episodio"], idi, modo, fecha, horas,
                                    avisos, hora_fija)
                            for idi in emision.get("idiomas", ["es"])) if t]
    if estado:                                    # override manual del formulario
        for t in trabajos:
            t["estado"], t["publicar_en"] = estado, None

    return {
        "hay_trabajo": bool(trabajos),
        "fecha": str(fecha),
        "episodio": emision["episodio"],
        "modo": modo,
        "formato": trabajos[0]["formato"] if trabajos else "largo",
        "guiones": " ".join(t["guion"] for t in trabajos),
        "trabajos": trabajos,
        "avisos": avisos,
    }


def plan_suelto(rutas, estado=None):
    """Ejecución manual sobre guiones concretos, al margen de la parrilla."""
    trabajos = []
    for r in rutas:
        p = Path(r)
        if not p.is_absolute():
            p = RAIZ / r
        if not p.exists():
            raise SystemExit(f"No existe el guion {r}")
        ident = p.name[:-len(".json")]
        episodio = ident.split(".")[0]
        idioma = ident.split(".")[-1] if "." in ident else "es"
        pista = musica_de(episodio)
        try:
            formato = json.loads(p.read_text(encoding="utf-8")).get("formato", "largo")
        except Exception:
            formato = "largo"
        trabajos.append({
            "id": ident, "guion": rel(p), "idioma": idioma, "formato": formato,
            "musica": rel(pista) if pista else "",
            "estado": estado or "private", "publicar_en": None,
        })
    return {"hay_trabajo": bool(trabajos), "fecha": str(hoy_madrid()),
            "episodio": trabajos[0]["id"].split(".")[0] if trabajos else "",
            "modo": "manual",
            "formato": trabajos[0]["formato"] if trabajos else "largo",
            "guiones": " ".join(t["guion"] for t in trabajos),
            "trabajos": trabajos, "avisos": []}


def main():
    ap = argparse.ArgumentParser(description="Decide qué se produce hoy.")
    ap.add_argument("--fecha", default=None, help="YYYY-MM-DD; por defecto hoy en hora española")
    ap.add_argument("--episodio", default=None, help="fuerza un episodio de la parrilla")
    ap.add_argument("--guion", nargs="*", default=None, help="guiones sueltos, ignora la parrilla")
    ap.add_argument("--estado", default=None, choices=["private", "unlisted", "public"],
                    help="fuerza el estado de subida y anula la publicación programada")
    ap.add_argument("--github-output", action="store_true",
                    help="además de stdout, escribe las claves en $GITHUB_OUTPUT")
    a = ap.parse_args()

    if a.guion:
        plan = plan_suelto(a.guion, a.estado)
    else:
        fecha = datetime.strptime(a.fecha, "%Y-%m-%d").date() if a.fecha else None
        plan = plan_del_dia(fecha, a.episodio, a.estado)

    compacto = json.dumps(plan, ensure_ascii=False, separators=(",", ":"))
    print(compacto)

    for aviso in plan.get("avisos", []):
        print(f"::warning::{aviso}", file=sys.stderr)

    if a.github_output and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as fh:
            fh.write(f"hay_trabajo={'true' if plan['hay_trabajo'] else 'false'}\n")
            fh.write(f"episodio={plan.get('episodio', '')}\n")
            fh.write(f"modo={plan.get('modo', '')}\n")
            fh.write(f"guiones={plan['guiones']}\n")
            fh.write(f"plan={compacto}\n")

    # Resumen legible para quien abra el log.
    if plan["hay_trabajo"]:
        print(f"\n{plan['episodio']} · {plan['fecha']} · modo {plan['modo']}", file=sys.stderr)
        for t in plan["trabajos"]:
            cuando = t["publicar_en"] or ("público ya" if t["estado"] == "public" else "sin programar")
            print(f"  {t['id']:<14} {t['estado']:<8} {cuando:<22} "
                  f"música: {Path(t['musica']).name if t['musica'] else '—'}", file=sys.stderr)
    else:
        print(f"\nNada que producir el {plan['fecha']}.", file=sys.stderr)


if __name__ == "__main__":
    main()
