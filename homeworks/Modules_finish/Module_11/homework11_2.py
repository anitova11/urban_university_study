import numpy as np
import matplotlib.pyplot as plt
import requests


while True:
    expression = input(f'\nВыберите библиотеку для демонстрации:\n1- requests\n2- numpy\n3- matplotlib\n4- выход\n-> ')

    match expression:
        case '1':
            print('Добро пожаловать в конвертер валют!')
            quote = input('Из какой валюты переводим? Например, EUR, USD, RUB -> ')
            base = input('В какую переводим? Например, EUR, USD, RUB -> ')
            amount = int(input('Введите количество -> '))
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
            print(r.json()[base] * amount)

        case '2':
            print('Давайте  создадим массив')
            arr = np.array([[2, 4, 6, 8], [1, 3, 5, 7]])
            print(f'Сам массив \n{arr[0: 2]}')
            print(f'Размерность массива - {arr.shape}')
            print(f'Элемент с  индексом 1,2 - {arr[1, 2]}')
            arr1 = arr * np.array([10, 20, 30, 40])
            print(f'Массив, умноженный на новый массив - \n{arr1}')
            arr1 = arr.reshape(4, 2)
            print(f'Поменяли размерность\n {arr1}')
            arr2 = np.ones(5, dtype=np.int64)
            print(f'Единичный массив {arr2}')

        case '3':
            x = np.linspace(0, 2, 100)
            fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
            ax.plot(x, x, label='если я лежу')
            ax.plot(x, x ** 3, label='если занимаюсь питоном')
            ax.set_xlabel('затрата энергии')
            ax.set_ylabel('рост голода')
            ax.set_title('хочу кушац')
            ax.legend()
            plt.show()

        case '4':
            break
