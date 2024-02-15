"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:
    def __init__(self, name: str, surname: str, age: int):
        self._name = name
        self._surname = surname
        self._age = age

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return self._name + ' ' + self._surname
