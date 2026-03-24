"""Google Colab bootstrap script.

Run this cell at the start of every Colab session:
    !python colab_setup.py

Or paste into first cell:
    %run colab_setup.py
"""

import os
import subprocess

# 1. Mount Google Drive for persistent storage
from google.colab import drive
drive.mount('/content/drive')

# 2. Clone or pull the repo
REPO_DIR = '/content/nvidia-nemotron-reasoning'
REPO_URL = 'https://github.com/yunior123/nvidia-nemotron-reasoning.git'

if os.path.exists(REPO_DIR):
    subprocess.run(['git', '-C', REPO_DIR, 'pull'], check=True)
    print(f"Updated {REPO_DIR}")
else:
    subprocess.run(['git', 'clone', REPO_URL, REPO_DIR], check=True)
    print(f"Cloned to {REPO_DIR}")

os.chdir(REPO_DIR)

# 3. Install dependencies
subprocess.run(['pip', 'install', '-q', '-r', 'requirements.txt'], check=True)

# 4. Set up Kaggle credentials from Drive (if stored there)
KAGGLE_DIR = os.path.expanduser('~/.kaggle')
DRIVE_KAGGLE = '/content/drive/MyDrive/.kaggle/kaggle.json'
os.makedirs(KAGGLE_DIR, exist_ok=True)

if os.path.exists(DRIVE_KAGGLE):
    import shutil
    shutil.copy(DRIVE_KAGGLE, os.path.join(KAGGLE_DIR, 'kaggle.json'))
    os.chmod(os.path.join(KAGGLE_DIR, 'kaggle.json'), 0o600)
    print("Kaggle credentials loaded from Drive")
else:
    print(f"No kaggle.json at {DRIVE_KAGGLE} — upload manually or set env vars")

# 5. Download competition data if not present
DATA_DIR = os.path.join(REPO_DIR, 'data')
if not os.path.exists(os.path.join(DATA_DIR, 'train.csv')):
    subprocess.run([
        'kaggle', 'competitions', 'download',
        '-c', 'nvidia-nemotron-model-reasoning-challenge',
        '-p', DATA_DIR
    ], check=True)
    subprocess.run(['unzip', '-o', f'{DATA_DIR}/*.zip', '-d', DATA_DIR])
    print("Competition data downloaded")
else:
    print("Competition data already present")

# 6. Check GPU
import torch
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB")
else:
    print("WARNING: No GPU detected!")

print("\nSetup complete. Ready to train.")
