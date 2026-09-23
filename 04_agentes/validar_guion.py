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
import unicodedata
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "05_calendario" / "registro_publicaciones.json"

# PPM · palabras por minuto de la narración.
#
# Fue 150 desde agosto, cuando la voz la ponía `edge-tts`. Gemini lee más
# despacio, y eso llevaba un mes escrito como pendiente sin arreglar. Medido el
# 18/09/2026 sobre los seis Shorts con `duracion_final_s` en su expediente de
# calidad, descontando las pausas deterministas de `pausa_despues_s`:
#
#   MDS-015 (edge-tts)  157 ppm      MDS-018  141 ppm
#   MDS-016             117 ppm      MDS-019  141 ppm
#   MDS-017             126 ppm      MDS-020  127 ppm
#
# Media de los cinco de Gemini: 130. Con 150 el validador daba 49 s para un
# vídeo que salió de 58 s (MDS-016), es decir, dejaba pasar por debajo del
# techo de 55 s guiones que se publican por encima. 130 no acierta al segundo
# —la dispersión real es de ±10 %— pero deja de mentir en la misma dirección
# siempre, que es lo que importa para un techo.
PPM = 130
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
# C38 (18/09/2026) · La duración de la serie deja de ser decorativa
#
# `guionista_corto.md` le da a cada serie una duración desde agosto. Nunca se ha
# cumplido ni una vez. Medido sobre los veinticinco Shorts del repositorio:
#
#   · la duración declarada de la serie va de 30 a 45 s,
#   · y los veinticinco guiones tienen entre 88 y 120 palabras, media 108,
#   · con excesos que van del 8 % (cuando la serie dice 45) al 98 % (cuando
#     dice 30). Las seis de «Ríete primero, te explico después» —serie de
#     30 s— tienen 101, 103, 106, 111, 111 y 113 palabras.
#
# Lo constante no es la serie: son las 108 palabras. Es decir, **el máximo del
# formato (55 s) se ha usado como objetivo**, y todo lo que sobra entre el
# remate y el cierre honesto es relleno para llegar ahí. Es la trampa 20 del
# proyecto —un mínimo escrito como suelo se usa como techo— vista por el otro
# lado: un máximo escrito como techo se usa como objetivo.
#
# Y es lo que el codirector describió dos días seguidos (16 y 17/09) como «me
# cuesta seguir el hilo» y «forzado entre el nudo y el desenlace»: entre los dos
# no hay nada que seguir, hay metraje.
#
# ERROR, no aviso, y con una tolerancia estrecha a propósito: con margen ancho
# el guionista escribe al borde del margen, que es exactamente lo que ha pasado
# con el techo de 55 s durante veinticinco Shorts.
#
# ── ANULADO COMO ERROR EL 23/09/2026 (C48, versión 12 del plan) ──────────────
# Pasa a ser AVISO. Lo que produjo en la práctica: los cinco Shorts de la
# semana del 21 se reescribieron para caber en la serie «sin añadir ni una
# afirmación, solo quitando y recolocando», y lo que se quitó fue justo lo que
# cosía una escena con la siguiente. El codirector los leyó tres días seguidos
# como «una sucesión de mensajes inconexos» (MDS-021, 022 y 023). El techo de
# 55 s sigue siendo ERROR; el número de la serie queda como referencia. Contra
# el relleno —que era el problema real de agosto— la protección ya no es un
# reloj: es la lectura en frío (C48, más abajo), que pregunta qué frase sobra.
# ---------------------------------------------------------------------------
# Los números de agosto eran 40 / 30 / 45 / 35 / 40. Dos suben hoy, y conviene
# decir por qué antes de que parezca que se mueve la portería:
#
#   · «Ríete primero, te explico después» pasa de 30 a 35 s, y «Esto no tiene
#     gracia y esto sí» de 35 a 40. Los dos números de agosto se escribieron
#     ANTES de que la regla 12 —cada vídeo termina diciendo dónde falla— se
#     extendiera a los Shorts. Un Short de este canal tiene que meter, como
#     mínimo: planteamiento (que ahora además tiene que llegar al segundo 10),
#     remate, el hallazgo con su fuente y el cierre honesto. Medido al escribir
#     los cinco de la semana del 21, eso no baja de 66 palabras ≈ 35 s. Un 30
#     que es aritméticamente imposible no es exigente: es un número que se
#     ignora, que es exactamente lo que llevaba pasando.
#   · Los otros tres no se tocan.
#
# Un 35 que se cumple es más estricto que un 30 que nadie ha cumplido nunca.
DURACION_SERIE_S = {
    "Desmonta el chiste": 40,
    "Ríete primero, te explico después": 35,
    "El experimento": 45,
    "Esto no tiene gracia y esto sí": 40,
    "Diagnósticos": 40,
}
TOLERANCIA_SERIE = 0.12

