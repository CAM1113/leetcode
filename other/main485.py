from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = 0
        max_length = 0
        start = 0
        while start + length < len(nums):
            if nums[start + length] == 0:
                start = start + length + 1
                length = 0
            else:
                length += 1
                if length > max_length:
                    max_length = length
        return max_length

