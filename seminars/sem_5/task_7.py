# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если д

# def prime_nums(n: int) -> int:
#     if n == 2:
#         yield n
#     for i in range(3, n // 2 + 1):
#         if n % i == 0:
#             continue
#         yield n
#
#
# for i in range(2, 101):
#     print(next(prime_nums(i)))

# def prime_nums(n: int):

def num_prime(num):  # реализуем функцию проверки числа на простоту
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def my_gen(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if num_prime(num):
            count += 1
            yield num


print(*my_gen(25))
