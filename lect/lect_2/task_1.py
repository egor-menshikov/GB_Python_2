# a = 'privet'
# b = 'priv'
# c = 'et'
# d = b + c
# print(d)
# print(a is d)
# print(id(a))
# print(id('privet'))
# print(id(b))
# print(id(c))
# print(id(d))
# print(isinstance(a, str))

# data = 3.14
# print(isinstance(data, (str, complex, bool)))
# a = type(data)
# print(a)
# print(type(data) is a)

# a = 2 + 2.0 * 2
# b = 2 * 3
# print(a)
# print(b)
# print(a == b)
# print(a is b)

# print(hash(-1) is hash(-2))
#
# my_list = [1, 4, 8]
# print(hash(my_list)) не сработает

# a: int = 1
# print(a)
# b: float = float(input('enter a number\n'))
# a = a / b
# print(type(a))

# from typing import Text as t
#
# _data: list[int, float, str] = [1, 3.4, 'car']


# def my_func(data: list[int, float, str]) -> bool:
#     data.append('ghf')
#     return True
#
#
# my_func(_data)
#
# tx = t("dasd")
# print(tx)

# print('hello world'.count('L'.casefold()))

# print(dir('hw'))


# a = int('FFFF', base=16)
# b = int('1010', base=2)
# print(a)
# print(bin(10))
# print(int('hello', base=30))

# import sys
# STEP = 2 ** 16
# num = 1
# for _ in range(60):
#     print(sys.getsizeof(num), num)
#     num *= STEP

# a = 1_2_3_45
# print(a)

# print(0.1 + 0.2)

# default = 3
# num = int(input('input'))
# level = num or default
# print(level)

# data = [1, 4, 5, 2]
#
# while data:
#     print(data.pop())

# a = ''
# print(a.__sizeof__())

# from decimal import Decimal as Dec
# num = Dec(3.21415423532532562643643643341412414134124123413413413413432546436543763735743573753524542)
# print(num)
# num2 = Dec(543252343.00000000000000001 / 34325463211.783071)
# print(num2)

# from decimal import (Decimal as Dec,
#                      getcontext)
#
# getcontext().prec = 160
# num = Dec(0.1) + Dec(0.2)
# print(type(num))
# print(num)

# from fractions import Fraction as Frac
#
# f1 = Frac(1, 3)
# print(f1)
# f2 = Frac(3, 5)
# print(f2)
# print(type(f2))
#
# num = f2 + f1
# print(num)
# print(type(num))

print(divmod(21, 10))
print(type(divmod(21, 10)))

print(round(3.5), 10)

print(pow(2, 3, 7))
