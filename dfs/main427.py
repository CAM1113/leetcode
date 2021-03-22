from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def dfs(grid: List[List[int]], start_row: int, start_col, end_row: int, end_col: int):
    node = Node(False, True, None, None, None, None)
    temp = grid[start_row][start_col]
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if grid[i][j] != temp:
                node.isLeaf = False
                node.topLeft = dfs(grid, start_row, start_col, (start_row + end_row) // 2, (start_col + end_col) // 2)
                node.topRight = dfs(grid, start_row, (start_col + end_col) // 2, (start_row + end_row) // 2, end_col)
                node.bottomLeft = dfs(grid, (start_row + end_row) // 2, start_col, end_row, (start_col + end_col) // 2)
                node.bottomRight = dfs(grid, (start_row + end_row) // 2, (start_col + end_col) // 2, end_row, end_col)
                return node

    node.isLeaf = True
    if temp == 1:
        node.val = True
    else:
        node.val = False
    return node


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return dfs(grid, 0, 0, len(grid), len(grid[0]))


if __name__ == '__main__':
    grid = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]
    n = Solution().construct(grid)
    print(n)
