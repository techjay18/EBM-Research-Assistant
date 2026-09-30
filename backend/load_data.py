import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
     r"C:\Users\jayde\OneDrive\Desktop\EBM assistant\dataset\CRx_DB_Q1_2026.csv",
    sep=';'
)

engine = create_engine(
    "postgresql://postgres:jay1873@localhost/ebm_db")

df.to_sql(
    "papers",
    engine,  # type: ignore[arg-type]
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")