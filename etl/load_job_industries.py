import pandas as pd
import sqlite3

job_industries = pd.read_csv(
    "data/jobs/job_industries.csv"
)

conn = sqlite3.connect("jobs.db")

job_industries.to_sql(
    "job_industries",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Job industries loaded successfully")