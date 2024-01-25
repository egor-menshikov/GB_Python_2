_list = [1, 2, 7]
print(max(_list))

_list_2 = [(1, 3), (600, 2)]
print(max(_list_2, key=lambda x: x[1]))

_list_3 = [1, 2, 3]
print(sum(_list_3, start=1000))


def something():
    x = 4
    print(locals())
    print(globals())


something()

for k,v in vars(list).items():
    print(k,v)
