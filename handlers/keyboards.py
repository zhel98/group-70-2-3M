from aiogram.types import (
ReplyKeyboardMarkup,
KeyboardButton,
InlineKeyboardMarkup,
InlineKeyboardButton,
)

reply_keyboard = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="Каталог")],
[KeyboardButton(text="Корзина"),KeyboardButton(text="Контакты"),],
[KeyboardButton(text="/menu")],],resize_keyboard=True,)

main_buttons = reply_keyboard

inline_keyboard = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
[InlineKeyboardButton(text="Начать игру",callback_data="quiz_start",)],
[InlineKeyboardButton(text="О нас",callback_data="about",)],])