from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in grid[0]] for _ in grid]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i < 1 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i > 0 and j < 1:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
