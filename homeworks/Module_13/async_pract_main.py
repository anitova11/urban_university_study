import asyncio
import time


async def get_temp():
    print('first pok')
    await asyncio.sleep(2)
    print('25 C')


async def get_press():
    print('second pok')
    await asyncio.sleep(4)
    print('101 kPa')


async def main():
    print('start')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_press())
    await task1
    await task2
    print('finish')


start = time.time()
asyncio.run(main())
end = time.time()

print(f'time = {round(end - start, 2)}')
