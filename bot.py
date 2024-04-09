import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

import config

logging.basicConfig(level=logging.INFO)

async def main():
	from handlers import start

	# session = AiohttpSession(proxy=config.PROXY)
	bot = Bot(token=config.TOKEN, session=None)

	dispatcher = Dispatcher()
	dispatcher.include_router(start.router)
	await dispatcher.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())