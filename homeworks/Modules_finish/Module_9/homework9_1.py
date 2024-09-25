def apply_all_func(int_list, *functions):
    dict_fun = {}
    for i in functions:
        dict_fun[i.__name__] = i(int_list)
    return dict_fun


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
