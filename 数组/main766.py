from typing import List


def is_ok(array: List[List], start_x: int, start_y: int):
    val = array[start_x][start_y]
    while start_x < len(array) and start_y < len(array[0]):
        if array[start_x][start_y] != val:
            return False
        start_y += 1
        start_x += 1
    return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        start_x = 0
        start_y = 0
        while start_y < len(matrix[0]):
            if not is_ok(matrix, start_x, start_y):
                return False
            start_y += 1

        start_x = 0
        start_y = 0
        while start_x < len(matrix):
            if not is_ok(matrix, start_x, start_y):
                return False
            start_x += 1
        return True
