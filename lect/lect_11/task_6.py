class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError(f'No such attribute: {item}')
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return None

    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value + 1)

    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)

    @property
    def get_x(self):
        return self.x


v = Vector(1, 3)
print(v.u)
