from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j+1):
                if s[i] != s[j]:
                    continue
                if j-i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
        level_set = set()
        already_set = set()
        times = 0
        for i in range(n):
            if dp[0][i]:
                level_set.add(i)

        while len(level_set) != 0:
            next_set = set()
            for e in level_set:
                if e == n - 1:
                    return times
                already_set.add(e)
                for i in range(e + 1, n):
                    if dp[e+1][i] and i not in already_set and i not in level_set:
                        next_set.add(i)
            level_set = next_set
            times += 1

        return times


if __name__ == '__main__':
    x = "abb"
    print(Solution().minCut(x))
