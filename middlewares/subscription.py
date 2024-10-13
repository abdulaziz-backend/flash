from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from config import REQUIRED_CHANNEL
from keyboards.reply import subscription_keyboard

class SubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, CallbackQuery):
            user_id = event.from_user.id
            message = event.message
        elif isinstance(event, Message):
            user_id = event.from_user.id
            message = event
        else:
            return await handler(event, data)

        try:
            user = await event.bot.get_chat_member(REQUIRED_CHANNEL, user_id)
            if user.status in ['member', 'administrator', 'creator']:
                return await handler(event, data)
        except TelegramBadRequest:
            pass
        
        await message.answer(f"Please subscribe to {REQUIRED_CHANNEL} to use this bot.", reply_markup=subscription_keyboard())
        return