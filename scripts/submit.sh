#!/bin/bash
set -e

ADAPTER_DIR="${1:?Usage: ./scripts/submit.sh <adapter_dir> [description]}"
DESCRIPTION="${2:-Submission from CLI}"
COMPETITION="nvidia-nemotron-model-reasoning-challenge"

# Get token from keychain or env
TOKEN="${KAGGLE_TOKEN:-$(security find-generic-password -s KAGGLE_API_TOKEN -w ~/.secrets/vault.keychain-db 2>/dev/null)}"
if [ -z "$TOKEN" ]; then
    TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.kaggle/kaggle.json'))['key'])" 2>/dev/null)
fi

if [ -z "$TOKEN" ]; then
    echo "Error: No Kaggle API token found"
    exit 1
fi

# Package adapter into submission.zip
echo "Packaging $ADAPTER_DIR into submission.zip..."
cd "$ADAPTER_DIR"
zip -r /tmp/submission.zip .
cd -

# Submit via API
echo "Submitting to $COMPETITION..."
RESPONSE=$(curl -s -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -F "submissionFile=@/tmp/submission.zip" \
    -F "submissionDescription=$DESCRIPTION" \
    "https://www.kaggle.com/api/v1/competitions/submissions/$COMPETITION")

echo "Response: $RESPONSE"
rm -f /tmp/submission.zip

echo ""
echo "Check score: ./scripts/check_score.sh"
