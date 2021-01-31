from typing import List


# 并查集+广度优先

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


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        array = [i for i in range(row * col)]
        num = 0
        next_grid = [(0, 0)]
        while find(array, 0) != find(array, col * row - 1):
            next_grid.sort(key=lambda x: grid[x[0]][x[1]])
            num = max(num, grid[next_grid[0][0]][next_grid[0][1]])
            i, j = next_grid[0]
            union(array, i * col + j, 0)
            next_grid.pop(0)
            if i + 1 < row and find(array, (i + 1) * col + j) != find(array, 0) and (i + 1, j) not in next_grid:
                next_grid.append((i + 1, j))
            if j + 1 < col and find(array, 0) != find(array, i * col + j + 1) and (i, j + 1) not in next_grid:
                next_grid.append((i, j + 1))
            if j - 1 >= 0 and find(array, 0) != find(array, i * col + j - 1) and (i, j - 1) not in next_grid:
                next_grid.append((i, j - 1))
            if i - 1 >= 0 and find(array, 0) != find(array, (i - 1) * col + j) and (i - 1, j) not in next_grid:
                next_grid.append((i - 1, j))

        return num


if __name__ == '__main__':
    x = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(Solution().swimInWater(x))
