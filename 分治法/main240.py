from typing import List


class Solution:
    def searchM atrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        min_index = 0
        max_index = len(matrix) - 1

        while min_index < max_index - 1:
            middle_index = (min_index + max_index) // 2
            if matrix[middle_index][0] < target:
                min_index = middle_index
            if matrix[middle_index][0] > target:
                max_index = middle_index
            if matrix[middle_index][0] == target:
                return True

        new_matrix = []
        if min_index == max_index:
            new_matrix = matrix[min_index]
        if max_index == min_index + 1:
            new_matrix = [*matrix[min_index], *matrix[max_index]]
        matrix = new_matrix
        matrix.sort()
        min_index = 0
        max_index = len(matrix) - 1
        while min_index < max_index - 1:
            middle_index = (min_index + max_index) // 2
            if matrix[middle_index] < target:
                min_index = middle_index
            if matrix[middle_index] > target:
                max_index = middle_index
            if matrix[middle_index] == target:
                return True

        return matrix[min_index] == target or matrix[max_index] == target


if __name__ == '__main__':
    m =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    t = 5
    print(Solution().searchMatrix(m, t))
