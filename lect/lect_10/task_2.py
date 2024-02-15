class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.hp = 100

    def level_up(self):
        self.level += 1

    def leech(self, other, damage):
        self.hp += damage
        other.hp -= damage


p1 = Person('P1')
p2 = Person('P2')

p1.leech(p2, 15)
print(p1.hp, p2.hp)
