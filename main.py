import logging
from aiogram import executor
from create_bot import dp
from handlers import admin


logging.basicConfig(level=logging.INFO)

admin.register_hendlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)