from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

from handlers.keyboards import reply_keyboard, inline_keyboard
from database import db

router_commands = Router()


@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот!",
        reply_markup=reply_keyboard,
    )


@router_commands.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start — письку сосал?\n"
        "/help — помощь\n"
        "/menu — список команд\n"
        "/add_product — добавить товар\n"
        "/drinks — список напитков",
        reply_markup=inline_keyboard,
    )


@router_commands.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer(
        "☕ Команды кафе:\n\n"
        "/start — запустить бота\n"
        "/help — помощь\n"
        "/menu — список команд\n"
        "/add_product — добавить товар в меню\n"
        "/drinks — показать все напитки"
    )


@router_commands.message(Command("drinks"))
async def cmd_drinks(message: Message):
    products = db.get_all_products()

    if not products:
        await message.answer("Меню пока пустое")
        return

    text = "☕ Напитки нашего кафе:\n\n"

    for product in products:
        # product: id, name, price, description, photo
        _, name, price, description, photo = product
        text += f"• {name} — {price}\n"

    await message.answer(text)


@router_commands.message(F.text == "пока")
async def say_goodbye(message: Message):
    await message.answer("До встречи!")


@router_commands.message(F.text == "Корзина")
async def cmd_cart(message: Message):
    await message.answer("Добавлена в корзину!!!")


@router_commands.callback_query(F.data == "about")
async def about_cafe(callback: CallbackQuery):
    await callback.message.answer(
        "☕ Мы — уютное кафе, где вас ждут вкусные напитки "
        "и приятная атмосфера!"
    )
    await callback.answer()


@router_commands.callback_query(F.data == "quiz_start")
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!", show_alert=True)
    await callback.message.answer("Первый вопрос: Второй закон Ньютона?")


@router_commands.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(
        f"ID этого стикера — {message.sticker.file_id}"
    )


@router_commands.message(Command("sticker"))
async def sticker_handler(message: Message):
    await message.answer(
        "Используй команду /sticker, чтобы получить стикер."
    )