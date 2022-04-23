from aiogram import Dispatcher, types
from key_bord import kb_st


async def send_welcome(message: types.Message):
    await message.reply("welcome, I am Data_bot, enter the year, month and day"
                        " and tell me what day of the week it was", reply_markup=kb_st)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['/start'])