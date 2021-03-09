# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 动态规划
# 使用二维数组dp[i][j]表示str[i:j]是否是回文子串


# 中心扩散法
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        max_start = 0
        max_end = 0
        for i in range(n):
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if 2 > max_len:
                    max_len = 2
                    max_start = i
                    max_end = i + 1
            for j in range(0, n):
                if j == 0:
                    dp[i][i + j] = True
                    continue

                if i - j < 0 or i + j >= n:
                    break
                mark = False
                if (i - j >= 0 and i + j < n) and dp[i - j + 1][i + j - 1] == True and s[i - j] == s[i + j]:
                    dp[i - j][i + j] = True
                    mark = True
                    if j * 2 + 1 > max_len:
                        max_len = 2 * j + 1
                        max_start = i - j
                        max_end = i + j

                if (i - j >= 0 and i + 1 + j < n) and dp[i - j + 1][i + j] == True and s[i - j] == s[i + j + 1]:
                    dp[i - j][i + j + 1] = True
                    mark = True
                    if 2 * j + 2 > max_len:
                        max_len = 2 * j + 2
                        max_start = i - j
                        max_end = i + j + 1
                if not mark:
                    break

        return s[max_start:max_end + 1]


# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        max_start = 0
        max_end = 0
        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j-i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_start = i
                    max_end = j

        return s[max_start:max_end + 1]


def main():
    s = "cbbdbba"
    print(Solution().longestPalindrome(s))


if __name__ == '__main__':
    main()
