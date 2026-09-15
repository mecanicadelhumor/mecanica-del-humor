#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
voz_precache.py — precachea contra Gemini la narración de un guion «largo»,
SIN producir vídeo. Pieza B de C27 (versión 6/7 de PLAN_DE_CAMBIOS.md).

Por qué existe: un episodio largo tiene ~40 escenas y el nivel gratuito de
Gemini da 10 peticiones al día POR MODELO. No cabe en un solo día — el
sábado de producción — pero sí de viernes a viernes: la planificación ya
escribe el guion del sábado con nueve días de margen (ver
05_calendario/bitacora/2026-09-12-direccion.md, punto 1). Este script es lo
que gasta esos días: se llama una vez al día, mira qué escenas del guion del
sábado que viene todavía no están en la caché de voz.py y sintetiza tantas
como el presupuesto de llamadas de hoy permita. El sábado, `voz.py` (cuando
soporte «largo» con Gemini, que es un paso posterior a este) se encuentra
casi todo hecho.

Lo llama un workflow nuevo, `voz_adelantada.yml`, propuesto en
`07_pruebas/voz-adelantada-14-09/` con su `.md` explicativo al lado —
`.github/workflows/` no se escribe en remoto, así que el codirector lo crea
a mano cuando quiera encenderlo.

Dos cosas que este script decide y que NO hay que tocar sin pensarlo:

1. **Modelo `gemini-2.5-flash-preview-tts` (MODELO_GEMINI_LARGO), nunca
   `gemini-3.1-flash-tts-preview` (MODELO_GEMINI, el de los Shorts, C7).**
   Son cuotas diarias independientes. Si el largo compitiera por el modelo
   de los Shorts, un episodio de 40 escenas se comería la cuota que
   necesitan los cinco Shorts de la semana.

2b. **Y desde C33 (14/09/2026) incluye además la DIRECCIÓN DE ACTOR.** La voz
   de una escena ya no depende solo de su texto: depende del papel que hace esa
   escena dentro del guion (apertura, remate, cifra, cierre...), que `voz.py`
   deriva del propio guion con `direccion_escena()`. Este script llama a esa
   misma función y cachea con esa misma dirección, de modo que lo precacheado el
   martes sea exactamente lo que `voz.py` busca el sábado. Si alguien vuelve a
   sintetizar aquí el texto pelado, pasan las dos cosas a la vez: el audio sale
   sin dirigir y además nunca se encuentra en la caché.

2. **La clave de caché incluye el MODELO exacto, no la palabra «gemini» a
   secas.** `voz.py` hoy cachea los Shorts con
   `_cache_voz_ruta(texto, "gemini", voz)` — una cadena fija, porque hasta
   ahora solo existía un modelo de Gemini en juego. Aquí se cachea con
   `_cache_voz_ruta(texto, MODELO_GEMINI_LARGO, voz)`, que es una cadena
   distinta («gemini-2.5-flash-preview-tts»), así que las dos cachés nunca
   chocan aunque compartan directorio y aunque compartan voz (`Charon`,
   `Puck`). **El día en que `voz.py` aprenda a sintetizar episodios largos
   con Gemini de verdad, tiene que pedir la caché con este mismo modelo
   exacto** — si ese día alguien vuelve a escribir el literal `"gemini"`
   para el largo (copiando el patrón de los Shorts sin fijarse), este
   precacheo de toda la semana se sintetiza dos veces y no sirve de nada.

Uso:

    python3 voz_precache.py 05_calendario/guiones/MDH-008.es.json
    python3 voz_precache.py MDH-008.es.json --presupuesto 9

