# import multiprocessing
# from PIL import Image
# from queue import Empty
#
#
# def resize_image(img_path, queue):
#     for image_path in img_path:
#         image = Image.open(image_path)
#         image = image.resize((800, 600))
#         queue.put((image_path, image))
#
#
# def change_color(queue):
#     while True:
#         try:
#             image_path, image = queue.get(timeout=5)
#         except Empty:
#             break
#         image = image.convert('L')
#         image.save(image_path)
#
#
# if __name__ == '__main__':
#     data = []
#     queue = multiprocessing.Queue()
#
#     for i in range(1, 101):
#         data.append(f'./images/racket ({i}).jpg')
#
#     resize_process = multiprocessing.Process(target=resize_image, args=(data, queue))
#     change_process = multiprocessing.Process(target=change_color, args=(queue, ))
#
#     resize_process.start()
#     change_process.start()
#
#     resize_process.join()
#     change_process.join()
#

import multiprocessing
from PIL import Image


def resize_image(img_path, pipe, stop_event):
    for image_path in img_path:
        image = Image.open(image_path)
        image = image.resize((100, 600))
        image.save(image_path)
        pipe.send(image_path)
    stop_event.set()


def change_color(pipe, stop_event):
    while not stop_event.is_set():
        image_path = pipe.recv()
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    conn1, conn2 = multiprocessing.Pipe()
    stop_event = multiprocessing.Event()

    for i in range(1, 101):
        data.append(f'./images/racket ({i}).jpg')

    resize_process = multiprocessing.Process(target=resize_image, args=(data, conn1, stop_event))
    change_process = multiprocessing.Process(target=change_color, args=(conn2, stop_event))

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()
