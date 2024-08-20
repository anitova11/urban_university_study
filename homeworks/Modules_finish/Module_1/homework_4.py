immutable_var = 1, True, 'a'
print(immutable_var)
#immutable_var[1] = 2  //Кортеж - неизменяемый тип данных, не получится изменить

mutable_list = [1, 'd', 5.6]
print(mutable_list)
mutable_list.extend([True, False])
mutable_list[3] = mutable_list[2]
print(mutable_list)
