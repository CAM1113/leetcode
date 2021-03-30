class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        dp = [1 for i in range(n + 1)]
        dp[1] = x
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2] * dp[i // 2]
            else:
                dp[i] = dp[(i + 1) // 2] * dp[(i - 1) // 2]
        return dp[-1]

if __name__ == '__main__':
    print(Solution().myPow(2,9))
