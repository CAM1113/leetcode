from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        while start < end - 1:
            middle = (start + end) // 2
            if nums[middle] < target:
                start = middle
                continue
            if nums[middle] > target:
                end = middle
                continue
            if nums[middle] == target:
                return middle
        return -1
