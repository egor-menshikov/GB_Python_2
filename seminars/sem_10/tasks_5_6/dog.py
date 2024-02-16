from seminars.sem_10.tasks_5_6.animal import Animal


class Dog(Animal):
    def __init__(self, run_speed, max_meal_capacity, name, age):
        self._run_speed = run_speed
        self._max_meal_capacity = max_meal_capacity
        super().__init__(name, age)

    def get_special_info(self):
        return f'{self._run_speed = }\n{self._max_meal_capacity = }'