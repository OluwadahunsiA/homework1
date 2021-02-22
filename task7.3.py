class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return f'Total sum: {self.count + other.count}'

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return f'Difference: {self.count - other.count}'
        elif(other.count - self.count) > 0:
            return f'Difference: {other.count - self.count}'
        else:
            return 'Invalid'

    def __mul__(self, other):
        return f'Total product: {self.count * other.count}'

    def __truediv__(self, other):
        return f'True division: {round((self.count)/(other.count))}'

    def make_order(self, total, cellno):
        shelf = ''
        count = 0
        for _ in range(total):
            shelf += '*'
            count += 1
            if count == cellno:
                shelf += '\\n'
                count = 0
            else:
                continue
        return shelf[:-2] if total % cellno == 0 else shelf


cell1 = Cell(10)
cell2 = Cell(3)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)

print(cell1.make_order(12, 5))
print(cell2.make_order(20, 2))
print(cell2.make_order(15, 5))
