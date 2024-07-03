# создание singleton. можно создать только один экземпляр класса.
class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('hi')
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)


other = [1, 2, 3]
user_data = {'name': 'Kseniya', 'age': 24, 'gender': 'female'}
user1 = User(*other, **user_data)
print(user1.gender)
