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

import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"


import streamlit as st

# === Page Config ===
st.set_page_config(
    page_title="Elasticity Risk Exposure Dashboard",
    layout="wide"
)

from pathlib import Path
import sys

# === Fix: Add root project directory to sys.path BEFORE anything else ===
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from utils.loaders import load_model, load_csv

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from app.components.feature_importance import plot_feature_importance
# Add near the top
from streamlit import cache_resource



# === Paths ===
DATA_DIR = BASE_DIR / "data"
PLOTS_DIR = BASE_DIR / "plots"
MODEL_PATH = DATA_DIR / "trained_model" / "rf_light_model.pkl"
X_TEST_PATH = DATA_DIR / "test" / "X_test.csv"
Y_TEST_PATH = DATA_DIR / "test" / "y_test.csv"
PREDICTION_PLOT_PATH = PLOTS_DIR / "actual_vs_predicted.png"



# === Header ===
st.title("📈 Elasticity Risk Exposure Dashboard")
st.write("""
Welcome to the Elasticity Risk Exposure Dashboard!  
This tool explores how price changes impact revenue and demand using real-world sales data and a trained machine learning model.  
Filter, visualize, and interact with your data to better understand elasticity in action.
""")

# === Load Model & Data ===
# === Load Model & Data ===
@cache_resource(show_spinner="⏳ Downloading and loading model...")
def safe_load_model():
    return load_model(MODEL_PATH)

@cache_resource(show_spinner="📦 Loading test data...")
def safe_load_test_data():
    X = load_csv(X_TEST_PATH)
    y = load_csv(Y_TEST_PATH)
    return X, y

try:
    model, feature_names = safe_load_model()
    X_test, y_test = safe_load_test_data()
except Exception as e:
    st.error("❌ Failed to load model or test data.")
    st.code(str(e), language="python")
    import traceback
    st.code(traceback.format_exc(), language="python")
    st.stop()



# === Predictions & Metrics ===
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# === Sidebar Filters (Scaffold Only) ===
st.sidebar.header("🔧 Filter Options")
if "Store" in X_test.columns:
    store_options = ["All"] + sorted(X_test["Store"].dropna().unique())
    store_filter = st.sidebar.selectbox("Select Store (optional)", options=store_options)
else:
    store_filter = "All"

if "Month" in X_test.columns:
    month_options = ["All"] + sorted(X_test["Month"].dropna().unique())
    month_filter = st.sidebar.selectbox("Select Month (optional)", options=month_options)
else:
    month_filter = "All"


# === Tabs Layout ===
tab1, tab2, tab3 = st.tabs(["📊 Performance", "📈 Feature Insights", "📥 Download"])

# === Tab 1: Model Performance ===
with tab1:
    from app.components.filtered_results import filter_data, display_filtered_metrics

    # Filter based on sidebar selection
    filtered_df = filter_data(X_test, y_test, y_pred, store_filter, month_filter)

    # Display metrics and plot
    display_filtered_metrics(filtered_df)


# === Tab 2: Feature Insights ===
with tab2:
    if st.checkbox("Show Feature Importances"):
        st.caption("Feature importances reflect the global trained model and do not change with filters.")
        st.subheader("🔍 Feature Importances")
        try:
            # Prepare importance DataFrame
            importances = pd.DataFrame({
                "feature": X_test.columns,
                "importance": model.feature_importances_
            })

            plot_feature_importance(importances)
        except Exception as e:
            st.error(f"❌ Could not plot feature importances: {e}")

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
