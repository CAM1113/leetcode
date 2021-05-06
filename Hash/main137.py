import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = collections.defaultdict(int)
        for c in nums:
            cnt_dict[c] += 1
        for c in cnt_dict.keys():
            if cnt_dict[c] == 1:
                return c

