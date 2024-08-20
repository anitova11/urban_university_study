def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    count = 0
    my_dict = {}
    for i in strings:
        count += 1
        bb = file.tell()
        file.write(i + '\n')
        my_dict[(count, bb)] = i
    file.close()
    return my_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('file_name.txt', info)
for elem in result.items():
    print(elem)
