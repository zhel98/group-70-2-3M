from aiogram import Router, F
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


@router_add_product.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название товара: ')
    await state.set_state(Add_product.name)


@router_add_product.message(Add_product.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара:')
    await state.set_state(Add_product.price)

@router_add_product.message(Add_product.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Введите описание товара:')
    await state.set_state(Add_product.description)


@router_add_product.message(Add_product.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Отправьте фото товара:')
    await state.set_state(Add_product.photo)


@router_add_product.message(Add_product.photo)
async def add_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()

    await message.answer_photo(photo=data['photo'], 
                               caption=f'Данные товара: \nНазвание - {data['name']} '
                               f'\nЦена - {data['price']} \nОписание - {data['description']}')

    db.add_product_db(name=data['name'], price=data['price'], description=data['description'], photo=data['photo'])

    await state.clear()