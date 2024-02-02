"""
Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""


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


print(riddle("Не лает, не кусает, в дом не пускает",
             ['замок', 'охранник', 'собака'], 3))
