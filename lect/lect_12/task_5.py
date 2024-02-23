class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


p = Person('Petr')
print(p.name)
p.name = 'Egor'
print(p.name)
