my_list = [1, 1, 3, 3, 3, 2, 5, 5, 4, 7, 7, 7]


def odd_list(data: list) -> list:
    return [k for k, v in enumerate(data, 1) if v % 2 != 0]

print(my_list)
print(odd_list(my_list))