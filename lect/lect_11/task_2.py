import sys


class User:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} created')

    def __del__(self):
        print(f'{self.name} deleted')


a = User('Egor')
print(sys.getrefcount(a))
b = User('Petr')
d = c = a
print(sys.getrefcount(d))
del a
print(sys.getrefcount(d))
