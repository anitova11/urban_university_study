from sys import set_int_max_str_digits
import time


def decor(func):
    def temp(a):
        return func(a).upper()

    return temp


@decor
def fun(a):
    return 'Hello!' * a



def decor(func):
    def temp(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        times = round(end - start, 4)
        print(times)
        return result

    return temp


@decor
def digits(*args):
    total = 0
    for i in args:
        total += i ** 100000
    return len(str(total))


set_int_max_str_digits(1000000)

res = digits(123, 453, 5788, 5420)
print(res)
print(fun(2))
