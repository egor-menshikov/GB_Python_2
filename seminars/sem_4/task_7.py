# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

data = {"company_1": [70, 12, 25, -28, 10, 36],
        "company_2": [-55, 10, -20, -10, -15, -15],
        "company_3": [40, 12, 21, -70, 11, 65]}


def profits(companies: dict[str: list[int]]) -> bool:
    for item in companies:
        print(sum(companies[item]))
    # return all(map(lambda x: sum(x) >= 0, companies.values()))
    return all([sum(item) >= 0 for item in companies.values()])


print(profits(data))
