"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.

"""
from pathlib import Path

filepath1 = Path.cwd() / 'task_123' / 'pairs'
filepath2 = Path.cwd() / 'task_123' / 'names'
filepath3 = Path.cwd() / 'task_123' / 'results'


def prepare(list1: list, list2: list) -> (list, list):
    if len(list1) > len(list2):
        for i in range(len(list1) - len(list2)):
            list2.append(list2[i])
        return list1, list2
    elif len(list1) < len(list2):
        for i in range(len(list2) - len(list1)):
            list1.append(list1[i])
        return list1, list2
    return list1, list2


def combine(filepath1: Path, filepath2: Path, filepath3: Path):
    with open(filepath1, mode='r', encoding='utf-8') as pairs, \
            open(filepath2, mode='r', encoding='utf-8') as names, \
            open(filepath3, mode='w', encoding='utf-8') as results:
        pairs_list, names_list = prepare(pairs.readlines(), names.readlines())
        for pair, name in zip(pairs_list, names_list):
            product = float(pair.split('|')[0]) * float(pair.split('|')[1])
            if product < 0:
                results.write(f'{name.strip().lower()}|{abs(product)}\n')
            else:
                results.write(f'{name.strip().upper()}|{int(product)}\n')


combine(filepath1, filepath2, filepath3)
