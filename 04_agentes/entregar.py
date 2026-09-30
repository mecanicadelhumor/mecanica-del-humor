#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
entregar.py — la entrega de una tarea programada, sin paquetes y sin nadie delante.

POR QUÉ EXISTE (dirección, 28/09/2026, versión 14 del plan, C53)
----------------------------------------------------------------
Hasta hoy las tres tareas programadas entregaban un `.tar.gz` que el codirector
tenía que descomprimir, commitear y subir a mano. Eso era trabajo recurrente
(regla 5) y además frágil: la semana del 21 el codirector no tuvo tiempo, y las
revisiones del 26 y el 27 se perdieron enteras. El canal no puede volar solo
mientras cada entrega necesite a una persona.

Ahora cada tarea sube su trabajo a una rama propia y un workflow lo pasa a
`main`. Este fichero hace las dos mitades, y existe para que la regla que
sostiene el reparto de ficheros (regla 10, `PROPIEDAD_DE_FICHEROS.md`) deje de
ser una promesa del prompt y pase a ser una comprobación: **lo que no es de la
tarea no llega a `main`, lo diga quien lo diga.**

LAS DOS MITADES
---------------
1. **La tarea** (al final de su sesión, desde la raíz del clon):

       python3 04_agentes/entregar.py --tarea revision --mensaje "revisión diaria 2026-09-29"
       python3 04_agentes/entregar.py --tarea revision --comprobar     # solo dice qué subiría

   Hace `git add -A`, separa lo suyo de lo ajeno (lo ajeno se deshace y se dice
   en voz alta, pero no bloquea: lo suyo se entrega igual), pasa
   `validar_guion.py` a los guiones que cambian, hace un commit y lo sube a
   **una rama nueva**, `claude/entrega-<tarea>-<AAAAMMDD-HHMM>`. Las sesiones en
   la nube solo pueden escribir en el repositorio si está añadido a la tarea
   (claude.ai/code/routines → Editar → Repositorios); las ramas `claude/` se
   aceptan siempre. Si el push falla, lo dice y sale con código 2: entonces, y
   solo entonces, se entrega el `.tar.gz` de siempre (plan B).

2. **El workflow «Entregas (C53)»** (`.github/workflows/entregas.yml`), en cuanto
   llega la rama:

       python3 04_agentes/entregar.py --aplicar claude/entrega-revision-20260929-0951

   Con **la copia de este fichero que hay en `main`** (una tarea no puede
   aflojarse las reglas cambiándolo en su rama), vuelve a clasificar lo que trae
   la rama, aplica **solo lo que es de la tarea** encima de lo último de `main`
   con una mezcla a tres bandas —si alguien ha cambiado lo mismo mientras tanto,
   no pisa: para y lo dice—, vuelve a validar los guiones, hace el commit con lo
   que se ha quedado fuera escrito en el mensaje, sube `main` y borra la rama.

CAMBIO DEL 30/09/2026 (dirección, versión 16 del plan, C53.2)
--------------------------------------------------------------
La primera entrega de verdad (la rutina de métricas, 30/09) funcionó, y enseñó
dos cosas de las rutinas de Code que no estaban previstas:

- **Cada sesión tiene su propia rama de trabajo** (`claude/<nombre-al-azar>`) y
  la plataforma le pide al modelo que suba ahí su trabajo. Si el modelo hace
  `git commit` ANTES de llamar a este script, `git add -A` ya no encontraba nada
  que entregar y el script decía «no hay nada que entregar» con código 0: el
  trabajo se quedaba en la rama de la sesión y a `main` no llegaba nada, sin un
  error (trampa 41). Desde hoy lo que se entrega se mide **contra `origin/main`**
  (su base común con la sesión), no contra el último commit, así que da igual si
  el modelo hizo commit antes o no.
- **Esas ramas de sesión se quedan en GitHub** y la página de la sesión ofrece
  «Create PR» sobre ellas. Nadie tiene que abrir nunca ese PR: saltaría la tabla
  de propiedad. `--aplicar` borra al final las ramas de sesión cuyo contenido ya
  está entero en `main`; las que traen algo que no está en `main` se quedan y se
  dicen en el resumen de la ejecución, para que las mire la dirección.

Lo que este script NO decide: si el trabajo está bien. Eso es de la tarea. Esto
solo garantiza que cada uno sube lo suyo, encima de lo último, y sin pisar.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
    MADRID = ZoneInfo("Europe/Madrid")
