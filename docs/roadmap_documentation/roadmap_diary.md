# Roadmap Diary Documentation

<br>

### Date:  April 26, 2025

## 📝 Elasticity Project Progress
### ✅ What has been completed:

#### Project Setup: Clean project import structure (load_raw_data() from src/data/), fresh imports.
- Initial Data Exploration:
- Loaded and previewed train.csv and store.csv.
- Checked data types and null values.
- Investigated StateHoliday column for mixed types and inconsistencies.
- Checked Date range in the dataset.

#### Sales Distribution:
- Plotted histogram of sales to look for distribution patterns.
- Noticed the spike near zero sales values.
- Zero-Sales Investigation:
- Counted the number of sales = 0 and sales < 100 entries.
- Replotted a cleaned histogram excluding zero sales to better understand "real" sales distribution.

#### ✅ Good commentary/annotations:
- Added markdown cells explaining why each analysis step was important.
- Wrote "sanity checks" notes about cleaning the StateHoliday column.
- Wrote thoughtful exploration on potential issues in sales data (zero sales spike).

## 🛠️ Pipeline

| Stage | Status |
|------|--------|
| Load + Explore Data | ✅ Done |
| Identify Dirty Data | ✅ Done (StateHoliday + Zero Sales) |
| Initial Visualization | ✅ Done (Sales histogram) |
| Feature Engineering | ⏳ Coming soon |
| Model Prep | 🚧 Coming later |
| Elasticity Modeling | 🚧 Coming later |
| Final Streamlit App | 🚧 Future goal |

## 🎯 Next Logical Steps for You

### Feature Engineering
- (Add log sales? Normalize date fields? Mark store closures?)
- Target Filtering
(Decide: Should we drop zero-sales days from elasticity modeling? Yes, probably.)
- Create Elasticity Features
- E.g., promotions, competition distance, etc. as inputs.
- Build the Model
- Regress log(Sales) or Sales vs price changes, promotions, etc.
- Deploy a Minimal Streamlit Dashboard
- Visualize elasticity curves per store or per product category.

<br>

### Date: May 29, 2025

## 🔜 Suggested Next Steps
Elasticity Curve:
- We can plot a simple revenue curve or price elasticity chart using stored or derived data.

DuckDB Integration:
- load dynamic slices from DuckDB (rossmann.duckdb), we can wire that in next.
- It's great for filter-by-query dashboards.

Model Comparison Tab:
- Compare models side-by-side (RandomForest vs. LinearReg or XGBoost).

Visual Polish:
- Add a sidebar logo, color theme, and styled headers.