import asyncio
import logging

from aiogram import Bot, Dispatcher

import config

logging.basicConfig(level=logging.INFO)

async def main():
	from handlers import start

	bot = Bot(token=config.TOKEN)

	dispatcher = Dispatcher()
	dispatcher.include_router(start.router)
	await dispatcher.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())