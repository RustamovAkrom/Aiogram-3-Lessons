from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f"Salom. Sening ID raqaming: {message.from_user.id},\n{message.from_user.first_name}"
    )


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("But buyruq /help")


@router.message(F.text == "Ishlar qanday?")
async def how_are_you(message: Message):
    await message.answer("OK!")


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMVZwFipPaKYKnpSEEaebRDd2mw18QAAgLlMRtb_AhIYW7xms0tVS8BAAMCAAN5AAM2BA",
        caption="It is your photo",
    )