# C48 (23/09/2026): primer Short al que se le exigen «historia» y
# «lectura_en_frio». Los anteriores ya están escritos o publicados; MDS-023,
# 024 y 025, reescritos por la dirección el 23/09, llevan «historia» pero su
# lectura la hizo el codirector en la conversación, no un subagente.
PRIMER_SHORT_C48 = 26

# C50 (versión 13, 23/09/2026): primer Short al que se le pide «visual» en
# cada escena. MDS-024 y MDS-025 lo llevan ya (lo escribió la dirección).
# Solo AVISO: una escena sin imagen sale como tarjeta de marca, y eso no
# puede parar una producción.
PRIMER_SHORT_C50 = 26
MAX_PLANOS_ESCENA = 4
MAX_TARJETAS_MARCA = 2

# La pausa por encima de la cual `guionista_corto.md` dice que «la pausa es el
# chiste» y la escena siguiente es el remate. Mismo umbral que usa voz.py para
# dirigir al actor (PAUSA_DE_REMATE_S): un solo número para las dos piezas.
PAUSA_DE_REMATE_S = 1.2

# El segundo en el que la mitad de la audiencia se ha ido, medido en la curva de
# retención de MDS-011 y MDS-015 (las dos únicas con curva). El remate no puede
# caer antes: si cae antes, quien se queda a partir de ahí ya no tiene nada por
# lo que quedarse. MDS-016 —1.280 visualizaciones, el único del canal por encima
# de 1.000— lo pone en el segundo 13. Los tres siguientes lo ponen en el 6, el 7
# y el 6, y ninguno pasó de 200.
SEGUNDO_DEL_ACANTILADO = 10.0

# Las dos comprobaciones de arriba son ERROR, y `producir.yml` (paso «Validar
# guiones», línea 190) para la producción con un error. Los veinticuatro Shorts
# escritos antes de hoy las incumplen —ese es justamente el hallazgo— y de ellos
# solo uno está pendiente de producirse: MDS-017, mañana sábado.
#
# Reescribirlo la víspera cuesta sus seis peticiones de voz (las cuatro que ya
# tiene en `cache_voz/` desde el 15/09 se perderían al cambiar la narración),
# vuelve a meter mano a un guion ya revisado dos veces, y lo que se gana dura un
# día. Así que va exento, y la exención vive AQUÍ y no en el guion: conceder otra
# obliga a tocar el código, que es la fricción que le corresponde. Es la trampa 9
# —una comprobación que puede parar algo tiene que mirar qué se lleva por
# delante— atendida antes de que pase, no después.
EXENTOS_C38 = {
    "MDS-017": "se publica el 19/09/2026, ya renderizado y con la voz en caché "
               "desde el 15/09. Exención única concedida el 18/09/2026.",
}

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
    r"\bbienvenid[oa]s?\b", r"\bhola,? (a )?tod[oa]s\b",
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
# C19+C16 (07/09): los ocho dibujos de 02_marca/iconos.svg, embebidos también
# en escena.html (ICONOS). Mantener las tres listas sincronizadas a mano.
ICONOS_VALIDOS = ["i-bisagra", "i-muelle", "i-ruptura", "i-bocadillos",
                  "i-pausa", "i-grieta", "i-publico", "i-balanza"]

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


