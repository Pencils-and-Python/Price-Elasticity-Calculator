# app/main.py

"""
1. Title: "Elasticity Risk Exposure Dashboard"

2. Model summary:
    - R²
    - RMSE
    - MSE

3. Image of actual vs predicted plot

4. Checkbox: "Show feature importances"
    - bar chart appears if checked

5. Optional filter: select Store or Month
    - updates displayed predictions

6. Download predictions button (optional)
"""

# app/main.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path

# === Paths ===
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PLOTS_DIR = BASE_DIR / "plots"
MODEL_PATH = DATA_DIR / "trained_model" / "random_forest_model_with_features.pkl"
X_TEST_PATH = DATA_DIR / "test" / "X_test.csv"
Y_TEST_PATH = DATA_DIR / "test" / "y_test.csv"
PREDICTION_PLOT_PATH = PLOTS_DIR / "actual_vs_predicted.png"

# === Page Config ===
st.set_page_config(
    page_title="Elasticity Risk Exposure Dashboard",
    layout="wide"
)

# === Header ===
st.title("📈 Elasticity Risk Exposure Dashboard")
st.write("""
Welcome to the Elasticity Risk Exposure Dashboard!  
This tool explores how price changes impact revenue and demand using real-world sales data and a trained machine learning model.  
Filter, visualize, and interact with your data to better understand elasticity in action.
""")

# === Load Model & Data ===
try:
    model, feature_names = joblib.load(MODEL_PATH)
    X_test = pd.read_csv(X_TEST_PATH)
    y_test = pd.read_csv(Y_TEST_PATH)
except Exception as e:
    st.error(f"❌ Failed to load model or data: {e}")
    st.stop()

# === Predictions & Metrics ===
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# === Sidebar Filters (Scaffold Only) ===
st.sidebar.header("🔧 Filter Options")
store_filter = st.sidebar.selectbox("Select Store (optional)", options=["All"] + sorted(
    X_test["Store"].unique()) if "Store" in X_test.columns else ["N/A"])
month_filter = st.sidebar.selectbox("Select Month (optional)", options=["All"] + sorted(
    X_test["Month"].unique()) if "Month" in X_test.columns else ["N/A"])

# === Tabs Layout ===
tab1, tab2, tab3 = st.tabs(["📊 Performance", "📈 Feature Insights", "📥 Download"])

# === Tab 1: Model Performance ===
with tab1:
    st.subheader("📊 Model Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("R²", f"{r2:.4f}")
    col2.metric("RMSE", f"${rmse:,.2f}")
    col3.metric("MSE", f"${mse:,.2f}")

    st.subheader("📉 Actual vs Predicted Sales")
    if PREDICTION_PLOT_PATH.exists():
        st.image(str(PREDICTION_PLOT_PATH), caption="Actual vs Predicted Sales ($)", use_column_width=True)
    else:
        st.warning("Prediction plot not found.")

# === Tab 2: Feature Insights ===
with tab2:
    if st.checkbox("Show Feature Importances"):
        st.subheader("🔍 Feature Importances")
        try:
            feature_importances = pd.Series(model.feature_importances_, index=X_test.columns)
            fig, ax = plt.subplots()
            feature_importances.sort_values().plot(kind='barh', ax=ax)
            ax.set_xlabel("Importance")
            ax.set_title("Feature Importances")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"❌ Could not plot feature importances: {e}")

    st.subheader("📐 Elasticity Curve (Coming Soon)")
    st.info("Elasticity curve visualization will appear here once implemented.")

# === Tab 3: Download Predictions ===
with tab3:
    st.subheader("📥 Download Predicted Results")

    # Join predictions to X_test for convenience (placeholder logic)
    results_df = X_test.copy()
    results_df["Actual"] = y_test
    results_df["Predicted"] = y_pred

    csv_data = results_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Predictions as CSV",
        data=csv_data,
        file_name="predictions.csv",
        mime="text/csv"
    )

# === Footer ===
st.caption("Part of the Elasticity Risk Exposure Project. Built with ❤️ and Streamlit.")
