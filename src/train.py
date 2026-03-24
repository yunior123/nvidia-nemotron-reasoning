"""LoRA fine-tuning script for Nemotron-3-Nano-30B.

NOTE: This must run on GPU (Kaggle/Google Cloud), NOT local Mac.
"""

# Placeholder — actual training will be done in Kaggle notebooks
# with access to RTX PRO 6000 Blackwell GPUs.
#
# Key parameters to match evaluation:
#   - Base model: nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
#   - LoRA rank: <= 32
#   - Output format: model must produce \boxed{answer}
#   - max_model_len: 8192
#
# Recommended frameworks:
#   - Unsloth (fast LoRA fine-tuning)
#   - Axolotl (config-driven training)
#   - TRL (HuggingFace RL training)
#   - PEFT (standard LoRA)
#
# Training data format:
#   Each sample should include the puzzle prompt and
#   a solution that ends with \boxed{answer}.
