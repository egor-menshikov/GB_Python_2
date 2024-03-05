"""
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
"""

import logging

PATH = 'history.log'
ENTRY = '{levelname:<8} | {asctime} | {msg}'


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        msg = f'{func.__name__}() | args: {args} | result: {result}'
        logging.basicConfig(level=logging.NOTSET, filename=PATH, filemode='a', format=ENTRY, style='{')
        logger = logging.getLogger(__name__)
        logger.info(msg)
        return result

    return wrapper


@log
def function(a, b):
    return a + b


function(5, 3)
