import sqlite3

class DatabaseConnection:
   
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            print(f"Connected to the database: {self.db_path}")
            return self.cursor
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the database: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            try:
                if exc_type is None:
                    self.connection.commit()
                else:
                    self.connection.rollback()
            except sqlite3.Error as e:
                print(f"An error occurred while handling the transaction: {e}")
            finally:
                self.connection.close()
                print("Database connection closed.")

if __name__ == "__main__":
    db_path = 'users.db'

    query = "SELECT * FROM users"

    with DatabaseConnection(db_path) as cursor:
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            print("Query Results:")
            for row in results:
                print(row)
        except sqlite3.Error as e:
            print(f"An error occurred while executing the query: {e}")
