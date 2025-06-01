# 📉 Elasticity Explorer

**Streamlit App to Analyze Price Elasticity of Demand & Revenue Impact**  
*Built with DuckDB, pandas, scikit-learn, and economic intuition*

SEO tags: #Elasticity #PriceModeling #RevenueOptimization #DemandForecasting #DataScience #Streamlit #DuckDB #QuantEcon #PricingStrategy #BusinessAnalytics
 
---

## 🔍 Overview

**Elasticity Explorer** is a web-based application that visualizes and models how changes in product pricing affect total revenue across various customer and store segments. 

Designed for economists, data scientists, and business analysts, the tool helps identify pricing strategies that **maximize revenue** without alienating price-sensitive consumers.

This project combines:
- Real-world **sales data**
- Custom **machine learning pipelines**
- Economic theory of **price elasticity of demand**
- Interactive **Streamlit interface**
- Fast, embedded **DuckDB SQL backend**

---

## 🚀 Features

- 📊 Visualize elasticity curves by store, product, or time
- 🔎 Explore impact of price changes on revenue
- 📉 Identify over- or under-priced products using elasticity estimates
- 🧪 Fit regression or tree-based models to predict elasticity dynamically
- ⚙️ Query and filter datasets on the fly with DuckDB

---

## 📂 Project Structure

```bash
elasticity_risk_exposure/
│
├── app/                              ← Streamlit application logic
│   ├── __init__.py
│   ├── main.py                       ← Streamlit entrypoint
│   │
│   ├── components/                   ← Custom Streamlit chart modules
│   │   ├── __init__.py
│   │   ├── feature_importance_plot.py
│   │   └── revenue_elasticity_curve.py
│   │
│   ├── config/                       ← Environment and settings loader
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── layout/                       ← (Optional) UI layout helpers
│   │   ├── __init__.py
│   │   ├── sidebar.py
│   │   ├── header.py
│   │   └── footer.py
│   │
│   └── pages/                        ← (Optional) multipage support
│       ├── __init__.py
│       └── analysis_dashboard.py
│
├── db/                               ← DuckDB and helper scripts
│   ├── helpers/                     
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── create_db.py
│   │   ├── db_cli.py
│   │   ├── queries.py
│   │   └── register.py
│   │
│   ├── raw/
│   │   └── raw.duckdb
│   │
│   └── processed/
│       └── rossmann.duckdb
│
├── data/                             ← All project datasets and models
│   ├── raw/
│   │   ├── store.csv
│   │   ├── test.csv
│   │   └── train.csv
│   │
│   ├── processed/
│   │   ├── processed_data.csv
│   │   └── train_df_exploration_clean.csv
│   │
│   ├── test/
│   │   ├── X_test.csv
│   │   └── y_test.csv
│   │
│   ├── trained_model/
│   │   └── random_forest_model_with_features.pkl
│   │
│   └── external/
│       └── rossmann-store-sales/
│           ├── sample_submission.csv
│           └── zip_files/
│               └── rossmann-store-sales.zip
│
├── docs/                             ← Internal documentation and planning
│   ├── roadmap.md
│   ├── blog/
│   │   ├── blog_draft.md
│   │   └── blog_outline.md
│   ├── problem_statement.md
│   ├── summary.md
│   ├── workflow.md
│   ├── structure.md                  ← You are here
│   └── roadmap_documentation/
│       ├── elasticity_feature_engineering_plan.ipynb
│       └── roadmap_diary.ipynb
│
├── notebooks/                        ← Data science notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_visualization.ipynb
│   ├── 05_dashboard_design.ipynb
│   ├── 99_scratchpad.ipynb
│   ├── duckdb_practice.ipynb
│   └── project_dashboard.html
│
├── plots/                            ← Final charts and visuals
│   └── actual_vs_predicted.png
│
├── scripts/                          ← Supporting data + ML logic
│   ├── __init__.py
│   ├── load_data.py
│   ├── initialize_duckdb.py
│   ├── model_trainer.py
│   └── predict.py
│
├── static/                           ← Streamlit or blog image assets
│   ├── sales_histogram.png
│   └── revenue_curve.png
│
├── utils/                            ← Reusable logic and helper functions
│   ├── __init__.py
│   ├── metrics.py
│   ├── plot_utils.py
│   ├── filters.py
│   └── reusable_data_loader.py
│
├── .env                              ← Environment configuration
├── .gitignore                        ← Git exclusions
├── environment.yml                   ← Conda environment
├── requirements.txt                  ← Pip alternative
└── README.md                         ← Project overview
```

## Live App 
Try the interactive app on Streamlit Cloud or run it locally:

```bash 
streamlit run app/main.py
```

## 🔧 Tech Stack
- Python 3.12.7
- Streamlit
- DuckDB
- pandas
- scikit-learn
- matplotlib / plotly
- Pytest for testing

## 📄 License
MIT License — open for research, education, and portfolio use.

## ✍️ Author

Brice Nelson — Senior Python Developer | Quantitative Analytics | Infrastructure & Fintech Systems  
📬 [Connect on LinkedIn](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/) | 📝 [Medium Blog: Pencils & Python](https://medium.com@quantshift)
