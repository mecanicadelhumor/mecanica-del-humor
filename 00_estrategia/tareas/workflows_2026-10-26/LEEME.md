# Workflow preparado para que lo muevas tú (26/10/2026)

**Qué es**: `presentador_prueba.yml`, el mismo que ya tienes, con **el paso «Dependencias» arreglado**.
`.github/workflows/` no lo puedo escribir yo (trampa 18); por eso se queda aquí.

**Por qué**: el 26/10, en dos ejecuciones seguidas (14:35 y 14:47 UTC), el paso se quedó colgado en
`apt-get update` sin escribir una línea y murió a los 10 minutos. No es culpa del cuaderno de Kaggle ni
del código: es el instalador de paquetes del runner de GitHub, que a veces se queda esperando a su
servidor. Cuando pasa, la prueba no llega ni a empezar.

**Qué cambia** (solo ese paso): apt con reintentos y su propio tope de tiempo, que si falla no tumba el
paso; `ffmpeg` y la fuente solo se piden **si no están ya** en el runner; y si al final no hay `ffmpeg`,
el run para con un error claro en vez de reventar más adelante. El paso pasa de 10 a 15 minutos. **Lo
demás del fichero es idéntico**, incluidos los secretos.

**Cómo moverlo** (2 minutos, cuando puedas; no corre prisa: mientras tanto se puede relanzar y a veces
sale a la primera):

1. GitHub → repositorio público → **`.github/workflows/presentador_prueba.yml`** → el lápiz (editar).
2. Borra todo el contenido y pega entero el de
   **`00_estrategia/tareas/workflows_2026-10-26/presentador_prueba.yml`**.
3. **Commit** directamente en `main`. No hace falta ningún secreto nuevo ni cambiar nada más.

Si prefieres no tocarlo, dilo en el cuaderno y lo dejo como está: solo significa que algún relanzamiento
se perderá de vez en cuando.
