# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'created {cls}')
#         return instance
#
#
# a = NamedInt(11, 'Valera')
# print(a)

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


a = Singleton('Vasya')
print(a.name)
del a