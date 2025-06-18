"""utils/loaders.py"""

import os
import urllib.request
import gdown
import pandas as pd
import joblib
from pathlib import Path

# === Constants ===
MODEL_URL = "https://drive.google.com/uc?export=download&id=19C0rN2QWdOOFRZs1rTh3uCw3v4IRrZBr"
MODEL_PATH = Path("data/trained_model/random_forest_model_with_features.pkl")


# === Model Handling ===
def download_model(model_path: Path = MODEL_PATH):
    """Download the model from Google Drive if it doesn't exist."""
    if not model_path.exists():
        try:
            model_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"Downloading model to: {model_path}")
            gdown.download(MODEL_URL, str(model_path), quiet=False)
            print("Model downloaded successfully.")
        except Exception as e:
            raise RuntimeError(f"Error downloading model: {e}")


def load_model(model_path: Path = MODEL_PATH):
    """Load the trained model from disk."""
    download_model(model_path)
    model, feature_names = joblib.load(model_path)
    return model, feature_names


# === CSV Loader ===
def load_csv(file_path: Path, **kwargs) -> pd.DataFrame:
    """Load a CSV file from the given path."""
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    try:
        return pd.read_csv(file_path, **kwargs)
    except Exception as e:
        raise IOError(f"Error loading CSV file: {file_path}\n{e}")
