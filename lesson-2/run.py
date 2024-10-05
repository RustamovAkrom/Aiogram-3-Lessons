import asyncio
import logging
import aiogram

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from .config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Salom. Sening ID raqaming: {message.from_user.id},\n{message.from_user.first_name}")


@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer("But buyruq /help")


@dp.message(F.text == "Ishlar qanday?")
async def how_are_you(message: Message):
    await message.answer("OK!")


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@dp.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMVZwFipPaKYKnpSEEaebRDd2mw18QAAgLlMRtb_AhIYW7xms0tVS8BAAMCAAN5AAM2BA",
                               caption="It is your photo")

async def main():
    await dp.start_polling(bot)


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")