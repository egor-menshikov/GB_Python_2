from memory_profiler import profile
from random import randint


@profile
def outer(n):
    arr = [randint(0, 100) for _ in range(300000)]
    return fibo(n)


def fibo(n):
    if n < 3:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(outer(7))
