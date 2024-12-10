#!/usr/bin/python3
from mysql.connector import connect, Error
import os
import traceback

def connect_db():
    """
    Connects to the database server
    """
    try:
        connection = connect(
            host=os.getenv("HOST"),
            password=os.getenv("PASSWORD"),
            user=os.getenv("USER")
        )
        q = "CREATE DATABASE IF NOT EXISTS ALX_prodev"
        cursor = connection.cursor()
        cursor.execute(q)
        connection.commit()
        print("Database connection established")
        return connection
    except Error as e:
        print("Connect error: ", e)
        traceback.print_exc()
        return None

def connect_to_prodev():
    """
    Connect to ALX_prodev
    """
    try:
        connection = connect(
            host=os.getenv("HOST"),
            password=os.getenv("PASSWORD"),
            user=os.getenv("USER"),
            database="ALX_prodev"
        )
        print("Successfully connected to ALX_prodev")
        return connection
    except Error as e:
        print("Prodev connection error: ", e)
        traceback.print_exc()
        return None

def create_table(connection):
    """
    Creates a table user_data if it does not exist with the required fields
    """
    if not connection:
        print("No valid database connection")
        return
    
    try:
        # Verify connection is still open
        if not connection.is_connected():
            print("Connection is closed")
            return
        
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
        print("Table created successfully")
    except Error as e:
        print("Table creation error: ", e)
        traceback.print_exc()

if __name__ == "__main__":
    # Print environment variables to verify
    print("HOST:", os.getenv("HOST"))
    print("USER:", os.getenv("USER"))
    print("PASSWORD:", "****" if os.getenv("PASSWORD") else "Not set")
    
    # Debugging connection steps
    connection = connect_db()
    if connection:
        connection.close()
    
    connection = connect_to_prodev()
    if connection:
        create_table(connection)
        connection.close()