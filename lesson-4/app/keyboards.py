from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Katalog")],
        [KeyboardButton(text="Korzinga"), KeyboardButton(text="Contacts")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Select my punkt.",
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
