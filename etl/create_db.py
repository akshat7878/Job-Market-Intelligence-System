import sqlite3

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()

with open("sql/schema.sql", "r") as file:
    sql_script = file.read()

cursor.executescript(sql_script)

conn.commit()

print("Database and tables created successfully")

conn.close()