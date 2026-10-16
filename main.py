import asyncio
import logging

from handlers import commands, echo, fsm_add_product, fsm_anketa
from config import bot, dp




async def main():
    #handlers registration
    dp.include_router(commands.router_commands)
    dp.include_router(fsm_add_product.router_add_product)
    dp.include_router(fsm_anketa.router_add_anketa)

    #echo registration
    dp.include_router(echo.router_echo)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
