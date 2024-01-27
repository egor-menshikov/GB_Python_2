# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
from random import randint

my_list = [randint(1, 10) for i in range(10)]
print(my_list)


def range_sum(data: list[int], start: int, end: int) -> int:
    return sum(data[start + 1:end])
