@echo off
setlocal enabledelayedexpansion
REM ===================================================================
REM sincronizar.cmd - empuja a GitHub lo que Cowork haya dejado escrito.
REM
REM Por que existe: Cowork escribe y hace commit en esta carpeta a traves
REM del puente con tu ordenador, pero ese puente no tiene red, y su
REM contenedor en la nube no tiene credenciales de este repositorio. El
REM unico sitio donde coinciden los ficheros y el acceso a GitHub es tu
REM maquina.
REM
REM Registrar en el Programador de tareas de Windows:
REM   - Al iniciar sesion, y ademas cada hora
REM   - "Ejecutar solo cuando el usuario haya iniciado sesion"
REM   - Accion: iniciar programa -> C:\MisProyectos\Humor\sincronizar.cmd
REM     Iniciar en (opcional) -> C:\MisProyectos\Humor
REM
REM Solo empuja commits que ya existen. No crea ninguno, no fusiona nada
REM y no toca ficheros: si no hay nada pendiente, no hace nada.
REM ===================================================================

cd /d "%~dp0"
set "LOG=%~dp0_sincronizar.log"

REM -------------------------------------------------------------------
REM El Programador de tareas no carga tu perfil igual que una consola.
REM Sin HOME, ssh no encuentra ni ~/.ssh/config ni tu clave, y GitHub
REM responde "Permission denied (publickey)" aunque desde tu terminal
REM funcione perfectamente. Esto es lo que fallaba el 18/08.
REM -------------------------------------------------------------------
if not defined HOME set "HOME=%USERPROFILE%"
set "GIT_SSH_COMMAND=ssh -o BatchMode=yes"
set "GIT_TERMINAL_PROMPT=0"

for /f "delims=" %%B in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set "RAMA=%%B"
if "%RAMA%"=="" (
  echo [%date% %time%] No es un repositorio git.>> "%LOG%"
  exit /b 0
)

git diff --quiet && git diff --cached --quiet
if errorlevel 1 (
  echo [%date% %time%] Hay cambios SIN commitear en %RAMA%; no se empuja nada.>> "%LOG%"
  exit /b 0
)

git rev-list --count "origin/%RAMA%..HEAD" > "%~dp0_sinc.tmp" 2>nul
set "PENDIENTES=0"
for /f "delims=" %%N in ('type "%~dp0_sinc.tmp" 2^>nul') do set "PENDIENTES=%%N"
del "%~dp0_sinc.tmp" 2>nul
if "%PENDIENTES%"=="0" exit /b 0

REM --- Intento 1: por SSH, que es como esta configurado el remoto ---
git push origin %RAMA% > "%~dp0_sinc.tmp" 2>&1
if not errorlevel 1 (
  echo [%date% %time%] Empujados %PENDIENTES% commits a %RAMA% por SSH.>> "%LOG%"
  del "%~dp0_sinc.tmp" 2>nul
  exit /b 0
)

echo [%date% %time%] SSH fallo al empujar %RAMA%:>> "%LOG%"
type "%~dp0_sinc.tmp" >> "%LOG%"
del "%~dp0_sinc.tmp" 2>nul

REM -------------------------------------------------------------------
REM Intento 2: por HTTPS con el token personal de .secrets\gh_token.
REM
REM La salida de git NO se vuelca al log en esta rama: cuando falla,
REM git repite la URL completa en el mensaje de error, y esa URL lleva el
REM token dentro. Un log con un token dentro es un token publicado.
REM -------------------------------------------------------------------
if not exist "%~dp0.secrets\gh_token" (
  echo [%date% %time%] No hay .secrets\gh_token: no se puede reintentar por HTTPS.>> "%LOG%"
  exit /b 1
)
set "TOKEN="
for /f "usebackq delims=" %%T in ("%~dp0.secrets\gh_token") do if not defined TOKEN set "TOKEN=%%T"

git push https://x-access-token:!TOKEN!@github.com/mecanicadelhumor/mecanica-del-humor.git %RAMA% > nul 2>&1
if errorlevel 1 (
  echo [%date% %time%] HTTPS tambien fallo. Revisa que el token no haya caducado y que tenga permiso Contents: write.>> "%LOG%"
  exit /b 1
)
echo [%date% %time%] Empujados %PENDIENTES% commits a %RAMA% por HTTPS ^(SSH no estaba disponible^).>> "%LOG%"
exit /b 0
