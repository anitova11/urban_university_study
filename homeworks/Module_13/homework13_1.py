import asyncio
import time


async def start_strongman(name, power):
    start = time.time()
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар номер {i + 1}')
    end = time.time()
    print(f'Силач {name} закончил соревнования за {round(end - start, 2)} секунд')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Ksu', 4))
    task2 = asyncio.create_task(start_strongman('Nick', 6))
    task3 = asyncio.create_task(start_strongman('Gosha', 2))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
