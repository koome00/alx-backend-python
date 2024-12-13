#!/usr/bin/python3

import sqlite3


class ExecuteQuery:
    def __init__(self, db_path, query, parameters):
        self.db_path = db_path
        self.query = query
        self.parameters = parameters

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.parameters)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

if __name__ == "__main__":
    db_path = 'users.db'
    query = "SELECT * FROM users WHERE age > ?"
    parameter = (25,)

    with ExecuteQuery(db_path, query, parameter) as results:
        for row in results:
            print(row)

