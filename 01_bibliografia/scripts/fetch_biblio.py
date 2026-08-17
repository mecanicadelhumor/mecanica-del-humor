#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_biblio.py — Agente Bibliotecario (paso 1 del pipeline del canal).

Toma la lista semilla curada (data/semillas.json), la enriquece con metadatos
verificados de OpenAlex, localiza la version legal en acceso abierto de cada
obra (OpenAlex best_oa_location -> Unpaywall -> Europe PMC) y descarga los PDF
disponibles.

Solo descarga contenido en acceso abierto. Nunca toca repositorios pirata.

Uso:
    python3 fetch_biblio.py --email tu@correo.com [--descargar] [--limite N]

Salidas:
    data/corpus.json      corpus enriquecido y deduplicado
    data/informe.md       informe legible del estado de acceso
    pdfs/<id>_<slug>.pdf  PDFs en acceso abierto
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
SEMILLAS = RAIZ / "data" / "semillas.json"
CORPUS = RAIZ / "data" / "corpus.json"
INFORME = RAIZ / "data" / "informe.md"
DIR_PDF = RAIZ / "pdfs"

OPENALEX = "https://api.openalex.org/works"
UNPAYWALL = "https://api.unpaywall.org/v2/{doi}"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

PAUSA = 0.15  # cortesia con las APIs publicas


# ---------------------------------------------------------------- utilidades

def normalizar(texto):
    """Minusculas, sin acentos, sin puntuacion. Para comparar titulos."""
    if not texto:
        return ""
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9 ]+", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def parecido(a, b):
    return SequenceMatcher(None, normalizar(a), normalizar(b)).ratio()


def slug(texto, largo=48):
    s = re.sub(r"[^a-z0-9]+", "-", normalizar(texto)).strip("-")
    return s[:largo].strip("-")


def limpiar_doi(doi):
    if not doi:
        return None
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi or None


def get(url, params=None, headers=None, timeout=25):
    try:
        r = requests.get(url, params=params, headers=headers or {}, timeout=timeout)
        if r.status_code == 200:
            return r
        return None
    except requests.RequestException:
        return None


# ------------------------------------------------------------------ OpenAlex

def openalex_por_doi(doi, email):
    r = get(f"{OPENALEX}/doi:{doi}", params={"mailto": email})
    return r.json() if r else None


def openalex_por_titulo(titulo, anio, email):
    """Busca por titulo y acepta solo si el parecido supera el umbral."""
    params = {"search": titulo, "per-page": 5, "mailto": email}
    r = get(OPENALEX, params=params)
    if not r:
        return None
    mejor, mejor_score = None, 0.0
    for w in r.json().get("results", []):
        s = parecido(titulo, w.get("title") or w.get("display_name") or "")
        if anio and w.get("publication_year"):
            if abs(int(w["publication_year"]) - int(anio)) <= 2:
                s += 0.06
        if s > mejor_score:
            mejor, mejor_score = w, s
    return mejor if mejor_score >= 0.72 else None


def extraer_openalex(w):
    if not w:
        return {}
    loc = w.get("best_oa_location") or {}
    prim = w.get("primary_location") or {}
    autores = []
    for a in (w.get("authorships") or [])[:8]:
        nombre = ((a.get("author") or {}).get("display_name"))
        if nombre:
            autores.append(nombre)
    return {
        "openalex_id": w.get("id"),
        "doi_verificado": limpiar_doi(w.get("doi")),
        "titulo_verificado": w.get("title") or w.get("display_name"),
        "anio_verificado": w.get("publication_year"),
        "revista": ((prim.get("source") or {}).get("display_name")),
        "tipo_openalex": w.get("type"),
        "citas": w.get("cited_by_count"),
        "autores_verificados": autores,
        "es_oa": bool((w.get("open_access") or {}).get("is_oa")),
        "estado_oa": (w.get("open_access") or {}).get("oa_status"),
        "url_pdf": loc.get("pdf_url"),
        "url_landing": loc.get("landing_page_url") or (w.get("open_access") or {}).get("oa_url"),
        "conceptos": [c.get("display_name") for c in (w.get("concepts") or [])[:6]],
    }


# ----------------------------------------------------------------- Unpaywall

def unpaywall(doi, email):
    r = get(UNPAYWALL.format(doi=doi), params={"email": email})
    if not r:
        return {}
    d = r.json()
    loc = d.get("best_oa_location") or {}
    return {
        "unpaywall_oa": bool(d.get("is_oa")),
        "unpaywall_pdf": loc.get("url_for_pdf"),
        "unpaywall_landing": loc.get("url_for_landing_page"),
        "unpaywall_via": loc.get("host_type"),
    }


