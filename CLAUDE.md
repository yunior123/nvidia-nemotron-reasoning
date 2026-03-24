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
