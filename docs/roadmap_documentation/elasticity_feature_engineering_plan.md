# 🛠️ Elasticity Project: Feature Engineering Plan

---

# 🎯 Goal
Prepare the dataset for elasticity modeling by engineering clean, relevant features.

---

# 🚀 Planned Steps:

| Step | Description | Goal |
|-----|--------------|-----|
| 1. Clean Data | Handle zero sales days | Prevent skewing elasticity |
| 2. Create Log Sales | Add a `log_sales` feature | Normalize sales data for modeling |
| 3. Add Promo Flags | Use existing promo data or create dummy variables | Understand promotion impact on elasticity |
| 4. Extract Date Features | Month, year, weekday, holiday flags | Capture seasonality effects |
| 5. Prepare for Modeling | Select features and target variable | Ready for regression

---

# ✍️ Step 1: Clean Zero Sales Days

- **Plan**: Drop rows where sales = 0
- **Why**: Zero sales days distort elasticity models
- **Code**:
  ```python
  df2 = df2[df2['Sales'] > 0]
  ```

---

# ✍️ Step 2: Create Log Sales

- **Plan**: Create a `Log_Sales` column
- **Why**: Elasticity is typically modeled in log-log space
- **Code**:
  ```python
  import numpy as np
  df2['Log_Sales'] = np.log(df2['Sales'])
  ```

---

# ✍️ Step 3: Create Promo Flags

- **Plan**: Use or create binary promo indicators
- **Why**: Promotions significantly impact demand
- **Example Code**:
  ```python
  df2['StateHoliday_Flag'] = (df2['StateHoliday'] != '0').astype(int)
  ```

---

# ✍️ Step 4: Extract Date Features

- **Plan**: Derive Month, Weekday, and Year from the date index
- **Why**: Capture seasonality and cyclic behavior
- **Code**:
  ```python
  df2['Month'] = df2.index.month
  df2['Weekday'] = df2.index.weekday
  df2['Year'] = df2.index.year
  ```

---

# ✍️ Step 5: Feature Selection

- **Plan**: Choose inputs and target for modeling
- **Target**: `Log_Sales`
- **Features**: Price, Promo flags, Month, Weekday, etc.

---

# 🏁 Next Step:
Begin implementing each feature engineering step to prepare for elasticity regression modeling.
