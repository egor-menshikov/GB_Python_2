import pathlib

SIZE = 8
# with open(pathlib.Path('files/task_3.data'), 'r', encoding='utf-8') as file:
#     data = []
#
#     for item in file:
#         data.append(item)
#
# print(data)

with open(pathlib.Path('files/task_3.data'), 'r', encoding='utf-8') as file:
    while res := file.read(SIZE):
        print(res)

with open(pathlib.Path('files/task_3.data'), 'r', encoding='utf-8') as file:
    a = file.readline()
    b = file.readline()
print(a)
print(b)
