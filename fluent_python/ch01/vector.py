from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        # The __repr__ special method is called by the repr built-in to get string representation
        # of the object for inspection
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# list comp

str = "this is a simple string"
ascii = [ord(s) for s in str]
print(ascii)

ascii = list(filter(lambda c: c > 50, map(ord, str)))
print(ascii)
