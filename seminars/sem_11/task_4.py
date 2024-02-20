"""Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    last_num = None
    last_str = None
    str_archives = []
    num_archives = []

    def __init__(self, number, text):
        self.number = number
        self.text = text
        if Archive.last_num is not None:
            Archive.num_archives.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.str_archives.append(Archive.last_str)
        Archive.last_num = number
        Archive.last_str = text

    def __str__(self):
        return str(list(zip(self.str_archives, self.num_archives)))


obj1 = Archive(1, '1')
obj2 = Archive(2, '2')
obj3 = Archive(3, '3')
print(obj3)
