"""Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json
from task_3 import LevelError, AccessError
from task_4 import User


class Login:
    def __init__(self, filepath):
        self.filepath = filepath

    @staticmethod
    def read_users(filepath) -> set:
        res = set()
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for access_lvl, entry in data.items():
            for uid, name in entry.items():
                res.add(User(access_lvl, uid, name))
        return res

    def __call__(self, *args, **kwargs):
        access_lvl = input('Введите уровень доступа:\n')
        uid = input('Введите id:\n')
        name = input('Введите имя:\n')
        sample = User(access_lvl, uid, name)
        users = self.read_users(self.filepath)
        for user in users:
            if sample == user:
                if sample.access_lvl > user.access_lvl:
                    raise LevelError(sample, user)
                else:
                    return f'У пользователя {user.name} уровень доступа {user.access_lvl}'
        raise AccessError(sample)


login = Login('users.json')
print(login())
