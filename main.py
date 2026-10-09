# 1. Создайте команду `/menu` — бот отвечает списком всех своих команд с кратким описанием каждой.
# 2. Добавьте reply-кнопку `/menu` в существующую клавиатуру `main_buttons`.
# 3. Создайте обработчик, который на сообщение `пока` (фильтр `F.text`) отвечает «До встречи!».

# ### Средний уровень

# 4. Создайте inline-кнопку «О нас» с `callback_data='about'` и обработчик: по нажатию бот отправляет короткое описание кафе.
# 5. Через FSM-диалог `/add_product` добавьте в базу 3 напитка. Затем создайте команду `/drinks`, 
# которая выводит все товары из базы. Если база пустая — бот отвечает «Меню пока пустое».

##### Сложный уровень (доп. задание ⭐)

# 6. Добавьте в FSM-диалог проверку названия: если пользователь прислал не текст,
# а фото или стикер (в этом случае `message.text` равен `None`), 
# бот просит ввести название ещё раз и **остаётся в том же состоянии** .
# 💡 *Подсказка: посмотрите, как устроена проверка цены через `isdigit()` — логика будет похожей.*
import asyncio
import logging
from aiogram import Bot, Dispatcher
from src.handlers import router
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
