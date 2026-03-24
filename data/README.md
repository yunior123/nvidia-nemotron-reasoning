# Data

Download competition data:

```bash
kaggle competitions download -c nvidia-nemotron-model-reasoning-challenge -p data/
unzip data/nvidia-nemotron-model-reasoning-challenge.zip -d data/
```

## Files
- `train.csv` — id, prompt, answer
- `test.csv` — id, prompt (replaced by hidden test set during scoring)
