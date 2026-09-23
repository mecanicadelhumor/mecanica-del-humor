#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_produccion/pipeline/fondo_visual.py — C50 · el vídeo detrás del texto.
Versión 13 del plan (23/09/2026).

Lo usa render.py. NO toca la red (regla 11.6): trabaja solo con lo que
`visual.py traer` ha dejado en build/<ID>/visual/ ANTES del render.

  · cortes()          en qué fotograma de su escena empieza cada plano.
  · plan()            la línea de tiempo del Short entero: qué tramos van sobre
                      archivo (el texto encima, con fondo transparente) y cuáles
                      son tarjeta de marca (el render de siempre).
  · pista_de_fondo()  el mp4 de fondo, mudo, con exactamente los fotogramas del
                      Short.

Por qué existe «desde» (lo vio el codirector el 23/09 en la prueba): los planos
de una escena se repartían la escena a partes iguales, así que en MDS-023 el
coche averiado salía mientras la voz decía «caldera» y la tostadora mientras
decía «sonríes». Ahora cada plano puede decir desde qué palabras de la
narración entra, y el corte cae justo antes de que la voz las diga. El
instante se estima sobre la voz REAL de esa escena: se miden sus silencios con
ffmpeg y las letras se reparten solo sobre el tiempo en que hay voz.
"""
import json
import re
import subprocess
import unicodedata
from pathlib import Path

PAUSA_POR_DEFECTO = 0.45   # la misma que voz.py cuando la escena no dice otra
ANTICIPO_S = 0.12          # la imagen entra un pelo antes que la palabra: así se ve a la vez que se oye
MIN_PLANO_S = 1.0          # un plano de menos de un segundo no se ve: es un parpadeo
REMATE_S = 1.75            # los últimos 1,75 s del cierre: la firma de marca (C15.5, igual que escena.html)
SILENCIO_DB = -38          # umbral de silencio para medir la voz de cada escena
SILENCIO_S = 0.14          # un silencio más corto que esto no es una pausa, es una consonante

# Tipos de escena que se componen en el centro (paneles, pasos, puntos): no
# caben en la banda de abajo sin quedar diminutos.
TIPOS_CENTRO = {"comparacion", "diagrama", "lista"}
# Tipos que nunca van sobre archivo: una gráfica encima de un vídeo no se lee.
TIPOS_SOLO_MARCA = {"figura"}


def _ffmpeg(*args):
    r = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *args],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg falló: {r.stderr[-800:]}")


# ---------------------------------------------------------------------------
# 1. Dónde cae cada corte
# ---------------------------------------------------------------------------
def _normalizar(texto):
    """Minúsculas, sin tildes ni signos, espacios simples. Devuelve también un
    mapa de cada carácter normalizado a su índice en el texto original."""
    salida, mapa = [], []
    for i, c in enumerate(texto or ""):
        b = unicodedata.normalize("NFD", c)[0].lower()
        if b.isalnum():
            salida.append(b)
            mapa.append(i)
        elif salida and salida[-1] != " ":
            salida.append(" ")
            mapa.append(i)
    return "".join(salida), mapa


def posicion(narracion, fragmento, desde=0):
    """Índice en `narracion` donde empieza `fragmento` (sin mirar tildes,
    mayúsculas ni signos), buscando a partir del carácter `desde` y solo en
    principio de palabra. None si no está."""
    n, mapa = _normalizar(narracion)
    f = _normalizar(fragmento)[0].strip()
    if not f:
        return None
    j0 = next((k for k, i in enumerate(mapa) if i >= desde), len(n))
    for inicio in (j0, 0):
        j = n.find(f, inicio)
        while j >= 0:
            if j == 0 or n[j - 1] == " ":
                return mapa[j]
            j = n.find(f, j + 1)
    return None


def _silencios(audio):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(audio),
                        "-af", f"silencedetect=noise={SILENCIO_DB}dB:d={SILENCIO_S}",
                        "-f", "null", "-"],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    texto = r.stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", texto)
    dur = (int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))) if m else 0.0
    ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", texto)]
    fin = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", texto)]
    fin += [dur] * (len(ini) - len(fin))
    return list(zip(ini, fin)), dur


def tramos_de_voz(audio, habla_s):
    """(activos, silencios): los intervalos en que SUENA la voz de la escena y
    los silencios que hay ENTRE ellos (sin el del principio ni el del final).
    Sin audio legible, un único tramo con toda la parte hablada."""
    por_defecto = ([(0.08, max(0.1, habla_s))], [])
    try:
        silencios, dur = _silencios(audio)
    except Exception:
        return por_defecto
    if dur <= 0:
        return por_defecto
    activos, t = [], 0.0
    for a, b in sorted(silencios):
        a, b = max(0.0, a), min(dur, b)
        if a > t + 0.02:
            activos.append((t, a))
        t = max(t, b)
    if dur > t + 0.02:
        activos.append((t, dur))
    if not activos:
        return por_defecto
    internos = [(a, b) for a, b in sorted(silencios)
                if a > activos[0][0] + 0.02 and b < activos[-1][1] - 0.02]
    return activos, internos


def _pesos(texto, con_pausas):
    """Cuánto «tiempo de voz» pesa cada carácter. Con el audio delante, las
    pausas ya las ponen los silencios medidos y los signos pesan cero; sin él,
    una coma y un punto se estiman como una pausa."""
    w = []
    for c in texto:
        if c.isalnum():
            w.append(1.0)
        elif c.isspace():
            w.append(0.35)
        elif c in ",;:":
            w.append(2.6 if con_pausas else 0.0)
        elif c in ".?!…":
            w.append(5.0 if con_pausas else 0.0)
        else:
            w.append(0.0)
    return w


def _instante(indice, pesos, activos):
    """Reparto proporcional: las letras, sobre el tiempo en que hay voz."""
    total = sum(pesos) or 1.0
    objetivo = sum(pesos[:indice]) / total * sum(b - a for a, b in activos)
    for a, b in activos:
        if objetivo < (b - a):
            return a + objetivo
        objetivo -= (b - a)
    return activos[-1][1]


def mapa_de_tiempo(texto, activos, silencios):
    """Función índice-de-carácter → instante (s) dentro de la escena.

    El reparto proporcional de letras se equivoca en las frases con muchas
    palabras cortas («Lo malo es que eran diez por grupo.»): medido el 23/09,
    hasta medio segundo, justo en los cortes que más importan, los que van a
    principio de frase. Así que se ANCLA en las pausas: cada signo de puntuación
    que la voz respeta es un silencio medido en el audio. Se empareja cada
    silencio con el signo más cercano a donde lo esperaba el reparto
    proporcional (a menos de 0,8 s y en orden), y la palabra que sigue a ese
    signo empieza EXACTAMENTE donde acaba el silencio. Entre anclas, reparto
    proporcional."""
    pesos = _pesos(texto, False)
    acum = [0.0]
    for w in pesos:
        acum.append(acum[-1] + w)
    t_ini, t_fin = activos[0][0], activos[-1][1]
    fronteras = [(m.start(), m.end()) for m in re.finditer(r"[,;:.?!…»]+[\s«]+(?=\w)", texto)]
    esperado = [_instante(pre, pesos, activos) for pre, _ in fronteras]
    asignado = {}
    for a, b in sorted(silencios, key=lambda s: -(s[1] - s[0])):
        centro = (a + b) / 2
        libres = [j for j in range(len(fronteras)) if j not in asignado
                  and abs(esperado[j] - centro) <= 0.8]
        if not libres:
            continue
        j = min(libres, key=lambda j: abs(esperado[j] - centro))
        antes = [asignado[i] for i in asignado if i < j]
        despues = [asignado[i] for i in asignado if i > j]
        if (antes and max(x[1] for x in antes) > a) or (despues and min(x[0] for x in despues) < b):
            continue                      # rompería el orden
        asignado[j] = (a, b)
    anclas = [(0.0, t_ini)]
    for j in sorted(asignado):
        pre, post = fronteras[j]
        a, b = asignado[j]
        anclas += [(acum[pre], a), (acum[post], b)]
    anclas.append((acum[-1], t_fin))

    def instante(indice):
        w = acum[max(0, min(indice, len(acum) - 1))]
        for (w0, t0), (w1, t1) in zip(anclas, anclas[1:]):
            if w <= w1:
                return t0 if w1 <= w0 else t0 + (t1 - t0) * (w - w0) / (w1 - w0)
        return t_fin
    return instante


def cortes(e, planos, fps, carpeta=None):
    """Para una escena y sus planos, devuelve (usados, n_f):
      · usados: lista de (k, fotograma_de_inicio) con k el índice del plano en
        `planos`, en orden. Si la escena es demasiado corta para todos sus
        planos, sobran los últimos (un plano de medio segundo no se ve).
      · n_f: fotogramas de la escena (los mismos que cuenta render.py).
    """
    dur = float(e.get("duracion_s") or 0)
    n_f = max(1, int(round(dur * fps)))
    if not planos:
        return [], n_f
    caben = max(1, int(dur // MIN_PLANO_S))
    planos = planos[:caben]
    n = len(planos)
    pausa = e.get("pausa_despues_s", PAUSA_POR_DEFECTO)
    pausa = PAUSA_POR_DEFECTO if pausa is None else float(pausa)
    habla = max(0.3, dur - pausa)
    texto = e.get("narracion") or ""
    audio = Path(carpeta) / e["audio"] if (carpeta and e.get("audio")) else None
    if audio is not None and audio.exists():
        activos, silencios = tramos_de_voz(audio, habla)
        instante = mapa_de_tiempo(texto, activos, silencios)
    else:
        pesos = _pesos(texto, True)
        activos = [(0.08, habla)]

        def instante(indice):
            return _instante(indice, pesos, activos)

    t = [0.0] + [None] * (n - 1)
    ultimo = 0
    for k in range(1, n):
        frag = str(planos[k].get("desde") or "").strip()
        if not frag:
            continue
        i = posicion(texto, frag, ultimo)
        if not i:                      # no está, o está al principio (eso es el plano 1)
            continue
        ultimo = i
        t[k] = max(0.0, instante(i) - ANTICIPO_S)

    # Los planos sin «desde» se reparten a partes iguales el hueco entre sus
    # vecinos con instante conocido (o el final de la escena).
    k = 1
    while k < n:
        if t[k] is not None:
            k += 1
            continue
        j = k
        while j < n and t[j] is None:
            j += 1
        izq = t[k - 1]
        der = t[j] if j < n else dur
        huecos = j - k + 1
        for m in range(k, j):
            t[m] = izq + (der - izq) * (m - k + 1) / huecos
        k = j

    # Orden y mínimos: cada plano dura al menos MIN_PLANO_S.
    for k in range(1, n):
        t[k] = max(t[k], t[k - 1] + MIN_PLANO_S)
    fin = dur
    for k in range(n - 1, 0, -1):
        t[k] = min(t[k], fin - MIN_PLANO_S)
        fin = t[k]
    usados = [(0, 0)]
    for k in range(1, n):
        f = int(round(t[k] * fps))
        if f - usados[-1][1] >= int(MIN_PLANO_S * fps * 0.8) and n_f - f >= int(MIN_PLANO_S * fps * 0.8):
            usados.append((k, f))
    return usados, n_f


def palabras_del_plano(texto, planos, usados, fps, dur):
    """Para la hoja de contactos: el trozo de narración que suena durante cada
    plano usado. Si el plano tiene «desde», su trozo empieza exactamente ahí;
    si no, se estima por tiempo (sin audio: la hoja se hace antes de la voz)."""
    pesos = _pesos(texto, True)
    total = sum(pesos) or 1.0
    acum, marcas = 0.0, []
    for w in pesos:
        marcas.append(acum / total)
        acum += w
    habla = max(0.3, dur)
    indices, ultimo = [], 0
    for j, (k, f) in enumerate(usados):
        if j == 0:
            indices.append(0)
            continue
        frag = str(planos[k].get("desde") or "").strip()
        i = posicion(texto, frag, ultimo) if frag else None
        if not i:
            frac = min(1.0, (f / fps + ANTICIPO_S) / habla)
            i = next((m for m, v in enumerate(marcas) if v >= frac), len(texto))
            while 0 < i < len(texto) and texto[i - 1].isalnum():
                i -= 1
        i = max(i, ultimo)
        indices.append(i)
        ultimo = i
    return [texto[indices[j]:(indices[j + 1] if j + 1 < len(indices) else len(texto))].strip()
            for j in range(len(indices))]


# ---------------------------------------------------------------------------
# 2. La línea de tiempo del Short
# ---------------------------------------------------------------------------
def cargar_local(carpeta_build):
    """El `visual/local.json` que deja `visual.py traer`, o None si no hay
    (y entonces el render es el de siempre)."""
    ruta = Path(carpeta_build) / "visual" / "local.json"
    if not ruta.exists():
        return None
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except Exception:
        return None
    return datos if datos.get("escenas") else None


def _partir(tramos, f_corte):
    """Todo lo que quede a partir de `f_corte` pasa a ser tarjeta de marca."""
    salida = []
    for tr in tramos:
        if tr["f1"] <= f_corte:
            salida.append(tr)
        elif tr["f0"] >= f_corte:
            salida.append(dict(tr, tipo="marca", plano=None))
        else:
            salida.append(dict(tr, f1=f_corte))
            salida.append(dict(tr, f0=f_corte, tipo="marca", plano=None))
    return salida


def _fusionar(tramos):
    salida = []
    for tr in tramos:
        if tr["f1"] <= tr["f0"]:
            continue
        if salida and tr["tipo"] == "marca" and salida[-1]["tipo"] == "marca":
            salida[-1]["f1"] = tr["f1"]
        else:
            salida.append(dict(tr))
    return salida


def plan(escenas, local, fps, carpeta_build):
    """Una entrada por escena, en orden:
        {"n", "n_f", "texto_pos", "tramos": [{"f0", "f1", "tipo", "plano"}]}
    con f0/f1 fotogramas RELATIVOS a la escena y tipo «archivo» o «marca».
    """
    salida = []
    por_escena = (local or {}).get("escenas", {})
    for i, e in enumerate(escenas):
        n = e["n"]
        v = por_escena.get(str(n)) or {}
        planos = [p for p in (v.get("planos") or [])]
        n_f = max(1, int(round(float(e["duracion_s"]) * fps)))
        if not planos or e.get("tipo") in TIPOS_SOLO_MARCA:
            tramos = [{"f0": 0, "f1": n_f, "tipo": "marca", "plano": None}]
        else:
            usados, n_f = cortes(e, planos, fps, carpeta_build)
            tramos = []
            for j, (k, f0) in enumerate(usados):
                f1 = usados[j + 1][1] if j + 1 < len(usados) else n_f
                p = planos[k]
                archivo = (bool(p.get("local")) and p.get("tipo") in ("video", "imagen")
                           and _legible(Path(carpeta_build) / p["local"], p.get("tipo")))
                tramos.append({"f0": f0, "f1": f1, "tipo": "archivo" if archivo else "marca",
                               "plano": p if archivo else None})
        if i == len(escenas) - 1 and e.get("tipo") == "cierre":
            tramos = _partir(tramos, max(0, n_f - int(round(REMATE_S * fps))))
        pos = "centro" if e.get("tipo") in TIPOS_CENTRO else (v.get("texto_pos") or "abajo")
        if pos not in ("abajo", "arriba", "centro"):
            pos = "abajo"
        salida.append({"n": n, "n_f": n_f, "texto_pos": pos, "tramos": _fusionar(tramos)})
    return salida


def _legible(fichero, tipo):
    """Un plano que no se puede leer sale como tarjeta de marca, no tumba el
    modo archivo del Short entero."""
    if not fichero.exists() or fichero.stat().st_size < 1024:
        return False
    if tipo == "imagen":
        return True
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height", "-of", "csv=p=0", str(fichero)],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    return r.returncode == 0 and "," in r.stdout


def hay_archivo(plan_):
    return any(tr["tipo"] == "archivo" for pe in plan_ for tr in pe["tramos"])


# ---------------------------------------------------------------------------
# 3. La pista de fondo
# ---------------------------------------------------------------------------
# Todos los trozos salen con el mismo códec, tamaño, cadencia y escala de
# tiempo, para poder unirlos sin recodificar. Calidad casi sin pérdida: el
# vídeo se vuelve a codificar una vez más al componer el texto encima.
_X264 = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "12", "-pix_fmt", "yuv420p",
         "-video_track_timescale", "15360", "-an"]


def _seg_video(fichero, inicio, nf, encuadre, W, H, fps, destino, dur_clip):
    necesita = nf / fps
    if dur_clip and inicio + necesita > dur_clip - 0.05:
        inicio = max(0.0, dur_clip - necesita - 0.05)
    lento = 1.0
    if dur_clip and dur_clip - inicio < necesita:
        # Clip más corto que el plano: se ralentiza un poco (hasta 1,6x) antes
        # que congelar el último fotograma, que es justo el «plano quieto» que
        # no queremos. Lo que aún falte, se congela (tpad).
        lento = min(1.6, necesita / max(0.1, dur_clip - inicio))
    cx = min(1.0, max(0.0, float((encuadre or {}).get("x", 0.5))))
    cy = min(1.0, max(0.0, float((encuadre or {}).get("y", 0.5))))
    vf = ((f"setpts={lento:.4f}*PTS," if lento > 1.001 else "")
          + f"fps={fps},scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
          + f"crop={W}:{H}:(iw-{W})*{cx:.4f}:(ih-{H})*{cy:.4f},setsar=1,"
          + f"tpad=stop_mode=clone:stop_duration={necesita + 1:.2f},format=yuv420p")
    _ffmpeg("-ss", f"{inicio:.3f}", "-i", str(fichero), "-vf", vf,
            "-frames:v", str(nf), "-r", str(fps), *_X264, str(destino))
    if fotogramas(destino) != nf and inicio > 0:
        # Un clip puede pasar ffprobe y no dar fotogramas desde `inicio` (la
        # duración que da la API se pasa, o el fichero está truncado). Se
        # prueba desde el principio antes de dar el plano por perdido.
        _ffmpeg("-i", str(fichero), "-vf", vf, "-frames:v", str(nf), "-r", str(fps),
                *_X264, str(destino))
    if fotogramas(destino) != nf:
        raise RuntimeError(f"{Path(fichero).name}: salen {fotogramas(destino)} fotogramas de {nf}")


def _seg_imagen(fichero, nf, variante, W, H, fps, destino):
    """Imagen fija (generada): nunca quieta. Acercamiento, alejamiento o paneo
    vertical lentos, según el número de plano (determinista, regla 11.5). Se
    trabaja a 2x para que el movimiento no tiemble: zoompan redondea a píxel."""
    Z = 0.09
    modo = variante % 3
    if modo == 0:
        z, x, y = f"1+{Z}*on/{nf}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif modo == 1:
        z, x, y = f"{1 + Z}-{Z}*on/{nf}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    else:
        z, x, y = f"{1 + Z}", "iw/2-(iw/zoom/2)", f"(ih-ih/zoom)*(1-on/{nf})"
    vf = (f"scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase:flags=lanczos,"
          f"crop={W * 2}:{H * 2},"
          f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={fps},setsar=1,format=yuv420p")
    _ffmpeg("-framerate", str(fps), "-loop", "1", "-i", str(fichero), "-vf", vf,
            "-frames:v", str(nf), "-r", str(fps), *_X264, str(destino))
    if fotogramas(destino) != nf:
        raise RuntimeError(f"{Path(fichero).name}: salen {fotogramas(destino)} fotogramas de {nf}")


def fotogramas(fichero):
    """Fotogramas de vídeo que tiene de verdad un fichero (contándolos)."""
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets",
                        "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(fichero)],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    try:
        return int(r.stdout.strip().split(",")[0])
    except ValueError:
        return -1


def _seg_negro(nf, W, H, fps, destino):
    _ffmpeg("-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={fps}",
            "-frames:v", str(nf), "-r", str(fps), *_X264, str(destino))


def pista_de_fondo(plan_, W, H, fps, carpeta_tmp, carpeta_build):
    """El mp4 de fondo del Short entero. En los tramos de marca va negro: ahí
    el fotograma de encima es opaco y lo tapa del todo."""
    carpeta_tmp = Path(carpeta_tmp)
    carpeta_tmp.mkdir(parents=True, exist_ok=True)
    trozos, n = [], 0
    for pe in plan_:
        for tr in pe["tramos"]:
            nf = tr["f1"] - tr["f0"]
            if nf <= 0:
                continue
            destino = carpeta_tmp / f"fondo_{n:03d}.mp4"
            p = tr.get("plano") or {}
            try:
                if tr["tipo"] == "archivo" and p.get("tipo") == "video":
                    _seg_video(Path(carpeta_build) / p["local"], float(p.get("inicio_s") or 0.0), nf,
                               p.get("encuadre"), W, H, fps, destino, float(p.get("duracion_s") or 0.0))
                elif tr["tipo"] == "archivo" and p.get("tipo") == "imagen":
                    _seg_imagen(Path(carpeta_build) / p["local"], nf, n, W, H, fps, destino)
                else:
                    _seg_negro(nf, W, H, fps, destino)
            except Exception as ex:
                if tr["tipo"] != "archivo":
                    raise
                # Un plano que no se deja montar sale como tarjeta de marca: se
                # cambia AQUÍ, en el plan, antes de capturar el texto, así que
                # render.py capturará ese tramo de la página de marca.
                print(f"::warning::C50 · escena {pe['n']}: un plano no se pudo montar ({ex}); "
                      f"sale como tarjeta de marca")
                tr["tipo"], tr["plano"] = "marca", None
                _seg_negro(nf, W, H, fps, destino)
            trozos.append(destino)
            n += 1
    lista = carpeta_tmp / "fondo.txt"
    lista.write_text("".join(f"file '{t.name}'\n" for t in trozos), encoding="utf-8")
    fondo = carpeta_tmp / "fondo.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", lista.name, "-c", "copy", fondo.name],
                       capture_output=True, text=True, cwd=carpeta_tmp, stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        raise RuntimeError(f"no se pudo unir la pista de fondo: {r.stderr[-800:]}")
    return fondo


def usado(plan_, fps):
    """Lo que de verdad salió en el vídeo, para publicar.py (créditos y
    contenido sintético) y para el expediente."""
    planos, t_escena = [], 0
    for pe in plan_:
        for tr in pe["tramos"]:
            if tr["tipo"] != "archivo":
                continue
            p = tr["plano"]
            planos.append({
                "escena": pe["n"], "desde_s": round((t_escena + tr["f0"]) / fps, 2),
                "hasta_s": round((t_escena + tr["f1"]) / fps, 2),
                **{k: p.get(k) for k in ("fuente", "id", "pagina", "autor", "autor_url", "licencia",
                                          "modelo", "prompt", "tipo") if p.get(k) is not None}})
        t_escena += pe["n_f"]
    return {"planos": planos,
            "sintetico": any(p.get("fuente") == "ia" for p in planos)}
