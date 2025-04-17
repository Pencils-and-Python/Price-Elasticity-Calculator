"""src/database/connection.py"""

import duckdb
from pathlib import Path

DB_PATH = Path("data/processed/elasticity.duckdb")

def connect_duckdb(persist: bool = True):
    return duckdb.connect(DB_PATH if persist else ":memory:")
