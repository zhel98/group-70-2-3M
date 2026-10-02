from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет {message.from_user.full_name} Я твой первый бот'
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - привет\n'
        '/help -список команд'
    )

@router.message(F.from_user.id == 5003920297)
async def get_group(message: Message):
    await message.answer('привет мой создатель!')
    