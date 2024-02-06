import pathlib

with open(pathlib.Path('files/task_3.data'), 'a+', encoding='utf-8') as file:
    file.write('Hello\nWorld\nHow\'s life?\n')
