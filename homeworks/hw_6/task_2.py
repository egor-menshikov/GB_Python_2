# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет все
# возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг
# друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
import random


def is_attacking(q1, q2):
    attacked = []
    for i in range(1, 9):
        for j in range(1, 9):
            if (i == q1[0] or
                    j == q1[1] or
                    abs(i - q1[0]) == abs(j - q1[1])):
                attacked.append((i, j))
    if q2 in attacked:
        return True
    return False


def check_queens(queens):
    for item in queens:
        for other in queens:
            if item != other:
                if is_attacking(item, other):
                    return False
    return True


def generate_boards():
    board_list = []
    while len(board_list) < 4:
        candidate = [(1, random.randint(1, 8))]
        while len(candidate) != 8:
            for i in range(len(candidate) + 1, 9):
                candidate.append((i, random.randint(1, 8)))
                if not check_queens(candidate):
                    break
        board_list.append(candidate)
    return board_list


print(*generate_boards(), sep='\n')
