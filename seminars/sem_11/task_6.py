"""Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

from math import sqrt


class Rectangle:
    def __init__(self, *args):
        self._length = args[0]
        self._width = self._length if len(args) == 1 else args[1]

    @property
    def area(self):
        return self._length * self._width

    @property
    def perimeter(self):
        return 2 * (self._length + self._width)

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def __add__(self, other):
        return Rectangle(sqrt(self.perimeter + other.perimeter))

    def __sub__(self, other):
        return Rectangle(sqrt(abs(self.perimeter - other.perimeter)))

    def __str__(self):
        return f'{self.length:.3f}, {self.width:.3f}'

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


a = Rectangle(2, 3)
b = Rectangle(3, 1)
print(a >= b)
