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
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from voz import (  # noqa: E402  (el sys.path.insert de arriba tiene que ir antes)
    CACHE_VOZ_DIR,
    ESPERA_ENTRE_LLAMADAS_GEMINI,
    MODELO_GEMINI_LARGO,
    RITMO_GEMINI_HZ,
    VOZ_GEMINI_ESCEPTICO,
    VOZ_GEMINI_NARRADOR,
    _cache_voz_ruta,
    _gemini_cliente,
    _gemini_pcm,
    _audio_plausible,
    _pcm_a_mp3,
    clase_de_error,
    direccion_escena,
    duracion_real,
    hablable,
)

# Ver el punto 1 de arriba: cuota propia, nunca la de los Shorts (C7).
# El literal vive en voz.py y se importa desde allí (arriba): dos copias del
# nombre de un modelo que forma parte de una clave de caché es una divergencia
# esperando a pasar, y cuando pase no dará ningún error — solo sintetizará todo
# dos veces. Ver la trampa 24 de PROMPT_DE_ARRANQUE.md.

# 10 peticiones/día es el límite real. Se pide con margen para no gastar la
# décima justo en el momento en que la API empieza a devolver 429 y perder
# tiempo reintentando algo que ya sabemos que va a fallar.
PRESUPUESTO_POR_DEFECTO = 9

# C33.1 (15/09/2026): tope de fallos por ejecución. Hasta hoy un fallo no
# contaba contra el presupuesto, así que con la API caída se intentaban las
# cuarenta escenas, una cada 25 s, y cada intento podía contar contra la cuota
# del día. Tres fallos seguidos bastan para saber que hoy no es el día.
FALLOS_MAXIMOS = 3


def _voz_de(escena):
    papel = "esceptico" if escena.get("voz") == "esceptico" else "narrador"
    return VOZ_GEMINI_ESCEPTICO if papel == "esceptico" else VOZ_GEMINI_NARRADOR


def escenas_pendientes(guion):
    """[(indice, texto, texto_dirigido, voz_gemini, ruta_cache), ...] sin cachear
    todavía con MODELO_GEMINI_LARGO. `indice` es 1-based, solo para el log.

    `texto_dirigido` es el prompt completo (dirección de actor + narración), que
    es lo que se le manda a la API y lo que entra en la clave de caché."""
    pendientes = []
    escenas = guion.get("escenas", [])
    for i, e in enumerate(escenas, 1):
        crudo = (e.get("narracion") or "").strip()
        if not crudo:
            continue
        texto = hablable(crudo)
        voz_gemini = _voz_de(e)
        # C33: la misma dirección que usará voz.py el sábado, o el precacheo no
        # se encuentra (y además sale sin dirigir). Ver el punto 2b de arriba.
        dirigido, _papel = direccion_escena(escenas, i, texto)
        cache = _cache_voz_ruta(texto, MODELO_GEMINI_LARGO, voz_gemini, dirigido)
        if not cache.exists():
            pendientes.append((i, texto, dirigido, voz_gemini, cache))
    return pendientes


def _agotado_por_dia(exc):
    # C33.1: la clasificación vive en voz.py. La de aquí buscaba «per day» o
    # «perday» y Google escribe «per_day»: nunca reconocía la cuota agotada.
    return clase_de_error(exc) == "dia"


def principal(guion_path, presupuesto):
    """Devuelve (hechas, restantes). No lanza para un fallo transitorio de
    una escena suelta: eso se reintenta el día siguiente."""
    guion = json.loads(Path(guion_path).read_text(encoding="utf-8"))
    ident = guion.get("id", Path(guion_path).stem)

    if guion.get("formato") != "largo":
        print(f"::warning::{guion_path}: formato «{guion.get('formato')}», no «largo». "
              f"C27-B es solo para el episodio del sábado; no se toca nada.")
        return 0, 0

    pendientes = escenas_pendientes(guion)
    total = len(pendientes)
    print(f"{ident}: {total} escena(s) sin cachear con {MODELO_GEMINI_LARGO}.")
    if not total:
        print("Nada que hacer — la caché ya cubre todo el guion.")
        return 0, 0

    cliente = None
    hechas = 0
    fallos = 0
    ultima = 0.0
    for i, texto, dirigido, voz_gemini, cache in pendientes:
        if fallos >= FALLOS_MAXIMOS:
            print(f"::warning::{fallos} fallos en esta ejecución: se para aquí para no "
                  f"gastar cuota. Quedan {total - hechas} escena(s) para el próximo día.")
            break
        if hechas >= presupuesto:
            print(f"Presupuesto de {presupuesto} llamada(s) agotado por hoy. "
                  f"Quedan {total - hechas} escena(s) para el próximo día.")
            break

        espera = ESPERA_ENTRE_LLAMADAS_GEMINI - (time.monotonic() - ultima)
        if ultima and espera > 0:
            time.sleep(espera)

        try:
            cliente = cliente or _gemini_cliente()
            pcm = _gemini_pcm(cliente, MODELO_GEMINI_LARGO, dirigido, voz_gemini)
            ultima = time.monotonic()
            CACHE_VOZ_DIR.mkdir(parents=True, exist_ok=True)
            # Escritura atómica: si el proceso muere a mitad de _pcm_a_mp3
            # (que llama a ffmpeg), no queda un .mp3 a medio escribir con el
            # nombre final haciéndose pasar por caché válida.
            tmp = cache.with_suffix(".tmp.mp3")
            _pcm_a_mp3(pcm, RITMO_GEMINI_HZ, tmp)
            dur = duracion_real(tmp)
            if not _audio_plausible(texto, dur):
                tmp.unlink(missing_ok=True)
                raise RuntimeError(f"toma descartada: {dur:.1f} s para "
                                   f"{len(texto.split())} palabras")
            tmp.replace(cache)
            hechas += 1
            print(f"  escena {i:>2}  cacheada  ({hechas}/{min(presupuesto, total)} hoy)")
        except Exception as exc:
            ultima = time.monotonic()
            fallos += 1
            if _agotado_por_dia(exc):
                print(f"::warning::cuota DIARIA de {MODELO_GEMINI_LARGO} agotada en la "
                      f"escena {i}. Quedan {total - hechas} escena(s) para el próximo día.")
                break
            print(f"::warning::escena {i}: fallo al sintetizar con Gemini, se deja para "
                  f"el próximo intento. Error: {str(exc)[:200]!r}")
            # Fallo transitorio (red, respuesta vacía...): no cuenta contra el
            # presupuesto de hoy más que la espera ya consumida, y no se marca
            # nada como agotado — mañana se reintenta esta misma escena.

    restantes = total - hechas
    print(f"\n{hechas} escena(s) cacheada(s) hoy. {restantes} pendiente(s) de {ident}.")
    return hechas, restantes


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guion")
    ap.add_argument("--presupuesto", type=int, default=PRESUPUESTO_POR_DEFECTO,
                     help=f"llamadas reales a Gemini como máximo hoy "
                          f"(por defecto {PRESUPUESTO_POR_DEFECTO}, por debajo del "
                          f"límite de 10/día para dejar margen)")
    a = ap.parse_args()
    # Quedar escenas pendientes es el estado normal de martes a jueves: no es
    # un fallo del workflow, así que esto no devuelve nunca un código de
    # salida distinto de 0 por esa causa. Solo una excepción no controlada
    # (guion inexistente, JSON roto, GEMINI_API_KEY ausente) debe parar el
    # job con error, y para eso ya basta con dejarla subir sin capturarla.
    principal(a.guion, a.presupuesto)
