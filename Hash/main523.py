import collections
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_hash = collections.defaultdict(int)
        mod_hash[0] = -1
        sums = 0
        for index, n in enumerate(nums):
            sums += n
            mod = sums % k
            if mod in mod_hash.keys():
                if index - mod_hash[mod] >= 2:
                    return True
            else:
                mod_hash[mod] = index
        return False


if __name__ == '__main__':
    x =  [23,2,6,4,7]
    k = 25
    print(Solution().checkSubarraySum(x, k))
