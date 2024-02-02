"""
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""
from sys import argv
from random import randint


_START = 0
_END = 10
_ATTEMPTS = 3


def guess_num(*args) -> bool:
    number = randint(int(args[1]), int(args[2]))
    for _ in range(int(args[3])):
        guess = int(input('Введите число: '))
        if guess == number:
            return True
        elif guess < number:
            print('Больше')
        else:
            print('Меньше')
    return False


if __name__ == '__main__':
    print(guess_num(*argv))