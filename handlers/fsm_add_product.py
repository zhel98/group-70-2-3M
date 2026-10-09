from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import db


class Add_product(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()


router_add_product = Router()


@router_add_product.message(Command("add_product"))
async def add_start_fsm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Введите название товара:")
    await state.set_state(Add_product.name)


@router_add_product.message(Add_product.name)
async def add_name(message: Message, state: FSMContext):
    # Доп зад: название должно быть текстом при фото или стикере остаёмся в том же состоянии.
    if message.text is None or not message.text.strip():
        await message.answer("Пожалуйста, введите название текстом:")
        return

    await state.update_data(name=message.text.strip())
    await message.answer("Введите цену товара (только число):")
    await state.set_state(Add_product.price)


@router_add_product.message(Add_product.price)
async def add_price(message: Message, state: FSMContext):
    if message.text is None or not message.text.isdigit():
        await message.answer(
            "Цена должна быть целым положительным числом. Попробуйте ещё раз:"
        )
        return

    await state.update_data(price=int(message.text))
    await message.answer("Введите описание товара:")
    await state.set_state(Add_product.description)


@router_add_product.message(Add_product.description)
async def add_description(message: Message, state: FSMContext):
    if message.text is None or not message.text.strip():
        await message.answer("Введите описание текстом:")
        return

    await state.update_data(description=message.text.strip())
    await message.answer("Отправьте фото товара:")
    await state.set_state(Add_product.photo)


@router_add_product.message(Add_product.photo)
async def add_photo(message: Message, state: FSMContext):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте фото товара:")
        return

    await state.update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()

    db.add_product_db(
        name=data["name"],
        price=data["price"],
        description=data["description"],
        photo=data["photo"],
    )

    await message.answer(
        f" Товар добавлен!\n\n"
        f"Название: {data['name']}\n"
        f"Цена: {data['price']}\n"
        f"Описание: {data['description']}"
    )

    await state.clear()