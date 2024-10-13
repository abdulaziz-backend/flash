from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📣 Broadcast", callback_data="broadcast")],
        [InlineKeyboardButton(text="👑 Add Admin", callback_data="add_admin")]
    ])
    return keyboard