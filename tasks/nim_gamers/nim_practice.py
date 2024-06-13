from tasks.nim_gamers.nim_game import put_stones, take_from_bunch, get_bunches, is_over

put_stones()
user_number = 1

while True:
    print("Текущая позиция")
    print(get_bunches())
    print(f'Ход игрока {user_number}')
    pos = int(input('Откуда берем?'))
    count = int(input('Сколько берем?'))
    while True:
        if take_from_bunch(pos, count) != 'again':
            break
        print('Попробуем еще раз')
        pos = int(input('Откуда берем?'))
        count = int(input('Сколько берем?'))
    if is_over():
        break
    user_number = 2 if user_number == 1 else 1
print(f'Выиграл игрок {user_number}')
