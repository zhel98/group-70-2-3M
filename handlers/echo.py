from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


router_echo = Router()

@router_echo.message()
async def echo(message: Message):
    await message.answer(f'Ты написал:{message.text}')