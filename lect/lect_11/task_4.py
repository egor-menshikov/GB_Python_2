class User:
    """User training class."""

    def __init__(self, name):
        """Adding name parameter"""
        self.name = name

    def func(self):
        """Some random method"""
        return self.name.capitalize()

    def __str__(self):
        return f'__str__ User({self.name})'

    def __repr__(self):
        return f"User('{self.name}')"


a = User('egor')
b = User('petr')

print(a)
print([a, b])

