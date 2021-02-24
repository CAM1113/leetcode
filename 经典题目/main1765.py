# bfs经典题目
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        result = [[-1 for i in l] for l in isWater]
        level = []
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 0:
                    level.append((i, j))
                    result[i][j] = 0
        num = 0
        while len(level) != 0:
            num += 1
            next_level = []
            for i, j in level:
                if i - 1 >= 0 and result[i - 1][j] == -1:
                    result[i - 1][j] = num
                    next_level.append((i - 1, j))
                if i + 1 < len(isWater) and result[i + 1][j] == -1:
                    result[i + 1][j] = num
                    next_level.append((i + 1, j))
                if j + 1 < len(isWater[0]) and result[i][j + 1] == -1:
                    result[i][j + 1] = num
                    next_level.append((i, j + 1))
                if j - 1 >= 0 and result[i][j - 1] == -1:
                    result[i][j - 1] = num
                    next_level.append((i, j - 1))
            level = next_level
        return result
