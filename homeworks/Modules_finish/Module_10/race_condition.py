import threading
import time

x = 0


def thread_task():
    global x
    for i in range(10000000):
        x = x + 1


def main():
    global x
    x = 0
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
    print(x)

# данная задача не является проблемой в версии python 3.10 и выше.
# чтобы решить эту проблему в более старых версиях, используется класс Lock. на примере функции

lock = threading.Lock()


def thread_task1():
    global x
    for i in range(10000000):
        lock.acquire()      # with lock:
        x = x + 1           # x = x + 1
        lock.release()

# это решит задачу наложения, НО заметно замедлит работу программы. Непозволительно замедлит. Не подходит
# можно еще использовать with lock. Но тоже медленно


# взаимная блокировка
lock1 = threading.Lock()
lock2 = threading.Lock()


def threading_locks1():
    lock1.acquire()
    print('thr1 lock1 acquired')
    time.sleep(1)
    lock2.acquire()
    print('thr1 lock2 acquired')
    lock2.release()
    lock1.release()


def threading_locks2():
    lock2.acquire()
    print('thr1 lock2 acquired')
    time.sleep(1)
    lock1.acquire()
    print('thr1 lock1 acquired')
    lock1.release()
    lock2.release()


t1 = threading.Thread(target=threading_locks1())
t2 = threading.Thread(target=threading_locks2())

t1.start()
t2.start()

t1.join()
t2.join()   # получаем взаимную блокировку потоков. Один не может открыть замок, потому что второй уже занял

# наверное, лучший способ с помощью try


def thread_task2():
    global x
    for i in range(10000000):
        try:
            lock.acquire()
            x = x + 1
        finally:
            lock.release()
