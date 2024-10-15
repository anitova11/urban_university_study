from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# kb = ReplyKeyboardMarkup()
# button = KeyboardButton(text='Info')
# kb.insert(button)

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Info', callback_data='info')
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Info')],
        [KeyboardButton(text='health'),
         KeyboardButton(text='health2')],
        [KeyboardButton(text='info2')]

    ],
    resize_keyboard=True
)


@dp.message_handler(commands='start')
async def starter(message):
    await message.answer('Hi!', reply_markup=start_menu)


@dp.callback_query_handler(text='info')  # из callback_data
async def infor(call):
    await call.message.answer('Информация типо')
    await call.answer()


# ----------------------------------------------------------

# @dp.message_handler(commands='start')
# async def start_(message):
#     await message.answer('Hi!', reply_markup=kb)
#
#
# @dp.message_handler(text='Info')
# async def inform(message):
#     await message.answer('Информация типо')

# -----------------------------------------------------------

# class UserStates(StatesGroup):
#     adress = State()
#
#
# @dp.message_handler(text='Заказать')
# async def buy(message):
#     await message.answer('Отправь нам свой адрес, пожалуйста!')
#     await UserStates.adress.set()
#
#
# @dp.message_handler(state=UserStates.adress)
# async def fsm_handler(message, state):
#     await state.update_data(first=message.text)
#     data = await state.get_data()
#     await message.answer(f'Доставка по адресу {data["first"]}')
#     await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
