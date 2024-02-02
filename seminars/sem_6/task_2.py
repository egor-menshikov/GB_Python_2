"""
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""

from random import randint

_START = 0
_END = 10
_ATTEMPTS = 3


def guess_num(start: int = _START, end: int = _END, attempts: int = _ATTEMPTS) -> bool:
    number = randint(start, end)
    for _ in range(attempts):
        guess = int(input('Введите число: '))
        if guess == number:
            return True
        elif guess < number:
            print('Больше')
        else:
            print('Меньше')
    return False


if __name__ == '__main__':
    print(guess_num())
