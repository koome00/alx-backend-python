
"""
create a generator that streams rows from an SQL database one by one.
"""

from mysql.connector import connect, Error
import os
import csv
import uuid

def connect_db():
    """
    Connects to the database server
    """
    try:
        connection = connect(
            host = "localhost",
            password = "root",
            user = "root"
        )
        print(connection)
        return connection
    except Error as e:
        print("Connect: ", e)


def create_database(connection):
    """
    Create database ALX_prodev
    """
    try:
        q = "CREATE DATABASE IF NOT EXISTS ALX_prodev"
        cursor = connection.cursor()
        cursor.execute(q)
        connection.commit()
        print("Database created or already exists.")
    except Exception as e:
        print("DB: ", connection)



def connect_to_prodev():
    """
    Connect to ALX_prodev
    """
    try:
        connection = connect(
            host = "localhost",
            password = "root",
            user = "root",
            database = "ALX_prodev"
        )
        print("Connected to prodev: ", connection)
        return connection
    except Error as e:
        print("Prodev: ",e)


def create_table(connection):
    """
    Creates a table user_data if it does not exists with the required fields
    """
    if not connection:
        print("No connection available")
        return

    try:
        create_table_query = """
CREATE TABLE IF NOT EXISTS user_data (
    user_id BINARY(16) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL(5,2) NOT NULL
)
"""
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table exists or already created")
    except Exception as e:
        print("Table: ", e)


def insert_data(connection, data):
    """
    inserts data in the database if it does not exist
    """
    
    try:
        with open(data, newline="", encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            cursor = connection.cursor()

            for row in reader:
                user_id = uuid.uuid4().bytes

                insert_query = """INSERT INTO user_data(user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """
                user_data = (user_id, row["name"], row["email"], float(row["age"]))
                cursor.execute(insert_query, user_data)
                connection.commit()
    except Exception as e:
        print("Insert Error: ", e)

