# Siguientes pasos

Ordenados por lo que desbloquea más. Los tres primeros los tienes que hacer tú porque requieren
cuentas a tu nombre; a partir del cuarto, el trabajo vuelve a ser mío.

---

## Lo que solo puedes hacer tú (≈45 minutos en total)

### 1. Crear los dos canales de YouTube — 10 min · **bloquea todo lo demás**

Los handles no se reservan sin canal, y cada día que pasa alguien puede cogerlos.

- `@mecanicadelhumor` — nombre: **Mecánica del Humor**
- `@humormechanics` — nombre: **Humor Mechanics**

Las descripciones están escritas en `02_marca/NOMBRE_Y_MARCA.md`, listas para copiar y pegar.

### 2. Crear el repositorio en GitHub — 15 min · **desbloquea la producción**

Es la pieza que le da internet al sistema. Mi contenedor puede escribir en un repositorio, pero no
puede crear uno desde cero.

```bash
# en tu ordenador, dentro de C:\MisProyectos\Humor
git init
git add .
git commit -m "Mecánica del Humor: bibliografía, marca, pipeline, agentes y 8 guiones"
gh repo create mecanica-del-humor --public --source=. --push
```

Después mueve el flujo de trabajo a donde GitHub lo busca:

```bash
mkdir -p .github/workflows
mv 03_produccion/.github/workflows/producir.yml .github/workflows/
git add . && git commit -m "workflow en su sitio" && git push
```

> **Público, no privado.** En repositorios públicos los minutos de Actions son ilimitados; en
> privados son 2.000 al mes. Aquí no hay nada secreto: las claves van como *secrets*, nunca en el
> código.

### 3. Cargar los secretos — 20 min

En *Settings → Secrets and variables → Actions*:

| Secreto | De dónde sale |
|---|---|
| `GEMINI_API_KEY` | La que ya tienes de Google AI Studio |
| `YT_CLIENT_ID` · `YT_CLIENT_SECRET` | Google Cloud Console → nuevo proyecto → activar *YouTube Data API v3* → credenciales OAuth de aplicación de escritorio |
| `YT_REFRESH_TOKEN` | Se obtiene una sola vez con el flujo OAuth. Si te atascas, dímelo y te preparo el script |

---

## Lo que hago yo en cuanto exista el repositorio

### 4. Primera ejecución real y ajuste del ritmo

Lanzar `producir.yml` sobre `MDH-001` y revisar lo único que no he podido probar: cómo suena la voz
y si las duraciones reales cuadran con las estimadas. Ahora mismo el render calcula a 150 palabras
por minuto; con el primer audio real se calibra al valor exacto de la voz elegida y todo el
calendario se recalcula solo.

### 5. Producir los ocho vídeos en español

Ocho ejecuciones. Salen en privado, con miniatura y subtítulos, listos para tu revisión. Coste: cero.

### 6. Adaptar los ocho al inglés

No traducir: **readaptar**. Los ejemplos culturales cambian, los juegos de palabras se sustituyen por
otros equivalentes y el ritmo se ajusta, porque el inglés es más corto. Un chiste traducido literal
deja de ser un chiste.

### 7. Montar las tres tareas programadas

| Cuándo | Qué |
|---|---|
| Lunes 08:00 | Analista lee métricas → editor jefe ajusta el calendario |
| Lunes 10:00 | Guionista → chistólogo → verificador → commit → dispara Actions |
| Diario 20:00 | Comprobar que las Actions terminaron y avisarte de lo que espera aprobación |

### 8. Cerrar los cabos sueltos del pipeline

- Música de cama: elegir tres piezas libres de derechos y meterlas en `03_produccion/assets/musica/`.
- Un tipo de escena `figura` con gráficas de matplotlib, para los vídeos con datos.
- Ejecutar `fetch_biblio.py` con internet para descargar los PDF en abierto y generar las fichas de
  hallazgo, que es lo que el guionista leerá a partir de la tanda 2.

---

## Decisiones que te tocan a ti antes del 8 de agosto

1. **¿Te convence «Mecánica del Humor»?** Si no, en `02_marca/` hay dos alternativas con los handles
   ya verificados. Cambiar el nombre ahora cuesta diez minutos; dentro de un mes, mucho más.
2. **¿Martes y viernes a las 18:00?** Es la parrilla propuesta. Se cambia en una línea del calendario.
3. **¿Cuánto quieres revisar?** Ahora mismo está montado para que apruebes cada vídeo antes de
   publicarlo. Cuando lleves tres semanas sin rechazar nada, quitamos ese paso y el canal queda solo.
4. **¿Empezamos publicando el 11 de agosto?** El calendario asume que sí. Si prefieres acumular los
   ocho antes de publicar el primero, también es defendible: se ve el conjunto antes de exponerlo.

---

## Riesgos que conviene tener presentes

| Riesgo | Qué hacemos |
|---|---|
| YouTube endurece su política sobre contenido producido en masa | Menos vídeos y mejores. Tesis propia en cada uno, nunca plantilla rellenada. Declarar el uso de IA en la descripción |
| Microsoft rompe `edge-tts` | Gemini TTS ya está contemplado como respaldo; Piper local como último recurso |
| Un dato citado resulta falso | El verificador tiene veto y bloquea la producción. Es el agente más importante del sistema |
| El canal no arranca | Por eso son ocho y no veinte. El 5 de septiembre habrá datos de cuatro formatos y se decide con ellos, no con intuición |
| Se agota la cuota gratuita de Gemini | Lo único crítico es el guion, y ese lo escribo yo. El resto degrada a plantillas sin romperse |

---

## Un apunte sobre el criterio editorial

Hay una tentación evidente en este nicho: convertirlo en un canal de trucos. «Cinco frases para caer
bien», «el truco para que se rían de tus chistes». Funcionaría a corto plazo.

Recomiendo no hacerlo, y el calendario está construido para evitarlo. Cada vídeo termina explicando
**dónde falla** lo que acaba de explicar: los estudios pequeños, las correlaciones que no son causas,
las técnicas que se vuelven en contra. Eso reduce el atractivo inmediato y a cambio construye lo
único que un canal así puede tener como foso: que se le pueda creer.

En un nicho donde casi todo es autoayuda reciclada, ser el que dice «esto no está tan claro» es una
posición muy defendible. Y es la única compatible con el nombre.
