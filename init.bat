@echo off
setlocal

set VENV_DIR=venv

if exist %VENV_DIR% (
    echo Virtual environment found. Activating...
    call %VENV_DIR%\Scripts\activate
) else (
    echo Virtual environment not found. Creating...
    python -m venv %VENV_DIR%
    call %VENV_DIR%\Scripts\activate
    echo Installing dependencies...
    pip install --upgrade pip
    pip install -r requirements.txt
)

if not exist config.txt (
    echo Config file not found. Creating...
    copy config.txt.example config.txt
)

cmd /k
