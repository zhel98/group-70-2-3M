from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from database import db


class AddBook(StatesGroup):
    book_id = State()
    title = State()
    author = State()
    genre = State()


router_books = Router()


@router_books.message(Command("add_book"))
async def add_book_start(message: Message, state: FSMContext):
    await message.answer("Введите номер книги -целое число):")
    await state.set_state(AddBook.book_id)


@router_books.message(AddBook.book_id)
async def add_book_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Номер книги должен быть числом. Трайни еще раз дурень:")
        return
    await message.answer("Введите название книги:")
    await state.set_state(AddBook.title)
    await state.update_data(book_id=int(message.text))


@router_books.message(AddBook.title)
async def add_book_title(message: Message, state: FSMContext):
    if message.text is None or not message.text.strip():
        await message.answer("Введите название книги текстом:")
        return

    await state.update_data(title=message.text.strip())
    await message.answer("Введите автора книги:")
    await state.set_state(AddBook.author)


@router_books.message(AddBook.author)
async def add_book_author(message: Message, state: FSMContext) :
    if message.text is None or not message.text.strip():
        await message.answer("Введите автора книги текстом:")
        return

    await state.update_data(author=message.text.strip())
    await message.answer("Введите жанр книги:")
    await state.set_state(AddBook.genre)


@router_books.message(AddBook.genre)
async def add_book_genre(message: Message, state: FSMContext):
    if message.text is None or not message.text.strip():
        await message.answer("Введите жанр книги текстом:")
        return

    await state.update_data(genre=message.text.strip())
    data = await state.get_data()
    await db.add_book(
        book_id=data["book_id"],
        title=data["title"],
        author=data["author"],
        genre=data["genre"],
    )
    await message.answer(
        "Книга добавлена!\n"
        f"Номер: {data['book_id']}\n"
        f"Название: {data['title']}\n"
        f"Автор: {data['author']}\n"
        f"Жанр: {data['genre']}"
    )
    await state.clear()


@router_books.message(Command("books"))
async def list_books(message: Message):
    books = await db.get_books()
    if not books:
        await message.answer("Каталог книг пока пуст.")
        return

    for book_id, title, author, genre in books:
        await message.answer(
            f"Номер: {book_id}\n"
            f"Название: {title}\n"
            f"Автор: {author}\n"
            f"Жанр: {genre}"
        )
