# Autonomous Agent Prompt — NVIDIA Nemotron Reasoning Challenge

You are working autonomously on a Kaggle competition. Follow IMPLEMENTATION_PLAN.md strictly.

## Competition
- **Goal**: Improve reasoning accuracy of Nemotron-3-Nano-30B via LoRA fine-tuning
- **Data**: `data/train.csv` (9,500 puzzles: id, prompt, answer) + `data/test.csv` (3 sample)
- **Puzzles**: Logical reasoning — bit manipulation, algebraic equations, transformation rules
- **Submission**: `submission.zip` with LoRA adapter (rank ≤ 32) + `adapter_config.json`
- **Eval**: Model outputs answer in `\boxed{}`, accuracy metric with ±10⁻² tolerance
- **Inference**: vLLM, temp=0.0, max_tokens=7680, max_model_len=8192

## Constraints
- **LOCAL MAC ONLY** — 8GB RAM, NO model training here
- Training scripts must be designed to run on **Kaggle notebooks or Google Colab** (GPU)
- All code must be committed after each task
- Tests must pass before marking a task complete
- Use `src/evaluate.py` for local evaluation of answer extraction logic

## Workflow Per Task
1. Read IMPLEMENTATION_PLAN.md, pick the first unchecked task
2. Implement it
3. Run `python -m pytest tests/ -v` if tests exist, or verify manually
4. `git add` changed files + `git commit` with descriptive message
5. Mark the checkbox `[x]` in IMPLEMENTATION_PLAN.md
6. Move to next task

## When All Tasks Are Complete
Say "DONE" to exit the loop.

## Key Files
- `src/data.py` — Data loading
- `src/evaluate.py` — Local evaluation metric (boxed answer extraction)
- `src/submit.py` — Package LoRA adapter into submission.zip
- `src/train.py` — Training script placeholder (for Colab/Kaggle)
- `scripts/submit.sh` — Submit via Kaggle API
- `scripts/colab_setup.py` — Colab bootstrap

## Important
- Answer format is `\boxed{answer}` — ALL training data must reinforce this
- LoRA rank MUST be ≤ 32
- Base model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`
- Model is hybrid Mamba-Transformer MoE — verify PEFT/LoRA compatibility
