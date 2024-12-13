#!/usr/bin/python3

import asyncio
import aiosqlite

async def async_fetch_users():
    db_path = 'users.db'
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users():
    db_path = 'users.db'
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    db_path = 'users.db'
    users, older_users = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    
    print("All Users:")
    for user in users:
        print(user)
    
    print("\nUsers Older Than 40:")
    for user in older_users:
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
