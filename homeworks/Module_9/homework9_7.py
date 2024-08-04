def is_prime(func):
    def temp(a, b, c):
        result = func(a, b, c)
        counter = 1
        for i in range(2, result):
            if result % i == 0:
                counter += 1
        if counter > 1:
            return 'not prime ' + str(result)
        else:
            return 'prime ' + str(result)
    return temp


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(1, 1, 5))
