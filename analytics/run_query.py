import pandas as pd
import sqlite3
import sys

def run_query(sql_file):
    conn = sqlite3.connect("jobs.db")

    with open(sql_file, "r") as file:
        query = file.read()

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

if __name__ == "__main__":
    sql_file = sys.argv[1]
    df = run_query(sql_file)
    print(df)