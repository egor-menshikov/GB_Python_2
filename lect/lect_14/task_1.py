def is_prime(p: int) -> bool:
    """
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time.
    Working
    ...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time.
    Working
    ...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time.\nWorking\n...')

    for i in range(2, p):
        if p % i == 0:
            return False
    return True

# if __name__ == '__main__':
#     import doctest
#     doctest.testfile('task_1.md', verbose=True)
