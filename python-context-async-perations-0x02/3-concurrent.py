import asyncio
import aiosqlite

async def async_fetch_users(db_path):
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users(db_path, age):
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (age,)) as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    db_path = 'users.db'
    users_task = async_fetch_users(db_path)
    older_users_task = async_fetch_older_users(db_path, 40)
    users, older_users = await asyncio.gather(users_task, older_users_task)
    
    print("All Users:")
    for user in users:
        print(user)
    
    print("\nUsers Older Than 40:")
    for user in older_users:
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
