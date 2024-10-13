import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import user, admin
from middlewares.language import LanguageMiddleware
from middlewares.subscription import SubscriptionMiddleware
from database import init_db

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.message.middleware(LanguageMiddleware())
dp.callback_query.middleware(LanguageMiddleware())
dp.message.middleware(SubscriptionMiddleware())
dp.callback_query.middleware(SubscriptionMiddleware())

async def main():
    await init_db()
    
    dp.include_router(user.router)
    dp.include_router(admin.router)
    
    print("This bot was created by abdulaziz")
    print("Subscribe to this channel: @pythonnews_uzbekistan")
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())