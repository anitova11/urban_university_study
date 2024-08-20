my_dict = {'Kseniya': 2000, 'Nikolay': 1999, 'Julya': 2022}
print(my_dict)
print(my_dict['Kseniya'])                               # существующий ключ
print(my_dict.get('Marina', 'Такого ключа не найдено')) # несуществующий ключ
my_dict['Marina'] = 1976                                # добавление нового элемента путем обращения по ключу
my_dict.update({'Melaniya': 2023})                      # добавление нового элемента через метод
del_key = my_dict.pop('Melaniya')                       # удаление элемента
print(del_key)
print(my_dict)

my_set = {1, True, False, 0, 'abc', -48, 0.23, 'Man', 'abc'}
print(my_set)
my_set.update('ki')                                     # добавление двух элементов через метод update
my_set.add(6)                                           # добавление числа через add
print(my_set)
a = my_set.pop()                                        # удаляет случайный элемент множества
my_set.remove('k')                                      # удаляет указанный элемент множества
print(my_set)
