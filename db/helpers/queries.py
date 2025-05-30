"""db/queries.py"""

from .duck_connection import get_connection
import pandas as pd

def get_sales_summary_by_store():
    """
    Get total sales and average price by store.
    Returns:
        pd.DataFrame: Aggregated store sales info
    """
    query = """
        SELECT 
            store_id,
            ROUND(AVG(price), 2) AS avg_price,
            SUM(sales) AS total_sales
        FROM sales_data
        GROUP BY store_id
        ORDER BY total_sales DESC
    """
    con = get_connection()
    return con.execute(query).fetchdf()

def get_price_revenue_curve(store_id=None):
    """
    Generate price vs. revenue aggregation.

    Args:
        store_id (str or None): Optional store filter
    Returns:
        pd.DataFrame: Price vs Revenue table
    """
    filter_clause = f"WHERE store_id = '{store_id}'" if store_id else ""
    query = f"""
        SELECT 
            price,
            SUM(sales) AS revenue
        FROM sales_data
        {filter_clause}
        GROUP BY price
        ORDER BY price
    """
    con = get_connection()
    return con.execute(query).fetchdf()

def get_feature_overview():
    """
    View the current schema and preview sample data.
    Returns:
        pd.DataFrame: Sample rows from the table
    """
    con = get_connection()
    return con.execute("SELECT * FROM sales_data LIMIT 10").fetchdf()
