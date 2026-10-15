from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Add_anketa(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()

router_add_product = Router ()


@router_add_product.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('введите название товара:')
    await state.set_state(Add_product.name)
    
@router_add_product.message(Add_product.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('введите цену товарв')
    await state.set_state(Add_product.price)
    
@router_add_product.message(Add_product.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('введите описание товара')
    await state.set_state(Add_product.description)

@router_add_product.message(Add_product.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('введите фото товара')
    await state.set_state(Add_product.photo)
    
@router_add_product.message(Add_product.photo)
async def add_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer_photo(
    photo=data['photo'],
    caption=(
        f"Данные товара:\n"
        f"Название — {data['name']}\n"
        f"Цена — {data['price']}\n"
        f"Описание — {data['description']}"
    ))
    await state.clear