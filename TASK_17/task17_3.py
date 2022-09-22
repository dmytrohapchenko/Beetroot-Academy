class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(self.value, int) or isinstance(self.value, float):
            return Fraction(self.value + other.value)
        raise ValueError(f'...')

    def __sub__(self, other):
        if isinstance(self.value, int) or isinstance(self.value, float):
            return Fraction(self.value - other.value)
        raise ValueError(f'...')

    def __mul__(self, other):
        if isinstance(self.value, int) or isinstance(self.value, float):
            return Fraction(self.value * other.value)
        raise ValueError(f'...')

    def __floordiv__(self, other):
        if isinstance(self.value, int) or isinstance(self.value, float):
            return Fraction(self.value // other.value)
        raise ValueError(f'...')

    def __str__(self):
        return f'Result: {self.value}'


x = Fraction(125)
y = Fraction(25)
print(x + y)
print(x - y)
print(x * y)
print(x // y)  # because magic method __div__ doesn't work at all
