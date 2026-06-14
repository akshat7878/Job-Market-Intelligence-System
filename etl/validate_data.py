import sqlite3

tables = [
    "companies",
    "skills",
    "industries",
    "postings",
    "job_skills",
    "job_industries",
    "salaries"
]

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count:,}")

conn.close()