#!/usr/bin/python3
"""
use a generator to compute
a memory-efficient aggregate function i.e average age for a large dataset
"""

seed = __import__('seed')


def stream_user_ages():
    """
    use a generator function to generate ages (one loop used)
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    q = "SELECT age FROM user_data"
    cursor.execute(q)
    for row in cursor.fetchall():
        if not row:
            break
        yield row


def find_age_average():
    """
    find the average age using ages provided by
    a generator function (one loop used)
    """
    total_age = 0
    count = 0
    for row in stream_user_ages():
        total_age += row["age"]
        count += 1

    average_age = total_age/count
    print(average_age)
    return average_age


find_age_average()