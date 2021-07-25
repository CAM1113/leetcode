from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sums = 0
        cnt = 0
        for c in costs:
            sums += c
            if sums > coins:
                return cnt
            cnt += 1
        return cnt