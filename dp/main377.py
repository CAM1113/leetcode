import collections
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        for i in range(1, target+1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]
        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))
