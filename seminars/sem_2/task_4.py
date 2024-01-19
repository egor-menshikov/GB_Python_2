# A=πr2
#
# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import decimal
# from math import pi
#
# decimal.getcontext().prec = 42
#
#
# def area(d):
#     return decimal.Decimal((pi) * (d / 2) ** 2)
#
# print(area(734.93741840948109))
#

import math
import decimal


def area(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * (d / 2) ** 2


def len_circle(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * d
