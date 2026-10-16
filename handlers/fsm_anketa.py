from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Add_anketa(StatesGroup):
    name = State()
    age = State()
    phone = State()
    
router_add_anketa = Router ()


@router_add_anketa.message(Command('Add_anketa'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('введите ваше имя:')
    await state.set_state(Add_anketa.name)
    
@router_add_anketa.message(Add_anketa.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('введите ваш возвраст:')
    await state.set_state(Add_anketa.age)
    
@router_add_anketa.message(Add_anketa.age)
async def age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('введите только цифры')
        return
    await state.update_data(age=int(message.text))
    await message.answer('введите ваш телефон:')
    await state.set_state(Add_anketa.phone)

@router_add_anketa.message(Add_anketa.phone)
async def add_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await message.answer(
        f"Данные анкеты:\n"
        f"Название — {data['name']}\n"
        f"Цена — {data['age']}\n"
        f"телефон — {data['phone']}"
    )
    await state.clear