from threading import Thread
from datetime import datetime
import requests

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []
start = datetime.now()


def func(url):
    response = requests.get(url)
    page_res = response.json()
    res.append(page_res)


first = Thread(target=func, args=(THE_URL, ))
second = Thread(target=func, args=(THE_URL, ))
third = Thread(target=func, args=(THE_URL, ))

first.start()
second.start()
third.start()

first.join()
second.join()
third.join()

end = datetime.now()
time = end - start
print(res)
print(time)