except Exception:                                   # pragma: no cover
    MADRID = timezone(timedelta(hours=2))

RAIZ = Path(__file__).resolve().parents[1]
RAMA = "main"
PREFIJO = "claude/entrega-"

# La producción de un día D arranca el día D a las 01:13 UTC (producir.yml).
HORA_PRODUCCION_UTC = (1, 13)

# ---------------------------------------------------------------------------
# PROPIEDAD — la tabla de 00_estrategia/PROPIEDAD_DE_FICHEROS.md, en código.
# {F} se sustituye por las fechas válidas (hoy y ayer, hora de España): la
# planificación empieza el jueves a las 22:00 y a veces termina el viernes.
# Si cambias la tabla del documento, cambia esta. Las dos dicen lo mismo.
# ---------------------------------------------------------------------------
PROPIEDAD = {
    "revision": [
        r"03_produccion/.+",
        r"04_agentes/.+",
        r"01_bibliografia/BIBLIOGRAFIA_CURADA\.md",
        r"01_bibliografia/data/semillas\.json",
        r"05_calendario/revisiones/.+",
        r"05_calendario/visuales/ajustes\.json",
        r"05_calendario/estado/{F}\.md",
        r"05_calendario/bitacora/{F}-revision[^/]*\.md",
        r"08_comunicacion/{F}-revision[^/]*\.md",
        r"07_pruebas/.+",
        # los guiones, solo con la excepción de las 48 horas (ver clasificar)
    ],
    "planificacion": [
        r"05_calendario/guiones/.+",
        r"05_calendario/parrilla\.json",
        r"05_calendario/publicaciones/.+",
        r"05_calendario/CALENDARIO\.md",
        r"05_calendario/demanda\.json",
        r"05_calendario/semillas_demanda\.json",
        r"05_calendario/pendientes_de_fuente\.md",
        r"05_calendario/revisiones/.+",          # aplica las notas y las retira
        r"05_calendario/bitacora/{F}-planificacion[^/]*\.md",
        r"08_comunicacion/{F}-planificacion[^/]*\.md",
    ],
    "metricas": [
        r"05_calendario/bitacora/{F}-metricas[^/]*\.md",
        r"08_comunicacion/{F}-metricas[^/]*\.md",
    ],
}

# Aunque un patrón de arriba lo cubra, esto no lo sube ninguna tarea nunca.
# Son de la dirección, del codirector o de GitHub Actions.
NUNCA = [
    r"\.github/.+",
    r"00_estrategia/.+",
    r"\.secrets/.+",
    r"05_calendario/registro_publicaciones\.json",
    r"05_calendario/qa/.+",
    r"05_calendario/metricas\.json",
    r"05_calendario/demanda_bruta\.json",
    r"05_calendario/ESTADO\.md",               # congelado (C45)
    r"05_calendario/MEJORAS\.md",              # congelado (21/08)
    r"08_comunicacion/novedades\.md",          # del codirector
    r"04_agentes/entregar\.py",                # este fichero: de la dirección
    r"03_produccion/pipeline/visual\.py",      # C50: de la dirección
    r"03_produccion/pipeline/fondo_visual\.py",
    r"03_produccion/cache_voz/.+",             # lo escribe Actions
    r"03_produccion/cache_visual/.+",
]

# Solo aquí se puede borrar un fichero. En el resto, un borrado no sube.
BORRAR_PERMITIDO = [r"05_calendario/revisiones/.+"]

GUION = re.compile(r"05_calendario/guiones/(MD[SH]-\d{3})\.es\.json")
TOKEN_EN_TEXTO = re.compile(r"github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{30,}")


def sh(*args, check=True):
    r = subprocess.run(list(args), cwd=RAIZ, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(args[:4])}…: {(r.stderr or r.stdout).strip()}")
    return r


def fechas_validas(ahora):
    hoy = ahora.astimezone(MADRID).date()
    return [hoy.isoformat(), (hoy - timedelta(days=1)).isoformat()]


def patron(p, fechas):
    alt = "(?:" + "|".join(re.escape(f) for f in fechas) + ")"
    return re.compile(p.replace("{F}", alt) + r"\Z")


def _json(ruta):
    try:
        return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))
    except Exception:
        return {}


def emision_de(episodio):
    for e in _json("05_calendario/parrilla.json").get("emisiones", []):
        if e.get("episodio") == episodio:
            return e.get("fecha")
    return None


def ya_subido(episodio):
    return any(p.get("episodio") == episodio and p.get("video_id")
               for p in _json("05_calendario/registro_publicaciones.json").get("publicaciones", []))


