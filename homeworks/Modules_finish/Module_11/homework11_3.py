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
    d = []
    at = []
    inf['type'] = obj.__class__.__name__  # тип объекта
    inf['module'] = obj.__class__.__module__  # из какого модуля
    for i in dir(obj):
        if callable(getattr(obj, i)):
            d.append(i)
        else:
            at.append(i)
    inf['methods'] = d  # методы объекта
    inf['callable'] = callable(obj)  # можем ли вызвать объект

    inf['attributes'] = at  # атрибуты

    try:
        inf['name'] = obj.__name__  # если есть имя
    except AttributeError:
        inf['name'] = None

    return inf


car1 = Car('Toyota')

pprint(introspection_info(car1))
# pprint(introspection_info(Car))
# pprint(introspection_info(add))
# pprint(introspection_info(34))
