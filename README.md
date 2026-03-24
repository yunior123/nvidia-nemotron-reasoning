# NVIDIA Nemotron Model Reasoning Challenge

**Kaggle Competition**: [nvidia-nemotron-model-reasoning-challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge)

## Competition Overview

Advance reasoning techniques using NVIDIA Nemotron open models on a novel benchmark of logical reasoning puzzles (bit manipulation, algebraic equations, etc.).

| Detail | Value |
|--------|-------|
| **Goal** | Improve reasoning accuracy of Nemotron-3-Nano-30B via LoRA fine-tuning |
| **Base Model** | [NVIDIA Nemotron-3-Nano-30B-A3B-BF16](https://www.kaggle.com/models/metric/nemotron-3-nano-30b-a3b-bf16) (30B total, 3B active, Mamba-Transformer MoE) |
| **Submission** | `submission.zip` containing LoRA adapter (rank <= 32) + `adapter_config.json` |
| **Evaluation** | Accuracy — model outputs answer in `\boxed{}`, compared to ground truth (exact string or +/-10^-2 tolerance) |
| **Prize Pool** | $106,388 total |
| **Deadline** | June 15, 2026 |
| **License** | CC BY 4.0 |

## Timeline

- **March 16, 2026** — Start Date
- **April 9, 2026** — Midpoint Cut-off (Open Progress Prize)
- **June 8, 2026** — Entry & Team Merger Deadline
- **June 15, 2026** — Final Submission Deadline

## Prizes

**Final Leaderboard:**
- 1st Place: $25,000 + 5 DGX Sparks
- 2nd Place: $15,000 + 2 DGX Sparks
- 3rd Place: $5,000 + 1 DGX Spark

**Open Progress Prize** (midpoint Apr 9): $5,000 + 1 DGX Spark

**Open Contribution Awards** (top 10% only):
- Best Data/Synthetic Data Method — 1 DGX Spark
- Best RL Method — 1 DGX Spark
- Best Fine-tuning Method — 1 DGX Spark

## Inference Parameters (vLLM)

| Parameter | Value |
|-----------|-------|
| max_lora_rank | 32 |
| max_tokens | 7680 |
| top_p | 1.0 |
| temperature | 0.0 |
| max_num_seqs | 64 |
| gpu_memory_utilization | 0.85 |
| max_model_len | 8192 |

## Data

- `train.csv` — id, prompt, answer (logical reasoning puzzles)
- `test.csv` — id, prompt (hidden test set replaces this during scoring)

## Allowed Techniques

- Prompting strategies
- Data filtering and curation
- Synthetic data generation
- Reinforcement learning
- Lightweight fine-tuning
- Any framework (HuggingFace, Unsloth, Axolotl, TRL, etc.)

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Download data (requires Kaggle API key)
./scripts/download_data.sh

# Or manually:
kaggle competitions download -c nvidia-nemotron-model-reasoning-challenge -p data/
unzip data/nvidia-nemotron-model-reasoning-challenge.zip -d data/
```

## Project Structure

```
├── data/              # Competition data (not tracked in git)
├── notebooks/         # EDA and experimentation
├── src/               # Core training and evaluation code
│   ├── data.py        # Data loading and processing
│   ├── train.py       # LoRA fine-tuning
│   ├── evaluate.py    # Local evaluation matching Kaggle metric
│   └── submit.py      # Package LoRA adapter for submission
└── scripts/           # Utility scripts
```

## Key Constraints

- LoRA rank must be <= 32
- Model must output answers in `\boxed{answer}` format
- Submissions evaluated server-side via vLLM (not notebook)
- Fine-tuning should happen on Kaggle/Google Cloud (RTX PRO 6000 Blackwell GPUs)

## Resources

- [Submission Demo Notebook](https://www.kaggle.com/code/ryanholbrook/nvidia-nemotron-submission-demo)
- [NVIDIA Nemotron Metric](https://www.kaggle.com/code/metric/nvidia-nemotron-metric)
- [OpenMathReasoning Dataset](https://huggingface.co/datasets/nvidia/OpenMathReasoning)
- [Nemotron-3-Nano HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16)
- [NeMo-Skills GitHub](https://github.com/NVIDIA/NeMo-Skills)
- [Nemotron-Cascade 2 Paper](https://research.nvidia.com/labs/nemotron/files/Nemotron-Cascade-2.pdf)
