# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = ('Текст выравнивается по правому краю так чтобы у самого '
        'длинного слова был один пробел между ним и номером строки')


def sort_str(data: str):
    res = sorted(data.split())
    # max_word = max(len(item) for item in res)
    max_word = len(max(res, key=len))
    for k, v in enumerate(res, 1):
        print(f'{k:2}. {v:>{max_word}}')


sort_str(text)