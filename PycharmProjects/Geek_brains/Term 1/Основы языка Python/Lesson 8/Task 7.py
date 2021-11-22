class ComplexNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return f'The sum is: {self.num1 + other.num1} + {(self.num2 + other.num2)} * i'

    def __mul__(self, other):
        return f'The result of multiplication is: {self.num1 * other.num1 - self.num2 * other.num2} + {self.num2 * other.num1 + self.num1 * other.num2} * i'


num1 = ComplexNumber(5, 8)
num2 = ComplexNumber(3, -2)
print(num1 + num2)
print(num1 * num2)
