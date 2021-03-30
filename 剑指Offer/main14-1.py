class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2

        for i in range(4, n + 1):
            max_mul = 1
            for j in range(2, i // 2 + 1):
                mul1 = j * (i - j)
                mul2 = j * dp[i - j]
                max_mul = max(mul1, mul2, max_mul)
            dp[i] = max_mul

        return dp[-1]


if __name__ == '__main__':
    print(Solution().cuttingRope(10))
