import time
import asyncio


async def notification():
    time.sleep(10)
    print('осталось 10 сек')


async def main():
    task = asyncio.create_task(notification())
    print('собираемся')
    print('едем')

asyncio.run(main())
