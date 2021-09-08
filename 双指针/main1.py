import collections
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = collections.defaultdict(list)
        index = 0
        for n in nums:
            num_index[n].append(index)
            index += 1
        for n in num_index.keys():
            n1 = target - n
            if n1 == n:
                if len(num_index[n]) > 1:
                    return [num_index[n][0], num_index[n][1]]
            else:
                if n1 in num_index.keys():
                    return [num_index[n][0], num_index[n1][0]]


if __name__ == '__main__':
    x = [3, 2, 4]
    print(Solution().twoSum(x, 6))
