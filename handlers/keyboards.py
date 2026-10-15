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
        [InlineKeyboardButton(text='get rick and rolled', url = 'https://share.google/KJV50wAUQAZNv4p5h')],
        [InlineKeyboardButton(text='начать игру',callback_data='quiz_start')]])

quiz_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = 'F=m x a', callback_data = 'answer_correct')],
        [InlineKeyboardButton(text = 'я ХЗ броузи', callback_data = 'answer_wrong')]]
    )

#команда инлайн две кнопки одна на сайт одна текстом отвечает 