import math
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        nums = 0
        for i in coins:
            nums += math.ceil(i / 2.0)
        return nums
