calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(strings):
    tuples = (len(strings), strings.upper(), strings.lower())
    count_calls()
    return tuples


def is_contains(my_string, my_list):
    count_calls()
    boo = False
    for i in my_list:
        if my_string.upper() in i.upper():
            boo = True
    return boo


print(string_info('Kitty'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
