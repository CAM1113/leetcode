from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        array = [[0, 0] for _ in range(len(prices))]
        array[0][0] = 0
        array[0][1] = -prices[0]
        for i in range(1, len(prices)):
            array[i][0] = max(array[i-1][0],array[i-1][1]+prices[i])
            array[i][1] = max(array[i-1][1],array[i-1][0]-prices[i])
        return array[-1][0]
