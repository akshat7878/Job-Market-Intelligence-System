import sqlite3
import pandas as pd

SOURCE_DB = "jobs.db"
DEMO_DB = "jobs_demo.db"

# Connect to source database
source_conn = sqlite3.connect(SOURCE_DB)

# Smaller samples for deployment
companies = pd.read_sql(
    "SELECT * FROM companies LIMIT 1000",
    source_conn
)

postings = pd.read_sql(
    "SELECT * FROM postings LIMIT 3000",
    source_conn
)

skills = pd.read_sql(
    "SELECT * FROM skills",
    source_conn
)

industries = pd.read_sql(
    "SELECT * FROM industries",
    source_conn
)

job_skills = pd.read_sql(
    "SELECT * FROM job_skills LIMIT 5000",
    source_conn
)

job_industries = pd.read_sql(
    "SELECT * FROM job_industries LIMIT 5000",
    source_conn
)

salaries = pd.read_sql(
    "SELECT * FROM salaries LIMIT 3000",
    source_conn
)

source_conn.close()

# Create demo database
demo_conn = sqlite3.connect(DEMO_DB)

companies.to_sql(
    "companies",
    demo_conn,
    if_exists="replace",
    index=False
)

postings.to_sql(
    "postings",
    demo_conn,
    if_exists="replace",
    index=False
)

skills.to_sql(
    "skills",
    demo_conn,
    if_exists="replace",
    index=False
)

industries.to_sql(
    "industries",
    demo_conn,
    if_exists="replace",
    index=False
)

job_skills.to_sql(
    "job_skills",
    demo_conn,
    if_exists="replace",
    index=False
)

job_industries.to_sql(
    "job_industries",
    demo_conn,
    if_exists="replace",
    index=False
)

salaries.to_sql(
    "salaries",
    demo_conn,
    if_exists="replace",
    index=False
)

demo_conn.close()

print("jobs_demo.db created successfully")