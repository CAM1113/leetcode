from typing import List


# python 超时
def dfs(nums: List[int], target: int, index: int, current_num: int, result: List[int]):
    if index == len(nums):
        if current_num == target:
            result[0] += 1
        return
    dfs(nums, target, index + 1, current_num + nums[index], result)
    dfs(nums, target, index + 1, current_num - nums[index], result)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = []
        sums = sum(nums)
        neg = sums - target
        if neg < 0 or neg % 2 != 0:
            return 0
        dfs(nums, target, 0, 0, result)
        return result[0]
