"""src/utils/reusable_data_loader.py"""

# 📦 reusable_data_loader.py

import pandas as pd

def load_and_clean_csv(filepath, date_cols=None, index_col=0, verbose=True):
    """
    Load a CSV file robustly and cleanly.

    Args:
        filepath (str): Path to the CSV file.
        date_cols (list, optional): List of columns to parse as dates.
        index_col (int or str, optional): Column to set as index.
        verbose (bool): Whether to print success message.

    Returns:
        pd.DataFrame: Cleaned DataFrame with dates parsed and bad rows skipped.
    """

    try:
        # Load with professional settings
        df = pd.read_csv(
            filepath,
            index_col=index_col,
            parse_dates=date_cols,
            on_bad_lines='skip',
            low_memory=False
        )

        # Coerce any remaining date parsing issues
        if date_cols:
            for col in date_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')

        if verbose:
            print(f"✅ Successfully loaded and cleaned: {filepath}")
            print(f"\u2022 Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

        return df

    except Exception as e:
        print(f"❌ Error loading {filepath}: {e}")
        return None

# ---
# Example usage (inside your project, in your notebooks):
# from reusable_data_loader import load_and_clean_csv
# df = load_and_clean_csv('../data/processed/train_df_exploration_clean.csv', date_cols=['Date'])
