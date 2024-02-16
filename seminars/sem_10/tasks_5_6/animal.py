class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f'{self._name = }\n{self._age = }'
