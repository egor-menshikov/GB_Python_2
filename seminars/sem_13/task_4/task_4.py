"""Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""

import json


class User:
    def __init__(self, access_lvl, uid, name):
        self.access_lvl = access_lvl
        self.uid = uid
        self.name = name

    def __repr__(self):
        return f'User(uid={self.uid}, name={self.name}, access_lvl={self.access_lvl})'

    def __hash__(self):
        return hash((self.uid, self.name))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


def read_users(filepath) -> set:
    res = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for access_lvl, entry in data.items():
        for uid, name in entry.items():
            res.add(User(access_lvl, uid, name))
    return res

# print(*read_users('users.json'), sep='\n')


