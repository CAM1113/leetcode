import sys
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -sys.maxsize)
        nums.append(-sys.maxsize)
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
