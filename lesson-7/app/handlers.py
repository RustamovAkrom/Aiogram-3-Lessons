from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middlewares import TestMiddleware


router = Router()

router.message.middleware(TestMiddleware())


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Salom. Sening ID raqaming: {message.from_user.id},\n{message.from_user.first_name}",
                        reply_markup=kb.main)


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
    await message.answer_photo(photo="AgACAgIAAxkBAAMVZwFipPaKYKnpSEEaebRDd2mw18QAAgLlMRtb_AhIYW7xms0tVS8BAAMCAAN5AAM2BA",
                               caption="It is your photo")
    

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer("Your selected catalog.", show_alert=True)
    await callback.message.edit_text("Salom!", reply_markup=await kb.inline_cars())




@router.message(Command("register"))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Ozizni ismingizni kiriting:")


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Ozizni telefon raqamingizni kiriting:")


@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()

    await message.answer(f"Our OK.\nISM: {data['name']}\nNUMBER: {data['number']}")
    await state.clear()