import os

print('текущая директория', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('текущая директория', os.getcwd())
# os.makedirs(r'third\fourth')
print(os.listdir())
for i in os.walk('.'):
    print(i)

os.chdir(r'C:\Users\bfi18\PycharmProjects\start_project\homeworks\Module_7')
print('текущая директория', os.getcwd())

file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(file, dirs, sep='\n')
os.startfile(file[0])
print(os.stat(file[0]))
os.system('pip install arcade')
