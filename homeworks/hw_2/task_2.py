# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

import fractions

frac1 = '1/2'
frac2 = '1/3'


def sum_product(frac1, frac2):
    fraction_1 = fractions.Fraction(frac1)
    fraction_2 = fractions.Fraction(frac2)
    numerator_1 = int(frac1.split('/')[0])
    numerator_2 = int(frac2.split('/')[0])
    denominator_1 = int(frac1.split('/')[1])
    denominator_2 = int(frac2.split('/')[1])
    lcm = denominator_1 * denominator_2

    sum_manual = str(int(numerator_1 * lcm / denominator_1) + int(numerator_2 * lcm / denominator_2)) + '/' + str(lcm)
    product_manual = str(numerator_1 * numerator_2) + '/' + str(lcm)

    print(f'Сумма дробей: {sum_manual}\n'
          f'Произведение дробей: {product_manual}\n'
          f'Сумма дробей: {fraction_1 + fraction_2}\n'
          f'Произведение дробей: {fraction_1 * fraction_2}')


sum_product(frac1, frac2)
