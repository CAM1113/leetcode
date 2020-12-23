# 动态规划
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。

# 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        min_val = prices[0]
        profit_list = [0 for _ in prices]
        for index in range(1, len(prices)):
            profit_list[index] = max(prices[index] - min_val, profit_list[index - 1])
            if min_val > prices[index]:
                min_val = prices[index]
        return profit_list[-1]


if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(p))
