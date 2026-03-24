"""Local evaluation matching the Kaggle metric.

Extracts answer from \\boxed{} and compares to ground truth.
Matches: exact string or numerical tolerance of 10^-2.
"""

import re


def extract_boxed_answer(text: str) -> str | None:
    """Extract the last \\boxed{...} content from model output."""
    matches = re.findall(r"\\boxed\{([^}]*)\}", text)
    if matches:
        return matches[-1].strip()
    # Fallback: last numeric value
    nums = re.findall(r"-?\d+\.?\d*", text)
    return nums[-1] if nums else None


def answers_match(predicted: str | None, ground_truth: str) -> bool:
    """Check if predicted answer matches ground truth."""
    if predicted is None:
        return False
    # Exact string match
    if predicted.strip() == ground_truth.strip():
        return True
    # Numerical tolerance
    try:
        pred_num = float(predicted)
        gt_num = float(ground_truth)
        if gt_num == 0:
            return abs(pred_num) < 1e-2
        return abs(pred_num - gt_num) / abs(gt_num) < 1e-2
    except (ValueError, ZeroDivisionError):
        return False


def compute_accuracy(predictions: list[str], ground_truths: list[str]) -> float:
    """Compute accuracy score matching Kaggle metric."""
    correct = sum(
        answers_match(extract_boxed_answer(pred), gt)
        for pred, gt in zip(predictions, ground_truths)
    )
    return correct / len(ground_truths) if ground_truths else 0.0
