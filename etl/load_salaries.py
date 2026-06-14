import pandas as pd
import sqlite3

salaries = pd.read_csv(
    "data/jobs/salaries.csv"
)

conn = sqlite3.connect("jobs.db")

salaries.to_sql(
    "salaries",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Salaries loaded successfully")