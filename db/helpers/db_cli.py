"""db/db_cli.py"""

import argparse
import duckdb
import sys
import os

# Add the parent directory to the path to make src.database accessible
# This gets the directory three levels up from the current file
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Now we can import from our project modules
from db.helpers.connection import connect_duckdb, DB_PATH


def list_tables():
    """Lists all tables in the database"""
    conn = connect_duckdb()
    tables = conn.execute("SHOW TABLES").fetchall()
    conn.close()

    if not tables:
        print("No tables found in the database.")
    else:
        print("Tables in the database:")
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table[0]}")


def sample_table(table_name: str, limit: int = 5):
    """Shows sample rows from a specific table"""
    conn = connect_duckdb()
    try:
        result = conn.execute(f"SELECT * FROM {table_name} LIMIT {limit}").fetchdf()
        print(f"\nSample data from '{table_name}':")
        print(result)
    except duckdb.Error as e:
        print(f"Error accessing table: {e}")
    conn.close()


def table_info(table_name: str):
    """Shows column information for a table"""
    conn = connect_duckdb()
    try:
        columns = conn.execute(f"PRAGMA table_info({table_name})").fetchdf()
        print(f"\nColumn information for '{table_name}':")
        print(columns)
    except duckdb.Error as e:
        print(f"Error getting table info: {e}")
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="DuckDB Database CLI")
    parser.add_argument("--list-tables", action="store_true", help="List all tables")
    parser.add_argument("--sample", type=str, help="Show sample rows from a table")
    parser.add_argument("--info", type=str, help="Show table column information")
    parser.add_argument("--rows", type=int, default=5, help="Number of sample rows to display")

    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}. Please create it first.")
        return

    if args.list_tables:
        list_tables()

    if args.sample:
        sample_table(args.sample, args.rows)

    if args.info:
        table_info(args.info)

    if not (args.list_tables or args.sample or args.info):
        parser.print_help()


if __name__ == "__main__":
    main()