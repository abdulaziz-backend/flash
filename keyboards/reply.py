from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import REQUIRED_CHANNEL
from translations import get_text

def language_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="lang_uz"),
         InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
         InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")]
    ])
    return keyboard

def main_menu(lang):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_text("download_button", lang), callback_data="download")],
        [InlineKeyboardButton(text=get_text("help_button", lang), callback_data="help"),
         InlineKeyboardButton(text=get_text("change_language_button", lang), callback_data="change_language")]
    ])
    return keyboard

def download_button(lang):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_text("download_more_button", lang), url="https://t.me/yt_insta_downloader_bot")]
    ])
    return keyboard

def subscription_keyboard(lang):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_text("join_channel_button", lang), url=f"https://t.me/{REQUIRED_CHANNEL[1:]}")],
        [InlineKeyboardButton(text=get_text("check_subscription_button", lang), callback_data="check_subscription")]
    ])
    return keyboard