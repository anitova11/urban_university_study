import requests
from datetime import datetime

start = datetime.now()
THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []

for i in range(3):
    response = requests.get(THE_URL)
    page_res = response.json()
    res.append(page_res)

end = datetime.now()
time = end - start
print(res)
print(time)


