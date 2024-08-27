from random import randint, random
from time import sleep
from threading import Thread
import queue


class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            sleep(randint(1, 5))
            if random() > 0.9:
                self.queue.put('горелая булка')
            else:
                self.queue.put('нормальная булка')


class Kotleta(Thread):
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        while self.count:
            print(self.queue.qsize())
            bulka = self.queue.get()
            if bulka == 'нормальная булка':
                sleep(randint(1, 5))
                self.count -= 1
            print('булок к приготовлению осталось ', self.count)


queue = queue.Queue(maxsize=10)
t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
