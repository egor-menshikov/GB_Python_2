class User:
    """User training class."""

    def __init__(self, name):
        """Adding name parameter"""
        self.name = name

    def func(self):
        """Some random method"""
        return self.name.capitalize()


a = User('Egor')

help(a)

# print(a.__doc__)
