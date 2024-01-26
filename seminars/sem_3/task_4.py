my_list = [1, 1, 3, 3, 3, 2, 5, 5, 4, 7, 7, 7]


def del_pairs(data: list) -> list:
    return [item for item in data if data.count(item) != 2]


print(del_pairs(my_list))
