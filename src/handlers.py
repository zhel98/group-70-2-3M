from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from src.keyboards import reply_keyboard, inline_keyboard, inline_keyboard2

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет {message.from_user.full_name} Я твой первый бот',
        reply_markup=reply_keyboard
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - привет\n'
        '/help -список команд',
        reply_markup=inline_keyboard
    )

@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer('Начинаем игру!!', show_alert=True)
    await callback.message.answer('первый вопрос: Второй закон Ньютона')
    

@router.message(F.text == 'каталог')
async def cat(message: Message):
    await message.answer(
        'выберите действие:',
        reply_markup=inline_keyboard2
    )

@router.callback_query(F.data == 'get_ez')
async def ez(callback: CallbackQuery):
    await callback.answer('мощный тыы тип!')

@router.message(F.from_user.id == 5003920297)
async def get_group(message: Message):
    await message.answer('привет мой создатель!')
    