def dentro_de_48h(episodio, ahora):
    """La excepción estrecha de la revisión: un guion que se produce en menos de
    48 horas y que todavía no se ha producido (regla 11.4)."""
    fecha = emision_de(episodio)
    if not fecha or ya_subido(episodio):
        return False
    h, m = HORA_PRODUCCION_UTC
    try:
        prod = datetime.strptime(fecha, "%Y-%m-%d").replace(hour=h, minute=m, tzinfo=timezone.utc)
    except ValueError:
        return False
    return timedelta(0) < prod - ahora <= timedelta(hours=48)


def clasificar(tarea, lista, ahora):
    """lista: [(estado, ruta)] con estado A/M/D. Devuelve (vale, fuera) con el
    motivo de cada cosa que se queda fuera."""
    fechas = fechas_validas(ahora)
    suyos = [patron(p, fechas) for p in PROPIEDAD[tarea]]
    nunca = [patron(p, fechas) for p in NUNCA]
    borrables = [patron(p, fechas) for p in BORRAR_PERMITIDO]
    vale, fuera = [], []
    for estado, ruta in lista:
        motivo = None
        g = GUION.fullmatch(ruta)
        if any(p.match(ruta) for p in nunca):
            motivo = "no es de ninguna tarea (dirección, codirector o Actions)"
        elif g and tarea == "revision":
            # La excepción estrecha: la revisión solo toca un guion que se
            # produce en menos de 48 horas y que aún no se ha producido.
            if estado != "M":
                motivo = "la revisión no crea ni borra guiones"
            elif not dentro_de_48h(g.group(1), ahora):
                motivo = ("guion fuera de la excepción de las 48 horas: el defecto va a "
                          f"05_calendario/revisiones/{g.group(1)}.md")
        elif not any(p.match(ruta) for p in suyos):
            motivo = f"no es de «{tarea}» (PROPIEDAD_DE_FICHEROS.md)"
        elif estado == "D" and not any(p.match(ruta) for p in borrables):
            motivo = "aquí no se borra nada"
        elif g and tarea == "planificacion" and ya_subido(g.group(1)):
            motivo = "guion ya producido: nunca sobre un episodio producido (regla 11.4)"
        (fuera if motivo else vale).append((estado, ruta, motivo))
    return vale, fuera


def validar_guiones(rutas):
    """[(ruta, motivo)] de los guiones que no pasan validar_guion.py."""
    malos = []
    for ruta in rutas:
        if GUION.fullmatch(ruta) and (RAIZ / ruta).exists():
            r = sh(sys.executable, "04_agentes/validar_guion.py", ruta, check=False)
            if r.returncode != 0:
                lineas = [l.strip() for l in (r.stdout + r.stderr).splitlines() if "ERROR" in l.upper()]
                malos.append((ruta, "validar_guion.py da ERROR: " + " | ".join(lineas[:5])))
    return malos


def estados_git(desde, hasta=None, indice=False):
    args = ["git", "diff", "--name-status", "--no-renames"]
    args += ["--cached"] if indice else []
    args += [desde] + ([hasta] if hasta else [])
    res = []
    for linea in sh(*args).stdout.splitlines():
        partes = linea.split("\t")
        if len(partes) >= 2:
            res.append((partes[0][0], partes[-1]))
    return res


def informe(titulo, vale, fuera):
    lineas = [titulo, f"Sube ({len(vale)}):"]
    lineas += [f"  {estado}  {ruta}" for estado, ruta, _ in vale]
    if fuera:
        lineas.append(f"NO SUBE ({len(fuera)}) — dilo en tu bitácora con estas palabras:")
        lineas += [f"  {estado}  {ruta}  → {motivo}" for estado, ruta, motivo in fuera]
    return "\n".join(lineas)


# ---------------------------------------------------------------------------
# 1 · La mitad de la tarea
# ---------------------------------------------------------------------------

def deshacer(ruta, estado, base="HEAD"):
    """Vuelve a dejar un fichero como estaba en la base (lo último de main que
    conoce la sesión), aunque la tarea ya lo hubiera metido en un commit."""
    if estado == "A":
        sh("git", "rm", "--cached", "-q", "-f", "--", ruta, check=False)
        (RAIZ / ruta).unlink(missing_ok=True)
    else:
        sh("git", "restore", "--staged", "--worktree", f"--source={base}", "--", ruta, check=False)


