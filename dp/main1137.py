class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [1 for _ in range(n)]
        dp[0] = 0
        index = 3
        while index < n:
            dp[index] = dp[index - 1] + dp[index - 2] + dp[index - 3]
        return dp[-1]
