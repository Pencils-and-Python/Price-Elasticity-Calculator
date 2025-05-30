# 🧾 Project Directory Structure — `elasticity_risk_exposure`

This document presents the complete directory layout of the Elasticity Risk Exposure project.  
It is designed for modularity, maintainability, and production-level readability — now enhanced for Streamlit integration.

---

## 🗂️ Folder Structure (Streamlit-Enhanced, Fully Preserved)

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
