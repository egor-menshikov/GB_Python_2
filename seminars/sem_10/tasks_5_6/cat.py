from seminars.sem_10.tasks_5_6.animal import Animal


class Cat(Animal):
    def __init__(self, jump_height, max_sleep_duration, name, age):
        self._jump_height = jump_height
        self._max_sleep_duration = max_sleep_duration
        Animal.__init__(self, name, age)

    def get_special_info(self):
        return f'{self._jump_height = }\n{self._max_sleep_duration = }'


if __name__ == '__main__':
    creature1 = Cat(2, 24, 'Vaksa', 7)

    print(creature1.get_info())
    print(creature1.get_special_info())
