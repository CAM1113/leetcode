from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                return [nums[start], nums[end]]
