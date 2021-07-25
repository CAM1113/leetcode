from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_result = 0
        for i in range(n//2):
            if nums[i] + nums[n-i-1]>max_result:
                max_result = nums[i] + nums[n-i-1]
        return max_result


