def func(a, b):
    try:
        result = a + b
    except TypeError as e:
        print(f'owibka {e}')
    else:
        print('finally')
        return -1


print(func(2, 'b'))
