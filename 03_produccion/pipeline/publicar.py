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

# Series del canal. Cada guion declara la suya en «serie» y aquí se convierte en
# una lista de reproducción de YouTube, creándola la primera vez.
#
# Por qué importa: desde febrero de 2026 YouTube reduce las notificaciones a los
# espectadores poco activos, así que la campanita ya no es un canal fiable de
# retorno. Lo que hace volver a alguien es reconocer una serie por su nombre.
DESCRIPCION_SERIE = {
    "Desmonta el chiste": "Un chiste, dos segundos de silencio, y el despiece: "
                          "qué expectativa se rompió, por qué fue inofensiva y "
                          "dónde estaba la bisagra.",
    "El experimento": "Un estudio real con un resultado que no te esperas, "
                      "contado en menos de un minuto. La fuente, en la descripción.",
    "Esto no tiene gracia y esto sí": "Dos chistes casi idénticos. Uno funciona y "
                                      "otro no. La diferencia se nota antes de que "
                                      "nadie la explique.",
    "Diagnósticos": "Qué dice de ti la clase de humor que usas, según la taxonomía "
                    "de estilos de humor que se usa en investigación.",
    "Mecanismos": "Cómo funciona una pieza del humor por dentro, con las fuentes "
                  "delante y el sitio donde falla al final.",
    # Estrena el 31/08 con MDS-006. Sin esta entrada la lista de reproducción
    # se habría creado con la descripción vacía y ya no se arregla sola: la
    # lista se crea una vez. Aviso de la planificación del 27/08.
    "Ríete primero, te explico después": "Primero el chiste. Después, por qué "
                  "te ha hecho gracia — y en qué casos ese mecanismo deja de "
                  "funcionar.",
}

# El andamiaje de la descripción (epígrafes y cierre) va en el idioma del
# canal: una descripción inglesa con «Capítulos» y «Fuentes» delata que el
# canal es una traducción de otro. El bloque de atribución de la música NO se
# traduce: es el texto que exige quien licencia la pista.
TEXTOS = {
    "es": {
        "capitulos": "Capítulos",
        "empezamos": "Empezamos",
        "fuentes": "Fuentes",
        "musica": "Música",
        "cierre": ("Guion documentado con investigación revisada por pares y producido "
                   "con ayuda de IA. Si detectas un error, dímelo en comentarios y lo "
                   "corrijo en pantalla."),
    },
    "en": {
        "capitulos": "Chapters",
        "empezamos": "Start",
        "fuentes": "Sources",
        "musica": "Music",
        "cierre": ("Script sourced from peer-reviewed research and produced with the help "
                   "of AI. If you spot an error, tell me in the comments and I'll correct "
                   "it on screen."),
    },
}


def textos(guion):
    return TEXTOS.get(guion.get("idioma", "es"), TEXTOS["es"])


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
        marcas.insert(0, f"00:00 {textos(guion)['empezamos']}")
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
    return list(pista["atribucion"])


def descripcion(guion, meta, biblio, creditos=()):
    T = textos(guion)
    L = []
    if meta.get("descripcion"):
        L.append(meta["descripcion"].strip())
    # Los capítulos son del episodio largo. Un Short de cuarenta segundos con
    # una tabla de capítulos delante es ruido en la descripción.
    caps = [] if guion.get("formato") == "corto" else capitulos(guion)
    if caps:
        L.append(f"\n{T['capitulos']}\n" + "\n".join(caps))
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
        L += [f"\n{T['fuentes']}"] + citas
    if creditos:
        L += [f"\n{T['musica']}"] + list(creditos)
    L.append("\n" + T["cierre"])
    return "\n".join(L)[:4900]


def lista_de_serie(yt, serie):
    """Devuelve el id de la lista de la serie, creándola si hace falta.

    Las listas SÍ están en la API de datos v3 (a diferencia de las pantallas
    finales, las tarjetas y el fijado de comentarios, que no lo están y por eso
    no se automatizan aquí). Coste de cuota: 1 por la búsqueda, 50 por crearla,
    y la creación ocurre una sola vez por serie en toda la vida del canal.
    """
    pagina = None
    while True:
        r = yt.playlists().list(part="snippet", mine=True, maxResults=50,
                                pageToken=pagina).execute()
        for pl in r.get("items", []):
            if pl["snippet"]["title"] == serie:
                return pl["id"]
        pagina = r.get("nextPageToken")
        if not pagina:
            break
    nueva = yt.playlists().insert(
        part="snippet,status",
        body={"snippet": {"title": serie,
                          "description": DESCRIPCION_SERIE.get(serie, "")},
              "status": {"privacyStatus": "public"}}).execute()
    print(f"  lista creada: «{serie}»")
    return nueva["id"]


def primer_comentario(guion, meta):
    """La pregunta del episodio, publicada como primer comentario.

    NO es un comentario que finge ser un espectador: es contenido editorial,
    lo escribe el guionista y va firmado por el canal. Esa distinción es la
    regla 7 de 00_estrategia/REGLAS.md y no se cruza.

    Fijarlo no está en la API v3. O se acepta sin fijar, o son diez segundos a
    mano; no vale la pena forzarlo.
    """
    if meta.get("primer_comentario"):
        return meta["primer_comentario"]
    return guion.get("pregunta_comentarios") or None


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

    # --- serie -> lista de reproducción ------------------------------------
    serie = guion.get("serie") or meta.get("serie")
    if serie:
        try:
            pl = lista_de_serie(yt, serie)
            yt.playlistItems().insert(
                part="snippet",
                body={"snippet": {"playlistId": pl,
                                  "resourceId": {"kind": "youtube#video", "videoId": vid}}}
            ).execute()
            print(f"  añadido a la lista «{serie}»")
        except HttpError as e:
            print(f"  aviso: no se pudo añadir a la lista «{serie}» ({e}).")

    # --- la pregunta, como primer comentario --------------------------------
    # Solo si el vídeo ya es público: en un vídeo privado el comentario no se
    # puede insertar, y en uno programado llegaría antes que el vídeo.
    pregunta = primer_comentario(guion, meta)
    if pregunta and estado == "public":
        try:
            yt.commentThreads().insert(
                part="snippet",
                body={"snippet": {"videoId": vid, "topLevelComment": {"snippet": {
                    "textOriginal": pregunta}}}}).execute()
            print("  pregunta publicada como primer comentario")
        except HttpError as e:
            print(f"  aviso: no se pudo publicar el primer comentario ({e}).")
    elif pregunta:
        print("  (el primer comentario se publicará cuando el vídeo sea público)")

    (carpeta / "publicado.json").write_text(
        json.dumps({"video_id": vid, "url": f"https://youtu.be/{vid}", "estado": estado,
                    "formato": guion.get("formato", "largo"),
                    "serie": serie or "",
                    "pregunta_pendiente": bool(pregunta and estado != "public")},
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
