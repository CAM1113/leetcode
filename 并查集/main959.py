from typing import List


def find(array, index):
    if array[index] == index:
        return index
    root = find(array, array[index])
    array[index] = root
    return root


def union(array, index1, index2):
    root1 = find(array, index1)
    root2 = find(array, index2)
    array[root2] = root1

# 失败
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        array = [i for i in range(len(grid) * 4)]
        for index in range(len(grid)):
            if grid[index] == ' ':
                union(array, index, index + 1)
                union(array, index, index + 2)
                union(array, index, index + 3)
            elif grid[index] == '/':
                union(array, index, index + 1)
                union(array, index + 2, index + 3)
            elif grid[index] == '\\':
                union(array, index, index + 3)
                union(array, index + 1, index + 2)
