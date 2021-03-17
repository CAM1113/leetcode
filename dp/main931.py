import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        num_row = len(matrix)
        num_col = len(matrix[0])
        dp = [[i for i in row] for row in matrix]
        for i in range(1, num_row):
            for j in range(num_col):
                j1 = sys.maxsize
                j2 = sys.maxsize
                if j - 1 >= 0:
                    j1 = dp[i - 1][j - 1]
                if j + 1 < num_col:
                    j2 = dp[i - 1][j + 1]
                j3 = dp[i - 1][j]
                dp[i][j] = min(j1, j2, j3) + dp[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    matrix = [[-48]]
    print(Solution().minFallingPathSum(matrix))
