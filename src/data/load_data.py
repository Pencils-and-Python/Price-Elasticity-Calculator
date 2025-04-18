"""src/data/load_data.py"""


import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data/raw"

from pathlib import Path
import pandas as pd
import os


def load_raw_data():
    """
    Load raw data files from various potential locations
    """
    # List of possible locations to check
    potential_paths = [
        Path("data/raw"),  # Project root data/raw
        Path.cwd() / "data" / "raw",  # Current working directory
        Path(__file__).parent.parent.parent / "data" / "raw"  # Repository root
    ]

    # Find the first path that contains the train.csv file
    for path in potential_paths:
        if (path / "train.csv").exists():
            train_df = pd.read_csv(path / "train.csv", parse_dates=["Date"])
            store_df = pd.read_csv(path / "store.csv")
            print(f"Data loaded from: {path}")
            return train_df, store_df

    # If we can't find the files, raise a more helpful error
    raise FileNotFoundError(
        "Could not find train.csv and store.csv. "
        "Please place these files in a 'data/raw' directory "
        "or specify the correct path to the data files."
    )

