# Final Project Structure: `elasticity_risk_exposure`

├── app/                            # Streamlit dashboard app
│   ├── __init__.py
│   ├── main.py                     # Streamlit UI entrypoint
│   ├── components/
│   │   ├── __init__.py
│   │   └── feature_importance_plot.py
│   │   └── revenue_elasticity_curve.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── db/                             # DuckDB setup and helpers
│   ├── __init__.py
│   ├── connection.py
│   ├── create_db.py
│   ├── db_cli.py
│   ├── queries.py
│   ├── register.py
│   └── elasticity.duckdb           # (ignored via .gitignore)
├── data/                           # Versioned data sets
│   ├── raw/
│   ├── processed/
│   └── trained_model/
│       └── random_forest_model_with_features.pkl
├── docs/                           # Project planning & blog drafts
│   ├── roadmap.md
│   ├── blog_draft.md
│   ├── blog_outline.md
│   ├── problem_statement.md
│   ├── summary.md
│   ├── workflow.md
│   ├── structure.md
│   └── roadmap_documentation/
│       ├── elasticity_feature_engineering_plan.ipynb
│       └── roadmap_diary.ipynb
├── notebooks/                      # Modeling and analysis notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_visualization.ipynb
│   ├── 05_dashboard_design.ipynb
│   ├── 99_scratchpad.ipynb
│   ├── duckdb_practice.ipynb
│   └── project_dashboard.html
├── plots/                          # Rendered HTML and static charts
│   └── actual_vs_predicted.png
├── scripts/                        # Python helpers for data & model
│   ├── __init__.py
│   ├── load_data.py
│   ├── initialize_duckdb.py
│   ├── model_trainer.py
│   └── predict.py
├── static/                         # Images for blog or Streamlit app
│   ├── sales_histogram.png
│   └── revenue_curve.png
├── utils/                          # Utility modules
│   ├── __init__.py
│   ├── metrics.py
│   ├── plot_utils.py
│   └── filters.py
│   └── reusable_data_loader.py
├── .gitignore
├── environment.yml
├── requirements.txt
└── README.md