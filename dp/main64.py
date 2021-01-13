from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        result = [a[:] for a in grid]
        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    if j == 0:
                        continue
                    else:
                        result[i][j] = result[i][j-1] + grid[i][j]
                    continue
                if j == 0:
                    if i == 0:
                        continue
                    result[i][j] = result[i-1][j] + grid[i][j]
                    continue

                result[i][j] = min(result[i-1][j],result[i][j-1]) + grid[i][j]
        return result[-1][-1]


def main():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))


if __name__ == '__main__':
    main()
