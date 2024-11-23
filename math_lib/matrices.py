import random

import utils as utls
import math_lib as ml

# matrixA = [[column for column in range(4)] for row in range(4)]

# row = 2
# column = 3

# matrixA[row - 1][column - 1] = 9

# print(matrixA)

# for row in matrixA:
#     columnI = ""
#     for column in row:
#         columnI += ((str(column) + " ") if (row.index(column) != -1) else (str(column)))
#     print("|" + columnI + "|")
# for row in matrixA:
#     row_string = ", ".join(str(column) for column in row)
#     print("|" + row_string + "|")

class Matrix:
    def __init__(self, rows, cols, fillValue = 0):
        self.rows = rows
        self.cols = cols
        self.data = [[fillValue for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def getRow(self, rowIndex):
        if rowIndex < 0 or rowIndex >= self.rows:
            raise IndexError("Row index out of range")
        return self.data[rowIndex]

    def setRow(self, rowIndex, row):
        if rowIndex < 0 or rowIndex >= self.rows:
            raise IndexError("Row index out of range")
        if len(row) != self.cols:
            raise ValueError("The length of the row must match the number of columns.")
        self.data[rowIndex] = row

    def getCol(self, colIndex):
        if colIndex < 0 or colIndex >= self.cols:
            raise IndexError("Col index out of range")
        return (self.data[row][colIndex] for row in range(self.rows))

    def setCol(self, colIndex, col):
        if colIndex < 0 or colIndex >= self.cols:
            raise IndexError("Col index out of range")
        if len(col) != self.cols:
            raise ValueError("The length of the col must match the number of rows.")
        for i in range(self.rows):
            self.data[i][colIndex] = col[i]

    def transpose(self):
        transposedMatrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposedMatrix.set(j, i, self.get(i, j))
        return transposedMatrix

    # __method__ methods

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if not isinstance(other, (Matrix, int, float, str)):
            raise TypeError("Object must be of type Matrix, int, float or str")

        if isinstance(other, (int, float)):
            matrixToReturn = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    element = self.get(row, col)
                    if not isinstance(element, (int, float)):
                        raise TypeError("Elements in the matrix must be of type int or float to perform addition with a numeric scalar")
                    matrixToReturn.set(row, col, element + other)
            return matrixToReturn

        elif isinstance(other, str):
            matrixToReturn = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    element = self.get(row, col)
                    if not isinstance(element, str):
                        raise TypeError("Elements in the matrix must be of type str to perform concatenation by a str scalar")
                    matrixToReturn.set(row, col, element + other)
            return matrixToReturn

        elif isinstance(other, Matrix):
            if ((self.rows != other.rows) or (self.cols != other.cols)):
                raise ValueError("Matrices must have the same dimentions to perform addition")

            matrixToReturn = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    elementSelf = self.get(row, col)
                    elementOther = other.get(row, col)
                    if not isinstance(element, str):
                        raise TypeError("Elements in the matrix must be of type str to perform concatenation by a str scalar")
                    matrixToReturn.set(row, col, elementSelf + elementOther)
            return matrixToReturn
    
    def __sub__(self, other):
        if not isinstance(other, (Matrix, int, float)):
            raise TypeError("Object must be of type Matrix, int, float")

        if isinstance(other, (int, float)):
            matrixToReturn = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    element = self.get(row, col)
                    if not isinstance(element, (int, float)):
                        raise TypeError("Elements in the matrix must be of type int or float to perform addition with a numeric scalar")
                    matrixToReturn.set(row, col, element - other)
            return matrixToReturn

        elif isinstance(other, Matrix):
            if ((self.rows != other.rows) or (self.cols != other.cols)):
                raise ValueError("Matrices must have the same dimentions to perform addition")

            matrixToReturn = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    elementSelf = self.get(row, col)
                    elementOther = other.get(row, col)
                    if not isinstance(element, str):
                        raise TypeError("Elements in the matrix must be of type str to perform concatenation by a str scalar")
                    matrixToReturn.set(row, col, elementSelf - elementOther)
            return matrixToReturn

# Only if the matrices.py is runned directly
if __name__ == "__main__":
    testMatrixRows = random.randint(1, 5)
    testMatrixCols = random.randint(1, 5)
    testMatrixFillValue = random.randint(1, 10)

    testMatrix = Matrix(testMatrixRows, testMatrixCols, testMatrixFillValue)

    # Perform getting and setting an element in the matrix
    for row in range(testMatrix.rows):
        for col in range(testMatrix.cols):
            element = testMatrix.get(row, col)
            print(f"Original element at ({row}, {col}): {element}")
            randomElement = random.random()
            testMatrix.set(row, col, randomElement)
            element2 = testMatrix.get(row, col)
            print(f"New element at ({row}, {col}): {element2}")
            print("......")
            print(f"Column {col}: {testMatrix.getCol(col)}")
        print("......")
        print(f"Row {row}: {testMatrix.getRow(row)}")

    print("Matrix data:")
    print(testMatrix)