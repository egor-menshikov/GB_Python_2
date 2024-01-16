# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n, e = 10, 3
count = 0
answer = 0
while count <= n:
    if count % e:
        answer += count
    count += 2
print(answer)