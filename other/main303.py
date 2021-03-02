from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        index = 1
        self.nums = nums
        while index < len(nums):
            self.nums[index] = self.nums[index] + self.nums[index - 1]
            index += 1

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]


if __name__ == '__main__':
    x = [-2, 0, 3, -5, 2, -1]
    y = NumArray(x)
