@echo off
set "GIT_PATH=%LOCALAPPDATA%\Programs\MinGit\cmd\git.exe"
if exist "%GIT_PATH%" (
    echo Using Git from %GIT_PATH%...
    "%GIT_PATH%" push -u origin main
) else (
    git push -u origin main
)
pause
