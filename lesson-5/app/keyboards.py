from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Catalog", callback_data="catalog")],
        [
            InlineKeyboardButton(text="Backet", callback_data="backet"),
            InlineKeyboardButton(text="Contacts", callback_data="contacts"),
        ],
    ]
)


settings = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="YouTube", url="https://youtube.com/")]]
)

cars = ["Tesla", "Mercades", "MBW"]


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://youtube.com/"))
    return keyboard.adjust(2).as_markup()