# ---------------------------------------------------------------------------
# C28 · el detalle concreto se dice con la misma palabra (12/09/2026)
#
# De dónde sale: MDS-014 (10/09) puso «lo jovial que estabas el MARTES» en
# pantalla mientras la voz de esa escena decía «lo jovial que estás HOY», y
# dos escenas antes había dicho «lo repetí el DOMINGO». Tres días para una
# sola idea y ninguno explicado. La dirección lo leyó como lo que es: «hace
# mención a martes pero luego no se explica en ningún caso nada acerca del
# martes».
#
# La regla 14.1 ya prohibía que la pantalla introdujera un dato que la voz no
# dice. Lo que no cubría es este caso, que es peor de detectar a ojo: el dato
# SÍ está en las dos partes, pero con dos palabras distintas, y el espectador
# se queda buscando la escena donde se explique la que ha leído.
#
# Por qué solo días y meses, y no «toda palabra de contenido» como decía el
# encargo original de C22: se midieron las dos variantes contra los 302
# guiones del repositorio el 12/09. La versión amplia (toda palabra de cuatro
# letras o más, comparada por raíz) señala el 73,5 % de las escenas — es
# ruido, no una comprobación, y por eso el encargo llevaba tres semanas sin
# poder escribirse. La versión estrecha señala el 1,0 %: tres escenas, las
# tres reales (MDS-014 «martes», MDH-006 escena 3 «marzo» en pantalla una
# escena antes de que lo diga la voz, y MDH-003 escena 19 «el lunes» como
# idiotismo que nadie pronuncia). Cero falsos positivos.
#
# La rama de números se probó y se descartó en la misma medición: «50 años»
# en pantalla contra «cincuenta años» en la voz, o «2003» contra «dos mil
# tres», son el mismo dato bien escrito, y separarlos del defecto de verdad
# exigiría un analizador de numerales castellanos. Cinco falsos positivos y
# ningún acierto: fuera.
#
# Es ERROR y no aviso: a diferencia del marcado en la narración —que voz.py
# sanea solo—, aquí no hay nada aguas abajo que lo arregle. Si llega al
# render, llega al público.
# ---------------------------------------------------------------------------
DIAS_SEMANA = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado",
               "domingo"}
MESES = {"enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"}
# «Parte 2», «Episodio 06» y «Capítulo 3» son rótulos de sección: nunca se
# dicen en voz alta y no son un dato del que el espectador espere explicación.
ROTULO_SECCION = re.compile(r"\b(parte|episodio|cap[ií]tulo)\s*\d+", re.IGNORECASE)


def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower())
                   if unicodedata.category(c) != "Mn")


def palabras(s):
    return re.findall(r"[a-z0-9]+", sin_acentos(s))


def aparece(fragmento, texto):
    """C50: ¿está `fragmento` en `texto`, a principio de palabra, sin mirar
    tildes, mayúsculas ni signos? Lo mismo que busca fondo_visual.posicion()
    en el render, para que lo que aquí pasa allí se encuentre."""
    f = " ".join(palabras(fragmento))
    t = " " + " ".join(palabras(texto)) + " "
    return bool(f) and (" " + f) in t


VENTANA_C17_DIAS = 42  # seis semanas


