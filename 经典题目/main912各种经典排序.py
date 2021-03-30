# 各种排序算法
from typing import List


# 冒泡排序,时间复杂度O(n**2)，
def BubbleSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(1, n - i):
            if nums[j - 1] > nums[j]:
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp
    return nums


# 选择排序，时间复杂度O(n**2)，
def SelectSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if nums[min_index] > nums[j]:
                min_index = j
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
    return nums


# 插入排序，时间复杂度O(n**2)，
def InsertSort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        j = i - 1
        while j > 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j] = temp
    return nums


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return InsertSort(nums)


if __name__ == '__main__':
    num = [5, 2, 3, 1]
    print(Solution().sortArray(num))
