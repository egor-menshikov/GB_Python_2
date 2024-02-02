# from sys import argv
#
# print('start')
# print(type(argv), argv)
# print('stop')

import random

random.seed(a=13)
state = random.getstate()
print(random.random())
random.setstate(state)
print(random.random())

_l = [1, 3, 4]

print(random.choice(_l))
print(random.choice(_l))
print(random.choice(_l))
