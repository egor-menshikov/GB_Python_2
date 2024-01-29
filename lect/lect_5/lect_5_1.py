data = [1, 2, 3, 4]
list_iter = iter(data)
print(type(list_iter))
print(list_iter)
# print(*list_iter)
# print(next(list_iter, -1))
# print(next(list_iter, -1))
# print(next(list_iter, -1))
# print(next(list_iter, -1))
# print(next(list_iter, -1))

flag = True
while flag:
    try:
        print(next(list_iter))
    except StopIteration:
        print('end')
        flag = False
