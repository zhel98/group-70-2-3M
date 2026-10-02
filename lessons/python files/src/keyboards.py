from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='каталог')],
        [KeyboardButton(text='корзина'),KeyboardButton(text='контакты')
        ]])


inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='наш сайт', url='https://farmamir.kg')],
        [InlineKeyboardButton(text='начать игру',callback_data='quiz_start')]])