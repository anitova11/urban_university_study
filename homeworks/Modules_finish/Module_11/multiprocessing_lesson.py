import datetime
import multiprocessing
import pprint

from PIL import Image


def resize_img(img_path):
    image = Image.open(img_path)
    image = image.resize((600, 600))
    image.save(img_path)


# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         all_images = []
#         for i in range(101):
#             all_images.append(f'./images/image — копия ({i}).jpg')
#         start = datetime.datetime.now()
#         pool.map(resize_img, all_images)
#     end = datetime.datetime.now()
#     print(end-start)

# all_images = []
# for i in range(101):
#     all_images.append(f'./images/image — копия ({i}).jpg')
# pprint.pprint(all_images)

start = datetime.datetime.now()
for i in range(101):
    imge_path = f'./images/image — копия ({i}).jpg'
    resize_img(imge_path)
end = datetime.datetime.now()
print(end-start)
