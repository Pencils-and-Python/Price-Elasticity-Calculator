"""db/create_db.py"""

import pandas as pd
import duckdb
from pathlib import Path
import os
from db.connection import DB_PATH

def create_duckdb_from_csv():
    """
    Creates a DuckDB database from processed CSV data.

    This function:
    1. Reads the processed_data.csv file
    2. Creates necessary directories if they don't exist
    3. Establishes a connection to a DuckDB database
    4. Creates a table in the database from the DataFrame
    5. Validates the data was imported correctly
    """
    # Define paths
    csv_path = Path("data/processed/processed_data.csv")

    # Create directory if it doesn't exist
    os.makedirs(DB_PATH.parent, exist_ok=True)

    # Read the CSV data
    print(f"Reading data from {csv_path}...")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows with {len(df.columns)} columns")

    # Connect to DuckDB
    print(f"Creating DuckDB database at {DB_PATH}...")
    conn = duckdb.connect(str(DB_PATH))

    # Create table from DataFrame
    print("Creating 'rossmann_sales' table...")
    conn.execute("CREATE TABLE IF NOT EXISTS rossmann_sales AS SELECT * FROM df")

    # Verify data was imported correctly
    row_count = conn.execute("SELECT COUNT(*) FROM rossmann_sales").fetchone()[0]
    print(f"Successfully imported {row_count} rows into DuckDB")

    # Display sample
    print("\nSample data from DuckDB:")
    result = conn.execute("SELECT * FROM rossmann_sales LIMIT 5").fetchdf()
    print(result)

    # Close connection
    conn.close()
    print("Database creation complete!")


if __name__ == "__main__":
    create_duckdb_from_csv()