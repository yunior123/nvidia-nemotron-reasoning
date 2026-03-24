#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="$SCRIPT_DIR/../data"

# Get token from keychain or kaggle.json
TOKEN="${KAGGLE_TOKEN:-$(security find-generic-password -s KAGGLE_API_TOKEN -w ~/.secrets/vault.keychain-db 2>/dev/null)}"
if [ -z "$TOKEN" ]; then
    TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.kaggle/kaggle.json'))['key'])" 2>/dev/null)
fi

echo "Downloading competition data..."
curl -L -H "Authorization: Bearer $TOKEN" \
  "https://www.kaggle.com/api/v1/competitions/data/download-all/nvidia-nemotron-model-reasoning-challenge" \
  -o "$DATA_DIR/data.zip"

echo "Extracting..."
cd "$DATA_DIR"
unzip -o data.zip
rm -f data.zip

echo "Done. Files:"
ls -la "$DATA_DIR"/*.csv
