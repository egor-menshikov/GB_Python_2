"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

"""
from pathlib import Path
import random
import string
import os

_PATH = Path.cwd() / 'task_4'


def filename_gen(length_min: int, length_max: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(random.randint(length_min, length_max)))


def create_files(extension: str,
                 name_min: int = 6,
                 name_max: int = 30,
                 bytes_min: int = 256,
                 bytes_max: int = 4096,
                 count: int = 42,
                 path: Path = _PATH):
    file_names = []
    while count:
        file_name = '.'.join((filename_gen(name_min, name_max), extension))
        if file_name not in file_names:
            file_names.append(file_name)
            count -= 1

    for item in file_names:
        if not os.path.isfile(Path(path, item)):
            with open(Path(path, item), mode='bw') as file:
                file.write(random.randbytes(random.randint(bytes_min, bytes_max)))


if __name__ == '__main__':
    create_files('txt', 4, 6, 256, 512, 5)
