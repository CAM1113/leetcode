# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
#         for i in range(len(text1)):
#             for j in range(len(text2)):
#                 if text1[i] == text2[j]:
#                     dp[i + 1][j + 1] = dp[i][j] + 1
#                 else:
#                     dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
#         return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    x = "cfcd"
    b = "cceeecd"
    print(Solution().longestCommonSubsequence(x, b))
