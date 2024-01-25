# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = ['Буся', False, 5141.4, -98989]

for number, item in enumerate(data, 1):
    print(f'{number} | {item} | {id(item)} | {sys.getsizeof(item)} | {hash(item)} |'
          f'  | {item.is_integer() if type(item) is int else ""} | {isinstance(item, str) if type(item) is str else ""}')