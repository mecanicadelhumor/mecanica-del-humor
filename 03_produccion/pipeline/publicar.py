#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publicar.py — Agente Publicador.

Sube el vídeo a YouTube en estado privado, con su miniatura, sus subtítulos y
sus capítulos. Publicar de verdad lo decides tú: este script nunca pone nada en
público salvo que se le pida explícitamente.

Credenciales por variables de entorno (secretos de GitHub Actions):
    YT_CLIENT_ID · YT_CLIENT_SECRET · YT_REFRESH_TOKEN

    python3 publicar.py build/MDH-001 --estado private

Cuota: la API da 10.000 unidades al día y una subida cuesta 1.600, así que
caben seis vídeos diarios. De sobra para dos por semana en dos idiomas.
"""
import argparse
import json
import os
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

AMBITOS = ["https://www.googleapis.com/auth/youtube.upload",
           "https://www.googleapis.com/auth/youtube.force-ssl"]


def credenciales():
    faltan = [v for v in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")
              if not os.environ.get(v)]
    if faltan:
        raise SystemExit(f"Faltan variables de entorno: {', '.join(faltan)}")
    return Credentials(
        None,
        refresh_token=os.environ["YT_REFRESH_TOKEN"],
        client_id=os.environ["YT_CLIENT_ID"],
        client_secret=os.environ["YT_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=AMBITOS)


def capitulos(guion):
    """YouTube crea capítulos si la descripción empieza por 00:00 y hay 3 o más."""
    marcas, reloj = [], 0.0
    for e in guion["escenas"]:
        if e.get("tipo") in ("titulo", "cierre") and e.get("titulo"):
            m, s = divmod(int(reloj), 60)
            titulo = e["titulo"].replace("*", "").replace("_", "")
            marcas.append(f"{m:02d}:{s:02d} {titulo}")
        reloj += e.get("duracion_s", 0)
    if marcas and not marcas[0].startswith("00:00"):
        marcas.insert(0, "00:00 Empezamos")
    return marcas if len(marcas) >= 3 else []


def creditos_musica(carpeta, raiz):
    """Bloque de atribución de la música usada, o [] si el vídeo no lleva.

    montaje.py deja el sha256 de la pista en musica.json; aquí se busca ese
    hash en assets/musica/creditos.json. Va por hash y no por nombre porque
    cama.mp3 es una copia de otra pista y el nombre miente.
    """
    marca = carpeta / "musica.json"
    if not marca.exists():
        return []                      # vídeo sin música: nada que atribuir
    usada = json.loads(marca.read_text(encoding="utf-8"))
    indice = raiz / "03_produccion" / "assets" / "musica" / "creditos.json"
    if not indice.exists():
        raise SystemExit(f"Falta {indice}: no se puede atribuir la música y "
                         "atribuirla es obligación de la licencia.")
    pistas = json.loads(indice.read_text(encoding="utf-8"))["pistas"]
    pista = pistas.get(usada.get("sha256"))
    if not pista:
        raise SystemExit(
            f"La música usada ({usada.get('archivo')}, sha256 "
            f"{usada.get('sha256','?')[:12]}...) no está en creditos.json. "
            "Añade su bloque de atribución antes de publicar: en las CC BY "
            "publicar sin atribuir incumple la licencia.")
    return ["\nMúsica"] + list(pista["atribucion"])


def descripcion(guion, meta, biblio, creditos=()):
    L = []
    if meta.get("descripcion"):
        L.append(meta["descripcion"].strip())
    caps = capitulos(guion)
    if caps:
        L.append("\nCapítulos\n" + "\n".join(caps))
    citas = []
    for f in sorted({e["fuente"] for e in guion["escenas"] if e.get("fuente")}):
        o = biblio.get(f)
        if not o:
            continue
        linea = f"· {o['autores']} ({o.get('anio','s.f.')}). {o['titulo']}. {o.get('fuente','')}"
        if o.get("doi"):
            linea += f" https://doi.org/{o['doi']}"
        citas.append(linea)
    if citas:                      # sin esto quedaba un epígrafe "Fuentes" vacío
        L += ["\nFuentes"] + citas
    L += list(creditos)
    L.append("\nGuion documentado con investigación revisada por pares y producido con ayuda de IA. "
             "Si detectas un error, dímelo en comentarios y lo corrijo en pantalla.")
    return "\n".join(L)[:4900]


def publicar(carpeta, estado="private", publicar_en=None):
    carpeta = Path(carpeta)
    guion = json.loads((carpeta / "guion.timed.json").read_text(encoding="utf-8"))
    raiz = Path(__file__).resolve().parents[2]

    # Título, descripción y etiquetas los escribe el agente Empaquetador, y su
    # sitio canónico es el repositorio (queda versionado y revisable antes de
    # publicar), no la carpeta build/ que se borra en cada ejecución:
    #     05_calendario/publicaciones/<ID>.json      <- canónico
    #     build/<ID>/publicacion.json                <- override puntual
    # <ID> es el nombre de la carpeta de build, que ya distingue idioma
    # (MDH-001.es / MDH-001.en). Si no hay ninguno de los dos, se cae al
    # titulo_trabajo del guion, que sirve para una prueba privada pero no
    # para publicar de cara al público.
    meta = {}
    for cand in (raiz / "05_calendario" / "publicaciones" / f"{carpeta.name}.json",
                 carpeta / "publicacion.json"):
        if cand.exists():
            meta = json.loads(cand.read_text(encoding="utf-8"))
            print(f"Metadatos de publicación: {cand}")
    if not meta:
        print("Aviso: sin publicacion.json — se usa el título de trabajo del guion.")

    sem = raiz / "01_bibliografia" / "data" / "semillas.json"
    biblio = {o["id"]: o for o in json.loads(sem.read_text(encoding="utf-8"))["obras"]} \
        if sem.exists() else {}
    creditos = creditos_musica(carpeta, raiz)

    yt = build("youtube", "v3", credentials=credenciales(), cache_discovery=False)
    estado_dict = {"privacyStatus": estado, "selfDeclaredMadeForKids": False}
    if publicar_en:
        estado_dict["publishAt"] = publicar_en   # ISO-8601 UTC; exige privacyStatus private

    cuerpo = {
        "snippet": {
            "title": (meta.get("titulo") or guion["titulo_trabajo"])[:100],
            "description": descripcion(guion, meta, biblio, creditos),
            "tags": meta.get("etiquetas", ["humor", "psicología", "ciencia", "habilidades sociales"])[:15],
            "categoryId": "27",                      # Educación
            "defaultLanguage": guion.get("idioma", "es"),
            "defaultAudioLanguage": guion.get("idioma", "es"),
        },
        "status": estado_dict,
    }

    peticion = yt.videos().insert(
        part="snippet,status", body=cuerpo,
        media_body=MediaFileUpload(str(carpeta / "final.mp4"), chunksize=-1, resumable=True))
    respuesta = None
    while respuesta is None:
        _, respuesta = peticion.next_chunk()
    vid = respuesta["id"]
    print(f"Subido: https://youtu.be/{vid}  (estado: {estado})")

    # La miniatura y los subtítulos son mejoras, no el objetivo: si uno de los
    # dos falla (p. ej. 403 "forbidden" en miniaturas porque el canal aún no
    # ha verificado el teléfono en youtube.com/verify) no debe tirar abajo la
    # subida ya hecha ni impedir que se guarde publicado.json. Se avisa y se
    # sigue; vuelve a lanzar publicar.py sobre el mismo vídeo cuando esté
    # resuelto — YouTube deja repetir thumbnails().set() sin duplicar nada.
    mini = carpeta / "miniatura.png"
    if mini.exists():
        try:
            yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(str(mini))).execute()
            print("  miniatura puesta")
        except HttpError as e:
            print(f"  aviso: no se pudo poner la miniatura ({e}).")
            if e.resp is not None and e.resp.status == 403:
                print("  → probablemente el canal no ha verificado el teléfono: "
                      "https://youtube.com/verify (desbloquea miniaturas personalizadas).")

    srt = carpeta / "subtitulos.srt"
    if srt.exists():
        try:
            yt.captions().insert(
                part="snippet",
                body={"snippet": {"videoId": vid, "language": guion.get("idioma", "es"),
                                  "name": "Original", "isDraft": False}},
                media_body=MediaFileUpload(str(srt))).execute()
            print("  subtítulos subidos")
        except HttpError as e:
            print(f"  aviso: no se pudieron subir los subtítulos ({e}).")

    (carpeta / "publicado.json").write_text(
        json.dumps({"video_id": vid, "url": f"https://youtu.be/{vid}", "estado": estado},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    return vid


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--estado", default="private", choices=["private", "unlisted", "public"])
    ap.add_argument("--publicar-en", default=None,
                    help="ISO-8601 UTC para programar, p. ej. 2026-08-11T16:00:00Z")
    a = ap.parse_args()
    publicar(a.carpeta, a.estado, a.publicar_en)
