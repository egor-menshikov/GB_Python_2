# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

data = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    extension = file_path[file_path.rfind('.'):]
    full_path = file_path[: file_path.rfind('.')]
    path = full_path[: full_path.rfind('/') + 1]
    filename = full_path[full_path.rfind('/') + 1:]
    return path, filename, extension


print(get_file_info(file_path='c:/users/r3.txt'))
