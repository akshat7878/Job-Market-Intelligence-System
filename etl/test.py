import sqlite3

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()

with open("sql/top_skills.sql", "r") as file:
    sql_script = file.read()

cursor.execute(sql_script)

results = cursor.fetchall()

for row in results:
    print(row)


conn.close()