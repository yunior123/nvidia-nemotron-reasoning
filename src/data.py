"""Data loading and processing for the Nemotron Reasoning Challenge."""

import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_train() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "train.csv")


def load_test() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "test.csv")


def format_prompt(prompt: str) -> str:
    """Format a puzzle prompt for the model, instructing boxed output."""
    return (
        f"{prompt}\n\n"
        "Please solve this step by step. "
        "Put your final answer within \\boxed{}."
    )
