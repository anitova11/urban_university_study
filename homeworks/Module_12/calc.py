import logging


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        d = a / b
        logging.info(f'Успешное деление {a} / {b}')
        return d
    except ZeroDivisionError as e:
        logging.error('Error division', exc_info=True)
        return -1


if __name__ == '__main__':
    print(add(2, 3))
    logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                        format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8')
    print(div(3, 4))
    print(div(3, 0))
