from random import randint
from collections import deque


def get_rand_values():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class Pool(deque):
    pass
