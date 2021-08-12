# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         length = len(s)
#         dp = [[1 for _ in range(length)] for _ in range(length)]
#         for j in range(length):
#             for i in range(j, -1, -1):
#                 if s[i] != s[j]:
#                     dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
#                     continue
#                 if i == j:
#                     continue
#                 if i == j - 1:
#                     dp[i][j] = 2
#                     continue
#                 dp[i][j] = dp[i + 1][j - 1] + 2
#         return dp[0][length - 1]

# 第二次做，感觉第一次的代码看不懂了
# 序列由小到大，先判断小序列的最长回文子序列
# 然后较大序列两端相等，就在小序列的长度上+2
# 不相等，是小序列中的较大值
# dp + 滑动窗口
# dp[i][j] 表示：起始点为i，长度为j的子序列的最大回文子序列
# dp表是按列一次填充的
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[1 for _ in range(len(s) + 1)] for _ in s]
        sub_len = 2  # 子序列的长度从2开始递增,因为长度为1的子序列必然是回文的
        while sub_len <= length:
            for start in range(length - sub_len + 1):
                # 开始节点是start，结束节点是 start+ sub_len - 1
                if s[start] == s[start + sub_len - 1]:
                    if sub_len == 2:
                        dp[start][sub_len] = 2
                    else:
                        dp[start][sub_len] = dp[start + 1][sub_len - 2] + 2
                else:
                    if sub_len == 2:
                        continue
                    else:
                        dp[start][sub_len] = max(dp[start][sub_len - 1],
                                                 dp[start + 1][sub_len - 1])
            sub_len += 1
        return dp[0][length]


if __name__ == '__main__':
    s = "bbbab"
    print(Solution().longestPalindromeSubseq(s))
