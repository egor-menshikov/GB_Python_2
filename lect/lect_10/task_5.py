class Parent1:
    def __init__(self):
        self.age = 37


class Parent2:
    def __init__(self):
        self.height = 180


class Parent3:
    def __init__(self):
        self.weight = 75


class Child(Parent1, Parent2, Parent3):
    def __init__(self):
        self.name = 'Egor'
        Parent1.__init__(self)
        Parent2.__init__(self)
        Parent3.__init__(self)


p1 = Child()
print(p1.name, p1.age, p1.height, p1.weight)

print(Child.mro())

# class Hero(Person, Address, Weapon):

# def __init__(self, power, name=None, race=None, speed=None,
#              country=None, city=None, street=None,
#              left_hand=None, right_hand=None):
#     self.power = power
#     Person.__init__(self, name, race, speed)
#     Address.__init__(self, country, city, street)
#     Weapon.__init__(self, left_hand, right_hand)
