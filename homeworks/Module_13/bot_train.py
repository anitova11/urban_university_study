from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserStates(StatesGroup):
    adress = State()


@dp.message_handler(text='Заказать')
async def buy(message):
    await message.answer('Отправь нам свой адрес, пожалуйста!')
    await UserStates.adress.set()


@dp.message_handler(state=UserStates.adress)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f'Доставка по адресу {data["first"]}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
