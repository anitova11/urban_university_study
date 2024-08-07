from time import sleep, time
from threading import Thread


def wite_words(word_count, file_name):

    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start1 = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end1 = time()
print(f'затрачено времени {end1 - start1}')

start2 = time()
first = Thread(target=wite_words, args=(10, 'example10.txt'))
second = Thread(target=wite_words, args=(30, 'example20.txt'))
third = Thread(target=wite_words, args=(200, 'example30.txt'))
fourth = Thread(target=wite_words, args=(100, 'example40.txt'))

first.start()
second.start()
third.start()
fourth.start()

first.join()
second.join()
third.join()
fourth.join()

end2 = time()
print(f'затрачено времени {end2 - start2}')
