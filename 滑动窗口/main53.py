import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        start = 0
        length = 0
        max_sum = -1e10
        while start + length < len(nums):
            sums += nums[start + length]
            if sums > max_sum:
                max_sum = sums
            if sums < 0:
                sums = 0
                start += 1
                length = 0
            else:
                length += 1
        return max_sum
