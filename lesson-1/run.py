import asyncio
import logging
import aiogram

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Salom!")


async def main():
    await dp.start_polling(bot)


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")