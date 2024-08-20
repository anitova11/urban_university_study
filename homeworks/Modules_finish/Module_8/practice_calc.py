def calc(line):
    first_num, operation, second_num = line.split()
    first_num = int(first_num)
    second_num = int(second_num)
    if operation == '+':
        print(f'result = {first_num + second_num}')
    if operation == '-':
        print(f'result = {first_num - second_num}')
    if operation == '/':
        print(f'result = {first_num / second_num}')
    if operation == '//':
        print(f'result = {first_num // second_num}')
    if operation == '*':
        print(f'result = {first_num * second_num}')
    if operation == '%':
        print(f'result = {first_num % second_num}')


cnt = 0

with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            print(f'error {exc} on line {cnt}')

