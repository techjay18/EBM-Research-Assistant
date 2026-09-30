import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv(
    r"C:\Users\jayde\OneDrive\Desktop\EBM assistant\dataset\CRx_DB_Q1_2026.csv",
    sep=';'
)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

df.to_sql(
    "papers",
    engine,  # type: ignore[arg-type]
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")