from typing import List


def get_next_xy(index_x, index_y, index_d, array, m, n):
    if (index_x == 0 and index_d == 3) or (index_x == m - 1 and index_d == 1) \
            or (index_y == 0 and index_d == 2) or (index_y == n - 1 and index_d == 0):
        index_d = (index_d + 1) % 4
    else:
        if index_d == 0:
            new_index_x = index_x
            new_index_y = index_y + 1
        elif index_d == 1:
            new_index_x = index_x + 1
            new_index_y = index_y
        elif index_d == 2:
            new_index_x = index_x
            new_index_y = index_y - 1
        else:
            new_index_x = index_x - 1
            new_index_y = index_y
        if array[new_index_x][new_index_y] == sys.maxsize:
            index_d = (index_d + 1) % 4

    if index_d == 0:
        new_index_x = index_x
        new_index_y = index_y + 1
    elif index_d == 1:
        new_index_x = index_x + 1
        new_index_y = index_y
    elif index_d == 2:
        new_index_x = index_x
        new_index_y = index_y - 1
    else:
        new_index_x = index_x - 1
        new_index_y = index_y
    return new_index_x, new_index_y, index_d


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        result = []
        index_x = 0
        index_y = 0
        index_d = 0
        m = len(matrix)
        n = len(matrix[0])
        for _ in range(n * m):
            result.append(matrix[index_x][index_y])
            matrix[index_x][index_y] = sys.maxsize
            index_x, index_y, index_d = get_next_xy(index_x, index_y, index_d, matrix, m, n)
        return result
