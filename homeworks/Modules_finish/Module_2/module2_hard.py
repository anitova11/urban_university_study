import random


def password(num):
    result = ''
    for i in range(1, num):
        for j in range(i, num):
            if (num % (i + j) == 0) & (i != j):
                result += str(i) + str(j)
    return result


number = random.randint(3, 20)
password(number)
print(number, '-', password(number))
