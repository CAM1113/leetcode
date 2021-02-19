from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 1 and 1 in obstacleGrid[0]:
            return 0
        if len(obstacleGrid[0]) == 1 and [1] in obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        steps = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]
        steps[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and j > 0:
                    steps[i][j] = steps[i - 1][j] + steps[i][j - 1]
                if i == 0 and j > 0:
                    steps[i][j] = steps[i][j - 1]
                if i > 0 and j == 0:
                    steps[i][j] = steps[i - 1][j]
        return steps[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [[0, 1], [0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
