def adder(numbers):
    summer = 0
    for i in numbers:
        summer += i
    return summer


def multiplier(numbers):
    mul = 1
    for i in numbers:
        mul *= i
    return mul


# функция высшего порядка (принимает в кач-ве аргумента др. функции)
def func_number(numbers, func):
    result = func(numbers)
    print(f'result = {result}')


numbs = [2, 3, 4, 6, 7, 8, 10]

func_number(numbs, adder)
func_number(numbs, multiplier)


def mul_num(number):
    return number * 2


result_map = map(mul_num, numbs)  # умножили все числа в листе на 2 функцией mul_num
print(list(result_map))  # функция map возвращает ссылку на объект. ленивые вычисления, поэтому применяем list


def is_bigger(number):
    return number > 5


result_big = filter(is_bigger, numbs)  # оставит в листе числа, которые больше 5 (функция is_bigger)
print(list(result_big))

a, b, c = map(int, input())
print(a)
