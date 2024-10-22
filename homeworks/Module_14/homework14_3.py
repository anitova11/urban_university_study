from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_reply = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')
kb_reply.add(button_calculate, button_buy)

kb_inline = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_calories)
kb_inline.add(button_formulas)

kb_buying = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button4 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button5 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button6 = InlineKeyboardButton(text='Product4', callback_data='product_buying')

kb_buying.add(button3)
kb_buying.add(button4)
kb_buying.add(button5)
kb_buying.add(button6)


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


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    vitamins = ['vitamin C.jpg', 'vitamin D.jpg', 'vitamin E.jpg', 'vitamin B1.jpg']
    count = 0
    for i in vitamins:
        count += 1
        with open(i, 'rb') as img:
            await message.answer(f'Название: Product{count} | Описание: {i[:-3:]} | Цена: {count * 100}')
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки', reply_markup=kb_buying)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


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
