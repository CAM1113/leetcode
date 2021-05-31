class Solution:
    def strangePrinter(self, s: str) -> int:
        s_list = [s[0]]
        for c in s:
            if c != s_list[-1]:
                s_list.append(c)
        s = "".join(s_list)
        dp = [[1 for _ in s] for _ in s]
        for length in range(1, len(s)):
            for start in range(len(s)):
                i = start
                j = i + length
                if j >= len(s):
                    break
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    min_val = dp[i][i] + dp[i + 1][j]
                    for k in range(i, j):
                        if dp[i][k] + dp[k + 1][j] < min_val:
                            min_val = dp[i][k] + dp[k + 1][j]
                    dp[i][j] = min_val

        return dp[0][-1]


if __name__ == '__main__':
    x = "aaabbb"
    print(Solution().strangePrinter(x))
