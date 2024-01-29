def func_fact(n: int):
    if n == 1 or n == 0:
        return 1
    return n * func_fact(n - 1)


print(func_fact(10))
