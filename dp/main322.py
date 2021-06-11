from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [1000 for _ in range(amount + 1)]
        for i in coins:
            if i < len(dp):
                dp[i] = 1
        for c in coins:
            for j in range(c, len(dp)):
                dp[j] = min(dp[j], dp[j - c] + 1)
        if dp[-1] == 1000:
            return -1
        return dp[-1]
