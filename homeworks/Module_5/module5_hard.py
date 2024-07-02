from time import sleep


class User:
    data = {}

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    video_rep = {}

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.video_rep[title] = [duration, time_now, adult_mode]

    def __str__(self):
        return self.title


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, login, password):
        if login in User.data:
            if hash(password) == User.data[login]:
                self.current_user = login

    def register(self, nickname, password, age):
        if nickname in User.data:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            User.data[nickname] = [password, age]
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i.title.casefold() not in self.videos:
                self.videos.append(i.title.casefold())

    def get_videos(self, search):
        result = []
        for i in self.videos:
            if search.lower() in i.lower():
                result.append(i)
        return result

    def watch_video(self, film):
        if film.casefold() not in self.videos:
            print('', end='')
        else:
            if self.current_user is None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            else:
                if (User.data[self.current_user][1] >= 18 and Video.video_rep[film][2]):
                    duration = Video.video_rep[film][0]
                    for i in range(duration):
                        print(i + 1, end=' ')
                        sleep(1)
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')