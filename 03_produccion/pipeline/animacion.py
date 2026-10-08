#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_produccion/pipeline/animacion.py — C55.2 · la animación a medida en las escenas
de mecanismo (brazo A del ciclo B1, C60). Versión 19 del plan (08/10/2026).

Lo usa render.py. NO toca la red (regla 11.6).

QUÉ HACE
--------
Si el guion marca una escena con `"animar": true` y existe la página
`05_calendario/animaciones/<ID>/animacion.html` (la escribe la rutina
«Animación», C55.2) que sabe pintar esa escena, el render captura ESA escena de
la página en vez de la tarjeta de marca o del vídeo de archivo. Cualquier otra
cosa sale como siempre.

POR DISEÑO NUNCA BLOQUEA (la misma garantía que C50)
----------------------------------------------------
Una escena animada que no llega, no se carga, no pasa la barrera de texto o falla
al capturar SALE COMO EN EL CONTROL, y el motivo queda en
`build/<ID>/animacion/usado.json` (que qa.py copia a la ficha). El marcador
(`bucle.py`) mira `animacion.escenas_animadas` de la ficha y aparta del ciclo al
Short que pidió animación y no la tuvo. Un fallo aquí no cuesta nunca un vídeo.

EL CONTRATO DE LA PÁGINA (lo que escribe la rutina «Animación»)
----------------------------------------------------------------
Un único fichero HTML autónomo (sin red, sin Math.random: regla 11.5), de 1080×1920,
con un elemento `#lienzo` de ese tamaño en la esquina superior izquierda. Expone:

  window.ESCENAS                    lista de números de escena que sabe pintar, p. ej. [4, 5]
  window.cargarTiempos(datos)       render.py la llama UNA vez antes de pintar, con
                                    {"4": {"dur": 8.65, "palabras": [[0.32, "No"], ...]}, ...}:
                                    la duración REAL de cada escena y el instante (s, desde el
                                    principio de la escena) en que la voz dice cada palabra.
                                    La página ancla en ellas lo que se mueve «en la palabra que
                                    lo nombra». El guion se escribe antes que la voz, así que la
                                    página NO puede traer esos tiempos escritos a mano.
  window.pintarEscena(n, t)         deja `#lienzo` como tiene que estar en el segundo `t`
                                    (0 ≤ t ≤ dur) de la escena n. Determinista.
  window.comprobarEscena(n, t)      lista de textos que no caben en su caja o salen de la zona
                                    segura (puede estar vacía). Es la barrera C21 de esta página.

