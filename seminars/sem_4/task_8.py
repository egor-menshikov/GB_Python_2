"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

var = globals().copy()
print(var)
var_new = {}

for k in var:
    if not k.startswith('__'):
        if k.endswith('s') and len(k) > 1:
            var_new[k[:-1]] = var[k]
            var[k] = None

for k in var_new:
    var[k] = var_new[k]
print(var)
for k in var:
    globals()[k] = var[k]

print(globals())
