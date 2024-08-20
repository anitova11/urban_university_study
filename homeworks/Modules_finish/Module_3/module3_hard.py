def func(*args):
    global counter # использовала глобальную переменную, чтобы при повторном вызове фун. значение не занулилось.
    for i in args:
        if isinstance(i, int):  # проверяем тип элемента int
            counter += i
        elif isinstance(i, str):  # проверяем тип str
            counter += len(i)
        elif isinstance(i, dict):  # проверяем тип dict, если является, то отдельно смотрим
            for key, value in i.items():  # ключ и значение.
                if isinstance(key, int):
                    counter += key
                elif isinstance(key, str):
                    counter += len(key)
                else:
                    func(*key)  # если ключ не int/str, то вызываем фун-ию заново
                if isinstance(value, int):
                    counter += value
                elif isinstance(value, str):
                    counter += len(value)
                else:
                    func(*value)  # если значение не int/str, то вызываем фун-ию заново
        else:
            func(*i)  # если не int, не str, не dict, то вызываем заново
    return counter


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

another_data_structure = [
    [1, 2, 3],
    {(1, 2): 4, 'b': [4, 'ab', (1, 3)]},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

counter = 0
print(func(data_structure))
counter = 0   # специально занулила значение, чтобы рассчет заново пошел
print(func(another_data_structure))


