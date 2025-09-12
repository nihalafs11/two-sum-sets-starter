#!/bin/sh
set -e
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$SCRIPT_DIR"
if [ -d env ]; then
  . env/bin/activate
fi
pytest -q
