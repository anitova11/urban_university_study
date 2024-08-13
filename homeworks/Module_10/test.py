import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def threading_locks1():
    lock1.acquire()
    print('thr1 lock1 acquired')
    time.sleep(2)
    lock2.acquire()
    print('thr1 lock2 acquired')
    lock2.release()
    lock1.release()


def threading_locks2():
    lock2.acquire()
    print('thr2 lock2 acquired')
    time.sleep(2)
    lock1.acquire()
    print('thr2 lock1 acquired')
    lock1.release()
    lock2.release()


t1 = threading.Thread(target=threading_locks1())
t2 = threading.Thread(target=threading_locks2())

t1.start()
t2.start()

t1.join()
t2.join()
