import collections
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        return False
        cnt = collections.defaultdict(int)
        for n in nums:
            cnt[n] += 1
