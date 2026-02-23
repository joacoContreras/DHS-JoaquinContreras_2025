#!/bin/bash
# Script para ejecutar el compilador fácilmente
# Uso: ./ejecutar.sh [archivo_entrada]
# Ejemplo: ./ejecutar.sh input/sinErrores.txt

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python3"
APP="$SCRIPT_DIR/src/main/python/App.py"

# Verificar que existe el venv
if [ ! -f "$VENV_PYTHON" ]; then
    echo "Error: No se encontró el entorno virtual en .venv/"
    echo "Crealo con: python3 -m venv .venv && .venv/bin/pip install antlr4-python3-runtime"
    exit 1
fi

# Archivo por defecto si no se pasa argumento
INPUT="${1:-input/stress_test_large.txt}"

exec "$VENV_PYTHON" "$APP" "$INPUT"
