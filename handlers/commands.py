from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

router_commands = Router()


@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! "
        "Я помогу вести каталог книг.\n"
        "/add_book — добавить книгу\n"
        "/books — показать каталог"
    )
