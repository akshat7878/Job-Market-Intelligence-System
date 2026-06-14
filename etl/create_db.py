import sqlite3

conn = sqlite3.connect("jobs.db")
print("Database created successfully")
conn.close()