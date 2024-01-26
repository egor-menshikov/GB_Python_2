l_1 = [1, 2, 2, 3]

l_2 = list(set(l_1))
print(l_2)

l_3 = []
for item in l_1:
    if item not in l_3:
        l_3.append(item)
print(l_3)