def _inicio_cierre(g, n=3):
    """C48.1: las `n` primeras palabras (normalizadas) de la narración y del
    título de la última escena, si es un «cierre». (None, None) si no lo hay."""
    esc = g.get("escenas") or []
    if not esc or esc[-1].get("tipo") != "cierre":
        return (None, None)
    def ini(texto):
        w = palabras(re.sub(r"[*_]", " ", texto or ""))[:n]
        return " ".join(w) if len(w) == n else None
    return (ini(esc[-1].get("narracion")), ini(esc[-1].get("titulo")))


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

        # C19+C16 (07/09): «icono» solo admite los ocho dibujos de
        # 02_marca/iconos.svg — un id que no esté en la lista no se dibuja
        # (iconoHTML() de escena.html lo ignora en silencio), así que aquí
        # se avisa en vez de fallar en render.py, que nunca lo vería.
        if e.get("icono") and e["icono"] not in ICONOS_VALIDOS:
            avisos.append(f"Escena {i}: «icono: {e['icono']}» no es uno de los ocho "
                           f"iconos de 02_marca/iconos.svg ({', '.join(ICONOS_VALIDOS)}). "
                           f"No se dibuja nada.")

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

        # El resaltado es de PANTALLA. En «narracion» se oye.
        #
        # MDS-011 (07/09/2026) se publicó diciendo en voz alta «guion bajo
        # pensamiento divergente guion bajo»: el guion traía
        # «_pensamiento divergente_» dentro de la narración, y el sintetizador
        # lee lo que le llega. `*ámbar*` y `_cian_` los interpreta `rico()` en
        # escena.html sobre «texto», «cifra», «titulo», «pie»...; sobre la
        # narración no los interpreta nadie.
        #
        # Es AVISO y no error a propósito: `voz.py` ya quita el marcado antes
        # de sintetizar, así que el defecto no puede volver a llegar al
        # público. Pararle la producción a un guion por algo que el pipeline
        # arregla solo sería cambiar un vídeo publicado con un fallo por un
        # día sin vídeo, que es peor. Esto está aquí para que el guionista
        # deje de escribirlo, no para bloquear.
        marcas_en_voz = sorted(set(re.findall(r"[*_`#\[\]|~]", e.get("narracion", ""))))
        if marcas_en_voz:
            avisos.append(f"Escena {i}: la narración lleva marcado de pantalla "
                          f"({' '.join(marcas_en_voz)}). El resaltado va en «texto», "
                          f"«cifra», «titulo» o «pie», nunca en «narracion»: ahí el "
                          f"sintetizador lo lee en voz alta. voz.py lo quita antes de "
                          f"sintetizar, pero el guion está mal escrito.")

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
        # traía el mismo corte. Nadie lo detectó hasta que el codirector lo oyó.
        #
        # La regla que hay detrás es del codirector y vale para todo el canal:
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

        # C28 · un día o un mes en pantalla se dice en la voz de ESA escena.
        # Ver el bloque de comentario de DIAS_SEMANA, arriba, para el caso
        # que lo escribió (MDS-014, 10/09/2026) y para por qué la versión
        # amplia de esta comprobación no se puede escribir.
        dichas = set(palabras(e.get("narracion", "")))
        vistas = palabras(ROTULO_SECCION.sub(" ", pantalla))
        huerfanas = sorted({w for w in vistas
                            if (w in DIAS_SEMANA or w in MESES) and w not in dichas})
        if huerfanas:
            errores.append(
                f"Escena {i} (C28): en pantalla pone "
                f"{', '.join('«' + w + '»' for w in huerfanas)} y la narración de esta "
                f"escena no lo dice. Un día o un mes en pantalla es un dato: quien mira "
                f"sin sonido lo lee y busca dónde se explica. Dilo con esa misma palabra "
                f"en la narración de esta escena, o quítalo de la pantalla.")

        # C29 · en formato largo, un paso de «diagrama» es una etiqueta, no
        # una frase. La rama horizontal de escena.html reparte 1840px entre
        # los pasos y descuenta 80px: con tres pasos la caja mide 533px y el
        # título va a 46px, donde caben cinco o seis palabras cortas.
        # ajustarTextoSVG() encoge hasta que quepa (12/09), pero encoger es
        # el remedio, no el sitio donde se arregla: MDH-006 escena 22 salió
        # publicada con «Espera a que lo abra el otro», 604px en 533.
        # Aviso y no error: el motor ya garantiza que quepa.
        if t == "diagrama" and not corto:
            n_pasos = max(1, len(e.get("pasos", [])))
            tope_pal = 6 if n_pasos <= 3 else (4 if n_pasos == 4 else 3)
            for j, p in enumerate(e.get("pasos", []), 1):
                n_pal = len((p.get("titulo") or "").split())
                if n_pal > tope_pal:
                    avisos.append(
                        f"Escena {i}, paso {j} (C29): «{p.get('titulo')}» son {n_pal} "
                        f"palabras y con {n_pasos} pasos caben {tope_pal}. El motor lo "
                        f"encogerá para que quepa, pero un paso de diagrama es una "
                        f"etiqueta: el matiz va en su «pie», que aguanta más.")

    # tipos repetidos seguidos.
    #
    # C38 (18/09/2026): en un Short la apertura son planteamiento, planteamiento
    # y remate, y las tres son «enunciado» por naturaleza — es la forma que
    # tiene MDS-016, el único vídeo del canal por encima de 1.000
    # visualizaciones. Con el tope en 2 este aviso saltaría en todos los Shorts
    # bien escritos, y un aviso que salta siempre se deja de leer. En el
    # episodio largo, donde la variedad visual sí es el problema, sigue en 2.
    seguidas_max = 3 if corto else MAX_SEGUIDAS
    racha, anterior = 1, None
    for i, t in enumerate(tipos, 1):
        racha = racha + 1 if t == anterior else 1
        if racha > seguidas_max:
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
        # «¿Qué tal?» solo es un saludo en las primeras palabras. Más adentro es
        # otra cosa («cuando te preguntan qué tal, sonríes»): falso positivo que
        # paró MDS-023 el 23/09/2026 en su reescritura. Por eso va aparte.
        saludo = re.match(r"^\W*(hola\W+)?qu[ée] tal\b", arranque)
        if saludo:
            errores.append(
                f"Escena 1: el vídeo abre con un saludo («{saludo.group(0).strip()}»). "
                f"Abre con el chiste, con una escena concreta o con una pregunta.")
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
        # C19 (07/09): la escena 1 de un Short deja de poder ser una tarjeta
        # de texto sobre fondo. Tres salidas válidas: «icono» (el vocabulario
        # dibujado de 02_marca/iconos.svg), «personaje» (el Engranaje
        # haciendo algo) o tipo «comparacion». Aviso, no error: el campo
        # «icono» es de hoy mismo y los guiones escritos antes de hoy no
        # pueden tenerlo. A partir de la planificación del jueves 10 sí debe
        # cumplirse siempre.
        e1 = escenas[0]
        if corto and not e1.get("icono") and not e1.get("personaje") and e1.get("tipo") != "comparacion":
            avisos.append("Escena 1 (C19, 07/09): sin «icono», sin «personaje» y sin ser "
                          "«comparacion», es una tarjeta de texto sobre fondo. El 72% de "
                          "las escenas de once Shorts ya son así — usa uno de los ocho "
                          "iconos de 02_marca/iconos.svg, con cuatro palabras o menos.")
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

        # -----------------------------------------------------------------
        # C38.1 · la duración de la serie
        # -----------------------------------------------------------------
        exento = EXENTOS_C38.get(str(g.get("id") or "").split(".")[0])
        if exento:
            avisos.append(f"C38: este guion está EXENTO de las comprobaciones de duración "
                          f"y de posición del remate — {exento}")
        objetivo = DURACION_SERIE_S.get(g.get("serie") or "")
        if objetivo:
            margen = objetivo * TOLERANCIA_SERIE
            if total > objetivo + margen and not exento:
                # C48 (23/09/2026): AVISO, ya no ERROR. Ver la cabecera de C38.
                avisos.append(
                    f"Dura {total:.0f}s y la referencia de la serie «{g['serie']}» son "
                    f"{objetivo}s. No es un error: la duración la decide la historia, y el "
                    f"techo son {LIMITES['corto']['max_s']}s. Pero pregúntale a la lectura en "
                    f"frío qué frase sobra, y si nombra una, quítala. Lo que NO se quita "
                    f"nunca es la frase que une una escena con la siguiente.")
            elif total < objetivo - margen:
                avisos.append(
                    f"Dura {total:.0f}s y la serie «{g['serie']}» son {objetivo}s. "
                    f"Corto no es malo, pero comprueba que el cierre honesto sigue "
                    f"entero: es lo que no se recorta.")

        # -----------------------------------------------------------------
        # C38.2 · dónde cae el remate
        #
        # El remate se detecta igual que en voz.py: es la escena que viene
        # después de una pausa de «la pausa es el chiste». Medido sobre los
        # 25 Shorts del repositorio, la detección no falla ninguna.
        # -----------------------------------------------------------------
        t_acum = 0.0
        remate_en = None
        for j, e in enumerate(escenas, 1):
            if j > 1 and float(escenas[j-2].get("pausa_despues_s") or 0.0) >= PAUSA_DE_REMATE_S:
                remate_en = t_acum
                break
            t_acum += dur(e)
        if remate_en is None:
            avisos.append(
                "Ninguna escena va precedida de una pausa de remate (≥"
                f"{PAUSA_DE_REMATE_S}s). Sin esa pausa el sintetizador no sabe que "
                "viene un remate y lo lee de corrido (voz.py, C33).")
        elif remate_en < SEGUNDO_DEL_ACANTILADO and not exento:
            # C48 (23/09/2026): AVISO, ya no ERROR. Obligar a estirar el
            # planteamiento hasta el segundo 10 produjo planteamientos a trozos
            # («Obligatoria. Y fui.», «Cuarenta minutos así.»). La idea sigue en
            # pie —no gastes lo mejor en el segundo 6—, pero como consejo.
            avisos.append(
                f"El remate cae en el segundo {remate_en:.0f}. La mitad de la audiencia "
                f"se va sobre el segundo {SEGUNDO_DEL_ACANTILADO:.0f}, así que un remate "
                f"antes de ahí se gasta en gente que se iba a quedar igual, y a partir "
                f"del {SEGUNDO_DEL_ACANTILADO:.0f} no queda nada. Alarga el planteamiento "
                f"o mueve la pausa una escena más adelante.")

        # -----------------------------------------------------------------
        # C48 · LA HISTORIA Y LA LECTURA EN FRÍO (23/09/2026)
        #
        # El 21, el 22 y el 23 de septiembre se publicaron tres Shorts que
        # pasaban este validador sin un error y que el codirector describió
        # como «una sucesión de mensajes inconexos, sin sentido, que huelen a
        # AI slop de lejos». Todo lo que este fichero comprueba es forma:
        # duraciones, campos, marcas, días de la semana. Ninguna línea de aquí
        # puede saber si alguien que no sabe nada sigue la historia — y quien
        # escribe el guion es el único lector que NUNCA puede comprobarlo,
        # porque ya sabe lo que quería decir («y a nadie a las ocho» se
        # entiende perfectamente si has escrito las cuatro escenas de antes).
        #
        # Lo que sí se puede comprobar aquí es que esa lectura SE HIZO y que
        # dijo que sí. Dos campos, obligatorios desde MDS-026 (el primero que
        # escribe la planificación con las reglas nuevas):
        #
        #   · «historia»: pregunta, respuesta y puente, en una frase cada uno.
        #     Si quien escribe no puede rellenarlos, el Short no tiene hilo.
        #   · «lectura_en_frio»: lo que contestó un lector que SOLO vio las
        #     narraciones y los textos de pantalla (un subagente sin contexto;
        #     ver guionista_corto.md). Veredicto «pasa» y ninguna frase que no
        #     entendiera.
        #
        # Es ERROR: un Short que no ha pasado la lectura en frío no se produce.
        # Parar un día cuesta un día; publicar un guion sin hilo cuesta la
        # confianza de quien lo ve, y eso es lo que decide el 15 de noviembre.
        # -----------------------------------------------------------------
        num = re.match(r"^MDS-(\d{3})", str(g.get("id") or ""))
        if num and int(num.group(1)) >= PRIMER_SHORT_C48:
            h = g.get("historia") or {}
            faltan = [k for k in ("pregunta", "respuesta", "puente")
                      if not str(h.get(k) or "").strip()]
            if faltan:
                errores.append(
                    f"C48: falta «historia» ({', '.join(faltan)}). Una frase cada uno: "
                    f"qué pregunta responde el Short, qué responde, y qué escena une el "
                    f"chiste con el estudio. Si no se puede escribir, el guion no tiene hilo.")
            lf = g.get("lectura_en_frio") or {}
            if not lf:
                errores.append(
                    "C48: falta «lectura_en_frio». Un Short no se produce sin que alguien "
                    "que solo ha visto las narraciones y los textos de pantalla haya "
                    "contado de qué va (guionista_corto.md, «La lectura en frío»).")
            else:
                if str(lf.get("veredicto") or "").strip().lower() != "pasa":
                    errores.append(
                        f"C48: la lectura en frío dice «{lf.get('veredicto')}». Solo se "
                        f"produce con «pasa».")
                if lf.get("frases_que_no_se_entienden"):
                    errores.append(
                        f"C48: la lectura en frío no entendió: "
                        f"{lf['frases_que_no_se_entienden']}. Reescríbelas y vuelve a "
                        f"pasar la lectura con un lector nuevo.")
                for k in ("lector", "de_que_va"):
                    if not str(lf.get(k) or "").strip():
                        errores.append(f"C48: «lectura_en_frio» no trae «{k}».")

        # -----------------------------------------------------------------
        # C48.1 · NINGUNA FÓRMULA DOS VECES SEGUIDAS (23/09/2026)
        #
        # El codirector, al leer los tres Shorts reescritos: «se entienden
        # mejor, pero ¿por qué todos tienen "y aquí falla"? ¿No hay más formas
        # de terminar un Short?». Los 25 publicados hasta el 22/09 cerraban
        # así. El cierre honesto (regla 12) es obligatorio; la frase no. Aquí se
        # compara el principio del cierre —las tres primeras palabras de su
        # narración y de su título de pantalla— con los de los cuatro Shorts
        # anteriores por número. AVISO y no error: dos cierres pueden empezar
        # igual por casualidad y estar bien; lo que no puede es no verse.
        # -----------------------------------------------------------------
        if num:
            propio = _inicio_cierre(g)
            for k in range(1, 5):
                previo = Path(path).parent / f"MDS-{int(num.group(1)) - k:03d}.es.json"
                try:
                    gp = json.loads(previo.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    continue
                for campo, a, b in (("narración", propio[0], _inicio_cierre(gp)[0]),
                                    ("título de pantalla", propio[1], _inicio_cierre(gp)[1])):
                    if a and a == b:
                        avisos.append(
                            f"C48.1: el cierre empieza igual que el de "
                            f"{gp.get('id', previo.stem)}, en su {campo} («{a}…»). El cierre honesto es "
                            f"obligatorio; la fórmula no. Dilo de otra manera y dentro de la "
                            f"historia (guionista_corto.md, la séptima regla).")

        # -----------------------------------------------------------------
        # C50 · LA IMAGEN DE CADA ESCENA (versión 13, 23/09/2026)
        #
        # «visual» dice qué se busca en el archivo para cada plano, desde qué
        # palabras de la narración entra y, de respaldo, qué imagen generar
        # (guionista_corto.md, «La imagen de cada escena»). Todo AVISO, nunca
        # ERROR: un plano sin imagen sale como tarjeta de marca, y eso no puede
        # parar una producción. Lo que sí hace este bloque es que un «desde» mal
        # copiado se vea antes del render, que es donde pondría la imagen a
        # destiempo sin avisar a nadie (lo que vio el codirector el 23/09).
        # -----------------------------------------------------------------
        tarjetas = 0
        for j, e in enumerate(escenas, 1):
            v = e.get("visual")
            if v is None:
                if num and int(num.group(1)) >= PRIMER_SHORT_C50:
                    avisos.append(
                        f"C50: la escena {j} no lleva «visual» y saldrá como tarjeta de marca. "
                        f"Si es a propósito, escribe \"visual\": \"marca\".")
                continue
            if v == "marca":
                tarjetas += 1
                continue
            planos_v = [v] if isinstance(v, dict) else v
            if not isinstance(planos_v, list) or not all(isinstance(x, dict) for x in planos_v):
                avisos.append(f"C50: escena {j}: «visual» tiene que ser \"marca\" o una lista de "
                              f"planos. Así no se entiende y la escena saldrá como tarjeta de marca.")
                continue
            if len(planos_v) > MAX_PLANOS_ESCENA:
                avisos.append(f"C50: escena {j}: {len(planos_v)} planos. Más de "
                              f"{MAX_PLANOS_ESCENA} en una escena son parpadeos: sobran.")
            for k, pl in enumerate(planos_v, 1):
                if pl.get("marca"):
                    tarjetas += 1
                elif not (pl.get("busqueda") or pl.get("prompt") or pl.get("fijar")):
                    avisos.append(f"C50: escena {j}, plano {k}: sin «busqueda», «prompt» ni "
                                  f"«marca»: no hay nada que buscar.")
                d = str(pl.get("desde") or "").strip()
                if not isinstance(pl.get("desde", ""), (str, type(None))):
                    avisos.append(f"C50: escena {j}, plano {k}: «desde» tiene que ser texto.")
                if k > 1 and not d:
                    avisos.append(
                        f"C50: escena {j}, plano {k}: sin «desde». Los planos sin «desde» se "
                        f"reparten la escena a partes iguales, y eso es lo que el 23/09 puso "
                        f"la imagen a destiempo de la frase.")
                elif d and not aparece(d, e.get("narracion")):
                    avisos.append(
                        f"C50: escena {j}, plano {k}: «desde: {d}» no está en la narración, "
                        f"así que el corte no sabe dónde caer. Cópialo tal cual de la narración.")
                consultas = pl.get("busqueda") or []
                if not isinstance(consultas, list):
                    consultas = [consultas]
                for q in consultas:
                    if re.search(r"[áéíóúñ¿¡]", str(q).lower()):
                        avisos.append(
                            f"C50: escena {j}, plano {k}: «{q}» parece estar en castellano. Los "
                            f"bancos de vídeo están etiquetados en inglés.")
        if tarjetas > MAX_TARJETAS_MARCA:
            avisos.append(
                f"C50: {tarjetas} tarjetas de marca. La tarjeta es el golpe del mensaje "
                f"clave, no el fondo: {MAX_TARJETAS_MARCA} por Short como mucho (el final ya "
                f"lleva la firma de marca por su cuenta).")

        # -----------------------------------------------------------------
        # C38.3 · la risa escrita (regla 13.1)
        # -----------------------------------------------------------------
        con_risa = [j for j, e in enumerate(escenas, 1) if e.get("risa")]
        if len(con_risa) > 1:
            errores.append(
                f"{len(con_risa)} escenas piden risa (escenas {con_risa}). En un Short, "
                f"una como mucho: tres o cuatro risas en cuarenta segundos es lo que el "
                f"codirector describió como artificial el 14/09.")
        for j in con_risa:
            if j == 1:
                errores.append("Escena 1 con «risa»: la regla 13.1 dice que el narrador no "
                               "se ríe al abrir.")
            if j == len(escenas):
                errores.append("El cierre con «risa»: la regla 13.1 dice que el cierre "
                               "honesto no admite guasa. Es la frase que sostiene la "
                               "credibilidad del canal.")
            if j > 1 and float(escenas[j-2].get("pausa_despues_s") or 0.0) >= PAUSA_DE_REMATE_S:
                errores.append("El remate con «risa»: la regla 13.1 dice que el remate se "
                               "dice completamente en serio. Un chiste contado por quien "
                               "se ríe de su propio chiste deja de tener gracia.")

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

    # ---------------------------------------------------------------------
    # P10 (08/09/2026) — que el Short tenga forma de historia.
    #
    # El codirector sobre MDS-011: «parece un corte despiezado del vídeo
    # largo, sin ninguna estructura de introducción, desarrollo y
    # desenlace». Comprobar la estructura entera (ritmo, si el chiste hace
    # gracia) exige leer el guion, y eso lo sigue haciendo quien revisa
    # (paso 1 de la revisión diaria). Lo que sí se puede comprobar sin
    # ambigüedad, contra lo que guionista_corto.md declara para cada serie:
    #
    #   · «El experimento» es un estudio contado como historia y «termina
    #     con la cifra grande en pantalla (tipo: dato) y su fuente»: exige
    #     una escena «dato» con «fuente».
    #   · «Esto no tiene gracia y esto sí» son «dos chistes casi idénticos»
    #     contados con «tipo: comparacion»: exige una escena «comparacion».
    #
    # (Que ninguna serie termine sin «cierre» ya es un error, más arriba:
    # «La última escena debe ser de tipo «cierre»».)
    #
    # Aviso, no error: MDS-011 y los guiones ya escritos no van a cumplir
    # esto en retrospectiva, y un comprobador que se equivoca a menudo se
    # acaba ignorando (REGLAS.md, historia de la regla 14.3). Probado
    # contra los quince Shorts del repositorio: cero falsos positivos —
    # las tres «El experimento» (MDS-002, MDS-009, MDS-011) ya traen su
    # «dato»/«fuente» y las tres «Esto no tiene gracia y esto sí»
    # (MDS-003, MDS-008, MDS-012) ya traen su «comparacion».
    # ---------------------------------------------------------------------
    serie = g.get("serie")
    if corto and serie == "El experimento":
        if not any(e.get("tipo") == "dato" and e.get("fuente") for e in escenas):
            avisos.append("P10: la serie «El experimento» exige una escena «dato» con "
                          "«fuente» — termina con la cifra grande, no solo con un "
                          "enunciado (guionista_corto.md). Este guion no la tiene.")
    if corto and serie == "Esto no tiene gracia y esto sí":
        if not any(e.get("tipo") == "comparacion" for e in escenas):
            avisos.append("P10: la serie «Esto no tiene gracia y esto sí» exige una "
                          "escena «comparacion» — son dos chistes casi idénticos que se "
                          "cuentan los dos antes de explicar nada (guionista_corto.md). "
                          "Este guion no la tiene.")

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
