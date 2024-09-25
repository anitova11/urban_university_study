import requests
import queue
from threading import Thread

# ACCESS_TOKEN =
ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'


class GetGenre(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = requests.get(RANDOM_GENRE_API_URL).json()
        self.queue.put(genre)


class Genius(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = self.queue.get()
        data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
        data = data.json()
        try:
            song_id = data['response']['hits'][0]['result']['api_path']
            print(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError:
            pass


queue = queue.Queue()
# genre_thread = GetGenre(queue)
# genius_thread = Genius(queue)

genre_list = []
genius_list = []

for i in range(10):
    t = GetGenre(queue)
    t.start()
    genre_list.append(t)

for i in range(10):
    t = Genius(queue)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()
