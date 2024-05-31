# 1 способ собственного написания
def getm(n):
    n = int(str(n).replace('0', ''))
    if n < 10:
        return n
    else:
        return n % 10 * getm(n // 10)


print(getm(402040))


# 2 способ из методички
def get_multiplied_digits(n):
    if n % 10 == 0:
        n += 1
    str_n = str(n)
    first = int(str_n[0])
    if len(str_n) == 1:
        return int(str_n)
    else:
        return first * get_multiplied_digits(int(str_n[1:]))


print(get_multiplied_digits(2042))
