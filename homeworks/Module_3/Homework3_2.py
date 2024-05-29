def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(2, c='hello')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1.5, True, '234']
values_dict = {'a': 2, 'b': 'str', 'c': 4.5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [52, 'gars']
print_params(*values_list_2, 42)
