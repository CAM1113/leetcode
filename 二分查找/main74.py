from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start < end - 1:
            if matrix[start][0] == target or matrix[end][0] == target:
                return True
            middle = (start + end) // 2
            if matrix[middle][0] < target:
                start = middle
            else:
                end = middle
        if matrix[start][0] <= target <= matrix[start][-1]:
            arr = matrix[start]
        else:
            arr = matrix[end]

        start = 0
        end = len(arr) - 1
        while start < end - 1:
            if arr[start] == target or arr[end] == target:
                return True
            middle = (start + end) // 2
            if arr[middle] <= target:
                start = middle
            else:
                end = middle
        return arr[start] == target or arr[end] == target


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 30
    print(Solution().searchMatrix(matrix, target))


if __name__ == '__main__':
    main()
