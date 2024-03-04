"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""


def func(text):
    """
    >>> func('hello world')
    'hello world'
    >>> func('HELlO wOrLd')
    'hello world'
    >>> func('hello, wo,r!ld')
    'hello world'
    >>> func('hELlыo, wo,r!ацацld')
    'hello world'
    """
    return ''.join([item for item in text if
                    65 <= ord(item) <= 90
                    or 97 <= ord(item) <= 122
                    or item.isspace()]).lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
