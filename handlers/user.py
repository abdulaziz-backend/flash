import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import reply as kb
from services import downloader
from database import User, Download
from config import REQUIRED_CHANNEL
from translations import get_text

router = Router()
logger = logging.getLogger(__name__)

class DownloadStates(StatesGroup):
    waiting_for_link = State()

@router.message(Command("start"))
async def cmd_start(message: Message, user_language: str):
    logger.info(f"User {message.from_user.id} started the bot")
    user = await User.get_or_create(message.from_user.id, message.from_user.username)
    await message.reply(get_text("welcome_message", user_language), reply_markup=kb.language_keyboard())

@router.callback_query(F.data.startswith("lang_"))
async def process_language(callback: CallbackQuery, user_language: str):
    lang = callback.data.split("_")[1]
    logger.info(f"User {callback.from_user.id} set language to {lang}")
    await User.update_language(callback.from_user.id, lang)
    await callback.message.edit_text(
        get_text("language_set", lang).format(lang=lang.upper()),
        reply_markup=kb.main_menu(lang)
    )

@router.callback_query(F.data == "check_subscription")
async def check_subscription(callback: CallbackQuery, user_language: str):
    logger.info(f"User {callback.from_user.id} checking subscription")
    try:
        user = await callback.bot.get_chat_member(REQUIRED_CHANNEL, callback.from_user.id)
        if user.status in ['member', 'administrator', 'creator']:
            await callback.message.edit_text(get_text("subscription_confirmed", user_language), reply_markup=kb.main_menu(user_language))
        else:
            await callback.answer(get_text("subscription_required", user_language), show_alert=True)
    except Exception as e:
        logger.error(f"Error checking subscription for user {callback.from_user.id}: {e}")
        await callback.answer(get_text("subscription_check_error", user_language), show_alert=True)

@router.message(Command("help"))
async def cmd_help(message: Message, user_language: str):
    logger.info(f"User {message.from_user.id} requested help")
    help_text = get_text("help_text", user_language)
    await message.reply(help_text, reply_markup=kb.main_menu(user_language))

@router.message(F.text.contains("http"))
async def process_link(message: Message, state: FSMContext):
    await message.reply("⏳ Processing your request... Please wait.")
    link = message.text
    platform = "youtube" if "youtube.com" in link or "youtu.be" in link else "instagram"
    
    try:
        media = await downloader.download_media(link, platform)
        if media:
            caption = "✅ Downloaded with @yt_insta_downloader_bot"
            with open(media, 'rb') as file:
                await message.reply_document(file, caption=caption, reply_markup=kb.download_button())
            await Download.create(message.from_user.id, platform)
            downloader.delete_file(media)
        else:
            await message.reply("❌ Sorry, couldn't download the media. Please check the link and try again.")
    except Exception as e:
        print(f"Error downloading media: {str(e)}")
        await message.reply("❌ An error occurred while processing your request. Please try again later.")

async def download_animation(message: Message, user_language: str):
    animation = ["⏳", "⌛"]
    i = 0
    while True:
        await message.edit_text(f"{animation[i]} {get_text('processing_request', user_language)}")
        await asyncio.sleep(0.5)
        i = (i + 1) % 2

@router.callback_query(F.data == "download")
async def prompt_download(callback: CallbackQuery, user_language: str):
    logger.info(f"User {callback.from_user.id} requested download")
    await callback.message.edit_text(get_text("send_link", user_language))

@router.callback_query(F.data == "help")
async def help_command(callback: CallbackQuery, user_language: str):
    await callback.message.edit_text(get_text("help_text", user_language), reply_markup=kb.main_menu(user_language))

@router.callback_query(F.data == "change_language")
async def change_language(callback: CallbackQuery, user_language: str):
    logger.info(f"User {callback.from_user.id} requested language change")
    await callback.message.edit_text(get_text("choose_language", user_language), reply_markup=kb.language_keyboard())