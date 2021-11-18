class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        new_mtrx = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        for i in range(len(new_mtrx)):
            for j in range(len(new_mtrx[i])):
                new_mtrx[i][j] = self.list1[i][j] + self.list2[i][j]
        mtrx = []
        for lst in new_mtrx:
            lines = ''
            for n in lst:
                lines += str(n)
                lines += ' '
            mtrx.append(lines)
        return '\n'.join(i for i in mtrx)
# я не поняла как нам из этого метода обратить в метод str
    def __str__(self):
        mtrx = []
        for lst in self.list1:
            lines = ''
            for n in lst:
                lines += str(n)
                lines += ' '
            mtrx.append(lines)
        return '\n'.join(i for i in mtrx)


matr = Matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]],

              [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(matr.__add__())
