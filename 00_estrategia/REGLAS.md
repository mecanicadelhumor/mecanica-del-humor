# Reglas — Mecánica del Humor

**Este archivo se lee antes de tocar nada.** Es corto a propósito.

Si algo de lo que vas a hacer choca con una regla de aquí, no lo hagas: pregunta a
Silvestre en la conversación. Ninguna de estas reglas se salta «solo por esta vez».

---

## 1. La línea que no se cruza

El canal existe para **enseñar algo verdadero sobre el humor** y, con ello, ayudar a la
gente a manejarse mejor con los demás. Todo lo que se produzca tiene que dejar internet
mejor de como lo encontró.

**Nunca:**

- Machismo, xenofobia, homofobia, capacitismo, ni humor a costa de un grupo por serlo.
  Un chiste que necesita una víctima colectiva no entra, por bueno que sea el mecanismo.
- Contenido diseñado para indignar, alarmar o angustiar.
- Trucos de manipulación social. La diferencia es simple: enseñar **por qué** funciona algo
  está bien; enseñar **cómo usarlo con alguien que no lo sabe** no.
- Autoayuda sin respaldo. Si no hay estudio, no hay vídeo.

**Cuando el tema sea incómodo** (humor negro, chistes sobre tragedias, el ridículo, la
vergüenza), se trata como lo que es: un objeto de estudio. Se explica el mecanismo, se dice
dónde falla y no se hace el chiste a costa de nadie real.

## 2. Ni un dato inventado

- Toda cifra en pantalla lleva `fuente`, y esa fuente existe en
  `01_bibliografia/BIBLIOGRAFIA_CURADA.md`.
- **El verificador conserva el veto.** Una sola afirmación falsa bloquea la producción.
- Si una gráfica necesita números que no están en el artículo, **no se hace la gráfica**.
  Interpolar puntos de una curva para que quede bonita es fabricar un dato.
- Nunca se busca una fuente para justificar un tema ya decidido. Primero la evidencia,
  luego el vídeo.

## 3. La demanda elige la pregunta; la bibliografía decide si se puede responder

Es la regla que separa «responder a lo que la gente se pregunta» de «clickbait».

Si una pregunta con mucha demanda no tiene respaldo en las 77 obras, **no se hace el
vídeo**: se anota en `05_calendario/pendientes_de_fuente.md`.

## 4. Cero coste

Todo el sistema funciona en el plan gratuito. Si una propuesta requiere pagar algo —una
API, un modelo, una fuente tipográfica, un banco de imágenes—, se descarta o se pregunta
antes. No hay excepciones «por unos céntimos».

## 5. Cero trabajo recurrente para Silvestre

Los cambios pueden pedir **una intervención puntual de setup** (crear una cuenta, activar
un ajuste, aprobar una muestra). No pueden pedir nada que haya que repetir cada semana.

Si un cambio solo funciona con alguien revisando a diario, ese cambio está mal diseñado.

## 6. Nada a nombre de Silvestre, nada con su cara

Las cuentas en otras plataformas son **de la marca**: Mecánica del Humor. Nunca con su
nombre, nunca con su cara, nunca con su imagen personal.

## 7. Nada de fingir que hay una persona

- **No se responden comentarios con IA.** Un comentario automático que finge ser alguien es
  exactamente la basura que este canal no quiere añadir.
- El uso de IA se declara en la descripción de cada vídeo, y se mantiene la declaración
  aunque no sea obligatoria. Desde mayo de 2026 YouTube detecta el contenido de IA
  automáticamente; declararlo antes es más honesto y además evita el marcado automático.
- La pregunta del episodio publicada como primer comentario **sí** vale: es contenido
  editorial, escrito por el guionista, y no finge ser un espectador.

## 8. Nada de spam

- **No** se publica automáticamente en Reddit, foros, grupos ni comentarios de otros
  canales.
- Las publicaciones automáticas en TikTok, Instagram, Bluesky y el pódcast son contenido
  propio en canales propios. Eso no es spam; lo otro sí.

## 9. Nada de material ajeno sin licencia

- **No** se usan clips de cómicos, programas ni películas. Aunque haya argumento de cita,
  un canal automatizado no debe exponerse a un strike.
- La alternativa es mejor y más de marca: **reconstruir** el chiste en el lenguaje visual
  del canal —despiece, diagrama, línea de tiempo— y nombrar la fuente.
- La música lleva su atribución literal. `publicar.py` ya bloquea la publicación si una
  pista no está en `creditos.json`; eso se queda.

## 10. Cómo se cambian las cosas

1. **Un cambio por producción.** Si entran dos y el resultado empeora, no se sabe cuál fue.
2. **Mirar antes de publicar.** Cualquier cambio en `escena.html`, `render.py`, `vista.py`
   o `miniatura.py` dispara la vista previa; se mira el muestrario, no se imagina.
3. **Si sube el coste de render, se mide.** Número de capturas antes y después, anotado en
   `05_calendario/MEJORAS.md`.
4. **Nunca sobre un episodio ya producido.** Los cambios entran en la siguiente producción.
5. **Determinista.** Mismo guion y mismo `t`, mismo píxel. Nada de `Math.random()`.
6. **Nada que dependa de internet en tiempo de render.**
7. **Archivos protegidos** — `voz.py`, `montaje.py`, `.github/workflows/producir.yml`: no se
   tocan sin permiso explícito de Silvestre en la conversación.
8. **`MEJORAS.md` se añade al final, nunca se reescribe.**

## 11. El criterio editorial que no se negocia

Cada vídeo termina explicando **dónde falla** lo que acaba de explicar: los estudios
pequeños, las correlaciones que no son causas, las técnicas que se vuelven en contra.

Reduce el atractivo inmediato y construye lo único que un canal así puede tener como foso:
que se le pueda creer. En un nicho donde casi todo es autoayuda reciclada, ser el que dice
«esto no está tan claro» es la posición más defendible, y la única compatible con el
nombre.

**Esto vale también para los Shorts.** Un Short de cuarenta segundos también puede terminar
con «y esto falla cuando…».

## 12. Y una que es fácil de olvidar

**El canal va de humor. Tiene que hacer gracia.**

Un vídeo que explica la teoría de la ruptura benigna sin provocar una sola ruptura benigna
le está pidiendo al espectador que se fíe de una promesa que el propio vídeo no cumple.

Mínimo: **dos risas por vídeo largo, una de ellas antes del segundo quince.** En un Short,
una, y va primero.
