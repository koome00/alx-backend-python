#!/usr/bin/python3

import os
from mysql.connector import connect, Error


def stream_users_in_batches(batch_size):
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
            q = f"SELECT * FROM user_data LIMIT {batch_size}"
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

def batch_processing(batch_size):
    user_dict = stream_users_in_batches(batch_size)
    for row in user_dict:
        if row["age"] >= 25:
            print(row)
    return None
        
