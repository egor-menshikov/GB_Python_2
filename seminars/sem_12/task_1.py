"""Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""
from math import factorial


class Facto:
    def __init__(self, k):
        self.storage = {}
        self.k = k

    def __str__(self):
        return ', '.join(f'{k}:{v}' for k, v in sorted(self.storage.items()))

    def __call__(self, value):
        for _ in range(self.k):
            self.storage[value] = factorial(value)
            value -= 1


if __name__ == '__main__':
    a = Facto(4)
    a(10)
    print(a)
