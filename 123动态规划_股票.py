# 股票买卖，动态规划
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n < 1:
            return 0
        k = 3

        # dp[n,k,2]表示在第n天交易了第k次所能获得的最大收益，最后的2表示在第n天持有股票的收益和不持有股票的收益
        dp = [[[0, 0] for _ in range(k)] for _ in range(n)]
        for i in range(3):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]
        for day in range(1,n):
            for times in range(k):
                if times < 1:
                    dp[day][times][0] = 0
                    dp[day][times][1] = max(dp[day-1][times][1], - prices[day])
                    continue
                dp[day][times][0] = max(dp[day-1][times][0],dp[day-1][times-1][1] + prices[day])
                dp[day][times][1] = max(dp[day-1][times][1],dp[day-1][times][0] - prices[day])
        max_val = 0
        for i in range(k):
            if dp[n-1][i][0] > max_val:
                max_val = dp[n-1][i][0]
        return max_val




if __name__ == '__main__':
    p = [1,2,3,4,5]
    print(Solution().maxProfit(p))
