import aiosqlite

from config import path_db
from database import queries


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute("PRAGMA foreign_keys = ON")
        await conn.execute(queries.create_books_table)
        await conn.execute(queries.create_books_detail_table)
        await conn.commit()


async def book_exists(book_id: int) -> bool:
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.select_book_id, (book_id,))
        return await cursor.fetchone() is not None


async def add_book(book_id: int, title: str, author: str, genre: str):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_book,(book_id, title, author),)
        await conn.execute(queries.insert_book_detail,(book_id, genre),)
        await conn.commit()


async def get_books() -> list[tuple[int, str, str, str]]:
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_books)
        return await cursor.fetchall()

