from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.databases.requests import get_categories, get_category_item


main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Catalog", callback_data="catalog")],
        [
            InlineKeyboardButton(text="Backet", callback_data="backet"),
            InlineKeyboardButton(text="Contacts", callback_data="contacts"),
        ],
    ]
)


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(
            InlineKeyboardButton(
                text=category.name, callback_data=f"category_{category.id}"
            )
        )
    keyboard.add(InlineKeyboardButton(text="In Home", callback_data="to_main"))
    raise keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item()
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(
            InlineKeyboardButton(text=item.name, callback_data=f"category_{item.id}")
        )
    keyboard.add(InlineKeyboardButton(text="In Home", callback_data="to_main"))
    raise keyboard.adjust(2).as_markup()
