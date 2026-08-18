@echo off
REM ===================================================================
REM sincronizar.cmd - empuja a GitHub lo que Cowork haya dejado escrito.
REM
REM Por que existe: Cowork escribe y hace commit en esta carpeta a traves
REM del puente con tu ordenador, pero ese puente no tiene red, y su
REM contenedor en la nube no tiene credenciales de este repositorio. El
REM unico sitio donde coinciden los ficheros y el acceso a GitHub es tu
REM maquina. Esto cierra ese hueco.
REM
REM Registrar en el Programador de tareas de Windows:
REM   - Al iniciar sesion
REM   - Y ademas cada 15 minutos, indefinidamente
REM   Accion: iniciar programa -> C:\MisProyectos\Humor\sincronizar.cmd
REM
REM Solo empuja commits que ya existen. No crea ninguno, no fusiona nada
REM y no toca ficheros: si no hay nada pendiente, no hace nada.
REM ===================================================================

cd /d "%~dp0"

for /f "delims=" %%B in ('git rev-parse --abbrev-ref HEAD 2^>nul') do set RAMA=%%B
if "%RAMA%"=="" (
  echo [%date% %time%] No es un repositorio git. >> "%~dp0_sincronizar.log"
  exit /b 0
)

git diff --quiet && git diff --cached --quiet
if errorlevel 1 (
  echo [%date% %time%] Hay cambios SIN commitear en %RAMA%; no se empuja nada. >> "%~dp0_sincronizar.log"
  exit /b 0
)

git push origin %RAMA% > "%~dp0_sincronizar.tmp" 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR al empujar %RAMA%: >> "%~dp0_sincronizar.log"
  type "%~dp0_sincronizar.tmp" >> "%~dp0_sincronizar.log"
) else (
  findstr /C:"Everything up-to-date" "%~dp0_sincronizar.tmp" > nul
  if errorlevel 1 echo [%date% %time%] Empujado %RAMA% a origin. >> "%~dp0_sincronizar.log"
)
del "%~dp0_sincronizar.tmp" 2> nul
exit /b 0
