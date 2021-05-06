def set_matrix_zero(matrix, i, j):
    if i < 0:
        # 第j列置0
        for r in range(len(matrix)):
            matrix[r][j] = 0
    if j < 0:
        # 第i行置0
        for c in range(len(matrix[0])):
            matrix[i][c] = 0


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set([])
        col_set = set([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for r in row_set:
            set_matrix_zero(matrix, r, -1)

        for c in col_set:
            set_matrix_zero(matrix, -1, c)


def main():
    x = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    Solution().setZeroes(x)
    print(x)


if __name__ == '__main__':
    main()
