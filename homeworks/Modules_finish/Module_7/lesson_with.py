import string

# name = 'file_name.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         line1 = line
#         for char in line:
#             if char in string.punctuation:
#                 line1.replace(char, '')
#         print(line1)


line = 'ghdj+flfg_ k,d'
str_punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
for i in str_punct:
    line = line.replace(i, '')
print(line)


# Используйте кодировку utf-8.
# Because there are 2 languages!
# Спасибо!