def base_de_la_sesion():
    """La base común entre lo que hay en el clon y `origin/main`. Si la tarea hizo
    commit antes de entregar (la plataforma se lo pide), lo que hay que entregar
    es todo lo que va de ahí a hoy, no solo lo que quedó sin commitear (C53.2)."""
    sh("git", "fetch", "-q", "origin", f"+refs/heads/{RAMA}:refs/remotes/origin/{RAMA}", check=False)
    r = sh("git", "merge-base", "HEAD", f"origin/{RAMA}", check=False)
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else "HEAD"


def entregar(tarea, mensaje, comprobar):
    ahora = datetime.now(timezone.utc)
    base = base_de_la_sesion()
    sh("git", "add", "-A")
    lista = estados_git(base, indice=True)
    if not lista:
        print("entregar.py: no hay nada que entregar (ni sin commitear ni en commits de la sesión).")
        return 0
    vale, fuera = clasificar(tarea, lista, ahora)
    malos = dict(validar_guiones([r for e, r, _ in vale if e != "D"]))
    if malos:
        fuera += [(e, r, malos[r]) for e, r, _ in vale if r in malos]
        vale = [v for v in vale if v[1] not in malos]
    print(informe(f"== entregar.py · tarea «{tarea}» · {ahora:%Y-%m-%d %H:%M} UTC", vale, fuera))
    if comprobar:
        sh("git", "reset", "-q", check=False)        # deja el índice como estaba
        print("(--comprobar: no se ha subido ni deshecho nada)")
        return 0

    for estado, ruta, _ in fuera:
        deshacer(ruta, estado, base)
    sh("git", "add", "-A")
    if sh("git", "diff", "--cached", "--quiet", base, check=False).returncode == 0:
        print("entregar.py: después de quitar lo ajeno, no queda nada que subir.")
        return 0
    if TOKEN_EN_TEXTO.search(sh("git", "diff", "--cached", base).stdout):
        print("entregar.py: HAY UN TOKEN EN LO QUE IBA A SUBIR. No se ha subido nada. Quítalo del "
              "fichero y vuelve a entregar. El repositorio es público.")
        return 4

    mensaje = (mensaje or f"{tarea} {ahora.astimezone(MADRID):%Y-%m-%d}").replace("[producir]", "").strip()
    if sh("git", "diff", "--cached", "--quiet", check=False).returncode != 0:
        sh("git", "-c", f"user.name=Mecánica del Humor ({tarea})",
           "-c", "user.email=mecanicadelhumor@users.noreply.github.com",
           "commit", "-q", "-m", mensaje)
    # (si no hay nada nuevo respecto al último commit, es que la tarea ya lo había
    # commiteado todo y limpio: se sube tal cual; «Entregas» toma el título del
    # último commit de la rama)
    rama = f"{PREFIJO}{tarea}-{ahora:%Y%m%d-%H%M}"
    r = sh("git", "push", "-q", "origin", f"HEAD:refs/heads/{rama}", check=False)
    if r.returncode != 0:
        print("entregar.py: EL PUSH NO HA PODIDO SUBIR LA RAMA. No se ha subido nada.\n"
              f"  {(r.stderr or r.stdout).strip()[:400]}\n"
              "Lo más probable: el repositorio no está añadido a esta tarea en "
              "claude.ai/code/routines. Entrega el .tar.gz de siempre (plan B) y dilo en la "
              "PRIMERA línea de tu bitácora y en tu nota de 08_comunicacion/.")
        return 2
    sha = sh("git", "rev-parse", "--short", "HEAD").stdout.strip()
    print(f"SUBIDO: commit {sha} en la rama {rama}. El workflow «Entregas (C53)» lo pasa a main "
          "en uno o dos minutos. Para comprobarlo: git fetch origin main && git log origin/main -3")
    return 0


# ---------------------------------------------------------------------------
# 2 · La mitad del workflow
# ---------------------------------------------------------------------------

def salida_actions(clave, valor):
    ruta = os.environ.get("GITHUB_OUTPUT")
    if ruta:
        with open(ruta, "a", encoding="utf-8") as fh:
            fh.write(f"{clave}={valor}\n")


def resumen_actions(texto):
    print(texto)
    ruta = os.environ.get("GITHUB_STEP_SUMMARY")
    if ruta:
        with open(ruta, "a", encoding="utf-8") as fh:
            fh.write(texto + "\n\n")


