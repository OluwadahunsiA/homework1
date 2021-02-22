class Matrix:
    def __init__(self, *args):
        self.dict = [*args]

    def __str__(self):
        matrix = ''
        initial = len(self.dict[1])
        for row in self.dict:
            if len(row) == initial:  # ensure all rows have the same columns.
                matrix += f"{'  '.join(map(str, row))}\n"
            else:
                break
        return matrix

    def __add__(self, other):
        matrix = ''
        for row in range(len(self.dict)):

            matrix += f"{ ' '.join(map(str, [(self.dict[row][i] + other.dict[row][j]) for i in range(len(self.dict)) for j in range(len(other.dict)) if i == j]))}\n"
        return matrix


mat1 = Matrix([1, 2, 4], [4, 5, 6], [2, 4, 5])
mat2 = Matrix([1, 2, 4], [1, 1, 1], [2, 2, 2])

print(mat1, end='\n')
print(mat2, end='\n')
print(mat1 + mat2)
