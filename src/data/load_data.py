"""src/data/load_data.py"""

import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

def load_raw_data():
    train_df = pd.read_csv(RAW_DATA_DIR / "train.csv", parse_dates=["Date"])
    store_df = pd.read_csv(RAW_DATA_DIR / "store.csv")
    return train_df, store_df
