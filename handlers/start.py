import sys

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

sys.path.append("..")

import config
from util import data_dict

router = Router()

def cancel_button(username: str, message_id: int) -> InlineKeyboardMarkup:
	builder = InlineKeyboardBuilder()

	builder.button(
        text="❌ Отменить",
        callback_data=f"cancel=username:{username},message_id:{message_id}"
    )

	return builder.as_markup()

def answer_button(username: str, chat_id: int, message_id: int) -> InlineKeyboardMarkup:
	builder = InlineKeyboardBuilder()

	builder.button(
        text="✅ Пометить отвеченным",
        callback_data=f"answer=username:{username},chat_id:{chat_id},message_id:{message_id}"
    )

	return builder.as_markup()

@router.message(CommandStart())
async def start(message: Message):
	user = message.from_user
	username = user.username

	if user.id == config.OWNER_ID: return await message.answer("❗ Вы являетесь владельцем бота")

	notification_message = await message.bot.send_message(
		chat_id=config.OWNER_ID,
		text=f"☎ Пользователь @{username} желает связаться с вами"
	)

	request_message = await message.answer(
		text="🕑 Обращение отправлено, ожидайте ответа",
		reply_markup=cancel_button(username, notification_message.message_id)
	)

	await notification_message.edit_reply_markup(
		reply_markup=answer_button(username, request_message.chat.id, request_message.message_id)
	)
    
@router.callback_query(F.data.startswith("answer"))
async def start(callback: CallbackQuery):
	data = data_dict(callback.data)

	username = data["username"]
	chat_id = data["chat_id"]
	message_id = data["message_id"]

	await callback.bot.send_message(chat_id, "✅ Ответ получен, проверьте личные сообщения")
	await callback.bot.delete_message(chat_id=chat_id, message_id=message_id)

	await callback.message.answer(f"✅ Вы ответили @{username}")
	await callback.message.delete()

	await callback.answer()
    
@router.callback_query(F.data.startswith("cancel"))
async def start(callback: CallbackQuery):
	data = data_dict(callback.data)

	username = data["username"]
	message_id = data["message_id"]

	await callback.bot.send_message(config.OWNER_ID, f"❌ Пользователь @{username} отменил обращение")
	await callback.bot.delete_message(chat_id=config.OWNER_ID, message_id=message_id)

	await callback.message.edit_text("❌ Обращение отменено")

	await callback.answer()