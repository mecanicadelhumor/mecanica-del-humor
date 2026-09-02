#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar_guion.py — portero automático del contrato de guion.

Se ejecuta antes de producir nada. Es barato, es determinista y detecta los
errores que un modelo comete cuando escribe treinta escenas seguidas.

    python3 validar_guion.py ../05_calendario/guiones/MDH-001.es.json

Devuelve código 1 si hay algún error grave: así GitHub Actions se para sola.
"""
import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "05_calendario" / "registro_publicaciones.json"

PPM = 150            # palabras por minuto de la narración
MIN_ESCENA = 2.6
MAX_ESCENA = 20.0    # con la deriva lenta aguanta hasta aquí; más es narrativamente malo
# Bajado de 14.0 a 10.0 el 27/08 (revisión diaria), tras C6.1: sin subtítulos
# quemados, el tramo estático de una escena no anima nada — esto es C6.4 de
# 00_estrategia/PLAN_DE_CAMBIOS.md («escenas más cortas y más numerosas», la
# única vía de movimiento que no toca montaje.py). Medido con render.py sobre
# un par de prueba: una escena de 18,6s captura 30 fotogramas; la misma
# narración partida en dos de ~10s captura 60 — el doble de movimiento por el
# mismo contenido, a cambio de más render (el coste sube con el número de
# escenas, no con el metraje — ver 05_calendario/bitacora/2026-08-27-revision.md).
# Sigue siendo AVISO, no error: no bloquea producción, solo adelanta al guion
# lo que antes solo delataba el vídeo terminado.
MAX_IDEAL = 10.0
MAX_SEGUIDAS = 2     # escenas consecutivas del mismo tipo

# ---------------------------------------------------------------------------
# Los dos formatos del canal.
#
# «largo» es el episodio semanal; «corto» es el Short diario, que es la puerta
# de entrada del canal. Un Short no es un recorte del largo: es una pieza
# entera, con su remate, que tiene que caber en la ventana que YouTube clasifica
# automáticamente como Short (180 s) y —mucho más importante— en la paciencia
# de alguien que está deslizando el dedo.
#
# 55 s no es el límite de YouTube, es el nuestro: por encima de eso el Short
# deja de rematar y empieza a explicar.
# ---------------------------------------------------------------------------
LIMITES = {
    "largo": {"min_s": 200, "max_s": 400, "min_escenas": 12, "max_escenas": 45},
    "corto": {"min_s": 18,  "max_s": 55,  "min_escenas": 3,  "max_escenas": 8},
}

# Fórmulas prohibidas en las primeras 40 palabras. Ninguna es «mala escritura»:
# todas son maneras de PROMETER el contenido en vez de darlo. Más del 55 % de
# los espectadores se va en los primeros 30 segundos cuando la entrada es floja,
# y este canal se juega ahí la mitad de todo.
#
# La lista se amplía. Lo que no se toca es el criterio: si la frase se puede
# borrar y el vídeo sigue entendiéndose, es preámbulo.
APERTURAS_PROHIBIDAS = [
    r"\ben este v[ií]deo\b", r"\bhoy (te |os |vamos a |voy a )?(explico|explicamos|cuento|vemos)\b",
    r"\bvamos a ver\b", r"\bte voy a (contar|explicar|ense[nñ]ar)\b",
    r"\bbienvenid[oa]s?\b", r"\bhola,? (a )?tod[oa]s\b", r"\bqu[ée] tal\b",
    r"\btodo el mundo cree\b", r"\bseguro que (alguna vez|te ha pasado)\b",
    r"\ben el v[ií]deo de hoy\b", r"\bantes de empezar\b",
    r"\bin this video\b", r"\btoday (i'?ll|we'?ll|i am going to)\b",
    r"\bwelcome (back )?to\b", r"\bbefore we (start|begin)\b",
    r"\beveryone (thinks|believes)\b",
]

CAMPOS = {
    "titulo": ["titulo"], "dato": ["cifra", "pie"], "enunciado": ["texto"],
    "lista": ["puntos"], "cita": ["texto", "autor"],
    "comparacion": ["a", "b"], "diagrama": ["pasos"],
    "figura": [], "cierre": ["titulo"],
}
TEXTUALES = ["titulo", "subtitulo", "texto", "cifra", "pie", "a", "b", "et_a", "et_b", "etiqueta"]
# «Episodio 01» o «Parte 3» no son afirmaciones: no exigen fuente.
CON_DATOS = ["subtitulo", "texto", "cifra", "pie", "a", "b"]

# Firma de una narración que se quedó a medias: acaba en dos puntos y una sola
# palabra («…los aviones son incómodos: cero.»), o directamente en dos puntos,
# coma o punto y coma, o colgando de una conjunción. Ver el comentario largo
# de más abajo, donde se usa.
CORTADA = re.compile(r"(:\s*\S+\s*\.?|[:,;]|\b(y|o|pero|and|or|but)\s*\.?)\s*$", re.I)


def dur(e):
    n = len((e.get("narracion") or "").split())
    return max(MIN_ESCENA, n / PPM * 60 + 0.5) + e.get("pausa_despues_s", 0.45)


def texto_pantalla(e):
    partes = [str(e.get(c, "")) for c in TEXTUALES]
    partes += [str(p) for p in e.get("puntos", [])]
    partes += [f"{p.get('titulo','')} {p.get('pie','')}" for p in e.get("pasos", [])]
    return " ".join(partes)


def normal(s):
    # Cada carácter no alfanumérico (incluidos «*» y «_», que son justo los que
    # marcan el resaltado ámbar/cian) se sustituye por un espacio suelto. Sin
    # colapsar los espacios que quedan, «*espacio*» deja dos espacios seguidos
    # alrededor de la palabra y el «pn.strip() in nn» de más abajo deja de
    # encontrar la subcadena exacta aunque el texto sea idéntico al oído. Es
    # decir: el detector de «pantalla = narración» quedaba ciego justo en el
    # caso normal, el de una escena con resaltado. Encontrado el 21/08
    # revisando MDS-001, donde «texto» y «narración» de las escenas 1 y 2 eran
    # literalmente la misma frase y no saltó ni un aviso.
    sin_marcas = re.sub(r"[^a-záéíóúñ0-9 ]", " ", (s or "").lower())
    return re.sub(r"\s+", " ", sin_marcas).strip()


VENTANA_C17_DIAS = 42  # seis semanas


def _fecha_utc(iso):
    """`subido_utc` ('2026-08-29T01:29:00Z') a datetime consciente de zona.
    Nunca lanza: si falta o no se puede leer, devuelve None y esa entrada se
    descarta en `fuentes_recientes` en vez de romper la validación."""
    if not iso:
        return None
    try:
        return datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None


def fuentes_recientes(id_actual, dias=VENTANA_C17_DIAS):
    """Códigos de «fuente» que ya aparecen en los guiones españoles subidos
    en las últimas seis semanas — la red de seguridad de C17 («no
    repetirse», `00_estrategia/PLAN_DE_CAMBIOS.md`).

    Determinista y sin red: lee `registro_publicaciones.json` (lo que YA se
    ha subido, escrito por `registrar.py`) y, de cada entrada dentro de la
    ventana, el guion al que apunta. Devuelve, por código de fuente, en qué
    episodios ya salió y en cuántas escenas de cada uno.

    Esto NO decide qué es «fuente central» — eso exige leer el guion entero
    y lo sigue haciendo quien revisa (paso 1 de la revisión diaria, C17 en
    `REGLAS.md`/`PLAN_DE_CAMBIOS.md`). Es solo el aviso de que hay que
    mirar: mucho más barato que acordarse de memoria de una docena de
    guiones. Por eso es AVISO, nunca error — no para la producción.

    Si falta el registro o un guion referenciado no existe o no es JSON
    válido, esa entrada (o todas) se salta en silencio.
    """
    try:
        reg = json.loads(REGISTRO.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    limite = datetime.now(timezone.utc) - timedelta(days=dias)
    por_fuente = {}
    for p in reg.get("publicaciones", []):
        if p.get("idioma") != "es" or p.get("episodio") == id_actual:
            continue
        fecha = _fecha_utc(p.get("subido_utc"))
        if not fecha or fecha < limite:
            continue
        ruta_guion = p.get("guion")
        if not ruta_guion:
            continue
        try:
            gp = json.loads((RAIZ / ruta_guion).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        cuenta = Counter(e["fuente"] for e in gp.get("escenas", []) if e.get("fuente"))
        for f, n in cuenta.items():
            por_fuente.setdefault(f, []).append((p["episodio"], n))
    return por_fuente


def validar(path):
    g = json.loads(Path(path).read_text(encoding="utf-8"))
    errores, avisos = [], []
    formato = g.get("formato", "largo")
    if formato not in LIMITES:
        errores.append(f"«formato» debe ser «largo» o «corto», no «{formato}».")
        formato = "largo"
    L = LIMITES[formato]
    corto = formato == "corto"

    if g.get("bloqueos"):
        errores.append(f"El guion trae bloqueos sin resolver: {g['bloqueos']}")
    if not g.get("tesis"):
        errores.append("Falta la tesis: el guion no sabe qué quiere que el espectador se lleve.")

    escenas = g["escenas"]
    total = 0.0
    tipos = []

    for i, e in enumerate(escenas, 1):
        t = e.get("tipo")
        tipos.append(t)
        d = dur(e)
        total += d

        for campo in CAMPOS.get(t, []):
            if not e.get(campo):
                errores.append(f"Escena {i} ({t}): falta el campo obligatorio «{campo}».")

        # En un Short ninguna escena puede pasar de 12 s: con seis escenas y
        # 55 s de techo, una de 20 s se come el vídeo entero.
        tope = 12.0 if corto else MAX_ESCENA
        if d > tope:
            errores.append(f"Escena {i}: dura {d:.1f}s. Máximo {tope}s — pártela en dos.")
        elif not corto and d > MAX_IDEAL:
            avisos.append(f"Escena {i}: {d:.1f}s. Por encima de {MAX_IDEAL}s la pantalla se queda quieta.")

        pantalla = texto_pantalla(e)
        afirmaciones = " ".join(str(e.get(c, "")) for c in CON_DATOS) + \
                       " " + " ".join(str(p) for p in e.get("puntos", []))
        # cifra en pantalla sin fuente
        if re.search(r"\d", afirmaciones) and not e.get("fuente"):
            errores.append(f"Escena {i}: hay una cifra en pantalla sin campo «fuente».")

        # resaltado ámbar: uno por escena
        n_amb = len(re.findall(r"\*[^*]+\*", pantalla))
        if n_amb > 1:
            avisos.append(f"Escena {i}: {n_amb} resaltados en ámbar. Debe haber uno como máximo.")
        if pantalla.count("*") % 2 or pantalla.count("_") % 2:
            avisos.append(f"Escena {i}: marca de resaltado sin cerrar.")

        # la pantalla no repite la narración
        pn, nn = normal(pantalla), normal(e.get("narracion", ""))
        if len(pn.split()) >= 5 and pn.strip() and pn.strip() in nn:
            avisos.append(f"Escena {i}: el texto en pantalla es literal de la narración. "
                          f"El ojo y el oído deben recibir cosas distintas.")

        # narración cortada a media frase
        #
        # De dónde sale esto: la escena 24 de MDH-002 se produjo con la
        # narración «La misma queja, dos versiones. "Los aviones son
        # incómodos": cero.» y ahí se acababa. El chiste —el remate entero de
        # la escena— estaba escrito en el panel de pantalla pero no en la
        # narración, así que la voz dijo «cero» y se calló. El guion inglés
        # traía el mismo corte. Nadie lo detectó hasta que Silvestre lo oyó.
        #
        # La regla que hay detrás es de Silvestre y vale para todo el canal:
        # **el audio tiene que ser autosuficiente**, porque mucha gente ve
        # YouTube sin mirar la pantalla. Lo que está en pantalla y no se dice,
        # para esa gente no existe.
        #
        # Esto NO comprueba esa regla —comprobarla de verdad exige entender el
        # guion, y por eso la revisión diaria lee los guiones enteros—. Lo que
        # detecta es la *firma* de una narración truncada: que acabe en dos
        # puntos y una palabra suelta, o colgando de una conjunción. Probado
        # contra los doce guiones del repositorio: cero falsos positivos y
        # pilla las dos escenas 24.
        #
        # Es error y no aviso a propósito: parar una producción se arregla
        # relanzándola; publicar un vídeo con un remate mudo, no. Si algún día
        # molesta, bajarlo a «avisos» es cambiar una palabra en la línea de
        # abajo.
        narr = (e.get("narracion") or "").strip()
        if narr and CORTADA.search(narr):
            errores.append(f"Escena {i}: la narración parece cortada a media frase "
                           f"(«…{narr[-40:]}»). Lo que no se dice, quien escucha sin "
                           f"mirar la pantalla no lo recibe.")

        # Una escena «figura» necesita o los datos (y figura.py hará el PNG
        # antes del render) o una imagen ya puesta a mano. Sin ninguna de las
        # dos sale un hueco en pantalla.
        if t == "figura" and not e.get("figura") and not e.get("imagen"):
            errores.append(f"Escena {i} (figura): necesita «figura» con los datos "
                           f"o «imagen» con una ruta. No tiene ninguna de las dos.")

        if t == "lista" and len(e.get("puntos", [])) > 5:
            errores.append(f"Escena {i}: una lista de más de 5 puntos no se lee en pantalla.")
        if t == "diagrama" and len(e.get("pasos", [])) > 5:
            errores.append(f"Escena {i}: un diagrama de más de 5 pasos no se lee.")

    # tipos repetidos seguidos
    racha, anterior = 1, None
    for i, t in enumerate(tipos, 1):
        racha = racha + 1 if t == anterior else 1
        if racha > MAX_SEGUIDAS:
            avisos.append(f"Escena {i}: {racha} escenas «{t}» seguidas. Rompe el ritmo visual.")
        anterior = t

    # ---------------------------------------------------------------------
    # EL GANCHO. Los primeros quince segundos.
    #
    # Regla del canal: el vídeo abre con LA COSA, no con la promesa de la cosa.
    # Un chiste, una escena concreta, o una pregunta que el espectador conteste
    # en su cabeza antes de que acabe la frase. Nunca «en este vídeo vamos a».
    # ---------------------------------------------------------------------
    if escenas:
        arranque = " ".join((escenas[0].get("narracion") or "").split()[:40]).lower()
        for patron in APERTURAS_PROHIBIDAS:
            if re.search(patron, arranque):
                errores.append(
                    f"Escena 1: el vídeo abre prometiendo contenido en vez de darlo "
                    f"(«{re.search(patron, arranque).group(0)}»). Abre con el chiste, "
                    f"con una escena concreta o con una pregunta.")
                break
        # Un rótulo de título por delante es el mismo preámbulo, en imagen.
        if corto and escenas[0].get("tipo") == "titulo":
            errores.append("Escena 1: un Short no empieza con un rótulo de título. "
                           "Los tres primeros segundos deciden si te deslizan.")
        if not corto and escenas[0].get("tipo") == "titulo" and dur(escenas[0]) > 8:
            avisos.append(f"Escena 1: {dur(escenas[0]):.1f}s de rótulo antes de empezar. "
                          f"Por encima de 8s es una portada, no un gancho.")

    # estructura
    if tipos and tipos[-1] != "cierre":
        errores.append("La última escena debe ser de tipo «cierre».")

    # ---------------------------------------------------------------------
    # Reglas propias del Short
    # ---------------------------------------------------------------------
    if corto:
        if not g.get("serie"):
            avisos.append("El Short no declara «serie». Las series con nombre son lo que "
                          "hace que alguien vuelva; la campanita ya no basta.")
        if not any(e.get("personaje") for e in escenas):
            avisos.append("Ninguna escena usa el personaje. En vertical es lo único que "
                          "reacciona, y la reacción es la mitad del remate.")
        # El remate: la última escena tiene que decir algo, no solo rotular.
        ultima = escenas[-1] if escenas else {}
        if len((ultima.get("narracion") or "").split()) < 6:
            errores.append("El Short no remata: la última escena apenas tiene narración. "
                           "Un Short sin remate es un recorte.")

    # duración total y número de escenas
    m, s = divmod(total, 60)
    if not L["min_escenas"] <= len(escenas) <= L["max_escenas"]:
        errores.append(f"{len(escenas)} escenas para formato «{formato}»: "
                       f"el rango es {L['min_escenas']}–{L['max_escenas']}.")
    if total < L["min_s"]:
        avisos.append(f"Dura {int(m)}m{s:04.1f}s: corto para el formato «{formato}» "
                      f"(mínimo {L['min_s']}s).")
    if total > L["max_s"]:
        errores.append(f"Dura {int(m)}m{s:04.1f}s: pasa del máximo del formato "
                       f"«{formato}» ({L['max_s']}s). Recorta.")

    # densidad de humor: el chistólogo debe haber dejado sus notas
    if not g.get("notas_humor"):
        avisos.append("No hay «notas_humor»: el chistólogo no ha pasado por aquí.")

    reparto = Counter(tipos)
    dominante, n_dom = reparto.most_common(1)[0]
    # En un Short de seis escenas, cuatro «enunciado» no son monotonía: son el
    # formato. La regla de variedad visual es del episodio largo.
    if not corto and n_dom / len(tipos) > 0.45:
        avisos.append(f"El {n_dom*100//len(tipos)}% de las escenas son «{dominante}». "
                      f"Demasiada monotonía visual.")

    # C17 — aviso de repetición de fuente contra el corpus producido en las
    # últimas seis semanas (ver fuentes_recientes más arriba).
    fuentes = sorted({e["fuente"] for e in escenas if e.get("fuente")})
    if fuentes and g.get("id"):
        recientes = fuentes_recientes(g["id"])
        for f in fuentes:
            usos = recientes.get(f)
            if usos:
                donde = ", ".join(f"{ep} ({n} esc.)" for ep, n in usos)
                avisos.append(f"C17: la fuente «{f}» ya aparece en {donde} "
                              f"(producido en las últimas seis semanas). Si allí también "
                              f"sostenía la tesis y no era un apoyo de pasada, es una "
                              f"repetición — revisar con el criterio del paso 1 antes de producir.")

    print(f"\n{path}")
    print(f"  [{formato}] {len(escenas)} escenas · {int(m)}m {s:04.1f}s · reparto {dict(reparto)}")
    print(f"  fuentes citadas: {', '.join(fuentes) or 'ninguna'}")
    if avisos:
        print(f"\n  AVISOS ({len(avisos)})")
        for a in avisos:
            print(f"    · {a}")
    if errores:
        print(f"\n  ERRORES ({len(errores)})")
        for x in errores:
            print(f"    ✗ {x}")
    else:
        print("\n  Sin errores graves.")
    return len(errores)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("guiones", nargs="+")
    a = ap.parse_args()
    fallos = sum(validar(p) for p in a.guiones)
    sys.exit(1 if fallos else 0)
