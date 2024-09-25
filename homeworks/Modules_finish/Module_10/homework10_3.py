from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.lock.acquire()

    def deposit(self):
        transaction = 100
        for i in range(transaction):
            num = randint(50, 500)
            self.balance += num
            print(f'Пополнение: {num}. Баланс: {self.balance}\n', end='')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            num = randint(50, 500)
            print(f'Запрос на {num} | ', end='')
            if num <= self.balance:
                self.balance -= num
                print(f'Снятие: {num}. Баланс: {self.balance}\n', end='')
            else:
                print(f'Запрос отклонён, недостаточно средств\n', end='')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
