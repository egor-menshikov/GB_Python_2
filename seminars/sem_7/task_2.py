"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from pathlib import Path
import string
import random

filepath = Path(Path.cwd() / 'task_123' / 'names')


def pseudoname():
    letters = string.ascii_lowercase
    vowels = 'aeiou'
    length = random.randint(4, 7)
    while True:
        name = ''.join(random.choice(letters) for _ in range(length))
        if any(letter in vowels for letter in name):
            return name.capitalize()


def fill_names(quantity: int, filename: Path):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.writelines([f'{pseudoname()}\n' for _ in range(quantity)])


fill_names(10, filepath)
