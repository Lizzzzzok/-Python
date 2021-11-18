class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return self.amount - other.amount
        else:
            return 'Impossible †o subtract as the result is a negative number'

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        return round(self.amount / other.amount)

    def make_order(self, c_in_r):
        row = ''
        n = 0
        for i in range(int(self.amount / c_in_r)):
            n += 1
            row += "*" * c_in_r
            if n == int(self.amount // c_in_r) and int(self.amount % c_in_r) == 0 :
                break
            row += '\\n'
        row += f'{"*" * (self.amount % c_in_r)}'
        return row


cell1 = Cell(12)
cell2 = Cell(15)
print(cell1)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
print(cell2.make_order(5))
