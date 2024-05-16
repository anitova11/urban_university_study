print('Задача1. Подсчет сдачи.')
money = int(input('Введите количество денег '))
print(money - 34*4.5)

print('\nЗадача2. «Сдача всем»')
price = float(input('Какая стоимость за килограмм? '))
weight = float(input('Какой вес товара? '))
money = int(input('Сколько у Вас денег? '))
print('Ваша сдача:', money - weight*price)

print('\nЗадача3. «Работаем с выводом данных»')
name = 'Вишня'
price = float(input('Какая стоимость за килограмм? '))
weight = float(input('Какой вес товара? '))
money = int(input('Сколько у Вас денег? '))
print(f'\nЧек\n{name} - {weight}кг - {price}руб/кг\n'
      f'Итого: {weight*price}руб\nВнесено: {money}руб Сдача: {money-weight*price}руб')

print('\nЗадача4. «Самая простая задача на свете»')
num = int(input('Введите число: '))
string1 = 'Купи конструктор!\n'
print(string1*num)

print('\nЗадача5. «Автоматизируем простоту!»')
num = int(input('Введите число: '))
fav = input('Введите название дела: ')
print(('Обожаю писать "'+fav+'"!\n')*num)


