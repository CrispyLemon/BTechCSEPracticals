# WAP to create a class Matrix. The porgram should be able to read, add, subtract and multiply two matrices. Additionally it should have methods to find the inverse of the matriix and check whether the matrix is an identity matrix or not.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])

    def __str__(self):
        return f"{self.matrix}"

    def __add__(self, other):
        if self.row == other.row and self.col == other.col:
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.col)] for i in range(self.row)])
        else:
            return "The matrices cannot be added"

    def __sub__(self, other):
        if self.row == other.row and self.col == other.col:
            return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.col)] for i in range(self.row)])
        else:
            return "The matrices cannot be subtracted"

    def __mul__(self, other):
        if self.col == other.row:
            return Matrix([[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.col)]) for j in range(other.col)] for i in range(self.row)])
        else:
            return "The matrices cannot be multiplied"

    def inverse(self):
        if self.row == self.col:
            temp = [[self.matrix[i][j] for j in range(self.col)] for i in range(self.row)]
            inv = [[0 for j in range(self.col)] for i in range(self.row)]
            for i in range(self.row):
                inv[i][i] = 1
            for i in range(self.row):
                for j in range(i + 1, self.col):
                    ratio = temp[j][i] / temp[i][i]
                    for k in range(self.col):
                        temp[j][k] -= ratio * temp[i][k]
                        inv[j][k] -= ratio * inv[i][k]
            for i in range(self.row - 1, -1, -1):
                for j in range(self.col - 1, -1, -1):
                    ratio = temp[j][i] / temp[i][i]
                    for k in range(self.col):
                        temp[j][k] -= ratio * temp[i][k]
                        inv[j][k] -= ratio * inv[i][k]
            for i in range(self.row):
                for j in range(self.col):
                    inv[i][j] /= temp[i][i]
            return Matrix(inv)
        else:
            return "The matrix is not square"
        
    def identity(self):
        if self.row == self.col:
            for i in range(self.row):
                for j in range(self.col):
                    if i == j:
                        if self.matrix[i][j] != 1:
                            return False
                    else:
                        if self.matrix[i][j] != 0:
                            return False
            return True
        else:
            return False
        
#implementation
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#add
mat1 = Matrix(matrix1)
mat2 = Matrix(matrix2)
print("The sum of the two matrices is: ", mat1 + mat2)
#subtract
print("The difference of the two matrices is: ", mat1 - mat2)
#multiply
print("The product of the two matrices is: ", mat1 * mat2)
#inverse
print("The inverse of the first matrix is: ", mat1.inverse())
#identity
print("The first matrix is an identity matrix: ", mat1.identity())  
print("The second matrix is an identity matrix: ", mat2.identity())