import csv


class ValidationDescriptor:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.param_name, value)

    def validate(self, value):
        for item in value.split():
            if not item.isalpha() or not item.istitle():
                print('ФИО должно состоять только из букв и начинаться с заглавной буквы')
                return False
        return True


class Student:
    name = ValidationDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}'

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as file:
            subjects = csv.reader(file).__next__()
            res = {}
            for item in subjects:
                res[item] = {'оценки': [], 'тесты': []}
        return res

    def add_grade(self, subject, grade):
        if subject not in self.subjects.keys():
            print('Предмет {Название предмета} не найден')
        elif not isinstance(grade, int) or grade not in range(2, 6):
            print('Оценка должна быть целым числом от 2 до 5')
        else:
            self.subjects[subject]['оценки'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects.keys():
            print('Предмет {Название предмета} не найден')
        elif not isinstance(test_score, int) or test_score not in range(0, 101):
            print('Результат теста должен быть целым числом от 0 до 100')
        else:
            self.subjects[subject]['тесты'].append(test_score)

    def get_average_grade(self):
        count = 0
        overall = 0
        for subject in self.subjects.keys():
            overall += sum(self.subjects[subject]['оценки'])
            count += len(self.subjects[subject]['оценки'])
        return overall / count

    def get_average_test_score(self, subject):
        return sum(self.subjects[subject]['тесты']) / len(self.subjects[subject]['тесты'])


a = Student('Меньшиков Егор Леонидович', 'subjects.csv')
a.add_grade('Математика', 5)
a.add_test_score('Физика', 100)
print(a.subjects)
print(a)
