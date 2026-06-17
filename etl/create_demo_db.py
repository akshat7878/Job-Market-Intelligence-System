import pandas as pd
import sqlite3

# Create new database
conn = sqlite3.connect("jobs_demo.db")

# Load original tables
companies = pd.read_sql(
    "SELECT * FROM companies LIMIT 5000",
    sqlite3.connect("jobs.db")
)

postings = pd.read_sql(
    "SELECT * FROM postings LIMIT 20000",
    sqlite3.connect("jobs.db")
)

skills = pd.read_sql(
    "SELECT * FROM skills",
    sqlite3.connect("jobs.db")
)

industries = pd.read_sql(
    "SELECT * FROM industries",
    sqlite3.connect("jobs.db")
)

job_skills = pd.read_sql(
    "SELECT * FROM job_skills LIMIT 50000",
    sqlite3.connect("jobs.db")
)

job_industries = pd.read_sql(
    "SELECT * FROM job_industries LIMIT 50000",
    sqlite3.connect("jobs.db")
)

salaries = pd.read_sql(
    "SELECT * FROM salaries LIMIT 20000",
    sqlite3.connect("jobs.db")
)

# Save into demo db
companies.to_sql("companies", conn, index=False)
postings.to_sql("postings", conn, index=False)
skills.to_sql("skills", conn, index=False)
industries.to_sql("industries", conn, index=False)
job_skills.to_sql("job_skills", conn, index=False)
job_industries.to_sql("job_industries", conn, index=False)
salaries.to_sql("salaries", conn, index=False)

conn.close()

print("Demo database created")