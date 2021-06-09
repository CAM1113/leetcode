from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        neg = sums - target
        if neg < 0 or neg % 2 != 0:
            return 0
        neg = neg // 2
        dp = [[0 for _ in range(neg + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[len(nums)][neg]


if __name__ == '__main__':
    n = [1, 2, 1]
    t = 0
    print(Solution().findTargetSumWays(n, t))
