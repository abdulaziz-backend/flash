from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from database import User

class LanguageMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, (Message, CallbackQuery)):
            user_id = event.from_user.id
            language = await User.get_language(user_id)
            data["user_language"] = language
        return await handler(event, data)