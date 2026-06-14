import pandas as pd
import sqlite3

companies = pd.read_csv(
    "data/companies/companies.csv"
)

conn = sqlite3.connect("jobs.db")

companies.to_sql(
    "companies",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print("Companies loaded successfully")