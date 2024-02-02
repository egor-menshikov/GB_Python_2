"""
� Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""
dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
       "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}


def riddle(question: str, answers: list, attempts: int) -> int:
    tries = 0
    print(question)
    while attempts:
        variant = input('Enter answer:\n')
        if variant in answers:
            tries += 1
            print('угадали')
            return tries
        else:
            tries += 1
            print('try again')
            attempts -= 1
    return -1


def riddle_storage(data):
    for k, v in data.items():
        riddle(k, v, 3)


# print(riddle("Не лает, не кусает, в дом не пускает",
#              ['замок', 'охранник', 'собака'], 3))

riddle_storage(dct)
