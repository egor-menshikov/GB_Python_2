from pathlib import Path

text = 'They Know What Is What But They Don\'t Know What Is What They Just Strut\n'
text2 = ['They Know What Is What',
         'But They Don\'t Know What Is What',
         'They Just Strut']

with open(Path('files/task_5'), 'w', encoding='utf-8') as file:
    res = file.write(text)
    print(f'{res = }\n{len(text) = }')
    file.write('\n')
print()

with open(Path('files/task_5'), 'a', encoding='utf-8') as file:
    for line in text2:
        res = file.write(line + '\n')
        print(f'{res = }\n{len(line) = }')
    file.write('\n')
print()

with open(Path('files/task_5'), 'a', encoding='utf-8') as file:
    file.writelines('\n'.join(text2))
    file.write('\n' * 2)

with open(Path('files/task_5'), 'a', encoding='utf-8') as file:
    for line in text2:
        print(line, file=file)
    file.write('\n')
