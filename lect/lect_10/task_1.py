class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.hp = 100
        print(f'{id(self) = }')


p1 = Person()
p2 = Person()
print(f'{id(p1) = }')
print(f'{id(p2) = }')
print(f'{id(Person) = }')
