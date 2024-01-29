# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

my_text = 'abcdefg'


def letters_dict(data: str) -> dict[str:int]:
    return {k: ord(k) for k in data}


print(letters_dict(my_text))
