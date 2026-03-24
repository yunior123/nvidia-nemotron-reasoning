#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="$SCRIPT_DIR/../data"

echo "Downloading competition data..."
kaggle competitions download -c nvidia-nemotron-model-reasoning-challenge -p "$DATA_DIR"

echo "Extracting..."
cd "$DATA_DIR"
unzip -o nvidia-nemotron-model-reasoning-challenge.zip
rm -f nvidia-nemotron-model-reasoning-challenge.zip

echo "Done. Files:"
ls -la "$DATA_DIR"/*.csv
