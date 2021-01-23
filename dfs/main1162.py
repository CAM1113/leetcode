from typing import List


def bfs(grid, search_list, last_val):
    if len(search_list) == 0:
        return last_val
    l = []
    for p in search_list:
        x, y = p[0], p[1]
        if x - 1 >= 0 and grid[x - 1][y] == 0:
            grid[x - 1][y] = 1
            l.append([x - 1, y])
        if x + 1 < len(grid) and grid[x + 1][y] == 0:
            grid[x + 1][y] = 1
            l.append([x + 1, y])
        if y - 1 >= 0 and grid[x][y - 1] == 0:
            grid[x][y - 1] = 1
            l.append([x, y - 1])
        if y + 1 < len(grid[0]) and grid[x][y + 1] == 0:
            grid[x][y + 1] = 1
            l.append([x, y + 1])
    return bfs(grid, l, last_val + 1)


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        search_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    search_list.append([i, j])
        if len(search_list) == 0 or len(search_list) == len(grid[0]) * len(grid):
            return -1
        result = -1
        return bfs(grid, search_list, result)


if __name__ == '__main__':
    a = [[1,0,1],[0,0,0],[1,0,1]]
    print(Solution().maxDistance(a))
