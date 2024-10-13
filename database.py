import asyncpg
import os
from contextlib import asynccontextmanager

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://flashdownloader_user:8D8kPH52tEsZHPCyxGxTSKt8lQuSszMz@dpg-cs5vejt6l47c73f8ta9g-a.oregon-postgres.render.com/flashdownloader')

async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute('''CREATE TABLE IF NOT EXISTS users (
                          id SERIAL PRIMARY KEY, 
                          telegram_id BIGINT UNIQUE, 
                          username TEXT, 
                          language TEXT DEFAULT 'en', 
                          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    await conn.execute('''CREATE TABLE IF NOT EXISTS downloads (
                          id SERIAL PRIMARY KEY, 
                          user_id INTEGER, 
                          platform TEXT, 
                          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    await conn.close()

@asynccontextmanager
async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

class User:
    @staticmethod
    async def get_or_create(telegram_id, username):
        async with get_db() as conn:
            user = await conn.fetchrow("SELECT * FROM users WHERE telegram_id = $1", telegram_id)
            if not user:
                await conn.execute("INSERT INTO users (telegram_id, username) VALUES ($1, $2)", telegram_id, username)
                user = await conn.fetchrow("SELECT * FROM users WHERE telegram_id = $1", telegram_id)
            return user

    @staticmethod
    async def update_language(telegram_id, language):
        async with get_db() as conn:
            await conn.execute("UPDATE users SET language = $1 WHERE telegram_id = $2", language, telegram_id)

    @staticmethod
    async def get_language(telegram_id):
        async with get_db() as conn:
            result = await conn.fetchval("SELECT language FROM users WHERE telegram_id = $1", telegram_id)
            return result if result else 'en'

    @staticmethod
    async def get_all_users():
        async with get_db() as conn:
            return await conn.fetch("SELECT * FROM users")

class Download:
    @staticmethod
    async def create(user_id, platform):
        async with get_db() as conn:
            await conn.execute("INSERT INTO downloads (user_id, platform) VALUES ($1, $2)", user_id, platform)

    @staticmethod
    async def get_stats():
        async with get_db() as conn:
            total_users = await conn.fetchval("SELECT COUNT(*) FROM users")
            new_users_today = await conn.fetchval("SELECT COUNT(*) FROM users WHERE DATE(created_at) = CURRENT_DATE")
            total_downloads = await conn.fetchval("SELECT COUNT(*) FROM downloads")
            return total_users, new_users_today, total_downloads
