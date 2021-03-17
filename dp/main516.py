class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[1 for _ in range(length)] for _ in range(length)]
        for j in range(length):
            for i in range(j, -1, -1):
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                    continue
                if i == j:
                    continue
                if i == j - 1:
                    dp[i][j] = 2
                    continue
                dp[i][j] = dp[i + 1][j - 1] + 2
        return dp[0][length - 1]


if __name__ == '__main__':
    s = "cbbd"
    print(Solution().longestPalindromeSubseq(s))

