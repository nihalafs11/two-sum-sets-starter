#!/bin/sh
set -e
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Install dependencies
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

