import pathlib


file = open(pathlib.Path('files/text.data'), mode='r+', encoding='utf-8')
print(file)
print(*file)
file.close()

file = open(pathlib.Path('files/text.data'), mode='x', encoding='utf-8')
file.close()
