text = ['Hi', 'bEEr', 'lOlOOLOLOllo']
res = map(lambda x: x.lower(), text)
print(*res)

_list = [1, 2, 3, 4, 5, 6, 7, 8]
res2 = filter(lambda x: x % 2 == 0, _list)
print(*res2)

l1 = [1, 3, 5]
l2 = ['a', 'b', 'c']
res3 = zip(l1, l2)
print(*res3)