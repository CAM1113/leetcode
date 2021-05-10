import collections
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sums = 0
        pro_sums_dict = collections.defaultdict(list)
        pro_sums_dict[0].append(0)
        max_len = 0
        for index, n in enumerate(nums):
            sums += n
            pro_sums_dict[sums].append(index + 1)
            l1 = pro_sums_dict[sums][-1]
            if sums - k not in pro_sums_dict.keys():
                continue
            l2 = pro_sums_dict[sums - k][0]
            if l1 - l2 > max_len:
                max_len = l1 - l2
        return max_len


def main():
    nums = [-5, 8, 2, -1, 6, -3, 7, 1, 8, -2, 7]
    k = -4
    print(Solution().maxSubArrayLen(nums, k))


if __name__ == '__main__':
    main()
