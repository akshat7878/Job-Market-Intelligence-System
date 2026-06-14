import pandas as pd
import sqlite3

postings = pd.read_csv(
    "data/postings.csv"
)

postings_subset = postings[
    [
        "job_id",
        "company_id",
        "title",
        "description",
        "location",
        "formatted_work_type",
        "formatted_experience_level",
        "remote_allowed",
        "work_type",
        "currency",
        "normalized_salary"
    ]
].copy()

postings_subset["company_id"] = postings_subset["company_id"].fillna(0).astype(int)
postings_subset["remote_allowed"] = postings_subset["remote_allowed"].fillna(0).astype(int)

conn = sqlite3.connect("jobs.db")

postings_subset.to_sql(
    "postings",
    conn,
    if_exists="append",
    index=False
)

conn.commit()
conn.close()

print("Postings loaded successfully")