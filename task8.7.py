class Complex:
    def __init__(self, real, complex):
        self.real = real
        self.complex = complex

    def __str__(self):
        return (f'Z = {self.real} + {self.complex}i')

    def __add__(self, other):
        return(
            f'Complex sum: {self.real + other.real} + {self.complex + other.complex}i')

    def __mul__(self, other):
        return(f'Complex product: {(self.real * other.real)-(self.complex * other.complex)} + {(self.real * other.complex) + (self.complex * other.real)}i')


a = Complex(2, 3)
b = Complex(4, 5)
print(b)
print(a+b)
print(a * b)
