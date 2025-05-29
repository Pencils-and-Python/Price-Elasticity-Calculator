"""scripts/load_data.py"""


from pathlib import Path
import pandas as pd
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data/raw"

def load_raw_data():
    """
    Load raw data files from various potential locations.

    Returns:
        tuple: (train_df, store_df)
    """
    potential_paths = [
        Path("data/raw"),
        Path.cwd() / "data" / "raw",
        Path(__file__).parent.parent.parent / "data" / "raw"
    ]

    for path in potential_paths:
        if (path / "train.csv").exists():
            train_df = pd.read_csv(path / "train.csv", parse_dates=["Date"])
            store_df = pd.read_csv(path / "store.csv")
            print(f"✅ Data loaded from: {path}")
            return train_df, store_df

    raise FileNotFoundError(
        "❌ Could not find train.csv and store.csv. "
        "Please place these files in a 'data/raw' directory."
    )


