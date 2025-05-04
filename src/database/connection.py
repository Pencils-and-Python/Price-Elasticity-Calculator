"""src/database/connection.py"""

import duckdb
from pathlib import Path

# Define the database path
DB_PATH = Path("data/processed/rossmann.duckdb")

def connect_duckdb(persist: bool = True):
    """
    Establishes a connection to the DuckDB database.

    Args:
        persist: If True, connects to the file-based database.
                If False, creates an in-memory database.

    Returns:
        A DuckDB connection object
    """
    return duckdb.connect(str(DB_PATH) if persist else ":memory:")
