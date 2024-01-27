# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

# lst = [1, 1, 2, 2, 3, 3]
lst = [1, 1, 1, 1, 1]


def unique_elem(data):
    result = list(set([item for item in data if data.count(item) > 1]))
    return result


print(unique_elem(lst))
