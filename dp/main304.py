from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        if row < 0:
            self.matrix = matrix
            return
        col = len(matrix[0])
        if col < 0:
            self.matrix = matrix
            return
        if matrix[0][0] is not int:
            self.matrix = matrix
            return
        for i in range(row):
            for j in range(col):
                sums = 0
                if i > 0:
                    sums += matrix[i - 1][j]
                if j > 0:
                    sums += matrix[i][j - 1]
                if i > 0 and j > 0:
                    sums -= matrix[i - 1][j - 1]
                matrix[i][j] += sums
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.matrix[row2][col2]
        if row1 > 0:
            result -= self.matrix[row1 - 1][col2]
        if col1 > 0:
            result -= self.matrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            result += self.matrix[row1 - 1][col1 - 1]
        return result


if __name__ == '__main__':
    matrix = [[[]]]

    NumMatrix(matrix)
