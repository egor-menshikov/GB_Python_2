# my_gen = (chr(i) for i in range(97, 123))
# print(type(my_gen))
# mult =(i + j for i in range(5) if i % 2 != 0 for j in range(5, 10))
# print(*mult)

from timeit import timeit

nums = [i for i in range(100001)]


def slower(data: list[int]) -> list[int]:
    res = []
    for item in data:
        if item % 2 == 0:
            res.append(item)
    return res


def remake_list(data: list[int]) -> list[int]:
    res = []
    for item in data:
        if item % 2 == 0:
            res = res + [item]
    return res


def faster(data: list[int]) -> list[int]:
    return [item for item in data if item % 2 == 0]


print(timeit('slower(nums[:])', globals=globals(), number=1))
print(timeit('remake_list(nums[:])', globals=globals(), number=1))
print(timeit('faster(nums[:])', globals=globals(), number=1))