# ---------------------------------------------------------------- Europe PMC

def europepmc(doi=None, titulo=None):
    if doi:
        q = f'DOI:"{doi}"'
    elif titulo:
        q = f'TITLE:"{titulo}"'
    else:
        return {}
    r = get(EPMC, params={"query": q, "format": "json", "pageSize": 1})
    if not r:
        return {}
    res = (r.json().get("resultList") or {}).get("result") or []
    if not res:
        return {}
    it = res[0]
    pmcid = it.get("pmcid")
    return {
        "pmid": it.get("pmid"),
        "pmcid": pmcid,
        "epmc_pdf": (
            f"https://europepmc.org/api/fulltextRepo?pprId={pmcid}&type=FILE&fileName=EMS.pdf"
            if pmcid and it.get("isOpenAccess") == "Y" else
            (f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/" if pmcid else None)
        ),
        "epmc_abierto": it.get("isOpenAccess") == "Y",
    }


# ---------------------------------------------------------------- descarga

def descargar_pdf(url, destino):
    if not url:
        return False, "sin url"
    try:
        r = requests.get(url, timeout=45, stream=True,
                         headers={"User-Agent": "canal-humor-bibliotecario/1.0 (investigacion academica)"})
        if r.status_code != 200:
            return False, f"HTTP {r.status_code}"
        cabecera = r.raw.read(5, decode_content=True) if hasattr(r.raw, "read") else b""
        contenido = cabecera + r.content if cabecera else r.content
        if not contenido.startswith(b"%PDF"):
            return False, "no es un PDF"
        destino.write_bytes(contenido)
        return True, f"{len(contenido)//1024} KB"
    except requests.RequestException as e:
        return False, type(e).__name__


# ---------------------------------------------------------------- deduplicar

def deduplicar(obras):
    """Deduplica por DOI verificado y por titulo difuso (>=0.90)."""
    vistos_doi, salida, duplicados = {}, [], []
    for o in obras:
        doi = o.get("doi_verificado") or limpiar_doi(o.get("doi"))
        dup_de = None
        if doi and doi in vistos_doi:
            dup_de = vistos_doi[doi]
        else:
            t = o.get("titulo_verificado") or o.get("titulo")
            for prev in salida:
                pt = prev.get("titulo_verificado") or prev.get("titulo")
                if parecido(t, pt) >= 0.90:
                    dup_de = prev["id"]
                    break
        if dup_de:
            o["duplicado_de"] = dup_de
            duplicados.append(o)
        else:
            if doi:
                vistos_doi[doi] = o["id"]
            salida.append(o)
    return salida, duplicados


# -------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True, help="Email de contacto para las APIs (obligatorio por cortesia).")
    ap.add_argument("--descargar", action="store_true", help="Descargar los PDF en acceso abierto.")
    ap.add_argument("--limite", type=int, default=0, help="Procesar solo las N primeras obras (pruebas).")
    ap.add_argument("--solo-articulos", action="store_true", help="Saltar libros (no tienen DOI ni OA).")
    args = ap.parse_args()

    datos = json.loads(SEMILLAS.read_text(encoding="utf-8"))
    obras = datos["obras"]
    if args.limite:
        obras = obras[:args.limite]

    DIR_PDF.mkdir(parents=True, exist_ok=True)
    enriquecidas, control = [], []

    for i, o in enumerate(obras, 1):
        if o.get("autores") == "control-negativo":
            o["nota_qa"] = "entrada de control: excluida del corpus"
            control.append(o)
            print(f"[{i}/{len(obras)}] {o['id']} — entrada de control, omitida")
            continue
        if args.solo_articulos and o.get("tipo") == "libro":
            o["acceso"] = "libro: adquirir o biblioteca"
            enriquecidas.append(o)
            continue

        print(f"[{i}/{len(obras)}] {o['id']} — {o['titulo'][:60]}...", flush=True)
        doi = limpiar_doi(o.get("doi"))
        w = openalex_por_doi(doi, args.email) if doi else None
        if not w:
            w = openalex_por_titulo(o["titulo"], o.get("anio"), args.email)
        o.update(extraer_openalex(w))
        time.sleep(PAUSA)

        doi_final = o.get("doi_verificado") or doi
        if doi_final and not o.get("url_pdf"):
            o.update(unpaywall(doi_final, args.email))
            time.sleep(PAUSA)
        if not o.get("url_pdf") and not o.get("unpaywall_pdf"):
            o.update(europepmc(doi_final, o["titulo"]))
            time.sleep(PAUSA)

        o["pdf_candidato"] = o.get("url_pdf") or o.get("unpaywall_pdf") or o.get("epmc_pdf")
        if o.get("tipo") == "libro":
            o["acceso"] = "libro: adquirir o biblioteca"
        elif o["pdf_candidato"]:
            o["acceso"] = "PDF en acceso abierto"
        elif o.get("url_landing") or o.get("unpaywall_landing"):
            o["acceso"] = "acceso abierto via web (sin PDF directo)"
        elif o.get("doi_verificado"):
            o["acceso"] = "cerrado: usar abstract + pedir al autor"
        else:
            o["acceso"] = "no localizado: revision manual"
        enriquecidas.append(o)

    corpus, duplicados = deduplicar(enriquecidas)

    descargados = 0
    if args.descargar:
        print("\n--- Descargando PDFs en acceso abierto ---")
        for o in corpus:
            url = o.get("pdf_candidato")
            if not url:
                continue
            destino = DIR_PDF / f"{o['id']}_{slug(o['titulo'])}.pdf"
            if destino.exists():
                o["pdf_local"] = destino.name
                continue
            ok, det = descargar_pdf(url, destino)
            print(f"  {o['id']}: {'OK' if ok else 'FALLO'} ({det})")
            if ok:
                o["pdf_local"] = destino.name
                descargados += 1
            time.sleep(PAUSA)

    salida = {
        "meta": {**datos["meta"], "generado": time.strftime("%Y-%m-%d %H:%M:%S"),
                 "total_semillas": len(obras), "total_corpus": len(corpus),
                 "duplicados_detectados": len(duplicados),
                 "controles_excluidos": len(control),
                 "pdfs_descargados": descargados},
        "pilares": datos["pilares"],
        "obras": corpus,
        "duplicados": duplicados,
        "controles": control,
        "fuentes_abiertas": datos["fuentes_abiertas"],
        "clasicos_dominio_publico": datos["clasicos_dominio_publico"],
    }
    CORPUS.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")

    # informe legible
    L = ["# Informe de acceso a la bibliografia\n",
         f"Generado: {salida['meta']['generado']}\n",
         f"- Semillas procesadas: {len(obras)}",
         f"- Obras en el corpus: {len(corpus)}",
         f"- Duplicados detectados y fusionados: {len(duplicados)}",
         f"- Entradas de control excluidas: {len(control)}",
         f"- PDFs descargados: {descargados}\n"]
    conteo = {}
    for o in corpus:
        conteo[o.get("acceso", "?")] = conteo.get(o.get("acceso", "?"), 0) + 1
    L.append("## Estado de acceso\n")
    for k, v in sorted(conteo.items(), key=lambda x: -x[1]):
        L.append(f"- {k}: **{v}**")
    L.append("\n## Detalle por pilar\n")
    for cod, nombre in datos["pilares"].items():
        items = [o for o in corpus if o["pilar"] == cod]
        if not items:
            continue
        L.append(f"### {cod}. {nombre}\n")
        L.append("| id | obra | anio | citas | acceso |")
        L.append("|---|---|---|---|---|")
        for o in sorted(items, key=lambda x: (x["prioridad"], -(x.get("citas") or 0))):
            t = (o.get("titulo_verificado") or o["titulo"])[:70]
            L.append(f"| {o['id']} | {t} | {o.get('anio_verificado') or o.get('anio','')} | "
                     f"{o.get('citas','-')} | {o.get('acceso','')} |")
        L.append("")
    if duplicados:
        L.append("## Duplicados detectados (control de calidad del pipeline)\n")
        for d in duplicados:
            L.append(f"- `{d['id']}` es duplicado de `{d['duplicado_de']}` — {d['titulo'][:60]}")
        L.append("")
    if control:
        L.append("## Entradas de control excluidas correctamente\n")
        for c in control:
            L.append(f"- `{c['id']}` — {c['titulo'][:60]}")
    INFORME.write_text("\n".join(L), encoding="utf-8")

    print(f"\nCorpus: {CORPUS}\nInforme: {INFORME}")
    print(f"Obras: {len(corpus)} | duplicados: {len(duplicados)} | PDFs: {descargados}")


if __name__ == "__main__":
    main()
