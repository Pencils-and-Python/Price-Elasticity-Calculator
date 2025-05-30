"""app/config/settings.py"""

from pathlib import Path

# === BASE PATH CONFIG ===
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "db" / "elasticity.duckdb"

# === UI SETTINGS ===
APP_TITLE = "📉 Elasticity Explorer"
APP_DESCRIPTION = "Interactive tool to analyze price elasticity of demand and its effect on revenue"
SIDEBAR_TITLE = "Elasticity Settings"

# === DATA SETTINGS ===
RAW_DATA_PATH = DATA_DIR / "raw" / "sales_data.csv"
CLEANED_DATA_PATH = DATA_DIR / "processed" / "clean_sales_data.csv"
CACHED_CITIES_PATH = DATA_DIR / "cache" / "popular_cities.csv"

# === MODEL SETTINGS ===
MODEL_PATH = BASE_DIR / "models" / "random_forest_elasticity.pkl"
FEATURES_USED = ["Price", "DayOfWeek", "Store", "Promotion", "Holiday"]
TARGET = "Revenue"

# === STREAMLIT SETTINGS ===
PLOT_WIDTH = 800
PLOT_HEIGHT = 500
SHOW_LOGS = False

# === DEV MODE ===
DEBUG = True
USE_CACHE = True

# === DATABASE SETTINGS ===
DUCKDB_TABLE = "elasticity_data"

# === UTIL ===
def get_project_info():
    return {
        "app_title": APP_TITLE,
        "description": APP_DESCRIPTION,
        "base_dir": str(BASE_DIR),
    }
