# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

my_friends = {'vasya': ('flashlight', 'food', 'fleshlight'),
              'misha': ('flashlight', 'axe'),
              'olya': ('flashlight', 'food')}


def sets(data: dict):
    friends = data.keys()

    working_set = set()
    for key in data:
        if working_set:
            working_set &= set(data[key])
        else:
            working_set = set(data[key])
    print('У всех друзей есть следующие вещи:')
    for item in working_set:
        print(item, '\n')
    print()

    for friend in friends:
        working_set = set(data[friend])
        for other_friend in [i for i in friends if i != friend]:
            working_set -= set(data[other_friend])
        if working_set:
            print(f'Уникальные вещи у {friend}:')
            for item in working_set:
                print(item, )
    print()

    for friend in friends:
        working_set = set()
        to_remove = set(data[friend])
        for other_friend in [i for i in friends if i != friend]:
            if working_set:
                working_set &= set(data[other_friend])
                working_set -= to_remove
            else:
                working_set = set(data[other_friend])
        if working_set:
            print(f'{friend} не взял \t {working_set}')


sets(my_friends)
