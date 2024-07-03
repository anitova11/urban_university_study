class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, login, password):
        self.data[login] = password


class User:
    """
    hi
    """
    def __init__(self, login, password, password_confirm):
        self.login = login
        if password == password_confirm:
            self.password = password


database = Database()
while True:
    choise = input('Привет! Выбери дейтсвие:\n1. Войти\n2. Зарегистрироваться\n')
    if choise == '2':
        user = User(input('Введите логин: '), password := input('Введите пароль: '),
                                              password2 := input('Повторите пароль: '))
        if password2 != password:
            print('пароли не совпадают, давай по новой')
            continue
        database.add_user(user.login, user.password)
    if choise == '1':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if login in database.data:
            if password == database.data[login] \
                    and password == '0':
                print('go')
                break
            else:
                print('неверный пароль')
        else:
            print('пользователь не найден')
        print(database.data)
