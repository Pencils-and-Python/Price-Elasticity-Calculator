"""app/components/feature_importance.py"""

import pandas as pd
import plotly.express as px
import streamlit as st

def plot_feature_importance(df: pd.DataFrame, top_n: int = 20):
    """
    Plot feature importances using Plotly.

    Parameters:
    - df: DataFrame with 'feature' and 'importance' columns
    - top_n: Number of top features to display
    """
    if df.empty:
        st.warning("No feature importance data available.")
        return

    df_sorted = df.sort_values("importance", ascending=False).head(top_n)

    fig = px.bar(
        df_sorted,
        x="importance",
        y="feature",
        orientation="h",
        title=f"Top {top_n} Most Important Features",
        labels={"importance": "Importance Score", "feature": "Feature"},
        height=500
    )

    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)
