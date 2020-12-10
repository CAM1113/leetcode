# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 动态规划
# 使用二维数组dp[i][j]表示str[i:j]是否是回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        ans = ''
        # 枚举子串的长度 l+1
        for l in range(len(s)):
            # 子串的起始位置
            for start in range(len(s)):
                end = start + l
                if end >= len(s):
                    # start + l > len(s),已经没有符合要求的子串了
                    break
                if l == 0:
                    dp[start][end] = True
                elif l == 1:
                    dp[start][end] = s[start] == s[end]
                else :
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]

                if dp[start][end] and l + 1 > len(ans):
                    ans = s[start:end + 1]  # end + 1 是因为切片
        return ans


def main():
    s = "cbbd"
    print(Solution().longestPalindrome(s))


if __name__ == '__main__':
    main()
