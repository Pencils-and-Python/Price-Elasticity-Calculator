"""scripts/initialize_duckdb.py"""

from scripts.load_data import load_raw_data
from db import connect_duckdb
from db import register_dataframes

def initialize_duckdb(persist: bool = True):
    train_df, store_df = load_raw_data()
    con = connect_duckdb()
    register_dataframes(train_df, store_df, con)

    print("✅ DataFrames registered in DuckDB.")
    print("Sample query result:")
    print(con.execute("SELECT * FROM train_df LIMIT 5").fetchdf())

    return con

if __name__ == "__main__":
    con = initialize_duckdb()
    count = con.execute("SELECT COUNT(*) FROM train_df").fetchone()[0]
    print(f"🔢 Train row count: {count}")
