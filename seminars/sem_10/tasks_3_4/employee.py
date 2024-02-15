"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from seminars.sem_10.tasks_3_4.person import Person


class Employee(Person):
    def __init__(self, uid: int, name=None, surname=None, age=None):
        if len(str(uid)) == 6:
            self._uid = uid
        else:
            flag = True
            while flag:
                uid = input('Enter employee id')
                if len(uid) == 6:
                    self._uid = int(uid)
                    flag = False
        self._access_lvl = self._uid % 7

        Person.__init__(self, name, surname, age)

    def get_info(self):
        return f'{self.full_name() + ', ' + str(self.get_age())}\nid: {self._uid}\naccess_lvl: {self._access_lvl}'


e1 = Employee(123456, 'Egor', 'Menshikov', 37)

print(e1.get_info())
