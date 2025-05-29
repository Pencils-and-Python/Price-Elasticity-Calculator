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

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_squared_error, r2_score

# 1. Set page title
st.set_page_config(page_title='Store Sales Prediction Dashboard')

# 🏷️ Title & description
st.title('Store Sales Prediction Dashboard')
st.write("""
This dashboard displays model evaluation metrics and prediction results 
from the Random Forest sales forecasting model.
""")

# 2. ✅ Load trained model
model, feature_names = joblib.load('../data/trained/random_forest_model_with_features.pkl')


# ✅ Load test data
X_test = pd.read_csv('../data/trained/X_test.csv')
y_test = pd.read_csv('../data/trained/y_test.csv')

# ✅ Make predictions
y_pred = model.predict(X_test)

# ✅ Calculate metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# ✅ Display metrics
st.subheader('Model Performance Metrics')
st.metric("R²", f"{r2:.4f}")
st.metric("RMSE", f"${rmse:,.2f}")
st.metric("MSE", f"${mse:,.2f}")

# 3. ✅ Display actual vs predicted plot
st.subheader('Actual vs Predicted Sales')
st.image('../plots/actual_vs_predicted.png', caption='Actual vs Predicted Sales ($)', use_column_width=True)

# 4. ✅ Optional: feature importances toggle
if st.checkbox('Show Feature Importances'):
    feature_importances = pd.Series(model.feature_importances_, index=X_test.columns)
    st.bar_chart(feature_importances.sort_values())

# ✅ Footer
st.caption("Part of the Elasticity Risk Exposure Project. Built with Streamlit.")


