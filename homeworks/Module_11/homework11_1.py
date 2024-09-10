import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()


files = []
for i in range(4):
    files.append(f'./numbers/file {i + 1}.txt')

# start = datetime.datetime.now()
# for i in range(1, 5):
#     read_info(f'./numbers/file_{i}.txt')
# end = datetime.datetime.now()
# print(end - start)

# 0:00:05.360205


if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, files)
    end = datetime.datetime.now()
    print(end - start)

# 0:00:02.273405
