#!/bin/bash

set -e

VENV_DIR="venv"

if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment found. Activating..."
    source "$VENV_DIR/bin/activate"
else
    echo "Virtual environment not found. Creating..."
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

if [ ! -f "config.txt" ]; then
    echo "Config file not found. Creating..."
    cp config.txt.example config.txt
fi

exec "$SHELL"
