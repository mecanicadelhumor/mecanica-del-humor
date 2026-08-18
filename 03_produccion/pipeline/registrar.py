#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
registrar.py — la memoria del canal.

Recoge los publicado.json que deja publicar.py en build/<ID>/ y los vuelca en
05_calendario/registro_publicaciones.json, que sí vive en el repositorio.

Sin esto, «¿qué vídeo salió ayer y cómo va?» exige entrar a YouTube a mano.
Con esto, el agente que revisa la calidad cada noche lee un fichero y sabe
qué mirar, con qué guion compararlo y si ya lo revisó.

    python3 registrar.py plan.json build

Es idempotente: relanzar la misma producción actualiza la entrada en vez de
duplicarla.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REGISTRO = RAIZ / "05_calendario" / "registro_publicaciones.json"

CABECERA = ("Qué se ha subido, cuándo y con qué guion. Lo escribe registrar.py al final de "
            "cada producción; lo leen el agente de revisión de calidad y el analista. "
            "«revisado» lo marca el agente de revisión cuando ya ha sacado conclusiones de "
            "ese vídeo, para no repasar dos veces lo mismo.")


def cargar():
    if REGISTRO.exists():
        datos = json.loads(REGISTRO.read_text(encoding="utf-8"))
        datos.setdefault("publicaciones", [])
        return datos
    return {"_nota": CABECERA, "publicaciones": []}


def titulo_de(ident):
    meta = RAIZ / "05_calendario" / "publicaciones" / f"{ident}.json"
    if meta.exists():
        return json.loads(meta.read_text(encoding="utf-8")).get("titulo", "")
    return ""


def main():
    plan_path = Path(sys.argv[1] if len(sys.argv) > 1 else "plan.json")
    build = Path(sys.argv[2] if len(sys.argv) > 2 else "build")
    if not plan_path.exists():
        print(f"No hay plan en {plan_path}: nada que registrar.")
        return

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    datos = cargar()
    por_id = {p["id"]: p for p in datos["publicaciones"]}
    nuevos = 0

    for t in plan.get("trabajos", []):
        subido = build / t["id"] / "publicado.json"
        if not subido.exists():
            print(f"  {t['id']}: sin publicado.json (no llegó a subirse). Se omite.")
            continue
        info = json.loads(subido.read_text(encoding="utf-8"))
        entrada = por_id.get(t["id"], {})
        entrada.update({
            "id": t["id"],
            "episodio": t["id"].split(".")[0],
            "idioma": t.get("idioma", "es"),
            "canal": "Humor Mechanics" if t.get("idioma") == "en" else "Mecánica del Humor",
            "titulo": titulo_de(t["id"]) or entrada.get("titulo", ""),
            "guion": t.get("guion", ""),
            "video_id": info.get("video_id"),
            "url": info.get("url"),
            "estado": info.get("estado"),
            "publicar_en": t.get("publicar_en"),
            "musica": Path(t.get("musica", "")).name,
            "subido_utc": entrada.get("subido_utc") or
                          datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "revisado": entrada.get("revisado", False),
        })
        if t["id"] not in por_id:
            datos["publicaciones"].append(entrada)
            por_id[t["id"]] = entrada
            nuevos += 1
        print(f"  {t['id']}: {entrada['url']}")

    datos["_nota"] = CABECERA
    datos["publicaciones"].sort(key=lambda p: (p.get("episodio", ""), p.get("idioma", "")))
    REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    REGISTRO.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    print(f"Registro actualizado: {len(datos['publicaciones'])} entradas ({nuevos} nuevas).")


if __name__ == "__main__":
    main()
