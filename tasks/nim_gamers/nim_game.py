from random import randint
_holder = []


def put_stones():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))


def take_from_bunch(position, count):
    if 1 <= position <= len(_holder):
        if count == '' or int(count) > _holder[position - 1] or int(count) < 1:
            return 'again'
        else:
            _holder[position - 1] -= count
    else:
        return 'again'


def get_bunches():
    return _holder


def is_over():
    return sum(_holder) == 0

