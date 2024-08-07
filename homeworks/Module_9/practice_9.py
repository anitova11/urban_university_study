# animal = 'мишка'
# animals = ['зайка', 'мишка', 'бегемотик']
#
#
# def gen_repeat(n):
#     def repeat(text):
#         return (text[:2] + '-') * n + text
#
#     return repeat
#
#
# def gen_func_repeat(*args):
#     def repeat(text):
#         for i in args:
#             print((text[:2] + '-') * i + text)
#
#     return repeat
#
#
# a = gen_repeat(2)
# print(a(animal))
# print()
#
# b = gen_func_repeat(1, 2, 3)
# b(animal)
#
# repa = [gen_repeat(n) for n in range(1, 4)]
# result = [repar(animal) for repar in repa]
# print(result)
#
# repa1 = [gen_repeat(n) for n in range(1, 4)]
# result1 = [repar(animal1) for repar in repa for animal1 in animals]
# print(result1)
import time


def decor(func):
    res = {}

    def temp(*args):
        if args not in res:
            res[args] = func(*args)
            return f'опа нью {res[args]}'
        else:
            return f'уже вычислено {res[args]}'

    return temp


@decor
def power(a, b):
    return a ** b


print(power(33, 44))
print(power(35, 53))
print(power(4, 5))
print(power(4, 5))
print(power(44, 5))
print(power(33, 44))
