from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        index = 0
        while start + index < len(nums) or start - index >= 0:
            if start + index < len(nums):
                if nums[start + index] == target:
                    return start + index
            if start - index >= 0:
                if nums[start - index] == target:
                    return start - index
