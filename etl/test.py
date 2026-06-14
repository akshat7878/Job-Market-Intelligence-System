import sqlite3

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM postings
""")

print(cursor.fetchone())

conn.close()