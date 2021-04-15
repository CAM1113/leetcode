class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        p2 = 1
        p3 = 1
        p5 = 1
        for i in range(2, n + 1):
            v2, v3, v5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(v2, v3, v5)
            if dp[i] == v2:
                p2 += 1
            if dp[i] == v3:
                p3 += 1
            if dp[i] == v5:
                p5 += 1
        return dp[n]


if __name__ == '__main__':
    x = 10
    print(Solution().nthUglyNumber(x))
