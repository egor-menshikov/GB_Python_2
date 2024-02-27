"""Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""

my_dict = {'a': 'one'}


def get(data: dict, key, default=None):
    try:
        return data[key]
    except KeyError:
        return default


print(get(my_dict, 'a', 2))
