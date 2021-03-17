class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1]
        for i in range(n - 1):
            dp2 = [0] * 5
            for i in range(5):
                for j in range(i + 1):
                    dp2[i] += dp[j]
            dp = dp2
        return sum(dp)


if __name__ == '__main__':
    n = 33
    print(Solution().countVowelStrings(n))
