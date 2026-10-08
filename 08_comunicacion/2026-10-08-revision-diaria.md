# Revisión diaria · 2026-10-08

- **Para la dirección:** MDS-034 no se produjo esta madrugada: «Instalar dependencias» de `producir.yml` (apt + `playwright install --with-deps`) se colgó 20 min y murió por timeout (run 37743064273). Ya pasó la barrera del `unattended-upgrades` del workflow, así que el cuelgue es otro (¿mirror de apt o descarga de Chromium?). Si hay reintento y vuelve a colgarse, conviene un `timeout` más corto por intento con repetición.
- **Para la planificación:** MDS-035 lo editó la revisión (esc. 4 «ejercicio neutro» y cierre sin el callback del micro apagado: dos lectores no lo entendieron). Un cierre con callback a una escena de 40 s antes necesita decirlo en claro. Mira `lectura_en_frio` del guion y `ajustes.json` (texto arriba en 1–3).
