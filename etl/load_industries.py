import pandas as pd
import sqlite3

industries = pd.read_csv(
    "data/mappings/industries.csv"
)

conn = sqlite3.connect("jobs.db")

industries.to_sql(
    "industries",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Industries loaded successfully")