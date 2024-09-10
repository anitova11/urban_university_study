from inspect import getmodule
from pprint import pprint


class Car:
    wheels = 4

    def __init__(self, name):
        self.name = name
        self.go = False
        self.petrol = 0

    def go(self):
        self.go = True

    def refuelling(self, fuel):
        self.petrol += fuel


def add(x):
    x += 2
    return x


def introspection_info(obj):
    inf = {}
    inf['type'] = str(type(obj)).split()[1]                     # тип объекта
    inf['module'] = getmodule(obj)                              # из какого модуля
    inf['methods'] = dir(obj)                                   # методы объекта
    inf['callable'] = callable(obj)                             # можем ли вызвать объект

    try:
        inf['attributes'] = obj.__dict__                        # если есть атрибуты
    except AttributeError:
        inf['attributes'] = 'Object has no attributes'

    try:
        inf['name'] = obj.__name__                              # если есть имя
    except AttributeError:
        inf['name'] = None

    return inf


car1 = Car('Toyota')

pprint(introspection_info(car1))
# pprint(introspection_info(Car))
# pprint(introspection_info(add))
# pprint(introspection_info(34))
