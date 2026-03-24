"""Package a LoRA adapter into submission.zip for Kaggle."""

import zipfile
from pathlib import Path


def create_submission(adapter_dir: str, output_path: str = "submission.zip") -> str:
    """Package LoRA adapter directory into submission.zip.

    The adapter directory must contain adapter_config.json and adapter weights.
    LoRA rank must be <= 32.
    """
    adapter_path = Path(adapter_dir)
    if not (adapter_path / "adapter_config.json").exists():
        raise FileNotFoundError(
            f"adapter_config.json not found in {adapter_dir}"
        )

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in adapter_path.rglob("*"):
            if file.is_file():
                zf.write(file, file.relative_to(adapter_path))

    print(f"Created {output_path} from {adapter_dir}")
    return output_path


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m src.submit <adapter_dir> [output.zip]")
        sys.exit(1)
    out = sys.argv[2] if len(sys.argv) > 2 else "submission.zip"
    create_submission(sys.argv[1], out)
