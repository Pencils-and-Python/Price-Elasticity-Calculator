"""utils/loaders.py"""

import os
import urllib.request
import streamlit as st
import gdown
import pandas as pd
import joblib
from pathlib import Path

# === Constants ===
MODEL_URL = "https://drive.google.com/file/d/17_UhY2TCPGFYqoJWYs60iLHv9fIFlXaz/view?usp=sharing"
MODEL_PATH = Path("data/trained_model/rf_light_model.pkl")


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


@st.cache_resource(show_spinner="Downloading and loading model...")
def load_model(model_path: Path = MODEL_PATH):
    """Download and load the model, with caching."""
    download_model(model_path)
    model, feature_names = joblib.load(model_path)
    return model, feature_names

# UI
st.title("Price Elasticity Risk Exposure")

if st.button("Run Prediction"):
    try:
        model, features = cached_load_model()
        # Prediction logic goes here, like:
        # X = pd.DataFrame(...), etc.
        # y_pred = model.predict(X)
        st.success("Model loaded and ready for prediction.")
    except Exception as e:
        st.error(f"💥 Failed to load model: {e}")
        st.stop()


# === CSV Loader ===
def load_csv(file_path: Path, **kwargs) -> pd.DataFrame:
    """Load a CSV file from the given path."""
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    try:
        return pd.read_csv(file_path, **kwargs)
    except Exception as e:
        raise IOError(f"Error loading CSV file: {file_path}\n{e}")
