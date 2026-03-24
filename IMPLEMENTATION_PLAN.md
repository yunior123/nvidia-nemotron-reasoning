# Implementation Plan — Nemotron Reasoning Challenge

## Phase 1: Data Understanding & Analysis
- [ ] Analyze train.csv: count puzzles by category (bit manipulation vs algebraic vs other)
- [ ] Analyze answer distribution: types (numeric, binary, string), lengths
- [ ] Analyze prompt structure: identify patterns, input-output examples format
- [ ] Create `notebooks/01_eda.py` with full EDA (not .ipynb — plain Python for git-friendliness)
- [ ] Write `tests/test_data.py` — verify data loading, format expectations

## Phase 2: Evaluation Pipeline
- [ ] Enhance `src/evaluate.py` — handle edge cases: nested boxed, multiple boxed, fractions, scientific notation
- [ ] Write `tests/test_evaluate.py` — unit tests for answer extraction with 20+ test cases
- [ ] Create `src/metric.py` — replicate exact Kaggle metric logic (reference: https://www.kaggle.com/code/metric/nvidia-nemotron-metric)
- [ ] Verify metric matches Kaggle's by testing against known train.csv answers

## Phase 3: Prompt Engineering & Data Preparation
- [ ] Create `src/prompts.py` — prompt templates that produce `\boxed{}` output
- [ ] Create `src/data_prep.py` — format training data as instruction-response pairs with boxed answers
- [ ] Generate `data/train_formatted.jsonl` — training data in chat/instruct format
- [ ] Write `tests/test_prompts.py` — verify all formatted data has `\boxed{}` in response
- [ ] Analyze which puzzle categories are hardest (prepare for targeted augmentation)

## Phase 4: Training Infrastructure (Colab/Kaggle-ready)
- [ ] Create `notebooks/02_train_lora.py` — LoRA fine-tuning script for Colab/Kaggle
  - Uses PEFT library
  - Configurable rank (default 16, max 32)
  - Loads Nemotron-3-Nano-30B from HuggingFace
  - Saves adapter to `adapters/` directory
  - Includes checkpointing every N steps
- [ ] Create `notebooks/03_inference.py` — test adapter locally on sample puzzles
- [ ] Update `src/submit.py` — validate adapter_config.json rank ≤ 32 before packaging
- [ ] Create `scripts/kaggle_train.sh` — one-liner to run training on Kaggle notebook

## Phase 5: Synthetic Data & Augmentation
- [ ] Create `src/augment.py` — generate synthetic reasoning traces for training data
- [ ] Implement chain-of-thought augmentation: step-by-step solutions ending in `\boxed{}`
- [ ] Create difficulty-stratified training splits
- [ ] Write `tests/test_augment.py` — verify augmented data quality

## Phase 6: Submission Pipeline
- [ ] Create end-to-end submission test: dummy adapter → submit.py → submission.zip → verify structure
- [ ] Update `scripts/submit.sh` — add validation before upload
- [ ] Create `scripts/leaderboard.sh` — fetch and display current leaderboard position
- [ ] Document full workflow in README.md

## Phase 7: First Real Submission (requires GPU — document instructions)
- [ ] Write clear instructions in `SUBMISSION_GUIDE.md` for running on Colab/Kaggle
- [ ] Include exact commands to: train → save adapter → download → submit
- [ ] Create `notebooks/04_full_pipeline.py` — complete train+eval+submit pipeline for Colab
