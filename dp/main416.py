# 0 1 背包问题
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        half = sums // 2
        dp = [[False for _ in range(half + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            n = nums[i - 1]
            for j in range(half + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= n:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - n]
        return dp[-1][-1]


if __name__ == '__main__':
    ns = [1, 5, 11, 5]
    print(Solution().canPartition(ns))
