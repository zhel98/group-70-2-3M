import asyncio
import logging

from config import bot, dp
from database import db
from handlers import books, commands


async def main() -> None:
    await db.init_db()
    dp.include_router(commands.router_commands)
    dp.include_router(books.router_books)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
