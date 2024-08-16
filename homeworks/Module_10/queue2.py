from threading import Thread
from time import sleep

import queue


def producer(queue):
    c = 0
    while True:
        c += 1
        message = 'ping ' + str(c)
        queue.put(message)


def worker(queue):
    while True:
        message = queue.get()
        sleep(1)
        print(message)


q = queue.Queue()

t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=worker, args=(q, ))

t1.start()
t2.start()

t1.join()
t2.join()
