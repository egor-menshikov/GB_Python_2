from seminars.sem_10.tasks_5_6.animal import Animal


class Parrot(Animal):
    def __init__(self, word_capacity, name, age):
        self._word_capacity = word_capacity
        Animal.__init__(self, name, age)

    def get_special_info(self):
        return f'{self._word_capacity = }'


if __name__ == '__main__':
    parrot = Parrot(1000, 'Kesha', '2')

    print(parrot.get_info())
    print(parrot.get_special_info())
