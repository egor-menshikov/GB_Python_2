# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с
# суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним, только если треугольник существует.

a = 4
b = 4
c = 4


def triangle_check(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('Треугольник не существует')
    elif a != b and a != c and b != c:
        print('Треугольник существует')
        print('Треугольник разносторонний')
    elif a == b == c:
        print('Треугольник существует')
        print('Треугольник равносторонний')
    else:
        print('Треугольник существует')
        print('Треугольник равнобедренный')


triangle_check(a, b, c)
