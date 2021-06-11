# 背包问题
class Solution:
    def numSquares(self, n: int) -> int:
        square_num = []
        index = 1
        while index <= n:
            sq = index ** 2
            if sq <= n:
                square_num.append(sq)
            else:
                break
            index += 1
        dp = [10000 for _ in range(n + 1)]
        dp[0] = 1
        for num in square_num:
            dp[num] = 1
        for num in square_num:
            for i in range(num, len(dp)):
                dp[i] = min(1 + dp[i - num], dp[i])
        return dp[-1]


if __name__ == '__main__':
    x = 1
    print(Solution().numSquares(x))
