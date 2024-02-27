"""Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class BasicErrorGroup(Exception):
    pass


class LevelError(BasicErrorGroup):
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    def __str__(self):
        return f'Уровень доступа {self.user1} выше чем {self.user2}'


class AccessError(BasicErrorGroup):
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f'В списке не найдено пользователя {self.user}'
