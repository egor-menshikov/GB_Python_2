"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""


def func(text):
    return ''.join([item for item in text if
                    65 <= ord(item) <= 90
                    or 97 <= ord(item) <= 122
                    or item.isspace()]).lower()