def aplicar(rama):
    m = re.fullmatch(re.escape(PREFIJO) + r"(revision|planificacion|metricas)-[\w.-]+", rama)
    if not m:
        resumen_actions(f"«{rama}» no es una rama de entrega: no se aplica nada.")
        return 1
    tarea = m.group(1)
    ahora = datetime.now(timezone.utc)
    sh("git", "fetch", "-q", "origin", f"+refs/heads/{RAMA}:refs/remotes/origin/{RAMA}",
       f"+refs/heads/{rama}:refs/remotes/origin/{rama}")
    sh("git", "checkout", "-q", "-B", RAMA, f"origin/{RAMA}")
    base = sh("git", "merge-base", f"origin/{RAMA}", f"origin/{rama}").stdout.strip()
    vale, fuera = clasificar(tarea, estados_git(base, f"origin/{rama}"), ahora)
    rutas = [r for _, r, _ in vale]
    if not rutas:
        resumen_actions(informe(f"### Entrega de «{tarea}» ({rama}): nada que aplicar", vale, fuera))
        sh("git", "push", "-q", "origin", "--delete", rama, check=False)
        return 0

    parche = sh("git", "diff", "--binary", "--no-renames", base, f"origin/{rama}", "--", *rutas).stdout
    if TOKEN_EN_TEXTO.search(parche):
        resumen_actions(f"### Entrega de «{tarea}» RECHAZADA: lleva un token. No se aplica nada.")
        return 4
    with tempfile.NamedTemporaryFile("w", suffix=".patch", delete=False, encoding="utf-8") as fh:
        fh.write(parche)
    r = sh("git", "apply", "--3way", "--index", "--whitespace=nowarn", fh.name, check=False)
    conflicto = sh("git", "diff", "--name-only", "--diff-filter=U", check=False).stdout.strip()
    if r.returncode != 0 or conflicto:
        sh("git", "reset", "-q", "--hard", f"origin/{RAMA}", check=False)
        resumen_actions(f"### Entrega de «{tarea}» NO APLICADA: choca con lo que hay en main\n\n"
                        f"```\n{(r.stderr or r.stdout or conflicto).strip()[:1500]}\n```\n\n"
                        f"La rama `{rama}` se queda sin borrar para que la mire la dirección.")
        return 3

    # Los guiones se validan ya aplicados, contra la parrilla y el registro de main.
    for ruta, motivo in validar_guiones([r for e, r, _ in vale if e != "D"]):
        sh("git", "reset", "-q", "HEAD", "--", ruta, check=False)
        if sh("git", "cat-file", "-e", f"HEAD:{ruta}", check=False).returncode == 0:
            sh("git", "checkout", "-q", "HEAD", "--", ruta, check=False)
        else:
            (RAIZ / ruta).unlink(missing_ok=True)
        fuera.append(("M", ruta, motivo))
        vale = [v for v in vale if v[1] != ruta]

    resumen_actions(informe(f"### Entrega de «{tarea}» ({rama})", vale, fuera))
    if sh("git", "diff", "--cached", "--quiet", check=False).returncode == 0:
        print("Después de filtrar, no queda nada que aplicar.")
        sh("git", "push", "-q", "origin", "--delete", rama, check=False)
        return 0

    titulo = sh("git", "log", "-1", "--format=%s", f"origin/{rama}").stdout.strip() or tarea
    cuerpo = [f"Entrega de la tarea «{tarea}» (rama {rama}), aplicada por «Entregas (C53)»."]
    if fuera:
        cuerpo.append("\nSe quedó fuera:")
        cuerpo += [f"- {ruta}: {motivo}" for _, ruta, motivo in fuera]
    sh("git", "-c", f"user.name=Mecánica del Humor ({tarea})",
       "-c", "user.email=mecanicadelhumor@users.noreply.github.com",
       "commit", "-q", "-m", titulo.replace("[producir]", "").strip(), "-m", "\n".join(cuerpo))

    for intento in range(1, 5):
        if sh("git", "push", "-q", "origin", f"HEAD:{RAMA}", check=False).returncode == 0:
            break
        # Un workflow ha subido algo entre medias: encima de lo último, y otra vez.
        if sh("git", "pull", "-q", "--rebase", "origin", RAMA, check=False).returncode != 0:
            sh("git", "rebase", "--abort", check=False)
            resumen_actions("El rebase contra main ha chocado al subir: no se ha aplicado nada.")
            return 3
    else:
        resumen_actions("main ha rechazado el push cuatro veces: no se ha aplicado nada.")
        return 5

    sh("git", "push", "-q", "origin", "--delete", rama, check=False)
    aplicadas = [r for _, r, _ in vale]
    toca_visuales = any(GUION.fullmatch(r) or r == "05_calendario/visuales/ajustes.json" for r in aplicadas)
    toca_vista = any(r in ("03_produccion/pipeline/escena.html", "03_produccion/pipeline/vista.py",
                           "03_produccion/pipeline/render.py") for r in aplicadas)
    salida_actions("visuales", "true" if toca_visuales else "false")
    salida_actions("vista", "true" if toca_vista else "false")
    resumen_actions(f"Aplicada en main: {sh('git', 'rev-parse', '--short', 'HEAD').stdout.strip()}.")
    return 0


