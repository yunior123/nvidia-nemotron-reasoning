@~/CLAUDE.md

# NVIDIA Nemotron Reasoning Challenge

## Project
- Kaggle competition: LoRA fine-tune Nemotron-3-Nano-30B for logical reasoning
- Submission: `submission.zip` with LoRA adapter (rank <= 32) + `adapter_config.json`
- Eval: accuracy via `\boxed{}` answer extraction, tolerance 10^-2

## Constraints
- 8GB local RAM — ALL training on Kaggle notebooks or Google Colab, NOT local Mac
- vLLM inference: temp=0.0, max_tokens=7680, max_model_len=8192
- Model: Nemotron-3-Nano-30B-A3B (hybrid Mamba-Transformer MoE)

## Test Command
```bash
python -m pytest tests/ -v
```

## Stack
- Python 3.10+
- transformers, peft, vllm, datasets, pandas
- Training frameworks: Unsloth, Axolotl, TRL (pick best for Mamba-Transformer MoE)

## Kaggle Integration
- **MCP**: Official Kaggle MCP at `https://www.kaggle.com/mcp` (configured in `.mcp.json`)
- **Submit**: `./scripts/submit.sh <adapter_dir>` — uploads submission.zip via API (file competition, no browser needed)
- **Check score**: `./scripts/check_score.sh`
- **Deploy notebook**: `git push` → GitHub Actions → `kaggle kernels push`
- **API auth**: Bearer token KGAT format, stored in macOS keychain as `KAGGLE_API_TOKEN`

## Cloud Compute
- **Kaggle Notebooks**: RTX PRO 6000 Blackwell (G4 VM), 30h/week free GPU
- **Google Colab**: T4 free / A100 Pro, bootstrap with `scripts/colab_setup.py`
- **Data path on Kaggle**: `/kaggle/input/competitions/nvidia-nemotron-model-reasoning-challenge/`
- Local Mac = code editing + EDA only (3MB dataset fits in RAM)

## Key Deadlines
- April 9, 2026 — Midpoint (Open Progress Prize: $5K + DGX Spark)
- June 8, 2026 — Entry & team merger deadline
- June 15, 2026 — Final submission deadline
