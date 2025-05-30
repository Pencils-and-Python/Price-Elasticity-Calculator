"""app/components/filtered_results.py
Purpose:
--------
Display R², RMSE, and MSE for filtered prediction results.

Definitions:
------------
- R² (Coefficient of Determination): Measures how well predictions approximate actual values.
  Ranges from 0 to 1 (or negative if the model performs worse than a horizontal line).
- RMSE (Root Mean Squared Error): Square root of the average squared differences between predicted and actual values.
  Interpretable in the same units as the target variable.
- MSE (Mean Squared Error): Average squared difference between predicted and actual values. Sensitive to outliers.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def filter_data(X, y, y_pred, store=None, month=None):
    """Apply store/month filters to the dataframes."""
    df = X.copy()
    df["Actual"] = y
    df["Predicted"] = y_pred

    # Only filter if column exists and user selected something
    if "Store" in df.columns and store and store != "All":
        df = df[df["Store"] == store]

    if "Month" in df.columns and month and month != "All":
        df = df[df["Month"] == month]

    return df


def display_filtered_metrics(df):
    """Display R², MSE, RMSE based on filtered results."""
    if df.empty:
        st.warning("No data available for this selection.")
        return

    mse = mean_squared_error(df["Actual"], df["Predicted"])
    rmse = mse ** 0.5
    r2 = r2_score(df["Actual"], df["Predicted"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Filtered R²", f"{r2:.4f}")
    col2.metric("Filtered RMSE", f"${rmse:,.2f}")
    col3.metric("Filtered MSE", f"${mse:,.2f}")

    st.subheader("📉 Actual vs Predicted (Filtered)")
    fig, ax = plt.subplots()
    ax.scatter(df["Actual"], df["Predicted"], alpha=0.6)
    ax.plot([df["Actual"].min(), df["Actual"].max()],
            [df["Actual"].min(), df["Actual"].max()], 'r--')
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Actual vs Predicted Sales (Filtered)")
    st.pyplot(fig)