La escena animada ocupa TODA la pantalla (es opaca): lleva su propio texto, que sigue la regla
14 (no dice nada que la voz no diga). No se anima la última escena del Short: lleva el remate
de marca «Síguenos» (C59).
"""
import json
import re
import shutil
from pathlib import Path

import fondo_visual

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
ANIMACIONES = RAIZ / "05_calendario" / "animaciones"
PAGINA = "animacion.html"
INSTANTES_BARRERA = 20          # como la barrera de C21 y la de la muestra de C55.1


class SinAnimacion(Exception):
    """La animación pedida no se puede usar; la escena sale como en el control."""


def pagina_de(ident):
    return ANIMACIONES / ident / PAGINA


def _ruta_corta(ruta):
    try:
        return str(Path(ruta).relative_to(RAIZ))
    except ValueError:
        return str(ruta)


def pedidas(guion, escenas):
    """Números de escena con `animar: true` y su motivo si no pueden animarse
    (ya aquí: la última, o sin página)."""
    ident = guion.get("id", "")
    ultima = escenas[-1]["n"] if escenas else None
    quieren = [e["n"] for e in escenas if e.get("animar")]
    motivos, validas = {}, []
    for n in quieren:
        if n == ultima:
            motivos[n] = "la última escena lleva el remate de marca (C59) y no se anima"
        elif not pagina_de(ident).exists():
            motivos[n] = f"no hay página: falta {_ruta_corta(pagina_de(ident))}"
        else:
            validas.append(n)
    return validas, motivos


def palabras(e, carpeta):
    """[[t, palabra], ...] con el instante (s, desde el inicio de la escena) en que
    la voz dice cada palabra. Con el audio de la escena delante se ancla en sus
    silencios (fondo_visual.mapa_de_tiempo); sin él, reparto proporcional."""
    texto = e.get("narracion") or ""
    dur = float(e.get("duracion_s") or 0)
    pausa = e.get("pausa_despues_s", fondo_visual.PAUSA_POR_DEFECTO)
    pausa = fondo_visual.PAUSA_POR_DEFECTO if pausa is None else float(pausa)
    habla = max(0.3, dur - pausa)
    audio = Path(carpeta) / e["audio"] if (carpeta and e.get("audio")) else None
    if audio is not None and audio.exists():
        activos, silencios = fondo_visual.tramos_de_voz(audio, habla)
        instante = fondo_visual.mapa_de_tiempo(texto, activos, silencios)
    else:
        pesos = fondo_visual._pesos(texto, True)
        activos = [(0.08, habla)]

        def instante(indice):
            return fondo_visual._instante(indice, pesos, activos)
    return [[round(float(instante(m.start())), 3), m.group(0)]
            for m in re.finditer(r"\S+", texto)]


class Pagina:
    """La página de animación abierta en un navegador. Se usa dentro de un
    `with sync_playwright()` de render.py."""

    def __init__(self, nav, ancho, alto, escala, ruta, datos):
        self.pag = nav.new_page(viewport={"width": ancho, "height": alto},
                                device_scale_factor=escala)
        self.errores = []
        self.pag.on("pageerror", lambda x: self.errores.append(str(x)))
        self.pag.goto(Path(ruta).resolve().as_uri())
        self.pag.wait_for_timeout(200)
        if self.errores:
            raise SinAnimacion(f"la página falla al cargar: {self.errores[0][:200]}")
        if not self.pag.evaluate("() => typeof pintarEscena === 'function' && "
                                 "typeof comprobarEscena === 'function' && Array.isArray(window.ESCENAS)"):
            raise SinAnimacion("la página no cumple el contrato (ESCENAS, pintarEscena, comprobarEscena)")
        if self.pag.evaluate("() => typeof cargarTiempos === 'function'"):
            self.pag.evaluate("d => cargarTiempos(d)", datos)
        self.lienzo = self.pag.locator("#lienzo")

    def sabe(self, n):
        return bool(self.pag.evaluate("n => window.ESCENAS.map(Number).includes(n)", n))

    def barrera(self, n, dur):
        """Textos que no caben, en INSTANTES_BARRERA instantes de la escena."""
        malos = []
        for k in range(INSTANTES_BARRERA):
            t = dur * k / (INSTANTES_BARRERA - 1)
            for m in self.pag.evaluate("([n, t]) => comprobarEscena(n, t)", [n, t]):
                malos.append((round(t, 2), str(m)))
                break
            if malos:
                break
        if self.errores:
            malos.append((0, f"error en la página: {self.errores[0][:200]}"))
        return malos

    def capturar(self, n, t, ruta):
        self.pag.evaluate("([n, t]) => pintarEscena(n, t)", [n, t])
        self.lienzo.screenshot(path=str(ruta))
        if self.errores:
            raise SinAnimacion(f"error en la página: {self.errores[0][:200]}")

    def cerrar(self):
        try:
            self.pag.close()
        except Exception:
            pass


def hacer(guion, escenas, carpeta, fps, escala, destino):
    """Prerenderiza TODAS las escenas animadas antes de que render.py monte nada.

    Así un fallo se conoce antes de componer el fondo y el plan: la escena que
    falle sale como en el control y las demás no se enteran. Devuelve
    `(frames, descartadas, previos)`:
      · frames       {n: [Path, ...]}, un PNG por fotograma, ya al tamaño del lienzo
      · descartadas  {n: motivo} las que se pidieron, había página, y no salieron
      · previos      {n: motivo} las que ni siquiera se intentaron (última escena, sin página)
    Nunca lanza."""
    from playwright.sync_api import sync_playwright
    ancho, alto = 1080, 1920
    validas, previos = pedidas(guion, escenas)
    frames, descartadas = {}, {}
    if not validas:
        return frames, descartadas, previos
    por_n = {e["n"]: e for e in escenas}
    datos = {str(n): {"dur": float(por_n[n]["duracion_s"]), "palabras": palabras(por_n[n], carpeta)}
             for n in validas}
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--force-color-profile=srgb",
                                          "--font-render-hinting=none",
                                          "--disable-lcd-text",
                                          "--hide-scrollbars"])
            try:
                pagina = Pagina(nav, ancho, alto, escala, pagina_de(guion["id"]), datos)
            except Exception as ex:
                nav.close()
                return frames, {n: f"{type(ex).__name__}: {ex}"[:300] for n in validas}, previos
            for n in validas:
                try:
                    if not pagina.sabe(n):
                        descartadas[n] = "la página no trae esta escena (ESCENAS)"
                        continue
                    dur = float(por_n[n]["duracion_s"])
                    malos = pagina.barrera(n, dur)
                    if malos:
                        descartadas[n] = f"no pasa la barrera: t={malos[0][0]} {malos[0][1]}"[:300]
                        continue
                    n_f = max(1, int(round(dur * fps)))
                    carpeta_n = Path(destino) / f"escena_{n}"
                    carpeta_n.mkdir(parents=True, exist_ok=True)
                    lista = []
                    for f in range(n_f):
                        ruta = carpeta_n / f"{f:06d}.png"
                        pagina.capturar(n, f / fps, ruta)
                        lista.append(ruta)
                    frames[n] = lista
                except Exception as ex:
                    descartadas[n] = f"{type(ex).__name__}: {ex}"[:300]
                    frames.pop(n, None)
            pagina.cerrar()
            nav.close()
    except Exception as ex:                    # el navegador mismo: ninguna escena sale animada
        return {}, {n: f"{type(ex).__name__}: {ex}"[:300] for n in validas}, previos
    return frames, descartadas, previos


def escribir_usado(carpeta, guion, escenas_animadas, descartadas, motivos_previos):
    """build/<ID>/animacion/usado.json: lo lee qa.py para la ficha."""
    d = Path(carpeta) / "animacion"
    if d.exists():
        shutil.rmtree(d, ignore_errors=True)
    todas = dict(motivos_previos)
    todas.update(descartadas)
    if not escenas_animadas and not todas:
        return
    d.mkdir(parents=True, exist_ok=True)
    pedidas_n = sorted(set(escenas_animadas) | set(todas))
    (d / "usado.json").write_text(json.dumps({
        "escenas_animadas": len(escenas_animadas),
        "escenas": sorted(escenas_animadas),
        "pedidas": pedidas_n,
        "descartadas": {str(n): m for n, m in sorted(todas.items())},
        "pagina": _ruta_corta(pagina_de(guion.get("id", ""))),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
