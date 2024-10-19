$ErrorActionPreference = "Stop"

$VENV_DIR = "venv"

if (Test-Path $VENV_DIR) {
    Write-Output "Virtual environment found. Activating..."
    & "$VENV_DIR\Scripts\Activate.ps1"
} else {
    Write-Output "Virtual environment not found. Creating..."
    python -m venv $VENV_DIR
    & "$VENV_DIR\Scripts\Activate.ps1"
    Write-Output "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
}

if (-Not (Test-Path "config.txt")) {
    Write-Output "Config file not found. Creating..."
    Copy-Item "config.txt.example" "config.txt"
}

$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") > $null
