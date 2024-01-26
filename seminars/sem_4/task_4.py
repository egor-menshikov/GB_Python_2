# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

from timeit import timeit
my_list: list = [1, 6, 0, 9, 4, 5, 3, 15, 4]


def func_sort(data: list) -> list:
    flag = True
    while flag:
        flag = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                flag = True
    return data


print(func_sort(my_list[:]))
print(my_list)
print(timeit('func_sort(my_list[:])', globals=globals()))