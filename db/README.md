File location: db_helpers/README.md

# Convert Data to DuckDB Instructions

1. Convert your CSV data to DuckDB using `python -m src.database.create_db`
2. Query the database in your notebooks or scripts using the connection utility
3. Explore the database with the CLI tool using commands like:
    - `python -m src.database.db_cli --list-tables`
    - `python -m src.database.db_cli --sample rossmann_sales --rows 10`
    - `python -m src.database.db_cli --info rossmann_sales`

This setup gives you a robust way to work with your data in DuckDB while maintaining compatibility with your existing code structure.