from time import time

# O(n)超时，换dfs
class Solution:
    def minDays(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            min_day = dp[i - 1] + 1
            if i % 2 == 0 and dp[i // 2] + 1 < min_day:
                min_day = dp[i // 2] + 1
            if i % 3 == 0 and dp[i // 3] + 1 < min_day:
                min_day = dp[i // 3] + 1
            dp[i] = min_day
        return dp[-1]


if __name__ == '__main__':
    x = 1
    t1 = time()
    print(Solution().minDays(5739253))
    t2 = time()
    print(t2-t1)
