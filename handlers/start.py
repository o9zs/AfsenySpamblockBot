from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config
from util import data_dict

router = Router()

def cancel(username: str, notification_id: int) -> InlineKeyboardMarkup:
	builder = InlineKeyboardBuilder()

	builder.button(
        text="❌ Отменить",
        callback_data=f"cancel=username:{username},notification_id:{notification_id}"
    )

	return builder.as_markup()

@router.message(CommandStart())
async def start(message: Message):
	username = message.from_user.username
	notification = await message.bot.send_message(config.OWNER_ID, f"☎ Пользователь @{username} желает связаться с вами")
	notification_id = notification.message_id

	await message.answer(
		"🕑 Обращение отправлено, ожидайте ответа",
		reply_markup=cancel(username, notification_id)
	)
    
@router.callback_query(F.data.startswith("cancel"))
async def start(callback: CallbackQuery):
	data = data_dict(callback.data)

	username = data["username"]
	notification_id = data["notification_id"]

	await callback.bot.edit_message_text(f"❌ Пользователь @{username} отменил обращение", config.OWNER_ID, notification_id)

	await callback.message.edit_text(
		"❌ Обращение отменено"
	)

	await callback.answer()