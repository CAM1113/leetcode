from typing import List


# 经典DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        result = [[0, nums[0]], [nums[0], nums[1]]]
        for i in range(2, len(nums)):
            no = max(result[-1][1], result[-2][1], result[-2][0])
            yes = max(result[-2][0] + nums[i], result[-2][1] + nums[i], result[-1][0] + nums[i])
            result.append([no, yes])
        return max(result[-1][0], result[-1][1])
