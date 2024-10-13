import logging
from aiogram import Router, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import admin as kb
from database import User, Download
from config import OWNER_ID
from database import get_db

router = Router()
logger = logging.getLogger(__name__)

class BroadcastStates(StatesGroup):
    waiting_for_message = State()

async def process_broadcast(message: Message):
    users = await User.get_all_users()
    broadcast_message = message.text.split('/broadcast ', 1)[1]
    for user in users:
        try:
            await message.bot.send_message(user['telegram_id'], broadcast_message)
        except Exception as e:
            logger.error(f"Failed to send message to {user['telegram_id']}: {e}")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(process_broadcast, commands=['broadcast'], is_chat_admin=True)

@router.message(Command("admin"), F.from_user.id == OWNER_ID)
async def admin_panel(message: Message):
    logger.info(f"Admin {message.from_user.id} accessed admin panel")
    total_users, new_users_today, total_downloads = await Download.get_stats()
    
    stats = f"📊 Stats:\n\n" \
            f"👥 Total Users: {total_users}\n" \
            f"🆕 New Users Today: {new_users_today}\n" \
            f"📥 Total Downloads: {total_downloads}"
    
    await message.reply(stats, reply_markup=kb.admin_keyboard())

@router.callback_query(F.data == "broadcast")
async def start_broadcast(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Admin {callback.from_user.id} started broadcast")
    await callback.message.edit_text("📣 Send the message you want to broadcast:")
    await state.set_state(BroadcastStates.waiting_for_message)

@router.message(BroadcastStates.waiting_for_message)
async def process_broadcast(message: Message, state: FSMContext):
    logger.info(f"Admin {message.from_user.id} sent broadcast message")
    users = await User.get_all_users()
    
    for user in users:
        try:
            await message.copy_to(user['telegram_id'])
            logger.info(f"Broadcast message sent to user {user['telegram_id']}")
        except Exception as e:
            logger.error(f"Failed to send message to user {user['telegram_id']}: {e}")
    
    await message.reply("✅ Broadcast completed!")
    await state.clear()

@router.callback_query(F.data == "add_admin")
async def add_admin(callback: CallbackQuery):
    logger.info(f"Admin {callback.from_user.id} initiated add admin process")
    await callback.message.edit_text("👑 To add a new admin, forward a message from them.")

@router.message(F.forward_from)
async def process_new_admin(message: Message):
    if message.from_user.id != OWNER_ID:
        return
    
    new_admin_id = message.forward_from.id
    logger.info(f"Admin {message.from_user.id} is adding new admin {new_admin_id}")
    user = await User.get_or_create(new_admin_id, message.forward_from.username)
    if user:
        await message.reply(f"✅ User {new_admin_id} has been added as an admin.")
    else:
        await message.reply("❌ This user is not registered in the bot.")

