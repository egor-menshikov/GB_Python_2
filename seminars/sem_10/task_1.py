# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


from math import pi


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2

    def length(self):
        return 2 * pi * self.__radius
