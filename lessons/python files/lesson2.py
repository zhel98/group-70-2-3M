import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

BOT_TOKEN = '8939204700:AAHaksTu8Wm31BMz0RPvYM7qjkxz9jdRryo'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет {message.from_user.full_name} Я твой первый бот'
    )

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - привет\n'
        '/help -список команд'
    )

@dp.message(F.from_user.id == 5003920297)
async def get_group(message: Message):
    await message.answer('привет мой создатель!')
    
# @dp.message()
# async def echo(message: Message):
#     await message.answer(f'ты написал: {message.text}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
