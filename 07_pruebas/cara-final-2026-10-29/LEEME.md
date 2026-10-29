# Muestra · el personaje acaba alegre (29/10/2026)

El codirector, en su cuaderno (después del 26/10): *«termina con cara triste el muñeco […] si en esos
segundos finales podría haber una transición de cara triste a cara alegre, manteniendo el mismo timing.
[…] No me gusta mucho que nuestra imagen del canal sea cara triste, y menos al final del vídeo»*.

Tiene razón y no es un caso suelto: **22 de los últimos 27 cierres llevan al personaje en «duda»**, la boca
torcida hacia abajo, porque el cierre es donde va el límite del estudio (regla 12). Y el personaje es lo
único que se queda en pantalla con la tarjeta «Síguenos»: la última imagen del Short era una cara triste.

Regla 11.2: **no entra en producción hasta que él lo vea.** Esta carpeta es lo que tiene que ver.

- **`final_risa.mp4`** — el cierre de `MDS-045` con la cola (b) ya aplicada y el personaje que pasa a
  «rie» cuando entra la tarjeta.
- **`final_ahora.mp4`** — lo mismo, como sale desde el 30/10 (cola (b), cara de «duda» hasta el final).
- **`fotogramas_finales.jpg`** — el personaje a 1,8 · 1,55 · 1,45 · 1,35 · 1,25 · 0,2 s del final
  (arriba ahora, abajo con la risa).

La etiqueta negra de arriba a la izquierda no sale en el Short; el fondo gris hace de vídeo de archivo y
no hay música (como en la muestra de la cola del 26/10).

## Qué cambia (en `cara_final.diff`, sin aplicar: solo `escena.html`)

- **El mismo timing**: nada se alarga. El cambio empieza al entrar la tarjeta (1,5 s del final) y dura
  0,35 s: la boca de antes se apaga mientras se enciende la sonrisa, las cejas cambian a mitad, y el
  personaje da un saltito de un 7 %. Después se queda sonriendo hasta el final.
- **Solo en el cierre vertical y solo si el personaje no estaba ya riendo.** El resto de escenas, igual:
  la «duda» del límite se sigue viendo mientras se dice el límite.
- Coste de render: cero (no hay capturas nuevas).

`cara_muestra.py` hace los dos vídeos (`python3 cara_muestra.py <carpeta temporal>`); `escena_ahora.html`
y `escena_risa.html` son las dos versiones del fichero que usa.
