def add_everything_up(a, b):
    try:
        num = round(a + b, 3)
    except TypeError as exc:
        num = str(a) + str(b)
    return num


print(add_everything_up('а вот вам C', 'трока'))  # тоже в except попадет с ошибкой TypeError
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
