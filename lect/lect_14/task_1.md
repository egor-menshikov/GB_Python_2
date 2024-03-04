ЛЯЛЯЛЛЯЛЯЛЯ
---
УРУРУРУРУРУРРУ
===

    >>> from task_1 import is_prime

НУ ТАКОЕ СЕБЕ

    >>> is_prime(42)
    False

    >>> is_prime(73)
    True

    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
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