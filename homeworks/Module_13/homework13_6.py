from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import tg_bot_db


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_reply = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton(text='Рассчитать')
kb_reply.insert(button_calculate)

kb_inline = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_calories)
kb_inline.add(button_formulas)


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью. Нажми "Рассчитать" и начнем', reply_markup=kb_reply)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb_inline)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await call.answer()
    await UserStates.age.set()


@dp.message_handler(state=UserStates.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост')
    await UserStates.growth.set()


@dp.message_handler(state=UserStates.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес')
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
