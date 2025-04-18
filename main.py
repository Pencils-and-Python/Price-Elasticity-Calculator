"""main.py"""

from src.data.load_data import load_raw_data
from src.database.connection import connect_duckdb
from src.data.register import register_dataframes

def main(persist: bool = True):
    train_df, store_df = load_raw_data()
    con = connect_duckdb(persist)
    register_dataframes(train_df, store_df, con)

    print("✅ DataFrames registered in DuckDB.")
    print("Sample query result:")
    print(con.execute("SELECT * FROM train_df LIMIT 5").fetchdf())

    return con

if __name__ == "__main__":
    con = main()
    result = con.execute("SELECT COUNT(*) FROM train_df").fetchall()
    print(f"Train row count: {result[0][0]}")
