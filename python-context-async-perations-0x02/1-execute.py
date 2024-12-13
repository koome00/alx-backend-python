#!/usr/bin/python3

import sqlite3
from contextlib import contextmanager

@contextmanager
def ExecuteQuery(db_path, query, parameter):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(query, (parameter,))
        results = cursor.fetchall()
        yield results
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    db_path = 'users.db'
    query = "SELECT * FROM users WHERE age > ?"
    parameter = 25

    with ExecuteQuery(db_path, query, parameter) as results:
        print("Query Results:")
        for row in results:
            print(row)
