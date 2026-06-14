import pandas as pd
import sqlite3

skills = pd.read_csv(
    "data/mappings/skills.csv"
)

conn = sqlite3.connect("jobs.db")

skills.to_sql(
    "skills",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Skills loaded successfully")