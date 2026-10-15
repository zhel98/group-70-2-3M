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

inline_keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='get rick and rolled', url = 'https://share.google/KJV50wAUQAZNv4p5h')],
        [InlineKeyboardButton(text = 'ez', callback_data = 'get_ez')]])

#команда инлайн две кнопки одна на сайт одна текстом отвечает 