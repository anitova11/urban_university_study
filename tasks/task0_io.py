#Задача 1 «Длина слова».
num_str = str(input('Введите число: '))
print(len(num_str))

# Задача 2 «Суммы и разности».
num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
summ = str(num1 + num2)
diff = str(num1 - num2)
print(f'Сумма чисел: {summ}\nРазность чисел: {diff}')

# Задача 3 «Среднее арифметическое».
num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
num3 = int(input('Введите третье целое число: '))
avg = str((num1 + num2 + num3) / 3)
print(avg)

#Задача 4 «Простые строчки».
mon = 'Понедельник'
tues = 'Вторник'
print(f'{mon}, {tues}')

# Задача 5 «Сложная формула».
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))
f = (((a * b) + (a * c)) ** 3) / 2
print(f)