SESION = re.compile(r"claude/(?!entrega-)[\w./-]+")
MARGEN_SESION = timedelta(hours=2)


def limpiar_ramas_de_sesion():
    """Borra las ramas de sesión de las rutinas (`claude/<nombre>`, nunca las de
    entrega) cuyo contenido ya está entero en main y que llevan más de dos horas
    quietas. Las que traen algo que no está en main se quedan y se dicen: son
    trabajo que `entregar.py` dejó fuera o que nunca se entregó (C53.2). Nunca
    falla la entrega: si algo sale mal aquí, se dice y se sigue."""
    try:
        r = sh("git", "ls-remote", "--heads", "origin", "refs/heads/claude/*", check=False)
        ramas = [l.split("refs/heads/", 1)[1] for l in r.stdout.splitlines() if "refs/heads/" in l]
        ramas = [x for x in ramas if SESION.fullmatch(x)]
        if not ramas:
            return
        sh("git", "fetch", "-q", "origin", f"+refs/heads/{RAMA}:refs/remotes/origin/{RAMA}",
           *[f"+refs/heads/{x}:refs/remotes/origin/{x}" for x in ramas], check=False)
        ahora = datetime.now(timezone.utc)
        borradas, quedan = [], []
        for x in ramas:
            ref = f"refs/remotes/origin/{x}"
            ts = sh("git", "log", "-1", "--format=%ct", ref, check=False).stdout.strip()
            if not ts or ahora - datetime.fromtimestamp(int(ts), timezone.utc) < MARGEN_SESION:
                continue                                   # puede estar trabajando todavía
            base = sh("git", "merge-base", f"origin/{RAMA}", ref, check=False).stdout.strip()
            if not base:
                quedan.append((x, "no comparte historia con main"))
                continue
            cambiadas = sh("git", "diff", "--name-only", "--no-renames", base, ref,
                           check=False).stdout.split()
            pendiente = sh("git", "diff", "--name-only", "--no-renames", f"origin/{RAMA}", ref,
                           "--", *cambiadas, check=False).stdout.split() if cambiadas else []
            if pendiente:
                quedan.append((x, ", ".join(pendiente[:6]) + (" …" if len(pendiente) > 6 else "")))
            elif sh("git", "push", "-q", "origin", "--delete", x, check=False).returncode == 0:
                borradas.append(x)
        if borradas or quedan:
            texto = ["### Ramas de sesión de las rutinas (C53.2)"]
            if borradas:
                texto.append("Borradas porque todo lo suyo ya está en main: " +
                             ", ".join(f"`{x}`" for x in borradas))
            if quedan:
                texto.append("**Se quedan, porque traen algo que no está en main** (nadie abre un PR "
                             "con ellas: que las mire la dirección):")
                texto += [f"- `{x}`: {q}" for x, q in quedan]
            resumen_actions("\n\n".join(texto))
    except Exception as e:                                  # nunca tumba la entrega
        resumen_actions(f"(La limpieza de ramas de sesión ha fallado y se ha saltado: {e})")


def main():
    ap = argparse.ArgumentParser(description="Entrega de una tarea programada (C53)")
    ap.add_argument("--tarea", choices=sorted(PROPIEDAD))
    ap.add_argument("--mensaje", default="")
    ap.add_argument("--comprobar", action="store_true", help="no sube nada: dice qué subiría")
    ap.add_argument("--aplicar", metavar="RAMA", help="(workflow) pasa a main lo que es de la tarea")
    a = ap.parse_args()
    if a.aplicar:
        codigo = aplicar(a.aplicar)
        limpiar_ramas_de_sesion()
        return codigo
    if not a.tarea:
        ap.error("falta --tarea")
    return entregar(a.tarea, a.mensaje, a.comprobar)


if __name__ == "__main__":
    sys.exit(main())
