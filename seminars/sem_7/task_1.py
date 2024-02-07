"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.

"""
from pathlib import Path
import random

filepath = Path.cwd() / 'task_123' / 'pairs'


def num_pairs(lines: int, filename: Path):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.writelines([f'{random.randint(-1000, 1000)}|{random.uniform(-1000, 1000)}\n'
                         for _ in range(lines)])


num_pairs(10, filepath)
