from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.databases.requests as rq
from app.middlewares import TestMiddleware


router = Router()

router.message.outer_middleware(TestMiddleware())


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply(f"Krasofkalar magaziniga hush kelibsiz", reply_markup=kb.main)


@router.message(F.text == "catalog")
async def catalog(message: Message):
    await message.answer("Categorini tanlang:", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer("Siz kategoriyani tanladingiz!")
    await callback.message.answer("Katalogdagi tovarni tanlang", 
                                  reply_markup=await kb.items(callback.data.split("_")[1]))
