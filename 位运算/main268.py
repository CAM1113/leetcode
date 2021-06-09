from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ i
            res = res ^ nums[i]
        res = res ^ len(nums)
        return res
