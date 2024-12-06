#!/usr/bin/python3
from mysql.connector import connect, Error
import os
import csv


def connect_db():
    """
    Connects to the database server
    """
    try:
        with connect(
            host = os.getenv("HOST"),
            password = os.getenv("PASSWORD"),
            user = os.getenv("USER")
        ) as connection:
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
        with connection.cursor() as cursor:
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
        with connect(
            host = os.getenv("HOST"),
            password = os.getenv("PASSWORD"),
            user = os.getenv("USER"),
            database = "ALX_prodev"
        ) as connection:
            print(connection)
            return connection
    except Error as e:
        print("Prodev: ",e)


def create_table(connection):
    """
    Creates a table user_data if it does not exists with the required fields
    """

    try:
        create_table_query = """
CREATE TABLE IF NOT EXISTS user_data (
    user_id BINARY(16) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL(5,2) NOT NULL,
)
"""
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit
    except Exception as e:
        print("Table: ", e)


def insert_data(connection, data):
    """
    inserts data in the database if it does not exist
    """
    try:
        insert_data_query = f"""
LOAD DATA INFILE '/{data}'
INTO TABLE user_data
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
"""
        with connection.cursor() as cursor:
            cursor.execute(insert_data_query)
            connection.commit()
    except Exception as e:
        print("Insert: ", e)



connection = connect_db()

if connection:
    create_database(connection)
    connection.close()
else:
    print("Failed to connect to MySQL.")