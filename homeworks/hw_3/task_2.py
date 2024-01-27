# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
# считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.

_text = 'Hello world. Hello Python. Hello again.'


def word_count(data: str) -> list[tuple[str, int]]:
    counts = {}
    text = ''
    result = []

    for item in data:
        if item.isalpha():
            text += item
        else:
            text += ' '
    text = text.lower().split()

    for item in text:
        if not counts.get(text.count(item)):
            counts[text.count(item)] = [item]
        elif item not in counts[text.count(item)]:
            counts[text.count(item)].append(item)

    for k in sorted(counts.keys(), reverse=True):
        for item in sorted(counts[k], reverse=True):
            result.append((item, k))

    return result


print(word_count(_text))
