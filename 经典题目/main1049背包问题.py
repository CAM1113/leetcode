# 0 1 背包问题 https://leetcode-cn.com/problems/last-stone-weight-ii/
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 问题转化为：在stones中挑选一部分stone使得挑选的stone尽可能接近stones总合的一半
        总和 = sum(stones)
        一半 = 总和 // 2
        dp = [[False for _ in range(一半 + 1)] for _ in range(len(stones) + 1)]
        dp[0][0] = True
        for i in range(1, len(stones) + 1):
            stone = stones[i - 1]
            for j in range(一半 + 1):
                if j >= stone:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stone]
                else:
                    dp[i][j] = dp[i - 1][j]
        for i in range(一半, -1, -1):
            if dp[len(stones)][i]:
                return 总和 - i * 2


if __name__ == '__main__':
    s = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeightII(s))
