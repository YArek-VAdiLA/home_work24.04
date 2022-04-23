from aiogram import Dispatcher,types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime
import serch_day as m
from keyboards import kb_day,kb_cancel

class FSMAdmin(StatesGroup):
   data= State()

async def send_welcome(message: types.Message):
    await message.reply("welcome, I am Data_bot, enter the year, month and day"
                        " and tell me what day of the week it was", reply_markup=kb_day)


async def Data(message: types.Message):
    await FSMAdmin.data.set()
    await message.reply("send date, for example:"
                        " 2012,12,12", reply_markup=kb_cancel)

async def date(message: types.Message,state: FSMContext ):
   parsed_message = message.text.split(',')
   if len(parsed_message) == 3:
        date = datetime.datetime(int(parsed_message[0]), int(parsed_message[1]), int(parsed_message[2]))
        datebase = date.ctime()
        dateday = m.selectday(datebase[:3])
        datedays = str(dateday[0][1])
        await message.reply(datedays)
   else:
        await message.reply("Некоректное сообщение.",kb_cancel)

   await state.finish()
   await message.reply("good day", reply_markup=kb_day)

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_day)





def register_hendlers(dp:Dispatcher):
    dp.register_message_handler(send_welcome, commands=['/start'], state=None)
    dp.register_message_handler(cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(Data,lambda message: message.text.startswith("day week"))
    dp.register_message_handler(date,state=FSMAdmin.data)
