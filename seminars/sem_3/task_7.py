# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


from timeit import timeit

text = ("It is a long established fact that a reader will be distracted by the readable content of a page when"
        " looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution"
        " of letters, as opposed to using 'Content here, content here', making it look like readable English."
        " Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text,"
        " and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions"
        " have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")


def char_count(data):
    letters = [item.lower() for item in data if item.isalpha()]
    chars = sorted(set(letters))
    result = {}
    for char in chars:
        count = 0
        for item in letters:
            if char == item:
                count += 1
        result[char] = count
    return result


def char_count_2(data):
    letters = [item.lower() for item in data if item.isalpha()]
    chars = sorted(set(letters))
    return {char: letters.count(char) for char in chars}


print(char_count(text).items())
print(char_count_2(text).items())

print(timeit('char_count(text).items()', globals=globals(), number=10000))
print(timeit('char_count_2(text).items()', globals=globals(), number=10000))
