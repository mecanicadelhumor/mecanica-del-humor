# Bitácora · Dirección en diferido · lunes 9 de noviembre de 2026

Contenedor arrancado a las 13:14 UTC. `origin/main` en `57caefb` (Visuales, 10:32). Sin sesión interactiva hoy
(ningún commit de «dirección» ajeno). Rama viva ajena: `claude/entrega-revision-20261104-1031` (ya en `main`).
Cuaderno: commit `dc55140` (09/11 12:15 +0100), dos puntos nuevos: «Incidencias» y «Sobre las voces».

## 1 · Lo roto: sin vídeo del 06 al 09/11

- Leídos los runs de «Producir vídeo» 307-314 y los de «Prueba de voces» 9-12. Producción: 404 «Model
  '…' not found» con `gemini-3.1-flash-tts-preview` y `-2.5-flash-preview-tts` (07-08/11) y con
  `gemini-3.8-flash-tts` y `-lite-tts` (08-09/11, tras el cambio de la revisión). Prueba de voces del 05/11:
  el 3.8 respondió bien por el mismo camino (`cli.interactions.create`).
- PyPI: `google-genai` **3.0.0, publicado el 06/11 a las 02:29 UTC**; la anterior, 2.34.0 (29/10).
  `requirements.txt` la instalaba sin tope.
- Medido en el contenedor (dos entornos virtuales, transporte `httpx` simulado): con 2.34.0
  `interactions.create` hace `POST …/v1beta/interactions`; con 3.0.0, `POST …/v1/interactions`. Con
  `HttpOptions(api_version="v1beta")`, las dos van a `v1beta`. Los modelos TTS son preview: solo en v1beta.
- Arreglo: `voz.py` (`API_GEMINI = "v1beta"` en `_gemini_cliente`), `prueba_voz.py` (igual) y
  `requirements.txt` (`google-genai>=2.34,<3`). Modelos de vuelta a 3.1 / 2.5 (cuaderno). Probado: el
  `_gemini_cliente` real de `voz.py` con las dos versiones de la librería llama a `v1beta`, y un 404
  sigue terminando en «no se publica» (el caso que tiene que fallar). Compila.
- Entrega 1 a las 13:18 UTC (`claude/entrega-direccion-20261109-1318`), en `main` como `bd6e946`.
- «Producir vídeo» lanzado a mano a las 13:19 UTC (run 42624441710, nº 315), sin entradas (lo de hoy:
  `MDS-067`, privado con publicación a las 18:00 UTC). La voz se sintetizó bien. Resultado: **ha salido bien**. La voz se hizo con `gemini-3.1-flash-tts-preview` (la de siempre), y el vídeo quedó subido a las 13:25 UTC, programado para publicarse a las 18:00 UTC (https://youtu.be/ggQ0Nvp60DA).

## 2 · El bucle

`resultados.json` (08/11 18:31): B2 sin datos que decidan (solo `MDS-060`). Nada que aplicar.

## 3 · El cuaderno

- **Incidencias** → arriba, y `MDS-062` (A) al martes 10/11 y `MDS-063` (control) al sábado 14/11 en
  `parrilla.json` (estaban aprobados y nunca subidos; los días estaban vacíos). Comprobado con
  `cola.py --fecha`: 07/11 ya sin trabajo, 10/11 → `MDS-062`, 14/11 → `MDS-063`.
- **Voces** → vuelta a los modelos que caducan; `voz-3.8-acento` (12/11), `voz-3.8-oir-2` (codirector,
  15/11), `voz-3.8-cambio` al 16/11.

## 4 · Lo vencido (`compromisos.json`)

Hechos: `voz-3.8-prueba` (05/11), `voz-3.8-oir`, `banco-guiones`, `visual-relevancia-nucleo` (05/11).
Al 12/11: `calidad-patron`. Al 16/11: `C51.3-prueba`, `C51.3-cara-fija`, `C61-esquina-libre`,
`iteracion-filtro`. Nuevos: `voz-3.8-acento`, `voz-3.8-oir-2`, `visual-recuento`, `voz-sdk-3`.

## 5 · Escrito

Plan v30; trampa 70 y «Dónde está el proyecto» del 09/11 en `PROMPT_DE_ARRANQUE.md`; nota a las rutinas;
tareas del codirector (privado) y `leido.json`.