No escribe voz.mp3, subtítulos ni build/: solo rellena
03_produccion/cache_voz/. No toca voz.py ni ningún fichero de producción.
"""
import argparse
import asyncio
import json
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from voz import (  # noqa: E402  (el sys.path.insert de arriba tiene que ir antes)
    CACHE_VOZ_DIR,
    MODELO_GEMINI_LARGO,
    VOZ_GEMINI_ESCEPTICO,
    VOZ_GEMINI_NARRADOR,
    CuotaDiariaAgotada,
    _cache_voz_ruta,
    _direccion_v1,
    _gemini_escena,
    clase_de_error,
    direccion_escena,
    hablable,
)

# Ver el punto 1 de arriba: cuota propia, nunca la de los Shorts (C7).
# El literal vive en voz.py y se importa desde allí (arriba): dos copias del
# nombre de un modelo que forma parte de una clave de caché es una divergencia
# esperando a pasar, y cuando pase no dará ningún error — solo sintetizará todo
# dos veces. Ver la trampa 24 de PROMPT_DE_ARRANQUE.md.

# 10 peticiones/día es el límite real. Desde C33.2 (15/09/2026) el presupuesto
# cuenta PETICIONES, no escenas cacheadas: un rechazo o un corte también gasta
# cuota, y hasta hoy no se contaban.
PRESUPUESTO_POR_DEFECTO = 9

# C33.1 (15/09/2026): tope de escenas fallidas por ejecución. Tres bastan para
# saber que hoy no es el día.
FALLOS_MAXIMOS = 3

RAIZ = Path(__file__).resolve().parents[2]


def _voz_de(escena):
    papel = "esceptico" if escena.get("voz") == "esceptico" else "narrador"
    return VOZ_GEMINI_ESCEPTICO if papel == "esceptico" else VOZ_GEMINI_NARRADOR


def escenas_pendientes(guion):
    """Escenas sin cachear todavía con MODELO_GEMINI_LARGO, como los `items` de
    voz.py: {i, texto, dirigido, firma, dirigido_v1, voz_gemini}.

    C33.2: la misma dirección y la misma firma que usará voz.py el día de la
    producción, y se da por cacheada también una escena guardada con la clave
    de la dirección v1 (14-15/09), que voz.py sigue encontrando."""
    pendientes = []
    escenas = guion.get("escenas", [])
    for i, e in enumerate(escenas, 1):
        crudo = (e.get("narracion") or "").strip()
        if not crudo:
            continue
        texto = hablable(crudo)
        voz_gemini = _voz_de(e)
        dirigido, _papel, firma = direccion_escena(escenas, i, texto)
        dirigido_v1, _ = _direccion_v1(escenas, i, texto)
        claves = (_cache_voz_ruta(texto, MODELO_GEMINI_LARGO, voz_gemini, firma),
                  _cache_voz_ruta(texto, MODELO_GEMINI_LARGO, voz_gemini, dirigido_v1))
        if not any(c.exists() for c in claves):
            pendientes.append({"i": i, "texto": texto, "dirigido": dirigido,
                               "firma": firma, "dirigido_v1": dirigido_v1,
                               "voz_gemini": voz_gemini})
    return pendientes


def _agotado_por_dia(exc):
    # C33.1: la clasificación vive en voz.py.
    return clase_de_error(exc) == "dia"


def largos_pendientes(hoy=None):
    """Rutas de los episodios LARGOS de la parrilla, de hoy en adelante y por
    fecha, que todavía no están subidos.

    C33.2 (15/09/2026): `voz_adelantada.yml` le pasa a este script «el guion del
    próximo sábado». Eso deja de ser suficiente por dos motivos: el 19/09 el
    sábado lleva un Short (MDS-017, movido) y el largo pasa al domingo 20; y si
    el workflow corre también en fin de semana, «el próximo sábado» es el de la
    semana siguiente mientras el largo de este domingo sigue a medias. Así que el
    guion que llega se toma como pista, y lo que se precachea es siempre el largo
    pendiente más cercano; si ese ya está completo, el siguiente.
    """
    import cola  # noqa: E402  (mismo directorio; sin efectos al importar)
    hoy = hoy or date.today()
    try:
        datos = json.loads((RAIZ / "05_calendario" / "parrilla.json").read_text(encoding="utf-8"))
    except Exception:
        return []
    subidos = cola.videos_subidos()
    rutas = []
    for em in sorted(datos.get("emisiones", []), key=lambda e: e.get("fecha", "")):
        if em.get("fecha", "") < hoy.isoformat():
            continue
        for idioma in em.get("idiomas", ["es"]):
            ruta = RAIZ / "05_calendario" / "guiones" / f"{em['episodio']}.{idioma}.json"
            if not ruta.exists():
                continue
            try:
                formato = json.loads(ruta.read_text(encoding="utf-8")).get("formato")
            except Exception:
                continue
            if formato == "largo" and not cola.subido_de_verdad(
                    f"{em['episodio']}.{idioma}", em, subidos):
                rutas.append(ruta)
    return rutas


def siguiente_largo(hoy=None):
    """El largo pendiente más cercano, o None."""
    rutas = largos_pendientes(hoy)
    return rutas[0] if rutas else None


def principal(guion_path, presupuesto):
    """Devuelve (hechas, restantes) del conjunto precacheado hoy.

    `guion_path` es solo una pista: se precachea el largo pendiente más cercano
    de la parrilla y, si sobra presupuesto, el siguiente. Si la parrilla no se
    puede leer, se usa la pista si es un largo.
    """
    candidatos = largos_pendientes()
    if not candidatos:
        pista = Path(guion_path)
        try:
            es_largo = json.loads(pista.read_text(encoding="utf-8")).get("formato") == "largo"
        except Exception:
            es_largo = False
        if not es_largo:
            print(f"::notice::No hay ningún largo pendiente en la parrilla y {guion_path} "
                  f"no es un largo. No se toca nada.")
            return 0, 0
        candidatos = [pista]
    elif Path(guion_path).resolve() != candidatos[0].resolve():
        print(f"::notice::Se pidió {Path(guion_path).name}; se precachea primero el largo "
              f"pendiente más cercano de la parrilla: {candidatos[0].name}.")

    estado = {"agotados": {}, "llamadas": {}, "rechazos": {}, "seguidos_429": {},
              "ultima": 0.0, "cliente": None}
    hechas_total = restantes_total = 0
    for ruta in candidatos:
        guion = json.loads(Path(ruta).read_text(encoding="utf-8"))
        ident = guion.get("id", Path(ruta).stem)
        pendientes = escenas_pendientes(guion)
        print(f"{ident}: {len(pendientes)} escena(s) sin cachear con {MODELO_GEMINI_LARGO}.")
        if not pendientes:
            continue
        if (estado["llamadas"].get(MODELO_GEMINI_LARGO, 0) >= presupuesto
                or estado["agotados"].get(MODELO_GEMINI_LARGO)):
            restantes_total += len(pendientes)
            continue
        h, r = asyncio.run(_precachear(ident, pendientes, presupuesto, estado))
        hechas_total += h
        restantes_total += r
    return hechas_total, restantes_total


async def _precachear(ident, pendientes, presupuesto, estado):
    total = len(pendientes)
    hechas = fallos = 0
    with tempfile.TemporaryDirectory() as tmp:
        for it in pendientes:
            gastadas = estado["llamadas"].get(MODELO_GEMINI_LARGO, 0)
            if gastadas >= presupuesto:
                print(f"Presupuesto de {presupuesto} petición(es) gastado por hoy.")
                break
            if fallos >= FALLOS_MAXIMOS:
                print(f"::warning::{fallos} escenas fallidas en esta ejecución: se para aquí "
                      f"para no gastar cuota.")
                break
            it["mp3"] = Path(tmp) / f"escena_{it['i']:03d}.mp3"
            try:
                origen = await _gemini_escena(it, MODELO_GEMINI_LARGO, estado)
            except CuotaDiariaAgotada:
                print(f"::warning::cuota DIARIA de {MODELO_GEMINI_LARGO} agotada en la "
                      f"escena {it['i']}.")
                break
            if origen is None:
                fallos += 1
                continue
            hechas += 1
            print(f"  escena {it['i']:>2}  cacheada [{origen}]  "
                  f"({estado['llamadas'].get(MODELO_GEMINI_LARGO, 0)} peticiones hoy)")

    restantes = total - hechas
    print(f"\n{hechas} escena(s) cacheada(s) hoy con "
          f"{estado['llamadas'].get(MODELO_GEMINI_LARGO, 0)} petición(es). "
          f"{restantes} pendiente(s) de {ident}.")
    return hechas, restantes


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guion")
    ap.add_argument("--presupuesto", type=int, default=PRESUPUESTO_POR_DEFECTO,
                     help=f"peticiones reales a Gemini como máximo hoy "
                          f"(por defecto {PRESUPUESTO_POR_DEFECTO}, por debajo del "
                          f"límite de 10/día para dejar margen)")
    a = ap.parse_args()
    # Quedar escenas pendientes es el estado normal entre semana: no es un
    # fallo del workflow, así que esto no devuelve nunca un código de salida
    # distinto de 0 por esa causa. Solo una excepción no controlada (guion
    # inexistente, JSON roto, GEMINI_API_KEY ausente) debe parar el job con
    # error, y para eso ya basta con dejarla subir sin capturarla.
    principal(a.guion, a.presupuesto)
