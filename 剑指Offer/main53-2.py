from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if nums[0] != 0:
            return 0
        start = 0
        end = len(nums)
        while start < end - 1:
            middle = (start + end) // 2
            if nums[middle] == middle:
                start = middle
            else:
                end = middle
        return end


if __name__ == '__main__':
    x = [0,2, 1, 3, 4, 5, 7]
    print(Solution().missingNumber(x))
