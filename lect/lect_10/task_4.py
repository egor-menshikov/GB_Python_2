from task_3 import Person


class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)

    def leech(self, other, damage):
        self.hp += damage * 2
        other.hp -= damage * 2

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self.max_up * 2)


p1 = Hero('archery', 'Egor', 'Human', 135)
print(p1.power)
print(f'{p1.name =}\n{p1.up = }\n{p1.power =}')
