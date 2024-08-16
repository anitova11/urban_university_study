from threading import Thread
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.que = Queue()
        self.tables = [*args]
        self.temp_tab = []  # хранилище для занятых столов

    def guest_arrival(self, *my_guests):
        for g in range(len(my_guests)):
            full = False
            for t in range(g, len(self.tables)):
                if self.tables[t].guest is None:
                    self.tables[t].guest = my_guests[g]
                    print(f'{my_guests[g].name} сел(-а) за стол номер {self.tables[t].number}')
                    my_guests[g].start()
                    full = True
                    self.temp_tab.append(self.tables[t])
                    break
            if not full:
                self.que.put(my_guests[g])
                print(f'{my_guests[g].name} в очереди')

    def discuss_guests(self):
        while not self.que.empty() or len(self.temp_tab) > 0:
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f"{t.guest.name} покушал(-а) и ушёл(ушла) |\n ---Стол номер {t.number} свободен---")
                    t.guest.join()
                    self.temp_tab.remove(t)
                    t.guest = None
                    if not self.que.empty():
                        t.guest = self.que.get()
                        t.guest.start()
                        self.temp_tab.append(t)
                        print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
