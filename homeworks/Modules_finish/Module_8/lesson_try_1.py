# try:
#     num = a + b
#     num = 1 / 0
#     print('done')
# except ZeroDivisionError:
#     print('no!!!')
# except NameError as noname:
#     print(f'what? {noname}')
# else:
#     print('Все прошло успешно!')
# finally:
#     print('Не так все страшно, да?')
#
# try:
#     file = open('nn.txt')
# except OSError as exc:
#     print(f'что-то будет... {exc}, ----{exc.args}----')

try:
    i = int(input('Введи число плиз'))
    num = 10 / i
except ZeroDivisionError as exc:
    print(f'no no no мистер фиш {exc}')
else:
    print('Ура, мы не делим на ноль')
finally:
    print('закончили упражнение')
