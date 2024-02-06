from pathlib import Path

with open(Path('files/task_5'), 'r', encoding='utf-8') as file:
    print(file.tell())
    file.seek(5)
    print(file.tell())

# Удаляем построчно с конца
last = before = 0
with open(Path('files/task_5'), 'r+', encoding='utf-8') as file:
    while file.readline():
        last, before = file.tell(), last
    file.seek(before, 0)
    file.truncate()

