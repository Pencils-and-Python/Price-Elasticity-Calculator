"""utils/loaders.py"""

import pandas as pd
import joblib
from pathlib import Path

def load_model(model_path: Path):
    """Load the trained model from disk."""
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return joblib.load(model_path)


def load_csv(csv_path: Path):
    """Load a CSV file and return a DataFrame."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    return pd.read_csv(csv_path)
