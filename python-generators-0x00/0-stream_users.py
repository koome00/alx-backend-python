#!/usr/bin/python3

from mysql.connector import connect, Error
import os


def stream_users():
    """
    stream users one by one using 
    """
    try:
        connection = connect(
            host = os.getenv("HOST"),
            password = os.getenv("PASSWORD"),
            user = os.getenv("USER"),
            database = "ALX_prodev"
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            q = "SELECT * FROM user_data"
            cursor.execute(q)
            for row in cursor.fetchall():
                yield row
        else:
            print("Connection failed")
    except Error as e:
        print("Error is: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()