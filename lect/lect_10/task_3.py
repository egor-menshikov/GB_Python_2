class Person:
    max_up = 3
    _max_level = 80
    __secret = 'surprise'

    def __init__(self, name, race='unknown', speed=100):
        self.up = 3
        self.name = name
        self.race = race
        self.level = 1
        self.hp = 100
        self._speed = speed

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def leech(self, other, damage):
        self.hp += damage
        other.hp -= damage

    def __trick(self):
        return self.__secret


p1 = Person('P1')
print(p1._Person__secret)
print(p1._Person__trick())
print(Person._Person__secret)
