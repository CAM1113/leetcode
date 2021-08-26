class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + dp[i // 2 + 1]
        return max(dp[-1], dp[-2], dp[-3])


if __name__ == '__main__':
    x = 15
    print(Solution().getMaximumGenerated(x))
