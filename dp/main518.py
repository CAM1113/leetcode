from typing import List


# 二维dp太慢
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            coin = coins[i - 1]
            for j in range(amount + 1):
                times = 0
                while coin * times <= j:
                    dp[i][j] += dp[i - 1][j - coin * times]
                    times += 1
        return dp[len(coins)][amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount + 1)]
