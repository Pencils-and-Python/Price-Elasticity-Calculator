# src/data/load_and_register.py

import pandas as pd
import duckdb
from pathlib import Path

# Paths
RAW_DATA_DIR = Path("data/raw")
DB_PATH = Path("data/processed/elasticity.duckdb")

def load_raw_data():
    train_df = pd.read_csv(RAW_DATA_DIR / "train.csv", parse_dates=["Date"])
    store_df = pd.read_csv(RAW_DATA_DIR / "store.csv")
    return train_df, store_df

def register_dataframes(train_df, store_df, con):
    con.register("train_df", train_df)
    con.register("store_df", store_df)

def connect_duckdb(persist: bool = True):
    if persist:
        return duckdb.connect(DB_PATH)
    else:
        return duckdb.connect(database=":memory:")

def main(persist: bool = True):
    train_df, store_df = load_raw_data()
    con = connect_duckdb(persist=persist)
    register_dataframes(train_df, store_df, con)

    print("DataFrames registered successfully! You can now run SQL queries like:")
    print("SELECT * FROM train_df LIMIT 5;")

    return con  # so you can run con.execute(...) in a notebook or app

if __name__ == "__main__":
    con = main()
    result = con.execute("SELECT COUNT(*) FROM train_df").fetchall()
    print(f"Train row count: {result[0][0]}")
