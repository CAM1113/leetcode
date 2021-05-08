import collections
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt_dict = collections.defaultdict(int)
        for n in nums:
            cnt_dict[n] += 1
        sums = 0
        for k in cnt_dict.keys():
            if cnt_dict[k] == 1:
                sums += k
        return sums