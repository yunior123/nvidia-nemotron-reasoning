#!/bin/bash
COMPETITION="nvidia-nemotron-model-reasoning-challenge"

TOKEN="${KAGGLE_TOKEN:-$(security find-generic-password -s KAGGLE_API_TOKEN -w ~/.secrets/vault.keychain-db 2>/dev/null)}"
if [ -z "$TOKEN" ]; then
    TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.kaggle/kaggle.json'))['key'])" 2>/dev/null)
fi

echo "Latest submissions for $COMPETITION:"
curl -s -H "Authorization: Bearer $TOKEN" \
    "https://www.kaggle.com/api/v1/competitions/submissions/list/$COMPETITION" \
    | python3 -m json.tool 2>/dev/null || \
    curl -s -H "Authorization: Bearer $TOKEN" \
    "https://www.kaggle.com/api/v1/competitions/submissions/list/$COMPETITION"
