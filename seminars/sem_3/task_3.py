my_tuple = 123, -45, 'apple', True, False, 132.14, 773.3


def type_dict(data: tuple) -> dict:
    res = dict()
    for item in data:
        if str(type(item)).split("'")[1] not in res.keys():
            res[str(type(item)).split("'")[1]] = [item]
        else:
            res[str(type(item)).split("'")[1]].append(item)
    return res


print(type_dict(my_tuple))
