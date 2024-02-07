"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

"""
from pathlib import Path
import os

from task_4 import create_files

options = [('ext', 3), ('xt', 2)]


def advanced_create_files(path: Path, *args: tuple):
    if not os.path.exists(path):
        Path(path).mkdir(parents=True)
    for extension, count in args:
        create_files(extension=extension, count=count, path=path)


if __name__ == '__main__':
    advanced_create_files(Path('task_4', 'test'), *options)
