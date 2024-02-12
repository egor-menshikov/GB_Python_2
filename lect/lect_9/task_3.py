import time
from typing import Callable


def dec_1(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('dec1')
        result = func(*args, **kwargs)
        return result

    print('A')
    return wrapper


def dec_2(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('dec2')
        result = func(*args, **kwargs)
        return result

    print('B')
    return wrapper


@dec_1
@dec_2
def x(a, b):
    return a + b


print(x(2, 3))
