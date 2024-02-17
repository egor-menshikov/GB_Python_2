class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        super().__init__(name)

    def wing_length(self):
        return self.wingspan


class Fish(Animal):
    def __init__(self, name, max_depth):
        self.max_depth = max_depth
        super().__init__(name)

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        if self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name, weight):
        self.weight = weight
        super().__init__(name)

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        if self.weight > 200:
            return 'Гигант'
        return 'Обычный'


class AnimalFactory:
    def __init__(self):
        self.animal_types = ['Bird', 'Fish', 'Mammal']

    def create_animal(animal_type, *args):
        animal_types = ['Bird', 'Fish', 'Mammal']
        if animal_type not in animal_types:
            raise ValueError('Недопустимый тип животного')
        else:
            if animal_type == 'Bird':
                return Bird(*args)
            if animal_type == 'Fish':
                return Fish(*args)
            return Mammal(*args)

# p = AnimalFactory.create_animal('Fish', 'Vasya', 500)
