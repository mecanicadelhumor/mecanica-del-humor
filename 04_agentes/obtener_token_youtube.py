#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obtener_token_youtube.py — saca un refresh token de YouTube para un canal.

Se ejecuta EN TU ORDENADOR, no en GitHub Actions: abre el navegador, te pide
que elijas la cuenta y que autorices, y te devuelve un refresh token que luego
pegas como secreto del repositorio.

    pip install google-auth-oauthlib
    python 04_agentes/obtener_token_youtube.py --client-id XXX --client-secret YYY

Hay que ejecutarlo UNA VEZ POR CANAL, eligiendo cada vez la cuenta de marca
correspondiente:

    Mecánica del Humor  ->  secreto YT_REFRESH_TOKEN
    Humor Mechanics     ->  secreto YT_REFRESH_TOKEN_EN

Por qué existe: los tokens actuales se pidieron solo con permiso de subida, y
la API de analítica de YouTube es otro servicio con su propio ámbito. Sin
`yt-analytics.readonly` no se pueden leer retención, CTR ni suscriptores, que
es justo lo que hace falta para decidir la tanda 2 con datos en vez de con
intuición. Volver a pasar por aquí añade ese permiso sin perder los otros.

Importante: al reautorizar, Google invalida el token anterior de ese cliente y
esa cuenta. Actualiza el secreto en GitHub inmediatamente después, o la
siguiente producción no podrá subir.
"""
import argparse
import os
import sys

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    sys.exit("Falta la librería.  pip install google-auth-oauthlib")

# El orden importa poco, pero la lista tiene que ser completa: si pides menos
# ámbitos de los que ya tenías, el token nuevo puede menos que el viejo.
AMBITOS = [
    "https://www.googleapis.com/auth/youtube.upload",        # subir vídeos
    "https://www.googleapis.com/auth/youtube.force-ssl",     # miniaturas, subtítulos
    "https://www.googleapis.com/auth/yt-analytics.readonly",  # métricas del canal
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-id", default=os.environ.get("YT_CLIENT_ID"))
    ap.add_argument("--client-secret", default=os.environ.get("YT_CLIENT_SECRET"))
    ap.add_argument("--puerto", type=int, default=8080)
    a = ap.parse_args()

    if not a.client_id or not a.client_secret:
        sys.exit("Faltan --client-id y --client-secret (o las variables "
                 "YT_CLIENT_ID / YT_CLIENT_SECRET). Son los mismos que ya "
                 "tienes en los secretos del repositorio.")

    config = {
        "installed": {
            "client_id": a.client_id,
            "client_secret": a.client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    }

    flujo = InstalledAppFlow.from_client_config(config, AMBITOS)
    print("\nSe va a abrir el navegador.")
    print("Elige la cuenta de marca del canal para el que quieres el token")
    print("y acepta los tres permisos que pide.\n")
    # prompt=consent fuerza a Google a devolver refresh_token aunque ya hubiera
    # autorizado antes; sin esto, una reautorización devuelve solo access_token
    # y el script parece funcionar pero no da nada útil.
    cred = flujo.run_local_server(port=a.puerto, prompt="consent",
                                  access_type="offline")

    if not cred.refresh_token:
        sys.exit("Google no ha devuelto refresh token. Revoca el acceso de la "
                 "aplicación en https://myaccount.google.com/permissions y "
                 "vuelve a ejecutar esto.")

    print("\n" + "=" * 68)
    print("REFRESH TOKEN (pégalo en el secreto del repositorio):\n")
    print(cred.refresh_token)
    print("\n" + "=" * 68)
    print("Ámbitos concedidos:")
    for s in (cred.scopes or []):
        print(f"  · {s}")
    print("\nSettings -> Secrets and variables -> Actions:")
    print("  canal español  -> YT_REFRESH_TOKEN")
    print("  canal inglés   -> YT_REFRESH_TOKEN_EN")


if __name__ == "__main__":
    main()
