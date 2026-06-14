import pandas as pd
import sqlite3

job_skills = pd.read_csv(
    "data/jobs/job_skills.csv"
)

conn = sqlite3.connect("jobs.db")

job_skills.to_sql(
    "job_skills",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Job skills loaded successfully")